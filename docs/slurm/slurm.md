# Slurm

Introduction to the Slurm workload manager, basic commands, job submission, and monitoring.

=== "sbatch"

    ```
    !/bin/bash
    #SBATCH time=00:10:00
    SBATCH partition=gpu
    ```

=== "srun"

    ```bash 
    srun --pty /bin/bash
    ```
