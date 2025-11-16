# Detailed Summary

## Background and Scope
This Black Start Capability Plan ensures the CAISO Balancing Authority Area maintains adequate Black Start generation capacity for system restoration following major blackouts. The plan covers grid planning, generator testing, recordkeeping, and operator training to meet WECC and NERC requirements. It applies to RMR Black Start Units, Interim Black Start Units, and Voluntary Black Start Units seeking CAISO recognition. Non-goals include addressing generators that can safely reject load down to auxiliary load and detailed field-level implementation procedures.

## Role Matrix and Use Cases
- **CAISO Grid Operators**: Execute system restoration using Black Start units
- **CAISO Operations Support Test Administrator**: Manages Black Start testing and availability determination
- **RMR/Interim Black Start Unit Owners**: Perform testing and maintain unit capability
- **Voluntary Black Start Participants**: Seek CAISO recognition through testing
- **Scheduling Coordinators**: Receive test dispatch notices
- **WECC/NERC**: Request documentation and review compliance

Main scenarios: Annual planning evaluation, Black Start testing (scheduled and unscheduled), system restoration execution, recordkeeping updates. Exception scenarios: Test failures, unit deficiencies, constrained water availability for hydro units.

## Business Process
**Main Process - Black Start Testing (8 steps):**
1. CAISO requests test from RMR/Interim units or Participant submits request
2. Submit G-213H Black Start Test Report Form to Operations Support Test Administrator
3. Alhambra Generation Dispatcher notifies SC via telephone before test
4. Transmit Availability Test Dispatch Notice electronically
5. Unit ramps to requested MW before first hour
6. Maintain requested MW for four full hours
7. Unit ramps down or continues in market transaction
8. Operations Support determines availability using revenue meter data

**Key Branch - Test Failure (≤4 steps):**
- Unit fails 99% availability threshold
- Set Availability Limit to achieved level
- Submit explanation and correction plan to CAISO
- Provide results to WECC/NERC upon request

## Domain Model
- **Black Start Unit** (required: name, location, MW capacity, type, latest test date, starting method; unique: unit identifier)
- **Test Record** (required: test date, duration, success indicator; reference: Black Start Unit)
- **RMR Contract** (required: contract terms, availability limits; reference: Black Start Unit)
- **Interim Contract** (required: contract terms; reference: Black Start Unit)
- **Cranking Path** (required: path diagram, switching requirements; reference: Black Start Unit)
- **Training Record** (required: training date, simulation results; reference: Grid Operator)
- **Test Dispatch Notice** (required: dispatch time, requested MW; reference: Black Start Unit)
- **Availability Calculation** (required: MWh output, temperature correction; reference: Test Record)

## Interfaces and Integrations
- **SCADA System**: Direction - bidirectional; Interaction - monitoring and control; Input - unit status; Output - operational commands; SLA - real-time during restoration
- **Market Scheduling System**: Direction - outbound; Theme - test energy scheduling; Input - test schedule; Output - market transactions; SLA - daily operations
- **WECC/NERC Reporting**: Direction - outbound; Theme - compliance documentation; Input - test results; Output - standardized reports; SLA - 30-day response time
- **Revenue Metering System**: Direction - inbound; Theme - availability calculation; Input - MWh data; Output - availability percentage; SLA - post-test processing

## Acceptance Criteria
- Given a Black Start unit has completed testing, When the CAISO reviews test results, Then the unit shall be added to the Black Start database if it meets all technical requirements
- Given a system blackout occurs, When Grid Operators initiate restoration, Then designated Black Start units shall start within specified time limits based on unit type
- Given an RMR unit fails availability test, When the owner submits correction plan, Then CAISO shall review and update unit status accordingly

## Non-functional Metrics
- **Performance**: Black Start units must start within technology-specific time limits (30min-2.5hr); Voltage regulation within emergency limits during restoration
- **Reliability**: Annual verification of Black Start capacity; 99% availability threshold for RMR units
- **Security**: Restricted distribution of System Restoration procedure E-501; Secure test documentation
- **Compliance**: Adherence to NERC EOP-005 and EOP-009 standards; WECC restoration plan requirements

## Milestones and Release Strategy
- Annual planning evaluation and contract updates
- Quarterly operator training sessions
- Five-year comprehensive plan review cycle
- Annual testing of at least one-third of RMR/Interim units
- System simulator implementation for enhanced training
- Database annual review and updates

## Risk List and Mitigation Strategies
- **Unit test failures**: Require correction plans and retesting; adjust availability limits
- **Insufficient Black Start capacity**: Annual planning evaluation; contract additional units
- **Communication system failure**: Test telephone and SCADA during Black Start tests
- **Transmission path unavailability**: Document and maintain cranking paths; coordinate with PTOs
- **Operator training gaps**: Annual training with simulation exercises
- **Documentation non-compliance**: 30-day response requirement for WECC/NERC requests
- **Water constraints for hydro**: No testing during constrained availability periods
- **Test scheduling conflicts**: Flexible testing approach with market schedule coordination

## Undecided Issues and Responsible Parties
- Specific percentage of Black Start units expected to fail to start - CAISO Planning
- Detailed temperature correction factor methodology - CAISO Operations Support
- Full system simulator implementation timeline - CAISO Training Department
- Technology-specific start time limits for unspecified technologies - CAISO Technical Committee
- Coordination procedures with neighboring Balancing Authorities - CAISO External Relations
- Specific successive start requirements in contracts - CAISO Contract Management
- Communication adequacy evaluation criteria - CAISO Operations
- Limited energy resource selection criteria - CAISO Planning