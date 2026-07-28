# Software Requirements Specification (SRS)
## Model Manager (MM)
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Model Manager (MM) software system. The intended audience includes project stakeholders, software developers, testers, system architects, and project managers. This SRS serves as the primary reference for the design, implementation, and verification of the system.

#### 1.2 Scope
The Model Manager (MM) is a software tool designed to automate the configuration, scheduling, execution, monitoring, and control of weather and climate model jobs (e.g., WRF, MM5, CAM). It extends existing model back-end systems to provide centralized management of jobs across one or more high-performance computing (HPC) clusters.

**In-Scope:**
*   Centralized job queue management and status monitoring.
*   Configuration and submission of standard model jobs (Weather FDDA/GMOD, ClimoFDDA).
*   Submission and monitoring of custom "by-hand" jobs.
*   Standalone post-processing job management.
*   Resource allocation and scheduling across multiple clusters.
*   User interfaces: Web-based GUI and Command-Line Interface (CLI).
*   Integration with cluster schedulers (e.g., PBS, Slurm) and data repositories (MetVault).
*   User authentication and role-based access control.

**Out-of-Scope (Non-Goals):**
*   Replacing the underlying scientific model executables.
*   Direct, low-level management of cluster hardware (CPU, memory, network).
*   Creation or modification of the core scientific algorithms within the models.
*   Long-term archival of data beyond integration with designated systems like MetVault.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **CAM:** Community Atmosphere Model
*   **CLI:** Command-Line Interface
*   **ClimoFDDA:** Climate Four-Dimensional Data Assimilation
*   **FDDA:** Four-Dimensional Data Assimilation
*   **GMOD:** (Weather) FDDA Model
*   **GUI:** Graphical User Interface
*   **HPC:** High-Performance Computing
*   **MM:** Model Manager
*   **MM5:** Fifth-Generation Penn State/NCAR Mesoscale Model
*   **PBS:** Portable Batch System
*   **RAL:** Research Applications Laboratory
*   **SLA:** Service Level Agreement
*   **SRS:** Software Requirements Specification
*   **WRF:** Weather Research and Forecasting Model

#### 1.4 References
*   Internal RAL Software Development Standards
*   MetVault System Interface Documentation
*   PBS/Slurm Scheduler API Documentation

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional and non-functional requirements. Appendices may contain supplementary diagrams or data models.

### 2. Overall Description

#### 2.1 Product Perspective
The MM is a middleware system that sits between users and heterogeneous HPC resources. It integrates with existing infrastructure components:
*   **Upstream:** Users (via Web GUI/CLI), Data Sources (MetVault, observational feeds).
*   **Downstream:** Cluster Schedulers (PBS, Slurm), Storage Systems.
*   **Interfaces:** See Section 2.5 for details.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Meteorologist/Software Engineer (NSAP)** | Expert in model configuration and operational workflows. Requires fine-grained control. | Advanced job configuration, cluster management, troubleshooting, and system customization. |
| **Research Scientist (RAL/External)** | Domain expert familiar with model setups. Runs customized experiments. | Ability to use custom data/processors, modify configurations, and run research-grade jobs. |
| **General User** | May monitor operations or run standard forecasts. Limited configuration expertise. | Simple, guided interfaces for standard jobs, clear monitoring views, and basic job control (stop/restart). |
| **System Administrator** | Maintains MM infrastructure and clusters. Has elevated privileges. | "Super user" capabilities, user/role management, system health monitoring, and log access. |

#### 2.3 Operating Environment
*   **Software:** Linux-based operating systems; Integration with PBS Pro and/or Slurm workload managers; Web server (e.g., Nginx/Apache); Backend application server (e.g., Python/Java).
*   **Hardware:** Capable of running on a dedicated management server; Network connectivity to all managed HPC clusters and storage systems (MetVault).
*   **Network:** Secure, low-latency network connections between MM and clusters are required for job control and status updates.

#### 2.4 Design and Implementation Constraints
1.  Must adhere to internal RAL security policies and software development standards.
2.  Must support integration with at least PBS and Slurm cluster schedulers.
3.  The system must not require modification to existing, validated scientific model executables.
4.  The web GUI must be accessible from standard modern browsers (Chrome, Firefox, Safari).

#### 2.5 Interfaces

