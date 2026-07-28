# Balanced Summary: Black Start Capability Plan (BCP)

## Goals and Scope
The Black Start Capability Plan (BCP) ensures the CAISO Balancing Authority Area has sufficient, properly located Black Start generators to restore the electric grid after a major blackout. It covers planning, testing, recordkeeping, and training to maintain this restoration capability in coordination with WECC requirements. The scope includes voluntary, interim, and RMR-contracted Black Start units.

## Stakeholders and User Stories
*   **CAISO Grid Planners:** Determine required Black Start capacity and location through contingency studies.
*   **CAISO Real-Time Dispatchers:** Coordinate system restoration and receive test notifications.
*   **Black Start Unit Owners/Operators (RMR, Interim, Voluntary):** Maintain and demonstrate their unit's Black Start capability.
*   **CAISO Operations Support Test Administrator:** Manages test processes and evaluates unit availability.
*   **WECC/NERC:** Provides overarching reliability standards and requests documentation.
*   **Transmission Owners/Neighboring Balancing Authorities:** Coordinate planning and cranking paths.

**User Stories:**
1.  As a **CAISO Grid Planner**, I want to conduct annual contingency studies so that Black Start resources are sufficient and well-located for restoration.
2.  As a **Black Start Unit Owner**, I want to test my unit's self-start capability every five years so that it remains certified for system restoration.
3.  As a **CAISO Real-Time Dispatcher**, I want to receive phone notification within 24 hours of a Black Start test so that I am aware of unit status.
4.  As the **CAISO Operations Support Test Administrator**, I want to receive completed test forms and ambient temperature data so that I can accurately calculate unit availability.
5.  As a **Transmission Owner**, I want to review cranking path documentation so that I can ensure transmission readiness for restoration.
6.  As a **WECC Representative**, I want to request test documentation so that I can verify regional compliance.

## Key Processes
1.  **Grid Planning (Trigger: Annual cycle or major system change):** CAISO determines required Black Start capacity and location via contingency studies.
2.  **Contracting (Trigger: Annual planning evaluation):** CAISO enters into RMR or Interim Black Start contracts with selected generators.
3.  **Test Initiation (Trigger: CAISO request or owner request):** A Black Start Test Notice is issued, or a unit owner submits a test request form.
4.  **Test Execution (Trigger: Test dispatch):** The unit starts without grid power, energizes a transmission path, and runs for a minimum duration.
5.  **Notification & Reporting (Trigger: Test completion):** The unit owner notifies the dispatcher by phone and submits a formal test result letter.
6.  **Recordkeeping (Trigger: Test completion or data change):** CAISO updates the Black Start database with test results and unit details.
7.  **Training (Trigger: Annual cycle):** CAISO grid operators are trained on restoration procedures and Black Start unit use.

## Domain Data Elements
*   **Black Start Unit** (Primary Key: Unit ID): Owner, Location, MW Capacity, Unit Type, Latest Test Date.
*   **Black Start Test** (Primary Key: Test ID): Unit ID, Test Date, Duration, Success/Failure Status, Output MWh.
*   **Cranking Path** (Primary Key: Path ID): Source Unit ID, Destination(s), Initial Switching Requirements, Diagram Reference.
*   **RMR/Interim Contract** (Primary Key: Contract ID): Unit ID, Start Date, End Date, Availability Limit, Technical Requirements.
*   **Contingency Study** (Primary Key: Study ID): Scenario Description, Outage Magnitude, Required Black Start Capacity, Assumptions.
*   **Training Record** (Primary Key: Training Session ID): Date, Participants, Simulation Scenario, Critique Report.

## Non-Functional Requirements
1.  **Availability:** Black Start units must achieve at least 99% of requested output during a four-hour availability test.
2.  **Performance:** Units must start and synchronize within technology-specific time limits (e.g., 30 mins for hydro/gas turbines).
3.  **Reliability:** The planning process must account for a percentage of Black Start units expected to fail on demand.
4.  **Maintainability:** The central Black Start database must be reviewed and updated at least annually.
5.  **Usability:** Operators must be trained annually on restoration procedures using relevant plans and simulations.
6.  **Compliance:** The plan and test results must satisfy NERC (EOP-005, EOP-009) and WECC requirements.

## Milestones and External Dependencies
1.  Annual completion of Black Start planning evaluation and contract renewals.
2.  Execution of Black Start tests for at least one-third of RMR/Interim units annually.
3.  Annual operator training on system restoration.
4.  **Dependency:** Coordination with WECC's regional Black Start Capability Plan.
5.  **Dependency:** Availability of a system simulator for enhanced operator training.

## Risks and Mitigation Strategies
1.  **Risk:** Black Start units fail to start or perform during an actual blackout.
    *   **Mitigation:** Regular testing, diverse fuel resources, and planning for a percentage of failures.
2.  **Risk:** Transmission damage blocks planned cranking paths.
    *   **Mitigation:** Document multiple paths and coordinate restoration plans with Transmission Owners.
3.  **Risk:** Inadequate communication systems hinder restoration coordination.
    *   **Mitigation:** Include communication aids in testing and planning evaluation.
4.  **Risk:** Limited energy resources (e.g., hydro) are depleted during extended restoration.
    *   **Mitigation:** Select such resources sparingly in the plan.
5.  **Risk:** Non-compliance with evolving NERC/WECC standards.
    *   **Mitigation:** Review and update the BCP at least every five years; submit documentation upon request.

## Undecided Issues
1.  The specific percentage of Black Start units expected to fail to start, to be determined by CAISO in studies.
2.  Start time limits for Black Start facilities in other reliability coordinator areas or with unspecified technologies are subject to negotiation.
3.  The frequency and scope of performance tests for RMR/Interim units conducted by CAISO "from time to time" without prior notification.
4.  The process for integrating a future system simulator into operator training.
5.  Specific corrective action plans for units failing CAISO criteria are defined by the owner/operator, not standardized.
6.  The method for CAISO to "pull its own" ambient temperature data if not submitted by a unit owner is unspecified.