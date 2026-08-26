# Mapping Storage Shares

Users can access storage shares from a personal computer using SMB (also known as Windows File Sharing).

If you are accessing storage from **off campus**, connect to the [UChicago VPN](https://cvpn.uchicago.edu/) first.

## Storage Locations

Use the following hostname when connecting to a storage location:

- **Home directory:** `ssdhomedirs.uchicago.edu`
- **Cronus & Athens shares:** `ssdfiles.uchicago.edu`
- **Acropolis shares:** `ssdacropolisshares.uchicago.edu`

See [Storage Locations](storage-locations.md) for more information about these storage locations and their corresponding paths.

## Home Directory

Your home directory is available on the cluster at `/home/<your_cnet_id>`.

To connect to your home directory from a personal computer:

### Windows

1. Open **File Explorer**.
2. In the address bar, enter `\\ssdhomedirs.uchicago.edu\<your_cnet_id>`.
3. Press **Enter**.
4. When prompted for credentials, enter your University of Chicago CNET ID and password.
5. For your username, use the `ADLOCAL\` prefix. For example, if your CNET ID is `johnsmith`, enter `ADLOCAL\johnsmith`.
6. Enter your corresponding CNET ID password.

After successfully authenticating, you can browse and work with your home directory using `File Explorer`.

### macOS

To connect to your home directory:

1. Open **Finder**.
2. From the menu bar, select **Go → Connect to Server...**
3. In the **Server Address** field, enter `smb://ssdhomedirs.uchicago.edu/<your_cnet_id>`.
4. Click **Connect**.
5. When prompted for credentials, enter your University of Chicago CNET ID and password.
6. For your username, use the `ADLOCAL\` prefix where required. For example, if your CNET ID is `johnsmith`, enter `ADLOCAL\johnsmith`.
7. Enter your corresponding CNET ID password.

After successfully authenticating, your home directory will appear in `Finder` and can be accessed like a folder on your Mac.

!!! note "Lab and Project Shares"
    Lab and project shares can be mapped using the same process. Use the hostname and share name corresponding to the storage location you need to access. See [Storage Locations](storage-locations.md) for the appropriate SMB address.
