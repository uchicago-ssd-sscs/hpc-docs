# Basics of SLURM

SLURM (Simple Linux Utility for Resource Management) is the workload manager used on most modern HPC clusters. It acts as both a scheduler and a resource manager.

Think of SLURM as an air traffic controller for computational jobs. Just as air traffic control manages which planes can take off, land, and use specific runways, SLURM manages:

1. **Resource allocation**: Which jobs get access to which compute nodes
2. **Job scheduling**: When jobs run based on priority, resource availability, and fairness
3. **Resource monitoring**: Tracking CPU, memory, and GPU usage
4. **Job lifecycle**: Starting, monitoring, and terminating jobs

## Job Submission Process

![Slurm Workflow](./../assets/images/slurm_workflow.png)


<!-- `User` → `Submit Job` → `SLURM Queue` → `Resource Check` → `Job Execution` → `Completion` -->

When you submit a job to SLURM:

1. **Job submission**: You specify resource requirements (CPUs, memory, GPUs, time limit)
2. **Queue placement**: SLURM places your job in a queue based on `partition` and `priority`
3. **Resource matching**: SLURM scans for available resources matching your requirements
4. **Allocation**: When resources become available, SLURM allocates nodes to your job
5. **Execution**: Your job runs on the allocated compute nodes
6. **Cleanup**: Upon completion, resources are released for other jobs

!!!info
    
    See [Running Jobs](./../jobs/overview.md) for more details on SLURM and Job Scheduling.