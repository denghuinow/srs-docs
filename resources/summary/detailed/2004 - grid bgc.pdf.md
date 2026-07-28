# Detailed Summary: Grid-BGC Application Version 1.0

## Background and Scope
This project aims to develop a grid-based software infrastructure to support bio-geochemical (BGC) modeling. The application will utilize the Daymet surface weather interpolation engine and the Biome-BGC model to generate gridded surface weather datasets and perform BGC modeling activities. The system will provide a graphical user interface (web portal) and leverage grid technologies (Globus toolkit) for secure, reliable communication with remote computing resources. Non-goals include detailed field-level data validation during merge operations, comprehensive visualization features (marked as low priority), and the implementation of resource quotas unless time permits.

## Stakeholders Matrix and Use Cases
*   **Scientist (Favored User):** Primary user who manages input data, runs simulations, visualizes results, and manages output data.
*   **Portal Administrator:** Manages day-to-day system operations, including user accounts, running jobs, and general portal settings and monitoring.
*   **Data User (Lowest Priority):** Researcher who needs to use simulation output data but does not initiate simulations.

**Main Scenarios:**
1.  A Scientist applies for an account, configures input data objects (e.g., Surface Observation, Site Data), and executes a Daymet modeling run.
2.  A Scientist configures BiomeBGC-specific objects (e.g., Plant Functional Type, Disturbance) and executes a BiomeBGC modeling run.
3.  A Scientist or Data User visualizes or downloads output data from a completed model run.
4.  A Portal Administrator approves a new user account and later monitors or terminates active user jobs.

**Exception Scenarios:**
5.  A user attempts to modify a data Object that is locked because it has been referenced in a project or shared, triggering an invalidation workflow for dependent projects.
6.  A user requests deletion of a locked Object, requiring confirmation to delete all dependent projects.
7.  A Portal Administrator runs a system consistency check to identify and correct missing file references on the storage system.
8.  A user's login fails three times, resulting in a locked account that requires administrator intervention to unlock.

## Business Process
**Main Process: Execute a Modeling Run**
1.  **Trigger:** Scientist decides to run a model (Daymet or BiomeBGC).
2.  **Input:** Scientist logs into the web portal.
3.  Scientist creates or selects the required input Objects (e.g., Surface Observation, Projection) of the correct type (List or Grid).
4.  Scientist creates a new Project (Daymet or BiomeBGC), referencing the prepared input Objects.
5.  Scientist configures the Project's simulation parameters and topology (for BiomeBGC).
6.  Scientist submits the model run, selecting a computational resource.
7.  System manages job execution on grid compute nodes, providing tile-by-tile status monitoring.
8.  **Output:** Upon completion, the system automatically creates an Output Object containing the results.

**Key Branch A: Account Creation & Approval**
1.  **Trigger:** New user applies for an account via the portal.
2.  User provides NCAR Gatekeeper username and required details.
3.  System sets account status to "Pending Approval" and notifies Portal Administrator.
4.  Portal Administrator reviews and approves (or rejects) the account, activating it.

**Key Branch B: Data Object Lifecycle & Dependency Management**
1.  **Trigger:** User attempts to modify or delete a data Object (e.g., Site Data Object).
2.  System checks the Object's state (Unlocked, Locked, Invalidated).
3.  If Locked (referenced elsewhere), the system prevents direct modification. Deletion is only allowed if the user agrees to delete all dependent Projects.
4.  Modification or deletion of a Locked Object invalidates all Projects that depend on it, changing their state and potentially deleting associated output data.

## Domain Model
Core entities manage users, data, and simulations. Key constraints include referential integrity and state-based rules to preserve data provenance.
1.  **User Account:** (Username: required, unique; Role: required; Status: required)
2.  **Object:** (ID: required, unique; Name: required; Type: required [List/Grid/Parameterization]; State: required; Owner: required, reference to User)
3.  **Project:** (ID: required, unique; Name: required; Type: required [Daymet/BiomeBGC/Visualization]; State: required; Owner: required, reference to User)
4.  **Template:** (ID: required, unique; Based on Object Type: required; Submitter: required, reference to User)
5.  **Model Run:** (ID: required, unique; Status: required; Project: required, reference to Project; Computational Resource: required)
6.  **Output Data:** (ID: required, unique; Run: required, reference to Model Run; Containing Object: required, reference to Object)
7.  **Compute Node:** (ID: required, unique; Status: required [Active/Locked])
8.  **Shared Access:** (Object/Project ID: required; User ID: required) // Manages collaboration permissions.

## Interfaces and Integrations
1.  **NCAR Gatekeeper System**
    *   **Direction:** Inbound
    *   **Interaction:** User Authentication & Account Info Retrieval
    *   **Input:** User credentials (username/password).
    *   **Output:** User authentication result and account information (name, email).
    *   **SLA:** Must adhere to NCAR security policies; account lockout handled by Gatekeeper.

2.  **NCAR Mass Storage System (MSS)**
    *   **Direction:** Outbound
    *   **Interaction:** Persistent Data Storage
    *   **Input:** All user-uploaded data files, model input files, and model output files.
    *   **Output:** File storage confirmation and retrieval of stored files.
    *   **SLA:** Reliable storage and retrieval; access method (user proxy vs. central account) TBD.

3.  **Globus Toolkit / Grid Compute Nodes**
    *   **Direction:** Outbound
    *   **Interaction:** Job Submission & Management
    *   **Input:** Packaged model run jobs (input data, executables).
    *   **Output:** Job status, stdout/stderr logs, and final output data.
    *   **SLA:** Secure job submission and monitoring; ability to terminate jobs.

