# Cluster Hardware Specifications

### Compute Nodes (CPU)

| Attribute             | Description                          |
| :-------------------- | :----------------------------------- |
| **Node Count**        |  20 nodes (**`sn[1-20]`**)           |
| **Processor**         |  Intel Xeon Platinum 8452Y           |
| **CPU Configuration** |  144 CPUs/node <br> (2 sockets × 36 cores × 2 threads)  |
| **Memory per Node**   |  515,283 MB (~503 GB)                |
| **Architecture**      |  x86_64 (     Sapphire Rapids)       |

> QOS required for Compute Nodes (CPU): `normal` (default)

### GPU Nodes

| Attribute             | Description (H100)                   | Description (L40S)                   
| :-------------------- | :----------------------------------- | :----------------------------------- 
| **Node Count**        |  1 node (**`gpu1`**)                 |  2 nodes (**`gpu[2-3]`**)            
| **Processor**         |  Intel Xeon Gold 6430                |  Intel Xeon Gold 6430                
| **CPU Configuration** |  128 CPUs/node <br> (2 sockets × 32 cores × 2 threads)  | 128 CPUs/node <br> (2 sockets × 32 cores × 2 threads)  |
| **Memory per Node**   |  1,547,488 MB (~1.48 TB)             |  773,344 MB (~755 GB)                
| **GPUs per Node**     |  2 × NVIDIA H100                     |  2 × NVIDIA L40S                     
| **GPU Memory**        |  80 GB per GPU                       |  48 GB per GPU                       
| **GPU Architecture**  |  NVIDIA Hopper                       |  NVIDIA Ada Lovelace                 
| **QoS Option**        |  `h100`                              |  `gpu`                 

!!! note "QoS Options"

    1. QOS required for L40S GPU Nodes: `gpu`

    2. QOS required for H100 GPU Nodes: `h100`

!!!info
    
    For more information, see [Quality of Service (QoS)](./../cluster-partitions/#qos-quality-of-service) Options. 
