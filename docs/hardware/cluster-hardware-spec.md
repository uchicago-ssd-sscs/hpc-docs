# Cluster Hardware Specifications

### Compute Nodes (CPU)

| Attribute             | Description                          |
| :-------------------- | :----------------------------------- |
| **Node Count**        |  20 nodes (**`sn[1-20]`**)           |
| **Processor**         |  Intel Xeon Platinum 8452Y           |
| **CPU Configuration** |  144 CPUs/node <br> (2 sockets × 36 cores × 2 threads)  |
| **Memory per Node**   |  515,283 MB (~503 GB)                |
| **Architecture**      |  x86_64 (     Sapphire Rapids)       |

### GPU Nodes

| Attribute             | Description (L40S)                   | Description (H100)                   |
| :-------------------- | :----------------------------------- | :----------------------------------- |
| **Node Count**        |  2 nodes (**`gpu[2-3]`**)            |  1 node (**`gpu1`**)            |
| **Processor**         |  Intel Xeon Gold 6430                |  Intel Xeon Gold 6430                |
| **CPU Configuration** |  128 CPUs/node <br> (2 sockets × 32 cores × 2 threads)  |  128 CPUs/node <br> (2 sockets × 32 cores × 2 threads)  |
| **Memory per Node**   |  773,344 MB (~755 GB)                |  1,547,488 MB (~1.48 TB)             |
| **GPUs per Node**     |  2 × NVIDIA L40S                     |  2 × NVIDIA H100                     |
| **GPU Memory**        |  48 GB per GPU                       |  80 GB per GPU                       |
| **GPU Architecture**  |  NVIDIA Ada Lovelace                 |  NVIDIA Hopper                       |


