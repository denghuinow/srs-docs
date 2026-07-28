# Software Requirements Specification (SRS)
## Model Manager (MM)
**Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Model Manager (MM). The MM is a software tool designed to automate the configuration, scheduling, execution, monitoring, and termination of weather and climate model jobs across one or more high-performance computing (HPC) clusters. This SRS serves as a contract between the stakeholders and the development team, providing a basis for design, implementation, testing, and acceptance.

#### 1.2 Document Conventions
*   **Requirements:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms "MUST," "MUST NOT," "SHALL," "SHALL NOT," "SHOULD," and "MAY" are used as defined in IETF RFC 2119.
*   **Formatting:** This document uses Markdown formatting. Code blocks and file paths are presented in monospace.

#### 1.3 Project Scope
The MM automates the end-to-end workflow management of computational model jobs. Its scope includes:
*   Providing user interfaces for job definition, submission, and monitoring.
*   Translating user configurations into executable job scripts for target HPC clusters.
*   Interfacing with cluster job schedulers (e.g., Slurm, PBS) to submit, query, and control jobs.
*   Managing job metadata, configurations, and status history.
*   Optionally interfacing with external data archives for input and output.

**Out of Scope:**
*   Development or modification of the underlying scientific weather/climate models.
*   Management of raw data sources or the creation of fundamental processing scripts.
*   Direct management of cluster hardware, operating systems, or scheduler software.

#### 1.4 References
*   Project Charter: Model Manager (MM) – Initial Vision
*   4DWX OTM System Architecture Document
*   MetVault Data Archive API Specification
*   GCAT Tool Interface Documentation

### 2. Overall Description

#### 2.1 Product Perspective
The MM is a standalone application that extends and enhances an existing model execution back-end. It is designed to be integrated as a core component within the broader 4DWX Operational Tasking and Management (OTM) system. It interacts with external HPC resources and can optionally connect to the MetVault data archive system.

#### 2.2 Product Functions (High-Level)
1.  **Job Configuration:** Guide users through setting up new model runs or post-processing tasks.
2.  **Job Submission & Scheduling:** Submit configured jobs to one or more HPC clusters, handling dependencies and resource requests.
3.  **Job Lifecycle Management:** Monitor job status, stop running jobs, restart failed jobs, and resume paused jobs.
4.  **Job History & Retrieval:** Store job configurations and metadata, allowing users to retrieve, modify, and re-run previous jobs.
5.  **Multi-Cluster Management:** Intelligently distribute jobs across available computing resources based on policy and user choice.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Scientist/Engineer (Primary)** | Expert in model configuration. Runs operational forecasts and research simulations. | Efficient, accurate setup of complex jobs. Fine-grained control over resources and parameters. Ability to manage many concurrent jobs. |
| **Technician/Monitor (Secondary)** | Less experienced with model details. Responsible for operational monitoring. | Simple, clear view of job status. Ability to run standard, pre-defined job types. Alerts for job failures. |
| **Super User / Administrator** | Has system-level responsibilities. Manages all users and jobs. | Permission to view, control, and modify any job in the system. User and resource management capabilities. System configuration. |

#### 2.4 Operating Environment
*   **Software:** The MM server component will run on a Linux-based platform. Client access is via modern web browsers (GUI) and shell/command line (CLI).
*   **Hardware:** The MM application server will require network connectivity to one or more remote HPC clusters and optionally to the MetVault archive.
*   **External Systems:** HPC cluster job schedulers (Slurm, PBS, LSF, etc.), MetVault data archive (optional), 4DWX OTM system (future integration).

#### 2.5 Design and Implementation Constraints
1.  The system MUST NOT require modification to existing, validated model executables or core scientific scripts.
2.  The user interface MUST be accessible from standard DOD security enclaves.
3.  For custom "by-hand" jobs, the MM SHALL NOT be responsible for deploying user scripts or executables to the target cluster; this is the user's responsibility (`CON-001`).
4.  The system MUST integrate with the existing GCAT tool's workflow for climate-specific job types (`CON-002`).

