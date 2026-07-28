# Software Requirements Specification (SRS)
## Libra: An Economy-Driven Cluster Scheduler

**Document Version:** 1.0
**Date:** [Date of Generation]
**Authors:** Project Group (Jahanzeb Sherwani, Nosheen Ali, Nausheen Lotia, Zahra Hayat)
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Libra scheduler, an economy-driven add-on to the Sun Grid Engine (SGE) cluster management system. It is intended for stakeholders, including the development team, faculty advisors, cluster administrators, and end-users, to serve as a definitive guide for the system's design, implementation, and validation.

#### 1.2 Scope
Libra is a Quality of Service (QoS) scheduler that allocates CPU time on a homogeneous Linux compute cluster based on user-defined budget and deadline constraints. It operates as an extension to SGE v5.3, managing sequential and embarrassingly parallel batch jobs. The core innovation is shifting from system-centric scheduling (e.g., maximizing throughput) to a user-centric, economy-driven model where CPU time is proportionally shared according to a user's utility.

**In-Scope:**
*   Integration with SGE's job submission and management interfaces.
*   A stride-scheduling algorithm for proportional CPU time allocation.
*   Job admission control based on budget and deadline feasibility.
*   Monitoring interfaces for users and administrators.
*   Management of user credit balances (conceptual).

**Out-of-Scope:**
*   Management of interactive or tightly-coupled parallel (non-embarrassing) jobs.
*   Scheduling of non-CPU resources (e.g., GPU, specialized hardware) as primary factors.
*   A full-fledged financial transaction system or billing interface.
*   Native job execution (relies on SGE/PVM/MPI).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SGE:** Sun Grid Engine.
*   **QoS:** Quality of Service.
*   **Batch Job:** A non-interactive job submitted for execution.
*   **Embarrassingly Parallel Job:** A job consisting of multiple independent tasks that can be executed concurrently with minimal communication.
*   **Stride Scheduling:** A proportional-share scheduling algorithm where a job's share of CPU is determined by its "stride" (inverse of tickets).
*   **Ticket:** A unit representing a share of resource allocation in stride scheduling.
*   **Pass Value:** A dynamic counter used by the stride scheduler to determine the next job to run.
*   **PVM/MPI:** Parallel Virtual Machine / Message Passing Interface (libraries for parallel execution).

#### 1.4 References
1.  Sun Grid Engine v5.3 Administration & User Documentation.
2.  Project Charter: "Libra: A Scalable Economy-Driven Cluster Scheduler."
3.  Waldspurger, C.A. and Weihl, W.E. (1995). "Stride Scheduling: Deterministic Proportional-Share Resource Management."

#### 1.5 Overview
The remainder of this SRS is organized as follows: Section 2 provides a general description of the product. Section 3 details specific requirements, including functional requirements, data models, and non-functional constraints. Appendices may include supplementary diagrams or analysis.

### 2. Overall Description

#### 2.1 Product Perspective
Libra is a dependent subsystem that integrates with the existing SGE architecture. It intercepts and enhances SGE's scheduling decisions. The relationship is shown below:

```
[User] --(qsub with budget/deadline)--> [SGE Frontend] --> [Libra Scheduler Module]
                                                                      |
                                                                      v
[Cluster Nodes] <--(job dispatch)-- [SGE Execution Daemons] <--(schedule info)--
```

**System Interfaces:**
*   **SGE:** Primary interface for job submission, queue management, and host selection.
*   **Cluster Nodes:** Homogeneous Linux machines managed by SGE.
*   **User/Admin CLI:** Command-line tools (`qsub`, `qstat`, `qalter`, `qdel`) extended by Libra.

#### 2.2 Product Functions
The high-level functions of Libra are:
1.  **Job Admission Control:** Evaluate and accept/reject jobs based on economic feasibility.
2.  **Proportional-Share Scheduling:** Allocate CPU time quanta to jobs using a stride-scheduling algorithm based on user budget and urgency.
3.  **Economic Management:** Map user budgets and deadlines to scheduling parameters (tickets/stride).
4.  **Status Reporting:** Provide enhanced job and cluster status information reflecting economic scheduling.
5.  **Administrative Control:** Allow administrators to configure policies and intervene in job scheduling.

