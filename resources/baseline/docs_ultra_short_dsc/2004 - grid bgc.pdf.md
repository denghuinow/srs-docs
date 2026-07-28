# Software Requirements Specification (SRS)
## Bio-Geochemical Modeling Grid Portal (BGC-Portal)

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review  
**Authors:** [SRS Generation System]

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Bio-Geochemical Modeling Grid Portal (BGC-Portal). The intended audience includes project stakeholders, software developers, testers, system administrators, and portal end-users. This SRS serves as the definitive specification for system development, testing, and acceptance.

#### 1.2 Scope
The BGC-Portal is a grid-based software infrastructure providing a web-accessible graphical interface for configuring, executing, and analyzing bio-geochemical model simulations (specifically Daymet and Biome-BGC). The system facilitates data object management, remote job execution on high-performance computing resources, result visualization, and data sharing within a scientific community.

**In-Scope:**
*   User authentication via NCAR Gatekeeper.
*   Management of simulation data objects (List, Grid, Parameterization).
*   Creation, configuration, and management of simulation projects.
*   Submission, monitoring, and control of model runs on the Hemisphere Linux cluster via the Globus toolkit.
*   Storage and retrieval of all data files via the NCAR Mass Storage System (MSS).
*   Visualization of model input and output data.
*   Sharing of data objects and projects among users.
*   Administrative management of users, jobs, and system resources.
*   Download of output data in native model formats.

**Out-of-Scope:**
*   User password management (delegated to NCAR Gatekeeper).
*   Spatial data validation during merge operations of data objects.
*   Direct user management of the Hemisphere cluster or MSS outside the portal's defined interfaces.
*   Creation or modification of the underlying Daymet or Biome-BGC model source code.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **BGC:** Bio-Geochemical
*   **MSS:** NCAR Mass Storage System
*   **Globus:** Globus Toolkit for grid computing
*   **Gatekeeper:** NCAR Gatekeeper authentication system
*   **Daymet:** A model for generating surfaces of daily weather parameters.
*   **Biome-BGC:** A model for simulating biogeochemical and hydrologic processes.
*   **Object:** A data entity within the portal (e.g., Site List, Parameterization Set).
*   **Project:** A container for objects and configuration defining a simulation run.

#### 1.4 References
*   NCAR Security Policy Documentation
*   Globus Toolkit Documentation
*   NCAR MSS Interface Specifications
*   NCAR Gatekeeper API Documentation

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general product description. Section 3 details specific functional requirements. Section 4 outlines external interface requirements. Section 5 specifies non-functional requirements. Section 6 lists other relevant project factors.

### 2. Overall Description

#### 2.1 Product Perspective
The BGC-Portal is a component integrated into the existing NCAR Dataportal Web Server ecosystem. It acts as a middleware layer between the scientist user and complex grid resources.

**System Interfaces:**
*   **Front-end:** User's Web Browser
*   **Back-end:** NCAR Dataportal Web Server
*   **Authentication:** NCAR Gatekeeper
*   **Compute:** Hemisphere Linux Cluster (via Globus GRAM)
*   **Storage:** NCAR Mass Storage System (via GridFTP/other MSS interfaces)
*   **Grid Middleware:** Globus Toolkit (Security, Data Management, Resource Management)

#### 2.2 Product Functions (Summary)
1.  Authenticate users via NCAR Gatekeeper.
2.  Provide CRUD (Create, Read, Update, Delete) operations for data objects and simulation projects.
3.  Submit configured simulation projects as jobs to the remote Hemisphere cluster.
4.  Monitor job status (Queued, Running, Completed, Failed) and provide controls (Pause, Terminate).
5.  Manage input/output file staging to/from the MSS.
6.  Generate visualizations for key data objects and model outputs.
7.  Enable sharing of objects/projects with other portal users.
8.  Provide administrative panels for system oversight.
9.  Allow download of result data files.

#### 2.3 User Characteristics
| User Class | Expertise | Primary Goals | Priority |
| :--- | :--- | :--- | :--- |
| **Scientist** | Domain expert in ecology, biogeochemistry, or climatology. Moderate computer literacy. | Configure and run simulations, analyze results, manage personal/team data. | **High** |
| **Portal Administrator** | Expert in system administration and the portal software. | Manage user accounts, monitor system health, control jobs, manage compute resources. | **High** |
| **Data User** | Scientist or student interested in results. | Find, view, and download shared simulation output data. | **Low** |

#### 2.4 Constraints
1.  **Technical:** Must utilize the Globus Toolkit for all grid communications.
2.  **Technical:** Must use the NCAR Mass Storage System (MSS) as the sole persistent file store.
3.  **Policy:** Must comply with all applicable NCAR security policies.
4.  **Infrastructure:** All users must possess a valid NCAR Gatekeeper account.
5.  **Browser Compatibility:** The web interface must be compatible with Internet Explorer 6.0, Netscape 7.1, and Safari 1.2.1, and require cookie support.

#### 2.5 Assumptions and Dependencies
*   The NCAR Gatekeeper system will be available and provide reliable authentication services.
*   The Hemisphere Linux cluster will be available and configured to accept jobs via Globus.
*   The NCAR MSS will be available and accessible with sufficient quota for users.
*   The NCAR Dataportal Web Server infrastructure will host the portal application.
*   The Daymet and Biome-BGC model executables are pre-installed and configured on the compute cluster.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 User Authentication (AUTH)**
*   **AUTH-1:** The system shall authenticate users exclusively through the NCAR Gatekeeper system.
*   **AUTH-2:** The system shall lock a user's portal account for a defined period after 3 consecutive failed login attempts.
*   **AUTH-3:** All credential transmission during login shall occur over a secure (SSL/TLS) data channel.

