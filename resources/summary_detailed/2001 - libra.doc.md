# Detailed Summary

## Background and Scope
Libra is an economy-driven cluster scheduler designed as an add-on to the Sun Grid Engine (SGE) cluster management system. Its primary purpose is to provide Quality of Service (QoS) computational economy by scheduling CPU time based on user utility rather than system performance. The scheduler manages sequential and embarrassingly parallel batch jobs on a homogeneous Linux cluster using a bid-based proportional resource-sharing model with stride scheduling. Non-goals include handling real parallel jobs with inter-job dependencies, implementing job migration for resource defragmentation, and providing a full pricing mechanism in the initial version.

## Role Matrix and Use Cases
- **Cluster User**: Submits jobs, monitors status, cancels own jobs, checks credit balance and usage history.
- **Cluster Administrator**: Manages cluster nodes, alters cost structures and scheduling policies, monitors all jobs and system load.
- Main scenarios: Job submission with budget/deadline, job status viewing, job cancellation, administrative cluster monitoring.
- Exception scenarios: Job rejection due to insufficient budget/deadline constraints, dynamic resource reallocation for urgent jobs.

## Business Process
**Main Process (Job Submission & Execution)**
1. User submits job with parameters (budget, deadline, execution time)
2. System verifies user and cluster acceptance status
3. Initialize job details and parse parameters
4. Accept/Reject decision based on budget/deadline feasibility
5. Calculate scheduling information (tickets, stride, pass)
6. Determine execution host based on load balancing
7. Dispatch job to appropriate queue
8. Execute job using stride scheduling algorithm

**Key Branch (Job Rejection)**
- Trigger: Job cannot meet deadline within budget
- Steps: Suggest alternative deadline/cost, return rejection to user, update cluster status

**Key Branch (Job Cancellation)**
- Trigger: User or administrator cancels job
- Steps: Remove job from queue, update cluster resources, revise scheduling decisions

## Domain Model
- **Job**: JobID (unique), UserID (required), JobType (sequential/parallel), ExecutionTime (required), Budget (required), Deadline (required), Status
- **User**: UserID (unique), Name (required), AuthenticationID (required)
- **Cluster**: ClusterID (unique), NodeCount, CurrentLoad
- **Node**: NodeID (unique), CPUCount, MemorySize, Status, CurrentLoad
- **Queue**: QueueID (unique), NodeID (reference), JobCount, MaxCapacity
- **SchedulingInfo**: JobID (reference), Tickets (required), Stride (required), Pass (required)
- **ResourceAllocation**: AllocationID (unique), JobID (reference), NodeID (reference), StartTime, EndTime

## Interfaces and Integrations
- **Sun Grid Engine**: Direction: Bidirectional, Theme: Job management and resource allocation, Input: Job parameters, Output: Scheduling decisions, SLA: <1 minute response time
- **Linux Operating System**: Direction: Libra→OS, Theme: System resource access, Input: Resource requests, Output: Execution control, SLA: Standard OS performance
- **PVM/MPI Libraries**: Direction: Libra→Libraries, Theme: Parallel job execution, Input: Job splitting requests, Output: Parallel execution management, SLA: Library-dependent performance

## Acceptance Criteria
- **Job Submission**: Given valid user credentials and job parameters, when user submits job, then system should accept job and provide scheduling estimate
- **QoS Enforcement**: Given multiple jobs with varying budgets/deadlines, when system schedules execution, then higher priority jobs should receive proportional resource allocation
- **Load Balancing**: Given heterogeneous cluster load, when scheduling decisions are made, then jobs should be distributed to least-loaded nodes

## Non-functional Metrics
- **Performance**: Maximum 1 minute response time for job submission; 10% deadline sensitivity allowance
- **Reliability**: Maximum 1 bug/KLOC; <5 minute system recovery time
- **Security**: User job privacy enforcement; administrative control over scheduling alterations
- **Compliance**: GNU GPL licensing; open-source distribution

## Milestones and Release Strategy
1. Core scheduling algorithm implementation
2. SGE integration testing
3. Economic model validation
4. Basic command-line interface completion
5. Performance benchmarking
6. Initial open-source release

## Risk List and Mitigation Strategies
- **Hardware Limitations**: Mitigation: Use simulation tools for larger-scale testing
- **SGE Integration Complexity**: Mitigation: Close coordination with SGE documentation and community
- **User Execution Time Estimation**: Mitigation: Implement job profiling and historical data analysis
- **Economic Model Validation**: Mitigation: Extensive simulation testing before deployment

## Undecided Issues and Responsible Parties
- Detailed pricing mechanism implementation (Project Team)
- GUI development timeline (Project Team)
- Simulation tool selection (design vs generic) (Project Team)
- Extended job accounting features (Project Team)
- Heterogeneous cluster adaptation (Not mentioned)
- Real-time job monitoring interface (Not mentioned)
- Advanced job migration capabilities (Not mentioned)
- Multi-cluster scheduling support (Not mentioned)