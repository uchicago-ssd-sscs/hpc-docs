# Logging in to globus.org

## Initial Login

### Accessing the Platform

1. Navigate to [globus.org](https://globus.org)
2. Click **LOG IN** in the upper right corner (door icon with arrow pointing in)

### Authentication Setup

3. You'll be directed to the credential selection page, which defaults to **CILogon**
4. Click the dropdown box under **"Use your organizational login"**
5. Type "University of Chicago" until it appears in the list, then select it
6. Click **Continue**

??? tip "Organization Selection"
    If you see text other than "**University of Chicago**" in the dropdown box, backspace to clear it first.

### UChicago Authentication

7. If not already authenticated with Okta, you'll be taken to the UChicago Okta Sign In page
8. Enter your **CNet ID** and **password**, then verify with **Duo** as usual

??? info "Permissions"
    Globus will request permissions at various points during navigation. Accept these prompts. You can manage permissions later via **Settings → Manage Your Consents**.

---

## File Manager

### Accessing Your Files

9. Globus opens to the **File Manager** tab by default
10. In the **Collection** search bar, enter `UChicago SSD` and search
11. Select **UChicago SSD Shares** from the results below

!!! note
    The collection name may change in the future. The default view shows your home directory as stored on the Isilon.

### Navigating Directories

12. Click **up one folder** to view parent directories
13. Click **up one folder** again to see the root directory. You should see both `home` and `share` folders

??? warning "Navigation Timeout Issue"
    The first time you click "up one folder," the request may timeout due to the large number of folders in `/home`. Click **Try again** repeatedly until only your home directory appears. This may take several attempts. There is currently no fix other than reducing the number of folders in `/home`.

### Accessing Lab Shares

14. Double-click **share** to view available lab shares
15. Double-click any lab share you have access to in order to view its contents

!!! tip "Quick Navigation"
    - Enter `/` in the path bar to jump to root
    - Enter `/share` to go directly to lab shares

### Download Limitations

!!! warning "HTTPS Transfer Subscription Required"
    The **Download** button on the right will be grayed out, as HTTPS transfer is a subscription-only feature.

---

## Console and Endpoint Management

### Viewing Endpoints

16. Click the **Console** tab in the left sidebar (located above Settings and below Timers)
17. Select **Endpoints** to view publicly-visible Globus endpoints
18. In the search bar:
    - Uncheck **"ADMINISTERED BY ME"**
    - Enter `UChicago SSD`
    - Click search

19. Select **UChicago SSD** from the results to view the Overview tab

### Endpoint Configuration Tabs

All properties in these tabs are configurable:

| Tab | Description |
|-----|-------------|
| **Overview** | General endpoint information and properties |
| **Components** | Configured gateways and mapped collections |
| **Storage Gateways** | Names and types of configured gateways |
| **Nodes** | Data Transfer nodes, IP addresses, and data transfer ports |
| **Collections** | All configured collections |

??? info "Configuration Details"
    Click any element to display detailed information, which can be configured as needed.

### Feature Limitations

!!! note "Subscription Features"
    - **Guest collections** have been disabled
    - Features like **MFA** and **High Assurance** require a subscription

---

## Account Management

### Managing Identities

20. Navigate to **Settings → Account** to view:
    - The identity you used to log in
    - Your primary identity (if you have linked identities)
    - Options to unlink non-primary identities using the trash can icon

---

## Logging Out

Click the **LOGOUT** tab in the lower left corner (door icon with arrow pointing out)

---

## Additional Resources

!!! question "Need Help?"
    For more information about Globus features and configuration, visit the [Globus Documentation](https://docs.globus.org).