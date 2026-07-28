# Detailed Summary: ERTMS/ETCS Functional Requirements Specification (FRS) v5.00

## Background and Scope
This document defines the functional requirements for the European Rail Traffic Management System/European Train Control System (ERTMS/ETCS). It primarily specifies operational requirements to ensure safe train supervision and control across European railways, supporting interoperability. The scope covers onboard, trackside, and control center functions across multiple application levels (0, 1, 2, 3, STM). Non-goals include detailed technical specifications (deferred to SRS), driver-machine interface design details, training procedures, RAMS, and environmental specifications, which are intentionally omitted or marked for separate documentation.

## Stakeholders Matrix and Use Cases
*   **Driver**: Operates the train using ETCS information and interfaces; responsible for data entry, acknowledgments, and safe driving.
*   **Railway Infrastructure Manager**: Provides and maintains trackside equipment (balises, loops, RBC) and infrastructure data.
*   **Train Operator/Railway Undertaking**: Responsible for trainborne equipment, train data, and overall service operation.
*   **ETCS Onboard System**: Executes core supervision, braking, and data processing functions based on inputs from trackside and driver.
*   **Radio Block Centre (RBC)**: Central trackside safety unit for Levels 2/3; manages movement authorities, train separation, and emergency commands.
*   **Specific Transmission Module (STM)**: Interfaces with national train control systems to provide compatibility.
*   **Maintenance Personnel**: Performs diagnostics and repairs based on system fault indications and recorded data.
*   **Safety Authority/Regulator**: Defines and oversees compliance with mandatory (M) safety requirements and national values.

**Main Scenarios**: 1) Train startup with self-test and data entry. 2) Receiving a movement authority and operating under Full Supervision. 3) Transition between application levels or operational states (e.g., to Shunting or On Sight). 4) Responding to a speed supervision warning or brake intervention. 5) Handling transmission failure or equipment fault. 6) Receiving and acknowledging plain text or emergency messages from trackside. 7) Executing a train trip or emergency stop procedure. 8) Recording journey data for investigation.
**Exception Scenarios**: Driver fails to acknowledge a required transition; train passes a stop signal; loss of communication with RBC; onboard equipment failure; revocation of a movement authority while train is moving.

## Business Process
**Main Process: Supervised Train Journey**
1.  **Trigger**: Driver powers on onboard equipment. **Input**: Power. **Output**: System start.
2.  Onboard performs automatic self-test; result indicated on DMI.
3.  Driver enters/confirms train and driver data (must be stationary for manual entry).
4.  System receives national values and infrastructure data from trackside.
5.  System receives a movement authority (MA) from trackside (e.g., via balise or RBC).
6.  Onboard calculates static and dynamic speed profiles, supervising speed and distance to end of MA.
7.  Driver drives train with information/guidance from DMI; system provides warnings before intervention.
8.  **Output**: Train reaches end of journey; data is recorded.

**Key Branch A: Transition to Shunting Operation**
1.  **Trigger**: Driver selection or automatic transition based on trackside info. **Input**: Shunting request.
2.  If under RBC control, permission must be obtained from RBC.
3.  Driver confirmation is requested (if automatic transition).
4.  System supervises to a national shunting speed limit. **Output**: Train in Shunting operational state.

**Key Branch B: Handling a Transmission Failure**
1.  **Trigger**: Loss of communication with trackside (e.g., RBC).
2.  System applies reaction per National Value: immediate emergency brake, service brake, or proceed to end of current MA.
3.  Failure is indicated to the driver on DMI.
4.  If possible, restriction is transmitted to RBC. **Output**: Train in a safe state or proceeding under restrictions.

## Domain Model
Core entities and their key attributes:
*   **Train**: TrainIdentification (required), MaxSpeed (required), Length (required), AxleLoad, Gauge, AirTightStatus, BrakeCalculationData.
*   **Driver**: DriverID (required), SelectedLanguage.
*   **Movement Authority (MA)**: AuthorityID, EndLocation (required), AssociatedTrackData (reference), Timeouts (optional).
*   **Operational State**: CurrentState (required, e.g., Full Supervision, Shunting), PreviousState.
*   **National Value**: ValueType (e.g., ceiling speed for unfitted operation), GeographicArea (required), DefaultValue (reference).
*   **Speed Profile**: StaticProfile (calculated from infrastructure/train data), DynamicProfile (calculated braking curves).
*   **Train Location**: FrontPosition, TrainLength, OdometryError.
*   **Recorded Data**: EventType (required), Timestamp (UTC, required), TrainID (reference), Details.