#### 2.6 Assumptions and Dependencies
*   Standard model configurations, data sources, and base processing scripts are available on the target HPC clusters (`ASM-001`).
*   User and service accounts with appropriate submission privileges exist on the connected HPC clusters.
*   The network latency and bandwidth between the MM server and the HPC clusters are sufficient for job script transfer and status polling.

### 3. External Interface Requirements

#### 3.1 User Interfaces
*   **Web-based GUI:** A responsive, intuitive web application for all job management functions. It shall include dashboards, forms for job configuration, and real-time status displays.
*   **Command-Line Interface (CLI):** A suite of command-line tools (`mm-submit`, `mm-status`, `mm-stop`, etc.) providing scriptable access to all core MM functionality for expert users and automation.

#### 3.2 Hardware Interfaces
The MM server requires standard network interfaces (1 GbE or higher) to communicate with HPC login nodes and archive systems.

#### 3.3 Software Interfaces
*   **HPC Cluster Schedulers:** The MM MUST interface via SSH and command-line tools (e.g., `sbatch`, `scancel`, `squeue` for Slurm) or a REST API if available.
*   **MetVault Archive:** Optional RESTful API for querying available input data and registering/pushing output data. The system must operate in a degraded mode if this connection is unavailable.
*   **4DWX OTM System:** A future defined API (TBD) for receiving tasking requests and reporting status.

#### 3.4 Communications Interfaces
All external communications SHALL use secure protocols (e.g., SSH, HTTPS/TLS 1.2+). Authentication credentials must be managed securely, following organizational IT security policies.

### 4. System Features

#### 4.1 Job Configuration and Submission
**Description:** This feature allows users to define a new computational job, specify its parameters, and submit it for execution.

**Requirements:**
*   `FR-101` The system SHALL provide a form/wizard to configure a new model job, including model type, domain, resolution, physics options, start/end times, and resource requirements (cores, memory, walltime).
*   `FR-102` The system SHALL provide a form to configure a standalone post-processing job, specifying input data location, processing script, and output destination.
*   `FR-103` The system SHALL allow a user to submit a pre-existing, manually configured job script that resides on a cluster by specifying its path and basic metadata.
*   `FR-104` The system SHALL allow a job to be submitted by loading a pre-defined, valid MM job configuration file (e.g., in YAML or JSON format).
*   `FR-105` During submission, the user SHALL have the option to select a specific HPC cluster for execution or select "Auto" for system-determined placement (`NFR-101`).
*   `FR-106` The system SHALL validate all user-provided configuration parameters against known constraints before submission.

#### 4.2 Job Management and Monitoring
**Description:** This feature provides oversight and control over the lifecycle of all submitted jobs.

**Requirements:**
*   `FR-201` The system SHALL provide a unified view (dashboard) of all jobs the user has permission to see, categorized by status (Scheduled, Queued, Running, Completed, Failed, Stopped).
*   `FR-202` For each job, the view SHALL display key metadata: Job ID, Name, User, Status, Cluster, Submission Time, Start/End Time, and progress indicators where applicable.
*   `FR-203` The system SHALL allow a user with appropriate permissions to stop (terminate) a scheduled or running job.
*   `FR-204` The system SHALL allow a user to restart a completed, failed, or stopped job with the option to modify its configuration.
*   `FR-205` The system SHALL allow a user to resume a job from a checkpoint, if the underlying model supports it.
*   `FR-206` The system SHALL provide detailed, real-time access to job output logs (stdout/stderr) from the HPC cluster.

#### 4.3 Job History and Retrieval
**Description:** This feature enables users to find, inspect, and re-use configurations from past jobs.

