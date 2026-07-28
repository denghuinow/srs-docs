# Software Requirements Specification (SRS)
## Model Manager (MM)
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### Document Control

| **Version** | **Date** | **Author** | **Changes** |
| :--- | :--- | :--- | :--- |
| 1.0 | 2023-10-27 | SRS Author | Initial Draft |

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Model Manager (MM) software tool. The intended audience includes project stakeholders, management, and the software development team at RAL. This SRS serves as the definitive specification for the system's capabilities and constraints.

### 1.2 Scope
The Model Manager is a software application designed to automate the end-to-end workflow for configuring, scheduling, executing, monitoring, and managing computational jobs for numerical weather prediction (NWP) and climate models. It extends an existing back-end system to support increased project scale and user base, providing both a web-based Graphical User Interface (GUI) and a Command-Line Interface (CLI).

**In-Scope Elements:**
*   Job lifecycle management (configuration, submission, scheduling, execution, monitoring, termination, restart).
*   Resource management across one or more high-performance computing (HPC) clusters, including automated node allocation.
*   Support for specific job types: real-time and off-line Weather FDDA, ClimoFDDA, and post-processing.
*   Multiple submission methods: guided setup module, configuration file import, and execution of pre-existing user scripts ("by-hand").
*   Centralized job queue and status monitoring.

**Out-of-Scope Elements:**
*   Development or modification of the core scientific model executables (e.g., WRF, MM5).
*   Design of internal data structures or low-level system processes.
*   Long-term data archival, curation, or sophisticated data management systems.
*   Comprehensive user identity and access management (creation, complex permissions).
*   Real-time ingestion and processing of raw observational data from external sources.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **4DWX OTM:** Four-Dimensional Weather Observing System Operations and Testbed Manager.
*   **ClimoFDDA:** Climate Four-Dimensional Data Assimilation.
*   **FDDA:** Four-Dimensional Data Assimilation.
*   **GMOD:** (Assumed to be the existing model framework/system).
*   **GUI:** Graphical User Interface.
*   **CLI:** Command-Line Interface.
*   **HPC:** High-Performance Computing.
*   **MM:** Model Manager.
*   **MM5:** Fifth-Generation Penn State/NCAR Mesoscale Model.
*   **NSAP:** (Assumed organizational unit, e.g., National Security Applications Program).
*   **RAL:** Research Applications Laboratory.
*   **SRS:** Software Requirements Specification.
*   **WRF:** Weather Research and Forecasting model.

### 1.4 References
*   Project Charter: "Model Manager Functional Requirements" (Input Document).
*   GMOD System Architecture Documentation.
*   4DWX OTM System Integration Specifications.

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its user classes, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, security, and design constraints.

## 2. Overall Description

### 2.1 Product Perspective
The Model Manager is a middleware component that sits between the user and the existing HPC job scheduling infrastructure (e.g., Slurm, PBS). It integrates with the legacy GMOD framework and must also function as a component within the larger 4DWX OTM system. It abstracts the complexities of cluster resource management and job script generation, providing a unified interface for diverse user needs.

### 2.2 User Classes and Characteristics
1.  **NSAP Scientists/Engineers (Expert Users):** Primary users responsible for operational, production model runs. They possess deep knowledge of model configuration, FDDA, and the existing system. They require efficient, reliable, and automated workflows.
2.  **Research Scientists (Advanced Users):** Users from RAL or external institutions who run experimental or customized simulations. They may supply their own executables, data, and processors. They require flexibility to integrate custom workflows with centralized monitoring.
3.  **General Users (Basic Users):** Users who need to monitor the status of operational runs, stop/restart jobs, or execute standard post-processing tasks. They have limited knowledge of the underlying system and require an intuitive, guided interface.
4.  **Project Sponsors/Management:** Interested in project delivery, adherence to schedule/budget, and overall system success metrics.
5.  **Software Development Team:** Responsible for implementing, testing, and maintaining the Model Manager based on this SRS.

### 2.3 Operating Environment
*   **Software:** Must operate within the existing Linux-based HPC cluster environment. Must interface with the cluster's job scheduler (e.g., Slurm). Must be compatible with the GMOD framework and 4DWX OTM system architecture.
*   **Hardware:** Must be deployable on standard servers with network access to one or more HPC clusters.

