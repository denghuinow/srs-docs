Purpose & Scope  
The Model Manager automates configuration, scheduling, and monitoring of weather/climate model jobs (e.g., GMOD, ClimoFDDA) and post-processing tasks. It extends the existing model back end system but does not handle custom cluster-specific job setup without user input or provide full CAM job support.  

Product Background / Positioning  
The Model Manager is a standalone tool integrated into the 4DWX OTM system, accessible via web GUI or command line. It interfaces optionally with MetVault for data storage but operates independently if MetVault is unavailable.  

Core Functional Overview  
1. Submit model jobs (real-time/off-line FDDA, ClimoFDDA) via configuration setup.  
2. Submit "by-hand" jobs requiring manual cluster setup and registration.  
3. Load and submit jobs from saved configuration files.  
4. Retrieve and re-run previously saved job configurations.  
5. Monitor scheduled, running, and completed jobs.  
6. Execute post-processing on model output files.  

Key Users & Usage Scenarios  
Three user groups:  
- Operational scientists (full access: submit, monitor, manage jobs).  
- Research scientists (submit custom jobs, view operational status).  
- Basic users (view job status, stop/restart standard jobs).  
Super users manage all jobs; others manage only their own.  

Major External Interfaces  
Web-based GUI and command-line tool for user interaction. Optional integration with MetVault for data storage. No protocol or field-level details specified.  

Key Non-functional Requirements  
Jobs must support email notifications for start/end/termination. Jobs must be resumable after interruption.  

Constraints, Assumptions & Dependencies  
MM manages cluster allocation automatically but allows user-specified clusters for custom jobs. "By-hand" jobs require manual registration with mandatory job metadata. MetVault is optional.  

Priorities & Acceptance Approach  
Primary priority: Core job submission (model, post-processing) and monitoring. Acceptance requires successful execution of all core functional capabilities without dependency on unresolved TBD items.