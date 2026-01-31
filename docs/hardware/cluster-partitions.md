# Cluster Partitions

## Partitions

**Partitions** are logical divisions of a cluster's compute resources that group nodes with similar characteristics or purposes. They allow users to target specific hardware types for their workloads.

!!! example "Why Use Partitions?"
    - Submit CPU-intensive jobs to CPU nodes
    - Route GPU workloads to specialized GPU hardware
    - Ensure fair resource allocation across different workload types

---

## Cluster Overview

The 6045 cluster consists of:

- **20 compute nodes** (CPU)
- **3 GPU nodes** (specialized accelerators)
- **1 dedicated login node**

---

## Available Partitions

### CPU Partition (Default)

**Purpose**: General-purpose CPU workloads

- **Node pool**: 20 compute nodes
- **Default partition**: Jobs submitted without specifying a partition will use this
- **Best for**: Traditional computing tasks, sequential processing, memory-intensive workloads

??? tip "When to Use CPU Partition"
    Use this partition for standard computational tasks that don't require GPU acceleration, such as data processing, simulations, and general-purpose scripting.

### GPU Partition

**Purpose**: GPU-accelerated workloads (CUDA, AI/ML, deep learning, etc.)

- **2 L40s GPU nodes**: High-performance GPUs for AI/ML and visualization
- **1 H100 GPU node**: Cutting-edge GPU for the most demanding workloads

??? warning "GPU Resource Considerations"
    **GPU nodes are shared resources with limited availability**. Be mindful of runtime and only request GPU resources when your workload can effectively utilize them.

---

## QoS (Quality of Service)

**Quality of Service (QoS)** settings define priority levels, resource limits, and scheduling policies for jobs. QoS controls factors like:

- Job priority in the queue
- Maximum runtime limits
- Resource allocation constraints
- Access to specific hardware features

!!! info "QoS Impact"
    Different QoS levels can affect how quickly your job starts and how long it can run. Choose the appropriate QoS based on your workload requirements.

---

## Quality of Service (QoS) Options

### `normal` (Default)

**Purpose**: General workloads

- Standard priority
- Default QoS for all jobs unless otherwise specified
- Suitable for most computational tasks

### `gpu`

**Purpose**: GPU workloads on the GPU partition

- Optimized for GPU-accelerated jobs
- Use with the GPU partition for machine learning, CUDA applications, and GPU-intensive tasks

---

## Best Practices

!!! success "Choosing the Right Resources"
    1. **Start with defaults**: Unless you need GPUs, the default partition and QoS are appropriate
    2. **Test first**: Run small test jobs before submitting large-scale workloads
    3. **Monitor usage**: Check your job's resource utilization to ensure you're requesting appropriate resources
    4. **Be specific**: Always specify partition and QoS explicitly in your job scripts for clarity and reproducibility

!!! warning "Resource Etiquette"
    - Don't request GPU resources for CPU-only workloads
    - Release resources promptly when jobs complete
    - Use appropriate time limits to avoid blocking other users