#### 2.3 User Characteristics
| Actor | Expertise | Primary Interaction |
| :--- | :--- | :--- |
| **Cluster User** | Knowledge of their application, basic SGE command-line usage. | Submits jobs with QoS parameters, monitors own jobs. |
| **Cluster Administrator** | Expert in SGE administration, Linux systems, and cluster policies. | Configures Libra, monitors overall cluster health and economic balance, manages all jobs. |
| **Project Developer** | Expert in C/POSIX programming, SGE internals, and scheduling algorithms. | Develops, debugs, and maintains the Libra codebase. |

#### 2.4 Constraints
1.  **Technical:** Must be compatible with SGE v5.3 API and a homogeneous Pentium-III Linux cluster.
2.  **Legal:** Code must be released under the GNU General Public License (GPL).
3.  **Implementation:** Code must adhere to the Hungarian Naming Convention.
4.  **Resource:** Initial development and testing are constrained to a 4-node cluster.

#### 2.5 Assumptions and Dependencies
*   Users provide a reasonable estimate of their job's standalone execution time.
*   The underlying SGE system is stable and functions correctly.
*   The economic model assumes a direct relationship between budget, deadline, and desired CPU share.
*   Success is dependent on the availability of the 4-node test cluster and SGE v5.3 software.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 Job Submission & Management (User-Facing)**
*   **FR-1:** The system shall allow a user to submit a batch job by extending the SGE `qsub` command to include the following mandatory parameters:
    *   `-b <budget>`: User's allocated credit for the job.
    *   `-dl <deadline>`: Absolute time by which the job must complete.
*   **FR-2:** The system shall allow a user to query the status of their jobs via an enhanced `qstat` command, displaying Libra-specific fields (e.g., allocated tickets, current pass value, economic status).
*   **FR-3:** The system shall allow a user to cancel their own pending or running job via the `qdel` command, triggering immediate cessation and resource deallocation.
*   **FR-4:** The system shall authenticate all user commands using the underlying SGE/user system authentication.

**3.1.2 Scheduler Core (Admission & Scheduling)**
*   **FR-5:** Upon receiving a new job from SGE, the scheduler shall parse the job's budget, deadline, and estimated runtime.
*   **FR-6:** The scheduler shall execute an admission control algorithm to **Accept** or **Reject** the job. A job shall be rejected if, given current cluster load and committed resources, it is deemed impossible to complete before its deadline within its budget.
*   **FR-7:** For each accepted job, the scheduler shall calculate its number of **Tickets**. The ticket count shall be a function of the job's budget and the urgency derived from its deadline (`Tickets = f(budget, deadline, current_time)`).
*   **FR-8:** The scheduler shall calculate a **Stride** for each job as a large constant (e.g., 10,000) divided by its number of tickets (`Stride = K / Tickets`).
*   **FR-9:** The scheduler shall maintain a **Pass** value for each job in a queue, initialized to its stride.
*   **FR-10:** When a CPU on a node becomes available, the scheduler shall select the job with the **minimum Pass value** from the node's active queue for execution.
*   **FR-11:** After a job runs for a scheduling quantum, the scheduler shall increment its Pass value by its Stride (`Pass_new = Pass_old + Stride`).
*   **FR-12:** The scheduler shall select the execution host for a job as the least-loaded node capable of running the job, as determined by SGE's load sensors.

**3.1.3 Administration & Monitoring**
*   **FR-13:** The system shall provide an administrative command to view the detailed status of all cluster nodes, including CPU load, memory, queue lengths, and aggregate economic commitment.
*   **FR-14:** The system shall provide an administrative command to alter the global scheduling policy parameters (e.g., the function `f()` in FR-7, the constant `K` in FR-8).
*   **FR-15:** The system shall allow an administrator to cancel, suspend, or resume any job on the cluster, overriding user permissions.

#### 3.2 Data Requirements & Domain Model

