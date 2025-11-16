# Balanced Summary

- **Goals and scope**: The EIRENE system defines functional requirements for a GSM-based digital radio standard to support European railways' mobile communication needs, ensuring interoperability for international trains and manufacturing economies of scale. It covers ground-train voice/data communications and ground-based mobile needs for trackside workers, station staff, and administrative personnel. The specification distinguishes mandatory, optional, and informational requirements to facilitate cross-border operations and consistent service levels.

- **Roles and user stories**:
  - As a **train driver**, I want to initiate Railway emergency calls with a single action so that I can quickly alert controllers and other drivers in emergencies.
  - As a **shunting team member**, I want to use shunting mode with a link assurance signal so that I can maintain communication integrity during critical manoeuvres.
  - As a **controller**, I want to establish group calls with Railway emergency priority so that I can coordinate responses across a predefined geographical area.
  - As a **general staff user**, I want to make point-to-point voice calls to authorised users so that I can perform routine operational and administrative tasks.
  - As an **on-train system (e.g., ERTMS/ETCS)**, I want to use the radio bearer for data communications so that train control applications can function safely and efficiently.

- **Key processes**:
  1. **System initialisation** (trigger: power-on) – Mobile equipment performs self-tests, connects to an authorised network, and registers functional numbers.
  2. **Call initiation** (trigger: user action or system request) – User or system initiates voice/data calls with assigned priority levels, supporting point-to-point, group, or broadcast modes.
  3. **Railway emergency call handling** (trigger: emergency button press) – System establishes high-priority call to predefined recipients, provides warning tones, and enables speech communication.
  4. **Shunting mode operation** (trigger: mode selection) – Establishes group call with link assurance signal for shunting teams, allowing only one member to transmit the signal at a time.
  5. **Location-dependent addressing** (trigger: mobile movement) – Routes calls to controllers based on the mobile's current location, using network-derived or external location data.
  6. **Functional number registration** (trigger: user input or system event) – User registers/deregisters functional numbers (e.g., train number) to enable addressing by role rather than equipment.
  7. **Direct mode fallback** (trigger: loss of network service) – Users switch to direct mode for local communications without network infrastructure when normal services are unavailable.

- **Domain data elements**:
  - **Mobile Equipment** (primary key: Telephone Number) – Functional Identity, Network Selection List, Group Memberships, Battery Status
  - **Functional Number** (primary key: Functional Number) – Train Number, Engine Number, Coach Number, User Role
  - **Call Record** (primary key: Call ID) – Call Type, Priority Level, Timestamp, Participant Identities
  - **Controller** (primary key: Controller ID) – Controller Type, Location, Functional Identity
  - **Shunting Group** (primary key: Group ID) – Shunting Leader, Driver, Team Members, Link Assurance Status
  - **Network Configuration** (primary key: Network ID) – Coverage Area, Call Set-up Time, Broadcast Areas

- **Non-functional requirements**:
  - Call set-up times must be under 2 seconds for Railway emergency calls and under 10 seconds for low-priority calls in 95% of cases.
  - The system must support seamless communications for mobiles travelling at speeds up to 500 km/h.
  - Mobile equipment must withstand railway environmental conditions, including shock, vibration, and electromagnetic compatibility.
  - Battery life for handheld radios must provide at least 8 hours of operation under typical usage cycles.
  - The network must achieve 95% coverage over 95% of the designated area for vehicle-mounted radios.
  - Functional number registration and deregistration must be completed within 30 seconds for up to ten numbers.

- **Milestones and external dependencies**:
  - Approval by GSM-R Operators, Functional, and Industry Groups (achieved 17 May 2006).
  - Implementation of ERTMS/ETCS train control systems requiring EIRENE bearer services.
  - Bilateral agreements for network interconnection and cross-border group call areas.
  - Development of national numbering plans and subscription profiles aligned with EIRENE standards.
  - Integration with external location systems (e.g., balises, GPS) for enhanced location-dependent addressing.

- **Risks and mitigation strategies**:
  - **Risk**: Network failure during critical operations. **Mitigation**: Implement direct mode as a fallback for local communications without infrastructure.
  - **Risk**: Ambiguities in functional addressing (e.g., duplicate train numbers). **Mitigation**: Enforce unique functional number registration and prevent duplicates.
  - **Risk**: Electromagnetic interference with railway signalling systems. **Mitigation**: Adhere to stringent EMC standards and national requirements.
  - **Risk**: Inconsistent service levels across networks. **Mitigation**: Harmonise subscription details and priorities internationally.
  - **Risk**: Unauthorised access to shunting or emergency features. **Mitigation**: Use access control and physical protection measures.

- **Undecided issues**:
  - Standardisation of pre-defined text messaging applications (left to national railways).
  - Specific languages to be supported beyond the minimum requirement of ten.
  - National variations in environmental requirements that must not prevent interoperability.
  - Optional features like automatic fax and direct mode implementation.
  - Methods for handling alphanumeric train numbers in non-interoperable cases.
  - Not mentioned.