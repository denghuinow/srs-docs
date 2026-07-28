# Software Requirements Specification (SRS) for Libra Scheduler Add-on

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review  
**Author:** SRS Development Team

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for "Libra," an economy-driven scheduler add-on for the Sun Grid Engine (SGE) cluster management system. The primary purpose of this document is to provide a detailed description of the system to be developed, serving as a foundation for design, implementation, testing, and project management. The intended audience includes software developers, system architects, test engineers, project managers, and stakeholders.

### 1.2 Scope
Libra is a software sub-component that integrates with an existing Sun Grid Engine (SGE) installation on a homogeneous Linux cluster. It introduces a computational economy model for scheduling sequential and embarrassingly parallel batch jobs. The system will manage job acceptance, scheduling, and dispatch based on user-defined budget and deadline constraints, employing heuristic-based algorithms for efficiency. The scope excludes:
*   Modification of the core Sun Grid Engine system.
*   Support for tightly-coupled parallel jobs (e.g., MPI).
*   Management of heterogeneous hardware resources.
*   A graphical user interface (GUI); interaction is via SGE command-line interfaces and configuration files.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SGE** | Sun Grid Engine, a distributed resource management (DRM) system. |
| **QoS** | Quality of Service. |
| **Embarrassingly Parallel** | A workload where tasks can be executed independently with no communication between them. |
| **Stride Scheduling** | A deterministic fair-share scheduling algorithm that assigns tickets and calculates a "stride" for each job. |
| **Bid** | A user-submitted value representing the maximum amount of "currency" they are willing to pay for a job. |
| **Heuristic** | A practical, non-exhaustive method for problem-solving that is sufficient for reaching an immediate, short-term goal. |
| **Homogeneous Cluster** | A compute cluster where all nodes have identical or very similar hardware and software configurations. |

### 1.4 References
*   Sun Grid Engine (SGE) Administration Guide.
*   Waldspurger, C. A., & Weihl, W. E. (1995). *Stride Scheduling: Deterministic Proportional-Share Resource Management*.
*   IEEE Std 830-1998 - Recommended Practice for Software Requirements Specifications.

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details specific external interface requirements. Section 4 enumerates all system features and functional requirements. Section 5 specifies non-functional requirements, including performance and design constraints.

## 2. Overall Description

### 2.1 Product Perspective
Libra is an add-on module that sits within the SGE architecture. It interfaces with SGE's scheduling components (`schedd`) and execution daemons (`execd`). The relationship is shown below:

```
[User] -> [qsub] -> [SGE Master (qmaster)]
                          |
                    [Libra Scheduler Add-on] --(accept/reject)--> [SGE Scheduling Logic]
                          |                                           |
                    [Economic Model & Queue]                     [Dispatch Decision]
                          |                                           |
                    [Job Dispatcher] -----------------------------> [SGE Execution Daemons (execd)]
```

Libra extends SGE's default scheduling policies but does not replace them. It operates as a specialized decision layer for jobs submitted with economic constraints.

### 2.2 Product Functions
The core functions of Libra are:
1.  **Constraint-Based Job Admission:** Evaluate incoming batch jobs submitted with a budget and deadline. Accept or reject them based on current system load, economic model state, and feasibility of meeting the deadline.
2.  **Economic Scheduling:** Manage a queue of accepted jobs using a proportional-share model. User bids determine resource share. The stride scheduling algorithm will be used to determine the order of job dispatch in a fair, deterministic manner.
3.  **Resource Selection & Dispatch:** Select appropriate compute nodes from the homogeneous cluster and initiate job execution via SGE's standard mechanisms.
4.  **Heuristic Optimization:** Apply fast, heuristic algorithms (as opposed to exhaustive combinatorial search) to make scheduling and admission decisions, ensuring low overhead.

### 2.3 User Characteristics
The primary user classes are:
*   **Cluster Users:** Scientists, researchers, or engineers who submit batch jobs. They are familiar with SGE commands (`qsub`, `qstat`) and understand the concepts of budget (virtual currency) and job deadlines.
*   **Cluster Administrators:** System personnel who install, configure, and maintain the SGE cluster and the Libra add-on. They possess in-depth knowledge of SGE architecture and Linux system administration.

### 2.4 Constraints
1.  **Integration Constraint:** Must function solely as a sub-component of the Sun Grid Engine (SGE) cluster management system. It cannot be a standalone scheduler.
2.  **Implementation Language:** All source code must be written in standard C (e.g., ANSI C99).
3.  **Algorithmic Constraint:** The scheduler is explicitly prohibited from performing exhaustive searches for optimal job combinations. All decision-making must be based on defined heuristics to ensure predictable and low-latency operation.
4.  **Platform Constraint:** Target environment is a homogeneous Linux cluster.

### 2.5 Assumptions and Dependencies
*   A functioning Sun Grid Engine (version 6.2 or compatible) cluster is already installed and configured.
*   The cluster is homogeneous (identical node configuration).
*   Jobs submitted to Libra are either sequential (single-core) or embarrassingly parallel (multiple independent tasks).
*   A virtual currency system for users is managed externally (e.g., via SGE user complexes or a separate database), though the interface to it is within scope.

## 3. External Interface Requirements

### 3.1 User Interfaces
*   **Job Submission:** Users will submit jobs using the standard `qsub` command with special Libra-specific parameters.
    ```bash
    # Example:
    qsub -l budget=500,deadline=2023-10-28T18:00:00 my_job_script.sh
    ```
*   **Job Monitoring:** Users will query job status using the standard `qstat` command. Libra will extend the output to include economic metrics (e.g., budget consumed, effective share).
*   **Administration:** Administrators will configure Libra via a dedicated configuration file (e.g., `libra_settings.conf`) and use SGE administrative commands (`qconf`) to enable the scheduler.

