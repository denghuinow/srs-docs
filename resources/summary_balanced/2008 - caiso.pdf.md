# Balanced Summary

## Goals and Scope
This plan ensures the availability of Black Start generators to restore the electrical grid after a major outage. It covers planning, testing, and coordination to meet WECC and NERC requirements for system restoration. The scope includes RMR units, Interim Black Start units, and voluntary participants within the CAISO Balancing Authority Area.

## Roles and User Stories
- **Grid Operator**: I want to dispatch Black Start units during emergencies so that system restoration can begin promptly.
- **Generator Owner**: I want to test my unit's Black Start capability so that it can be certified for system restoration use.
- **CAISO Planner**: I want to determine required Black Start capacity locations so that restoration plans meet contingency study needs.
- **Test Administrator**: I want to evaluate Black Start test results so that unit availability can be accurately determined.
- **Training Coordinator**: I want to conduct annual restoration simulations so that operators maintain proficiency with Black Start procedures.

## Key Processes
1. **Trigger: Annual planning cycle** - CAISO determines Black Start requirements through contingency studies.
2. **Trigger: Generator request** - Voluntary Black Start units demonstrate capability through testing every five years.
3. **Trigger: CAISO dispatch** - RMR and Interim Black Start units undergo performance tests with or without notice.
4. **Trigger: Test completion** - Participants notify CAISO of test results within 24 hours and submit detailed reports within 14 days.
5. **Trigger: Database maintenance** - CAISO updates Black Start database annually with unit information and test status.
6. **Trigger: Training schedule** - Grid operators receive annual restoration training including Black Start procedures.
7. **Trigger: System blackout** - Certified Black Start units initiate restoration without external power assistance.

## Domain Data Elements
- **Black Start Unit** (Unit ID): Name, Location, Capacity, Type, Latest Test Date
- **Test Record** (Test ID): Unit ID, Test Date, Duration, Success Status, Requested MW
- **Contingency Study** (Study ID): Outage Scenario, Demand Level, Required Capacity, Affected Area
- **Contract** (Contract ID): Unit ID, Type (RMR/Interim), Terms, Availability Requirements
- **Training Record** (Training ID): Operator ID, Date, Simulation Type, Completion Status
- **Cranking Path** (Path ID): Source Unit, Destination, Switching Requirements, Diagram Reference

## Non-functional Requirements
- Units must start within technology-specific time limits (30 minutes to 2.5 hours)
- Database must be reviewed and updated annually
- Operators must receive annual restoration training
- Test documentation must be provided to regulators within 30 days of request
- Communication systems must be adequate during restoration
- Voltage must be maintained within emergency limits during Black Start operation

## Milestones and External Dependencies
- Annual planning evaluation completion
- WECC restoration plan compliance verification
- Five-year testing cycle for voluntary units
- Annual RMR and Interim Black Start contract negotiations
- System simulator availability for operator training

## Risks and Mitigation Strategies
- **Risk**: Black Start unit failure during actual emergency
  **Mitigation**: Regular testing and performance verification
- **Risk**: Insufficient Black Start capacity in critical locations
  **Mitigation**: Annual planning studies and contract negotiations
- **Risk**: Operator unfamiliarity with restoration procedures
  **Mitigation**: Mandatory annual training and simulations
- **Risk**: Transmission path unavailability during restoration
  **Mitigation**: Cranking path documentation and coordination
- **Risk**: Test energy market scheduling complications
  **Mitigation**: Required CAISO market schedule submission for tests

## Undecided Issues
- Percentage of Black Start units expected to fail to start (to be determined by CAISO)
- Specific start time limits for unspecified technologies or cross-region units
- Full implementation timeline for system simulator training
- Not mentioned
- Not mentioned
- Not mentioned