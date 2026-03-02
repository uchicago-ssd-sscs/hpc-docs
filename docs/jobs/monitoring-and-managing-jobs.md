# Monitoring and Managing Jobs

## SLURM Quick Reference

| Task | Command | Example |
|------|---------|---------|
| Submit batch job | [`sbatch`](./../submitting-jobs/#sbatch) | `sbatch job.sh` |
| Interactive job | [`srun`](./../submitting-jobs/#srun) | `srun --pty bash` |
| View your jobs | [`squeue -u`](./../monitoring-and-managing-jobs/#squeue-view-job-queue) | `squeue -u $USER` |
| Job details | [`scontrol show job`](./../monitoring-and-managing-jobs/#scontrol-show-job-detailed-job-information) | `scontrol show job <job-id>` |
| Cancel job | [`scancel`](./../monitoring-and-managing-jobs/#scancel-cancel-jobs) | `scancel <job-id>` |
| View partitions | [`sinfo`](./../monitoring-and-managing-jobs/#sinfo-partition-and-node-information) | `sinfo -p <partition-name>` |
| Job history | [`sacct`](./../monitoring-and-managing-jobs/#sacct-job-accounting-information) | `sacct -j <job-id>` |
| SSH to node | [`ssh`](./../monitoring-and-managing-jobs/#ssh-into-running-jobs) | `ssh <node-id>` |
| GPU monitoring | [`nvidia-smi`](./../monitoring-and-managing-jobs/#checking-gpu-usage) | `nvidia-smi` |
| Real-time stats | [`sstat`](./../monitoring-and-managing-jobs/#sstat-real-time-job-statistics) | `sstat -j <job-id>` |

## Monitoring Job Status

### **squeue** - View Job Queue

1. **View all jobs:**

    ```bash
    squeue
    ```

2. **View only your jobs:**

    ```bash
    squeue -u $USER
    ```

3. **View jobs in a specific partition:**

    ```bash
    squeue -p <partition-name>
    ```

4. **Custom output format:**

    ```bash
    squeue -u $USER -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R"
    ```

??? tip "Understanding `squeue` Output"
    - `JOBID`: Unique job identifier
    - `PARTITION`: Partition the job is running on
    - `NAME`: Job name
    - `USER`: Job owner
    - `ST`: Job state (`PD` = Pending, `R` = Running, `CG` = Completing, `CD` = Completed)
    - `TIME`: Runtime so far
    - `NODES`: Number of nodes
    - `NODELIST(REASON)`: Nodes allocated or reason for pending

### **scontrol show job** - Detailed Job Information

1. **View detailed information about a specific job:**

    ```bash
    scontrol show job <jobid>
    ```

    **Example output includes:**

    - Job state and reason
    - Resource allocation details
    - Start and end times
    - Working directory
    - Output and error file paths

### **sacct** - Job Accounting Information

1. **View completed jobs:**

    ```bash
    sacct
    ```

2. **View specific job with detailed information:**

    ```bash
    sacct -j <jobid> --format=JobID,JobName,Partition,State,Elapsed,CPUTime,MaxRSS,ExitCode
    ```

3. **View jobs from the last 7 days:**

    ```bash
    sacct -S $(date -d '7 days ago' +%Y-%m-%d)
    ```

??? info "Useful `sacct` Formats"
    Common fields to include in `--format`:
    
      - `JobID`: Job identifier
      - `JobName`: Job name
      - `State`: Final job state
      - `Elapsed`: Wall clock time
      - `CPUTime`: Total CPU time
      - `MaxRSS`: Maximum memory used
      - `ExitCode`: Job exit code

---

## Checking Available Resources

### **sinfo** - Partition and Node Information

1. **View all partitions:**

    ```bash
    sinfo
    ```

2. **View specific partition:**

    ```bash
    sinfo -p <partition-name>
    ```

3. **Detailed node information:**

    ```bash
    sinfo -N -l
    ```

4. **Custom format showing available resources:**

    ```bash
    sinfo -o "%20P %5D %14F %10m %11l %N"
    ```

??? tip "Understanding `sinfo` Output"
    - `PARTITION`: Partition name
    - `AVAIL`: Partition availability (up/down)
    - `TIMELIMIT`: Maximum job runtime for partition
    - `NODES`: Total nodes in partition
    - `STATE`: Node states (`alloc` = allocated, `idle` = available, `down` = offline, `mix` = partially allocated)
    - `NODELIST`: List of nodes

### **scontrol show partition** - Partition Details

1. **View detailed partition information:**

    ```bash
    scontrol show partition <partition-name>
    ```

### **scontrol show node** - Node Details

1. **View specific node information:**

    ```bash
    scontrol show node <nodename>
    ```

2. **View all nodes in a partition:**

    ```bash
    scontrol show node | grep -A 20 <partition-name>
    ```

---

## Managing Jobs

### **scancel** - Cancel Jobs

1. **Cancel a specific job:**

    ```bash
    scancel <jobid>
    ```

2. **Cancel all your jobs:**

    ```bash
    scancel -u $USER
    ```

3. **Cancel all your pending jobs:**

    ```bash
    scancel -u $USER -t PENDING
    ```

4. **Cancel all jobs in a specific partition:**

    ```bash
    scancel -u $USER -p <partition-name>
    ```

!!! warning "Job Cancellation"
    **Cancelled jobs cannot be recovered.** Make sure you're cancelling the correct job(s) before confirming.

### **scontrol hold/release** - Hold or Release Jobs

1. **Hold a pending job (prevent it from running):**

    ```bash
    scontrol hold <jobid>
    ```

2. **Release a held job:**

    ```bash
    scontrol release <jobid>
    ```

### **scontrol update** - Modify Job Parameters

1. **Change job time limit:**

    ```bash
    scontrol update jobid=<jobid> TimeLimit=10:00:00
    ```

!!! info "Update Limitations"
    **You can only modify certain job parameters, and only for jobs that are pending or already started. Some changes require administrator privileges.**

---

## Accessing Compute Nodes

### SSH into Running Jobs

Once your job is running, you can SSH directly to the compute node:

**1. Find your job's node:**

```bash
squeue -u $USER -o "%.18i %.9P %.20j %.10u %.2t %.10M %.6D %R"
```

**2. SSH to the node:**

```bash
ssh <nodename>
```

??? warning "SSH Access Rules"
    - You can only SSH to nodes where you have a running job
    - Access is automatically granted when your job starts
    - Access is revoked when your job ends
    - Do not run intensive commands outside your job's allocation

**Check your processes on the node:**

```bash
top -u $USER
htop -u $USER
ps aux | grep $USER
```

---

## Monitoring Resource Usage

### **sstat** - Real-time Job Statistics

1. **Monitor running job resources:**

    ```bash
    sstat -j <jobid> --format=JobID,AveCPU,MaxRSS,NTasks
    ```

2. **Continuous monitoring:**

    ```bash
    watch -n 5 "sstat -j <jobid> --format=JobID,AveCPU,MaxRSS,MaxVMSize,NTasks"
    ```

### Checking GPU Usage

1. **On the compute node (via SSH):**

    ```bash
    nvidia-smi
    ```

2. **Watch GPU usage continuously:**

    ```bash
    watch -n 1 nvidia-smi
    ```

??? tip "GPU Monitoring Tool"
    `nvidia-smi`: Shows GPU utilization, memory usage, and running processes

---

## Tips and Best Practices

!!! success "Efficient Job Management"
    1. **Use descriptive job names**: Makes it easier to identify jobs in the queue
    2. **Set appropriate time limits**: Too short = job killed, too long = longer wait in queue
    3. **Monitor test runs**: Run short test jobs to estimate resource requirements
    4. **Check queue before submitting**: Avoid submitting to busy partitions if possible
    5. **Clean up output files**: Regularly remove old log files to save space

!!! tip "Resource Estimation"
    - Use `sacct` to review completed jobs and refine resource requests
    - Request slightly more time than needed, but be reasonable
    - Monitor memory usage with `sstat` and adjust `--mem` accordingly
    - For GPU jobs, ensure your code actually utilizes the GPU

!!! warning "Common Pitfalls"
    - **Forgetting to specify partition/QoS**: Jobs may go to wrong resources
    - **Not checking job output**: Errors may go unnoticed
    - **Requesting too many resources**: Increases queue wait time
    - **Running on login node**: Always use compute nodes for intensive work

---

## Additional Resources

!!! question "Need More Help?"
    - [Slurm Official Documentation](https://slurm.schedmd.com/)
    - [Slurm Command Summary](https://slurm.schedmd.com/pdfs/summary.pdf)
    - Use `man <command>` for detailed command documentation (e.g., `man sbatch`)
    - Contact cluster support ([ssc-server-support@lists.uchicago.edu](mailto:ssc-server-support@lists.uchicago.edu)) for issues specific to your system