**Purpose & Scope**
The system is a digital radio standard for European railways, ensuring interoperability for trains and staff crossing national borders. It provides ground-train voice/data communications and ground-based mobile communications for trackside workers, station staff, and administrative personnel. It does not specify requirements for the fixed network infrastructure or controller equipment beyond defined interfaces.

**Product Background / Positioning**
The system, named EIRENE (European Integrated Railway Radio Enhanced Network), is based on the GSM standard with railway-specific enhancements. It is intended to replace existing national railway radio systems to create a unified, interoperable communications platform across Europe. It also provides the radio bearer for the ERTMS/ETCS train control system.

**Core Functional Overview**
1.  Railway-specific voice group and broadcast calls (VGCS/VBS) for operational communications.
2.  Functional addressing, allowing calls to users (e.g., drivers) by a role/number (e.g., train number) rather than a personal device number.
3.  Location-dependent addressing, automatically routing calls from a train to the appropriate controller based on its location.
4.  Railway emergency calls (train and shunting emergencies) as high-priority group calls.
5.  Shunting mode operations, providing dedicated group communications for shunting teams.
6.  Direct mode operation for set-to-set communications without network infrastructure.
7.  Support for GSM telephony, SMS, and data services (including for ERTMS/ETCS).

**Key Users & Usage Scenarios**
*   **Train Drivers (Cab Radio Users):** Primary users for safety and operational calls. They initiate calls to controllers, other drivers, and send emergency alerts. They register their functional number (train number) at the start of a journey.
*   **Controllers/Dispatchers (Fixed Network Users):** Manage train movements. They receive location-dependent calls from drivers and can initiate group broadcasts.
*   **Trackside Staff (Operational Radio Users):** Includes shunting teams and maintenance workers. They use group calls for coordinated activities and have a dedicated shunting mode.
*   **General Railway Staff (General Purpose Radio Users):** Use standard telephony and group call features for administrative and support communications.
*   **ERTMS/ETCS System:** A non-human user that uses the system's data bearer services for train control information.

**Major External Interfaces**
*   **Air Interface (Um):** Standard GSM radio interface to mobile equipment.
*   **ERTMS/ETCS Interface:** A specified data interface (EURORADIO FFFIS) for train control systems.
*   **Public Fixed Networks:** Interfaces to national public telephone networks (PSTN/ISDN).
*   **Private Railway Fixed Networks:** Interfaces to existing railway telecommunication networks.
*   **On-Train Systems (via Cab Radio):** Potential interfaces for public address, intercom, driver safety devices, and train-borne recorders (nationally determined or via a Train Interface Unit).

**Key Non-functional Requirements**
*   **Coverage:** 95% probability of a minimum field strength (e.g., -98 dBm for voice, -95 dBm for ETCS on lines ≤220 km/h) along train routes.
*   **Call Setup Time:** Dependent on eMLPP priority level. Must be achieved with authentication and ciphering enabled.
*   **Handover Success Rate:** At least 99.5% under design load conditions.
*   **Frequency Band:** Operation in the Railway-GSM (R-GSM) band (876-915 MHz uplink / 921-960 MHz downlink), with a designated UIC band subset (876-880 / 921-925 MHz).
*   **Reliability/Availability:** Mobile equipment must automatically retry a failed Railway emergency call setup for up to 30 seconds.
*   **Environmental (Mobile Equipment):** Must operate from -20°C to +55°C (Cab radio: -20°C to +70°C), withstand vibration/shock per railway standards, and comply with railway EMC/electrical safety standards.

**Constraints, Assumptions & Dependencies**
*   **Constraint:** The system must be backwards-compatible with the listed versions of GSM specifications.
*   **Constraint:** All mandatory requirements must be met for interoperability; optional features, if implemented, must follow the specified standard.
*   **Dependency:** Relies on GSM network infrastructure (BSS, NSS, GPRS) and standard GSM services.
*   **Dependency:** National railways must obtain public MSISDN number allocations from regulatory bodies.
*   **Assumption:** Location information for location-dependent addressing is primarily derived from the GSM cell ID.

**Priorities & Acceptance Approach**
*   **Priority Levels:** Five eMLPP levels are mandated, mapped to railway priorities: Level 0 (Railway emergency), Level 2 (Public emergency/Driver group calls), Level 3 (Railway operation), Level 4 (Railway information/all other calls). Higher priorities can pre-empt lower ones.
*   **Acceptance:** Compliance with all mandatory ("(M)") requirements in this SRS is required for interoperability. Conformance to referenced GSM and railway standards (e.g., ETSI EN 301 515, environmental specs) is mandatory.