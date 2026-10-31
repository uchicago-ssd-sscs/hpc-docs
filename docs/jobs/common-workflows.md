# Common Workflows

## SLURM Quick Reference

| Task | Command | Example |
|------|---------|---------|
| Submit batch job | [`sbatch`](./submitting-jobs.md#sbatch) | `sbatch job.sh` |
| Interactive job | [`srun`](./submitting-jobs.md#srun) | `srun --pty bash` |
| View your jobs | [`squeue -u`](./monitoring-and-managing-jobs.md#squeue-view-job-queue) | `squeue -u $USER` |
| Job details | [`scontrol show job`](./monitoring-and-managing-jobs.md#scontrol-show-job-detailed-job-information) | `scontrol show job <job-id>` |
| Cancel job | [`scancel`](./monitoring-and-managing-jobs.md#scancel-cancel-jobs) | `scancel <job-id>` |
| View partitions | [`sinfo`](./monitoring-and-managing-jobs.md#sinfo-partition-and-node-information) | `sinfo -p <partition-name>` |
| Job history | [`sacct`](./monitoring-and-managing-jobs.md#sacct-job-accounting-information) | `sacct -j <job-id>` |
| SSH to node | [`ssh`](./monitoring-and-managing-jobs.md#ssh-into-running-jobs) | `ssh <node-id>` |
| GPU monitoring | [`nvidia-smi`](./monitoring-and-managing-jobs.md#checking-gpu-usage) | `nvidia-smi` |
| Real-time stats | [`sstat`](./monitoring-and-managing-jobs.md#sstat-real-time-job-statistics) | `sstat -j <job-id>` |

## Workflow 1: Submit and Monitor a Job

```bash
# Submit job
sbatch my_job.sh
# Output: Submitted batch job 12345

# Check status
squeue -j 12345

# View detailed info
scontrol show job 12345

# Monitor resources (once running)
sstat -j 12345 --format=JobID,AveCPU,MaxRSS
```

## Workflow 2: Interactive GPU Session

```bash
# Request interactive GPU node
srun --partition=<partition-name> --qos=gpu --gres=gpu:1 --time=02:00:00 --pty bash

# Once allocated, check GPU
nvidia-smi

# Run your commands
python train_model.py

# Exit when done
exit
```

## Workflow 3: Check Available Resources Before Submitting

```bash
# Check partition availability
sinfo -p <partition-name>

# Check detailed node status
scontrol show partition <partition-name>

# View current queue load
squeue -p <partition-name>

# Submit job if resources look good
sbatch --partition=<partition-name> --qos=gpu my_gpu_job.sh
```

## Workflow 4: Troubleshooting a Stuck Job

```bash
# Check job status and reason
squeue -j <jobid>

# Get detailed job information
scontrol show job <jobid>

# Check job history
sacct -j <jobid> --format=JobID,State,Reason,ExitCode

# If needed, cancel and resubmit
scancel <jobid>
```