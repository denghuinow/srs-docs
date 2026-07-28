# Software Requirements Specification (SRS)
## Model Manager System

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the **Model Manager** system. The primary purpose of this document is to provide a detailed description of the system's capabilities, interfaces, and performance characteristics to serve as a basis for design, implementation, and verification. The intended audience includes project stakeholders, software architects, developers, testers, and system administrators.

#### 1.2 Scope
The Model Manager is a software tool designed to facilitate the end-to-end management of computational jobs for weather and climate models (e.g., Weather FDDA, ClimoFDDA) across one or more high-performance computing (HPC) clusters. The system will provide a centralized interface for configuring, scheduling, executing, monitoring, and controlling model runs. Its core value is in abstracting the complexities of multi-cluster job management, providing users with a consistent and efficient workflow regardless of the underlying HPC infrastructure.

**In-Scope:**
*   Configuration and submission of new model jobs via templates or custom parameters.
*   Management (monitor, stop, restart, resume) of jobs in all states (scheduled, running, completed).
*   Centralized resource (node) allocation across multiple clusters.
*   Provision of both a Web-based Graphical User Interface (GUI) and a Command-Line Interface (CLI).
*   User-specified target cluster selection for job execution.

**Out-of-Scope:**
*   The actual execution of the weather/climate model binaries on cluster nodes.
*   User account management or cluster authentication (will integrate with existing systems like LDAP/SSO).
*   Detailed performance profiling or debugging of the model code itself.
*   Long-term archival and data management of model outputs (interfaces may be provided).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface
*   **CLI:** Command-Line Interface
*   **FDDA:** Four-Dimensional Data Assimilation
*   **GUI:** Graphical User Interface
*   **HPC:** High-Performance Computing
*   **Job:** A single instance of a configured model to be executed.
*   **Node Allocation:** The process of assigning specific compute nodes within a cluster to a job.
*   **SRS:** Software Requirements Specification

#### 1.4 References
*   (To be populated with relevant organizational standards, cluster specifications, and interface documents)

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements including performance, security, and usability. Section 5 describes external interface requirements.

### 2. Overall Description

#### 2.1 Product Perspective
The Model Manager is a standalone middleware system that sits between the end-user (scientist, modeler, technician) and the heterogeneous HPC cluster environments (e.g., Slurm, PBS Pro schedulers). It will integrate with existing cluster resource managers, authentication services, and possibly file systems, but will present a unified, simplified interface to the user.

#### 2.2 Product Functions
The high-level functions of the Model Manager are:
1.  **Job Configuration:** Guide users through setting up model runs using predefined templates (e.g., Weather FDDA) or fully custom parameters.
2.  **Job Submission & Scheduling:** Submit configured jobs to a selected or auto-assigned HPC cluster, handling the translation to the native cluster's job scheduler.
3.  **Job Lifecycle Management:** Provide real-time monitoring of job status, and controls to stop, restart, or resume jobs.
4.  **Multi-Cluster Coordination:** Intelligently manage and allocate compute resources across a federation of clusters based on availability, policy, and user preference.
5.  **Dual Interface Provision:** Serve user needs through an intuitive web GUI and a scriptable/automateable CLI.

#### 2.3 User Characteristics
*   **Primary Users (Scientists/Modelers):** Domain experts with deep knowledge of weather/climate models but varying levels of HPC technical expertise. They require an intuitive interface to run their experiments without deep involvement in cluster operations.
*   **Secondary Users (HPC Staff/Admins):** Technical personnel who may use the system for monitoring overall load, troubleshooting, or assisting users. They require detailed insights and controls.
*   **Automated Systems:** Other scripts or systems that may interact with the Model Manager via its CLI or API for automated workflows.

#### 2.4 Constraints
1.  **Architectural:** The system must be capable of managing jobs across multiple, potentially heterogeneous, HPC clusters.
2.  **Interface:** The system **must** provide both a web-based GUI and a command-line tool.
3.  **User Control:** The system **must** allow users to optionally specify a target cluster for job execution, overriding any automated allocation logic.
4.  **Integration:** Must work within the existing security and authentication framework of the supported HPC centers.

#### 2.5 Assumptions and Dependencies
*   It is assumed that target HPC clusters have a stable job scheduler (Slurm, PBS, etc.) and network connectivity to the Model Manager server.
*   The system depends on the continued operation and stable APIs of the underlying cluster resource managers.
*   User authentication and authorization will be delegated to existing institutional systems.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Job Configuration and Submission
*   **FR1.1:** The system shall provide templates for common model jobs (e.g., Weather FDDA, ClimoFDDA).
*   **FR1.2:** The system shall allow users to create a new job by filling a form based on a selected template (GUI) or by specifying parameters (CLI).
*   **FR1.3:** The system shall allow for the submission of fully custom "by-hand" jobs where users provide a pre-written job script or direct command.
*   **FR1.4:** During job setup, the system shall allow the user to optionally select a specific target cluster from a list of available clusters.
*   **FR1.5:** If no cluster is specified by the user, the system shall automatically select a target cluster based on configurable policies (e.g., resource availability, queue wait times, fairness).
*   **FR1.6:** The system shall validate job configuration parameters (e.g., resource requests, file paths) before submission and provide clear error messages.

