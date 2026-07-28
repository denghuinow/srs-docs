# Software Requirements Specification (SRS) for Libra: An Economy-Driven Cluster Scheduler

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Approved for Development

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Libra system. Libra is an economy-driven scheduler designed as an add-on to the Sun Grid Engine (SGE) cluster management system. Its primary purpose is to provide Quality of Service (QoS) for batch jobs by scheduling CPU time based on user utility (budget and deadline) rather than solely on system performance metrics. This document is intended for use by the project stakeholders, developers, testers, and project managers.

### 1.2 Scope
Libra will operate as a scheduling component integrated with SGE version 5.3 on a homogeneous Linux cluster. The system will manage sequential and embarrassingly parallel batch jobs. It will implement a bid-based economic model and the stride scheduling algorithm to allocate resources. The scope explicitly excludes:
*   Management of tightly-coupled parallel jobs (beyond embarrassingly parallel).
*   User-to-user bargaining or resource negotiation mechanisms.
*   Modifications to the underlying Linux kernel or SGE core.
*   A dedicated graphical user interface (GUI) or economic pricing front-end (deferred).

### 1.3 Definitions, Acronyms, and Abbreviations
*   **SGE:** Sun Grid Engine, a distributed resource management system.
*   **QoS:** Quality of Service, the ability to provide different priority levels to different applications or data flows.
*   **Batch Job:** A predefined sequence of commands processed without user interaction.
*   **Embarrassingly Parallel:** A workload where tasks can be executed independently with little to no communication.
*   **Stride Scheduling:** A deterministic fair-share scheduling algorithm where each job receives a "stride" inversely proportional to its number of "tickets."
*   **Tickets:** A unit representing a job's share of system resources in stride scheduling.
*   **PVM:** Parallel Virtual Machine, a software library for parallel computing.
*   **MPI:** Message Passing Interface, a standardized message-passing system.
*   **KLOC:** Thousand Lines of Code.

### 1.4 References
*   Sun Grid Engine 5.3 Administration & User Documentation.
*   Waldspurger, C. A., & Weihl, W. E. (1995). *Stride scheduling: deterministic proportional-share resource management*.
*   GNU Coding Standards.
*   Project Charter for Libra.

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its functions, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines the non-functional requirements, including performance, security, and supportability. Section 5 lists constraints, assumptions, and dependencies.

## 2. Overall Description

### 2.1 Product Perspective
Libra is a middleware component that fits into an existing cluster software stack. It is not a standalone product but an add-on module that intercepts jobs from SGE, makes scheduling decisions based on economic criteria, and instructs SGE on where and when to dispatch the job. The system architecture is depicted below:

```
[User] -> [SGE qsub] -> [Libra Scheduler] -> [SGE Resource Manager] -> [Execution Host]
      \_______________________________________/
                    (Status & Control)
```

All hardware interfaces (CPU, memory, network) and basic job lifecycle management are inherited from SGE.

### 2.2 Product Functions
The core functions of Libra are:
1.  **Job Admission Control:** Evaluate incoming job requests (budget, deadline, estimated runtime) and accept or reject them.
2.  **Economic Scheduling:** Calculate a job's priority and resource share (tickets/stride) using its bid (budget/deadline) and a cluster-defined cost model.
3.  **Resource Selection:** Determine the optimal execution host and SGE queue for an accepted job, considering current cluster load and job type (sequential/parallel).
4.  **Job Dispatch:** Instruct the SGE resource manager to place the job into the selected queue on the chosen host.
5.  **Resource Allocation Enforcement:** Execute jobs by time-slicing CPU resources across nodes according to the calculated stride schedule.
6.  **State Management:** Maintain and update internal cluster status (job states, node loads, financial accounts).
7.  **User & Admin Interface:** Provide mechanisms (via SGE) for users to submit, monitor, and manage their jobs, and for administrators to control the system.

### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Cluster User** | Members of a research or engineering group. Have a finite "budget" of compute credits. Technical proficiency with command-line tools. | Submit jobs with budget, deadline, and runtime estimates. Monitor status of own jobs. Cancel or modify own pending jobs. |
| **Cluster Administrator** | System manager or lead researcher. Has full knowledge of the cluster hardware and SGE. Possesses superuser or equivalent privileges. | Monitor all jobs and cluster node status. Configure and modify the cluster's economic model (e.g., base cost per CPU-hour). Suspend, resume, or cancel any job. Recover the system from failures. |

### 2.4 Operating Environment
*   **Hardware:** A homogeneous test cluster of four (4) Pentium-III workstations connected via a local area network.
*   **Software:**
    *   Operating System: Linux (Distribution to be specified, e.g., Red Hat 9).
    *   Cluster Management: Sun Grid Engine (SGE), version 5.3.
    *   Parallel Libraries: PVM and MPI libraries for supporting embarrassingly parallel jobs.
    *   Development: Standard C compiler (e.g., GCC).
