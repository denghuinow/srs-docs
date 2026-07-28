# Balanced Summary: Model Manager

## Goals and Scope
The Model Manager (MM) is a software tool designed to automate the configuration, scheduling, running, monitoring, and control of weather and climate model jobs. Its primary goal is to extend and enhance the current model back-end system, providing a more automated and procedural approach for managing jobs across one or more clusters. The tool will be accessible via a web-based GUI and a command-line interface, operating either as a standalone application or in conjunction with the MetVault system.

## Stakeholders and User Stories
*   **NSAP Scientists/Engineers:** Experienced users responsible for setting up and maintaining operational model runs.
*   **RAL/External Research Scientists:** Experienced users who need to run customized model jobs for research, potentially providing their own data and processors.
*   **Less Experienced Users:** Users who need to monitor operational runs, stop/restart jobs, or set up standard model jobs.
*   **Software Development Team:** Engineers at RAL responsible for developing the system based on these requirements.
*   **NSAP Project Sponsors/Management:** Stakeholders overseeing project scope and deliverables.

**User Stories:**
1.  As a **Meteorologist**, I want to set up and schedule a new real-time FDDA model job through a guided interface so that operational forecasting is automated.
2.  As a **Research Scientist**, I want to submit a 'by-hand' job with my own executables and scripts so that I can run a highly customized model experiment.
3.  As an **Operator**, I want to view all running and scheduled jobs in a central queue so that I can monitor system status and job progress.
4.  As a **User**, I want to retrieve, modify, and re-run a previously saved job configuration so that I can efficiently repeat similar analyses.
5.  As a **Model Developer**, I want to run post-processing (e.g., generate plots) on existing model output files so that I can analyze results without re-running the model.
6.  As a **Super User**, I want to stop or restart any user's job from the monitoring interface so that I can manage cluster resources and address issues.

## Key Processes
1.  **Job Submission Initiation:** A user logs in and chooses to submit a new job, triggering the job setup workflow.
2.  **Job Type Selection:** The user selects the type of job to configure (e.g., Weather FDDA, Climo, Post-processing, By-hand).
3.  **Configuration & Parameterization:** For guided setups, the user defines job parameters (e.g., JOBID, domain, model, data sources, nodes) through the Job-Setup module.
4.  **Job Registration/Scheduling:** The completed configuration is saved and submitted to the MM, which schedules it on an appropriate cluster.
5.  **Job Monitoring:** Users can view the job queue to see scheduled, running, and completed jobs, checking status and logs.
6.  **Job Control:** Authorized users can stop, restart, resume, or delete jobs from the queue.
7.  **Output Handling:** Upon job completion, output can be saved to a specified location or sent to the MetVault, and optional post-processing can be triggered.

## Domain Data Elements
*   **Job Configuration:** (Primary Key: `JobID`). Key Fields: JobType, Model (WRF/MM5), DomainSpec, CycleTime, NodeCount, DataSources.
*   **Cluster Resource:** (Primary Key: `ClusterID`). Key Fields: Hostname, NodeList, Status, AllocatedJobs, Capacity.
*   **User Profile:** (Primary Key: `UserID`). Key Fields: Role, Permissions, SavedConfigs, Email.
*   **Data Source:** (Primary Key: `SourceID`). Key Fields: Type (IC/BC, Obs), Location, ProcessorScript, TimePeriod.
*   **Post-Processing Task:** (Primary Key: `TaskID`). Key Fields: ParentJobID, Type (Plot, NAPS, MDV), ConfigFile, OutputDestination.
*   **Job Execution Record:** (Primary Key: `ExecutionID`). Key Fields: JobID, StartTime, EndTime, Status, ClusterUsed, LogPath.

## Non-Functional Requirements
1.  The system must support managing jobs across multiple high-performance computing clusters.
2.  The web GUI and command-line tool must be responsive for routine configuration and monitoring tasks.
3.  The system must ensure job configurations and user data are secure, with access controlled by user roles.
4.  The MM must be reliable for operational 24/7 model runs, with robust failure handling for job scheduling.
5.  The architecture must allow for the integration of new model types and post-processors in the future.
6.  The system should provide email notifications for job start, completion, and termination events.

## Milestones and External Dependencies
1.  Finalize definitions for standard GMOD job configurations and default IC/BC data sources.
2.  Define specifications for integrating the existing GCAT (ClimoFDDA) tool functionalities.
3.  Develop the interface and data exchange protocol with the MetVault system for data storage/retrieval.
4.  Establish the node allocation and management system for multi-cluster support.
5.  Complete the design for the job configuration file schema.

## Risks and Mitigation Strategies
1.  **Risk:** Complexity in managing diverse, customized job setups across clusters may lead to scheduling conflicts or failures.
    *   **Mitigation:** Implement robust job validation and a sandbox/testing mode for custom configurations before production runs.
2.  **Risk:** Integration with the existing MetVault and GCAT systems could face compatibility issues.
    *   **Mitigation:** Develop clear, versioned APIs and conduct incremental integration testing with both systems.
3.  **Risk:** The system may become a single point of failure for all operational model runs.
    *   **Mitigation:** Design the core scheduling and monitoring components for high availability and implement comprehensive logging for recovery.
4.  **Risk:** Performance bottlenecks in the web GUI when monitoring a very large number of concurrent jobs.
    *   **Mitigation:** Implement efficient data pagination, caching strategies, and asynchronous updates for the job queue display.
5.  **Risk:** User resistance from experienced scientists accustomed to the current manual ("by-hand") processes.
    *   **Mitigation:** Ensure the 'by-hand' submission path remains fully functional and provide thorough training highlighting efficiency gains.

## Undecided Issues
1.  Defining the specific defaults for a standard GMOD job configuration.
2.  Determining the level of customization needed for post-processing options (e.g., pseudo-soundings, cross-sections).
3.  Finalizing the list of standard observational data sources and their processing scripts.
4.  Defining model-specific options for WRF jobs during setup.
5.  Establishing a job prioritization scheme for the scheduling system.
6.  Specifying the detailed information to be shown when a user requests "more detailed information" about a job.