# Creating Your First Sbatch Script

1. Create a directory for **slurm batch** or **sbatch** scripts

    ```bash
    mkdir -p ~/scripts
    cd ~/scripts
    ```

2. Create and edit your sbatch script

    ```bash
    vi hello_world.sh
    ```

3. Example sbatch script

    ```bash
    #!/bin/bash
    #SBATCH --job-name=hello_world       # Job name
    #SBATCH --output=hello_world.out     # Standard output file
    #SBATCH --error=hello_world.err      # Standard error file
    #SBATCH --partition=cpu              # Partition to submit to
    #SBATCH --qos=normal                 # Define QoS (Quality of Service)
    #SBATCH --ntasks=1                   # Number of tasks
    #SBATCH --cpus-per-task=1            # Number of CPU cores per task
    #SBATCH --mem=1G                     # Memory per node
    #SBATCH --time=00:10:00              # Walltime (HH:MM:SS)


    # Your commands go below
    echo "Hello, Cluster!"
    ```

4. Submit slurm job

    ```bash
    sbatch hello_world.sh
    ```

5. Check job Status

    ```bash
    squeue -u <username>
    ```

6. View output

    - Standard output: `hello_world.out`
    - Standard error: `hello_world.err`

!!! info 
    For production or large jobs, always load modules inside your Slurm script using module load so that the compute nodes have the correct environment. For more details, refer to [Software Environment & Modules](software-environment-and-modules.md)