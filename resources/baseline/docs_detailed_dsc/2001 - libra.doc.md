# Software Requirements Specification (SRS)
## For Libra: An Economy-Driven Cluster Scheduler

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft  
**Project:** Libra Scheduler Add-on for Sun Grid Engine

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Libra scheduler, an economy-driven add-on for the Sun Grid Engine (SGE) cluster management system. It is intended for use by the project development team, stakeholders, and quality assurance personnel to guide the design, implementation, and validation of the system.

#### 1.2 Scope
Libra is a Quality of Service (QoS) scheduler that introduces a computational economy model to a homogeneous Linux cluster managed by SGE. It schedules CPU time for sequential and embarrassingly parallel batch jobs based on user-defined utility (budget and deadline), enforcing proportional resource sharing via a bid-based economic model and the stride scheduling algorithm.

**In-Scope:**
*   Integration with Sun Grid Engine 5.3 as an add-on module.
*   Management of sequential and embarrassingly parallel (parametric) jobs.
*   Job acceptance/rejection based on economic feasibility.
*   Dynamic priority calculation (tickets, stride) using a user's budget and deadline.
*   Load-balanced dispatch to the least-loaded execution node.
*   Proportional CPU time-slicing on each node using stride scheduling.
*   Command-line interfaces for users and administrators.
*   Centralized cluster status tracking.

**Out of Scope (Non-Goals):**
*   Support for tightly-coupled parallel jobs with inter-process communication dependencies (e.g., MPI with synchronization).
*   Job migration for resource defragmentation.
*   A full-fledged graphical user interface (GUI) in the initial release.
*   Management of heterogeneous hardware resources.
*   Scheduling of resources beyond CPU (e.g., GPU, specialized hardware) in the initial release.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SGE:** Sun Grid Engine.
*   **QoS:** Quality of Service.
*   **CLI:** Command Line Interface.
*   **GUI:** Graphical User Interface.
*   **PVM/MPI:** Parallel Virtual Machine / Message Passing Interface (libraries for parallel computing).
*   **Ticket:** A unit representing a job's share of CPU resources in the stride scheduling algorithm.
*   **Stride:** The inverse of tickets; determines the interval between CPU allocations for a job.
*   **Pass:** A counter used by the stride scheduler to determine which job runs next.
*   **Quantum:** A fixed unit of CPU time allocated to a job during a scheduling cycle.

#### 1.4 References
*   Sun Grid Engine 5.3 Administration & User Documentation.
*   Waldspurger, C. A., & Weihl, W. E. (1995). *Stride Scheduling: Deterministic Proportional-Share Resource Management*.
*   GNU General Public License (GPL) v2 or later.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its stakeholders, and operating environment. Section 3 details the specific functional and non-functional requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
Libra is a dependent add-on module that sits within the SGE ecosystem. It intercepts job submissions, applies its economic scheduling logic, and instructs SGE on where and how to queue jobs. SGE remains responsible for low-level resource management, job dispatch, and interaction with the operating system.

#### 2.2 Stakeholders and User Classes
| Stakeholder Class | Description | Key Interests |
| :--- | :--- | :--- |
| **Cluster User** | Researcher or engineer submitting computational jobs. | Submitting jobs with budget/deadline constraints, monitoring job status and cost, managing own job queue. |
| **Cluster Administrator** | Responsible for cluster health, policy, and user support. | Monitoring system load and node status, configuring scheduling policies and cost models, controlling any job for administrative purposes. |
| **SGE System** | The underlying cluster management infrastructure. | Receiving scheduling decisions from Libra, managing job queues, dispatching to execution hosts. |
| **Development Team** | Engineers building and maintaining Libra. | Clear requirements, testable components, manageable integration points. |

#### 2.3 Operating Environment
*   **Software:** Sun Grid Engine 5.3, Linux Operating System (kernel 2.4+), PVM/MPI libraries for parallel jobs.
*   **Hardware:** Homogeneous Linux cluster (initially a 4-node Pentium-III test cluster).
*   **Network:** High-speed interconnect (e.g., Fast Ethernet, Gigabit Ethernet) for cluster communication.

#### 2.4 Design and Implementation Constraints
1.  Must comply with SGE 5.3's external scheduler interface (API).
2.  Initial release must be command-line focused.
3.  Source code must be released under the GNU GPL license.
4.  Core scheduling algorithms must be heuristic-based to ensure sub-minute response times.

