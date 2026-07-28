# Software Requirements Specification (SRS)
## For Grid-BGC Application Version 1.0

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Grid-BGC Application Version 1.0. It is intended for use by the project stakeholders, including developers, testers, project managers, and end-users, to ensure a common understanding of the system to be developed.

#### 1.2 Scope
The Grid-BGC Application is a grid-based software infrastructure designed to support biogeochemical (BGC) modeling. It provides a web portal interface for scientists to manage input data, execute the Daymet surface weather interpolation engine and the Biome-BGC model on remote computational resources, visualize results, and manage output data. The system leverages grid technologies (Globus toolkit) for secure access and utilizes the NCAR Mass Storage System (MSS) for all file-based storage.

**In-Scope Features:**
*   Web portal for end-to-end simulation workflow management.
*   Integration with NCAR Gatekeeper for user authentication.
*   Role-based access control for Scientists and Portal Administrators.
*   Data organization via reusable "Objects" and "Projects."
*   Core functions for creating, sharing, templating objects, and running simulations.
*   Basic administrative functions for user and job management.

**Out-of-Scope Features:**
*   Advanced, dedicated visualization projects for model output.
*   A dedicated post-processing evaluation project module.
*   Full functionality for the "Data User" role (lowest priority).
*   Implementation of user resource quotas (lowest priority).
*   Native format conversion for data downloads; data is provided in system-native formats only.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **BGC:** Biogeochemical
*   **DEM:** Digital Elevation Model
*   **MSS:** Mass Storage System (NCAR)
*   **NCAR:** National Center for Atmospheric Research
*   **SRS:** Software Requirements Specification
*   **UI:** User Interface
*   **API:** Application Programming Interface

#### 1.4 References
*   NCAR Security Policies
*   Globus Toolkit Documentation
*   NCAR Dataportal Web Server Integration Guide
*   Daymet Model Documentation
*   Biome-BGC Model Documentation

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, security, and constraints.

### 2. Overall Description

#### 2.1 Product Perspective
The Grid-BGC Application is a new, self-contained web application that will integrate into the existing NCAR Dataportal Web Server ecosystem. It acts as a middleware layer between the end-user and high-performance computing resources, grid infrastructure (Globus), and mass storage (NCAR MSS). It depends on the external NCAR Gatekeeper system for user authentication and authorization.

#### 2.2 Product Functions (Summary)
1.  **User Management:** Account creation, approval, and role assignment.
2.  **Data Object Management:** Creation, storage, retrieval, sharing, and templating of data objects (e.g., Surface Observation, DEM).
3.  **Project Management:** Grouping objects into projects for Daymet or Biome-BGC simulations.
4.  **Simulation Job Management:** Configuration, submission, monitoring, and termination of modeling jobs on grid resources.
5.  **Output Management:** Storage, browsing, and downloading of simulation results.
6.  **Basic Visualization:** Integrated visualization of model input and output data.
7.  **Administration:** Monitoring of system health, active jobs, and user management.

#### 2.3 User Characteristics
| User Class | Description | Key Skills/Knowledge |
| :--- | :--- | :--- |
| **Scientist (Primary)** | Researcher conducting BGC modeling. Uses the portal for core workflows. | Domain knowledge in BGC modeling, basic computer literacy, understanding of input data formats. |
| **Portal Administrator** | IT staff or senior scientist responsible for system oversight. | System administration, understanding of NCAR security and infrastructure. |
| **Data User (Future)** | Researcher who accesses and uses output data but does not run simulations. | Data analysis skills. *(Low priority for v1.0)* |

#### 2.4 Constraints
1.  **Technical:** Must use the Globus toolkit for all grid communications.
2.  **Storage:** All persistent file storage must use the NCAR Mass Storage System (MSS).
3.  **Integration:** The web portal must be integrated into the existing NCAR Dataportal Web Server framework.
4.  **Security:** Must comply with all NCAR security policies and constraints.
5.  **Authentication:** User authentication is exclusively handled via the external NCAR Gatekeeper system.
6.  **Architectural:** The system design must account for the latency and asynchronous nature of grid job execution.

#### 2.5 Assumptions and Dependencies
*   The NCAR Gatekeeper service will be available and provide the necessary authentication API.
*   The required computational resources (e.g., specific clusters, queues) for Daymet and Biome-BGC are accessible via the Globus grid.
*   The NCAR MSS will be available for all storage operations.
*   Users (Scientists) will have a basic understanding of the input parameters required for the Daymet and Biome-BGC models.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
The system shall provide a web-based GUI accessible via modern browsers. The interface shall include:
*   A dashboard for Scientists showing their projects, objects, and recent jobs.
*   Forms for creating and configuring data objects and simulation projects.
*   A job monitoring interface with status (Queued, Running, Completed, Failed), progress indicators, and logs.
*   A data browser for the MSS, tailored to the user's accessible objects and project outputs.
*   An administrative panel for user account approval and system monitoring.

**3.1.2 Hardware Interfaces**
The application server shall interface with:
*   NCAR MSS for file storage/retrieval.
*   Remote computational resources via the Globus GRAM (Grid Resource Allocation & Management) protocol.

**3.1.3 Software Interfaces**
*   **NCAR Gatekeeper:** For user authentication (SOAP/Web Service API).
*   **Globus Toolkit (v4+):** For grid security (GSI), file transfer (GridFTP), and job management (GRAM).
*   **NCAR Dataportal Web Server:** For hosting and serving the web application.
*   **Backend Database:** (e.g., PostgreSQL) for storing metadata about users, objects, projects, and jobs.

