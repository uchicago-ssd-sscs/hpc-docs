# Cluster Partitions

The 6045 cluster consists of 20 compute nodes, 3 GPU nodes, and a dedicated login node.

1. **CPU Partition** (*default*): For general CPU workloads

    - 20-node pool

2. **GPU Partition**: For GPU-accelerated jobs (CUDA, AI/ML, etc.)

    - 2 **L40s** GPU nodes
    - 1 **H100** GPU nodes

### QoS (Quality of Service) Options

1. **normal** (default QoS): general workloads
2. **gpu**: gpu workloads on the l40s partition