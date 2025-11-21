**Purpose & Scope**  
Libra provides an economy-driven scheduler for high-performance Linux clusters, prioritizing user-defined budget and deadline constraints over system performance. It exclusively manages sequential and embarrassingly parallel batch jobs on homogenous clusters, integrating as an add-on to Sun Grid Engine (SGE). It excludes grid-level bargaining (e.g., user-to-user negotiation) and heterogeneous cluster support.  

**Product Background / Positioning**  
Libra operates as a component within the SGE cluster management system, enhancing its scheduling module with market-based resource allocation. It replaces SGE’s default scheduling policies without modifying the Linux kernel, leveraging SGE’s existing job accounting and process migration capabilities.  

**Core Functional Overview**  
- Enforce QoS-driven scheduling based on user budget and deadline.  
- Dynamically reallocate resources to meet urgent job deadlines.  
- Allocate CPU time proportionally using bid-based resource-sharing.  
- Calculate job priority and scheduling parameters (tickets/stride).  
- Manage job lifecycle: submission, status monitoring, and cancellation.  

**Key Users & Usage Scenarios**  
Cluster users submit jobs with budget/deadline constraints via SGE command-line interface. Administrators configure scheduling policies, monitor cluster status, and adjust cost structures. Users cannot alter scheduling criteria; admins alone control policy changes.  

**Major External Interfaces**  
- **User interfaces**: Command-line for users (submit/view/delete jobs) and admins (policy/node management).  
- **Hardware interfaces**: SGE’s CPU/memory/swap usage and network protocols.  
- **Software interfaces**: Direct integration with SGE 5.3, using PVM/MPI for parallel jobs.  

**Key Non-functional Requirements**  
- Job submission response time ≤1 minute.  
- Deadline compliance within ±10% error margin.  
- Maximum bug rate: 1 bug per KLOC.  
- System recovery from outage ≤5 minutes.  

**Constraints, Assumptions & Dependencies**  
- Only supports homogenous Linux clusters; no kernel modifications.  
- Depends on SGE’s job accounting module and accurate user-provided job execution times.  
- Requires SGE 5.3 as the foundational cluster management system.  

**Priorities & Acceptance Approach**  
Core priority: QoS enforcement (budget/deadline) must be met for all accepted jobs. Acceptance requires: (1) deadline error ≤10%, (2) submission response time ≤1 minute, (3) no user-bargaining functionality.