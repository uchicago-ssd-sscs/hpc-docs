# Storage Locations

The Social Sciences Division (SSD) provides network storage for **user home directories** and **shared lab and project data**. These storage locations are available from the HPC cluster environment and can also be accessed from personal computers using SMB (also known as Windows File Sharing).

If you are accessing storage from **off campus**, connect to the [UChicago VPN](https://cvpn.uchicago.edu/) first.

## Storage Overview

The following table summarizes the storage locations available to cluster users:

| Storage | HPC path | macOS | Windows |
|---|---|---|---|
| **Home directory** | `/home/<your_cnet_id>` | `smb://ssdhomedirs.uchicago.edu/<your_cnet_id>` | `\\ssdhomedirs.uchicago.edu\<your_cnet_id>` |
| **Cronus shared storage** | `/share/<sharename>` | `smb://ssdfiles.uchicago.edu/<sharename>` | `\\ssdfiles.uchicago.edu\<sharename>` |
| **Athens shared storage** | `/share/<sharename>` | `smb://ssdfiles.uchicago.edu/<sharename>` | `\\ssdfiles.uchicago.edu\<sharename>` |
| **Acropolis shared storage** | `/share/<sharename>`* | `smb://ssdacropolisshares.uchicago.edu/<sharename>` | `\\ssdacropolisshares.uchicago.edu\<sharename>` |

> **Note:** Use the Acropolis-specific storage hostname only for shares hosted on Acropolis shared storage.

## Home Directories

Your home directory is associated with your University of Chicago CNET ID and automatically mounted when you login to the cluster.

Home directories are private to individual users and are not intended for sharing files with other users.

To access your home directory from a personal computer, use the SMB address shown in the table above. See [**Mapping Storage Shares**](mapping-directions.md) for step-by-step instructions.


## Lab and Project Shares

Lab and project shares provide shared storage for research groups, labs, and projects. These shares are available from the cluster environment under `/share/<sharename>` and can also be accessed from personal computers using SMB.

Use the share name provided to you by your research group or project administrator.

For Cronus & Athens group and project shares, use:

- **macOS:** `smb://ssdfiles.uchicago.edu/<sharename>`
- **Windows:** `\\ssdfiles.uchicago.edu\<sharename>`

For Acropolis group and project shares, use:

- **macOS:** `smb://ssdacropolisshares.uchicago.edu/<sharename>`
- **Windows:** `\\ssdacropolisshares.uchicago.edu\<sharename>`

> **Legacy hostname:** `sscs-fs0.uchicago.edu` is a legacy hostname for `ssdfiles.uchicago.edu`. If you have an existing mapping or documentation that references `sscs-fs0.uchicago.edu`, you can use either the legacy hostname or `ssdfiles.uchicago.edu` for new connections.

## Connecting from a Personal Computer

SMB allows you to access files stored on the HPC storage system as though they were in a folder on your local computer. Once connected, you can browse files and directories, drag and drop files between your computer and the storage system, and open files stored on the share using software installed on your computer.

For more extensive step-by-step instructions on connecting to these locations from macOS or Windows, see [**Mapping Storage Shares**](mapping-directions.md).