### 2.4 Design and Implementation Constraints
1.  **Integration Constraint:** Must extend, not replace, the current model back-end system and accommodate the GMOD framework.
2.  **Deployment Constraint:** Must be capable of operating as a standalone application and as an integrated module within the 4DWX OTM system.
3.  **Model Support Constraint:** Must explicitly support jobs for the MM5 and WRF models, configured for FDDA (Weather/Climo) and post-processing types.
4.  **Custom Job Constraint:** User-provided scripts and executables for "by-hand" jobs must be pre-staged on the target cluster's filesystem; the MM will not handle their upload or storage.
5.  **Job Heterogeneity Constraint:** The architecture must support jobs with widely varying resource requirements (CPU cores, memory, wall time) and execution durations (minutes to days).

### 2.5 Assumptions and Dependencies
*   The underlying HPC cluster scheduler (e.g., Slurm) is stable and available.
*   Necessary model executables, libraries, and data are installed and accessible on the target clusters.
*   Users have valid accounts and standard permissions on both the MM system and the HPC clusters.
*   The existing GMOD framework provides stable interfaces or data locations that the MM can utilize.

## 3. System Features and Requirements

### 3.1 Feature: Job Configuration and Submission
**Description:** Users shall be able to define new model jobs through multiple methods and submit them to the system for execution.

**3.1.1 Requirement (FR-1.1): Guided Job Setup**
The system shall provide a web-based, form-driven interface (wizard or multi-step form) for configuring standard GMOD jobs (Weather FDDA, ClimoFDDA). This interface shall present users with validated fields for domain settings, physics options, FDDA parameters, start/end times, and resource requests (nodes, wall clock).

**3.1.2 Requirement (FR-1.2): Configuration File Import**
The system shall allow users to upload or specify the path to a pre-existing, valid job configuration file (in a system-defined format, e.g., YAML, JSON) to populate a new job submission.

**3.1.3 Requirement (FR-1.3): "By-Hand" Script Submission**
The system shall allow users to submit a pre-existing executable or shell script located on a cluster filesystem. The user must specify the full path, required arguments, and resource requirements. The MM will wrap this script for scheduling and monitoring but will not modify its contents.

**3.1.4 Requirement (FR-1.4): Job Configuration Save/Template**
The system shall allow users to save a fully or partially configured job as a named template for future use.

**3.1.5 Requirement (FR-1.5): Job Configuration Clone and Modify**
The system shall allow users to retrieve any of their previously saved configurations or completed jobs, clone them, and modify parameters to create a new job submission.

### 3.2 Feature: Job Scheduling and Execution
**Description:** The system shall manage the queueing, dispatch, and execution of jobs on one or more HPC clusters.

**3.2.1 Requirement (FR-2.1): Multi-Cluster Support**
The system shall be aware of and capable of submitting jobs to multiple, designated HPC clusters. The target cluster may be specified by the user or determined by system policy.

**3.2.2 Requirement (FR-2.2): Resource Allocation**
The system shall interact with the cluster's native scheduler to request and secure the compute nodes and wall time as specified in the job configuration.

**3.2.3 Requirement (FR-2.3): Job Dependency Management**
The system shall allow users to define dependencies between jobs (e.g., post-processing job starts only after the main FDDA job succeeds).

### 3.3 Feature: Job Monitoring and Control
**Description:** Users shall have a centralized view of job status and be able to control their own jobs.

**3.3.1 Requirement (FR-3.1): Centralized Job Queue Dashboard**
The system shall provide a GUI and CLI view showing all running, queued (scheduled), recently completed, and failed jobs. Display shall include, at minimum: Job ID, Name, Owner, Status, Cluster, % Complete (if running), Start Time, and Estimated Finish Time.

**3.3.2 Requirement (FR-3.2): Detailed Job View**
Upon user request (e.g., clicking a job ID), the system shall display detailed information about a job. This includes full configuration parameters, real-time log output (tail), scheduler status, resource utilization metrics, and output file locations.