## Interfaces and Integrations
*   **Driver-Machine Interface (DMI) - Onboard**: Direction: Bidirectional. Interaction: Primary user interface. Input: Driver acknowledgments, data entry, selections. Output: Speed, target distance, warnings, system status, text messages. SLA: Information must be clear and timely to allow safe reaction.
*   **Trackside Transmission (Balise/Loop) - Onboard**: Direction: Track-to-train (primarily). Interaction: Intermittent data provision. Input: Movement authorities, track description, national values. Output: (For loops) train data. SLA: Data must be received and processed reliably at designated locations.
*   **Radio (GSM-R) - RBC**: Direction: Bidirectional. Interaction: Continuous communication for Levels 2/3. Input: Train position, integrity, data. Output: Movement authorities, emergency commands, plain text. SLA: High availability and safety-critical data integrity required.
*   **Specific Transmission Module (STM) - National System**: Direction: Bidirectional. Interaction: Compatibility interface. Input: National system data. Output: ETCS-formatted data for onboard processing. SLA: Must not interfere with national system safety.
*   **Braking System - Onboard**: Direction: Onboard-to-train. Interaction: Control command. Input: Commands for service or emergency brake intervention. Output: Brake application. SLA: Fail-safe activation upon safety-critical commands.
*   **Recording Interface - External Media**: Direction: Onboard-to-external. Interaction: Data extraction. Input: Request for data. Output: Recorded journey data. SLA: Standardized format for investigation.
*   **Railway Management System - Onboard/RBC**: Direction: To ETCS. Interaction: Provision of operational data. Input: Train scheduling/data. Output: (Potential) advisory information. SLA: Non-safety-critical informational exchange.

## Acceptance Criteria
**Capability: Train Operation under Full Supervision**
*   Given a train with valid data is in Full Supervision, When it approaches the end of its movement authority, Then the onboard system shall calculate and supervise a braking curve and provide a warning at least 5 seconds before intervention.
*   Given the train is moving, When it exceeds the permitted speed by a harmonised margin, Then the onboard equipment shall execute a brake intervention until speed is compliant.

**Capability: Level/State Transition**
*   Given a train approaches a level transition to a higher ETCS level, When trackside information is received, Then the onboard shall automatically switch to the highest level it is equipped for.
*   Given an automatic transition occurs that increases driver responsibility, When the transition happens, Then ETCS shall request driver acknowledgement and apply brakes if not given.

**Capability: Failure Handling**
*   Given a loss of transmission with the RBC occurs, When the failure is detected, Then the onboard system shall react according to the predefined National Value (e.g., apply brake or proceed to MA end).

## Non-functional Metrics
*   **Performance**: System must be functional up to 500 km/h train speed. Driver must acknowledge transitions within 5 seconds when required.
*   **Reliability/Availability**: Onboard equipment must perform automatic self-test at start-up. Recorded data for accidents must be stored for at least 24 hours; operational data for at least one week.
*   **Security/Compliance**: Must be compatible with existing national systems as per CCS TSI without interference. Mandatory (M) requirements shall be respected in every application.
*   **Observability**: All data entered, received, or indicated to the driver shall be recorded with UTC timestamp. Faults and system status must be indicated to the driver on the DMI.

## Milestones and Release Strategy
1.  Finalization and agreement on FRS v5.00 content (Official Release 21 June 2007).
2.  Development of detailed System Requirement Specification (SRS) based on FRS.
3.  Sub-system development and testing (e.g., onboard, RBC, balise).
4.  Integration testing and interoperability trials across different levels (0-3, STM).
5.  Safety approval and certification for mandatory functions.
6.  Phased deployment by railways, potentially starting with Level 1 or 2 on key corridors.

## Risk List and Mitigation Strategies
1.  **Risk**: Interoperability failure between different ETCS levels or national systems. **Mitigation**: Strict adherence to mandatory requirements and compatibility rules defined in FRS and TSI.
2.  **Risk**: Loss of continuous radio communication (Levels 2/3) leading to service disruption. **Mitigation**: Define and implement robust fall-back procedures (National Values for transmission failure).
3.  **Risk**: Incorrect train data entry compromising safety calculations. **Mitigation**: Data validation, use of default/harmonized values, and allowing entry only when stationary.
4.  **Risk**: Driver misunderstanding or missing DMI warnings/acknowledgments. **Mitigation**: Clear DMI design principles, standardized indications, and acoustic alerts.
5.  **Risk**: Onboard equipment failure during operation. **Mitigation**: Fail-safe design to apply brake and stop train, with clear fault indication.
6.  **Risk**: Inconsistent implementation of optional (O) functions leading to operational confusion. **Mitigation**: CCS TSI to define specific conditions where optional functions become mandatory for safety.
7.  **Risk**: Errors in odometry leading to inaccurate train location. **Mitigation**: Use of balises for position correction and accounting for odometry error in calculations (e.g., release speed).
8.  **Risk**: Unsafe state transition while train is moving. **Mitigation**: Automatic transitions where possible, with driver acknowledgement required for transitions increasing responsibility.

## Undecided Issues and Responsible Parties
*Note: The FRS v5.00 document explicitly marks many sections as "Intentionally deleted," indicating requirements were moved to the SRS or other documents. Therefore, specific undecided issues within this FRS are not listed. Detailed technical specifications, DMI design, training, RAMS, and environmental specs are the responsibility of respective working groups (e.g., UNISIG, EEIG) and are addressed in subordinate specifications.*