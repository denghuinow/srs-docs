# Detailed Summary: Black Start Capability Plan (BCP)

## Background and Scope
This plan establishes the framework for ensuring the CAISO Balancing Authority Area has sufficient Black Start generation capability to restore the electric grid following a major blackout. It covers the planning, testing, recordkeeping, and training activities necessary to maintain designated generators that can self-start without off-site power. The scope includes managing contracts (RMR and Interim), conducting performance tests, and coordinating with regional entities like WECC. Non-goals include addressing generators that can only safely reject load to auxiliary levels and detailing field-level operational procedures for actual blackout events.

## Stakeholders Matrix and Use Cases
*   **CAISO Grid Planners**: Determine required Black Start capacity and location through contingency studies and annual verification.
*   **CAISO Real-Time (RT) Dispatcher**: Receives test notifications and coordinates operational actions during tests and actual events.
*   **CAISO Operations Support Test Administrator**: Manages the test scheduling, execution, and result analysis for Black Start units.
*   **Generator Owner/Operator (Participant)**: Responsible for demonstrating unit capability through testing and submitting required documentation.
*   **Scheduling Coordinator (SC)**: Receives test dispatch notices and manages market schedules for test energy.
*   **WECC/NERC**: Provides overarching reliability standards and requests documentation for review and compliance.
*   **Transmission Owner (PTO)**: Notified of tests and involved in planning cranking paths and transmission capacity.

**Main Scenarios**: 1) Annual planning verification of Black Start resources. 2) A Participant voluntarily seeks CAISO Black Start status. 3) CAISO requests a scheduled performance test for an RMR/Interim unit. 4) A unit owner requests an Availability Test.
**Exception Scenarios**: 1) A Black Start test fails to meet the 99% availability threshold. 2) A hydroelectric unit cannot be tested due to constrained water availability. 3) A unit retests and passes, requiring an update to its Availability Limit. 4) Ambient temperature data is not submitted post-test.

## Business Process
**Main Process: Annual Black Start Planning & Verification**
1.  **Trigger/Input**: Annual cycle or grid study update.
2.  CAISO Planners conduct contingency studies to determine required Black Start quantity and location.
3.  Verify sufficiency against WECC restoration plan requirements.
4.  Document cranking paths and initial switching requirements.
5.  Perform planning evaluation (fuel diversity, paths, communications, unit capability).
6.  Coordinate with neighboring Balancing Authorities and Transmission Owners.
7.  Enter into annual RMR/Interim Black Start contracts with selected generators.
8.  **Output**: Updated Black Start database and contracted generator portfolio.

**Key Branch A: Generator Unit Testing (RMR/Interim Unit)**
1.  **Trigger**: CAISO test request or owner's request.
2.  Owner submits test request using form G-213H to Test Administrator.
3.  CAISO Dispatcher notifies the SC and transmits the Test Dispatch Notice.
4.  Unit Operator ramps to requested MW and maintains it for four hours.
5.  **Output**: Test completion, result analysis, and potential update to unit's Availability Limit.

**Key Branch B: Recordkeeping Update**
1.  **Trigger**: Test completion or annual review.
2.  CAISO updates the Black Start database with test results and unit details.
3.  If a test fails, the owner must submit a corrective action plan.
4.  **Output**: Updated database and compliance documentation for WECC/NERC.

## Domain Model
*   **Black Start Unit** (required: UnitID [unique], Name, Location, Type, FuelType, MWCapacity, Status [Voluntary/Interim/RMR])
*   **Test Event** (required: TestID [unique], UnitID [reference], ScheduledDateTime, RequestedMW, ActualMWh, Result [Pass/Fail], TestReportURL)
*   **Contract** (required: ContractID [unique], UnitID [reference], Type [RMR/Interim], StartDate, EndDate, AvailabilityLimit)
*   **Cranking Path** (required: PathID [unique], SourceUnitID [reference], TargetUnitID [reference], DiagramReference)
*   **Contingency Study** (required: StudyID [unique], ScenarioDescription, OutageMagnitude, RequiredBlackStartMW)
*   **Participant (Owner/Operator)** (required: ParticipantID [unique], ContactInfo)
*   **Training Session** (required: SessionID [unique], Date, Topic, Attendees [reference to Operators], SimulationReportURL)
*   **Compliance Document** (required: DocID [unique], SubmittedBy [reference], ForEntity [WECC/NERC], SubmissionDate, Content)

## Interfaces and Integrations
*   **Market Scheduling System** (Direction: Outbound | Theme: Test Energy Scheduling | Input: Test parameters, unit ID | Output: Market schedule submission | SLA: Submit schedule prior to test)
*   **SCADA/Grid Telemetry** (Direction: Inbound | Theme: Real-time Unit Performance | Input: Voltage, frequency, MW output during test | Output: Data for test analysis | SLA: Real-time data feed during test window)
*   **Revenue Metering System** (Direction: Inbound | Theme: Test Result Validation | Input: Actual MWh output during 4-hour test | Output: Meter data for availability calculation | SLA: Data provided within 24h post-test)
*   **WECC/NERC Portals** (Direction: Outbound | Theme: Compliance Reporting | Input: Test results, corrective plans | Output: Submitted documentation | SLA: Within 30 days of request)
*   **Internal Database (E-501)** (Direction: Internal | Theme: Black Start Recordkeeping | Input: All unit data, test records, contracts | Output: Updated database for annual review | SLA: Annual update cycle)
*   **Dispatcher Communication (Phone/Electronic)** (Direction: Bi-directional | Theme: Test Coordination | Input: Test notices, success/failure calls | Output: Operational instructions | SLA: 24h notification for test results)

