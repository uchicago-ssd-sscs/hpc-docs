# Frequently Asked Questions (FAQs)

## Access

#### How do I get an account on the new SSCS Cluster?

Access to shared storage and group permissions are managed by the **SSCS Research Support Group**. Labs shares are maintained for Faculty research projects, with the goal of ensuring security and availability of materials. You can request an SSCS account for access to our compute and storage resources, [here](https://sscshelp.uchicago.edu/catalog_items/1406720-account-request/service_requests/new). 

## Software

#### How do I request a Software? 

Our group maintains access to a number of statistical and programming packages for researchers, ranging from Matlab, Stata, and R, to Python, Ollama and Conda.


!!! info "Need More Help?"

    Contact the Cluster Support team at [ssc-server-support@lists.uchicago.edu](mailto:ssc-server-support@lists.uchicago.edu)

## Jobs

#### How do I check my job status?
    
Use the [`squeue`](./../jobs/monitoring-and-managing-jobs#monitoring-job-status) command to check the status of your jobs. Each job will show a State Code indicating its current status.

??? info "Job State Codes"

    The following tables outline a variety of job state and reason codes you may encounter when using squeue to check on your jobs.

    | Status      | Code | Explanation                                                          |
    |-------------|------|----------------------------------------------------------------------|
    | COMPLETED   | `CD` | The job has completed successfully.                                  |
    | COMPLETING  | `CG` | The job is finishing but some processes are still active.            |
    | FAILED      | `F`  | The job terminated with a non-zero exit code and failed to execute.  |
    | PENDING     | `PD` | The job is waiting for resource allocation. It will eventually run.  |
    | PREEMPTED   | `PR` | The job was terminated because of preemption by another job.         |
    | RUNNING     | `R`  | The job is currently allocated to a node and is running.             |
    | SUSPENDED   | `S`  | A running job has been stopped with its cores released to other jobs.|
    | STOPPED     | `ST` | A running job has been stopped with its cores retained.              |

For more details on submitting and managing jobs, visit our [Running Jobs](./../jobs/overview/) Page.

#### Can I request access to GPU nodes?

GPU nodes are available for research workloads requiring accelerated computing. If you have a use case that requires GPU resources, reach out to the Cluster Support team at [ssc-server-support@lists.uchicago.edu](mailto:ssc-server-support@lists.uchicago.edu) to discuss your requirements and get access.

## Usage Policy

#### New SSCS Cluster Usage Policy?

The SSCS cluster is intended for academic research and instructional use by authorized University of Chicago faculty, students, and staff. Users are expected to use cluster resources responsibly, avoid monopolizing shared compute. Unauthorized or commercial workloads are not permitted on the cluster.

For questions about permitted use, contact us at [ssc-server-support@lists.uchicago.edu](mailto:ssc-server-support@lists.uchicago.edu).
