# Software Requirements Specification (SRS)
## Grid-BGC Application Version 1.0

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Grid-BGC Application Version 1.0. It is intended to serve as a comprehensive guide for developers, testers, project managers, and stakeholders involved in the design, implementation, verification, and maintenance of the system.

#### 1.2 Document Conventions
*   Requirements are uniquely identified using the format `FR-XXX` for Functional Requirements and `NFR-XXX` for Non-Functional Requirements.
*   Key terms are **bolded** upon first use.
*   All file paths, system names, and code references are presented in `inline code` blocks.

#### 1.3 Project Scope
The Grid-BGC Application is a grid-based software infrastructure designed to support bio-geo-chemical modeling. It provides a graphical web portal that enables scientists to manage input data, execute simulations using the Daymet and Biome-BGC models on distributed computational resources, and visualize, download, and share results. The system leverages the Globus toolkit and integrates with NCAR's computational resources and the NCAR Mass Storage System (MSS) to facilitate secure, distributed scientific workflows.

**Out of Scope:**
*   Development of the core Daymet or Biome-BGC scientific models.
*   Administration of the underlying NCAR Gatekeeper, MSS, or compute cluster hardware.
*   Advanced statistical analysis or custom visualization tools beyond basic data viewing and export.

#### 1.4 References
*   NCAR Security and Gatekeeper Policy Documentation
*   Globus Toolkit Documentation
*   Daymet Model Algorithm Theoretical Basis Document
*   Biome-BGC Model User's Guide

### 2. Overall Description

#### 2.1 Product Perspective
The Grid-BGC Application is a new, self-contained web portal that acts as a middleware layer between the user and existing NCAR cyberinfrastructure. It is dependent on several external systems:
*   **NCAR Dataportal Web Server:** Hosting environment for the web application.
*   **NCAR Gatekeeper:** Primary user authentication and authorization service.
*   **NCAR Mass Storage System (MSS):** Primary repository for all file-based data.
*   **Globus Toolkit:** Provides grid communication services for job submission and data transfer.
*   **Hemisphere Linux Cluster (CU):** Primary computational resource for model execution.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Scientist (Primary)** | Domain expert in biogeochemistry or climatology. Comfortable with model parameters but not necessarily with grid computing. | Configure and run modeling projects, manage input/output data, visualize results. |
| **Portal Administrator** | Technical staff responsible for system health and user support. Has elevated privileges. | Manage user accounts, monitor and manage jobs, perform system oversight. |
| **Data User (Secondary)** | Researcher interested in results but not in running simulations. May be internal or external to the project. | Discover, access, and download published output datasets. |

#### 2.3 Operating Environment
*   **Server:** Application hosted on the NCAR Dataportal Web Server (Linux-based).
*   **Client:** Web portal compatible with Internet Explorer 6.0+, Netscape 7.1+, and Safari.
*   **Backend:** Integration with Globus Toolkit, NCAR MSS, and the Hemisphere Linux cluster at CU.

#### 2.4 Design and Implementation Constraints
1.  **NFR-INT-01:** All persistent, file-based data must be stored on the NCAR Mass Storage System (MSS).
2.  **NFR-SEC-01:** User authentication must be performed via the NCAR Gatekeeper system.
3.  **NFR-ARCH-01:** Grid communications must be implemented using the Globus toolkit.
4.  **NFR-PER-01:** The system must handle large grid datasets (multi-gigabyte) efficiently.

#### 2.5 Assumptions and Dependencies
*   The NCAR Gatekeeper, MSS, and Hemisphere cluster will remain operational and accessible.
*   Users will have valid NCAR Gatekeeper credentials.
*   Required model executables (Daymet, Biome-BGC) are pre-installed and configured on the compute nodes.
*   User documentation will be completed and made available online.

### 3. System Features and Requirements

#### 3.1 User Account Management
**3.1.1 Description**
This feature handles the lifecycle of user accounts, from application and approval to login and security management.

**3.1.2 Functional Requirements**
*   **FR-ACC-01:** A public portal page shall allow a new user to apply for an account by providing their NCAR Gatekeeper username and email address.
*   **FR-ACC-02:** The system shall notify the Portal Administrator of a pending account application.
*   **FR-ACC-03:** A Portal Administrator shall be able to approve or reject account applications via an administrative interface.
*   **FR-ACC-04:** Upon approval, the system shall create a **User Account** record linked to the Gatekeeper username.
*   **FR-ACC-05:** Users shall log in to the portal using their NCAR Gatekeeper credentials.
*   **FR-ACC-06:** The system shall lock a user account after three consecutive failed login attempts.
*   **FR-ACC-07:** A Portal Administrator shall be able to view, unlock, and modify the status (active/inactive) of any user account.

