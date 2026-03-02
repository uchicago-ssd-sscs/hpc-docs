# Jupyter via VSCode Guide

This guide demonstrates how to run **Jupyter notebooks** on a **compute node** via Slurm while **editing them locally in VSCode**.

??? note "Who is this guide for?"

    - Users familiar with logging into the cluster and submitting jobs via Slurm
    - Users who want to use VSCode as their development environment with remote Jupyter support

??? note "Prerequisites"

    - Cluster access (VPN + login node)
    - VSCode installed locally with `Remote - SSH` and `Jupyter` extensions
    - Basic familiarity with Slurm and Linux command line

## Batch Job with Jupyter on Compute Node via VSCode

### Step 0: (optional) Install `ipykernel` for your environment

If you have multiple environments, installing its python kernel for Jupyter will allow switching between them without restarting the Jupyter server.

```bash
# Load your environment (venv, conda, etc.)
$ module load miniconda
$ conda activate <my_conda_env>

# Install `ipykernel`
$ conda install ipykernel

# Create python backend/kernel
$ python -m ipykernel install \
         --user \
         --name=<NAME> \
         --display-name=<DISPLAY NAME>
```

### Step 1: Connect to the login node with VSCode

With the `Remote - SSH` extension installed, select the `Remote-SSH: Connect to Host...` option from the command palette and connect to `[CNETID]@sscs-cronus2.ssd.uchicago.edu`. When prompted enter your CNETID password.

### Step 2: Install `Jupyter` extension for VSCode

Make sure you are connected to the login node and install the `Jupyter` extension. Note the connection info in the lower left corner of the VSCode window and whether the extension is being installed in the local or remote VSCode instance.

### Step 3: Prepare a slurm batch script to launch Jupyter

```bash hl_lines="24-25 32-37"
#!/usr/bin/env bash

# jupyter_example.sbatch

#SBATCH --job-name=jupyter
#SBATCH --output=./logs/%j/stdout.log  # %j = $SLURM_JOB_ID
#SBATCH --error=./logs/%j/stderr.log

#SBATCH --time=00-01:00:00 # DD-HH:MM:SS
#SBATCH --partition=cpu
#SBATCH --qos=normal

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=36
#SBATCH --threads-per-core=1
#SBATCH --mem=240G

# Environment setup
module purge
module load miniconda
conda activate <my_conda_env>

# Node connection info
JUPYTER_IP=$(ip route get 1.1.1.1 | awk '{print $7; exit}')
JUPYTER_PORT=$(shuf -i 49152-65535 -n 1)

# Logs directory
LOGS_DIR="${SLURM_SUBMIT_DIR}/logs/${SLURM_JOB_ID}"

# Launch Jupyter
JUPYTER_LOG="${LOGS_DIR}/jupyter.log"
jupyter lab \
        --no-browser \
        --ip=$JUPYTER_IP \
        --port=$JUPYTER_PORT \
        --preferred-dir="/home/$USER" \
        --notebook-dir="/home/$USER" >"$JUPYTER_LOG" 2>&1 &

# Keep batch job alive
wait
```

### Step 4: Submit the batch job and check job status:

```bash
# Submit job to slurm
$ sbatch ./jupyter_example.sbatch

# Check job status, id, etc.
$ squeue -u $USER
```

### Step 5: Get connection URL for Jupyter

Obtain the connection URL for the running Jupyter server on the compute node. The batch script above redirects the Jupyter server's logs to `logs/${SLURM_JOB_ID}/jupyter.log`. Copy the URL which <u>**DOES NOT**</u> include `127.0.0.1`:

```bash hl_lines="12"
# logs/${SLURM_JOB_ID}/jupyter.log

...

[I 2026-01-16 07:08:09.836 ServerApp] Jupyter Server 2.17.0 is running at:
[I 2026-01-16 07:08:09.836 ServerApp] http://172.29.0.1:50127/lab?token=52de9402aadc1a552cfa3eb75cea7e058c99a96ecca64428
[I 2026-01-16 07:08:09.836 ServerApp]     http://127.0.0.1:50127/lab?token=52de9402aadc1a552cfa3eb75cea7e058c99a96ecca64428
[I 2026-01-16 07:08:09.836 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2026-01-16 07:08:09.857 ServerApp]

    Or copy and paste one of these URLs:
        http://172.29.0.1:50127/lab?token=52de9402aadc1a552cfa3eb75cea7e058c99a96ecca64428
        http://127.0.0.1:50127/lab?token=52de9402aadc1a552cfa3eb75cea7e058c99a96ecca64428

...
```

### Step 6: Change the notebook's python kernel

In VSCode, press the `Select Kernel` button in the top right of the notebook window and use the `Existing Jupyter Server...` option to enter the URL of the Jupyter server from above to connect to the Jupyter server on the compute node. Proceed to name the connection and select the Python kernel you wish to use.

### Step 7: Tests / confirmation

Run some quick tests to make sure notebook execution occurs on the compute node and not the login node:

```python
import os
import socket
print(f"Hostname: {socket.gethostname()}")
print(f"Submit Host: {os.environ['SLURM_SUBMIT_HOST']}")
print(f"Job ID: {os.environ['SLURM_JOB_ID']}")

# E.g.
> Hostname: sn1
> Submit Host: cronus
> Job ID: 1234
```

### Step 8: Cancel job when finished

When you are doing working, cancel your batch job:

```bash
# Run `squeue` to determine the id of the job running your jupyter server
$ squeue -u $USER
> JOBID PARTITION NAME  USER ST     TIME NODES NODELIST
> 1234        cpu bash $USER  R HH:MM:SS     1 sn1

# Cancel your job
$ scancel -j 1234
```