**Requirements:**
*   `FR-301` The system SHALL persistently store the complete configuration and submission metadata for every job.
*   `FR-302` The system SHALL provide search and filter capabilities to find past jobs by name, date, user, model type, or status.
*   `FR-303` The user SHALL be able to retrieve a saved job configuration, view it, modify any parameter, and submit it as a new job instance.
*   `FR-304` The system SHALL allow a user to export a job's configuration to a standard file format for sharing or offline backup.

#### 4.4 User and Permission Management
**Description:** This feature controls access to jobs and system functions based on user roles.

**Requirements:**
*   `FR-401` A "Super User" SHALL have view and control permissions over all jobs in the system.
*   `FR-402` A "Regular User" SHALL only have view and control permissions over jobs they have submitted.
*   `FR-403` Job lists and actions in both the GUI and CLI SHALL be filtered and enforced according to these permissions.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-201` The system MUST support the concurrent submission and monitoring of at least 50 real-time forecast ensemble members distributed across several clusters (`NFR-102`).
*   `NFR-202` Job status information (queued, running, completed) in the GUI MUST be updated at least every 60 seconds.
*   `NFR-203` The system's overhead (time from user submission to job being queued on the cluster) MUST be less than 30 seconds for standard job types.

#### 5.2 Safety & Security Requirements
*   `NFR-301` All user authentication MUST integrate with the organization's central identity management system (e.g., LDAP/Active Directory).
*   `NFR-302` All communications with HPC clusters and archives MUST be encrypted.
*   `NFR-303` User credentials for cluster access MUST be stored and handled using industry-standard secure vault mechanisms.

#### 5.3 Reliability & Availability Requirements
*   `NFR-401` The MM service (GUI and CLI backend) MUST have an operational availability of 99.5% during core business hours.
*   `NFR-402` The failure of the MM server MUST NOT affect jobs already submitted and running on HPC clusters.
*   `NFR-403` The system MUST gracefully handle the loss of connection to an HPC cluster, queueing actions and providing clear error messages.

#### 5.4 Usability Requirements
*   `NFR-501` A technically proficient user MUST be able to configure and submit a standard real-time forecast job using the GUI within 5 minutes.
*   `NFR-502` The web GUI MUST be usable by personnel with standard training, without requiring deep knowledge of the underlying HPC scheduler commands.

#### 5.5 Portability & Compatibility
*   `NFR-601` The MM backend core SHALL be designed to easily add support for new HPC cluster scheduler types with minimal code changes.

### 6. Other Requirements

#### 6.1 Priorities
**Priority 1 (Core):** Features `FR-101`, `FR-105`, `FR-201`, `FR-202`, `FR-203`, `FR-301`, `FR-401`, `FR-402`, and all `NFR-1xx` and `NFR-2xx` requirements related to standard real-time/off-line forecast automation.
**Priority 2 (Required):** Features `FR-102`, `FR-103`, `FR-104`, `FR-204`, `FR-302`, `FR-303` (support for custom jobs, post-processing, and history).
**Priority 3 (Future Enhancement):** Feature `FR-205` (resume from checkpoint), advanced job dependency chains, and deeper 4DWX OTM integration.

#### 6.2 Acceptance Approach
Acceptance testing will involve a suite of representative job scenarios:
1.  Submission and successful execution of a standard real-time forecast job on an auto-selected cluster.
2.  Submission of a custom "by-hand" job to a user-specified cluster.
3.  Submission of a job via a pre-defined configuration file.
4.  Retrieval, modification, and re-submission of a past job.
5.  Monitoring of a job's status and review of its logs.
6.  Stopping a running job.
7.  Verification of permission enforcement (regular vs. super user).
8.  Demonstration of concurrent ensemble job management across multiple clusters.

The system will be deemed acceptable when it correctly performs all Priority 1 and Priority 2 scenarios without requiring user intervention in cluster-level commands or script creation, meeting the performance and reliability criteria outlined in Section 5.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Developer | | | |
| QA Manager | | | |