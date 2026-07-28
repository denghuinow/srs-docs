# Detailed Summary: Libra Economy-Driven Cluster Scheduler

## Background and Scope
Libra is an economy-driven cluster scheduler designed as an add-on to the Sun Grid Engine (SGE) cluster management system. Its primary objective is to provide Quality of Service (QoS) through a computational economy model, scheduling CPU time based on user utility (budget and deadline) rather than system-centric performance metrics. The scope includes managing sequential and embarrassingly parallel batch jobs on a homogeneous Linux cluster, with the scheduler enforcing proportional resource sharing via a bid-based economic model and stride scheduling algorithm. Non-goals include supporting real parallel jobs with inter-thread dependencies, implementing job migration for resource defragmentation, and providing a full-fledged GUI in the initial version.

## Stakeholders Matrix and Use Cases
*   **Cluster User**: Submits jobs with budget and deadline constraints, monitors job status, and manages their own submissions.
*   **Cluster Administrator**: Oversees cluster operations, monitors node status and system load, manages scheduling policies and cost structures, and can control any job.
*   **Sun Grid Engine (SGE) System**: The underlying cluster management platform that handles job queuing, resource management, and job dispatch based on Libra's scheduling decisions.
*   **Project Development Team**: Responsible for implementing, testing, and maintaining the Libra scheduler software.

**Main Scenarios:**
1.  User submits a job with budget, deadline, and execution time.
2.  Scheduler accepts/rejects job based on feasibility of meeting constraints.
3.  Scheduler calculates job priority (tickets, stride) for proportional CPU allocation.
4.  Scheduler selects least-loaded execution host and appropriate queue.
5.  Dispatcher places job into the selected queue for execution.
6.  Stride scheduling algorithm time-slices CPU among jobs in a queue.
7.  User views the status of their submitted jobs.
8.  Administrator alters the cluster's scheduling policy or cost structure.

**Exception Scenarios:**
1.  Job submission is rejected due to insufficient budget or an infeasible deadline.
2.  A user or administrator cancels a pending or running job.

## Business Process
**Main Process: Job Submission & Scheduling**
1.  **Trigger**: User submits a job via SGE interface with parameters (executable, budget, deadline, estimated runtime).
2.  SGE forwards job details to Libra for initialization.
3.  Libra evaluates job feasibility (Accept/Reject Job) based on cluster load and job constraints.
4.  If accepted, Libra calculates the job's scheduling information (tickets, stride) using the economic model.
5.  Libra determines the optimal execution host (least-loaded node) and queue.
6.  Libra dispatches the job to the selected host/queue.
7.  Libra updates the central cluster status with the new job allocation.
8.  The stride scheduler on each host executes jobs by allocating CPU quanta based on calculated passes.

**Key Branch A: Job Rejection**
1.  **Trigger**: Job constraints cannot be met.
2.  Libra rejects the job.
3.  Libra may suggest an alternative deadline or budget to the user.
4.  Job is not entered into the scheduling system.

**Key Branch B: Job Cancellation**
1.  **Trigger**: User or administrator requests job deletion.
2.  Job is removed from its queue.
3.  Libra updates the cluster status, freeing reserved resources.
4.  Scheduling decisions for remaining jobs are revised.

## Domain Model
*   **User** (required: id, name, authentication; unique: id)
*   **Job** (required: id, type, estimatedRuntime, budget, deadline, status; unique: id; reference: user)
*   **Cluster** (required: masterHost)
*   **ExecutionHost (Node)** (required: hostId, cpuLoad, availableMemory, status; reference: cluster)
*   **Queue** (required: queueId, hostId, jobTypePolicy; reference: executionHost)
*   **SchedulingInfo** (required: jobId, tickets, stride, pass; reference: job)
*   **ResourceAllocation** (required: jobId, hostId, queueId, startTime, quantum; reference: job, executionHost, queue)

