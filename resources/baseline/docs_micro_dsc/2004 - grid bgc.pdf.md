# Software Requirements Specification (SRS)
## For the Bio-Geochemical Simulation Web Portal

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Bio-Geochemical Simulation Web Portal. This portal will provide scientists with a unified interface to manage data, execute simulations using the Daymet and Biome-BGC models, and share results, leveraging grid computing resources and specific institutional infrastructure. The intended audience for this document includes project stakeholders, software developers, system architects, and quality assurance teams.

#### 1.2 Scope
The system will be a web-based portal that enables authenticated scientists to:
*   Securely manage their user profiles and data objects.
*   Prepare, submit, monitor, and manage bio-geochemical simulation jobs (Daymet and Biome-BGC) on backend grid computing resources.
*   Store, retrieve, share, and download all simulation-related data via the NCAR Mass Storage System (MSS).
*   Facilitate collaboration through controlled data sharing mechanisms.

**Out-of-Scope:**
*   Development or modification of the core Daymet or Biome-BGC scientific models.
*   Administration of the underlying grid computing resources or the NCAR MSS.
*   Provisioning of NCAR Gatekeeper accounts to end-users.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **BGC:** Bio-GeoChemical
*   **Biome-BGC:** A model that simulates the storage and flux of water, carbon, and nitrogen within terrestrial ecosystems.
*   **Daymet:** A model providing gridded estimates of daily weather parameters.
*   **Globus Toolkit:** A set of open-source software tools for grid computing, including security (GSI), data management (GridFTP), and job submission (GRAM).
*   **GRAM:** Grid Resource Allocation and Management component of the Globus Toolkit.
*   **GSI:** Grid Security Infrastructure, part of the Globus Toolkit.
*   **MSS:** Mass Storage System (NCAR's hierarchical storage management system).
*   **NCAR:** National Center for Atmospheric Research.
*   **SRS:** Software Requirements Specification.

#### 1.4 References
1.  Globus Toolkit Documentation
2.  NCAR Mass Storage System User Guide
3.  Biome-BGC Model Theory and User Manual
4.  Daymet Daily Surface Weather Data Documentation

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details specific system requirements, including external interfaces, functional capabilities, and non-functional attributes.

### 2. Overall Description

#### 2.1 Product Perspective
The portal is a new, self-contained web application that will act as a middleware layer between the scientist user and complex backend infrastructure. It will integrate with the following external systems:
*   **NCAR Authentication Services:** For user verification via Gatekeeper accounts.
*   **Globus Toolkit Services:** For secure job submission (GRAM) and potentially data transfer (GridFTP) to grid resources.
*   **NCAR Mass Storage System (MSS):** As the primary and sole repository for all user data, model inputs, and simulation outputs.
*   **Backend Grid Compute Resources:** Where the Daymet and Biome-BGC model executables will run.

#### 2.2 Product Functions
The major functions of the portal are:
1.  **User Management:** Authentication, authorization, and profile management.
2.  **Data Object Management:** CRUD (Create, Read, Update, Delete) operations for surface observations, site data, and other simulation inputs/outputs stored in MSS.
3.  **Simulation Workflow Management:** Configuration, validation, submission, monitoring, and termination of Daymet and Biome-BGC simulation runs on grid resources.
4.  **Data Sharing & Collaboration:** Controlled sharing of data objects and simulation results with other portal users.
5.  **Data Transfer:** Downloading output data from MSS to the user's local machine via the web interface.

#### 2.3 User Characteristics
*   **Primary User (Scientist):** Possesses domain expertise in bio-geochemistry or ecology but may have varying levels of computational proficiency. Has a valid NCAR Gatekeeper account. Expects a reliable, intuitive interface to manage complex simulations without needing deep knowledge of the underlying grid infrastructure.
*   **System Administrator:** Manages portal configuration, user roles, and monitors system health. Has administrative privileges on the portal and knowledge of Globus and MSS.

#### 2.4 Constraints
1.  **Technical:** The system **must** be built using the Globus Toolkit for grid security and job management.
2.  **Architectural:** All persistent file storage **must** be performed on the NCAR Mass Storage System (MSS). The portal itself must not maintain a separate file store.
3.  **Policy:** Access to the portal is restricted to users with valid NCAR Gatekeeper accounts.
4.  **Regulatory:** The system must comply with NCAR's security and data management policies.

#### 2.5 Assumptions and Dependencies
*   The Daymet and Biome-BGC model executables are pre-installed, configured, and accessible on the target grid computing resources.
*   The NCAR MSS and Globus services are available and operational.
*   Users obtain their NCAR Gatekeeper accounts through processes external to this portal.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **UI 1:** Responsive Web Interface. The primary portal shall be accessed via a modern web browser (Chrome, Firefox, Safari, Edge). It shall include:
    *   A dashboard for job and data overview.
    *   Forms for configuring simulation parameters.
    *   Interactive tables and lists for managing data objects and jobs.
    *   Visual progress indicators for running jobs.
    *   A mechanism for browsing and selecting files from the user's MSS space.

##### 3.1.2 Hardware Interfaces
*   **HI 1:** The portal application server shall interface with NCAR's backend grid computing resources via the Globus GRAM protocol.

##### 3.1.3 Software Interfaces
*   **SI 1: Globus Toolkit (GRAM/GSI).** The portal shall use the Globus Toolkit to authenticate users (leveraging Gatekeeper credentials via GSI), submit jobs to grid resources, and query job status.
*   **SI 2: NCAR MSS API/Client.** The portal shall integrate with the NCAR MSS using its official client libraries or command-line tools (e.g., `msread`, `mswrite`, `msls`) to perform all file operations (store, retrieve, list, delete).
*   **SI 3: NCAR Authentication Service.** The portal shall interface with NCAR's authentication service to validate user Gatekeeper credentials at login.

##### 3.1.4 Communications Interfaces
*   **CI 1:** All communication between the user's browser and the web portal shall be encrypted using HTTPS/TLS 1.2 or higher.
*   **CI 2:** Communication between the portal and Globus/Grid services shall use standard GSI-secured protocols.

#### 3.2 Functional Requirements

##### 3.2.1 User Management (UM)
*   **UM-1:** The system shall allow a user to log in using their NCAR Gatekeeper credentials.
*   **UM-2:** The system shall allow a logged-in user to view and update their personal profile information (e.g., name, email, affiliation).
*   **UM-3:** The system shall maintain role-based access (Scientist, Admin).

##### 3.2.2 Data Object Management (DM)
*   **DM-1:** The system shall allow a user to upload a file from their local machine for storage in their personal workspace on the NCAR MSS.
*   **DM-2:** The system shall provide a user with a browsable list of their data objects (files and directories) stored in the MSS.
*   **DM-3:** The system shall allow a user to delete data objects from their MSS workspace via the portal.
*   **DM-4:** The system shall allow a user to apply metadata tags (e.g., project, site, data type) to data objects.

##### 3.2.3 Simulation Job Management (JM)
*   **JM-1:** The system shall provide a form for users to configure a new simulation run, selecting either the Daymet or Biome-BGC model.
*   **JM-2:** The configuration form shall allow the user to specify input parameters and select input data files from their MSS workspace.
*   **JM-3:** The system shall validate the job configuration before submission.
*   **JM-4:** The system shall submit the validated job to the appropriate grid resource via the Globus GRAM interface.
*   **JM-5:** The system shall provide a real-time dashboard view showing the status (e.g., Pending, Running, Completed, Failed) of all user-submitted jobs.
*   **JM-6:** The system shall allow a user to terminate a running job.
*   **JM-7:** Upon job completion, the system shall automatically move standard output, standard error, and model output files to a designated location in the user's MSS workspace.

##### 3.2.4 Data Sharing and Download (SD)
*   **SD-1:** The system shall allow a user to share a specific data object or directory from their MSS workspace with another registered portal user.
*   **SD-2:** The system shall allow a user to set sharing permissions (Read-Only).
*   **SD-3:** The system shall provide a user with a list of data objects shared with them by others.
*   **SD-4:** The system shall allow a user to initiate a download of a data object from the MSS to their local machine via the web browser.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance
*   **PER-1:** The portal web interface shall load the user dashboard within 3 seconds under normal load.
*   **PER-2:** Job status updates on the dashboard shall be refreshed at least every 30 seconds without requiring a full page reload.
*   **PER-3:** Listing files from a user's MSS workspace shall complete within 10 seconds for directories containing up to 1000 items.

##### 3.3.2 Security
*   **SEC-1:** All user sessions shall expire after 12 hours of inactivity.
*   **SEC-2:** User credentials shall never be stored in plain text within the portal's database.
*   **SEC-3:** Direct access to MSS files shall be scoped strictly to the user's own files and those explicitly shared with them.

##### 3.3.3 Reliability & Availability
*   **REL-1:** The portal shall have a target availability of 99.5% during core business hours (8 AM - 6 PM, Mountain Time, weekdays).
*   **REL-2:** Submitted job metadata shall be persisted such that no job information is lost if the portal application restarts.

##### 3.3.4 Usability
*   **USA-1:** A new user with a valid account shall be able to submit a basic simulation job following a provided tutorial within 15 minutes of first login.
*   **USA-2:** The portal shall provide contextual help and tooltips for all major configuration parameters.

---
*Document End*