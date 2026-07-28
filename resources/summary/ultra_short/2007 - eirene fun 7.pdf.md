**Purpose & Scope**
The system is a digital radio communications standard (EIRENE) for European railways, based on GSM. Its primary purpose is to ensure interoperability for trains and staff crossing national borders, particularly on high-speed international lines. It provides ground-to-train and ground-to-ground voice and data communications for operational and support staff. The specification defines requirements for the network infrastructure and mobile terminals but excludes the detailed design of controller equipment and national numbering plans.

**Product Background / Positioning**
EIRENE is intended to replace existing national railway radio systems to create a unified European standard. It is part of the Technical Specification for Interoperability. The system interfaces with existing railway fixed networks, public operator networks, and specialised systems like the ERTMS/ETCS train control system. An EIRENE network is a GSM-based railway telecommunications network that complies with this specification.

**Core Functional Overview**
1.  Voice Services: Point-to-point, broadcast (one-way to a group), group (talk/listen within a group), and multi-party (up to six parties) calls.
2.  Railway Emergency Calls: High-priority voice calls to stop all railway movements in a defined area, with distinct "Train" and "Shunting" types.
3.  Functional & Location-Dependent Addressing: Call users by their role (e.g., "driver of train X") or call a function (e.g., controller) based on the caller's current location.
4.  Shunting Mode: A dedicated group call mode for shunting operations, featuring a link assurance signal (an audible tone) to confirm radio link integrity.
5.  Direct Mode: Fall-back, direct radio-to-radio communication without network infrastructure.
6.  Data Bearer Services: Support for general data applications and, where implemented, text messaging, fax, and safety-critical data for ERTMS/ETCS train control.
7.  Call Management: Includes multi-level priority/pre-emption, closed user groups, call forwarding, hold, waiting, and barring.

**Key Users & Usage Scenarios**
*   **Driver (Cab Radio User)**: Primary user in the locomotive cab. Scenarios: calling the primary controller, making/receiving railway emergency calls, communicating with other drivers in the area or on the same train, and entering shunting mode.
*   **Operational Staff (Operational Radio User)**: Trackside workers, shunting teams, maintenance personnel. Scenarios: participating in shunting group calls, sending emergency calls, communicating with controllers.
*   **General Staff (General Purpose Radio User)**: Administrative, station, and depot personnel for support communications.
*   **Controller (Fixed Terminal User)**: Manages train movements. Scenarios: receiving driver calls, initiating group/emergency calls, managing call queues with priority display.
Permissions differ: e.g., only drivers and authorised operational staff can initiate railway emergency calls; shunting group membership is controlled.

**Major External Interfaces**
*   Interface to private railway fixed networks.
*   Interface to public telephone operator networks.
*   Interface to controller equipment (specification is network-side only).
*   Interface to specialised railway systems (e.g., ERTMS/ETCS Radio Block Centre, balise readers for location).
*   Data interfaces on mobiles for external applications (e.g., train-borne recorder, driver safety device).

**Key Non-functional Requirements**
*   **Performance & Coverage**: Supports mobile speeds up to 500 km/h. Call setup times: Railway emergency call <2 seconds, group call between drivers <5 seconds (required for 95% of cases). Coverage target: 95% of time over 95% of area for vehicle-mounted radios.
*   **Reliability & Availability**: Network and mobile equipment must meet defined reliability, availability, and maintainability (RAM) requirements.
*   **Safety & Priority**: A five-level priority scheme (Railway Emergency highest) with mandatory pre-emption of lower priority calls.
*   **Environmental**: Equipment must withstand railway operational environments (climatic, physical shock, vibration, EMC) as specified for each radio type (Cab, Operational, General Purpose).
*   **Interoperability**: Mobiles must function on any EIRENE-compliant network and in public GSM networks within allocated bands.

**Constraints, Assumptions & Dependencies**
*   **Constraints**: Must comply with relevant CENELEC and ISO 9001 standards. National implementations can adopt stricter environmental standards but must not prevent interoperability.
*   **Assumptions**: The system is based on the ETSI GSM standard. National railways will determine the specific languages supported and the detailed responsibilities of controller types.
*   **Dependencies**: Successful cross-border operation depends on bilateral agreements between network operators for interconnection and area definition for group/broadcast calls. Support for ERTMS/ETCS is dependent on that system's implementation.

**Priorities & Acceptance Approach**
*   **Priorities**: Requirements are categorised as Mandatory (for interoperability), Optional, or Informative. The five call priority levels (Railway Emergency, Control-command, Public Emergency/Driver Group, Railway Operation, Railway Information) define the pre-emption hierarchy.
*   **Acceptance Approach**: Compliance with mandatory requirements is necessary for interoperability on designated lines. Performance criteria (e.g., call setup times) have defined success rates (95%) and limits for 99% of cases. Functional acceptance would involve verifying core services (voice, emergency calls, addressing) and performance under specified environmental conditions.