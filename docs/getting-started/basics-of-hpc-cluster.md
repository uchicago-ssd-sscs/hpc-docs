# Basics of HPC Cluster

An HPC (High-Performance Computing) cluster is a collection of interconnected computers (nodes) that work together to perform computationally intensive tasks. HPC clusters are designed to handle massive parallel workloads, process large datasets, and run simulations that would take days or weeks on a single machine.

## Node Architecture

HPC clusters typically consist of two main types of nodes:

### Login Nodes

Login nodes are your entry point to the cluster. When you SSH into the cluster, you land on a login node.

???info "What login nodes are for?"
    - Connecting to the cluster via SSH (see [Accessing Cluster](accessing-the-cluster.md))
    - Editing code and scripts
    - Submitting jobs to the scheduler (see [Submitting Jobs](./../jobs/submitting-jobs.md))
    - File management (moving, copying small files)
    - Compiling code
    - Managing your job queue

???warning "What NOT to do on login nodes!"
    - Run computationally intensive programs
    - Train machine learning models
    - Process large datasets
    - Perform any task that consumes significant CPU/memory

Login nodes are shared among all users. Running heavy computations here degrades performance for everyone and may result in your processes being terminated by system administrators.

### Compute Nodes

Compute nodes are where the actual work happens. These are the powerful machines equipped with high-core CPUs, large memory, and specialized hardware like GPUs (L40S, H100).

???info "Key characteristics"
    - Dedicated to running submitted jobs
    - Not directly accessible via SSH (you must go through the scheduler)
    - Equipped with high-performance processors and accelerators
    - Isolated from other users' jobs for fair resource allocation


> For details on available partitions, node types, and resource limits, see [Cluster Partitions](./../hardware/cluster-partitions.md).