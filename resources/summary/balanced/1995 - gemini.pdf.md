# Balanced Summary: Gemini 8-m Telescopes Control System Software Requirements

## Goals and Scope
The Software Requirements Specification (SRS) establishes the operational requirements for the Gemini Control System software, guiding the development of controls and data acquisition systems. Its primary goal is to enable the efficient acquisition of astronomical data through automated, reliable, and user-friendly software. The document is oriented toward software developers, not end-user astronomers, and follows from higher-level operational concepts.

## Stakeholders and User Stories
*   **Astronomer:** The end-user/customer who has developed a science plan for data collection, ranging from novice to expert.
*   **Science Observer:** The on-site person responsible for monitoring data acquisition and validating data integrity for the astronomer.
*   **Telescope Operator:** The on-site controller responsible for the integrity and accurate functioning of the telescope and instruments during observations.
*   **Support Personnel:** On-site or near-site personnel responsible for hardware and software maintenance, installation, and configuration changes.
*   **Developer:** Personnel responsible for designing, testing, configuring, and upgrading software subsystems.
*   **Administrator:** Personnel responsible for high-level functional control of the integrated Gemini system, including scheduling and system modifications.

**User Stories:**
1.  As an **Astronomer**, I want to interact with an automatic sequencer via a simple, safe interface so that I can concentrate on data acquisition and quality assessment.
2.  As a **Science Observer**, I want to monitor all subsystems and data integrity so that I can ensure the science plan is functioning correctly.
3.  As a **Telescope Operator**, I want direct control of the telescope and instruments with a quick-response interface so that I can ensure system safety and performance.
4.  As **Support Personnel**, I want full access to all subsystems for testing and maintenance so that I can perform repairs and diagnostics without interfering with operations.
5.  As a **Developer**, I want to use standardized development environments and interfaces so that I can create modular, maintainable software components.
6.  As an **Administrator**, I want to inquire about system utilization and scheduling so that I can make informed decisions about maintenance and observation changes.

## Key Processes
1.  **System Start-Up (Trigger: Power-on/Cold Start):** The system boots, performs self-tests, downloads software to IOCs, and initializes all subsystems to a configured state.
2.  **Observation Planning (Trigger: User/Program Request):** An astronomer develops a computer-executable science program, potentially using a telescope simulator for testing.
3.  **Observation Queue Management (Trigger: New Program/Changed Conditions):** The scheduler software sorts and dispatches pre-programmed observing sequences from a queue based on target positions, weather, and instrument configurations.
4.  **Observation Execution (Trigger: Sequencer Dispatch):** The sequencer interprets and sends commands to the Telescope Control Software (TCS) and Instrument Control Software (ICS) to carry out the observing program.
5.  **Data Acquisition & Storage (Trigger: Detector Readout):** Astronomical data is read from detectors, optionally pre-processed, compressed using loss-less techniques, and stored in a standard format (e.g., FITS) with multiple backup copies.
6.  **System Monitoring & Fault Notification (Trigger: Continuous/Event):** All subsystems are continuously monitored; faults are logged and reported with specific origin and problem details to the Observatory Control Software (OCS).
7.  **Error Recovery & Reconﬁguration (Trigger: Subsystem Failure):** Predefined procedures are executed to reconfigure the system to continue observing with remaining equipment, aiming for recovery within 5 minutes.

## Domain Data Elements
*   **Science Program**
    *   *Primary Key:* Program_ID
    *   *Key Fields:* Astronomer_ID, Target_Coordinates, Instrument_Configuration, Exposure_Sequence, Scheduling_Priority
*   **Observation (Exposure)**
    *   *Primary Key:* Exposure_ID
    *   *Key Fields:* Program_ID, Timestamp, Instrument_ID, Detector_Data_Pointer, Header_Metadata (e.g., telescope position, filter)
*   **Subsystem (Telescope/Instrument)**
    *   *Primary Key:* Subsystem_ID
    *   *Key Fields:* Status (e.g., RUNNING, MAINTENANCE), Configuration_Parameters, Version, Operational_Log_Pointer
*   **User Session**
    *   *Primary Key:* Session_ID
    *   *Key Fields:* User_ID, Location, Access_Mode (e.g., OBSERVING, OPERATION), Assigned_Resources
*   **Engineering Data Log**
    *   *Primary Key:* Log_Entry_ID
    *   *Key Fields:* Subsystem_ID, Timestamp, Parameter_Name, Parameter_Value, Data_Type (e.g., status, sensor reading)
*   **Command**
    *   *Primary Key:* Command_ID
    *   *Key Fields:* Source, Target/Channel, Opcode, Parameter_Set, Timestamp

## Non-Functional Requirements
1.  **Performance:** Commands must be accepted/rejected within 2 seconds; status display updates within 4 seconds at local stations.
2.  **Reliability/Availability:** Target total system downtime due to failures is 2% (requirement) with a 1% goal, translating to roughly 15 minutes per night.
3.  **Capacity:** The system must support simultaneous operation of up to six active control nodes and two monitoring nodes without appreciable performance degradation.
4.  **Maintainability:** Software must be modular, table-driven where possible, and include built-in test (BIT) facilities and simulator modules for each subsystem.
5.  **Security:** Access is controlled via an Access Mode Allocation system based on user role, operational level, and location. Intrusion protection for the astronomical database is required.
6.  **Supportability:** A formal supportability plan is required, addressing maintenance levels, personnel skill constraints, and support equipment.

## Milestones and External Dependencies
1.  Initial implementation of the automatic sequencer in a "pass through" mode.
2.  Fulfillment of classical (interactive) observing requirements before implementing service/queue-based observing.
3.  Development and integration of "expert" flexible scheduling software (may be a future phase).
4.  Dependency on the establishment of G8MT standards for online software and the development environment.
5.  Dependency on the definition of a G8MT standard for acquisition and storage of detector data.

## Risks and Mitigation Strategies
1.  **Risk:** Single-point hardware failures causing observation downtime.
    *   **Mitigation:** Implement data redundancy and software retry procedures; design for reconfiguration around failed non-critical subsystems.
2.  **Risk:** Evolution of Gemini software standards breaking compatibility with visitor instruments.
    *   **Mitigation:** Define a stable, long-lived subset of interfaces for visitor instruments; handle additional requirements on a case-by-case basis.
3.  **Risk:** Insufficient network bandwidth impacting transparency of remote operations.
    *   **Mitigation:** Design software to minimize link bandwidth impact; use data compression; accept that perceived transparency will vary with link speed.
4.  **Risk:** High complexity leading to unreliable or unmaintainable software.
    *   **Mitigation:** Enforce modularity, use commercial/off-the-shelf software where feasible, and apply strict configuration control and versioning (CVS).
5.  **Risk:** Failure conditions cascading across subsystems.
    *   **Mitigation:** Design subsystems to be as autonomous as possible; ensure failure of one subsystem does not affect others via communication links or shared resources.

## Undecided Issues
1.  Definition of a G8MT standard for acquisition and storage of detector data.
2.  Choice of link technology to transfer detector data.
3.  Final desirable hardware specification for development and target systems.
4.  G8MT standards for online software and the development environment.
5.  The detailed supportability plan.
6.  Descriptions and software access requirements for star catalogs.