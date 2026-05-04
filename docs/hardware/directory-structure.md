# Directory Structure

This page provides an overview of the key directories on the cluster, covering their intended use, storage capacity, and availability across login and compute nodes.

## /home/<cnet_id\>

Your personal home directory, automatically assigned upon account creation. This is the default directory you land in upon logging in to the cluster. 
> 
>    cd  $HOME
> 

- **Filesystem:** NFS
- **Total Capacity:** 100G (per user)
- **Use this for:** Configuration files, scripts, and small personal files.

??? warning "Storage Limit"
    `/home` has a limited capacity shared across all users. Avoid storing large datasets or job output here.


## /scratch/<cnet_id\>

A high-capacity local disk available exclusively on compute nodes, intended for temporary storage during job execution. A personal directory under `/scratch/<cnetid>` is automatically created when you start a job. The `/scratch` directory is only accessible during an active job — you must have a running job to read or write to this space.

- **Filesystem:** Local Disk
- **Total Capacity:** 6.4T
- **Available On:** Compute nodes only
- **Use this for:** Large temporary files, job input/output, and intermediate results during job execution.

??? warning "Temporary Storage"
    `/scratch` is local to each compute node and is not shared across nodes. Copy any results you wish to keep back to `/home` or `/share` before your job ends, as data may not persist after the job completes.

??? info "Accessing `/scratch/<cnet_id>`" 
    1. Run a job via `srun` (see [Submitting Jobs](./../../jobs/submitting-jobs/#srun))
    ```bash
    srun <cli-options> --pty /bin/bash 
    cd /scratch/<cnet_id>
    ```
    2. Create a job via `sbatch` and SSH into compute node (see [Submitting Jobs](./../../jobs/submitting-jobs/#sbatch) & [SSH into running jobs](./../../jobs/monitoring-and-managing-jobs/#ssh-into-running-jobs))
    ```bash
    $ sbatch first-job.sh
    Submitted batch job 946393

    $ squeue -u $USER -o "%.18i %.9P %.20j %.10u %.2t %.10M %.6D %R"
    Get the Node name

    $ ssh <nodename>

    cd /scratch/<cnet_id>
    ```

<!-- ## /software

Houses all centrally managed software available on the cluster, maintained by the SSCS Cluster Admin team. Software is made accessible via the **Environment Modules** system.

- **Filesystem:** NFS
- **Total Capacity:** 1.0T
- **Access:** Restricted — managed by SSCS administrators.

!!! info "Loading Software"
    Users access software through the `module` command rather than directly accessing this directory. See [Environment Modules](./../../software/modules/#softare-environment-modules) for more information. -->


## /share

A large shared NFS filesystem accessible to authorized research groups, labs, and schools connected to the cluster. Access is restricted by group membership.

- **Filesystem:** NFS
- **Access:** Restricted to authorized groups.
- **Use this for:** Collaborative research data shared across labs or departments.

!!! note
    Access to `/share` is granted based on group membership. Contact [SSCS Server Support](mailto:ssc-server-support@lists.uchicago.edu) to request access for your lab or research group.

    Once access is granted, your lab’s shared directory is available at:
    ```bash
    cd /share/johndoelab
    ```
    **Permissions note** — who can read/write:

      > Only members of the `johndoelab` group have read/write access to this directory.

    This directory can also be accessed at `/mnt/share/johndoelab`.

## Filesystem Snapshots (Backup)

The cluster storage system automatically maintains filesystem snapshots to protect against accidental file deletion or corruption. Snapshots are available for the following directories:

- /home
- /share/<lab_name\>

These snapshots allow files and directories to be restored to a previous state if needed.

### Snapshot Frequency

Snapshots are created automatically at multiple intervals:

| Frequency | Purpose |
|----------|---------|
| Hourly | Recover recent accidental changes |
| Daily | Recover files deleted within the past several days |
| Monthly | Long-term recovery and archival protection |

Snapshots are managed automatically by the storage system and older snapshots are removed according to retention policies.

### Requesting File Recovery

If you need to recover a file or directory, please contact the cluster support team at [**ssc-server-support@lists.uchicago.edu**](mailto:ssc-server-support@lists.uchicago.edu), with the following information:

- Name of file or directory
- Full path to the file or directory  
- Approximate date and time when the file existed  
- Your username and lab/group (if applicable)

The support team will assist with restoring the data from available snapshots.

!!! warning
    Snapshots are not a substitute for good data management practices. Users should maintain their own backups for critical data whenever possible.

## Useful Commands

#### Check Disk Usage
```bash
# Check your home directory usage
du -sh ~

# Check a specific directory
du -sh /path/to/directory

# Check available space on a specific filesystem
df -h /home
```

#### Check File and Directory Sizes
```bash
# List files with sizes in human-readable format
ls -lh

# List top 10 largest files/directories in current directory
du -sh * | sort -rh | head -10
```

#### Navigate and Manage Files
```bash
# Check current directory
pwd

# Check who you are
whoami

# Check your group memberships
groups $USER
```