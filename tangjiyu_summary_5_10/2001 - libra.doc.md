# 2001 - Libra

## Overview
Libra is an Economy-Driven Cluster Scheduler designed as an add-on to the Sun Grid Engine (SGE) cluster management system.^[1]^ Its primary objective is to provide Quality of Service (QoS) computational economy in cluster computing by managing batch jobs based on user utility, such as deadlines and budgets, rather than system performance.^[2]^

## Key Features
- **Market-Based Economy Model**: Uses a bid-based proportional resource-sharing model to allocate CPU time according to user-specified QoS parameters like deadlines and budgets.^[3]^
- **Stride Scheduling Algorithm**: Enforces resource allocations proportional to a user’s priority, determined by job tickets inversely proportional to job strides.^[4]^
- **Dynamic Resource Allocation**: Allows dynamic reallocation of resources to meet urgent job deadlines, even if submitted later.^[5]^
- **Scalability and Configurability**: Performance does not degrade with additional nodes and jobs; supports various scheduling policies incorporating QoS parameters.^[6]^
- **Job Accounting and Security**: Provides basic job accounting and ensures administrative security and privacy of user job status.^[7]^

## Functional Requirements
- **Submit Job**: Users submit jobs with details including execution time, resources required, budget, and deadline.^[8]^
- **View Job Status**: Users and administrators can monitor job progress and details.^[9]^
- **Delete/Change Job**: Users can cancel jobs or modify certain parameters under specific circumstances.^[10]^
- **Initialize Job**: Prepares scheduler with job details for eventual scheduling.^[11]^
- **Accept/Reject Job**: Determines job acceptance based on budget, deadline, and execution time.^[12]^
- **Calculate Scheduling Information**: Uses Stride Scheduling to allocate CPU cycles based on budget and deadline.^[13]^
- **Determine Execution Host**: Selects the least loaded host and appropriate queue for job execution.^[14]^
- **Dispatch Job**: Inserts job into the execution queue.
- **Update Cluster Status**: Updates cluster status upon job scheduling or completion.^[15]^
- **Execute Job**: Manages time-slicing between executing jobs based on stride-scheduling.^[16]^

## User Characteristics
- **End Users**: Need technical know-how to submit jobs with details like execution time and resources required.^[17]^
- **Administrators**: Advanced cluster operators qualified in Linux, SGE, and Libra Scheduler.^[18]^

## Constraints
- **Hardware Resources**: Currently tested on a network of four Pentium-III workstations with 128 Mb RAM.^[19]^
- **Simulation Tools**: May require a specially designed simulation tool for performance analysis.^[20]^

## Assumptions and Dependencies
- **SGE Compatibility**: Assumes compatibility of SGE modules with Libra’s scheduling policies.^[21]^
- **Job Estimation**: Users are assumed to provide fair estimates of job execution times.^[22]^

## Performance Requirements
- **Response Time**: Maximum 1 minute for job submission response.^[23]^
- **Deadline Sensitivity**: Ensures job completion within a 10% error allowance of submitted deadlines.
- **Cost Sensitivity**: Maximum cost charged will not exceed the user-submitted maximum.

## Supportability
- **Coding Standards**: Adheres to GNU General Purpose License and Hungarian Naming Convention.^[24]^
- **Documentation**: Online user documentation in the form of man pages.^[25]^

## Interfaces
- **User Interfaces**: Command-line or SGE interface for job submission, status monitoring, and job management.^[26]^
- **Administrator Interfaces**: Additional commands for cluster and job management.^[27]^
- **Hardware/Software Interfaces**: Incorporates SGE’s interfaces for CPU, memory usage, and network communication.^[28]^

## Licensing
- **Open Source**: Released under GPL license.^[29]^