##### 2.5.1 User Interfaces
*   **Web-based GUI:** The primary interface for all user interactions, including job setup, submission, monitoring, control, and configuration management.
*   **Command Line Tool (CLI):** A scriptable interface supporting all core functions for automation and integration into user workflows.

##### 2.5.2 Hardware Interfaces
The MM interfaces with HPC clusters via network protocols to communicate with cluster head nodes and schedulers.

##### 2.5.3 Software Interfaces
| Interface | Direction | Purpose | Key Data Exchanged |
| :--- | :--- | :--- | :--- |
| **MetVault** | Bi-directional | Data storage/retrieval for model I/O. | Input: Historical data requests. Output: Model output files & metadata. |
| **Cluster Scheduler (PBS/Slurm)** | MM → Cluster | Job submission & resource management. | Input: Job scripts, resource reqs (nodes, walltime). Output: JobID, status updates. |
| **Email Server (SMTP)** | MM → External | User notifications. | Input: Job events, user email. Output: Status notification emails. |

##### 2.5.4 Communications Interfaces
All external communications will use secure protocols (SSH for cluster commands, HTTPS for GUI, authenticated APIs for MetVault).

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Target HPC clusters are stable, properly configured, and accessible to the MM service account.
*   **Assumption:** Required observational and boundary condition data sources (via MetVault or direct paths) will be available at runtime.
*   **Dependency:** The availability and performance of integrated systems (MetVault, cluster schedulers) will directly impact MM functionality.

### 3. System Features and Requirements

#### 3.1 Functional Requirements

##### 3.1.1 User Authentication and Authorization (FR-01)
*   **FR-01.1:** The system shall require user authentication (username/password or institutional SSO) to access any functionality.
*   **FR-01.2:** The system shall implement Role-Based Access Control (RBAC) with at least the following roles: `General User`, `Scientist`, `Administrator`.
*   **FR-01.3:** Administrators ("super users") shall have the ability to control (stop, restart, delete) any job in the system.

##### 3.1.2 Job Configuration and Submission (FR-02)
*   **FR-02.1:** The system shall provide a module to configure and submit new Weather FDDA (GMOD) model jobs.
*   **FR-02.2:** The system shall provide a module to configure and submit new ClimoFDDA model jobs.
*   **FR-02.3:** The system shall allow users to save a job configuration (parameters, resources) for future re-use.
*   **FR-02.4:** The system shall allow users to load a saved job configuration, modify it, and submit it as a new job.
*   **FR-02.5:** The system shall allow submission of a "by-hand" job by registering an existing script or executable with mandatory metadata (Job ID, script path, estimated runtime, resource requirements).
*   **FR-02.6:** The system shall validate job configurations for completeness and logical consistency before accepting submission.

##### 3.1.3 Job Scheduling and Execution (FR-03)
*   **FR-03.1:** The system shall maintain a central queue of all jobs (scheduled, running, completed, failed).
*   **FR-03.2:** The system shall interface with cluster schedulers to allocate resources and launch jobs on the appropriate cluster.
*   **FR-03.3:** The system shall allow jobs to be scheduled for future execution times.

##### 3.1.4 Job Monitoring and Control (FR-04)
*   **FR-04.1:** Users shall be able to view a consolidated queue of all their jobs, with filtering by status (e.g., running, scheduled, completed).
*   **FR-04.2:** Selecting a job from the queue shall display detailed status information, including current processing stage, allocated cluster nodes, and estimated time remaining.
*   **FR-04.3:** Users with appropriate permissions shall be able to stop, restart, resume, or delete jobs from the queue.
*   **FR-04.4:** The system shall update job status information at a minimum frequency of once every 30 seconds.

##### 3.1.5 Post-Processing Management (FR-05)
*   **FR-05.1:** The system shall allow configuration of post-processing steps as part of a model job workflow.
*   **FR-05.2:** The system shall allow submission of a standalone post-processing job on existing model output data.

##### 3.1.6 Data and Integration Management (FR-06)
*   **FR-06.1:** The system shall retrieve historical input data from MetVault for re-run jobs.
*   **FR-06.2:** The system shall transfer model output products to specified destinations, including MetVault for storage.
*   **FR-06.3:** The system shall provide a mechanism to define and manage standard vs. custom data sources and processors.

