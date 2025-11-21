# Detailed Summary

## Background and Scope
The ERTMS/ETCS Functional Requirements Specification defines operational requirements for the European Train Control System, focusing on interoperability and safety across European railways. It specifies mandatory (M) and optional (O) functions for train control and supervision, covering multiple application levels (0-3) and operational states. Non-goals include detailed technical implementation specifications, environmental requirements, training procedures, and RAMS specifications, which are intentionally omitted from this document.

## Role Matrix and Use Cases
**Roles:** Driver, RBC (Radio Block Centre), Infrastructure Systems, STM (Specific Transmission Module), Maintenance Personnel, Traffic Management  
**Main Scenarios:**  
- Train startup with self-test and data entry  
- Level transitions between ETCS application levels  
- Movement authority supervision and revocation  
- Emergency stop commands from RBC  
- Shunting operations with speed supervision  
**Exception Scenarios:**  
- Transmission failures with fallback procedures  
- Equipment failures triggering brake intervention  
- Unauthorized level transitions requiring driver acknowledgement  

## Business Process
**Main Process (Train Operation):**  
1. System startup and self-test  
2. Train data entry and validation  
3. Movement authority reception  
4. Speed profile calculation  
5. Continuous train supervision  
6. Driver interface interaction  
7. Brake intervention when required  
8. Data recording and reporting  

**Key Branch (Failure Handling):**  
Trigger: Transmission failure  
1. Detect communication loss  
2. Apply national failure procedure  
3. Notify driver via DMI  
4. Execute brake intervention if required  

**Key Branch (Level Transition):**  
Trigger: Level change detection  
1. Validate train capability for new level  
2. Request driver acknowledgement if responsibility increases  
3. Apply brake if acknowledgement not received  
4. Transition operational state  

## Domain Model
**Entities:**  
- Train (required: identification, length, speed, category)  
- Driver (required: identification, language)  
- Movement Authority (required: target location, validity period)  
- RBC (required: identification, area coverage)  
- National Values (required: default values, area applicability)  
- Operational State (required: current state, transition rules)  
- Speed Profile (required: static profile, dynamic braking curves)  
- DMI (required: display configuration, language setting)  

## Interfaces and Integrations
- **RBC to Train** (Direction: Bidirectional)  
  Theme: Movement authority and train position exchange  
  Input: Train location, integrity status  
  Output: Movement authorities, emergency commands  
  SLA: Continuous communication with fallback procedures

- **Infrastructure to Train** (Direction: Track-to-train)  
  Theme: Track data and national values transmission  
  Input: Balise/loop/radio messages  
  Output: Speed profiles, track descriptions  
  SLA: Intermittent/continuous based on application level

- **STM Integration** (Direction: Bidirectional)  
  Theme: National system compatibility  
  Input: National system data  
  Output: ETCS-compatible information  
  SLA: Non-interference with ETCS operation

## Acceptance Criteria
**Train Startup:**  
Given train is powered on  
When self-test completes successfully  
Then DMI displays ready status and permits data entry

**Movement Authority Supervision:**  
Given valid movement authority is received  
When train approaches authority limit  
Then system calculates braking curve and provides driver warning

**Level Transition:**  
Given train approaches level transition boundary  
When higher responsibility level is entered  
Then system requests driver acknowledgement before proceeding

## Non-functional Metrics
**Performance:** Maximum operational speed of 500 km/h; Driver acknowledgement timeout of 5 seconds  
**Reliability:** Continuous operation during transmission failures; Redundant radio systems for RBC handover  
**Security:** Protected override controls; Secure train identification transmission  
**Compliance:** CCS TSI compatibility; National value harmonization  
**Observability:** Comprehensive data recording with UTC timestamping; Two-tier data retention (24 hours for accidents, 1 week for operational data)

## Milestones and Release Strategy
1. Version 5.00 official release (June 2007)
2. Implementation of mandatory functions across participating railways
3. STM integration for national system compatibility
4. RBC deployment for level 2/3 operations
5. Driver training program development
6. System validation and interoperability testing

## Risk List and Mitigation Strategies
1. **Transmission failures** - Implement multiple fallback procedures based on national values
2. **Equipment failures** - Automatic brake application and RBC notification
3. **Level transition errors** - Driver acknowledgement requirements and automatic brake application
4. **Data integrity issues** - Validation checks and default value usage
5. **Driver error** - Protected controls and confirmation requirements
6. **National system interference** - STM compatibility requirements
7. **Train integrity monitoring** - Manual confirmation capability when automated systems fail
8. **RBC handover failures** - Dual radio system support for seamless transitions

## Undecided Issues and Responsible Parties
1. Detailed environmental specifications - Not mentioned
2. Specific RAMS requirements - Not mentioned
3. Comprehensive training requirements - Not mentioned
4. Detailed DMI specifications - Not mentioned
5. Exact performance metrics beyond speed - Not mentioned
6. Specific security implementation details - Not mentioned
7. Maintenance procedures and intervals - Not mentioned
8. Detailed interoperability testing protocols - Not mentioned