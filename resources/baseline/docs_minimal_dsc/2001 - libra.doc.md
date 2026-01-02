# Software Requirements Specification (SRS)
## Economy-Driven Cluster Scheduler Add-on for Sun Grid Engine (SGE)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for an economy-driven cluster scheduler add-on for the Sun Grid Engine (SGE) management system. The purpose of this software is to provide Quality of Service (QoS) guarantees by scheduling batch jobs based on user-submitted budget and deadline constraints, using a proportional resource-sharing economic model. This SRS is intended for use by the development team, project stakeholders, and quality assurance personnel.

#### 1.2 Scope
The system will be an integrated component of an existing SGE cluster management system. It will manage the scheduling of sequential and embarrassingly parallel batch jobs on a homogeneous Linux cluster. The core innovation is the application of an economic model (bid-based proportional sharing) and the stride scheduling algorithm to dynamically allocate CPU time, ensuring users receive service proportional to their submitted budget while meeting specified deadlines where feasible. The system will decide on job admission, calculate scheduling parameters, and enforce CPU time allocation. It will not manage data storage, network resources, or non-CPU hardware. Initial deployment is scoped to a specific four-workstation test cluster.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SGE:** Sun Grid Engine (or Son of Grid Engine), a distributed resource management (DRM) system.
*   **QoS:** Quality of Service.
*   **DRM:** Distributed Resource Management.
*   **Batch Job:** A non-interactive computational task submitted to the cluster.
*   **Embarrassingly Parallel Job:** A job consisting of multiple independent tasks that can be executed concurrently with minimal communication.
*   **Homogeneous Cluster:** A compute cluster where all worker nodes have identical hardware and performance characteristics.
*   **Bid:** The monetary budget a user is willing to pay for their job.
*   **Deadline:** The latest time by which a user requires their job to be completed.
*   **Tickets:** A unit representing a job's share of the total system resources in proportional-share scheduling.
*   **Stride:** A fixed, inverse-priority value assigned to a job in stride scheduling.
*   **Pass:** A dynamic value used in stride scheduling to determine the next job to run (job with the smallest pass).
*   **Time Quantum:** A fixed unit of CPU time allocated to a job during scheduling.

#### 1.4 References
*   GNU General Public License (GPL), Version 2 or later.
*   Sun Grid Engine (SGE) Administration and User Documentation.
*   Waldspurger, C. A., & Weihl, W. E. (1995). *Stride Scheduling: Deterministic Proportional-Share Resource Management*.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its major functions, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements including performance, security, and design constraints.

---

### 2. Overall Description

#### 2.1 Product Perspective
This system is a **scheduler add-on module** that integrates with the existing SGE architecture. It will intercept job submission and scheduling decisions, augmenting or modifying the native SGE scheduler's behavior. The relationship is that of a plugin or external scheduler module (`sge_schedd` integration point). The system relies on SGE for core cluster management, job queueing, and task dispatch to execution hosts.

#### 2.2 Product Functions
1.  **Job Admission Control:** Evaluate incoming jobs against user constraints (budget, deadline) and current cluster state (load, resource prices) to accept or reject them.
2.  **Economic Parameter Calculation:** Translate a user's budget and deadline into scheduling parameters (tickets, stride) using a configured bid-based proportional resource-sharing model.
3.  **Proportional-Share Scheduling:** Implement the stride scheduling algorithm to select the next job to execute based on dynamically maintained pass values.
4.  **Resource Enforcement:** Allocate CPU time quanta to jobs and advance their state, ensuring the long-term distribution of CPU time matches the calculated proportional shares.
5.  **Administrative Interface:** Provide mechanisms for cluster administrators to monitor the economic state, adjust system parameters, and view scheduling decisions.

#### 2.3 User Characteristics
*   **Cluster Users (Scientific Researchers, Engineers):** These users submit batch jobs. They are technically proficient but are not experts in scheduling algorithms. Their primary concern is getting their computational work completed within their budget and by their deadline.
*   **Cluster Administrators:** These users manage the cluster infrastructure. They are highly technically proficient in Linux and SGE administration. They need to configure the economic model, monitor system fairness and utilization, and troubleshoot scheduling issues.

#### 2.4 Constraints
1.  **Integration Constraint:** Must function as a component within the Sun Grid Engine ecosystem.
2.  **Implementation Language:** Must be implemented in standard C (C99 or ANSI C).
3.  **Algorithmic Constraint:** Must use heuristic scheduling strategies; exhaustive search for optimal scheduling is explicitly prohibited due to performance requirements.
4.  **Licensing Constraint:** All source code must be released under the GNU General Public License (GPL).
5.  **Development Environment:** Initial development and unit testing are constrained to a specific four-workstation homogeneous Linux cluster.
6.  **Job Type Constraint:** Designed for sequential and embarrassingly parallel batch jobs only.

#### 2.5 Assumptions and Dependencies
*   The underlying SGE system is correctly installed, configured, and operational.
*   The cluster is homogeneous (identical CPU performance across all nodes).
*   Job runtime estimates, while potentially inaccurate, are provided by the user or a job profiling system.
*   The system assumes a stable and trusted user community; security is focused on integrity of scheduling, not malicious user isolation.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 SGE Integration Interfaces
*   **REQ-INT-1:** The module shall interface with the SGE `sge_schedd` daemon to receive job submission events and scheduling requests.
*   **REQ-INT-2:** The module shall provide scheduling decisions back to SGE in a format compatible with the SGE scheduler API.

##### 3.1.2 User Interface
*   **REQ-UI-1:** The system shall extend the SGE `qsub` command to accept new flags for `--budget` and `--deadline`.
    > **Example:** `qsub --budget 1000 --deadline 2023-12-01T18:00:00 my_job_script.sh`
