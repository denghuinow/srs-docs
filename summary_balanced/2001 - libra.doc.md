# Balanced Summary

- **Goals and scope**  
  Libra is an economy-driven cluster scheduler designed to maximize user utility by scheduling CPU time based on user-defined budget and deadline constraints rather than system performance. It operates as an add-on to the Sun Grid Engine (SGE) cluster management system, managing sequential and embarrassingly parallel batch jobs on a homogeneous Linux cluster.

- **Roles and user stories**  
  - As a cluster user, I want to submit jobs with budget and deadline so that my computational needs are prioritized according to my constraints.  
  - As a cluster user, I want to monitor job status so that I can track progress and execution.  
  - As a cluster user, I want to cancel or modify my jobs so that I can adjust to changing requirements.  
  - As a cluster administrator, I want to check node status and cluster usage so that I can oversee resource allocation and performance.  
  - As a cluster administrator, I want to alter scheduling policies and cost structures so that I can optimize cluster operation and user satisfaction.

- **Key processes**  
  1. Trigger: Job submission → Initialize job details and parse parameters.  
  2. Accept or reject job based on budget, deadline, and cluster load.  
  3. Calculate scheduling information (tickets, stride, pass) using stride scheduling.  
  4. Determine execution host considering load balancing and job type.  
  5. Dispatch job to the selected host and queue.  
  6. Update cluster status to reflect reserved resources and queue changes.  
  7. Execute job using stride-scheduling to time-slice CPU quanta.

- **Domain data elements**  
  - Job: Job ID, Job Type, Execution Time, Budget, Deadline  
  - User: User ID, Name, Authentication ID, Credit Balance  
  - Cluster Node: Node ID, CPU Load, Available Memory, Queue Status  
  - Scheduling Info: Tickets, Stride, Pass, Quantum  
  - Queue: Queue ID, Host ID, Job List, Load Status  
  - Execution Host: Host ID, System Type, Current Load, Pending Jobs

- **Non-functional requirements**  
  - Scalable performance with increasing nodes and jobs.  
  - Maximum response time of 1 minute for job submission.  
  - Deadline sensitivity with 10% completion error allowance.  
  - Security to prevent unauthorized job or scheduling alterations.  
  - Adherence to GNU coding standards and open-source licensing.  
  - Support for command-line and SGE-based user/administrator interfaces.

- **Milestones and external dependencies**  
  - Integration with Sun Grid Engine 5.3 cluster management system.  
  - Use of PVM and MPI libraries for parallel job execution.  
  - Availability of a 4-node Pentium-III Linux cluster for testing.  
  - Development or adoption of a simulation tool for performance analysis.  
  - Release under GPL open-source license.

- **Risks and mitigation strategies**  
  - Risk: Limited hardware for testing may affect performance validation. Mitigation: Use simulation tools to model larger clusters.  
  - Risk: User job execution time inaccuracy may impact scheduling. Mitigation: Assume users provide fair estimates; suggest alternatives if needed.  
  - Risk: SGE compatibility issues with Libra’s scheduling policies. Mitigation: Assume SGE module workability and test integration early.  
  - Risk: Scalability challenges with high job loads. Mitigation: Design heuristics to avoid exhaustive search, ensure dynamic resource allocation.  
  - Risk: Insufficient job accounting features. Mitigation: Implement basic job accounting module as part of scheduler functions.

- **Undecided issues**  
  - Detailed costing and pricing policy for user charges.  
  - Development of a dedicated GUI for job submission and administration.  
  - Decision on designing a custom simulation tool versus using a generic one.  
  - Support for job migration to reduce resource fragmentation.  
  - Not mentioned  
  - Not mentioned