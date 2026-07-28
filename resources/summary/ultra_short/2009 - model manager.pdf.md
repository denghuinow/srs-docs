**Purpose & Scope**
The Model Manager (MM) is a tool for configuring, scheduling, running, monitoring, and stopping weather and climate model jobs. It automates the setup and management of these jobs across one or more computing clusters. It does not include the development of the underlying scientific models or data sources.

**Product Background / Positioning**
The MM extends and enhances the existing model back-end system to meet increased operational demands. It is a standalone tool but will also be integrated into the broader 4DWX OTM system. It can operate with or without a connection to the MetVault data archive.

**Core Functional Overview**
*   Set up and submit new model jobs (e.g., real-time forecasts, re-runs, climate studies).
*   Set up and submit standalone post-processing jobs on model output.
*   Submit pre-configured 'by-hand' jobs that exist outside the MM.
*   Submit a job by loading a pre-defined job configuration file.
*   Retrieve, modify, and re-run a previously saved job configuration.
*   View and monitor scheduled, running, and completed jobs.
*   Stop, restart, or resume jobs.

**Key Users & Usage Scenarios**
Primary users are scientists and engineers familiar with model setups, who configure and run operational or research jobs. A secondary group includes less experienced users who monitor status or run standard jobs. A "super user" has permissions to manage any job, while regular users can only manage their own.

**Major External Interfaces**
The system provides a web-based GUI and a command-line tool for user access. It interfaces with one or more high-performance computing clusters for job execution. It has an optional interface to the MetVault data archive for input and output.

**Key Non-functional Requirements**
*   The system must manage jobs across multiple clusters, making allocation decisions transparently to the user.
*   Users must have the option to specify a particular cluster for their job.
*   The system must support the concurrent operation of real-time forecast ensembles across several clusters.

**Constraints, Assumptions & Dependencies**
*   For custom jobs, the user is responsible for ensuring required scripts and executables reside on the target cluster.
*   The system assumes the existence of standard model configurations, data sources, and processing scripts.
*   Integration with the GCAT tool's functionality for climate jobs is required.

**Priorities & Acceptance Approach**
Core priority is automating the setup and management of standard real-time and off-line forecast jobs. Support for custom jobs and post-processing is also required. Acceptance will be based on the system's ability to correctly configure, schedule, run, and monitor the defined job types without user intervention in cluster management.