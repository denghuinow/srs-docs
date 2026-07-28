**Purpose & Scope**
The system ensures the CAISO grid can be restored after a complete or major blackout. It does this by planning for, testing, and maintaining generators that can start without external power. The plan does not cover generators that can only safely reject load down to their auxiliary load.

**Product Background / Positioning**
This is the CAISO's formal Black Start Capability Plan (BCP). It exists to meet WECC and NERC reliability standards for system restoration. It governs the relationship between the CAISO and generator owners/operators under Reliability Must Run (RMR), Interim, or voluntary Black Start contracts.

**Core Functional Overview**
*   Determine required quantity and location of Black Start generators via contingency studies.
*   Annually verify sufficiency of Black Start units against WECC requirements.
*   Document cranking paths from Black Start units to other generators.
*   Conduct periodic performance tests of contracted Black Start units.
*   Maintain a database of all designated Black Start generators.
*   Train grid operators annually on system restoration using Black Start units.

**Key Users & Usage Scenarios**
Primary users are CAISO planners, operators, and test administrators. Generator owners/operators participate in testing and reporting. Operators use the plan during training simulations and actual blackout restoration events. Contracted units are subject to scheduled and unscheduled performance tests.

**Major External Interfaces**
Interfaces exist with generator owners/operators for testing and contracting. Coordination is required with WECC, NERC, neighboring Balancing Authorities, and Transmission Owners. The system interacts with grid control systems (SCADA) and market scheduling systems for test energy.

**Key Non-functional Requirements**
*   Black Start units must maintain voltage within emergency limits from no load to full load.
*   Units must start and synchronize to the grid within defined time limits (e.g., 30 minutes for hydro/gas turbines, 2.5 hours for hot steam turbines).
*   The plan and associated database are reviewed and updated at least annually.
*   Test records and deficiency plans must be provided to WECC/NERC within 30 days of request.

**Constraints, Assumptions & Dependencies**
The plan is constrained by NERC and WECC reliability standards. It depends on generator owners/operators to perform tests and report results. A key assumption is that a percentage of Black Start units will fail to start during a real event. Hydroelectric units cannot be tested during periods of constrained water availability.

**Priorities & Acceptance Approach**
The highest priority is ensuring sufficient, tested Black Start capacity is available for grid restoration. Acceptance is based on generators passing performance tests (e.g., maintaining 99% of requested output during a 4-hour test) and the CAISO's annual verification that planning requirements are met. Failure requires a corrective action plan from the generator owner.