4.  **Web Client (Browser)**
    *   **Direction:** Bidirectional
    *   **Interaction:** Web Portal User Interface
    *   **Input:** User actions (clicks, form entries, file uploads).
    *   **Output:** Rendered HTML pages, data listings, visualization images (low priority).
    *   **SLA:** Support for IE 6.0, Netscape 7.1, Safari 1.2.1; requires cookies.

## Acceptance Criteria
**Capability: User Account Management**
*   Given a new visitor to the portal, when they apply for an account with a valid NCAR Gatekeeper username, then the account is created in a "Pending Approval" state and the administrator is notified.
*   Given a Portal Administrator, when they approve a pending user account, then the account status changes to "Active" and the user can log in.

**Capability: Daymet Model Execution**
*   Given a Scientist with the required unlocked input Objects (Surface Observation, Site Data, etc.), when they create a Daymet Project, reference those Objects, and submit a run, then a job is launched on the selected compute resource and an Output Object is created upon successful completion.
*   Given a running Daymet model job, when the Scientist or Administrator terminates it, then all associated temporary and output files are deleted from storage.

**Capability: Data Integrity**
*   Given a Surface Observation Object that is referenced by a locked Daymet Project, when the owner tries to edit it, then the system prevents the edit and informs the user the Object is locked.
*   Given a locked BiomeBGC Output Object that is shared, when the owner deletes it and chooses to delete dependent projects, then the Object and all specified dependent projects and their data are permanently removed.

## Non-Functional Metrics
*   **Performance:** Model run job status shall be updated and visible to the user at least every 60 seconds. The portal shall load listing pages within 5 seconds under normal load.
*   **Reliability:** The system shall maintain data integrity, preventing changes to input data of completed runs. The portal shall have 99% uptime during business hours.
*   **Security:** All authentication shall use secure channels. User access shall be controlled via integration with NCAR Gatekeeper and internal role-based permissions.
*   **Compliance:** The system shall adhere to NCAR security policies and constraints.
*   **Observability:** Portal Administrators shall have access to metrics dashboards showing user counts, job states, and storage usage. System consistency checks shall validate file pointers in the database against physical storage.

## Milestones and Release Strategy
1.  Project Kick-off & Environment Setup (Globus, MSS access).
2.  Core Infrastructure Completion: User Authentication, Account Management, Basic Object/Project CRUD.
3.  Daymet Modeling Pipeline Completion: Object creation, Project assembly, Job submission/monitoring for Daymet.
4.  BiomeBGC Modeling Pipeline Completion: Integration of PFT, Disturbance objects, and complex topology configuration.
5.  Data Management & Sharing Features: Object sharing, template system, data download.
6.  Version 1.0 Release: Includes core modeling pipelines, administration features, and documentation. Low-priority items (advanced visualization, resource quotas) deferred.

## Risk List and Mitigation Strategies
1.  **Risk:** Complexity of data dependency and state management (Locked/Invalidated) leading to logic errors.
    *   **Mitigation:** Implement a simplified, well-documented state machine for Objects/Projects and conduct thorough testing of dependency chains.
2.  **Risk:** Performance issues with large file transfers to/from the NCAR MSS.
    *   **Mitigation:** Implement asynchronous file upload/download and consider staging areas. Clarify MSS access credentials early.
3.  **Risk:** Globus toolkit integration proves more complex than anticipated, delaying job management features.
    *   **Mitigation:** Develop a thin abstraction layer for grid operations and create mock services for early UI development.
4.  **Risk:** The BiomeBGC simulation topology configuration is overly complex for users.
    *   **Mitigation:** Prototype the UI early with scientist feedback, offering sensible defaults and guided workflows.
5.  **Risk:** Insufficient storage capacity or performance on the chosen compute cluster (Hemisphere Linux cluster).
    *   **Mitigation:** Work with cluster administrators to estimate needs and monitor usage during testing.
6.  **Risk:** Portal Administrator workload for account approval and job management is high.
    *   **Mitigation:** Automate notifications and provide bulk action capabilities in the admin interface.
7.  **Risk:** Data model inconsistencies between the portal database and actual files on MSS.
    *   **Mitigation:** Implement and regularly run the automated system consistency check tool for admins.
8.  **Risk:** Scope creep from low-priority features (visualization, analysis projects).
    *   **Mitigation:** Strictly prioritize and defer all low-priority items, marking them for potential post-V1.0 releases.

## Undecided Issues and Responsible Parties
1.  **Specific file formats and archive structures for user-uploaded data (e.g., for Surface Observation, Site Data).** (Responsible: System Architect / Scientist Liaison)
2.  **Mechanism for MSS access: using user's portal credentials or proxying through a central account.** (Responsible: System Architect / NCAR Security)
3.  **Detailed specification of the "subset" operation for creating new Objects from existing ones.** (Responsible: UI Designer / Scientist Liaison)
4.  **Native data formats for the Daymet and BiomeBGC models that the system must support.** (Responsible: Scientist Liaison)
5.  **Complete list of general system configuration settings controllable by the Portal Administrator.** (Responsible: Product Owner)
6.  **Definition and implementation details for Site Specific PFT List topology in BiomeBGC projects.** (Responsible: Scientist Liaison)
7.  **Validation ranges or rules for data values in Disturbance Objects (e.g., fire intensity).** (Responsible: Scientist Liaison)
8.  **Detailed design and requirements for Visualization and Evaluation Projects (marked TBD).** (Responsible: Product Owner / Scientist Liaison)