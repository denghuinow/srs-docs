# Balanced Summary: ERTMS/ETCS Functional Requirements Specification (FRS) v5.00

## Goals and Scope
The ERTMS/ETCS (European Rail Traffic Management System / European Train Control System) defines functional requirements for a standardized train control system across Europe. Its primary goal is to provide drivers with information to drive trains safely and supervise train and shunting movements, supporting interoperability and safety up to 500 km/h. The specification covers operational, infrastructure, and trainborne functions across multiple application levels.

## Stakeholders and User Stories
*   **Driver**: Operates the train using the ETCS interface for safe movement and supervision.
*   **Railway Infrastructure Manager**: Maintains trackside equipment (e.g., RBC, balises) and provides movement authorities and track data.
*   **Train Operator/Manager**: Ensures trains are equipped with compliant ETCS onboard systems and manages train data.
*   **Maintenance Personnel**: Performs upkeep and troubleshooting of onboard and trackside ETCS components.
*   **Safety Regulator**: Oversees system compliance with mandatory safety and interoperability requirements.
*   **System Integrator/Supplier**: Develops and implements ETCS components according to the specification.

**User Stories:**
1.  As a **Driver**, I want to enter train data before departure so that the ETCS can correctly supervise the journey.
2.  As a **Driver**, I want clear visual and acoustic warnings before a brake intervention so that I can react and maintain control.
3.  As an **Infrastructure Manager**, I want to send movement authorities and track descriptions to trains via radio or balises so that I can control traffic flow and ensure separation.
4.  As a **Train Operator**, I want the onboard system to record all operational data so that driver performance and incidents can be investigated.
5.  As a **Maintenance Technician**, I want the onboard equipment to perform an automatic self-test at startup so that I can quickly verify system health.
6.  As a **Safety Regulator**, I require defined failure modes (e.g., emergency brake on transmission loss) so that system safety is maintained under all conditions.

## Key Processes
1.  **System Start & Self-Test (Trigger: Power-on)**: Onboard equipment performs an automatic self-test at startup, indicating the result to the driver.
2.  **Train Data Entry (Trigger: Driver selection or system request)**: Driver enters or confirms train data (e.g., speed, length, brake parameters) before movement is permitted.
3.  **Movement Authority Reception & Supervision (Trigger: Receipt of trackside data)**: Onboard system receives movement authorities and track data, calculates static/dynamic speed profiles, and supervises the train's speed and distance to the authority's end.
4.  **Operational State Management (Trigger: Trackside command, driver action, or system condition)**: System manages transitions between states like Full Supervision, Shunting, or On Sight operation, often requiring driver acknowledgement.
5.  **Brake Intervention (Trigger: Speed limit violation, passed stop signal, or emergency command)**: System applies service or emergency brakes if supervision limits are breached or upon specific safety commands.
6.  **Data Recording (Trigger: Continuous operation)**: Onboard system records all entered, received, and indicated data linked to time and location for investigation.
7.  **Failure Handling (Trigger: Equipment or transmission failure)**: System executes predefined reactions (e.g., brake application, restricted operation) based on national values and indicates the failure to the driver.

## Domain Data Elements
*   **Train**
    *   *Primary Key:* Train Identification (Train Number)
    *   *Key Fields:* Maximum Speed, Train Length, Brake Parameters, Gauge, Axle Load
*   **Movement Authority (MA)**
    *   *Primary Key:* MA Identifier / Reference
    *   *Key Fields:* End Location, Route Information, Associated Speed Profiles, Time-out Values
*   **Driver**
    *   *Primary Key:* Driver Identification
    *   *Key Fields:* Selected Language, Current Operational Status
*   **Track Segment / Infrastructure**
    *   *Primary Key:* Location Reference (e.g., balise group ID)
    *   *Key Fields:* Static Speed Profile, Gradient, Adhesion Conditions, National Values
*   **Radio Block Centre (RBC)**
    *   *Primary Key:* RBC ID
    *   *Key Fields:* Controlled Area, Handover Parameters, Communication Status
*   **Event Log / Journal**
    *   *Primary Key:* Timestamp & Location
    *   *Key Fields:* Event Type (e.g., brake intervention, state transition), Speed, System Messages

## Non-Functional Requirements
1.  **Safety & Reliability**: The system must be fail-safe, with failures leading to a restrictive state (e.g., brake application).
2.  **Interoperability**: ETCS must be compatible with existing national systems (via STMs) and allow trains equipped for higher levels to run on lines with lower levels.
3.  **Performance**: Must be functional for train speeds up to 500 km/h.
4.  **Availability**: System design must consider RAMS (Reliability, Availability, Maintainability, Safety) principles, though specifics are detailed elsewhere.
5.  **Usability**: The Driver-Machine Interface (DMI) must present information understandably, support multiple languages, and provide timely warnings.
6.  **Data Integrity**: Recorded data must be accurate, time-synchronized (UTC), and retained for specified periods (e.g., 24 hours for accident data).

## Milestones and External Dependencies
1.  Finalization and official release of FRS version 5.00 (21 June 2007).
2.  Development and deployment of the detailed System Requirements Specification (SRS) based on this FRS.
3.  Harmonization of national values and default values across participating railways.
4.  Availability of Specific Transmission Modules (STMs) for compatibility with legacy national systems.
5.  Implementation of trackside infrastructure (RBCs, balises) and onboard equipment across the European rail network.

## Risks and Mitigation Strategies
1.  **Risk**: Failure in continuous transmission (e.g., radio loss) leading to loss of supervision.
    *   **Mitigation**: Define national fall-back procedures (e.g., immediate brake, continue to end of MA) to ensure safety.
2.  **Risk**: Incorrect train data entry compromising braking curve calculations.
    *   **Mitigation**: Validate data where possible, use confirmed default values, and record all entries for audit.
3.  **Risk**: Seamless handover failure between Radio Block Centres (RBCs).
    *   **Mitigation**: Define robust handover protocols; allow performance penalty for single-radio units but maintain safety.
4.  **Risk**: Driver non-response to required acknowledgements (e.g., during state transition).
    *   **Mitigation**: Initiate brake application after a timeout to enforce a safe state.
5.  **Risk**: Odometry errors causing inaccurate train location.
    *   **Mitigation**: Use balises as reference points for location correction and account for error in supervision calculations.

## Undecided Issues
1.  Specific implementation details for the Driver-Machine Interface (DMI) are not defined in this document.
2.  Detailed training requirements for drivers and maintenance staff are not specified.
3.  Exact environmental specifications (temperature, vibration, etc.) for equipment are not provided.
4.  Comprehensive RAMS (Reliability, Availability, Maintainability, Safety) targets and analysis methods are deferred.
5.  The selection of which Optional (O) functions are required in specific national or TSI (Technical Specification for Interoperability) contexts is not finalized.
6.  Detailed protocols for "Other technical functions" are not covered in this version.