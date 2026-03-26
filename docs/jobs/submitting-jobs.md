# Submitting Jobs

A job is an allocation of resources such as compute nodes assigned to a user for an amount of time. Jobs can be interactive or batch (e.g., a script) scheduled for later execution.

### sbatch

`sbatch` is used to submit a job script for later execution. When you submit the job, Slurm responds with the job's ID, which will be used to identify this job in reports from Slurm.

```bash
$ sbatch first-job.sh
Submitted batch job 946393
```

!!! note "Recommended Submission Method"
    We recommend using `sbatch` for submitting jobs on the SSCS cluster. Batch jobs allow for better resource utilization and do not require an active terminal session. However, interactive jobs via `srun` are also supported for testing and debugging purposes.

### srun

`srun` is used to submit a job for execution or initiate job steps in real time. A job can contain multiple job steps executing sequentially or in parallel on independent or shared resources within the job's node allocation. This command is typically executed within a script which is submitted with sbatch or from an interactive prompt on a compute node.

```bash
srun <cli-options> --pty /bin/bash
```

!!!info
    For `<cli-options>`, see [Command Line Options](cli-options.md).