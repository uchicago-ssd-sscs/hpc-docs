# Accessing Cluster

## Secure Shell Connect

After connecting the VPN, SSH into the login node using a terminal on your personal device (Mac, Windows, Linux, etc.):

The example below is for the **login node 1** (Cronus):
```bash linenums="1"
ssh username@cronus.uchicago.edu
```
The `username` field is your CNET ID only, not your full email address.

!!! warning
    Login nodes are shared interactive systems built for file transfer, file editing and testing. **_Do not run heavy computations here_.**


## SSH Tools

- **macOS/Linux:** Terminal (built-in SSH)
- **Windows:** Command prompt, PuTTY, PowerShell, WSL, MobaXterm

!!! tip
    Outbound SSH from the cluster is not available. Use local clients to pull data to your desktop if needed.


## Graphical Access (RealVNC)

If you require a graphical desktop environment, you may connect to the login node using **VNC Viewer**.

After connecting to the cVPN:

1. Download and install **VNC Viewer** from the [RealVNC website](https://www.realvnc.com/en/connect/download/viewer/){:target="_blank"}.

2. Open **VNC Viewer**.

3. In the **RealVNC Connect** address bar, enter the login node hostname or IP address followed by the VNC port (`5999`).

    > **Example for login node 1 (Cronus):**
    
    > `cronus.uchicago.edu:5999`


4. Press **Enter**.

5. When prompted, log in using your **CNET ID username** (not your full email address) and password.

6. Accept any security or certificate prompt if displayed.

---

## Two-Factor Authentication

The cluster requires Two-Factor Authentication (2FA) via Duo for all user accounts. Ensure Duo is set up on your device prior to accessing the cluster.

!!!info "Two-Factor Authentication"
    
    To set up Two-Factor Authentication (Duo) for your account, follow the [2FA Setup Guide](https://cnet.uchicago.edu/2FA/index.htm). 