#### 3.2 Data Object Management
**3.2.1 Description**
This feature allows Scientists to create, upload, validate, and manage **Data Objects**, which are the fundamental units of input data (e.g., Surface Observations, DEMs, Parameterization files).

**3.2.2 Functional Requirements**
*   **FR-DATA-01:** A Scientist shall be able to create a new **Data Object** by specifying its **Object Type** (List, Grid, Parameterization) and uploading corresponding data files.
*   **FR-DATA-02:** During upload, the system shall validate the file format and structure against predefined specifications (e.g., NetCDF conventions).
*   **FR-DATA-03:** The system shall automatically extract and store technical and scientific metadata from validated files.
*   **FR-DATA-04:** Each **Data Object** shall have a mutable **Sharing Status** (Private, Shared with specific users, Public Template).
*   **FR-DATA-05:** Each **Data Object** shall have a **Data Integrity State**: `Unlocked` (editable), `Locked` (in use by a project), or `Invalidated` (source files missing/corrupt).
*   **FR-DATA-06:** The user interface shall clearly indicate the **Data Integrity State** and **Sharing Status** of every object.
*   **FR-DATA-07:** A Scientist shall be able to delete their own `Unlocked` **Data Objects**, with a confirmation prompt.

#### 3.3 Project Configuration and Execution
**3.3.1 Description**
This core feature enables Scientists to configure Daymet or Biome-BGC modeling projects, submit them for execution on grid resources, and monitor their progress.

**3.3.2 Functional Requirements**
*   **FR-PROJ-01:** A Scientist shall be able to create a new **Project**, selecting its type (Daymet or Biome-BGC).
*   **FR-PROJ-02:** The Scientist shall configure the project by selecting required, locked **Data Objects** (e.g., DEM, Surface Observations) and setting model-specific parameters (e.g., simulation topology, time period).
*   **FR-PROJ-03:** The system shall prevent a project from being submitted if any referenced **Data Object** is not in a `Locked` state.
*   **FR-PROJ-04:** Upon submission, the Scientist shall select an available computational resource node (e.g., Hemisphere cluster).
*   **FR-PROJ-05:** The system shall create a **Compute Job** record and use the Globus toolkit to submit the job to the selected resource.
*   **FR-PROJ-06:** The system shall provide a job monitoring interface showing overall **Job Status** (Pending, Running, Complete, Failed) and, for grid-based projects, **Tile Statuses**.
*   **FR-PROJ-07:** A Scientist shall be able to terminate their own running jobs.

#### 3.4 Output Management and Visualization
**3.4.1 Description**
This feature manages the results of successful model runs, providing capabilities for data access, basic visualization, and download.

**3.4.2 Functional Requirements**
*   **FR-OUT-01:** Upon successful completion of a **Compute Job**, the system shall automatically create a **Model Output** object, linking it to the source **Project ID**.
*   **FR-OUT-02:** The system shall retrieve output files from the compute node and store them on the MSS.
*   **FR-OUT-03:** A Scientist shall be able to view a list of their **Model Output** objects, filtered by source project.
*   **FR-OUT-04:** For a selected **Model Output**, the user shall be able to view basic metadata (creation date, tile info, contained datasets).
*   **FR-OUT-05:** The system shall provide basic graphical visualization (e.g., 2D maps, time series plots) for standard output variables.
*   **FR-OUT-06:** Users shall be able to download the full dataset or selected subsets of a **Model Output** object they own or that has been shared with them.

#### 3.5 Sharing and Collaboration
**3.5.1 Description**
This feature enables users to share **Data Objects** and **Model Outputs** with other specific users or publish them as system-wide templates for community reuse.

**3.5.2 Functional Requirements**
*   **FR-SHR-01:** The owner of a **Data Object** or **Model Output** shall be able to change its **Sharing Status** to grant read-access to one or more specific users.
*   **FR-SHR-02:** A Scientist shall be able to promote one of their **Data Objects** to a **System Template** by providing a description.
*   **FR-SHR-03:** All users shall be able to browse and view available **System Templates**.
*   **FR-SHR-04:** A Scientist shall be able to create a new **Data Object** based on a **System Template**, creating a personal copy.

