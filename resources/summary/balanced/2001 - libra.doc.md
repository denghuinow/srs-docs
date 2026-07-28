# Balanced Summary: Libra Economy-Driven Cluster Scheduler

## Goals and Scope
Libra is an economy-driven cluster scheduler designed as an add-on to the Sun Grid Engine (SGE) cluster management system. Its primary goal is to provide Quality of Service (QoS) by scheduling CPU time based on user utility—specifically budget and deadline constraints—rather than traditional system-centric performance metrics. The initial scope is limited to managing sequential and embarrassingly parallel batch jobs on a homogeneous Linux cluster.

## Stakeholders and User Stories
*   **Cluster User:** Submits jobs with budget and deadline constraints for execution on the cluster.
*   **Cluster Administrator:** Oversees cluster operations, manages scheduling policies, and monitors system status.
*   **Project Owner/Client (Rajkumar Buyya):** Defines the project vision and requirements for an economy-driven scheduler.
*   **Faculty Advisor (Dr. Arif Zaman):** Provides academic guidance and oversight for the project.
*   **Project Group (Jahanzeb Sherwani, Nosheen Ali, Nausheen Lotia, Zahra Hayat):** Develops and implements the Libra scheduler software.

**User Stories:**
1.  As a **Cluster User**, I want to submit a job with a budget and deadline so that my job is scheduled according to my quality-of-service needs.
2.  As a **Cluster User**, I want to monitor the status of my submitted jobs so that I can track their progress.
3.  As a **Cluster User**, I want to cancel a submitted job so that I can stop unnecessary execution and cost.
4.  As a **Cluster Administrator**, I want to check the load and status of each cluster node so that I can manage overall system health.
5.  As a **Cluster Administrator**, I want to alter the cluster's scheduling policy and cost structure so that I can optimize resource allocation.
6.  As a **Cluster Administrator**, I want to cancel, suspend, or resume any job so that I can maintain control over cluster operations.

## Key Processes
1.  **Submit Job:** A user submits a job with parameters (budget, deadline, etc.) via the SGE interface (triggered by user command).
2.  **Initialize Job:** The scheduler parses and stores the submitted job details after SGE acceptance (triggered by job acceptance from SGE).
3.  **Accept/Reject Job:** The scheduler evaluates if the job's deadline and budget can be satisfied given current cluster load (triggered by job initialization).
4.  **Calculate Scheduling Information:** For accepted jobs, the scheduler allocates "tickets" based on budget/deadline and calculates a "stride" for proportional CPU time sharing (triggered by job acceptance).
5.  **Determine Execution Host:** The scheduler selects the least-loaded node and appropriate queue for the job (triggered by scheduling calculation).
6.  **Dispatch Job:** The job is placed into the selected queue on the execution host to await CPU time (triggered by host determination).
7.  **Execute Job:** The stride-scheduling algorithm selects the job with the minimum "pass" value for a CPU time quantum, advancing its pass by its stride (continuously triggered while jobs are in queues).

## Domain Data Elements
*   **Job:** (Primary Key: Job ID) Fields: Job Type, Standalone Execution Time, Budget, Deadline, Location of Executable/Data.
*   **User:** (Primary Key: User ID) Fields: Name, Authentication ID, Credit Balance.
*   **Execution Host/Node:** (Primary Key: Node ID) Fields: CPU Load, Available Memory, Status (e.g., active, down), Queue List.
*   **Queue:** (Primary Key: Queue ID) Fields: Associated Node, Job List, Scheduling Policy.
*   **Cluster Status:** (Primary Key: Timestamp) Fields: Total CPU Load, Node Status Summary, Aggregate Pending Job Count.
*   **Scheduling Ticket:** (Primary Key: [Job ID, Node ID]) Fields: Number of Tickets, Stride Value, Current Pass Value.

## Non-functional Requirements
1.  **Performance:** Job submission response time must be under 1 minute.
2.  **Reliability:** Maximum bug rate of 1 bug per thousand lines of code (KLOC).
3.  **Scalability:** Scheduler performance must not degrade with the addition of nodes and jobs.
4.  **Security:** Ensure user privacy and prevent unauthorized alteration of scheduling criteria.
5.  **Deadline Sensitivity:** Ensure jobs complete within a 10% error margin of their submitted deadlines (assuming accurate job statistics).
6.  **Supportability:** Code must follow Hungarian Naming Convention and GNU General Purpose License standards.

## Milestones and External Dependencies
1.  Successful integration with the Sun Grid Engine (SGE) v5.3 cluster management system.
2.  Availability of a 4-node Pentium-III Linux cluster for implementation and testing.
3.  Dependence on SGE's functionality for job queuing, resource management, and process migration.
4.  Use of PVM/MPI libraries for the execution of embarrassingly parallel jobs.
5.  Development or acquisition of a simulation tool for testing scheduler performance.

## Risks and Mitigation Strategies
1.  **Risk:** Inaccurate user estimates of job execution time leading to missed deadlines.
    *   **Mitigation:** Rely on the 10% error allowance in scheduling and potentially develop guidelines for user estimation.
2.  **Risk:** Performance bottlenecks or failures in the underlying SGE components.
    *   **Mitigation:** Thorough testing of the integrated system and adherence to SGE's interface specifications.
3.  **Risk:** Limited testing scale due to small (4-node) hardware cluster.
    *   **Mitigation:** Develop or use a simulation tool to model larger cluster environments and loads.
4.  **Risk:** Complexity of implementing a dynamic, proportional-share scheduling algorithm.
    *   **Mitigation:** Prototype the stride-scheduling algorithm independently before full integration.
5.  **Risk:** Security vulnerabilities from extended user interfaces (budget/deadline submission).
    *   **Mitigation:** Implement strict user authentication and authorization checks within the SGE framework.

## Undecided Issues
1.  The exact economic model and pricing policy for charging users.
2.  Whether to develop a custom Graphical User Interface (GUI) or rely on command-line/SGE interfaces.
3.  Whether to design a custom simulation tool or use a freely available generic one for testing.
4.  The specific heuristics to be used for the scheduling problem to avoid exhaustive searches.
5.  The detailed implementation of the "job accounting" module for tracking resource usage and costs.
6.  The process for users to modify certain job parameters (like output directory) after submission.