## Interfaces and Integrations
*   **System**: Sun Grid Engine (SGE); **Direction**: Libra ← SGE; **Interaction**: Job submission & status relay; **Input**: User-submitted job parameters; **Output**: Job acceptance/rejection, scheduling decisions; **SLA**: Job submission response time <1 min.
*   **System**: Linux Operating System; **Direction**: Libra → OS; **Interaction**: Resource enforcement & job execution; **Input**: Scheduling decisions (quantum, job); **Output**: Process execution, resource usage data; **SLA**: Leverages OS process control.
*   **System**: PVM/MPI Libraries; **Direction**: Libra → Libraries; **Interaction**: Parallel job execution; **Input**: Embarrassingly parallel job splits; **Output**: Coordinated parallel process execution; **SLA**: Dependent on library performance.
*   **Interface**: Cluster User CLI/GUI; **Direction**: User ↔ System; **Interaction**: Job submission, status query, cancellation; **Input**: Commands and job parameters; **Output**: Job status, cost queries, history.
*   **Interface**: Administrator CLI/GUI; **Direction**: Admin ↔ System; **Interaction**: Cluster monitoring & policy control; **Input**: Admin commands; **Output**: Node status, load, job logs, policy confirmations.

## Acceptance Criteria
*   **Capability: QoS-driven Job Acceptance**
    *   Given a user submits a job with a budget and deadline, When the cluster load is high but the job offers a high budget, Then the job is accepted and scheduled with high priority.
    *   Given a user submits a job with an impossible deadline given current load, When the scheduler evaluates it, Then the job is rejected with a suggested feasible deadline.
*   **Capability: Proportional Resource Sharing**
    *   Given multiple jobs are running on a host with different calculated ticket allocations, When CPU time is sliced by the stride scheduler, Then each job receives CPU quanta proportional to its ticket share.
*   **Capability: Load Balancing**
    *   Given a new job is accepted for scheduling, When determining its execution host, Then the least-loaded node in the cluster is selected.

## Non-functional Metrics
*   **Performance**: Job submission response time < 1 minute; Deadline adherence within 10% error margin (assuming accurate job stats).
*   **Reliability**: Maximum bug rate of 1 bug/KLOC; System reboot/recovery time <5 minutes.
*   **Security**: User job privacy and status confidentiality; Prevention of unauthorized alteration of scheduling criteria.
*   **Compliance**: Code released under GNU GPL open-source license.
*   **Observability**: Administrator ability to monitor node status, cluster load, and all job statuses.

## Milestones and Release Strategy
1.  Finalize economic model and stride scheduling integration design.
2.  Develop core scheduler module (job acceptance, priority calculation).
3.  Implement host selection, dispatching, and cluster status update features.
4.  Integrate Libra module with Sun Grid Engine 5.3.
5.  Testing and validation on the 4-node Pentium-III test cluster.
6.  Initial open-source release under GPL with command-line interfaces.

## Risk List and Mitigation Strategies
1.  **Risk**: SGE integration complexity or incompatibility with Libra's scheduling decisions.
    *   **Mitigation**: Early prototyping of the interface; close adherence to SGE 5.3 APIs.
2.  **Risk**: Economic model fails to balance user utility and system utilization effectively.
    *   **Mitigation**: Develop a simulation tool to model and tune the bid-based algorithm before full implementation.
3.  **Risk**: Inaccurate user estimates of job execution time leading to missed deadlines.
    *   **Mitigation**: Implement basic job accounting to refine runtime predictions over time; include 10% error allowance in scheduling.
4.  **Risk**: Limited test cluster size (4 nodes) hinders scalability validation.
    *   **Mitigation**: Use software simulation to test scheduler behavior with a larger number of nodes and jobs.
5.  **Risk**: Performance overhead of dynamic, economy-driven scheduling degrades response time.
    *   **Mitigation**: Employ heuristics for scheduling decisions to avoid exhaustive searches; profile and optimize critical paths.

## Undecided Issues and Responsible Parties
1.  **Detailed pricing and cost accounting mechanism** (Economic Model Lead).
2.  **Development vs. acquisition of a simulation/testing tool** (Project Lead).
3.  **Specification of heuristics for the NP-hard scheduling problem** (Scheduling Algorithm Lead).
4.  **Full design of a GUI for users and administrators** (UI/UX Lead - post-MVP).
5.  **Adaptation strategy for heterogeneous clusters or resources beyond CPU** (Future Scope Lead).