**3.1.2 Data Object Management (OBJ)**
*   **OBJ-1:** The system shall allow Scientists to create, view, edit, and delete data objects of type: `List`, `Grid`, and `Parameterization`.
*   **OBJ-2:** When a data object is used as input to a submitted simulation job, the system shall mark it as `LOCKED`, preventing edits or deletion until the job reaches a final state (Completed, Failed, Terminated).
*   **OBJ-3:** The system shall allow Scientists to share data objects with other individual users or publicly.
*   **OBJ-4:** The system shall provide "Expert Templates" – pre-configured, read-only objects that can be copied by users as a starting point.

**3.1.3 Simulation Project Management (PROJ)**
*   **PROJ-1:** The system shall allow Scientists to create a Project, which aggregates one or more data objects and model configuration parameters.
*   **PROJ-2:** The system shall enforce consistency: if a component object of a Project is modified, the Project shall be marked as `INVALID` and must be reconfigured before it can be run.
*   **PROJ-3:** Scientists shall be able to save, clone, and share Projects.

**3.1.4 Job Execution and Control (JOB)**
*   **JOB-1:** The system shall submit a valid Project to the Hemisphere cluster for execution using the Globus Resource Allocation Manager (GRAM).
*   **JOB-2:** The system shall stage all necessary input files from the MSS to the cluster's scratch space prior to job execution.
*   **JOB-3:** The system shall monitor job status (via Globus) and provide real-time status updates (Queued, Running, Completed, Failed).
*   **JOB-4:** The system shall allow the submitting Scientist or an Administrator to terminate a running or queued job.
*   **JOB-5:** Upon job completion, the system shall stage output files from the cluster scratch space back to the user's designated area on the MSS.

**3.1.5 Visualization and Data Access (VIZ)**
*   **VIZ-1:** The system shall provide graphical visualizations for `List` and `Grid` object types. *(Priority: Low)*
*   **VIZ-2:** The system shall provide basic visualizations (e.g., time-series charts, summary statistics) for standard model outputs.
*   **VIZ-3:** Scientists and Data Users shall be able to download the raw output files (in their native format) from the MSS via the portal.

**3.1.6 Administrative Functions (ADMIN)**
*   **ADMIN-1:** The Administrator shall be able to view, enable, disable, and delete user portal accounts (linked to Gatekeeper IDs).
*   **ADMIN-2:** The Administrator shall be able to view all jobs in the system and terminate any job.
*   **ADMIN-3:** The Administrator shall be able to add, lock, and unlock compute node resources (Hemisphere cluster nodes) available to the portal.
*   **ADMIN-4:** The Administrator shall be able to run a utility to validate internal file reference consistency (e.g., check for orphaned files on MSS, broken links in the portal database).

#### 3.2 External Interface Requirements

**3.2.1 User Interfaces**
*   The interface shall be a web portal accessible via the specified browsers.
*   The portal shall use a consistent, intuitive layout with clear navigation for Scientists.
*   Administrative functions shall be contained in a separate, access-controlled section of the portal.

**3.2.2 Hardware Interfaces**
*   The system shall interact with the NCAR MSS for all persistent file I/O operations.

**3.2.3 Software Interfaces**
*   **Authentication:** Interface with the NCAR Gatekeeper system via its defined API/protocol.
*   **Grid Compute:** Utilize the Globus Toolkit (v4.x assumed) for job submission, management, and file transfer.
*   **Web Server:** Operate as an application within the NCAR Dataportal Web Server environment (e.g., Apache/Tomcat).

**3.2.4 Communications Interfaces**
*   All grid communication (job management, file transfer) shall use protocols provided by the Globus Toolkit (e.g., GridFTP, GRAM).

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   Portal page load times for Scientists shall be under 3 seconds for standard operations under typical load.
*   Job status updates shall be polled and reflected in the UI within 30 seconds of a state change on the cluster.

#### 4.2 Safety Requirements
*   Not applicable.

#### 4.3 Security Requirements
*   The system shall comply with all NCAR IT security policies.
*   User sessions shall timeout after a period of inactivity (e.g., 60 minutes).
*   Direct access to MSS files shall be mediated by the portal, enforcing user ownership and sharing permissions.

#### 4.4 Software Quality Attributes

**4.4.1 Reliability & Data Integrity**
*   The system shall guarantee that input data for a running job cannot be altered, preserving reproducibility.
*   The system shall implement robust error handling for failures in grid communication (MSS, Globus) and provide clear user feedback.

**4.4.2 Maintainability**
*   The portal administration module shall provide the tools specified in ADMIN-3 and ADMIN-4 to facilitate system upkeep without direct database or filesystem manipulation.

**4.4.3 Portability**
*   The web application shall be compatible with the browsers listed in Section 2.4.

### 5. Other Requirements

#### 5.1 Priority and Release Planning
*   Requirements for **Scientists** (AUTH, OBJ, PROJ, JOB core functions) are of the highest priority.
*   Requirements for **Portal Administrators** (ADMIN) are high priority for operational stability.
*   Requirements for **Data Users** and advanced **Visualization (VIZ-1)** are of lower priority and may be deferred to later releases.

#### 5.2 Acceptance Criteria
Acceptance of the system will be based on successful demonstration of the following key flows:
1.  A Scientist can authenticate, create a Project using objects, submit it as a job, monitor its execution, visualize results, and download outputs.
2.  An Administrator can manage a user account, view all system jobs, and terminate a selected job.
3.  All data persistence is confirmed to occur on the NCAR MSS.
4.  All job execution is confirmed to occur via the Globus toolkit on the Hemisphere cluster.
5.  The security requirements, particularly account lockout and secure login, are verified.

---
*Document End*