# Conda Environment

## Overview

**Conda** is an open-source package and environment management system that runs on Linux, macOS, and Windows. It helps you:

- Install, run, and update packages and their dependencies
- Create isolated environments with different Python versions and packages
- Manage complex software stacks without conflicts
- Easily share reproducible computing environments

## Why Use Conda on the Cluster?

Using Conda on the cluster provides several advantages:

- **Isolation**: Keep project dependencies separate without affecting other users or system packages
- **Reproducibility**: Share exact environment specifications with collaborators
- **Flexibility**: Install specific package versions without administrator privileges
- **Consistency**: Ensure your code runs the same way across different systems

---

## Getting Started with Conda

### Loading Conda Module

Before using Conda, load the module:

```bash
module load anaconda3
```

!!! tip "Add to Your Profile"
    To automatically load Conda when you log in, add the module load command to your `~/.bashrc`:
    ```bash
    echo "module load anaconda3" >> ~/.bashrc
    ```

### Verifying Installation

Check that Conda is available:

```bash
conda --version
```

---

## Working with Environments

### Creating an Environment

1. **Create an environment with a specific Python version:**

    ```bash
    conda create -n myenv python=3.11
    ```

2. **Create an environment with specific packages:**

    ```bash
    conda create -n ml_project python=3.11 numpy pandas scikit-learn
    ```

3. **Create an environment from a YAML file:**

    ```bash
    conda env create -f environment.yml
    ```

    ??? example "Example environment.yml"
        ```yaml
        name: my_research
        channels:
          - conda-forge
          - defaults
        dependencies:
          - python=3.11
          - numpy=1.24
          - pandas=2.0
          - matplotlib=3.7
          - scikit-learn=1.3
          - pip
          - pip:
            - some-pip-only-package
        ```

### Activating an Environment

```bash
conda activate myenv
```

??? success "Active Environment"
    When an environment is active, your prompt will change to show `(myenv)` at the beginning, indicating you're working in that environment.

### Deactivating an Environment

```bash
conda deactivate
```

### Listing Environments

1. **View all your environments:**

    ```bash
    conda env list
    ```

    or

    ```bash
    conda info --envs
    ```

---

## Managing Packages

### Installing Packages

1. **Install a single package:**

    ```bash
    conda install numpy
    ```

2. **Install multiple packages:**

    ```bash
    conda install numpy pandas matplotlib
    ```

3. **Install from a specific channel:**

    ```bash
    conda install -c conda-forge pytorch
    ```

4. **Install a specific version:**

    ```bash
    conda install numpy=1.24.3
    ```

??? tip "Conda Channels"
    Channels are repositories where Conda looks for packages. Common channels include:
    
    - `defaults`: Anaconda's main channel
    - `conda-forge`: Community-maintained packages
    - `bioconda`: Bioinformatics packages

### Updating Packages

1. **Update a specific package:**

    ```bash
    conda update numpy
    ```

2. **Update all packages in current environment:**

    ```bash
    conda update --all
    ```

### Removing Packages

```bash
conda remove numpy
```

### Listing Installed Packages

1. **In current environment:**

    ```bash
    conda list
    ```

2. **Search for a specific package:**

    ```bash
    conda list numpy
    ```

---

## Using Conda in Job Scripts

### Example SLURM Script with Conda

```bash hl_lines="12-13 15-16 21-22"
#!/bin/bash
#SBATCH --job-name=conda_job
#SBATCH --partition=<partition-name>
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=output_%j.log

# Load Conda module
module load anaconda3

# Activate your environment
conda activate myenv

# Run your Python script
python my_analysis.py

# Deactivate environment (optional, job ends anyway)
conda deactivate
```

??? warning "Important: Conda Initialization"
    If you encounter issues activating Conda in job scripts, you may need to initialize Conda first:
    ```bash
    source $(conda info --base)/etc/profile.d/conda.sh
    conda activate myenv
    ```

---

## Complete Workflow Example

### Setting Up a Machine Learning Project

**1. Create and activate a new environment:**

```bash
module load anaconda3
conda create -n ml_project python=3.11
conda activate ml_project
```

**2. Install required packages:**

```bash
conda install numpy pandas scikit-learn matplotlib jupyter
conda install -c conda-forge pytorch torchvision
```

**3. Verify installation:**