#### 2.5 User Documentation
Initial release will include:
*   A man page for user commands (`libra_submit`, `libra_status`, `libra_cancel`).
*   An administrator guide detailing installation, configuration, and policy management.
*   API documentation for developers extending the economic model.

#### 2.6 Assumptions and Dependencies
*   Users can provide a reasonable estimate of their job's execution time.
*   SGE 5.3 is correctly installed and configured on the cluster.
*   The cluster is homogeneous in terms of CPU performance for accurate stride scheduling.
*   Job workloads are primarily CPU-bound.

### 3. System Requirements

#### 3.1 Functional Requirements

**3.1.1 Job Submission & Feasibility Analysis**
*   **FR-1:** The system shall accept job submission parameters from SGE, including: Job ID, User ID, executable path, estimated runtime (T_est), budget (B), and deadline (D).
*   **FR-2:** The system shall evaluate the feasibility of accepting a new job based on current cluster load, the job's T_est, B, and D.
*   **FR-3:** If the job is deemed infeasible (cannot meet deadline with available resources/budget), the system shall reject the job and may suggest an alternative feasible deadline or minimum budget to the user via SGE.
*   **FR-4:** If the job is feasible, the system shall calculate the job's priority in the form of **tickets**, derived from the function `Tickets = f(B, D, T_est, System_Load)`.

**3.1.2 Scheduling & Dispatch**
*   **FR-5:** The system shall calculate a **stride** value for each accepted job as the inverse of its tickets (e.g., `Stride = K / Tickets`, where K is a large constant).
*   **FR-6:** The system shall select an execution host for the job by identifying the node with the lowest current CPU load that can accommodate the job type.
*   **FR-7:** The system shall select an appropriate SGE queue on the target host based on the job's type (sequential or parallel).
*   **FR-8:** The system shall dispatch the job to the selected host and queue by instructing SGE.
*   **FR-9:** The system shall maintain a central **Cluster Status** record, updating it with new `ResourceAllocation` entries (Job ID, Host ID, Queue ID, start time, quantum).

**3.1.3 Job Execution & Resource Sharing**
*   **FR-10:** On each execution host, a **stride scheduler** shall manage the local queue, allocating CPU quanta to jobs in proportion to their ticket allocation.
*   **FR-11:** The stride scheduler shall use a `pass` counter for each job, incrementing it by the job's `stride` upon each CPU allocation, and always select the job with the smallest `pass` value to run next.
*   **FR-12:** The system shall support the execution of embarrassingly parallel jobs by leveraging PVM/MPI libraries to spawn and manage multiple independent processes across allocated CPU slices.

**3.1.4 Monitoring & Control**
*   **FR-13:** A user shall be able to query the status (Pending, Running, Completed, Cancelled, Rejected) and economic metrics (cost incurred, deadline proximity) of their own submitted jobs via a CLI.
*   **FR-14:** An administrator shall be able to view the status of all cluster nodes (hostId, cpuLoad, availableMemory, status), overall cluster load, and the status of all jobs via a CLI.
*   **FR-15:** An administrator shall be able to modify global scheduling policies and cost structure parameters (e.g., base cost per CPU-hour, urgency multipliers).
*   **FR-16:** Both users and administrators shall be able to cancel any pending or running job. The system shall update the Cluster Status to free resources and recalculate schedules if necessary.

**3.1.5 Integration**
*   **FR-17:** The system shall integrate with SGE 5.3 via its defined external scheduler interface.
*   **FR-18:** The system shall interact with the Linux OS to enforce CPU time quanta for processes.

#### 3.2 Domain Model (Data Requirements)
The system shall maintain persistent or runtime data for the following entities:
```yaml
User:
  attributes: id (PK), name, authentication_credentials

Job:
  attributes: id (PK), userId (FK to User), type [sequential, parallel],
              estimatedRuntime, budget, deadline, status [pending, running, completed, cancelled, rejected]

ExecutionHost (Node):
  attributes: hostId (PK), clusterId, cpuLoad, availableMemory, status [up, down, busy]

Queue:
  attributes: queueId (PK), hostId (FK to ExecutionHost), jobTypePolicy

SchedulingInfo:
  attributes: jobId (PK, FK to Job), tickets, stride, pass

ResourceAllocation:
  attributes: allocationId (PK), jobId (FK to Job), hostId (FK to ExecutionHost),
              queueId (FK to Queue), startTime, quantum
```