*   **Interfaces:** Primary integration is through SGE's programming and command-line interfaces.

### 2.5 Design and Implementation Constraints
1.  **Implementation Language:** All components must be written in standard C (ANSI/ISO C89/C99).
2.  **Coding Standards:** Code must adhere to the Hungarian Naming Convention and the GNU coding standards for formatting and structure.
3.  **Algorithmic Constraint:** Scheduling decisions (host selection, admission) shall be made using efficient heuristics, not exhaustive or NP-complete search algorithms.
4.  **Platform Constraint:** Initial development and testing are constrained to the specified four-node Pentium-III test cluster.

### 2.6 Assumptions and Dependencies
*   **Dependency:** Libra is entirely dependent on the correct functioning, stability, and published interfaces of Sun Grid Engine 5.3. Any changes in SGE may break Libra.
*   **Assumption:** Users will provide a reasonably accurate estimate of their job's execution time. System guarantees (e.g., deadline adherence) are predicated on this assumption.
*   **Assumption:** The underlying Linux operating system and hardware are stable and function correctly. Libra does not manage hardware faults.
*   **Assumption:** User authentication and basic accounting are handled by SGE and the underlying OS.

## 3. System Features & Functional Requirements

### 3.1 Job Submission and Admission Control (LIB-FR-001)
**Description:** The system shall accept job submission requests from SGE, evaluate them against economic and resource criteria, and return an accept or reject decision.

**Requirements:**
*   **LIB-FR-001.1:** The system shall receive a job submission request containing, at minimum: user ID, estimated execution time (wall clock), deadline, and budget (in allocated credits).
*   **LIB-FR-001.2:** The system shall evaluate if the user's budget is sufficient to support the job's estimated cost at the current cluster pricing.
*   **LIB-FR-001.3:** The system shall evaluate if the job's deadline is feasible given the current cluster load and the job's estimated execution time.
*   **LIB-FR-001.4:** The system shall reject the job and notify the user (via SGE) if either the budget is insufficient or the deadline is infeasible.
*   **LIB-FR-001.5:** Upon acceptance, the system shall reserve the user's budget for the estimated job cost.

### 3.2 Economic Scheduling and Ticket Calculation (LIB-FR-002)
**Description:** The system shall calculate a job's resource share (represented as tickets) based on its utility function (budget/deadline) using a configurable economic model.

**Requirements:**
*   **LIB-FR-002.1:** The system shall implement a bid function, `Bid = Budget / (Deadline - Current_Time)`.
*   **LIB-FR-002.2:** The system shall convert a job's bid into a number of scheduling "tickets," where a higher bid results in more tickets. The exact mapping (e.g., linear, logarithmic) shall be configurable by the administrator.
*   **LIB-FR-002.3:** The system shall calculate a "stride" for each job as `Stride = K / Tickets`, where `K` is a large constant.
*   **LIB-FR-002.4:** The system shall maintain a global "pass" value for the scheduler and select the job with the smallest pass value to run next, incrementing its pass by its stride upon selection.

### 3.3 Execution Host and Queue Selection (LIB-FR-003)
**Description:** The system shall select the most appropriate execution host and SGE queue for an accepted job.

**Requirements:**
*   **LIB-FR-003.1:** The system shall maintain a real-time view of cluster load (e.g., CPU queue length, memory usage) for each execution host.
*   **LIB-FR-003.2:** For sequential jobs, the system shall select the host with the lowest current load that meets the job's implicit requirements.
*   **LIB-FR-003.3:** For embarrassingly parallel jobs, the system shall select a set of hosts that can collectively provide the required number of parallel tasks, optimizing for overall cluster load balance.
*   **LIB-FR-003.4:** The system shall map the selected host(s) to the corresponding SGE execution queue(s).

### 3.4 Job Dispatch and Execution (LIB-FR-004)
**Description:** The system shall dispatch the scheduled job to SGE for execution and ensure runtime resource allocation follows the stride schedule.

**Requirements:**
*   **LIB-FR-004.1:** The system shall instruct the SGE resource manager (`qmod`, `qrsh` or equivalent) to dispatch the job to the pre-selected queue on the chosen host(s).
*   **LIB-FR-004.2:** The system shall interface with the OS-level scheduler (via SGE/policies or a low-level library) to enforce time-slicing of CPU resources among concurrent jobs according to their stride-based schedule.
*   **LIB-FR-004.3:** The system shall monitor job execution state (started, finished, failed) via callbacks or polling of SGE.

### 3.5 State and Accounting Management (LIB-FR-005)
**Description:** The system shall maintain internal state and update financial accounts upon job completion.

