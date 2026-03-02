# Conda Environment

Conda is an open-source package and environment management system that allows you to create isolated environments with specific Python versions and packages. On the cluster, Conda is available via the **Miniconda module**. Upon loading the module, the `base` Conda environment is automatically activated.

!!! info "Module Alias"
    The `miniconda` module is the recommended interface. Internally, it loads the **Miniforge distribution**, which is fully compatible with Miniconda and uses the conda-forge ecosystem.

## Quick Reference

| Task | Command |
|------|---------|
| Load Conda module | `module load miniconda` |
| Create environment | `conda create -n myenv python=3.11` |
| Activate environment | `conda activate myenv` |
| Deactivate environment | `conda deactivate` |
| List environments | `conda env list` |
| Install package | `conda install package_name` |
| Remove package | `conda remove package_name` |
| List packages | `conda list` |
| Remove environment | `conda env remove -n myenv` |
| Clean cache | `conda clean --all` |


## Getting Started

### Loading the Module

```bash
module load miniconda
```

!!! note "Base Environment"
    Loading the Miniconda module automatically activates the `base` Conda environment. Avoid installing packages into `base` — always create a project-specific environment instead.

### Creating and Activating an Environment

```bash
# Create a new environment
conda create -n myenv python=3.11

# Activate it
conda activate myenv

# Install packages
conda install numpy pandas scikit-learn
```

## Using Conda in SLURM Jobs

```bash hl_lines="12-14 19-20"
#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --partition=<partition-name>
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=output_%j.log

# Load Conda and activate your environment
module load miniconda
conda activate myenv

# Run your script
python my_script.py

# Deactivate your environment
conda deactivate
```

## Best Practices

- **Never install into** `base` — always create project-specific environments.
- **Clean up unused environments** to conserve disk quota — Conda environments can be large.
- **Prefer Conda over pip** where possible; use pip only for packages unavailable in Conda.

> Conda environments can consume significant disk space over time. Run `conda clean --all` periodically to remove unused packages and caches.

## Troubleshooting

#### Package Conflicts
```bash
# Create a fresh environment and install packages one at a time
conda create -n new_env python=3.11
conda activate new_env
conda install package1
conda install package2
```

### Slow Installation: 

Modern Conda includes the **libmamba solver**, which significantly improves installation speed. Enable it once, then use Conda normally:

```bash
conda config --set solver libmamba
mamba install numpy pandas
```

## Additional Resources

- [Official Conda Documentation](https://docs.conda.io/)
- [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [Conda-Forge Channel](https://conda-forge.org/)