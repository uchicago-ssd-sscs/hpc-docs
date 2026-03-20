# Transferring Data to/from the Cluster

We recommended following tools to move files between your local machine and the cluster:

1. **Globus (*preferred*)**
    
    We use Globus for reliable, high-performance data transfer to and from the cluster. It handles large datasets easily, supports automatic resume/retry, and runs without requiring an open terminal session. You can find instructions to login at [File Transfer (Globus Login)](https://wiki.ssd.uchicago.edu/en/SSCS/server/storage/Globus/User)

2. **SFTP Tools**
    
    If you prefer small transfers, consider using an SFTP (*Secure File Transfer Protocol*) application on your local device. Below are some popular examples:

    - **macOS:** FileZilla, Cyberduck
    - **Windows:** WinSCP

3. **Command Line Transfers** 

    **SCP**

    ```bash
    scp <username>@cronus.uchicago.edu:/home/<username>/path/to/file ~/local/destination/
    ```

    **RSYNC**

    ```bash
    rsync -avP <username>@cronus.uchicago.edu:/home/<username>/path/to/dir ~/local/destination/
    ```

    !!! warning
        Run these from your local device (***not on the cluster***). 