**3.3.3 Requirement (FR-3.3): Job Control Actions**
Authenticated users shall be able to stop (terminate) or restart their own jobs that are in a running or queued state via both GUI and CLI.

**3.3.4 Requirement (FR-3.4): Notification**
The system shall provide a configurable mechanism (e.g., email, dashboard alert) to notify users upon job completion (success or failure).

### 3.4 Feature: Post-Processing Job Management
**Description:** Users shall be able to configure and run jobs that process existing model output.

**3.4.1 Requirement (FR-4.1): Post-Processing Job Definition**
The system shall provide an interface to configure post-processing jobs. As a minimum, this includes selecting input model run(s) and output data, choosing from a list of standard post-processing tasks (e.g., plot generation, diagnostics), and specifying resource requirements.

**3.4.2 Requirement (FR-4.2): Input Data Association**
The post-processing job configuration shall clearly link to the output data from one or more prior model runs managed by the MM.

### 3.5 Feature: User Interfaces
**Description:** The system shall provide two primary modes of interaction.

**3.5.1 Requirement (FR-5.1): Web-Based GUI**
The system shall provide a responsive, web-based graphical user interface accessible via standard browsers. The GUI shall implement all user-facing functions described in FR-1.1, FR-3.1, FR-3.2, FR-3.3, and FR-4.1.

**3.5.2 Requirement (FR-5.2): Command-Line Interface (CLI)**
The system shall provide a comprehensive CLI with commands and options corresponding to all key functional areas (job submit, list, status, stop, restart, configure). The CLI shall be scriptable for automation.

## 4. Non-Functional Requirements

### 4.1 Performance Requirements
*   **Job Submission Latency:** The time from user submission click to the job being placed in the cluster scheduler's queue shall be less than 10 seconds for standard jobs.
*   **Dashboard Refresh:** The job queue dashboard shall update status information at least every 30 seconds without perceptible lag to the user.
*   **Concurrent Users:** The system shall support at least 20 concurrent active users without degradation of service.
*   **Concurrent Jobs:** The system shall be capable of managing at least 50 concurrently active (running or queued) jobs.

### 4.2 Safety & Security Requirements
*   **Authentication:** Users must authenticate with the system using existing organizational credentials (e.g., LDAP).
*   **Authorization:** Users may only view, control, or modify jobs that they own. A supervisory/administrative role may be required for system management.
*   **Audit Trail:** All job submission, modification, and control actions (start, stop, restart) shall be logged with timestamp, user, and job ID.

### 4.3 Software Quality Attributes
*   **Reliability:** The MM service shall have an uptime availability of 99.5% during core business hours. Job metadata and configuration must be persisted to prevent loss on service restart.
*   **Usability:** The GUI shall be intuitive enough for a General User to monitor jobs and perform basic tasks with less than 30 minutes of training. Expert user workflows for common tasks must be more efficient than the pre-MM manual process.
*   **Maintainability:** The codebase shall be modular, with clear separation between UI, business logic, and cluster communication layers. It shall be well-documented.

### 4.4 Undecided Issues / TBD
The following items require stakeholder resolution and will impact detailed design:
1.  The precise default configuration parameters for a "standard" GMOD FDDA job.
2.  The definitive list of observational data sources and their associated pre-processing scripts to be supported by default.
3.  The scope and configurability of the post-processing module (beyond basic plot generation).
4.  The algorithm or rules for prioritizing jobs within the MM's internal queue (e.g., operational vs. research, project).
5.  The exhaustive list of data points to be displayed in the "Detailed Job View" (FR-3.2).

---
**Appendix A: User Story Mapping to Requirements**

| User Story | Primary Functional Requirement(s) |
| :--- | :--- |
| 1. Set up/submit real-time FDDA job | FR-1.1, FR-1.4 |
| 2. Submit custom "by-hand" job | FR-1.3 |
| 3. Retrieve/modify saved job | FR-1.5 |
| 4. View centralized job queue | FR-3.1 |
| 5. Run post-processing on output | FR-4.1, FR-4.2 |
| 6. Stop/restart own jobs | FR-3.3 |