#### 3.6 Administrative Oversight
**3.6.1 Description**
This feature provides the Portal Administrator with tools to manage the system, its users, and its jobs.

**3.6.2 Functional Requirements**
*   **FR-ADM-01:** The Administrator shall have a dedicated interface accessible after login.
*   **FR-ADM-02:** The Administrator shall be able to perform all actions listed in FR-ACC-03 and FR-ACC-07.
*   **FR-ADM-03:** The Administrator shall be able to view a dashboard showing system metrics (total jobs, active users, storage usage).
*   **FR-ADM-04:** The Administrator shall be able to view, filter, and manage (e.g., terminate) all **Compute Jobs** in the system.
*   **FR-ADM-05:** The Administrator shall be able to initiate a consistency check that validates the integrity of **Data Objects** against files in the MSS and updates their **Data Integrity State** accordingly.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The primary interface shall be a web portal with a consistent layout: a header with user info and navigation, a main content area, and a footer with help links.
*   **NFR-UI-01:** Context-sensitive online help shall be accessible from every page via a help icon or link.
*   Lists of objects (Data, Projects, Outputs) shall be presented in sortable, filterable tables.
*   Forms for configuration shall use appropriate controls (dropdowns, checkboxes, numeric inputs) with validation.

#### 4.2 Hardware Interfaces
*   The system shall interface with the Hemisphere Linux cluster via Globus GRAM for job submission.
*   The system shall interface with the NCAR MSS for all file storage and retrieval operations.

#### 4.3 Software Interfaces
*   **NCAR Gatekeeper:** Authentication via secure web service calls or proxy validation.
*   **Globus Toolkit 4.x:** Use of GRAM, GridFTP, and MDS services.
*   **NCAR MSS:** Use of MSS client libraries or commands for file put/get operations.
*   **Dataportal Web Server:** Apache HTTP Server with PHP/Python.

#### 4.4 Communications Interfaces
*   All communications between the web portal and external services (Gatekeeper, Globus, MSS) shall use secure, authenticated channels (HTTPS, GSI-secured GridFTP).

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NFR-PER-02:** The portal interface shall load any dashboard or list view within 3 seconds under normal load.
*   **NFR-PER-03:** Metadata for **Data Objects** and **Projects** shall be stored in a relational database for fast querying.
*   **NFR-PER-04:** File transfers to/from the MSS shall be managed asynchronously to prevent web request timeouts.

#### 5.2 Safety Requirements
*   Not applicable.

#### 5.3 Security Requirements
*   **NFR-SEC-02:** All user sessions shall timeout after 30 minutes of inactivity.
*   **NFR-SEC-03:** User credentials shall never be stored in plain text within the application database.
*   **NFR-SEC-04:** The system shall enforce role-based access control (RBAC) on all functions and data objects.
*   **NFR-SEC-05:** All interactions with the MSS shall use authenticated sessions (method TBD - see Undecided Issues).

#### 5.4 Software Quality Attributes
*   **Reliability:** The job monitoring system shall accurately reflect the state of jobs on the compute cluster.
*   **Usability:** The workflow for creating a first project shall be guided for new users. Error messages shall be clear and suggest corrective actions.
*   **Maintainability:** The system shall log all significant actions (logins, job submissions, file transfers) for auditing and debugging.

### 6. Other Requirements

#### 6.1 Database Requirements
A relational database shall store the metadata and relationships for the domain data elements:
*   User Account
*   Data Object
*   Project (Daymet/BiomeBGC)
*   Model Output
*   System Template
*   Compute Job
*(See Section "Domain Data Elements" in the input summary for key fields).*

#### 6.2 Undecided Issues & Open Questions
1.  The specific onboarding workflow for new users needing to create initial data objects.
2.  Detailed functional specs for data subsetting operations during download.
3.  The definitive native file formats for DEM and Analysis Mask datasets.
4.  The implementation details and UI design for advanced Visualization and Evaluation projects.
5.  The policy and mechanism for user resource quotas and compute node setting controls.
6.  The authentication method with the NCAR MSS (proxy credential vs. user credential delegation).

---
*This document is considered a living specification and may be updated as development progresses and requirements are clarified.*