# Detailed Summary: Model Manager (MM)

## Background and Scope
The Model Manager (MM) is a software tool designed to automate the configuration, scheduling, execution, monitoring, and control of weather and climate model jobs. It extends the existing model back-end system to manage jobs across one or more clusters, providing centralized node allocation and management. The primary goal is to streamline operational model runs and support research activities by offering both web-based and command-line interfaces. Non-goals include replacing the underlying model executables (e.g., WRF, MM5) or directly managing low-level cluster hardware details beyond job allocation.

## Stakeholders Matrix and Use Cases
*   **Meteorologist/Software Engineer (NSAP):** Experienced users who configure and maintain operational model runs, requiring advanced customization and cluster management.
*   **Research Scientist (RAL/External):** Users familiar with model setups who run customized jobs for research, potentially providing their own input data and processors.
*   **General User:** Less experienced users who monitor operational runs, stop/restart jobs, or set up standard model jobs with minimal configuration.
*   **System Administrator (Implied):** Responsible for maintaining the MM infrastructure, clusters, and user access (e.g., "super user" capabilities).

**Main Scenarios:**
1.  Set up and submit a new Weather FDDA (GMOD) model job via the Job-Setup module.
2.  Set up and submit a new ClimoFDDA model job via the Job-Setup module.
3.  Set up and submit a standalone post-processing job on existing model output.
4.  Submit a pre-configured "by-hand" job by registering custom scripts with the MM.
5.  Load a job configuration from a file, optionally modify it, and submit the job.
6.  Retrieve a previously saved job configuration, modify it, and re-submit.
7.  View and monitor scheduled, running, and completed jobs via a job queue.
8.  Stop, restart, or resume a job (with "super user" privileges for any job).

**Exception Scenario:** Submitting a "custom" GMOD job where the user supplies non-standard executables or pre-processors, requiring manual verification of component availability on the target cluster.

## Business Process
**Main Process: Submit and Manage a Model Job**
1.  **Trigger:** User logs into the MM system.
2.  User selects "Submit a new job" and chooses a job type (e.g., model, post-processing, by-hand).
3.  For a new model job, user configures parameters (model type, domain, time cycle, data sources, nodes).
4.  User optionally configures post-processing steps and output destinations.
5.  User saves the job configuration (optional) and submits the job to the MM.
6.  MM schedules the job, allocates cluster resources, and initiates execution.
7.  User monitors job status via the job queue.
8.  Upon completion, output is stored as specified, and notifications are sent.

**Key Branch A: Submit "By-Hand" Job**
1.  User selects "Submit a 'By Hand' Job".
2.  User provides mandatory job metadata (ID, script location, run time, estimated duration, executables).
3.  User submits the job; MM registers it for execution without deep configuration knowledge.
4.  The custom job notifies the MM upon completion.

**Key Branch B: Job Control**
1.  User views the job queue and selects a specific running or scheduled job.
2.  User chooses an action (Stop, Restart, Resume, Delete).
3.  MM executes the control command on the cluster.
4.  Job status is updated in the queue.

## Domain Model
*   **Job:** Core entity representing a computational task. Fields: JobID (required, unique), JobType (required), Owner (required, reference to User), Status, ScheduleTime, ClusterAllocation, ConfigurationSnapshot.
*   **User:** System user. Fields: UserID (required, unique), Role (e.g., scientist, admin), Email.
*   **Job Configuration:** Saved setup parameters for a job. Fields: ConfigID (unique), JobType, Parameters (key-value store), Owner (reference to User), CreationDate.
*   **Cluster:** A computational resource pool. Fields: ClusterID (unique), Name, NodeCount, Status.
*   **Data Source:** Source of input data. Fields: SourceID, Type (e.g., ETA, WMO), LocationPath, IsStandard (boolean).
*   **Processor:** A script or executable. Fields: ProcessorID, Type (e.g., Pre-processor, Model, Post-processor), Path, IsCustom (boolean).
*   **Output Product:** Result of a job or post-processing step. Fields: ProductID, Job (reference), Type (e.g., plot, data file), DestinationPath.
*   **Notification:** Alert for a job event. Fields: NotificationID, Job (reference), EventType (e.g., start, end), RecipientEmail.

