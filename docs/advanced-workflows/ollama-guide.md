# Ollama Guide

[Ollama](https://ollama.com/) is an open source platform for conveniently running large language models (LLMs) on local compute resources. To accomodate LLM workflows, the cluster is equipped with 2 GPU nodes with the following specs:

| Partition | CPUS    | RAM   | GPUS      | VRAM |
| :-------- | :------ | :---- | :-------- | :--- |
| L40S      | 64 (2x) | 755G  | L40S (2x) | 48G  |

!!! warning 

    Even though each GPU node has 755G of real memory, it is recommended to treat the effective maximum as less (e.g. ~704G) to leave room for system processes.

Running ollama on the cluster involves 2 primary steps:

1. Launching the ollama server on a compute node

2. Communicating with the server interactively via the CLI or programmatically via the API

To accommodate multiple users running ollama on the same node, ollama is containerized and ran using [apptainer](https://apptainer.org/). This allows multiple jobs to run their own independent ollama instance. To simplify the process of running ollama via apptainer, a module is provided which aliases the `ollama` command to behave like a native install while running ollama inside a container.

Running a job with ollama can be done interactively or using a batch job. Both methods are described below.

## Running Ollama: Interactive

Interactive jobs are useful for becoming more familiar with the ollama workflow, quick testing, or fine tuning ollama server configs. Below are examples steps for running an interactive ollama job:

1. First, log into the cluster and confirm your are on a login node. Then launch an interactive job (e.g. max runtime 1 hour, 1 cpu, 1 L40S gpu, and 56G RAM)
```bash
hostname
> Cronus

srun --partition=l40s --qos=gpu --time=00-01:00:00 \
     --ntasks=1 --cpus-per-task=1 --gpus=1 --mem=56G \
     --job-name=ollama_example --pty /bin/bash
```

2. After running the `srun` command, your shell should indicate you are now running on a compute node and no longer on a login node. Note your shell display should indicate a change in hostname (e.g. `cnetid@cronus` should change to `cnetid@gpu[2-3]`). This can also be confirmed using the `hostname` command:
```bash
hostname # the hostname no longer corresponds to a login node ("cronus")
> gpu2
```

3. Load the ollama module
```bash
module avail ollama       # view available ollama modules/versions
module load ollama/0.13.0 # load specific ollama version (e.g. 0.13.0)
module list               # view activate/loaded modules
```
4. Configure the ollama server (see `ollama serve --help` for config options)
```bash
# Specify ollama to run on localhost on a random port.
export OLLAMA_HOST=localhost:$(shuf -n1 -i60000-65000)

# Note: SSCS maintains a read only directory of preinstalled models on gpu nodes.
# export OLLAMA_MODELS="${SSCS_LLMS}/ollama/models"
```

5. Start the ollama server in the background
```bash
# Launch ollama server in background
ollama serve &

# Alternatively, use the following to run in background and redirect
# ollama's server output to a separate log file.
ollama serve >> "ollama_serve_${SLURM_JOB_ID}.log" 2>&1 &
```
6. Once the server is running, `ollama` commands can be ran as normal (see `ollama help`)
```bash
ollama list                  # list installed models
ollama pull [MODEL]          # install model
ollama run  [MODEL]          # start chat session
ollama run  [MODEL] [PROMPT] # run individual prompt
ollama stop [MODEL]          # unload model
ollama ps                    # list running models
```
7. Interacting with the ollama server can also be done via an API:

    * [Ollama REST API](https://docs.ollama.com/api/introduction)
    * [Ollama Python API](https://github.com/ollama/ollama-python)

    !!! note
        See [Example Python Script: Ollama Python API](./../ollama-guide/#example-python-script-ollama-python-api), for a simple usage example.

8. If any ollama server configs need to be changed, the server needs to be restarted for changes to take affect.
```bash
sleep 30 & # example/dummy background process for demonstration

jobs # list processes running in the background
[1]-  Running                 ollama serve &
[2]+  Running                 sleep 30 &

fg 1 # bring background process "1" (ollama serve) to foreground
> ollama serve

# Press Ctrl+C to stop the current foreground process

# Re-export any ollama server configs, e.g.:
export OLLAMA_MODELS="${SSCS_LLMS}/ollama/models"
export OLLAMA_CONTEXT_LENGTH=32768

# Relaunch ollama server
ollama serve &
```

## Running Ollama: Batch

Batch jobs are the recommended method of running jobs. However they require the job's workflow to be scripted as they are submitted from the login node to a compute node and ran non-interactively.

Batch jobs require writing a submission script and submitting to the scheduler from the login node:
```bash
hostname # confirm you are on a login node (Cronus)
> Cronus

sbatch [SUBMISSION SCRIPT] # submit job/script

squeue -u $USER            # view status of current jobs

     JOBID PARTITION     NAME        USER ST       TIME  NODES NODELIST(REASON)
      2074      l40s ollama_e   <cnet_id>  R       0:06      1 gpu2
```

Below is a batch script which submits a job to a compute node allocation similar to the `srun` command in the interactive example above. In addition, a simple python script to demonstrate the how to use the [ollama python API](https://github.com/ollama/ollama-python) is also provided below.

Example batch script for submitting a job to a compute node which launches an ollama server and submits prompts using a python script:

!!! note
    This example requires the ollama python package to be installed.

    Here, it is assumed a python virtual environment named **venv_ollama**
    exists in the same directory the job was submitted from and has the
    ollama python package installed. (Read the inline comments)

    The script below sets **OLLAMA_MODELS** path to the read only directory of preinstalled models on gpu nodes, maintained by SSCS.
    ```bash
    export OLLAMA_MODELS="${SSCS_LLMS}/ollama/models"
    ```
    
    If a model you need is not available, reach out to the Cluster Support team at [ssc-server-support@lists.uchicago.edu](mailto:ssc-server-support@lists.uchicago.edu) to request it be pulled in.

```bash
#!/usr/bin/env bash

#SBATCH --job-name=ollama_example
#SBATCH --output=logs/%j_%x.out   # write stdout to ${SLURM_SUBMIT_DIR}/logs/${SLURM_JOB_ID}_${SLURM_JOB_NAME}.out
#SBATCH --error=logs/%j_%x.err    # write stderr to ${SLURM_SUBMIT_DIR}/logs/${SLURM_JOB_ID}_${SLURM_JOB_NAME}.err

#SBATCH --time=00-01:00:00
#SBATCH --partition=l40s
#SBATCH --qos=gpu

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --gpus=1
#SBATCH --mem=56G

# Load required modules
module purge
module load ollama/0.13.0
module load python/3.12.12

# This example requires the ollama python package to be installed.
# Here, it is assumed a python virtual environment named "venv_ollama"
# exists in the same directory the job was submitted from and has the
# ollama python package installed.
source "${SLURM_SUBMIT_DIR}/venv_ollama/bin/activate"

# Configure ollama server
export OLLAMA_HOST="localhost:$(shuf -n1 -i60000-65000)"
export OLLAMA_MODELS="${SSCS_LLMS}/ollama/models"

# Start ollama server
OLLAMA_SERVER_LOGFILE="${SLURM_SUBMIT_DIR}/logs/${SLURM_JOB_ID}_ollama_server.log"
ollama serve >> "$OLLAMA_SERVER_LOGFILE" 2>&1 &

# Submit prompt using python script
python "${SLURM_SUBMIT_DIR}/ollama_example.py"
```

## Example python script: Ollama Python API:
```python
#!/usr/bin/env python

# ollama_example.py
# Simple ollama python api example. Output is simply printed to stdout.
# See official documentation here: https://github.com/ollama/ollama-python

import os
from ollama import Client

# Create ollama client for the ollama server running at OLLAMA_HOST
client = Client(host=os.environ["OLLAMA_HOST"])

# Generate response to a prompt
response = client.generate(model='deepseek-r1:8b', prompt="Why is the sky blue?", think=False)
print("Model: ", response["model"])
print("Response:\n", response["response"], "\n")

print("=====All response content=====")
for key, val in response:
    print(f"{key}: {val}")
```
