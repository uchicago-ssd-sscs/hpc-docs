# File Transfer with Globus

## Installing Globus Connect Personal

### Download and Setup

1. Download **Globus Connect Personal** from [globus.org/globus-connect-personal](https://www.globus.org/globus-connect-personal)
2. Follow the basic first-time setup instructions provided on the download page

---

## Transferring Files

### Starting a Transfer

There are two ways to initiate a file transfer:

=== "From Globus Connect Personal"

    1. Click the **Globus Connect Personal** icon in your menu bar/system tray
    2. Select **Web: Transfer Files**
    3. Your default browser will launch and prompt you to log in to globus.org

=== "From Web UI"

    1. Navigate to [globus.org](https://globus.org) and log in
    2. Go to the **File Manager** tab
    3. Select **Transfer or Sync data from one collection to another** (two diagonal arrows slanting from lower-right to upper-left)

### Setting Up the Transfer

Once logged in, the web UI will display your local collection in the File Manager.

#### Source Collection (Left Panel)

4. Your local collection should appear in the left panel
5. Navigate to the file(s) or directory you want to transfer
6. **Select items** by checking the box to the left of the file or directory name

??? tip "Selecting Multiple Items"
    You can select multiple files or folders by checking multiple boxes. This allows you to transfer several items in a single operation.

#### Destination Collection (Right Panel)

7. In the right panel's **Collection** search bar, enter `UChicago SSD Shares`
8. Your home directory should appear
9. Navigate to your desired destination folder

!!! tip "Quick Path Entry"
    Instead of navigating through folders, you can type the full path directly in the **Path** bar.  
    Example: `/home/jlodder/Downloads`

### Executing the Transfer

10. Click **Start** above the file listing in the left panel to initiate the transfer
11. A green notification box will appear with the message **"Transfer request submitted successfully"** and a **View details** link.

### Monitoring Transfer Progress

12. Click **View details** to monitor the transfer in real-time
13. You will receive an **email notification** with transfer details upon completion

!!! info "Viewing Transferred Files"
    Click **refresh list** (↻) above the right panel to see your transferred files immediately after completion.

---

## Transfer Direction Reference

| Transfer Type | Left Panel (Source) | Right Panel (Destination) |
|---------------|---------------------|---------------------------|
| **Upload to UChicago** | Your local collection | UChicago SSD Shares |
| **Download from UChicago** | UChicago SSD Shares | Your local collection |
| **Between remote locations** | Any collection | Any collection |

---

## Troubleshooting

!!! warning "Common Issues"
    **Collection not appearing?**
    
    - Ensure Globus Connect Personal is running (check menu bar/system tray)
    - Verify you've completed the initial collection setup
    - Try refreshing the File Manager page
    
    **Transfer stuck or failed?**
    
    - Check the transfer details page for error messages
    - Verify you have write permissions to the destination
    - Ensure both endpoints are online and accessible

---

## Additional Resources

!!! question "Need Help?"
    - [Globus Connect Personal Documentation](https://docs.globus.org/globus-connect-personal/)
    - [Transfer Files Guide](https://docs.globus.org/how-to/get-started/)
    - UChicago IT Support for access issues