```bash
python -c "import torch; print(torch.__version__)"
python -c "import sklearn; print(sklearn.__version__)"
```

**4. Export environment for reproducibility:**

```bash
conda env export > environment.yml
```

**5. Create a job script (train_model.sh):**

```bash hl_lines="11-12 16"
#!/bin/bash
#SBATCH --job-name=ml_training
#SBATCH --partition=<partition-name>
#SBATCH --qos=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --output=training_%j.log

module load anaconda3
conda activate ml_project

python train_model.py --epochs 100 --batch-size 64

conda deactivate
```

**6. Submit the job:**

```bash
sbatch train_model.sh
```

---

## Sharing Environments

### Export Environment

1. **Export exact package versions:**

    ```bash
    conda env export > environment.yml
    ```

2. **Export without build information (more portable):**

    ```bash
    conda env export --no-builds > environment.yml
    ```

3. **Export only explicitly installed packages:**

    ```bash
    conda env export --from-history > environment.yml
    ```

### Recreate Environment from Export

On another system or for another user:

```bash
conda env create -f environment.yml
```

??? tip "Reproducibility Best Practice"
    Always include an `environment.yml` file in your project repository. This allows others to recreate your exact environment, ensuring reproducible results.

---

## Environment Management

### Removing an Environment

```bash
conda env remove -n myenv
```

### Cloning an Environment

```bash
conda create --name myenv_copy --clone myenv
```

### Cleaning Up

1. **Remove unused packages and caches:**

    ```bash
    conda clean --all
    ```

!!! info "Disk Space"
    **Conda can consume significant disk space over time.** Regular cleaning helps manage your quota on the cluster.

---

## Best Practices

!!! success "Conda Best Practices on Clusters"
    1. **Use descriptive environment names**: `ml_project_v2` instead of `test`
    2. **Create project-specific environments**: Avoid installing everything in the base environment
    3. **Pin important package versions**: Specify versions in environment.yml for reproducibility
    4. **Export environments regularly**: Keep environment.yml updated in version control
    5. **Clean up unused environments**: Remove old environments to save disk space
    6. **Test environments before large jobs**: Verify package installations work as expected
    7. **Document your environment**: Include a README with setup instructions

!!! warning "Common Pitfalls"
    - **Don't modify the base environment**: Always create new environments for your projects
    - **Avoid mixing pip and conda**: When possible, install packages via Conda; use pip only for packages not available in Conda
    - **Watch your disk quota**: Conda environments can be large; monitor your usage
    - **Don't activate multiple environments**: Deactivate one before activating another

---

## Troubleshooting

### Environment Activation Issues

If `conda activate` doesn't work:

```bash
# Initialize Conda for your shell
conda init bash

# Or source Conda manually
source $(conda info --base)/etc/profile.d/conda.sh
```

### Package Conflicts

If you encounter dependency conflicts:

```bash
# Create a fresh environment
conda create -n new_env python=3.11

# Install packages one at a time to identify conflicts
conda activate new_env
conda install package1
conda install package2
```

### Slow Package Installation

```bash
# Use mamba, a faster Conda alternative
conda install -c conda-forge mamba

# Then use mamba instead of conda
mamba install numpy pandas
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Create environment | `conda create -n myenv python=3.11` |
| Activate environment | `conda activate myenv` |
| Deactivate environment | `conda deactivate` |
| List environments | `conda env list` |
| Install package | `conda install package_name` |
| Update package | `conda update package_name` |
| Remove package | `conda remove package_name` |
| List packages | `conda list` |
| Export environment | `conda env export > environment.yml` |
| Create from YAML | `conda env create -f environment.yml` |
| Remove environment | `conda env remove -n myenv` |
| Clean cache | `conda clean --all` |

---

## Additional Resources

!!! question "Learn More"
    - [Official Conda Documentation](https://docs.conda.io/)
    - [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
    - [Managing Environments Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
    - [Conda-Forge Channel](https://conda-forge.org/)
    - [Bioconda (for bioinformatics)](https://bioconda.github.io/)

!!! info "Getting Help"
    - Run `conda --help` for command overview
    - Run `conda <command> --help` for specific command help (e.g., `conda install --help`)
    - Check cluster-specific documentation for local Conda configurations
    - Contact cluster support for installation issues