#### 3.3 External Interface Requirements

**3.3.1 Software Interfaces**
*   **SI-1: Sun Grid Engine 5.3**
    *   **Direction:** Libra ← SGE
    *   **Protocol/API:** SGE External Scheduler Interface (DRMAA or specific callbacks).
    *   **Input:** Job submission events with parameters.
    *   **Output:** Job acceptance/rejection signals, host/queue dispatch instructions.

**3.3.2 Hardware Interfaces**
*   **HI-1:** Standard x86 server hardware compatible with Linux and SGE 5.3.

**3.3.3 User Interfaces**
*   **UI-1: User CLI**
    *   **Command:** `libra_submit -exe <file> -t <runtime> -b <budget> -d <deadline>`
    *   **Command:** `libra_status -j <jobid> | -u <userid> | -a`
    *   **Command:** `libra_cancel <jobid>`
*   **UI-2: Administrator CLI**
    *   **Command:** `libra_admin -nodes` # View node status
    *   **Command:** `libra_admin -policy set <param> <value>` # Adjust policy
    *   **Command:** `libra_admin -job kill <jobid>` # Force cancel job

#### 3.4 Non-Functional Requirements

**3.4.1 Performance**
*   **NF-1:** The time from user job submission to a definitive accept/reject response shall be less than 1 minute under normal load.
*   **NF-2:** For jobs with accurate `T_est`, the scheduler shall complete execution within a window of `Deadline ± 10%`.

**3.4.2 Reliability & Availability**
*   **NF-3:** The code quality target is a maximum defect density of 1 bug per thousand lines of code (1 bug/KLOC).
*   **NF-4:** In the event of a scheduler restart, recovery of cluster state and resumption of scheduling shall complete within 5 minutes.

**3.4.3 Security**
*   **NF-5:** Users shall only be able to view and modify the status of jobs they own.
*   **NF-6:** Only authenticated administrators shall be allowed to modify scheduling policies or cancel any user's job.
*   **NF-7:** Job data (executables, input/output) privacy shall be enforced by underlying OS and SGE permissions.

**3.4.4 Compliance**
*   **NF-8:** The entire codebase shall be released under the GNU General Public License (GPL) v2 or later.

**3.4.5 Observability**
*   **NF-9:** The administrator CLI shall provide real-time insight into per-node CPU load, memory availability, and a list of all active jobs with their economic parameters (budget, tickets, deadline).

### 4. Appendices

#### 4.1 Acceptance Criteria (Verification)
*   **AC-1 (QoS-driven Acceptance):**
    *   *Test:* Submit a high-budget job when cluster load is >80%. *Result:* Job is accepted and assigned a high ticket count relative to running jobs.
    *   *Test:* Submit a job with a deadline 1 minute in the future for a 10-minute `T_est` job. *Result:* Job is rejected with a message suggesting a feasible later deadline.
*   **AC-2 (Proportional Sharing):**
    *   *Test:* Run two jobs on one host with ticket allocations 100 and 300. Monitor CPU usage over time. *Result:* The second job receives approximately 75% of the CPU quanta, the first receives ~25%.
*   **AC-3 (Load Balancing):**
    *   *Test:* With a 4-node cluster where nodes have loads of 90%, 30%, 70%, and 10%, submit a new job. *Result:* The job is dispatched to the node with 10% load.

#### 4.2 Undecided Issues & Open Questions
| Issue | Description | Responsible Party | Notes |
| :--- | :--- | :--- | :--- |
| **UI-01** | Detailed algorithm for pricing and cost accounting (`f(B, D, T_est, Load)`). | Economic Model Lead | Core to the economic model. Requires simulation. |
| **T-01** | Build a custom simulation tool vs. acquire/adapt an existing one for algorithm testing. | Project Lead | Impacts early validation timeline. |
| **ALG-01** | Specification of heuristics for the NP-hard optimal scheduling problem. | Scheduling Algorithm Lead | Necessary to meet NF-1 (response time <1 min). |
| **UI-02** | Full design of a web-based or desktop GUI for users and admins. | UI/UX Lead | Post-MVP feature. |
| **FUT-01** | Strategy for extending the model to heterogeneous clusters or GPU resources. | Future Scope Lead | For future roadmap planning. |

---
*This document was generated based on the provided project summary.*