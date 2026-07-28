**Purpose & Scope**
The system, Libra, is an economy-driven scheduler that provides Quality of Service (QoS) for batch jobs on a cluster. It works as an add-on to the Sun Grid Engine (SGE) cluster management system to schedule CPU time based on user utility (budget and deadline) rather than only system performance. It will only manage sequential and embarrassingly parallel jobs on a homogeneous Linux cluster and does not provide mechanisms for user-to-user bargaining or resource negotiation.

**Product Background / Positioning**
Libra is a component that integrates with the existing Sun Grid Engine (SGE) cluster management system. SGE receives jobs and delegates them to Libra for scheduling and execution host placement. Libra then informs the SGE resource manager to dispatch the job. It operates within this existing cluster software stack without requiring modifications to the Linux kernel.

**Core Functional Overview**
*   Accept or reject jobs based on user-submitted budget, deadline, and estimated execution time.
*   Calculate job priority and resource share (tickets, stride) using a bid-based economic model and the stride scheduling algorithm.
*   Determine the appropriate execution host and queue for an accepted job, considering cluster load and job type.
*   Dispatch the job to the selected queue on the chosen host.
*   Execute jobs by time-slicing CPU resources according to the stride scheduling algorithm.
*   Update the cluster's status information when jobs are scheduled or completed.
*   Allow users to submit jobs, view job status, and delete/change their own jobs (via SGE interface).

**Key Users & Usage Scenarios**
There are two user classes. Cluster **users** submit jobs specifying budget, deadline, and execution time; they can monitor and cancel their own jobs. The cluster **administrator** oversees the entire system, can monitor all jobs and node status, alter the cluster's cost structure and scheduling policy, and cancel, suspend, or resume any job.

**Major External Interfaces**
The primary interface is with the Sun Grid Engine (SGE) software, version 5.3. User and administrator interactions occur through the SGE interface or Linux command line. For parallel job execution, interfaces with PVM and MPI libraries are required. All hardware interfaces (CPU, memory, network) are inherited from SGE.

**Key Non-functional Requirements**
*   Performance: Job submission response time must be under one minute.
*   Reliability: The system must ensure job completion within 10% of the user-specified deadline (assuming accurate job statistics).
*   Security: User job status must be kept private, and only administrators can alter scheduling criteria or resource allocation.
*   Supportability: Code must follow the Hungarian Naming Convention and GNU coding standards.
*   Reliability: Maximum bug rate is 1 bug per thousand lines of code (KLOC). System recovery from an outage must take less than five minutes.

**Constraints, Assumptions & Dependencies**
*   It is constrained to run on a specific test cluster of four Pentium-III workstations with SGE on Linux.
*   It is entirely dependent on the correct functioning and interfaces of the Sun Grid Engine (SGE).
*   It assumes users provide a fair estimate of job execution times.
*   All code must be written in standard C.
*   The scheduler will use heuristics, not exhaustive searches, for scheduling decisions.

**Priorities & Acceptance Approach**
The highest priority is core scheduling functionality: accepting/rejecting jobs based on economic criteria and executing them with the stride algorithm. The economic pricing front-end and a dedicated GUI are deferred. Acceptance will be based on meeting the specified performance metrics (response time, deadline adherence) and correctly implementing the defined scheduling functions within the SGE environment.