# Short Summary: Libra – An Economy-Driven Cluster Scheduler

## Background and Objectives
Libra is an economy-driven cluster scheduler designed as an add-on to the Sun Grid Engine (SGE) cluster management system. Its primary objective is to provide Quality of Service (QoS) through a computational economy model, scheduling CPU time based on user utility (budget and deadline) rather than solely system performance.

## In Scope
- Managing sequential and embarrassingly parallel batch jobs on a homogeneous Linux cluster.
- Implementing a bid-based proportional resource-sharing economic model.
- Utilizing the stride scheduling algorithm to enforce proportional CPU time allocations.
- Providing job submission, status viewing, and deletion/change functionalities via SGE interfaces.
- Ensuring dynamic, scalable, and configurable scheduling with administrative security.

## Out of Scope
- Managing real parallel jobs with dependent threads requiring inter-job communication.
- Supporting job migration for decreasing resource fragmentation.
- Including user-to-user bargaining mechanisms for resource negotiation.
- Developing a dedicated GUI in the initial version (command-line interface only).
- Exhaustive search algorithms for job scheduling; heuristics will be used instead.

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Cluster Users:** Submit jobs with budget and deadline constraints to the cluster.
- **Cluster Administrators:** Oversee cluster scheduling, usage, and modify policies.
- **Project Owner/Client (Rajkumar Buyya):** Defines project vision and requirements.
- **Faculty Advisor (Dr. Arif Zaman):** Provides academic guidance and oversight.
- **Project Group (Jahanzeb Sherwani, Nosheen Ali, Nausheen Lotia, Zahra Hayat):** Develop and implement the Libra scheduler.

**User Stories:**
1. As a cluster user, I want to submit a job with budget and deadline parameters so that my job is scheduled according to my QoS needs.
2. As a cluster user, I want to view my job's execution status so that I can monitor progress and plan accordingly.
3. As a cluster user, I want to cancel or modify non-critical job parameters so that I can adapt to changing requirements.
4. As a cluster administrator, I want to check the load and status of each cluster node so that I can ensure efficient resource utilization.
5. As a cluster administrator, I want to alter the cluster's cost structure and scheduling policies so that I can optimize overall system performance and fairness.
6. As a cluster administrator, I want to cancel, suspend, or resume any job so that I can manage cluster resources and address issues proactively.

## Success Metrics
- All jobs are completed within a 10% error margin of their submitted deadlines, assuming accurate job statistics.
- The scheduler maintains scalability without performance degradation as nodes and jobs are added to the cluster.
- User costs never exceed the maximum budget specified during job submission.

## Major Constraints
- Hardware is limited to a test cluster of four Pentium-III workstations with 128 MB RAM running Linux and SGE.
- The scheduler must integrate as a sub-component of SGE version 5.3 without modifying the Linux kernel.
- All code must be written in standard C and comply with GNU General Public License (GPL) open-source requirements.
- A simulation tool for testing may need to be developed if no suitable free alternative is available.
- The initial release will only support a command-line interface via Linux or SGE, not a dedicated GUI.

## Undecided Issues
- The exact costing and pricing policy for charging users will be specified in a later version.
- Whether to develop a custom simulation tool or use an available generic tool for testing purposes.
- The potential future addition of a GUI for user and administrator interfaces after core functionality is implemented.