##### 3.1.2 Job Monitoring and Control
*   **FR2.1:** The system shall provide a dashboard (GUI) and commands (CLI) to list all jobs owned by the user, filtered by status (Scheduled, Queued, Running, Completed, Failed, Stopped).
*   **FR2.2:** For each job, the system shall display key metadata: Job ID, Name, Model Type, Target Cluster, Status, Submission Time, Start/End Time, and Resource allocation.
*   **FR2.3:** The system shall provide near-real-time updates on job status by polling or receiving events from the underlying cluster schedulers.
*   **FR2.4:** The system shall allow an authorized user to **stop** a running or queued job.
*   **FR2.5:** The system shall allow an authorized user to **restart** a completed, failed, or stopped job with the original configuration.
*   **FR2.6:** The system shall allow an authorized user to **resume** a stopped job from the last checkpoint, if the model supports it (this may require model-specific configuration).

##### 3.1.3 Multi-Cluster Management
*   **FR3.1:** The system shall maintain a registry of available HPC clusters, including their connection details, scheduler type, and resource capabilities.
*   **FR3.2:** The system shall implement a central allocation manager that tracks node/resource usage across all managed clusters.
*   **FR3.3:** The allocation manager shall enforce global policies to prevent over-subscription of resources across clusters.
*   **FR3.4:** The system shall translate a generic Model Manager job description into the specific job script syntax (e.g., Slurm `#SBATCH` directives, PBS `#PBS` directives) required by the target cluster's scheduler.

##### 3.1.4 User Interfaces
*   **FR4.1 Web GUI:** The system shall provide a secure, responsive web interface accessible from standard browsers.
    *   **FR4.1.1:** The GUI shall include a login page integrated with organizational authentication.
    *   **FR4.1.2:** The GUI shall provide a main dashboard for job overview and control.
    *   **FR4.1.3:** The GUI shall include a wizard or form for configuring new jobs from templates.
*   **FR4.2 CLI:** The system shall provide a command-line tool (`model-manager`) with a comprehensive set of sub-commands.
    *   **FR4.2.1:** Example command structure: `model-manager job submit --template weather-fdda --cluster cluster-a ...`
    *   **FR4.2.2:** The CLI shall support JSON/YAML output for easy parsing by other scripts.
    *   **FR4.2.3:** The CLI shall have detailed help (`--help`) for all commands.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
*   **NFR1.1:** The web GUI dashboard shall load and display the user's job list within 2 seconds under normal load.
*   **NFR1.2:** Job status updates in the GUI shall be refreshed with a latency of no more than 30 seconds from the actual state change on the cluster.
*   **NFR1.3:** The CLI shall respond to query commands (e.g., `list`, `status`) within 1 second.
*   **NFR1.4:** The central allocation manager shall be able to handle decision-making for concurrent submission requests from at least 50 users.

##### 3.2.2 Reliability & Availability
*   **NFR2.1:** The Model Manager core service shall have an availability of 99.5% during business hours.
*   **NFR2.2:** Job metadata and configuration shall be persisted reliably. The loss of the Model Manager service shall not affect jobs already submitted and running on clusters.
*   **NFR2.3:** The system shall implement retry logic for transient failures in communication with cluster schedulers.

##### 3.2.3 Security
*   **NFR3.1:** All user access (GUI and CLI) shall require authentication.
*   **NFR3.2:** Users shall only be able to view, control, and modify jobs that they own.
*   **NFR3.3:** All communication between the Model Manager and cluster schedulers shall be encrypted (e.g., via SSH tunnels, APIs over HTTPS).
*   **NFR3.4:** Sensitive configuration data (passwords, keys) shall be stored using industry-standard encryption.

##### 3.2.4 Usability
*   **NFR4.1:** The web GUI shall be intuitive enough for a new user to submit a template-based job with minimal training.
*   **NFR4.2:** The CLI shall follow consistent and predictable patterns (e.g., similar to `git` or `kubectl`).
*   **NFR4.3:** Comprehensive logging shall be maintained for all user actions and system events for audit and debugging purposes.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Web GUI:** As described in FR4.1. A modern, browser-based interface.
*   **CLI:** As described in FR4.2. A single binary or script installable on user workstations or login nodes.

#### 4.2 Hardware Interfaces
*   The Model Manager server must have network connectivity to the login/head nodes of all managed HPC clusters.

#### 4.3 Software Interfaces
*   **Cluster Scheduler APIs/CLIs:** The system must interface with scheduler systems such as **Slurm** (`squeue`, `scancel`, `sbatch`), **PBS Professional** (`qsub`, `qstat`, `qdel`), etc.
*   **Authentication Provider:** LDAP, OAuth2, or OpenID Connect service for user authentication.
*   **Database:** A relational (e.g., PostgreSQL) or NoSQL database for persisting job metadata, templates, and system configuration.

#### 4.4 Communications Interfaces
*   **Protocols:** HTTP/HTTPS for the Web GUI and REST API. SSH for secure communication with cluster head nodes. Standard TCP/IP networking.

### 5. Appendices

#### 5.1 Use Case Examples (Brief)
*   **Use Case: Submit a Standard Weather FDDA Job**
    *   **Actor:** Scientist
    *   **Flow:** 1. Log into Web GUI. 2. Click "New Job", select "Weather FDDA" template. 3. Fill in domain, start/end times, resolution. 4. (Optional) Select "Cluster-B" from dropdown. 5. Click "Submit". System validates, allocates resources, translates to Slurm script, and submits to the chosen cluster.
*   **Use Case: Monitor and Stop Jobs via CLI**
    *   **Actor:** Modeler
    *   **Flow:** 1. Run `model-manager job list --status running`. 2. Identify a misconfigured job by its ID. 3. Run `model-manager job stop <job-id>`. System sends cancellation command to the relevant cluster scheduler.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Architect | | | |
| QA Manager | | | |