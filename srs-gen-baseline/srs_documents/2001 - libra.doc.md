Here is a comprehensive Software Requirements Specification (SRS) document for the Libra project, following professional standards and markdown formatting.

# Software Requirements Specification for Libra Scheduler

**Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft  
**Project:** Libra - An Economy-Driven Cluster Scheduler

---

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for Libra, an economy-driven cluster scheduler designed to provide Quality of Service (QoS) through a computational economy model. The system prioritizes user utility over raw system performance by allowing users to specify budget and deadline constraints for their computational jobs. This SRS is intended for developers, testers, project managers, and stakeholders involved in the Libra project.

### 1.2 Scope
Libra is an add-on module for the Sun Grid Engine (SGE) cluster management system that introduces an economy-based scheduling paradigm. It will schedule sequential and embarrassingly parallel batch jobs on homogeneous Linux clusters using a bid-based proportional resource-sharing model. The system will operate within the constraints of a limited test environment without requiring modifications to the Linux kernel.

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|------|------------|
| SGE | Sun Grid Engine, a cluster management system |
| QoS | Quality of Service |
| MVP | Minimum Viable Product |
| Batch Job | A computational task submitted for non-interactive execution |
| Embarrassingly Parallel | A parallel computing paradigm where tasks require little to no communication |
| Stride Scheduling | A proportional-share scheduling algorithm |

### 1.4 References
- Sun Grid Engine Documentation
- Stride Scheduling Research Papers
- Linux Standard Base Specification

### 1.5 Overview
This document is organized into sections covering overall description, specific requirements, and constraints. Section 2 provides a high-level overview of the product, while Section 3 details the functional and non-functional requirements.

## 2. Overall Description

### 2.1 Product Perspective
Libra functions as a sub-component integrated with the Sun Grid Engine cluster management system. It extends SGE's capabilities by adding economy-driven scheduling while maintaining compatibility with existing SGE infrastructure.

**Architecture Context Diagram:**
```
+----------------+     +----------------+     +----------------+
|   SGE Queue    | --> |  Libra Module  | --> |  SGE Executor  |
|   Manager      |     |  (Scheduler)   |     |    Daemon      |
+----------------+     +----------------+     +----------------+
         ^                      |                      |
         |                      v                      v
+----------------+     +----------------+     +----------------+
|  User Job      |     |  Economic      |     |  Cluster       |
|  Submission    |     |  Policy Engine |     |  Nodes         |
+----------------+     +----------------+     +----------------+
```

### 2.2 Product Functions
- Economy-driven job scheduling based on user bids and deadlines
- Proportional resource allocation using stride scheduling
- Integration with SGE job management infrastructure
- Support for sequential and embarrassingly parallel job types
- Resource management within constrained hardware environment

### 2.3 User Characteristics
**Primary Users:**
- **Cluster Users:** Submit jobs with budget and deadline constraints
- **Cluster Administrators:** Monitor system performance and economic policies
- **Researchers:** Study economic scheduling models and their effectiveness

### 2.4 Constraints
- Must operate on a test cluster of four Pentium-III workstations with 128MB RAM each
- Implementation must use standard C programming language
- Must function as an SGE sub-component without kernel modifications
- Must maintain compatibility with existing SGE installations

### 2.5 Assumptions and Dependencies
- Sun Grid Engine is properly installed and configured on the cluster
- Cluster nodes are homogeneous in hardware configuration
- Users will provide realistic budget and deadline constraints
- The economic policy framework will be finalized in future versions

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
**Job Submission Interface:**
```c
// Example job submission structure
typedef struct {
    char* job_script;      // Path to executable/script
    double budget;         // User's allocated budget
    time_t deadline;       // Job completion deadline
    int parallelism;       // Degree of parallelism (1=sequential)
    int priority;          // Derived from economic model
} libra_job_t;
```

#### 3.1.2 Hardware Interfaces
- Compatible with Pentium-III architecture
- Supports systems with 128MB RAM minimum
- Standard Ethernet network connectivity

#### 3.1.3 Software Interfaces
**SGE Integration:**
- Interfaces with SGE `qsub` for job submission
- Hooks into SGE scheduling events
- Compatible with SGE 6.0 or later
- Uses SGE's DRMAA (Distributed Resource Management Application API)

#### 3.1.4 Communications Interfaces
- Standard TCP/IP communication between cluster nodes
- SGE inter-daemon communication protocols

### 3.2 Functional Requirements

#### 3.2.1 Job Scheduling Requirements

**FR-1: Sequential Job Scheduling**
- **Description:** The system shall schedule sequential (single-threaded) batch jobs on available cluster nodes.
- **Priority:** High
- **Input:** Job script, budget, deadline constraints
- **Processing:** Determine optimal node placement based on economic model
- **Output:** Job execution on selected node

