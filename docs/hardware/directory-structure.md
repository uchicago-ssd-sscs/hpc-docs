# Directory Structure

This page provides an overview of the key directories on the cluster, covering their intended use, storage capacity, and availability across login and compute nodes.

## /home/<cnet_id\>

Your personal home directory, automatically assigned upon account creation. This is the default directory you land in upon logging in to the cluster. 
> 
>    cd  $HOME
> 

- **Filesystem:** NFS
- **Total Capacity:** 100G (shared across all users)
- **Use this for:** Configuration files, scripts, and small personal files.

??? warning "Storage Limit"
    `/home` has a limited capacity shared across all users. Avoid storing large datasets or job output here.


## /scratch/<cnet_id\>

A high-capacity local disk available exclusively on compute nodes, intended for temporary storage during job execution. A personal directory under `/scratch/<cnetid>` is automatically created when you start a job.

- **Filesystem:** Local Disk
- **Total Capacity:** 6.4T
- **Available On:** Compute nodes only
- **Use this for:** Large temporary files, job input/output, and intermediate results during job execution.

??? warning "Temporary Storage"
    `/scratch` is local to each compute node and is not shared across nodes. Copy any results you wish to keep back to `/home` or `/share` before your job ends, as data may not persist after the job completes.

## /software

Houses all centrally managed software available on the cluster, maintained by the SSCS Cluster Admin team. Software is made accessible via the **Environment Modules** system.

- **Filesystem:** NFS
- **Total Capacity:** 1.0T
- **Access:** Restricted — managed by SSCS administrators.

!!! info "Loading Software"
    Users access software through the `module` command rather than directly accessing this directory. See [Environment Modules](./../../software/modules/#softare-environment-modules) for more information.


## /share

A large shared NFS filesystem accessible to authorized research groups, labs, and schools connected to the cluster. Access is restricted by group membership.

- **Filesystem:** NFS
- **Total Capacity:** 865T
- **Access:** Restricted to authorized groups.
- **Use this for:** Collaborative research data shared across labs or departments.

!!! note
    Access to `/share` is granted based on group membership. Contact [SSCS Server Support](mailto:ssc-server-support@lists.uchicago.edu) to request access for your lab or research group.


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