*   **REQ-UI-2:** The system shall provide administrative commands (e.g., `qeco`) for administrators to view the current resource price, total pool of tickets, and per-job stride/pass values.

##### 3.1.3 Logging Interface
*   **REQ-LOG-1:** All admission decisions, stride calculations, and scheduling selections shall be logged to the SGE master daemon log (`messages`) with a unique module identifier.

#### 3.2 Functional Requirements

##### 3.2.1 Job Submission & Admission
*   **REQ-FUN-1:** The system shall accept a job submission request containing: Job Script, Budget (in abstract monetary units), and Deadline (ISO 8601 timestamp).
*   **REQ-FUN-2:** The system shall evaluate the feasibility of a new job based on a heuristic that considers:
    *   The job's budget and estimated runtime.
    *   The current global resource "price per CPU-second".
    *   The cluster's available capacity before the job's deadline.
*   **REQ-FUN-3:** The system shall immediately reject any job deemed infeasible and notify the user via SGE's standard rejection mechanism.
*   **REQ-FUN-4:** Upon acceptance, the job shall be placed into the managed queue with its calculated scheduling parameters.

##### 3.2.2 Economic Model & Parameter Calculation
*   **REQ-FUN-5:** The system shall maintain a dynamic global resource price, calculated as Total Budgets of All Active Jobs / Total Available CPU-seconds until the furthest deadline among active jobs.
*   **REQ-FUN-6:** For each accepted job, the system shall calculate its share of resources (`tickets`) as: `Tickets_job = Budget_job / (Price * Runtime_Estimate_job)`.
*   **REQ-FUN-7:** The system shall calculate a `stride` for each job as a large constant integer (e.g., 10,000) divided by the job's `tickets`. (`Stride_job = K / Tickets_job`).
*   **REQ-FUN-8:** Each job shall be initialized with a `pass` value equal to its `stride`.

##### 3.2.3 Stride Scheduling Execution
*   **REQ-FUN-9:** The scheduling loop shall, for each scheduling decision on an available CPU core, select the runnable job with the **minimum `pass` value**.
*   **REQ-FUN-10:** The system shall allocate a fixed `time quantum` (e.g., 100 ms) to the selected job.
*   **REQ-FUN-11:** After the time quantum is consumed (or the job yields/finishes), the system shall advance the job's `pass` value by its `stride` (`pass = pass + stride`).
*   **REQ-FUN-12:** The system shall re-evaluate the global resource price and all job tickets/strides upon:
    a) A new job being accepted.
    b) A job finishing and leaving the system.

##### 3.2.4 Administrative Functions
*   **REQ-FUN-13:** An administrator shall be able to view the current state of all scheduled jobs, including their budget, deadline, tickets, stride, and pass values.
*   **REQ-FUN-14:** An administrator shall be able to manually set a base global resource price, overriding the dynamic calculation.
*   **REQ-FUN-15:** An administrator shall be able to drain the system (prevent new admissions) for maintenance.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **REQ-PER-1:** The admission control heuristic shall make an accept/reject decision within 2 seconds of job submission.
*   **REQ-PER-2:** The scheduling decision logic (selecting min pass) shall have a time complexity of O(log n) or better, where n is the number of active jobs.
*   **REQ-PER-3:** The scheduler overhead shall not consume more than 2% of the total CPU resources on the master node.

##### 3.3.2 Software Quality Attributes
*   **REQ-QLT-1 (Fairness):** Over a sufficiently long period, the CPU time allocated to a job shall be proportional to its calculated tickets, with a deviation of no more than ±5%.
*   **REQ-QLT-2 (Determinism):** Given an identical sequence of job submissions and cluster state, the scheduling decisions and parameter calculations must be reproducible.
*   **REQ-QLT-3 (Robustness):** The scheduler module shall not cause the SGE master daemon to crash. If the module fails, it shall default to logging an error and ceding control back to the native SGE scheduler.

##### 3.3.3 Design Constraints
*   **REQ-CON-1:** The code shall be written in standard C (C99) without compiler-specific extensions.
*   **REQ-CON-2:** The scheduling algorithm shall be heuristic-based, as specified in the project summary.
*   **REQ-CON-3:** The source code and build system shall be compatible with a standard GNU/Linux toolchain (gcc, make, autotools).

##### 3.3.4 License & Legal
*   **REQ-LIC-1:** The entire codebase shall be licensed under the GNU General Public License version 2 or later.
*   **REQ-LIC-2:** All source files shall contain a GPL copyright header and a copy of the license must be included in the distribution.

---

### 4. Appendices

#### 4.1 Data Structures (Pseudo-Code)
```c
typedef struct {
    sge_job_id_t sge_id;      // Native SGE job identifier
    int user_id;              // Submitting user
    double budget;            // User-submitted budget
    time_t deadline;          // User-submitted deadline (epoch time)
    double runtime_estimate;  // Estimated CPU seconds required
    double tickets;           // Calculated share
    long long stride;         // Calculated stride (integer)
    long long pass;           // Current pass value
    int status;               // PENDING, RUNNING, COMPLETED, REJECTED
} eco_job_t;

typedef struct {
    double total_budget_pool; // Sum of budgets of all active jobs
    time_t furthest_deadline; // Latest deadline among active jobs
    double price_per_cpu_sec; // Global resource price
    priority_queue_t *job_queue; // Min-heap keyed on job->pass
} scheduler_state_t;
```

#### 4.2 Stride Scheduling Algorithm Summary
```
Initialization:
    For each job i: pass_i = stride_i

Scheduling Loop:
    job_to_run = extract_min(pass) from runnable queue
    allocate_time_quantum(job_to_run)
    pass_i = pass_i + stride_i
    re-insert job_to_run into queue with new pass_i
```

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| SGE Admin Representative | | | |