## Interfaces and Integrations
*   **MetVault:** Direction: Bi-directional. Theme: Data storage and retrieval. Input: Model output files and metadata for storage. Output: Historical input data for re-run jobs. SLA: Data retrieval for past cycles must match original runtime availability.
*   **Web-based GUI:** Direction: User to MM. Interaction: Primary user interface for all functions (setup, monitoring, control). Input: User actions and configuration data. Output: Job status, forms, tables. SLA: Responsive interaction for job submission and monitoring.
*   **Command Line Tool:** Direction: User to MM. Interaction: Scriptable interface for job management. Input: Command arguments and configuration files. Output: Status messages and logs. SLA: Support for batch submission and integration into user workflows.
*   **Cluster Scheduler (e.g., PBS, Slurm):** Direction: MM to Cluster. Interaction: Job submission and resource management. Input: Job resource requirements (nodes, runtime). Output: Job execution status and allocation info. SLA: Reliable job launch and status feedback.
*   **Email Server:** Direction: MM to External. Interaction: User notifications. Input: Job events and user email preferences. Output: Notification emails. SLA: Timely delivery of job status alerts.

## Acceptance Criteria
**For Job Submission:**
*   **Given** a user has configured a new Weather FDDA job with valid parameters,
*   **When** the user submits the job,
*   **Then** the job appears in the "scheduled" queue and begins execution on the allocated cluster at the specified time.

**For Job Monitoring:**
*   **Given** a job is running,
*   **When** a user views the job queue and selects that job,
*   **Then** the system displays detailed status information including current processing stage, estimated remaining time, and allocated cluster nodes.

**For Custom Job Support:**
*   **Given** a user has prepared a custom "by-hand" job script on a known cluster,
*   **When** the user registers the job with the MM by providing the required metadata,
*   **Then** the MM accepts the job, schedules it, and the user can monitor its status in the central queue.

## Non-functional Metrics
*   **Performance:** Job submission latency < 5 seconds; Job status update frequency ≤ 30 seconds.
*   **Reliability:** System availability > 99.5%; Successful job execution rate > 95% for configured jobs.
*   **Security:** User authentication required for all actions; Role-based access control (e.g., "super user").
*   **Compliance:** Adherence to internal RAL software development and operational standards.
*   **Observability:** Comprehensive logging of all job lifecycle events; Centralized view of all cluster and job statuses.

## Milestones and Release Strategy
1.  Core MM architecture and job queue management.
2.  Job Setup module for standard Weather FDDA (GMOD) jobs.
3.  Integration with primary cluster scheduler and basic MetVault interaction.
4.  Web GUI and CLI for core functions (submit, monitor, control).
5.  "By-hand" job submission and ClimoFDDA job support.
6.  Enhanced post-processing module and advanced configuration management.

## Risk List and Mitigation Strategies
1.  **Risk:** Complexity of integrating with diverse, existing "by-hand" job scripts. **Mitigation:** Define clear, minimal mandatory metadata requirements and provide templates.
2.  **Risk:** Unclear requirements for "standard" configurations (e.g., default GMOD setup, data sources). **Mitigation:** Convene stakeholder workshops to define and document standards early.
3.  **Risk:** Performance bottlenecks in managing multiple large clusters. **Mitigation:** Design scalable architecture with load testing using simulated job loads.
4.  **Risk:** User resistance to new workflow from experienced scientists. **Mitigation:** Provide extensive training, phased rollout, and demonstrate time-saving benefits.
5.  **Risk:** Post-processing customization scope becomes unmanageable. **Mitigation:** Prioritize and implement a core set of standard post-processors first, based on user voting.
6.  **Risk:** Dependency on MetVault availability for re-run jobs. **Mitigation:** Implement graceful degradation allowing manual directory specification for input data.
7.  **Risk:** Inaccurate job runtime estimates causing poor cluster utilization. **Mitigation:** Implement feedback loop where MM learns from historical job runtimes to improve estimates.
8.  **Risk:** Data security and access control for multi-user, multi-cluster environment. **Mitigation:** Implement robust authentication/authorization and audit trails from the start.

## Undecided Issues and Responsible Parties
1.  Definition of defaults for a standard GMOD job configuration. (Responsible: Lead Meteorologist & System Architect)
2.  Domain creation and management specifics, especially for WRF vs. MM5. (Responsible: Modeling Software Engineers)
3.  Standard set of observational data sources and their processing scripts. (Responsible: Data Integration Team)
4.  Scope and customization level for post-processing options. (Responsible: Product Manager & User Committee)
5.  Job prioritization scheme within the queue. (Responsible: System Architect & Operations Lead)
6.  Detailed requirements and support for CAM model jobs. (Responsible: ClimoFDDA Team Lead)
7.  Definition of "standard MM5 executable" and supported WRF model options. (Responsible: Modeling Software Engineers)
8.  Specification of what constitutes "detailed information" for a job in the monitoring view. (Responsible: UI Designer & Lead User)