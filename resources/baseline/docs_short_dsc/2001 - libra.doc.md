# Software Requirements Specification (SRS)
## For
**Libra – An Economy-Driven Cluster Scheduler**

**Version:** 1.0  
**Date:** [Current Date]  
**Authors:** Jahanzeb Sherwani, Nosheen Ali, Nausheen Lotia, Zahra Hayat  
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for Libra, an economy-driven cluster scheduler add-on for the Sun Grid Engine (SGE). It is intended for use by the project stakeholders, developers, testers, and project management to guide the design, implementation, and verification of the system.

### 1.2 Scope
Libra is a software component that integrates with SGE version 5.3 to introduce a computational economy model for scheduling batch jobs on a homogeneous Linux cluster. It schedules CPU time based on user-defined Quality of Service (QoS) parameters—budget and deadline—using a bid-based proportional resource-sharing model and the stride scheduling algorithm. The system will provide command-line interfaces for job management and administrative control, ensuring dynamic, scalable, and secure operation.

**In-Scope Items:**
*   Management of sequential and embarrassingly parallel (independent, non-communicating) batch jobs.
*   Implementation of an economic model for proportional resource allocation.
*   Integration with existing SGE interfaces for job submission, status inquiry, and management.
*   Administrative tools for policy configuration and cluster monitoring.
*   A scalable and configurable scheduler core.

**Out-of-Scope Items:**
*   Management of tightly-coupled parallel jobs requiring inter-process communication (MPI, PVM).
*   Job migration capabilities.
*   Peer-to-peer user bargaining mechanisms.
*   A dedicated Graphical User Interface (GUI) in the initial release.
*   Exhaustive (optimal) scheduling algorithms; heuristic-based approaches will be used.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SGE** | Sun Grid Engine, a distributed resource management (DRM) system. |
| **QoS** | Quality of Service, guarantees related to job completion time and cost. |
| **Economy Model** | A system where resources are allocated based on economic principles like bidding and pricing. |
| **Stride Scheduling** | A deterministic fair-share scheduling algorithm that allocates resources in proportion to tickets or bids. |
| **Embarrassingly Parallel** | A parallel computing problem where little to no effort is required to separate it into independent parallel tasks. |
| **GPL** | GNU General Public License, a free software license. |
| **CLI** | Command-Line Interface. |

### 1.4 References
1.  Sun Grid Engine 5.3 Administration and User Documentation.
2.  GNU General Public License, Version 2 or later.
3.  Waldspurger, C. A., & Weihl, W. E. (1995). *Stride scheduling: deterministic proportional-share resource management*.

### 1.5 Overview
The remainder of this SRS is organized as follows: Section 2 provides a general description of the product, its perspective, functions, and constraints. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements including performance, security, and design constraints.

## 2. Overall Description

### 2.1 Product Perspective
Libra is an add-on module to the existing SGE cluster management system. It interfaces with SGE's scheduling and execution components to override or augment its default (typically FIFO or priority-based) scheduling policy with an economy-driven model. The relationship is depicted below:

```
[User] --(qsub with budget/deadline)--> [SGE + Libra Scheduler] --(dispatches)--> [Cluster Nodes]
         ^                                   |                                   ^
         |--(qstat, qalter, qdel)------------|                                   |
         |                                    `--(monitoring & policy)--> [Administrator]
