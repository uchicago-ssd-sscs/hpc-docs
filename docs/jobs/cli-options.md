# Command Line Options

The below table lists some commonly used `sbatch`/`srun` options as well as their meaning. All the listed options can be used with the `sbatch` command (either on the command line or as directives within a script). Many are also commonly used with `srun` within a script or interactive job.

| Option <br>(long form) | Option <br>(short form) | Meaning | sbatch | srun |
| :----------------- | :------------------ | :------ | :------------: | :---: |
| `--time` | `-t` | maximum walltime | :material-check: | :material-close: |
| `--time-min` | (none) | minimum walltime | :material-check: | :material-close: |
| `--nodes` | `-N` | number of nodes | :material-check: | :material-check: |
| `--ntasks` | `-n` | number of MPI tasks | :material-check: | :material-check: |
| `--cpus-per-task` | `-c` | number of processors per MPI task | :material-check: | :material-check: |
| `--gpus` | `-G` | total number of GPUs | :material-check: | :material-check: |
| `--gpus-per-node` | (none) | number of GPUs per node | :material-check: | :material-check: |
| `--gpus-per-task` | (none) | number of GPUs per MPI task | :material-check: | :material-check: |
| `--constraint` | `-C` | constraint (e.g., type of resource) | :material-check: | :material-close: |
| `--qos` | `-q` | quality of service (QOS) | :material-check: | :material-close: |
| `--account` | `-A` | project to charge for this job | :material-check: | :material-close: |
| `--licenses` | `-L` | licenses (filesystem required for job) | :material-check: | :material-close: |
| `--job-name` | `-J` | name of job | :material-check: | :material-close: |

!!! info 
    Long and short forms are interchangeable but differ in format. Long form uses double hyphens with an equals sign (e.g., `--time=10:00:00`), while short form uses a single hyphen with a space (e.g., `-t 10:00:00`). **We recommend using long form in scripts for clarity and readability**.