# Short Summary: Model Manager Functional Requirements

## Background and Objectives
The Model Manager (MM) is a software tool designed to automate the configuration, scheduling, running, monitoring, and management of weather and climate model jobs. Its primary objective is to extend and enhance the current model back-end system to support increased project demands, staff, and hardware, providing a more automated and procedural workflow for users.

## In Scope
*   Configuration, scheduling, running, monitoring, and stopping/restarting model jobs.
*   Management of jobs across one or more clusters, including node allocation.
*   Support for Weather FDDA (real-time and off-line), ClimoFDDA, and post-processing jobs.
*   Submission of jobs via a setup module, configuration files, or pre-existing "by-hand" scripts.
*   A web-based GUI and command-line interface for user access.

## Out of Scope
*   Detailed specification of data structures or internal system processes.
*   The development of the model executables (e.g., WRF, MM5) themselves.
*   Long-term archival or detailed data management beyond basic output saving.
*   User account creation and advanced permission management systems.
*   Real-time data ingestion from external observational sources.

## Stakeholders and Core Use Cases
*   **NSAP Scientists/Engineers:** Experienced users who set up and maintain operational model runs.
*   **Research Scientists (RAL/External:** Experienced users who run customized model jobs for research, possibly with their own data and processors.
*   **General Users:** Less familiar users who may monitor status, stop/restart jobs, or run standard model jobs.
*   **Project Sponsors/Management:** Oversee project delivery and alignment with organizational goals.
*   **Software Development Team:** Engineers at RAL responsible for developing the system based on these requirements.

**Core User Stories:**
1.  As a **Meteorologist**, I want to set up and submit a new real-time FDDA model job through a guided interface so that operational forecasts can be initiated without manual script configuration.
2.  As a **Research Scientist**, I want to submit a custom "by-hand" job to the Model Manager so that I can run my specialized experimental setup while benefiting from centralized job monitoring.
3.  As a **Software Engineer**, I want to retrieve and modify a previously saved job configuration to re-run a similar job with adjusted parameters, saving setup time.
4.  As a **General User**, I want to view all currently running and scheduled jobs in a centralized queue so that I can monitor system status and job progress.
5.  As a **Meteorologist**, I want to run post-processing (e.g., generate plots) on existing model output files so that I can analyze results without re-running the model.
6.  As any **User**, I want to stop or restart my own running jobs via the manager so that I can control resource usage and respond to issues promptly.

## Success Metrics
*   Reduction in manual steps and time required to configure and submit standard model jobs.
*   Successful management and execution of concurrent jobs across multiple clusters without user intervention in node allocation.
*   User adoption across the three identified user classes, evidenced by the submission and monitoring of jobs via the provided interfaces.

## Major Constraints
*   Must integrate with and extend the existing model back-end system and accommodate the current GMOD framework.
*   Must be capable of running as both a standalone application and as part of the larger 4DWX OTM system.
*   Must support jobs for specific, predefined models (MM5, WRF) and job types (FDDA, ClimoFDDA).
*   User-supplied custom scripts and executables for "by-hand" jobs must reside on the target cluster prior to submission.
*   The system's design must account for jobs with varying resource demands and runtimes.

## Undecided Issues
*   Defining the default configuration for a standard GMOD job.
*   Determining the standard set of observational data sources and their corresponding processing scripts.
*   The level of customization and configuration options needed for post-processing jobs.
*   How jobs should be prioritized within the system's scheduling queue.
*   The specific, detailed information to be displayed when a user requests "more detailed information" about a job.