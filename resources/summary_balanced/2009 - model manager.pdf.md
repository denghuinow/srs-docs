# Balanced Summary

- **Goals and scope (2–3 sentences)**  
The Model Manager (MM) is a software tool designed to automate the setup, scheduling, running, monitoring, and stopping/restarting of weather and climate model jobs. It extends the current model back-end system and supports multiple job types, including real-time and off-line FDDA, ClimoFDDA, and post-processing jobs. The MM can operate as a standalone application or integrate with the 4DWX OTM system and MetVault.

- **Roles and user stories (≤5 roles; total ≤6 user stories)**  
1. As a Meteorologist, I want to set up and run a real-time GMOD job so that operational forecasts are automated and reliable.  
2. As a Research Scientist, I want to submit a custom 'by-hand' job so that I can run specialized experiments with my own executables.  
3. As a Software Engineer, I want to retrieve and modify a saved job configuration so that I can re-run previous jobs with updated parameters.  
4. As an Operational User, I want to monitor running jobs and view their status so that I can ensure timely completion and intervene if needed.  
5. As a User, I want to stop and restart my jobs so that I can manage computational resources and respond to errors.

- **Key processes (ordered list ≤7 steps; each step 1 sentence, indicate the trigger)**  
1. **Trigger: User logs in** – User accesses the system via web GUI or command line.  
2. User selects a job type (e.g., model, post-processing, by-hand).  
3. User configures job parameters (e.g., domains, data sources, executables).  
4. User saves or loads job configuration (optional).  
5. **Trigger: User submits job** – Job is scheduled on one or more clusters.  
6. MM manages node allocation and job execution.  
7. User monitors job status and can stop/restart jobs as needed.

- **Domain data elements (entities ≤6; for each entity, list the primary key and 3–5 key field names)**  
1. **Job Configuration** – PK: JobID; Fields: JobType, CycleTime, DomainSettings, ExecutablePath  
2. **Cluster** – PK: ClusterID; Fields: ClusterName, NodeCount, Status, Location  
3. **Model Output** – PK: OutputID; Fields: JobID, FilePath, CycleTime, Format, MetVaultFlag  
4. **User** – PK: UserID; Fields: UserName, Role, Email, SavedConfigs  
5. **Observational Data** – PK: ObsID; Fields: SourceType, ProcessorScript, TimePeriod, Location  
6. **Post-Processing Job** – PK: PostProcessID; Fields: InputSource, ProcessorType, OutputDestination, NodeRequest

- **Non-functional requirements (≤6 items)**  
1. Support web-based GUI and command-line access.  
2. Manage multiple clusters with centralized control.  
3. Provide email notifications for job events.  
4. Ensure job configurations are saveable and retrievable.  
5. Allow concurrent job monitoring and management.  
6. Integrate optionally with MetVault for data storage.

- **Milestones and external dependencies (≤5 items)**  
1. Integration with 4DWX OTM system.  
2. Dependency on MetVault for certain data storage and retrieval.  
3. Completion of GCAT functionality integration for ClimoFDDA.  
4. Definition of standard IC/BC data sources and pre-processors.  
5. Support for WRF and MM5 model executables.

- **Risks and mitigation strategies (≤5 items)**  
1. **Risk:** Custom jobs may fail due to incorrect user-supplied executables.  
   **Mitigation:** Provide validation checks and clear documentation.  
2. **Risk:** Cluster resource contention from multiple jobs.  
   **Mitigation:** Implement job prioritization and node management.  
3. **Risk:** Integration issues with external systems like MetVault.  
   **Mitigation:** Define clear APIs and fallback modes.  
4. **Risk:** User errors in complex job setups.  
   **Mitigation:** Offer templates and guided configuration wizards.  
5. **Risk:** Scalability with growing number of jobs and users.  
   **Mitigation:** Design for distributed clusters and load balancing.

- **Undecided issues (≤6 items; unknown write "Not mentioned")**  
1. Default configurations for GMOD jobs.  
2. Standard IC/BC data sources and pre-processors.  
3. Customization level for post-processing options.  
4. Job prioritization mechanism.  
5. Detailed information shown in job monitoring.  
6. Support for CAM jobs.