```

### 2.2 Product Functions
The core functions of Libra are:
1.  **Economic Job Admission:** Accept jobs with user-specified budget and deadline constraints.
2.  **Bid Processing:** Calculate a job's effective "bid" or priority based on its budget, deadline, and system pricing policy.
3.  **Proportional Scheduling:** Use the stride scheduling algorithm to allocate CPU time slices to jobs in proportion to their bids.
4.  **Job Lifecycle Management:** Provide mechanisms to submit, view, modify, and delete jobs via SGE commands.
5.  **Administrative Control:** Allow administrators to view system load, adjust pricing/cost models, and manage (cancel/suspend/resume) jobs.
6.  **Configuration Management:** Enable dynamic adjustment of scheduling policies and economic parameters without system restart.

### 2.3 User Characteristics
| Stakeholder Category | Characteristics & Skills |
| :--- | :--- |
| **Cluster User** | Scientific researchers or engineers familiar with Linux CLI and SGE commands (`qsub`, `qstat`). Understands basic job parameters (runtime estimate, resources) and the economic concepts of budget and deadline. |
| **Cluster Administrator** | System administrator with in-depth knowledge of SGE configuration, Linux system management, and cluster operations. Responsible for policy setting and resource fairness. |
| **Development Team** | Proficient in C programming, Linux systems programming, and understanding of scheduling algorithms and economic models. |

### 2.4 Constraints
1.  **Hardware:** Initial development and testing will be performed on a cluster of four Pentium-III workstations with 128 MB RAM each.
2.  **Software Integration:** Must function as a sub-component of SGE 5.3. Modifications to the Linux kernel are prohibited.
3.  **Implementation Language:** The core scheduler must be implemented in standard ANSI C.
4.  **Licensing:** All source code must be released under the GNU General Public License (GPL).
5.  **Interface:** The initial release shall only provide a CLI, utilizing and extending existing SGE command-line utilities.

### 2.5 Assumptions and Dependencies
*   **Assumption:** Users can provide reasonably accurate estimates of their job's required CPU time for deadline calculation.
*   **Assumption:** The underlying SGE system is correctly installed and configured on a homogeneous Linux cluster.
*   **Dependency:** The successful integration and operation of Libra is dependent on the stability and APIs of SGE 5.3.
*   **Dependency:** A simulation tool (either custom-developed or existing) is required for comprehensive testing of scheduling policies under load.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 Job Submission (FR1)
*   **Requirement ID:** FR1.1
*   **Description:** The system shall allow users to submit batch jobs via the `qsub` command with extended options for budget and deadline.
*   **Input:** Standard SGE `qsub` parameters, plus `-budget [amount]` and `-deadline [datetime]`.
*   **Process:** Libra shall intercept the submission, validate economic parameters, calculate an initial bid, and place the job in the appropriate economic scheduling queue.
*   **Output:** A standard SGE job ID upon successful acceptance, or an error message if parameters are invalid (e.g., budget <= 0, deadline in the past).

#### 3.1.2 Job Status Inquiry (FR2)
*   **Requirement ID:** FR2.1
*   **Description:** Users shall be able to query the status of their jobs using the `qstat` command, with enhanced output to include economic metrics.
*   **Output:** Standard SGE `qstat` information, augmented with job `budget`, `deadline`, `current cost accrued`, and `estimated completion time`.

#### 3.1.3 Job Modification/Deletion (FR3)
*   **Requirement ID:** FR3.1
*   **Description:** Users shall be able to modify non-critical parameters (e.g., budget increase, deadline extension) or delete their own pending or running jobs using `qalter` and `qdel`.
*   **Constraint:** Critical parameters that fundamentally alter the job's resource footprint (e.g., required memory) may not be alterable after submission, per SGE/Libra policy.

#### 3.1.4 Economic Scheduling Core (FR4)
*   **Requirement ID:** FR4.1
*   **Description:** The scheduler shall implement a **bid-based proportional-sharing model**. A job's bid strength shall be a function of its submitted budget, deadline, and the system's current pricing policy.
*   **Requirement ID:** FR4.2
*   **Description:** The scheduler shall use the **stride scheduling algorithm** to translate bids into deterministic CPU time allocations across all runnable jobs on a node.
*   **Requirement ID:** FR4.3
*   **Description:** The scheduling decisions shall be dynamic, re-calculating allocations when jobs enter, complete, or have their bids modified.

#### 3.1.5 Administrative Monitoring (FR5)
*   **Requirement ID:** FR5.1
*   **Description:** The administrator shall be able to view the real-time load (CPU utilization, memory, queue lengths) and economic status (total revenue, average bid) of each cluster node via a dedicated CLI command (e.g., `libra_monitor`).

#### 3.1.6 Administrative Policy Control (FR6)
*   **Requirement ID:** FR6.1
*   **Description:** The administrator shall be able to modify global economic parameters (e.g., base price per CPU-hour, pricing algorithm coefficients) via a configuration file or runtime command without stopping the scheduler.
*   **Requirement ID:** FR6.2
*   **Description:** The administrator shall have the authority to cancel, suspend, or resume any job in the system, regardless of ownership, via enhanced `qmod` or `qdel` commands with administrative privileges.

### 3.2 Non-Functional Requirements

#### 3.2.1 Performance Requirements
*   **Requirement ID:** NFR1
*   **Description:** **Deadline Adherence:** Given accurate user-provided job runtime estimates, at least 90% of jobs shall complete within 110% of their submitted deadline (i.e., a 10% error margin).
*   **Requirement ID:** NFR2
*   **Description:** **Budget Guarantee:** Under no circumstance shall the final cost charged to a user exceed the maximum budget specified at job submission.
*   **Requirement ID:** NFR3
*   **Description:** **Scalability:** The scheduler's decision-making overhead shall not cause significant performance degradation (defined as >5% increase in average job wait time) as the cluster scales from 4 to 32 nodes, or as the number of concurrent jobs increases from 50 to 500.

#### 3.2.2 Security Requirements
*   **Requirement ID:** NFR4
*   **Description:** User authentication and authorization shall be delegated to the underlying SGE system. Libra shall inherit and respect SGE's user and access control lists (ACLs).
*   **Requirement ID:** NFR5
*   **Description:** Administrative functions (policy change, job management on behalf of others) shall require SGE administrator privileges.

#### 3.2.3 Design Constraints
*   **Requirement ID:** NFR6
*   **Description:** The system shall be developed in standard C (C99 standard).
*   **Requirement ID:** NFR7
*   **Description:** The codebase shall be modular, separating the economic model, scheduling algorithm, and SGE integration layers to facilitate maintenance and testing.

#### 3.2.4 Quality Attributes
*   **Reliability:** The scheduler shall maintain a mean time between failures (MTBF) greater than the underlying SGE master daemon.
*   **Configurability:** All economic and scheduling policies shall be controlled via well-documented configuration files.
*   **Testability:** The system shall provide logging mechanisms to record scheduling decisions, bid calculations, and job state transitions for validation and debugging.

## 4. Appendices

### 4.1 Undecided Issues (TBD)
1.  The precise mathematical formula for calculating a job's bid from its budget, deadline, and system price.
2.  The choice between developing a custom discrete-event simulation tool for Libra or adapting an existing generic cluster simulator.
3.  The specification for a potential Phase 2 GUI for user and administrator interfaces.

### 4.2 Success Metrics Validation Plan
*   **Deadline Adherence:** Will be validated by submitting a suite of benchmark jobs with known runtimes and deadlines to the test cluster and measuring actual completion times.
*   **Budget Guarantee:** Will be verified by instrumenting the billing module and ensuring the final cost calculation logic never references a value greater than the job's initial budget.
*   **Scalability:** Will be assessed using the simulation tool (see TBD #2) to model increasing loads and node counts, measuring scheduling overhead and job wait times.

---
*This document is considered the authoritative source of requirements for the Libra v1.0 project.*