**3.1.4 Communications Interfaces**
All communication between the portal and grid resources shall be secured using the Globus Security Infrastructure (GSI) over standard HTTPS and GridFTP protocols.

#### 3.2 Functional Requirements

**3.2.1 User Account and Authentication (UAA)**
*   **UAA-1:** The system shall allow a new user to register using their NCAR Gatekeeper credentials.
*   **UAA-2:** Upon registration, the system shall assign the user a "Pending" status and notify a Portal Administrator.
*   **UAA-3:** A Portal Administrator shall be able to approve or reject a pending user account, assigning the "Scientist" role upon approval.
*   **UAA-4:** The system shall allow a Portal Administrator to assign the "Portal Administrator" role to other users.
*   **UAA-5:** The system shall prevent users with "Pending" status from accessing any core application features.

**3.2.2 Data Object Management (DOM)**
*   **DOM-1:** The system shall allow a Scientist to create a new data object (e.g., Surface Observation, DEM) by uploading files and providing metadata (name, description, geographic domain, etc.).
*   **DOM-2:** The system shall store the object's physical files in the NCAR MSS and its metadata in the application database.
*   **DOM-3:** The system shall allow a Scientist to view, search, and filter a list of their own data objects.
*   **DOM-4:** The system shall allow a Scientist to share a data object with one or more specific, registered Scientists, granting them "read" or "read/write" permissions.
*   **DOM-5:** The system shall allow a Scientist to create a template from an existing object for easy reuse.

**3.2.3 Project and Simulation Management (PSM)**
*   **PSM-1:** The system shall allow a Scientist to create a new "Project" (Daymet or Biome-BGC type).
*   **PSM-2:** For a Daymet Project, the system shall allow the Scientist to select/configure required input objects (e.g., Surface Observations) and set model parameters via a web form.
*   **PSM-3:** For a Biome-BGC Project, the system shall allow the Scientist to select/configure required input objects (e.g., Daymet output, DEM) and set model parameters via a web form.
*   **PSM-4:** The system shall allow the Scientist to submit the configured project for execution on a user-selected computational resource (from a pre-configured list).
*   **PSM-5:** The system shall submit the job to the grid using the Globus GRAM interface and track its Job ID.

**3.2.4 Job Monitoring and Output (JMO)**
*   **JMO-1:** The system shall provide a "My Jobs" page where a Scientist can see the status (Queued, Running, Completed, Failed, Canceled) of all their submitted jobs.
*   **JMO-2:** The system shall periodically poll the grid resource (via Globus) to update job statuses.
*   **JMO-3:** For a running job, the system shall provide a link to view the standard output and error logs streamed from the computational resource.
*   **JMO-4:** Upon successful job completion, the system shall automatically stage the output files from the compute resource to the user's designated space in the NCAR MSS and record the output location in the database.
*   **JMO-5:** The system shall allow a Scientist to browse and download the output files (in their native system format, e.g., NetCDF, HDF) from a completed project.

**3.2.5 Administration (ADM)**
*   **ADM-1:** The system shall provide an administrative dashboard accessible only to users with the "Portal Administrator" role.
*   **ADM-2:** The dashboard shall display a list of pending user accounts with options to approve or reject them.
*   **ADM-3:** The dashboard shall display a list of all currently running and recently completed jobs across all users, with filtering capabilities.
*   **ADM-4:** The dashboard shall display key system metrics (e.g., number of active users, total jobs this month, MSS storage used).

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   The web portal UI shall respond to user actions (e.g., page loads, form submissions) within 2 seconds under normal load (≤ 50 concurrent users).
*   The system shall be capable of managing and monitoring at least 100 concurrent simulation jobs.

**3.3.2 Safety & Security Requirements**
*   All user sessions shall be encrypted using TLS 1.2 or higher.
*   Direct access to the NCAR MSS shall be performed using principle of least privilege, adhering to the final decision on user credentials vs. proxy account.
*   No user credentials shall be stored in plain text within the application database or configuration files.
*   The system shall enforce role-based access control (RBAC) on all data objects and functions.

**3.3.3 Software Quality Attributes**
*   **Availability:** The web portal shall aim for 99% uptime during core business hours (8 AM - 6 PM MT).
*   **Reliability:** The job submission and status tracking mechanism shall have a transaction success rate of ≥ 95%.
*   **Usability:** A Scientist familiar with the domain shall be able to create and submit a simple project without referring to documentation.
*   **Maintainability:** The system shall have a modular architecture, separating UI, business logic, and grid communication layers.

### 4. Appendices

#### 4.1 Undecided Issues (TBD)
1.  **MSS Access Mechanism:** Final architecture for user access to MSS (direct user credentials vs. system proxy account).
2.  **Object Invalidation Workflow:** Detailed process for marking objects/projects as "invalid" when a dependent object is modified or deleted.
3.  **Administrator Settings:** Comprehensive list of system-wide configurable parameters (e.g., default computational resources, job timeout values).
4.  **Upload Format Specifications:** Exact file formats, naming conventions, and archive structures required for each type of data object upload.
5.  **Data Subsetting:** Implementation details for spatial or temporal subsetting of data during the download process.

---
*This document is considered a living artifact and may be updated as requirements are clarified and the project evolves.*