## Acceptance Criteria
**Capability: Annual Planning Verification**
*   Given the annual planning cycle has commenced, when CAISO planners complete contingency studies, then the required Black Start capacity and location are documented and verified against WECC requirements.
*   Given the planning evaluation is complete, when CAISO coordinates with neighboring authorities, then any interdependencies or gaps in regional Black Start coverage are identified.

**Capability: Unit Performance Testing**
*   Given an RMR unit is scheduled for an Availability Test, when the unit operates for the four-hour test period, then its availability is calculated (avg. MWh vs. requested MW) considering temperature correction.
*   Given a test fails the 99% threshold, when the Test Administrator analyzes the results, then the unit's Availability Limit is downgraded and a corrective action plan is requested from the owner.

**Capability: Recordkeeping & Compliance**
*   Given a Black Start test is completed, when the results are finalized, then the unit's record in the Black Start database is updated with the latest test date and status.
*   Given WECC requests documentation, when the 30-day window elapses, then the required test reports and justifications have been submitted.

## Non-Functional Metrics
*   **Performance**: 1) Black Start units must synchronize to the grid within technology-specific time limits (e.g., 30 min for hydro/gas turbine). 2) Test result analysis and database update completed within 14 days of test.
*   **Reliability**: 1) Annual verification ensures a sufficient percentage of Black Start units are available, accounting for expected failure-to-start rates. 2) Database availability for restoration events meets 99.9% uptime.
*   **Security/Compliance**: 1) All procedures and tests align with NERC EOP-005 and EOP-009 standards. 2) Access to the System Restoration database (E-501) is restricted.
*   **Observability**: 1) All test actions and dispatcher communications are logged with timestamps and responsible parties. 2) Training simulations include critique reports for performance tracking.

## Milestones and Release Strategy
1.  Complete annual Black Start planning study and resource verification.
2.  Execute annual RMR and Interim Black Start contract renewals.
3.  Schedule and complete performance tests for at least one-third of contracted units annually.
4.  Conduct annual Real-time Grid Operator training on system restoration and Black Start procedures.
5.  Update the Black Start database and submit annual compliance documentation to WECC/NERC as required.
6.  Review and update the BCP document at least every five years.

## Risk List and Mitigation Strategies
1.  **Risk**: Insufficient Black Start capacity due to generator retirements or failures.
    *   **Mitigation**: Annual planning studies identify gaps; CAISO proactively seeks new contracts or voluntary units.
2.  **Risk**: Black Start test fails, reducing available proven capacity.
    *   **Mitigation**: Require corrective action plans from owners; test a different unit to maintain required portfolio.
3.  **Risk**: Cranking paths are damaged or unavailable during a real event.
    *   **Mitigation**: Document multiple paths in planning; coordinate restoration switching with Transmission Owners.
4.  **Risk**: Non-compliance with evolving NERC/WECC standards.
    *   **Mitigation**: Assign compliance monitoring; update procedures and training annually.
5.  **Risk**: Operator error during a complex restoration event.
    *   **Mitigation**: Mandate annual training with system simulations and critiques.
6.  **Risk**: Communication failure during test or event.
    *   **Mitigation**: Test communication aids (phones, SCADA) as part of Black Start tests; have backup methods.
7.  **Risk**: Data inconsistency in the Black Start database.
    *   **Mitigation**: Implement annual review and update cycle with clear ownership (CAISO).
8.  **Risk**: Contracted unit unavailable due to market or maintenance conflicts.
    *   **Mitigation**: Contract with multiple units; include availability guarantees in RMR/Interim contracts.

## Undecided Issues and Responsible Parties
1.  Specific percentage of Black Start units expected to fail to start in contingency studies (to be determined by CAISO Planners).
2.  Start time limits for Black Start facilities using unspecified technologies (negotiated by CAISO with the Participant).
3.  Criteria and process for a "system simulator" for operator training (CAISO Training Department).
4.  Detailed temperature correction factor formula for test analysis (CAISO Operations Support Test Administrator).
5.  Process for integrating Voluntary Black Start units into the formal restoration sequence (CAISO Planners and Operators).
6.  Specific "successive starts" requirements within RMR/Interim contracts (CAISO Contract Management).
7.  Formal SLA for data exchange with neighboring Balancing Authorities for coordinated planning (CAISO Planners).
8.  Long-term strategy for phasing out limited energy resources (e.g., hydro) for Black Start (CAISO Planners).