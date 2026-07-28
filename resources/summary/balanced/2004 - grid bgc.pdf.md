# Balanced Summary: Grid-BGC Application Version 1.0

## Goals and Scope
The Grid-BGC Application is a grid-based software infrastructure designed to support bio-geo-chemical modeling. It provides a graphical web portal for scientists to manage input data, run simulations using the Daymet and Biome-BGC models, and visualize and share results. The system leverages the Globus toolkit and NCAR's computational and storage resources to enable secure, distributed scientific workflows.

## Stakeholders and User Stories
*   **Scientist (Favored User):** Primary user who manages data, runs simulations, and analyzes results.
*   **Portal Administrator:** Manages user accounts, monitors system operations, and handles job management.
*   **Data User (Low Priority):** Researcher who accesses and downloads simulation output data but does not initiate runs.

**User Stories:**
1.  As a Scientist, I want to create and configure a Daymet modeling project so that I can generate gridded surface weather datasets.
2.  As a Scientist, I want to execute and monitor a Biome-BGC model run so that I can perform biogeochemical simulations.
3.  As a Scientist, I want to visualize and download output data so that I can analyze and share my results.
4.  As a Portal Administrator, I want to approve new user accounts and manage account status so that system access is controlled.
5.  As a Portal Administrator, I want to monitor and manage running jobs so that I can ensure system stability and assist users.
6.  As a Data User, I want to download published output datasets so that I can use them for my own research.

## Key Processes
1.  **Account Application & Login:** A user applies for an account and, once approved, logs in via the web portal using NCAR Gatekeeper credentials. *(Trigger: User accesses the portal)*
2.  **Data Object Creation:** A scientist creates or uploads input data objects (e.g., Surface Observations, DEMs) which can be shared or used as templates. *(Trigger: User initiates a new data object setup)*
3.  **Project Configuration:** The scientist creates a Daymet or Biome-BGC project, referencing the required input objects and defining simulation parameters. *(Trigger: User starts a new modeling project)*
4.  **Model Execution & Monitoring:** The user submits the project to a selected computational resource and monitors the job status on a tile-by-tile basis. *(Trigger: User submits a project for execution)*
5.  **Output Management:** Upon successful completion, the system automatically creates an output object containing results, which can be visualized, downloaded, or shared. *(Trigger: Model run completes)*
6.  **Data Sharing & Collaboration:** Users can share specific data objects with other users or mark them as system-wide templates for reuse. *(Trigger: User sets sharing permissions on an object)*
7.  **Administrative Oversight:** The portal administrator manages user accounts, reviews system metrics, and performs consistency checks on stored data. *(Trigger: Admin logs into the administrative interface)*

## Domain Data Elements
*   **User Account:** (Primary Key: User ID). Key Fields: Gatekeeper Username, Role, Account Status, Email.
*   **Data Object:** (Primary Key: Object ID). Key Fields: Object Type (List/Grid/Parameterization), Owner, Sharing Status, Data Integrity State (Unlocked/Locked/Invalidated), Metadata.
*   **Project (Daymet/BiomeBGC):** (Primary Key: Project ID). Key Fields: Project Type, Referenced Object IDs, Owner, Simulation Topology, Execution Status.
*   **Model Output:** (Primary Key: Output ID). Key Fields: Source Project ID, Contained Datasets, Tile Information, Creation Date.
*   **System Template:** (Primary Key: Template ID). Key Fields: Base Object ID, Submitter, Object Type, Description.
*   **Compute Job:** (Primary Key: Job ID). Key Fields: Associated Project ID, User, Resource Node, Job Status, Tile Statuses.

## Non-Functional Requirements
1.  The web portal must be compatible with specified browsers (Internet Explorer 6.0, Netscape 7.1, Safari).
2.  The system must integrate with and store all file-based data on the NCAR Mass Storage System (MSS).
3.  User authentication must comply with NCAR Gatekeeper security policies and use secure data channels.
4.  The system architecture must be implemented using the Globus toolkit for grid communications.
5.  Context-sensitive online help must be available from every page in the portal.
6.  User accounts must be locked after three consecutive failed login attempts.

## Milestones and External Dependencies
1.  Integration with the NCAR Dataportal Web Server for hosting the web portal.
2.  Deployment and configuration of compute node software on the Hemisphere Linux cluster at CU.
3.  Successful interfacing with the NCAR Mass Storage System for all data storage.
4.  Reliance on the continued operation and policies of the NCAR Gatekeeper system for user authentication.
5.  Completion of user documentation, including a full online manual.

## Risks and Mitigation Strategies
1.  **Risk:** Complex data dependency and state management (locked/invalidated) could lead to user confusion or data loss.
    *   **Mitigation:** Implement clear user interfaces showing object states and enforce confirmation prompts for destructive actions.
2.  **Risk:** Performance bottlenecks when handling large grid datasets or numerous concurrent model runs.
    *   **Mitigation:** Design efficient data handling for the MSS and implement robust job queuing and monitoring.
3.  **Risk:** Security vulnerabilities from integrating multiple systems (Portal, Gatekeeper, MSS, Globus).
    *   **Mitigation:** Adhere strictly to NCAR security policies and conduct thorough security testing of all interfaces.
4.  **Risk:** Low-priority features (visualization, data user tools) may not be delivered if time is limited.
    *   **Mitigation:** Clearly prioritize core modeling workflows and define minimal viable features for later phases.
5.  **Risk:** Incorrect file format handling or metadata extraction during data upload.
    *   **Mitigation:** Provide strict format specifications (e.g., NetCDF conventions) and implement validation during upload.

## Undecided Issues
1.  The specific workflow for users who need to set up supporting data before their first model run.
2.  Detailed specifications for data subsetting operations (e.g., for Surface Observation Objects).
3.  The native model file formats for DEM and Analysis Mask datasets.
4.  The implementation method and user interface for the Visualization and Evaluation projects.
5.  Whether to implement resource quotas for users and the specific controls for compute node settings.
6.  The method for authenticating users with the NCAR Mass Storage System (proxy vs. user credentials).