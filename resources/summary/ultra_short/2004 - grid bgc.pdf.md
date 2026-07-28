**Purpose & Scope**
The system is a grid-based software infrastructure for bio-geochemical modeling. It provides a graphical interface to run Daymet and Biome-BGC simulations, manage input/output data, and visualize results. It does not handle user password management or enforce spatial data validation during merge operations.

**Product Background / Positioning**
The application is a web portal integrated into the NCAR Dataportal Web Server. It utilizes the Globus toolkit and remote compute resources (Hemisphere Linux cluster) to execute modeling jobs, with all file storage on the NCAR Mass Storage System (MSS).

**Core Functional Overview**
*   User account management tied to NCAR Gatekeeper authentication.
*   Creation and management of data objects (List, Grid, Parameterization types) and simulation projects.
*   Execution, monitoring, and control of Daymet and BiomeBGC model runs on remote compute resources.
*   Sharing of data objects and use of expert templates.
*   Download of model output data in native formats.
*   Administrative functions for user, job, and system resource management.

**Key Users & Usage Scenarios**
*   **Scientists (Primary):** Manage data, configure and run simulations, visualize results, and share data.
*   **Portal Administrators:** Manage user accounts, monitor/terminate jobs, and oversee system operations.
*   **Data Users (Low Priority):** Access and download shared simulation output.
Typical scenarios include setting up and running a Daymet or BiomeBGC modeling run, visualizing outputs, and downloading data for further analysis.

**Major External Interfaces**
*   **User Interface:** A web-based portal compatible with specified browsers (IE 6.0, Netscape 7.1, Safari 1.2.1), requiring cookies.
*   **Hardware Interface:** Integration with the NCAR Mass Storage System for all file storage.
*   **Software Interface:** Dependence on the NCAR Gatekeeper system for user authentication.
*   **Communication Interface:** Use of the Globus toolkit for grid communications.

**Key Non-functional Requirements**
*   **Security:** Must comply with NCAR security policies. User accounts lock after 3 failed login attempts. All login actions use secure data channels.
*   **Reliability/Data Integrity:** The system must prevent changes to objects/projects used in a model run to preserve input/output consistency, enforcing locked/invalidated states.
*   **Maintainability:** The portal admin must be able to validate file reference consistency and manage compute node resources (add, lock, unlock).

**Constraints, Assumptions & Dependencies**
*   Must use the Globus toolkit.
*   Must use the NCAR Mass Storage System for all file storage.
*   All users must have a valid NCAR Gatekeeper account.
*   Depends on the NCAR Gatekeeper system for user authentication and information.
*   Assumes integration with the specified Dataportal Web Server and Hemisphere Linux cluster.

**Priorities & Acceptance Approach**
*   Scientists are the favored user class; Data Users are the lowest priority.
*   Visualization for several object types is marked as low priority.
*   Acceptance is implicitly based on fulfilling the specified functional flows (e.g., successful model run execution, data sharing, administrative controls) and adhering to the stated constraints (e.g., using MSS, Globus).