**3.2.1 Logical Data Model**
*   **Job (`Job`):**
    *   `job_id` (PK): Integer. Unique identifier from SGE.
    *   `user_id` (FK): String. Submitting user.
    *   `type`: Enum {Sequential, Parallel}.
    *   `est_execution_time`: Integer (seconds).
    *   `budget`: Float (credits).
    *   `deadline`: Timestamp.
    *   `status`: Enum {PENDING, RUNNING, COMPLETED, CANCELLED, REJECTED}.
    *   `executable_path`: String.
*   **Scheduling Instance (`Scheduling_Ticket`):**
    *   `job_id` (PK, FK): Integer.
    *   `node_id` (PK, FK): Integer.
    *   `ticket_count`: Integer.
    *   `stride`: Integer.
    *   `current_pass`: Integer.
*   **Execution Node (`Execution_Host`):**
    *   `node_id` (PK): Integer.
    *   `hostname`: String.
    *   `cpu_load`: Float (0.0 - 1.0).
    *   `available_memory`: Integer (MB).
    *   `status`: Enum {ACTIVE, DOWN, SUSPENDED}.
*   **Queue (`Queue`):**
    *   `queue_id` (PK): String.
    *   `node_id` (FK): Integer.
    *   `scheduling_policy`: String (default: "libra_stride").

#### 3.3 Non-Functional Requirements

| ID | Requirement Category | Specific Requirement | Verification Method |
| :--- | :--- | :--- | :--- |
| **NFR-1** | Performance | Job submission (accept/reject decision) response time shall be ≤ 60 seconds. | Load testing with simulated job bursts. |
| **NFR-2** | Reliability | The delivered code shall have a defect density of ≤ 1 bug per KLOC. | Code review & testing metrics tracking. |
| **NFR-3** | Scalability | Scheduling decision latency shall show no more than logarithmic degradation as the number of active jobs increases from 10 to 1000. | Simulation testing with increasing load. |
| **NFR-4** | Security | User A shall not be able to view, modify, or cancel the jobs of User B. | Penetration testing of SGE/Libra interface. |
| **NFR-5** | QoS (Deadline) | For jobs with accurate execution time estimates, ≥ 90% shall complete within 110% of their submitted deadline. | Controlled test suite with known job profiles. |
| **NFR-6** | Supportability | All source code shall follow the Hungarian Naming Convention. | Automated code style checking. |
| **NFR-7** | Supportability | The system shall be licensed under the GNU GPL. | License file inclusion in repository. |

#### 3.4 External Interface Requirements
*   **CLI:** Shall extend SGE commands (`qsub`, `qstat`, `qdel`) seamlessly. New options must follow SGE's `-option <value>` convention.
*   **SGE Integration API:** Shall use the SGE DRMAA (Dynamic Resource Management Application API) or native SGE scheduler event interface for intercepting jobs and providing scheduling hints.

### 4. Appendices

#### 4.1 Undecided Issues & Open Questions
1.  **Economic Model:** The precise formula `f(budget, deadline, current_time)` for calculating tickets is TBD. Options include linear, exponential, or weighted combinations.
2.  **GUI:** Decision pending on developing a custom GUI for visualization vs. using command-line tools only.
3.  **Simulation Tool:** Will evaluate existing tools (e.g., SimGrid, CloudSim) vs. developing a light-weight custom simulator.
4.  **Job Modification:** The feasibility and mechanism for allowing users to modify non-critical job parameters post-submission requires further analysis of SGE's `qalter` capabilities.

#### 4.2 Risk Management Summary
*   **Primary Technical Risk:** Complexity of stride algorithm integration with SGE's native scheduler.
    *   **Mitigation:** Develop a standalone prototype of the stride scheduler first, then integrate.
*   **Primary Validation Risk:** Small test cluster size limiting performance and scalability assessment.
    *   **Mitigation:** Prioritize the development/acquisition of a simulation tool for large-scale tests.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Owner | Rajkumar Buyya | | |
| Faculty Advisor | Dr. Arif Zaman | | |
| Lead Developer | Jahanzeb Sherwani | | |