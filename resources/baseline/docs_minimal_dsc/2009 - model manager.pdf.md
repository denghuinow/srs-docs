# Software Requirements Specification (SRS)
## Model Job Automation and Management System (MJAMS)

**Document Version:** 1.0  
**Date:** [Current Date]  
**Authors:** [Author Name/Team]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Model Job Automation and Management System (MJAMS). The purpose of MJAMS is to provide a unified interface for automating the end-to-end lifecycle of computational weather and climate model jobs, from configuration and submission to monitoring and management, across heterogeneous high-performance computing (HPC) resources. This document is intended for use by the project stakeholders, developers, testers, and project managers.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The words `MUST`, `SHALL`, `WILL`, `SHOULD`, `MAY`, and `CAN` are used as described in IETF RFC 2119.
*   **Formatting:** User inputs, file paths, and code are denoted as `inline code`.

#### 1.3 Project Scope
MJAMS is a stand-alone software tool designed to automate the configuration, scheduling, execution, monitoring, and control of computational model jobs. Its core value is in reducing manual effort, minimizing human error, and providing a consistent interface for job management across one or more HPC clusters.

**In-Scope:**
*   Configuration of new model and post-processing jobs via a structured interface.
*   Submission and management of jobs defined externally ("by-hand").
*   Persistent storage, retrieval, and versioning of job configurations.
*   Real-time monitoring of job status across multiple clusters.
*   Administrative control over jobs (stop, restart, delete).
*   Automated resource allocation (node selection) based on job requirements.
*   Integration points for inclusion within a larger scientific workflow or portal system.

**Out-of-Scope:**
*   The actual scientific model code or post-processing scripts.
*   The underlying HPC batch scheduling system (e.g., Slurm, PBS Pro). MJAMS will interface with these systems.
*   User authentication and authorization at the cluster level (relies on existing infrastructure).
*   Long-term archival of model output data.

#### 1.4 References
*   IETF RFC 2119: Key words for use in RFCs to Indicate Requirement Levels.
*   Project Charter: MJAMS – Initial Vision and Goals.

### 2. Overall Description

#### 2.1 Product Perspective
MJAMS is envisioned as a middleware layer between the end-user and the complex ecosystem of HPC batch schedulers and cluster infrastructures. It abstracts the specifics of individual clusters while providing enhanced job management capabilities not natively present in standard schedulers.

```
[User] <-> [MJAMS Interface] <-> [MJAMS Core & Database] <-> [Adapter Layer] <-> [Cluster Scheduler (Slurm/PBS)] <-> [HPC Cluster]
```

#### 2.2 User Classes and Characteristics
1.  **Expert Modelers:** Scientists and engineers intimately familiar with model configuration. They will use MJAMS to create, fine-tune, and manage complex, custom job configurations for research and operations.
2.  **Standard Users:** Researchers or technicians who run standard, pre-defined model jobs. Their primary interactions are job submission, status monitoring, and basic management (stop/restart).
3.  **Monitors:** Team members (may overlap with Standard Users) who primarily need to view the status of running and queued jobs across all managed clusters without submitting new jobs.

#### 2.3 Operating Environment
*   **Software:** Must run on a central server or login node with network access to target HPC clusters. Will require Python 3.8+ and associated dependencies. Must interface with cluster schedulers (Slurm, PBS Pro, LSF).
*   **Hardware:** Standard server hardware. No specific computational requirements beyond hosting the application and database.
*   **Network:** Secure shell (SSH) and potentially REST API connectivity to cluster head nodes.

#### 2.4 Design and Implementation Constraints
1.  **C1:** The system MUST NOT require modification to the user's pre-existing job scripts or configurations for submission. Users MUST be able to provide mandatory information (e.g., script path, resource needs) to wrap and submit these "by-hand" jobs.
2.  **C2:** The system MUST manage jobs across multiple, potentially heterogeneous, HPC clusters.
3.  **C3:** The system MUST handle automated node/core allocation based on user-provided job requirements, interacting with the cluster's scheduler.
4.  **C4:** The system SHALL be designed as a stand-alone tool but MUST expose APIs or integration modules to allow embedding within a larger scientific workflow or portal system.

#### 2.5 Assumptions and Dependencies
*   Users have valid credentials and necessary permissions on the target HPC clusters.
*   Target HPC clusters are operational and accessible.
*   A relational database (e.g., PostgreSQL) is available for MJAMS configuration storage.

### 3. System Features and Requirements

#### 3.1 Job Configuration and Submission

**3.1.1 Description**
This feature allows users to define a new computational job, either from scratch using a guided interface or by providing the details of an existing job script.

**3.1.2 Functional Requirements**
*   `FR-101`: The system SHALL provide a form-based interface (CLI and/or GUI) for configuring a new model or post-processing job. Configurable parameters MUST include, at a minimum:
    *   Job name and description.
    *   Target HPC cluster.
    *   Executable path and arguments.
    *   Input data directory/paths.
    *   Output data directory.
    *   Computational resources (number of nodes, cores per node, memory, wall-clock time, GPU requirements).
    *   Dependency on other MJAMS-managed jobs.
