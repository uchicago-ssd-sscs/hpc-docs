# Softare Environment & Modules

The 6045 cluster uses TCL modules. For testing, learning, or light interactive work, you can load modules directly on the login node. 

### Module Commands

| Command     | Description                          |
| ----------- | ------------------------------------ |
| `module avail`       | List all available software modules  |
| `module load <module>`       | Load software into your environment |
| `module list`    | List loaded modules |
| `module purge`   | Unload all modules |

!!! info
    
    - You can load modules directly on the login node for testing purposes.
    - Load modules within your sbatch scripts for submitted jobs (recommended best practice).

### Running a Python Script with Slurm

Here’s an example Slurm script that references a Python script (`query_csv.py`) located in your `~/scripts` directory and loads the python module:

```python hl_lines="12 13"
#!/bin/bash
#SBATCH --job-name=python_csv_job
#SBATCH --output=python_csv.out
#SBATCH --error=python_csv.err
#SBATCH --partition=cpu
#SBATCH --qos=normal
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=00:30:00

module load python
python3 ~/scripts/query_csv.py
```

!!! warning
    
    Load modules within your Slurm scripts, not only on the login node, to ensure consistency and reproducibility.