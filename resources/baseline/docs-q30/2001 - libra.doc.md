```markdown
# Software Requirements Specification (SRS)
## Libra: Economy-Driven Cluster Scheduler

**Version:** 1.0  
**Date:** 2024-01-15  
**Status:** Draft

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [System Features](#3-system-features)
4. [External Interface Requirements](#4-external-interface-requirements)
5. [Non-Functional Requirements](#5-non-functional-requirements)
6. [Constraints, Assumptions & Dependencies](#6-constraints-assumptions--dependencies)

---

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for Libra, an economy-driven scheduler for high-performance Linux clusters. The system prioritizes user-defined budget and deadline constraints over traditional system performance metrics, providing Quality of Service (QoS) guarantees through market-based resource allocation.

### 1.2 Scope
Libra operates as an add-on scheduling module for Sun Grid Engine (SGE) 5.3, designed exclusively for homogeneous Linux clusters. The system manages sequential and embarrassingly parallel batch jobs while enforcing economic constraints.

**In-Scope:**
- QoS-driven scheduling based on budget and deadline constraints
- Dynamic resource reallocation for deadline compliance
- Bid-based CPU time allocation
- Integration with SGE's existing job management infrastructure

**Out-of-Scope:**
- Grid-level bargaining or user-to-user negotiation
- Heterogeneous cluster support
- Linux kernel modifications
- Non-batch job types (interactive, real-time)

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|------|------------|
| SGE | Sun Grid Engine - Cluster management system |
| QoS | Quality of Service - Service level guarantees |
| PVM | Parallel Virtual Machine - Message passing interface |
| MPI | Message Passing Interface - Parallel computing standard |
| KLOC | Thousand Lines of Code - Software quality metric |

### 1.4 References
- Sun Grid Engine 5.3 Administration Guide
- PVM/MPI Programming Specifications
- Linux Cluster Architecture Standards

## 2. Overall Description

### 2.1 Product Perspective
Libra integrates as a component within the SGE cluster management ecosystem, replacing SGE's default scheduling policies while leveraging existing infrastructure:

```
SGE Infrastructure → Libra Scheduler → Resource Allocation
    ↑                    ↑                    ↓
Job Accounting    Economic Policies    Process Migration
```

### 2.2 Product Functions
- **Economic Scheduling**: Enforce budget and deadline constraints
- **Dynamic Reallocation**: Adjust resource allocation based on urgency
- **Proportional Allocation**: Distribute CPU time using bid-based sharing
- **Priority Calculation**: Compute job priorities using economic parameters
- **Lifecycle Management**: Handle job submission, monitoring, and termination

### 2.3 User Characteristics

#### 2.3.1 Cluster Users
- Technical professionals submitting computational jobs
- Familiar with SGE command-line interface
- Provide budget and deadline constraints for jobs
- Cannot modify scheduling policies

#### 2.3.2 Administrators
- System administrators managing cluster resources
- Configure economic policies and cost structures
- Monitor system status and performance
- Exclusive control over scheduling criteria

### 2.4 Operating Environment
- **Platform**: Homogeneous Linux clusters
- **Cluster Manager**: Sun Grid Engine 5.3
- **Parallel Processing**: PVM/MPI support
- **Kernel**: Standard Linux kernel (no modifications required)

### 2.5 Design and Implementation Constraints
- Must operate within SGE 5.3 architecture
- No kernel-level modifications permitted
- Limited to homogeneous cluster configurations
- Dependent on SGE's job accounting accuracy

## 3. System Features

### 3.1 QoS-Driven Scheduling

#### 3.1.1 Description
Enforce scheduling decisions based on user-provided budget and deadline constraints rather than system performance metrics.

#### 3.1.2 Requirements
- **QoS-001**: The system shall accept job submissions with budget constraints
- **QoS-002**: The system shall accept job submissions with deadline constraints
- **QoS-003**: The system shall prioritize jobs based on economic parameters
- **QoS-004**: The system shall guarantee deadline compliance within ±10% error margin

### 3.2 Dynamic Resource Reallocation

#### 3.2.1 Description
Dynamically adjust resource allocation to meet urgent job deadlines and optimize economic efficiency.

#### 3.2.2 Requirements
- **DRR-001**: The system shall monitor job progress against deadlines
- **DRR-002**: The system shall reallocate resources for jobs approaching deadlines
- **DRR-003**: The system shall maintain economic efficiency during reallocation

### 3.3 Bid-Based Resource Sharing

#### 3.3.1 Description
Allocate CPU time proportionally using a bid-based resource-sharing mechanism with ticket/stride scheduling.

#### 3.3.2 Requirements
- **BRS-001**: The system shall implement bid-based CPU time allocation
- **BRS-002**: The system shall calculate job priority using economic bids
- **BRS-003**: The system shall implement stride scheduling based on bids
- **BRS-004**: The system shall allocate resources proportionally to bid values

### 3.4 Job Lifecycle Management

#### 3.4.1 Description
Manage the complete job lifecycle from submission through completion or cancellation.

#### 3.4.2 Requirements
- **JLM-001**: The system shall accept job submissions via SGE interface
- **JLM-002**: The system shall provide job status monitoring capabilities
- **JLM-003**: The system shall support job cancellation requests
- **JLM-004**: The system shall maintain job accounting records

## 4. External Interface Requirements

### 4.1 User Interfaces

#### 4.1.1 Command-Line Interface (Users)
```bash
# Job submission with economic constraints
qsub -l budget=100 -l deadline="2024-01-20 18:00" job_script.sh

