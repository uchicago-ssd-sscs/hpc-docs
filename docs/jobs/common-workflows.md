# Common Workflows

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
srun --partition=gpu --qos=gpu --gres=gpu:1 --time=02:00:00 --pty bash

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
sinfo -p gpu

# Check detailed node status
scontrol show partition gpu

# View current queue load
squeue -p gpu

# Submit job if resources look good
sbatch --partition=gpu --qos=gpu my_gpu_job.sh
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

---

## Quick Reference Table

| Task | Command | Example |
|------|---------|---------|
| Submit batch job | `sbatch` | `sbatch job.sh` |
| Interactive job | `srun` | `srun --pty bash` |
| View your jobs | `squeue -u` | `squeue -u $USER` |
| Job details | `scontrol show job` | `scontrol show job <job-id>` |
| Cancel job | `scancel` | `scancel <job-id>` |
| View partitions | `sinfo` | `sinfo -p <partition-name>` |
| Job history | `sacct` | `sacct -j <job-id>` |
| SSH to node | `ssh` | `ssh <node-id>` |
| GPU monitoring | `nvidia-smi` | `nvidia-smi` |
| Real-time stats | `sstat` | `sstat -j <job-id>` |