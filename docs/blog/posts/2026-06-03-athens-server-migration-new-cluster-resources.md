---
date: 2026-06-03
categories:
- Maintenance
---

# Athens Server Migration & New Cluster Resources

On Tuesday, June 9th, 2026 from 9:00 AM to 5:00 PM, SSCS will conduct a migration of the Athens server to a new compute environment, enabling access to new cluster resources including H100 and L40S GPU nodes.

<!-- more -->

This upgrade enables access to the Social Sciences Division's new cluster compute resources, including:

- **20** liquid-cooled compute nodes
- **1** Nvidia H100 node
- **2** Nvidia L40S nodes

The system will also now provide **Globus access** for data transfer.

Maintenance is expected to conclude before 5:00 PM. We will send a follow-up notification via email once maintenance is complete. If you have any questions, please reach out to us at [ssc-server-support@lists.uchicago.edu](mailto:ssc-server-support@lists.uchicago.edu).


## **Important Security Note**

After the upgrade, users will need to delete their existing Athens SSH host keys and reconnect to access Athens:

On Windows:

  1. Open `File Explorer` (`Win + E`)

  2. Show hidden files: on the top bar, click **View** > **Show** > **Hidden Items**
   
  3. Delete everything under the hidden folder `C:\Users\<username>\.ssh\known_hosts`

On MacOS:

  1. Open `Finder`
   
  2. Show hidden files: `Command + Shift + .`
   
  3. Delete everything under the hidden folder `/Users/<username>/.ssh/known_hosts`


## RealVNC Replacing EasyVNC

[RealVNC Instructions](./../../getting-started/accessing-the-cluster.md)