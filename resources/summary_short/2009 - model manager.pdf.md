# Short Summary

- **Background and objectives**: The Model Manager (MM) is being developed to automate and streamline the setup, scheduling, running, and monitoring of weather and climate model jobs, addressing the growing needs of NSAP projects and staff.

- **In scope**:
  - Configure, schedule, run, monitor, stop, restart, and resume model jobs.
  - Support for Weather FDDA, ClimoFDDA, and post-processing jobs.
  - Job submission via setup module, by-hand scripts, configuration files, or saved configurations.
  - Centralized control over multiple clusters with optional cluster selection.
  - Integration with MetVault for data storage and retrieval.

- **Out of scope**:
  - CAM job setup details (marked TBD).
  - Specific definitions for standard MM5 executables and observational data sources.
  - Detailed customization levels for post-processing.
  - Job prioritization method.
  - Detailed information shown for job monitoring.

- **Roles and core use cases**:
  - As a Meteorologist, I want to set up and run model jobs so that I can perform operational or research forecasting.
  - As a Software Engineer, I want to automate job management so that system efficiency and scalability are improved.
  - As a User, I want to monitor and control jobs so that I can ensure timely completion and handle issues.

- **Success metrics**:
  - Successful automation of job setup and execution.
  - Support for multiple job types and user customization.
  - Effective monitoring and control of job status and resources.

- **Major constraints**:
  - Must integrate with existing model back-end systems and MetVault.
  - Must support both web-based GUI and command-line access.
  - Jobs may run across one or more clusters with centralized management.
  - Users can optionally specify cluster and node allocation.
  - Custom jobs require user-provided scripts and executables on target clusters.

- **Undecided issues**:
  - Default configurations for GMOD jobs.
  - Standard IC/BC data sources and pre-processors.
  - Observational data sources and processing scripts.
  - Post-processing customization level.
  - Job prioritization approach.