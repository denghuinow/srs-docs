# Functional Requirements Specification for the Model Manager

## 1. Introduction

### 1.1 Purpose
This document defines the functional requirements for the Model Manager (MM) software tool. It describes the main functionality of the tool from the user's perspective and will serve as input for a potential Software Requirement Specifications (SRS) document.

### 1.2 Document Conventions
- MM: Model Manager
- 4DWX OTM: 4DWX On the Move
- Model job: A collection of processes computing a weather or climate model over a given domain and time period
- Post-processing job: Processes that take model output files as input, perform calculations or conversions, and produce output files in different formats
- By-hand job: Existing scripts and executables set up by the user on a cluster in advance

### 1.3 Intended Audience
The intended audience includes users of the system, scientists and software engineers at RAL who will develop the system, NSAP project sponsors and management.

### 1.4 Project Scope
The Model Manager is a software tool that allows users to configure, schedule, run, monitor, and stop (and re-start/resume) model jobs. The primary goal is to extend the current model back end system and automate the setup, running and monitoring of model jobs, including a more automated node management system.

### 1.5 References
"4DWX on the Move (4DWX OTM)", Scott Swerdlin, concept paper

## 2. Overall Description

### 2.1 Product Perspective
With the increase in NSAP projects, staff and hardware, a more automated and procedural way of setting up and running model jobs has become necessary. The MM provides this extension and enhancement to the current model back end. The MM is a standalone software tool, which will also be part of the 4DWX OTM system.

The MM can run in conjunction with the MetVault, and can also run as a stand-alone application. The MM will be accessible from a web-based GUI and a command line tool.

### 2.2 Product Features
The main functions of the system include:
- Set up and submit a model job
- Set up and submit a "post-processing" job
- Submit a 'by-hand' job
- Load a job configuration from a file and submit the job
- Retrieve and run a previously saved job configuration
- View scheduled, running and old jobs

### 2.3 User Classes and Their Characteristics
1. Scientists and software engineers at NSAP - experienced users familiar with the model back end
2. Scientists at RAL (and outside) - experienced users for research purposes who may want to set up customized model jobs
3. Less experienced users - may want to view status of operational model runs, stop/restart existing jobs or set up standard model jobs

## 3. System Features

### 3.1 Set up and submit a model job
Allows users to set up and schedule model jobs using the MM's Job-Setup module. Supports two main types:
- Weather FDDA (real time or off-line): Automates setup of GMOD jobs, re-runs and case studies
- Climo: Integrates GCAT functionalities within the MM for ClimoFDDA jobs

Key capabilities:
- Default GMOD job configuration that can be customized
- Accepts "custom" GMOD jobs with user-provided input data, pre-processors or customized executables
- Domain definition options (create own, choose predefined, or submit TERRAIN files)
- Cycle time specification and job type determination (case study or re-run)
- Restart file configuration options
- Sigma-level configuration choices
- Node allocation specification
- Email notification options for job start/end/termination
- Standard or custom IC/BC data sources and pre-processors
- Additional pre-processors for IC/BC data (e.g., LDAS)
- Standard and custom observational data sources and processing
- Model-specific options (MM5 executables or WRF model options)
- Final and Prelim Analysis options for re-runs and case studies
- Additional processing on model output
- Option to save model output in MetVault
- Job configuration saving capability
- Post-processing integration

### 3.2 Set up and submit a "post-processing" job
Provides ability to run "post-processing" on existing model output files. Supports various post-processing types:
- Plots (NCL or RIP)
- NAPS
- MDV
- Sites
- MEDOC
- Stereo
- Verification

Key capabilities:
- Model output file location specification (JOBID/cycle time or direct file path)
- Custom or default configuration file usage
- Output product destination specification
- Node allocation specification
- Job configuration saving
- Job submission

### 3.3 Submit a 'By-hand' job
Accommodates current GMOD-framework and allows running customized jobs. Key capabilities:
- Custom job registration with mandatory information:
  - Job ID
  - Script location
  - Run time and estimated duration
  - Executable names and max runtime
  - Node count
  - Output product location
- Optional information:
  - Script run frequency
  - Job type
  - Additional information
- Job configuration saving
- Job submission
- Job queue viewing
- Email notifications for job status
- Custom job completion notification to MM

### 3.4 Load a job configuration from a file and submit the job
Provides ability to load job configurations from files. Key capabilities:
- File-based job configuration loading
- Configuration modification capability
- Changed configuration saving
- Job submission

### 3.5 Retrieve and run a previously saved job configuration
Allows retrieval of previous job configurations for re-running or modification. Key capabilities:
- User authentication
- Saved job configuration viewing with attributes (Job ID, type, last run cycle/time)
- Configuration modification/deletion
- Changed configuration saving
- Job submission

### 3.6 View scheduled, running and old jobs
Facilitates monitoring of running jobs, viewing job queue and past jobs. Key capabilities:
- User authentication
- Job viewing options (running, scheduled, past, or all jobs)
- Job table display with attributes:
  - User ID (job owner)
  - Job ID and type
  - Job priority
  - Start time and remaining/elapsed time
  - Cycle and stage information
  - Status (SCHEDULED, RUNNING, DONE)
  - Cluster and node information
  - Processor count
- Detailed job information viewing
- Log file access
- Job deletion (user's jobs or any job by super user)
- Job stopping (user's jobs or any job by super user)
- Job re-starting (user's jobs or any job by super user)
- Job resuming (user's jobs or any job by super user)