# Job status monitoring
qstat -u $USER

# Job cancellation
qdel <job_id>
```

#### 4.1.2 Administrative Interface
```bash
# Policy configuration
libra_policy --set-cost-cpu 10 --set-cost-memory 5

# Cluster status monitoring
libra_status --economic-metrics

# Node management
libra_nodes --add node01 --remove node02
```

### 4.2 Hardware Interfaces
- **CPU**: Utilization monitoring via SGE infrastructure
- **Memory**: Allocation and usage tracking
- **Swap**: Usage monitoring for resource planning
- **Network**: Inter-node communication protocols

### 4.3 Software Interfaces

#### 4.3.1 SGE 5.3 Integration
- **Interface Type**: Direct module integration
- **Protocol**: SGE scheduler API
- **Data Exchange**: Job accounting and resource allocation

#### 4.3.2 Parallel Processing Support
- **PVM**: Parallel Virtual Machine integration
- **MPI**: Message Passing Interface support
- **Compatibility**: Standard SGE parallel environment configurations

## 5. Non-Functional Requirements

### 5.1 Performance Requirements

| Requirement | Metric | Target |
|-------------|--------|---------|
| Job Submission Response | Time from submission to scheduling decision | ≤ 1 minute |
| Deadline Compliance | Actual vs. scheduled completion time | ±10% error margin |
| System Recovery | Time from outage to full operation | ≤ 5 minutes |
| Resource Allocation | CPU time distribution accuracy | Proportional to bids ±5% |

### 5.2 Reliability Requirements
- **AVAIL-001**: System availability of 99.5% during operational hours
- **REL-001**: Maximum bug density of 1 bug per KLOC
- **REL-002**: Graceful degradation under high load conditions

### 5.3 Security Requirements
- **SEC-001**: User authentication via SGE security infrastructure
- **SEC-002**: Policy modification restricted to administrators
- **SEC-003**: Job isolation between users

### 5.4 Maintainability Requirements
- **MAINT-001**: Modular design for scheduler policy updates
- **MAINT-002**: Comprehensive logging for debugging
- **MAINT-003**: Configuration management for economic parameters

## 6. Constraints, Assumptions & Dependencies

### 6.1 Technical Constraints
- **CON-001**: Limited to homogeneous Linux clusters
- **CON-002**: No kernel modifications permitted
- **CON-003**: SGE 5.3 as mandatory foundation
- **CON-004**: Sequential and embarrassingly parallel jobs only

### 6.2 Assumptions
- **ASM-001**: Users provide accurate job execution time estimates
- **ASM-002**: SGE job accounting module provides reliable data
- **ASM-003**: Cluster resources remain stable during job execution
- **ASM-004**: Economic parameters reflect user priorities accurately

### 6.3 Dependencies
- **DEP-001**: Sun Grid Engine 5.3 cluster management system
- **DEP-002**: SGE job accounting module accuracy
- **DEP-003**: Linux operating system compatibility
- **DEP-004**: PVM/MPI libraries for parallel job support

### 6.4 Acceptance Criteria

#### 6.4.1 Mandatory Acceptance Tests
1. **Deadline Compliance**: 95% of jobs complete within ±10% of specified deadlines
2. **Response Time**: Job submission response time ≤ 1 minute for 99% of submissions
3. **Economic Enforcement**: No user-bargaining functionality present
4. **QoS Guarantees**: All accepted jobs receive specified budget/deadline enforcement

#### 6.4.2 Priority Implementation
1. **High Priority**: QoS enforcement (budget/deadline) for all accepted jobs
2. **Medium Priority**: Dynamic resource reallocation and bid-based allocation
3. **Low Priority**: Administrative interface enhancements and extended monitoring

---

## Appendix A: Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | SRS Author | Initial draft creation |
```