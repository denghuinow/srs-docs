# Software Requirements Specification (SRS)
## Grid-BGC Application Version 1.0

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Grid-BGC Application Version 1.0. It serves as a formal agreement between the project stakeholders (scientists, administrators, developers) and the development team, providing a comprehensive blueprint for the system's design, implementation, and validation.

#### 1.2 Scope
The Grid-BGC Application is a grid-based software infrastructure designed to support bio-geochemical (BGC) modeling. Its core purpose is to provide a web portal interface that enables scientists to:
*   Prepare and manage input data for the Daymet surface weather interpolation engine and the Biome-BGC model.
*   Configure and execute modeling runs on remote computational resources via the Globus toolkit.
*   Manage, share, and access the output data from these simulations.

The system will handle user authentication, data dependency management, job lifecycle management, and integration with the NCAR Mass Storage System (MSS). Features explicitly **out of scope** for Version 1.0 include:
*   Detailed field-level data validation during data merge operations.
*   Comprehensive data visualization and analysis features (marked as low priority).
*   Implementation of user resource quotas (unless development time permits).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **BGC:** Bio-GeoChemical
*   **CRUD:** Create, Read, Update, Delete
*   **Globus:** Globus Toolkit, a set of software components for grid computing.
*   **MSS:** Mass Storage System (NCAR's persistent storage infrastructure).
*   **NCAR:** National Center for Atmospheric Research.
*   **PFT:** Plant Functional Type (a Biome-BGC model parameter).
*   **SLA:** Service Level Agreement
*   **SRS:** Software Requirements Specification

#### 1.4 References
*   NCAR Security Policy Documentation
*   Globus Toolkit Documentation
*   Daymet Model Documentation
*   Biome-BGC Model Documentation

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its stakeholders, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements. Appendices may contain supplementary diagrams or data models.

### 2. Overall Description

#### 2.1 Product Perspective
The Grid-BGC Application is a self-contained web portal that acts as a middleware layer between end-users and high-performance computing (HPC) resources. It integrates with several external systems:
*   **NCAR Gatekeeper:** For user authentication and identity management.
*   **Globus Toolkit & Grid Compute Nodes:** For secure job submission and management.
*   **NCAR Mass Storage System (MSS):** For persistent, reliable storage of all scientific data.
*   **User Web Browser:** The primary client interface.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Priority |
| :--- | :--- | :--- |
| **Scientist** | Primary user. Expert in BGC modeling. Creates data, configures and runs simulations, analyzes results. Requires an intuitive workflow for complex model configuration. | **High (Favored)** |
| **Portal Administrator** | Manages system health, user accounts, and active jobs. Requires tools for monitoring, intervention, and configuration. Technical proficiency assumed. | **High** |
| **Data User** | Secondary researcher. Accesses and downloads output data from completed runs but does not initiate simulations. Requires reliable data discovery and access controls. | **Low** |

#### 2.3 Operating Environment
*   **Server:** Application hosted on a web server compatible with the chosen development stack (e.g., Java/Python). Must integrate with NCAR's security and network infrastructure.
*   **Client:** Web browsers including Internet Explorer 6.0, Netscape 7.1, and Safari 1.2.1. Requires cookie support.
*   **External Systems:** NCAR Gatekeeper, Globus Toolkit (v4.x+), NCAR MSS, and the Hemisphere Linux compute cluster (or similar).

#### 2.4 Design and Implementation Constraints
1.  Security authentication must delegate to the NCAR Gatekeeper system.
2.  All persistent data storage must use the NCAR MSS.
3.  Job submission and management must be performed via the Globus Toolkit.
4.  The user interface must be a web portal accessible via specified browsers.
5.  The data model must enforce referential integrity and state-based rules to preserve scientific provenance.

#### 2.5 Assumptions and Dependencies
*   Assumes stable and available NCAR Gatekeeper, MSS, and Globus services.
*   Assumes the Daymet and Biome-BGC model executables are available and compatible with the target compute resources.
*   Development depends on timely clarification of "Undecided Issues" (see Section 6).

### 3. System Features and Requirements

#### 3.1 Feature: User Account Management
**Description:** The system shall manage user accounts, including application, approval, authentication, and role-based access.

**3.1.1 Functional Requirement: FR-ACM-01 (Account Application)**
*   **Priority:** High
*   **Description:** A new visitor shall be able to apply for a portal account.
*   **Input:** User's NCAR Gatekeeper username, full name, email address, and justification.
*   **Processing:** The system shall validate the Gatekeeper username format and create a local user record.
*   **Output:** The user account shall be created with a status of "Pending Approval". A notification shall be sent to the Portal Administrator.

**3.1.2 Functional Requirement: FR-ACM-02 (Account Approval/Rejection)**
*   **Priority:** High
*   **Description:** A Portal Administrator shall be able to approve or reject pending user accounts.
*   **Input:** Administrator's action (Approve/Reject) on a specific pending account.
*   **Processing:** The system shall update the user account status to "Active" (if approved) or "Rejected" (if rejected) and log the action.
*   **Output:** The user's status is updated. If approved, the user receives a notification and can log in. If rejected, the user is notified.

**3.1.3 Functional Requirement: FR-ACM-03 (Authentication & Lockout)**
*   **Priority:** High
*   **Description:** Users shall authenticate via the NCAR Gatekeeper. Three consecutive failed login attempts shall lock the portal account.
*   **Input:** User credentials (username/password).
*   **Processing:** Credentials are passed to the Gatekeeper for validation. Failed attempts are counted per user session.
*   **Output:** On success, a session is established. On the third consecutive failure, the local account status is set to "Locked", requiring administrator intervention (FR-ACM-04) to unlock.

#### 3.2 Feature: Data Object Lifecycle Management
**Description:** The system shall manage the creation, storage, sharing, and state-driven modification/deletion of all data Objects (e.g., Surface Observation, Site Data, PFT, Output Data).

**3.2.1 Functional Requirement: FR-DATA-01 (Object State Model)**
*   **Priority:** High
*   **Description:** Every data Object shall have a state: `Unlocked`, `Locked`, or `Invalidated`. State transitions shall be enforced by the system.
*   **Rules:**
    *   `Unlocked`: Object is not referenced by any locked Project. It can be modified or deleted.
    *   `Locked`: Object is referenced by at least one Project with a state of `Submitted`, `Running`, or `Completed`. It cannot be modified.
    *   `Invalidated`: A previously `Locked` Object was modified or deleted by its owner (cascading action). All Projects referencing it are marked `Invalidated`.

**3.2.2 Functional Requirement: FR-DATA-02 (Modification of Locked Object)**
*   **Priority:** High
*   **Description:** The system shall prevent the direct modification of a `Locked` Object.
*   **Input:** User request to edit a `Locked` Object.
*   **Processing:** System checks Object state. If `Locked`, the edit action is blocked.
*   **Output:** User is presented with a message: "This object is locked because it is used in project(s) [List]. To modify it, you must first create a new copy."

**3.2.3 Functional Requirement: FR-DATA-03 (Deletion of Locked Object)**
*   **Priority:** High
*   **Description:** A user may delete a `Locked` Object only by explicitly agreeing to delete all dependent Projects.
*   **Input:** User request to delete a `Locked` Object.
*   **Processing:** System identifies all Projects (`Submitted`, `Running`, `Completed`) that reference the Object.
*   **Output:** User is presented with a confirmation dialog listing all dependent Projects. Upon confirmation, the Object and all listed Projects (and their associated Output Data and Model Runs) are permanently deleted from the database and MSS.

**3.2.4 Functional Requirement: FR-DATA-04 (Object Sharing)**
*   **Priority:** Medium
*   **Description:** The owner of an Object shall be able to grant `read` or `read/write` access to other specific portal users.
*   **Input:** Owner selects an Object, a target user, and a permission level.
*   **Processing:** System creates a `Shared Access` record linking the Object, User, and permission.
*   **Output:** The target user can now see and (depending on permission) potentially use the Object in their own Projects.

#### 3.3 Feature: Daymet Modeling Pipeline
**Description:** The system shall enable Scientists to configure and execute Daymet model runs.

**3.3.1 Functional Requirement: FR-DAY-01 (Project Creation)**
*   **Priority:** High
*   **Description:** A Scientist shall be able to create a new Project of type "Daymet".
*   **Input:** Project name, description, and selection of required, unlocked input Objects (Surface Observation [List], Site Data [Grid], Projection, etc.).
*   **Processing:** System validates that referenced Objects are of the correct type and are `Unlocked`.
*   **Output:** A new `Daymet` Project record is created in a `Draft` state.

**3.3.2 Functional Requirement: FR-DAY-02 (Job Submission & Monitoring)**
*   **Priority:** High
*   **Description:** A Scientist shall submit a configured Daymet Project for execution on a selected computational resource.
*   **Input:** User action to submit the Project. Selection of a compute resource from an administrator-configured list.
*   **Processing:**
    1.  System locks all referenced input Objects and changes Project state to `Submitted`.
    2.  System packages input files, model executable, and configuration into a job.
    3.  System uses Globus Toolkit to submit the job to the selected resource.
    4.  System creates a `Model Run` record and begins polling for status.
*   **Output:** A `Model Run` is initiated. The user is redirected to a monitoring page where job status (Pending, Running, Tile X of Y, Completed, Failed) is updated at least every 60 seconds.

**3.3.3 Functional Requirement: FR-DAY-03 (Output Handling)**
*   **Priority:** High
*   **Description:** Upon successful completion of a Daymet Model Run, the system shall automatically create an Output Data Object.
*   **Input:** Notification (via Globus or polling) that the job completed successfully.
*   **Processing:** System retrieves output files from the compute node, transfers them to the MSS, and creates an `Output Data` Object of type `Grid` linked to the Model Run.
*   **Output:** A new `Locked` Output Data Object appears in the user's workspace. The Project state changes to `Completed`.

#### 3.4 Feature: BiomeBGC Modeling Pipeline
**Description:** The system shall enable Scientists to configure and execute more complex BiomeBGC model runs, including topology configuration.

**3.4.1 Functional Requirement: FR-BGC-01 (Advanced Object Configuration)**
*   **Priority:** High
*   **Description:** A Scientist shall be able to create and manage BiomeBGC-specific Parameterization Objects: `Plant Functional Type (PFT)` and `Disturbance`.
*   **Input:** Object name, description, and model-specific parameter values (e.g., for Disturbance: type, year, intensity).
*   **Processing:** System stores the parameter set as a new `Parameterization` type Object.
*   **Output:** A new Object is available for use in BiomeBGC Projects.

**3.4.2 Functional Requirement: FR-BGC-02 (Topology Configuration)**
*   **Priority:** High
*   **Description:** When creating a BiomeBGC Project, the Scientist shall define a topology (e.g., Site Specific PFT List) mapping geographic sites to specific PFTs.
*   **Input:** Selection of a Site Data `Grid` Object and assignment of one or more PFT `Parameterization` Objects to its constituent sites.
*   **Processing:** System stores the topology configuration as part of the Project definition.
*   **Output:** Project is configured for a spatially variable simulation.

**3.4.3 Functional Requirement: FR-BGC-03 (Job Execution)**
*   **Priority:** High
*   **Description:** The system shall submit, monitor, and handle output for BiomeBGC jobs, analogous to FR-DAY-02 and FR-DAY-03, but using BiomeBGC-specific job packaging.
*   *Note: Inherits core behavior from Daymet features but uses different model executables and input structures.*

#### 3.5 Feature: Administrative Operations
**Description:** The system shall provide tools for the Portal Administrator to manage the system and users.

**3.5.1 Functional Requirement: FR-ADMIN-01 (Job Monitoring & Termination)**
*   **Priority:** High
*   **Description:** A Portal Administrator shall be able to view all active Model Runs and terminate any run.
*   **Input:** Administrator selects a `Running` or `Pending` Model Run and chooses "Terminate".
*   **Processing:** System uses Globus to issue a termination command to the remote resource. It then cleans up temporary files and sets the Model Run and associated Project states to `Failed` or `Terminated`.
*   **Output:** The job is stopped. Associated temporary files on the compute node and MSS are deleted.

**3.5.2 Functional Requirement: FR-ADMIN-02 (System Consistency Check)**
*   **Priority:** Medium
*   **Description:** A Portal Administrator shall be able to execute a tool that verifies the integrity of the database records against the physical files in the MSS.
*   **Input:** Administrator initiates the check.
*   **Processing:** System scans database records for file paths (pointers) and verifies the corresponding files exist in the MSS.
*   **Output:** A report is generated listing any orphaned database records (file missing in MSS) or orphaned files in MSS (no database record).

**3.5.3 Functional Requirement: FR-ADMIN-03 (Dashboard)**
*   **Priority:** Medium
*   **Description:** The Administrator portal shall include a dashboard displaying key metrics.
*   **Input:** N/A (automatic aggregation).
*   **Processing:** System aggregates data from User, Project, Model Run, and storage tables.
*   **Output:** Dashboard displays: Total/Active user counts, counts of Projects/Runs by state, total storage used, and recent system activity.

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **P1:** The web portal shall load listing pages (e.g., "My Objects", "My Projects") within **5 seconds** under normal operational load (≤50 concurrent users).
*   **P2:** The status of a running Model Run (e.g., "Tile 45/100") shall be updated and visible on the user's monitoring page at least every **60 seconds**.
*   **P3:** File upload progress shall be indicated to the user. The system shall handle large (>1GB) file uploads asynchronously without browser timeout.

#### 4.2 Reliability & Availability
*   **R1:** The system shall maintain **99% uptime** during standard business hours (8 AM - 6 PM, Mountain Time, Monday-Friday), excluding scheduled maintenance.
*   **R2:** The system shall enforce data integrity constraints to prevent changes to the input data of `Completed` runs, ensuring scientific reproducibility.
*   **R3:** All critical operations (job submission, file transfer to MSS) shall include retry logic and comprehensive error logging.

#### 4.3 Security Requirements
*   **S1:** All authentication traffic between the user's browser and the portal shall be encrypted (using HTTPS/SSL).
*   **S2:** User authorization shall be managed via a combination of NCAR Gatekeeper roles and internal portal roles (`Scientist`, `Data User`, `Administrator`).
*   **S3:** Direct access to the MSS and compute resources shall be mediated by the portal; user credentials shall not be exposed to these backend systems (proxying or service account model TBD per Undecided Issue #2).

#### 4.4 Usability
*   **U1:** The user interface for creating a BiomeBGC Project topology shall include guided workflows and sensible defaults to manage complexity.
*   **U2:** All user actions with irreversible consequences (e.g., deleting a locked Object, terminating a run) shall require explicit confirmation.

#### 4.5 Observability & Supportability
*   **O1:** The system shall log all user actions (CRUD on Objects/Projects, job submission), administrative actions, and system errors for audit and debugging purposes.
*   **O2:** Portal Administrators shall have access to the metrics dashboard (FR-ADMIN-03) and system consistency check tool (FR-ADMIN-02).

### 5. Acceptance Criteria (Summary)
The following high-level scenarios must pass for Version 1.0 to be accepted:
1.  A new user can apply for an account, be approved by an administrator, and log in successfully.
2.  A Scientist can create the necessary input Objects, assemble them into a Daymet Project, submit it, monitor its tile-by-tile progress, and successfully retrieve the output.
3.  A Scientist can configure PFT and Disturbance Objects, define a site-specific topology, and execute a BiomeBGC run to completion.
4.  An attempt to edit a `Locked` Object is prevented by the system.
5.  A Portal Administrator can terminate an active user's job, resulting in proper cleanup.
6.  The system consistency check tool identifies and reports missing file references.

### 6. Undecided Issues & Open Questions
The following items require resolution by the designated parties prior to or during detailed design/implementation:
1.  **Specific file formats and archive structures for user-uploaded data (e.g., for Surface Observation, Site Data).** (Responsible: System Architect / Scientist Liaison)
2.  **Mechanism for MSS access: using user's portal credentials or proxying through a central account.** (Responsible: System Architect / NCAR Security)
3.  **Detailed specification of the "subset" operation for creating new Objects from existing ones.** (Responsible: UI Designer / Scientist Liaison)
4.  **Native data formats for the Daymet and BiomeBGC models that the system must support.** (Responsible: Scientist Liaison)
5.  **Complete list of general system configuration settings controllable by the Portal Administrator.** (Responsible: Product Owner)
6.  **Definition and implementation details for Site Specific PFT List topology in BiomeBGC projects.** (Responsible: Scientist Liaison)
7.  **Validation ranges or rules for data values in Disturbance Objects (e.g., fire intensity).** (Responsible: Scientist Liaison)
8.  **Detailed design and requirements for Visualization and Evaluation Projects (marked TBD for future versions).** (Responsible: Product Owner / Scientist Liaison)

---
*[End of Document]*