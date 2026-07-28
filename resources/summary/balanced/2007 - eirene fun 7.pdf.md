# Balanced Summary: EIRENE Functional Requirements Specification

## Goals and Scope
The EIRENE specification defines functional requirements for a digital radio system to meet European railways' mobile communication needs, ensuring interoperability along international lines and manufacturing economies of scale. It encompasses ground-train voice/data communications and ground-based mobile communications for trackside workers, station staff, and administrative personnel. The primary objective is to provide a consistent standard for high-speed international routes while also serving as a basis for replacing national radio systems.

## Stakeholders and User Stories
- **Railway Driver**: Uses the Cab radio for operational communications and safety-critical functions.
- **Controller (Primary/Secondary)**: Manages train operations and coordinates emergency communications.
- **Trackside Worker**: Uses Operational or General Purpose radios for maintenance and shunting activities.
- **On-Train Staff (e.g., Conductor)**: Requires communication with the driver and external parties.
- **Network Operator**: Maintains the EIRENE network infrastructure and ensures service availability.
- **System Manufacturer**: Develops compliant mobile and network equipment.

**User Stories:**
1. As a driver, I want to initiate a railway emergency call with a single button press so that I can quickly alert all relevant personnel in an emergency.
2. As a controller, I want to establish group calls to all drivers in a specific area so that I can broadcast important operational information.
3. As a shunting team member, I want to use a link assurance signal during shunting operations so that the driver knows the communication link is intact.
4. As a trackside worker, I want to use direct mode communications when network coverage is unavailable so that I can maintain local communications.
5. As a network operator, I want to manage subscriber priorities and group memberships so that I can ensure high-priority calls are handled appropriately.
6. As a train driver crossing borders, I want the radio to automatically select the correct network so that I maintain seamless communications.

## Key Processes
1. **Call Initiation**: Triggered by user action (e.g., button press, dialing) to establish voice or data calls.
2. **Priority Handling**: Triggered by call setup; higher-priority calls pre-empt lower-priority ones.
3. **Functional Number Registration**: Triggered when a user starts a functional role (e.g., driver registers train number).
4. **Railway Emergency Call Management**: Triggered by emergency button; includes warning tone, speech phase, and termination.
5. **Shunting Mode Operation**: Triggered by entering shunting mode; enables group call with link assurance signal.
6. **Network Selection**: Triggered at power-up or when crossing borders; mobile attaches to authorized network.
7. **Text Message Transfer**: Triggered by application; messages sent via bearer service without interfering with voice calls.

## Domain Data Elements
- **Subscriber**: Primary Key: Telephone Number; Fields: Functional Number(s), Priority Level, Group Memberships, Access Restrictions.
- **Train**: Primary Key: Train Number; Fields: Engine Number, Leading Cab Coach Number, Registered Driver ID.
- **Shunting Group**: Primary Key: Group ID; Fields: Service Area ID, Team Members, Link Assurance Status.
- **Controller**: Primary Key: Controller ID; Fields: Location, Controller Type (Primary/Secondary/Power), Functional Number.
- **Emergency Call Record**: Primary Key: Call ID; Fields: Originator Functional Number, Time Established, Time Cleared, Recipient List.
- **Network**: Primary Key: Network ID; Fields: Network Type (EIRENE/Public), Priority Order, Coverage Areas.

## Non-Functional Requirements
1. Call setup times: Railway emergency calls <2s, group calls between drivers <5s (95% of cases).
2. Network coverage: At least 95% of time over 95% of designated area for vehicle-mounted radios.
3. Mobile operation: Support speeds up to 500 km/h with seamless communications.
4. Environmental resilience: Equipment must withstand railway climatic, physical, and EMC conditions.
5. Battery life: Minimum 8 hours for handheld radios under typical usage cycles.
6. Text message performance: Transfer time <30 seconds per segment for 95% of messages.

## Milestones and External Dependencies
1. Implementation of mandatory features in all EIRENE networks for interoperability.
2. Bilateral agreements for network interconnection at borders.
3. Integration with ERTMS/ETCS for train control applications (where implemented).
4. Development of standardized interfaces for external applications (e.g., driver safety device).
5. National decisions on optional features (e.g., text messaging, automatic fax).

## Risks and Mitigation Strategies
1. **Interoperability failures at borders**: Mitigation: Strict adherence to mandatory requirements and standardized numbering plans.
2. **Network coverage gaps**: Mitigation: Network planning to meet 95%/95% coverage criteria and fallback to direct mode.
3. **Priority call conflicts**: Mitigation: Clear pre-emption rules and network management of priority levels.
4. **Functional number duplication**: Mitigation: Registration procedures that prevent duplicate assignments.
5. **Equipment environmental failures**: Mitigation: Compliance with specified climatic, mechanical, and EMC requirements.

## Undecided Issues
1. Implementation of automatic network selection for border crossing (directed vs. manual).
2. Standardization of alphanumeric train number support for interoperability.
3. Specific call setup time for 99% of cases (only defined as ≤1.5× the 95% requirement).
4. National variations in controller responsibilities (Primary vs. Secondary).
5. Optional feature implementation (e.g., text messaging, direct mode) leading to service inconsistencies.
6. Methods for providing greater location accuracy for location-dependent addressing (e.g., GPS integration).