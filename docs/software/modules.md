# Softare Environment & Modules

The 6045 cluster uses TCL modules. For testing, learning, or light interactive work, you can load modules directly on the login node. 

## Module Commands

| Command     | Description                          |
| ----------- | ------------------------------------ |
| `module avail`       | List all available software modules  |
| `module load <module>`       | Load software into your environment |
| `module list`    | List loaded modules |
| `module purge`   | Unload all modules |

!!! info
    
    - You can load modules directly on the login node for testing purposes.
    - Load modules within your sbatch scripts for submitted jobs (recommended best practice).

## Available Modules

The following modules are currently available on the cluster:

<!-- MODULES_START -->

**Last updated**: April 20, 2026 at 05:54 UTC

| Module | Version(s) | &nbsp; | Module | Version(s) |
|--------|------------|:------:|--------|------------|
| `boost` | `1.90.0` | | `matlab` | `R2023b` |
| `cmake` | `3.31.9` | | `miniconda` | `25.9.1` |
| `cuda` | `11.8.0`<br>`12.8.1` | | `mkl` | `2025.3` |
| `fsl` | `6.0.7.21` | | `netcdf` | `4.9.3` |
| `gcc` | `14.0` | | `nvhpc` | `25.3` |
| `gdal` | `3.12.0` | | `ollama` | `0.13.0`<br>`0.13.5` |
| `geos` | `3.14.1` | | `openblas` | `0.3.30-openmp` |
| `go` | `1.26.0` | | `openjdk` | `25.0.2` |
| `hdf4` | `4.3.1` | | `openmpi` | `5.0.9` |
| `hdf5` | `1.14.6`<br>`2.0.0` | | `python` | `3.12.12`<br>`miniconda-25.9.1`<br>`miniforge-25.9.1` |
| `ipopt` | `3.14.19` | | `R` | `4.2.3`<br>`4.3.3`<br>`4.4.3`<br>`4.5.3` |
| `julia` | `1.12.5` | | `rust` | `1.93.1` |
| `knitro` | `14.2.0` | | `stata` | `19` |
| `llama.cpp` | `b7898` | |  |  |

<!-- MODULES_END -->

---

## Running a Python Script with Slurm

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

module load python/3.12.12
python3 ~/scripts/query_csv.py
```

!!! warning
    
    Load modules within your Slurm scripts, not only on the login node, to ensure consistency and reproducibility.