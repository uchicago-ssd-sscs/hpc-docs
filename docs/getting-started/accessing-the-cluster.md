# Accessing Cluster

## Secure Shell Connect

After connecting the VPN, SSH into the login node using a terminal on your personal device (Mac, Windows, Linux, etc.):

The example below is for the **login node 1** (ln1):
```bash linenums="1"
ssh <username>@10.49.193.5
```
The `<username>` field is your CNET ID only, not your full email address.

!!! warning
    Login nodes are shared interactive systems built for file transfer, file editing and testing. **_Do not run heavy computations here_.**


## SSH Tools

- **macOS/Linux:** Terminal (built-in SSH)
- **Windows:** Command prompt, PuTTY, PowerShell, WSL, MobaXterm

!!! tip
    Outbound SSH from the cluster is not available. Use local clients to pull data to your desktop if needed.