### 3.2 Hardware Interfaces
Libra will interface with the cluster hardware indirectly through SGE. It must be capable of querying SGE for node states (free/busy, load) and resource availability.

### 3.3 Software Interfaces
1.  **Sun Grid Engine API/Library:** Libra must interface with SGE's internal scheduling API (e.g., the `sge_gdi` (Grid Database Interface) and scheduling hooks) to receive job submissions, query cluster state, and dispatch jobs.
2.  **Standard C Library:** Use of `libc` for all standard operations.
3.  **Configuration File:** Parse a simple key-value or structured text configuration file for parameters like heuristic coefficients, stride scheduling intervals, and default policies.

### 3.4 Communications Interfaces
Libra will use the same communication protocols as SGE (typically TCP/IP-based internal communication) for inter-process communication between the `qmaster`, `schedd`, and `execd` daemons. No new network protocols are required.

## 4. System Features

### 4.1 Feature 1: Job Admission Control
**Description:** This feature evaluates each job submitted with Libra parameters and decides to admit it to the economic queue or reject it immediately.

**4.1.1 Functional Requirements:**
*   **FR-1.1:** The system shall parse `budget` and `deadline` parameters from jobs submitted via `qsub`.
*   **FR-1.2:** The system shall estimate the computational cost (in node-time) required for the submitted job based on historical data or user-provided hints.
*   **FR-1.3:** The system shall execute a heuristic admission algorithm that considers the job's budget, deadline, estimated cost, and current system load/queue.
*   **FR-1.4:** The system shall reject any job where the budget is insufficient to meet the deadline under the current and projected load, according to the heuristic model.
*   **FR-1.5:** The system shall return a clear error message to the user via SGE upon job rejection.
*   **FR-1.6:** The system shall place accepted jobs into the managed economic job queue.

### 4.2 Feature 2: Economic Scheduling with Stride Algorithm
**Description:** This feature manages the queue of admitted jobs, allocating resource shares proportionally to user bids and determining dispatch order.

**4.2.1 Functional Requirements:**
*   **FR-2.1:** The system shall assign each job a number of "tickets" proportional to its submitted `budget`.
*   **FR-2.2:** The system shall implement the stride scheduling algorithm to determine the next job to receive a resource allocation (time slice on a node).
    *   *Calculation:* `Stride = K / Tickets`, where K is a large constant.
    *   *State:* Maintain a `pass` counter for each job, initialized to 0.
    *   *Selection:* Select the job with the smallest `pass` value, increment its `pass` by its `stride`.
*   **FR-2.3:** The system shall re-calculate resource shares dynamically when a new job is admitted or a running job completes.
*   **FR-2.4:** The system shall decrement a job's remaining budget as it consumes resources based on a defined cost-per-unit-time.

### 4.3 Feature 3: Job Dispatch & Execution
**Description:** This feature selects an appropriate cluster node and initiates the execution of the job selected by the scheduler.

**4.3.1 Functional Requirements:**
*   **FR-3.1:** The system shall query SGE for the list of available, healthy nodes in the homogeneous cluster.
*   **FR-3.2:** For a selected job, the system shall select a node using a heuristic (e.g., first available, least loaded) that is compatible with the job's resource request.
*   **FR-3.3:** The system shall dispatch the job to the selected node using the standard SGE job dispatch mechanism.
*   **FR-3.4:** The system shall monitor the status of dispatched jobs (start, completion, failure) via SGE callbacks.
*   **FR-3.5:** Upon job completion or failure, the system shall update its internal queue, release resources, and make the scheduler ready for the next decision cycle.

### 4.4 Feature 4: Configuration and Administration
**Description:** This feature allows system administrators to configure the behavior of the Libra scheduler.

**4.4.1 Functional Requirements:**
*   **FR-4.1:** The system shall read its operational parameters from a configuration file at startup.
*   **FR-4.2:** The configuration shall include parameters such as:
    *   Base cost per CPU-hour.
    *   Heuristic coefficients for admission control.
    *   Stride scheduling constant (K).
    *   Scheduling cycle interval.
*   **FR-4.3:** The system shall log its major activities (admission decisions, scheduling events, errors) to the SGE master daemon log or a dedicated log file.

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
*   **PR-1:** The admission decision heuristic (FR-1.3) must complete in O(n) time or better relative to the current queue size `n`.
*   **PR-2:** The scheduling decision cycle (selecting the next job via stride) must have constant time complexity, O(1).
*   **PR-3:** The scheduler's overhead (admission + scheduling logic) shall not increase the average job submission-to-dispatch latency by more than 10% compared to native SGE.

### 5.2 Safety & Security Requirements
*   **SR-1:** The scheduler shall not allow a user to consume resources beyond their allocated budget. Enforcement must happen at the scheduler level before dispatch.
*   **SR-2:** The system shall inherit the user authentication and authorization model of the underlying SGE system. Libra shall not implement its own security model.

### 5.3 Software Quality Attributes
*   **Maintainability:** The code shall be modular, with clear separation between admission logic, scheduling logic, and SGE interface. It shall be well-commented.
*   **Reliability:** The scheduler must be resilient to malformed job parameters, defaulting to a safe rejection policy without crashing.
*   **Portability:** While dependent on SGE, the C code shall adhere to standard C (C99) and avoid platform-specific constructs to the maximum extent possible.

### 5.4 Design Constraints
*   **DC-1:** As stated in Section 2.4, the implementation language is Standard C.
*   **DC-2:** The solution must be an add-on to SGE, not a fork or a replacement of its core components.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Manager | | | |
| Lead Architect | | | |
| QA Manager | | | |