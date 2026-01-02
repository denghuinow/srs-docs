**Purpose & Scope**: The system is an economy-driven cluster scheduler add-on for the Sun Grid Engine (SGE) management system. It provides Quality of Service (QoS) by scheduling sequential and embarrassingly parallel batch jobs on a homogeneous Linux cluster based on user-submitted budget and deadline constraints.

**Core Functions**:
*   Accept or reject submitted jobs based on user budget, deadline, and current cluster state.
*   Calculate job scheduling parameters (tickets, stride) using a bid-based proportional resource-sharing model and the stride scheduling algorithm.
*   Dynamically allocate and enforce CPU time to jobs in proportion to their calculated priority/share.
*   Execute jobs by selecting the job with the minimum pass value for a time quantum, advancing its pass by its stride.

**Key Users**: Cluster users who submit jobs and cluster administrators who oversee scheduling and cluster usage.

**Key Constraints**: The scheduler must integrate as a component of the Sun Grid Engine (SGE) cluster management system. It must be implemented in standard C, use heuristic scheduling (not exhaustive search), and be released as open-source software under the GNU GPL license. Initial development and testing are constrained to a specific four-workstation Linux cluster.