*   `FR-102`: The system SHALL allow a user to submit a pre-existing, custom job script ("by-hand" job). The user MUST provide:
    *   Path to the main job script.
    *   Target cluster.
    *   Estimated resource requirements (nodes, walltime).
    *   (Optional) A descriptive job name.
*   `FR-103`: Upon submission, the system SHALL validate the provided configuration against cluster-specific limits and policies before interfacing with the batch scheduler.
*   `FR-104`: The system SHALL save every submitted job's configuration to a persistent database with a unique ID, timestamp, and user identifier.
*   `FR-105`: The system SHALL translate the internal job representation into the appropriate batch scheduler script (e.g., Slurm `#SBATCH` directives) and submit it.

#### 3.2 Job Repository and Re-submission

**3.2.1 Description**
This feature provides access to a history of all configured jobs, allowing users to retrieve, modify, and re-submit them.

**3.2.2 Functional Requirements**
*   `FR-201`: The system SHALL provide a searchable/filterable list of all past job configurations saved in the repository.
*   `FR-202`: A user SHALL be able to select a past job configuration, view its complete parameters, and create a new copy for modification.
*   `FR-203`: The user SHALL be able to modify any parameter of the copied configuration before submitting it as a new job.
*   `FR-204`: The system SHALL maintain versioning or a clear audit trail, linking re-submitted jobs back to their original configuration.

#### 3.3 Job Monitoring and Dashboard

**3.3.1 Description**
This feature provides a real-time, unified view of all MJAMS-managed jobs across all configured clusters.

**3.3.2 Functional Requirements**
*   `FR-301`: The system SHALL display a consolidated dashboard showing all jobs in the following states: `Queued`, `Running`, `Completed`, `Failed`, `Stopped`.
*   `FR-302`: For each job, the dashboard SHALL display, at a minimum: Job Name, User, Status, Cluster, Queue, Resources Used, Submission Time, Start/End Time.
*   `FR-303`: The dashboard SHALL automatically refresh status at a configurable interval (e.g., every 60 seconds).
*   `FR-304`: The system SHALL provide detailed, drill-down views for any job, showing:
    *   Full configuration parameters.
    *   Standard output and error logs from the cluster scheduler.
    *   Real-time performance metrics (if available from the cluster), e.g., CPU/memory utilization.

#### 3.4 Job Management and Control

**3.4.1 Description**
This feature allows authorized users to intervene in the lifecycle of scheduled and running jobs.

**3.4.2 Functional Requirements**
*   `FR-401`: A user SHALL be able to stop/cancel a job that is in `Queued` or `Running` state.
*   `FR-402`: A user SHALL be able to restart a job that is in `Completed`, `Failed`, or `Stopped` state. Restarting SHALL create a new job submission based on the last saved configuration.
*   `FR-403`: A user SHALL be able to delete a job record from the MJAMS repository. This action SHALL NOT affect any data or processes on the HPC cluster unless the job is running (deletion of a running job must first trigger `FR-401`).
*   `FR-404`: All management actions SHALL require user confirmation and SHALL be logged for audit purposes.

#### 3.5 Multi-Cluster and Resource Management

**3.5.1 Description**
This underlying capability enables MJAMS to abstract and manage resources across different HPC environments.

**3.5.2 Functional Requirements**
*   `FR-501`: The system administrator SHALL be able to configure multiple HPC clusters within MJAMS, specifying connection details, scheduler type, and resource limits.
*   `FR-502`: During job submission, the system SHALL automatically request the user-specified resources (from `FR-101`) from the selected cluster's scheduler, handling the node allocation process.
*   `FR-503`: The system SHALL be able to query each configured cluster's scheduler to obtain the status of MJAMS-managed jobs.

### 4. Non-Functional Requirements

#### 4.1 Performance
*   `NFR-601`: The job status dashboard SHALL update and render for the user within 5 seconds of a refresh request.
*   `NFR-602`: Job submission (from final user confirmation to receipt of scheduler job ID) SHALL complete within 10 seconds under normal load.

#### 4.2 Reliability & Availability
*   `NFR-701`: The MJAMS core service SHALL have an availability of 99.5% during standard working hours.
*   `NFR-702`: The failure of MJAMS SHALL NOT affect already running jobs on the HPC clusters.

#### 4.3 Usability
*   `NFR-801`: An expert user shall be able to configure and submit a standard new model job within 3 minutes.
*   `NFR-802`: The system SHALL provide clear, non-technical error messages when a job submission fails (e.g., "Insufficient memory available in the 'large' queue" instead of "PBS Error 12345").

#### 4.4 Security
*   `NFR-901`: User credentials for HPC clusters SHALL be stored securely using industry-standard encryption and shall never be logged.
*   `NFR-902`: Users SHALL only be able to view, manage, and modify jobs that they own, unless granted explicit administrative privileges.

#### 4.5 Portability & Integration
*   `NFR-1001`: The system's core logic SHALL be accessible via a well-documented REST API to facilitate integration with larger systems.
*   `NFR-1002`: The adapter layer for cluster schedulers SHALL be designed as pluggable modules to allow support for new schedulers without major code refactoring.

---
*Document End*