**FR-2: Embarrassingly Parallel Job Scheduling**
- **Description:** The system shall schedule embarrassingly parallel jobs that can run independently across multiple nodes.
- **Priority:** High
- **Input:** Parallel job specification, budget, deadline
- **Processing:** Distribute independent tasks across available nodes
- **Output:** Coordinated execution of parallel tasks

**FR-3: Budget-Based Allocation**
- **Description:** The system shall allocate CPU time based on user-submitted budget constraints.
- **Priority:** High
- **Input:** User budget allocation
- **Processing:** Convert budget to resource shares using economic model
- **Output:** Proportional resource allocation

**FR-4: Deadline-Constrained Scheduling**
- **Description:** The system shall consider user-submitted deadlines when making scheduling decisions.
- **Priority:** High
- **Input:** Job deadline specification
- **Processing:** Calculate scheduling priority incorporating time constraints
- **Output:** Deadline-aware job ordering

#### 3.2.2 Economic Model Requirements

**FR-5: Bid-Based Resource Sharing**
- **Description:** The system shall implement a bid-based proportional resource-sharing model.
- **Priority:** High
- **Input:** User bids (budget allocations)
- **Processing:** Calculate resource shares proportional to bids
- **Output:** Fair resource distribution based on economic contributions

**FR-6: Stride Scheduling Implementation**
- **Description:** The system shall use stride scheduling for proportional resource allocation.
- **Priority:** High
- **Input:** Calculated resource shares
- **Processing:** Implement stride scheduling algorithm
- **Output:** Time-sliced CPU allocation proportional to shares

#### 3.2.3 Integration Requirements

**FR-7: SGE Module Integration**
- **Description:** The system shall integrate as an add-on module to Sun Grid Engine.
- **Priority:** High
- **Input:** SGE scheduling events and job queues
- **Processing:** Intercept and modify SGE scheduling decisions
- **Output:** Economy-driven scheduling within SGE framework

### 3.3 Performance Requirements

**PR-1: Resource Efficiency**
- The system shall utilize at least 85% of available cluster CPU capacity during peak loads
- Memory overhead shall not exceed 16MB per scheduler instance

**PR-2: Scheduling Latency**
- Job scheduling decisions shall be made within 100ms for clusters of up to 4 nodes
- Economic calculations shall add no more than 10% overhead to base SGE scheduling

**PR-3: Scalability**
- The scheduling algorithm shall efficiently handle up to 100 concurrent jobs
- Economic model calculations shall scale linearly with the number of active jobs

### 3.4 Design Constraints

**DC-1: Implementation Language**
```c
// All core scheduling logic must be implemented in standard C
// Example constraint-compliant function signature
int libra_schedule_job(libra_job_t *job, node_info_t *nodes, int node_count);
```

**DC-2: Hardware Limitations**
- Maximum memory usage: 128MB RAM per node
- Processor compatibility: Pentium-III instruction set
- Network: Standard 100Mbps Ethernet

**DC-3: Integration Constraints**
- No modifications to Linux kernel source code
- Must use SGE's published APIs and extension points
- Must not break existing SGE functionality

### 3.5 Software System Attributes

**Reliability:**
- The scheduler shall maintain 99% uptime during testing periods
- Economic model calculations shall be numerically stable and free from race conditions

**Maintainability:**
- Code shall follow standard C conventions with comprehensive documentation
- Modular design shall allow for replacement of economic policies

**Portability:**
- Source code shall compile with gcc and standard C libraries
- Shall be portable across Linux distributions supporting SGE

### 3.6 Undecided Issues and Risks

**UR-1: Economic Policy Specification**
- The exact pricing and costing policy for charging users will be specified in a later version
- Current implementation will use a placeholder economic model

**UR-2: Advanced QoS Metrics**
- Additional quality of service metrics beyond budget and deadline are not yet defined
- Future versions may include reliability, availability, or performance guarantees

## 4. Appendices

### 4.1 Stride Scheduling Algorithm Outline
```c
// Pseudo-code for stride scheduling implementation
typedef struct {
    int tickets;        // Proportional to user's bid
    int stride;         // Inverse of tickets
    int pass;           // Current pass value
} scheduler_entity_t;

void schedule_next_job() {
    // Select entity with minimum pass value
    scheduler_entity_t *next = find_min_pass_entity();
    
    // Execute job for quantum time
    execute_job(next->assigned_job);
    
    // Update pass value
    next->pass += next->stride;
}
```

### 4.2 SGE Integration Points
- **Event Client:** Responds to SGE scheduling events
- **Job Verifier:** Validates economic constraints during job submission
- **Scheduler Hook:** Modifies SGE's default scheduling decisions
- **Policy Module:** Implements economic allocation policies

---

**Document Approval**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | | | |
| Lead Developer | | | |
| Quality Assurance | | | |