**Requirements:**
*   **LIB-FR-005.1:** The system shall maintain a persistent record of all scheduled jobs, including user, tickets, stride, pass, host, status, and actual cost.
*   **LIB-FR-005.2:** Upon job completion (successful or failed), the system shall calculate the final cost based on actual CPU time used and the cluster's pricing model.
*   **LIB-FR-005.3:** The system shall debit the user's account for the final job cost and release any reserved budget that was not used.
*   **LIB-FR-005.4:** The system shall update cluster load information and free resources associated with the completed job.

### 3.6 User and Administrator Interface (LIB-FR-006)
**Description:** The system shall provide functional interfaces for users and administrators, primarily through SGE command-line tools.

**Requirements:**
*   **LIB-FR-006.1:** Users shall submit jobs using the standard `qsub` command with extended directives for `budget`, `deadline`, and `estimated_time`.
*   **LIB-FR-006.2:** Users shall monitor the status of their own jobs using the standard `qstat` command, enhanced with Libra-specific fields (e.g., tickets, estimated completion time).
*   **LIB-FR-006.3:** Users shall cancel their own pending or running jobs using the `qdel` command.
*   **LIB-FR-006.4:** The administrator shall view the status of all jobs and all cluster nodes via an enhanced `qstat` or a dedicated Libra admin command.
*   **LIB-FR-006.5:** The administrator shall modify global scheduling parameters (e.g., base price, ticket conversion function) via a configuration file or admin command.
*   **LIB-FR-006.6:** The administrator shall have the authority to suspend (`qmod -s`), resume (`qmod -us`), or cancel (`qdel`) any job in the system.

## 4. Non-Functional Requirements

### 4.1 Performance Requirements
*   **LIB-NFR-001 (Response Time):** The system shall provide a response (accept/reject) to a job submission request within **60 seconds** of receipt from SGE, under normal cluster load (<90% utilization).
*   **LIB-NFR-002 (Scheduling Overhead):** The CPU overhead of the Libra scheduling daemon shall not exceed 5% of a single CPU core on the master node.

### 4.2 Reliability & Availability Requirements
*   **LIB-NFR-003 (Deadline Adherence):** For jobs with accurate execution time estimates, the system shall complete execution within **±10%** of the user-specified deadline, in 95% of cases.
*   **LIB-NFR-004 (Recovery Time):** In the event of a software failure of the Libra scheduler, recovery (restart and reconciliation of job state with SGE) shall be possible in **less than 5 minutes**.
*   **LIB-NFR-005 (Defect Rate):** The delivered code shall have a maximum defect density of **1 bug per KLOC** as measured by critical and major bugs found during system testing.

### 4.3 Security Requirements
*   **LIB-NFR-006 (Data Privacy):** A user shall only be able to view the detailed status (beyond basic queue position) and accounting information for their own jobs. Job status and financial data must be kept private from other users.
*   **LIB-NFR-007 (Authorization):** Only users with authenticated administrator privileges shall be permitted to alter global scheduling criteria, pricing models, or resource allocation policies.
*   **LIB-NFR-008 (Integrity):** The system shall ensure that a user's budget is accurately debited for used resources and cannot be corrupted by other user's jobs or system errors.

### 4.4 Supportability & Maintainability Requirements
*   **LIB-NFR-009 (Coding Standards):** All source code shall conform to the Hungarian Naming Convention and GNU coding standards, as verified by a code review checklist.
*   **LIB-NFR-010 (Documentation):** All external APIs (especially the SGE interface module) shall be fully documented in the code (using a format like Doxygen) and in a separate integration guide.
*   **LIB-NFR-011 (Configurability):** Economic parameters (base price, ticket calculation function) shall be configurable via a well-documented text configuration file without requiring code recompilation.

### 4.5 Portability Constraint
*   **LIB-NFR-012:** The system is initially required to run only on the specified test environment (Pentium-III, Linux, SGE 5.3). However, code shall avoid non-portable constructs to facilitate future migration.

## 5. Acceptance Criteria

The Libra system will be considered acceptable upon successful demonstration of the following in the test environment:

1.  **Core Scheduling Functionality:** The system correctly accepts/rejects jobs based on budget and deadline, calculates tickets/stride, dispatches jobs via SGE, and enforces stride-based CPU sharing.
2.  **Performance Metrics:**
    *   Job submission response time is consistently under 60 seconds.
    *   For a test suite of jobs with accurate runtimes, 95% complete within 10% of their specified deadlines.
3.  **Integration:** The system operates stably as an add-on to SGE 5.3 without causing SGE failures or requiring SGE modifications.
4.  **Security & Administration:** User job privacy is maintained, and administrative functions (job control, parameter configuration) work as specified.

*Note: The development of an economic pricing front-end and a dedicated GUI are explicitly deferred and are not part of the acceptance criteria for this release.*