#### 3.2 External Interface Requirements
*   **EI-01:** The web GUI shall render correctly on the latest two versions of major browsers (Chrome, Firefox, Safari).
*   **EI-02:** The CLI shall support execution on standard Linux shells (bash, zsh).
*   **EI-03:** The MM-to-Scheduler API shall support both PBS Pro 20+ and Slurm 21+.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance
*   **PER-01:** The latency between user job submission and its appearance in the scheduled queue shall be less than 5 seconds under normal load.
*   **PER-02:** Job status information in the GUI shall be updated at least every 30 seconds.
*   **PER-03:** The system shall support concurrent management of at least 500 active jobs (scheduled + running).

##### 3.3.2 Reliability & Availability
*   **REL-01:** The MM core service shall have a monthly availability of > 99.5%.
*   **REL-02:** The successful execution rate for fully configured, validated jobs shall be > 95%, excluding failures due to external cluster or data source issues.

##### 3.3.3 Security
*   **SEC-01:** All user sessions shall timeout after 30 minutes of inactivity.
*   **SEC-02:** All passwords shall be stored using strong, salted cryptographic hashing.
*   **SEC-03:** All actions performed on jobs (submit, modify, control) shall be logged in an audit trail with user ID, timestamp, and action details.

##### 3.3.4 Usability
*   **USA-01:** A General User shall be able to submit a standard GMOD job with less than 10 clicks/selections from the main dashboard, using default configurations.
*   **USA-02:** The system shall provide contextual help and tooltips for all configuration parameters.

##### 3.3.5 Observability & Supportability
*   **OBS-01:** The system shall log all major job lifecycle events (submit, schedule, start, complete, fail, control).
*   **OBS-02:** The system shall provide an administrative dashboard showing health status of all integrated clusters and background services.

### 4. Appendices

#### 4.1 Domain Model (UML Class Diagram Summary)
```
+----------------+       +----------------+       +---------------------+
|      User      |       |      Job       |       | Job Configuration   |
+----------------+       +----------------+       +---------------------+
| - UserID (PK)  |1    * | - JobID (PK)   |1    1 | - ConfigID (PK)     |
| - Role         |-------| - JobType      |-------| - JobType           |
| - Email        |       | - Owner (FK)   |       | - Parameters        |
+----------------+       | - Status       |       | - Owner (FK)        |
                         | - ScheduleTime |       | - CreationDate      |
                         | - ClusterAlloc |       +---------------------+
                         +----------------+
                                 |
                                 |1
                                 |
                         +---------------------+
                         |   Output Product    |
                         +---------------------+
                         | - ProductID (PK)    |
                         | - Job (FK)          |
                         | - Type              |
                         | - DestinationPath   |
                         +---------------------+

(Associated Entities: Cluster, DataSource, Processor, Notification)
```

#### 4.2 Acceptance Criteria (Gherkin Style)
*   **Job Submission:**
    *   **Given** a logged-in user is on the Job Setup page,
    *   **And** has selected "Weather FDDA" as the job type,
    *   **And** has provided all required, valid parameters,
    *   **When** the user clicks the "Submit" button,
    *   **Then** a success message is displayed,
    *   **And** the new job appears in the user's job queue with status "Scheduled".
*   **Job Monitoring:**
    *   **Given** a user has at least one job with status "Running",
    *   **When** the user navigates to the main Job Queue view,
    *   **And** clicks on the running job's ID,
    *   **Then** a detailed panel opens showing the current processing stage (e.g., "WRF Integration"),
    *   **And** the cluster nodes allocated (e.g., "cluster-a[node001-node008]"),
    *   **And** an estimated time remaining.

#### 4.3 Open Issues and Pending Decisions
1.  **Issue:** Default parameter set for a standard GMOD job.
    *   **Responsible:** Lead Meteorologist & System Architect.
2.  **Issue:** Detailed domain configuration workflow for WRF vs. MM5 models.
    *   **Responsible:** Modeling Software Engineers.
3.  **Issue:** Final list of "standard" observational data sources and their default processing scripts.
    *   **Responsible:** Data Integration Team.
4.  **Issue:** Job prioritization algorithm within the central queue (FIFO, priority scores, project-based).
    *   **Responsible:** System Architect & Operations Lead.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Architect | | | |
| QA Manager | | | |