**Purpose & Scope**
Libra is an economy-driven scheduler add-on for the Sun Grid Engine cluster management system, providing quality-of-service computational economy for sequential and embarrassingly parallel batch jobs on a homogeneous Linux cluster.

**Core Functions**
*   Accept or reject jobs based on user-submitted budget and deadline constraints.
*   Schedule accepted jobs using a bid-based proportional resource-sharing model and the stride-scheduling algorithm.
*   Dispatch and execute jobs on selected cluster nodes.

**Key Constraints**
*   Must function as a sub-component of the Sun Grid Engine (SGE) cluster management system.
*   All code must be written in standard C.
*   The scheduler will not perform exhaustive searches for job combinations; it will use heuristics.