# Detailed Summary: EIRENE Functional Requirements Specification

## Background and Scope
This document defines the functional requirements for the European Integrated Railway Radio Enhanced Network (EIRENE), a GSM-based digital radio system for European railways. It aims to ensure interoperability for trains and staff crossing national borders and to provide manufacturing economies of scale. The specification covers ground-train voice/data communications and ground-based mobile communications for trackside workers, station staff, and administrative personnel. Non-goals include detailed implementation specifications and non-railway public emergency services.

## Stakeholders Matrix and Use Cases
*   **Train Driver:** Uses the Cab Radio for operational communications, emergency calls, and train control data. Main scenario: Initiates a call to the primary controller. Exception: Sends a Railway Emergency Call.
*   **Primary Controller:** Coordinates train movements and manages emergency calls within a designated track area. Main scenario: Receives and manages a Railway Emergency Call from a driver.
*   **Secondary Controller:** Responsible for safe train running on a designated area of track. Main scenario: Communicates with a driver regarding signalling.
*   **Power Supply Controller:** Manages the traction power supply. Main scenario: Receives a call from a driver regarding power issues.
*   **Shunting Team Member:** Uses an Operational Radio for shunting operations. Main scenario: Participates in a shunting group call with link assurance signal.
*   **Trackside Worker / General Staff:** Uses General Purpose or Operational Radios for maintenance and support communications. Main scenario: Makes a point-to-point call to a colleague.
*   **Chief Conductor / On-Train Staff:** Responsible for passenger activities; can be contacted via the Cab Radio system. Main scenario: Receives a call from the driver.
*   **Network Operator / Railway Administration:** Manages subscriber profiles, network configuration, and numbering plans. Main scenario: Configures a new functional number for a train.

## Business Process
**Main Process: Driver Initiates a Call to Controller**
1.  **Trigger:** Driver presses dedicated button to call primary controller.
2.  **Input:** Cab Radio determines destination using location-dependent addressing.
3.  **Process:** System establishes a point-to-point call with railway operation priority.
4.  **Output:** Call is connected to controller's terminal; functional identities are exchanged and displayed.
5.  **Process:** Parties communicate via loudspeaker/handset.
6.  **Branch A (Call Successful):** Driver or controller terminates the call.
7.  **Branch B (Call Failed):** System provides audible/visual failure indication to driver.
8.  **Output:** Call is cleared; resources are released.

**Key Branch 1: Initiate Railway Emergency Call**
1.  **Trigger:** User presses red emergency button on Cab or Operational Radio.
2.  **Process:** System establishes a high-priority group/broadcast call to predefined users in the area.
3.  **Output:** A 5-second warning tone is played to all recipients.
4.  **Process:** Speech path is opened for the originator to provide information.

**Key Branch 2: Enter Shunting Mode**
1.  **Trigger:** Shunting team leader initiates a shunting group call.
2.  **Process:** Designated team members join the group call.
3.  **Input:** A team member activates the link assurance signal.
4.  **Output:** An intermittent tone is heard by all group members, confirming link integrity.

## Domain Model
*   **Subscriber:** Represents a user of the EIRENE system. Fields: Subscriber ID (Unique), Functional Numbers (Reference to FunctionalNumber, up to 3), Priority Level (Required), Group Memberships (Reference to CallGroup).
*   **Mobile Equipment:** Base entity for radio terminals. Fields: Equipment ID (Unique), Type (Cab/General/Operational, Required), Telephone Number (Unique), Current Network (Reference to Network).
*   **Cab Radio:** A type of Mobile Equipment installed in a locomotive cab. Inherits Mobile Equipment fields. Additional Fields: Associated Train Number, Associated Engine/Stock Number.
*   **Call:** Represents a communication instance. Fields: Call ID (Unique), Type (Point-to-point/Group/Broadcast, Required), Priority (Required), Participants (Reference to Subscriber), Start/End Time.
*   **FunctionalNumber:** A number representing a user's role. Fields: Functional Number (Unique, Numeric), Associated Telephone Number (Reference to Subscriber, Required), Description/Alphanumeric ID.
*   **CallGroup:** A predefined set of subscribers for group calls. Fields: Group ID (Unique), Geographic Area, Member List (Reference to Subscriber).
*   **Controller:** A type of Subscriber with a control function. Inherits Subscriber fields. Additional Fields: Controller Type (Primary/Secondary/Power), Control Area.
*   **Network:** Represents a GSM-R or public mobile network. Fields: Network ID (Unique), Type (EIRENE/Public), Authorized Status.

## Interfaces and Integrations
*   **ERTMS/ETCS (Train Control):** Direction: Bi-directional. Theme: Safety-critical data bearer service. Input: Train control messages from Radio Block Centre (RBC). Output: Messages to on-train ETCS equipment. SLA: Must support data communications for Level 2/3; priority scheme applies.
*   **Train-Borne Recorder:** Direction: From Cab Radio. Theme: Logging of safety-critical events. Input: Activation/termination of emergency calls, driver safety device alarms, radio faults. Output: Data for post-incident analysis. SLA: Event transmission as each event occurs.
*   **Driver Safety Device (DSD):** Direction: From DSD to Cab Radio. Theme: Transmission of driver alertness alarms. Input: DSD activation signal. Output: Data message to primary controller containing train number, location. SLA: Automatic triggering upon DSD activation.
*   **External Networks (Public/PSTN):** Direction: Bi-directional. Theme: Interconnection for external calls. Input: Calls from public networks to EIRENE subscribers. Output: Calls from EIRENE to public numbers. SLA: Subject to bilateral agreements; must comply with open specifications.
*   **On-Train Systems (PA, Intercom):** Direction: Bi-directional via Cab Radio. Theme: Integration with internal communications. Input: Calls for on-train staff/devices. Output: Automated call routing to appropriate internal system. SLA: Calls possible even if driver MMI is off.
*   **Balise / External Location System:** Direction: Input to Cab Radio. Theme: Directed network selection at borders. Input: Location/network identity data. Output: Triggers network change. SLA: Defers change if voice calls are ongoing.
*   **Controller Terminal Equipment:** Direction: Bi-directional. Theme: Interface for controller workstations. Input: Call requests, functional identities. Output: Call queue display, control functions. SLA: Architecture defined by railway operator.
*   **Text Message Application:** Direction: Bi-directional via data interface. Theme: Bearer service for text messages. Input: Application-layer messages. Output: Delivered messages via radio bearer. SLA: Must not interfere with high-priority voice/data calls.

## Acceptance Criteria
**Capability: Railway Emergency Call**
*   Given a driver presses the red emergency button, when the system initiates the call, then a warning tone must be heard by all target users within 2 seconds, and a continuous visual indication must be displayed.
*   Given a Railway Emergency Call is active, when a train enters the affected area, then the same audible and visual warning indications must be provided to that driver.

**Capability: Functional Addressing**
*   Given a controller dials a train's functional number, when the call is established, then the driver's Cab Radio must display the controller's functional identity, and the controller's terminal must display the train number.
*   Given a driver registers a train number, when another driver attempts to register the same number, then the new driver must be warned and allowed to override, and the original driver must be notified.

**Capability: Shunting Mode with Link Assurance**
*   Given a shunting group call is active, when a team member activates the link assurance signal, then an intermittent 800-850Hz tone must be heard by all group members, and only the signal originator can speak.
*   Given the link assurance signal is active, when any member initiates a Shunting Emergency Call, then the link assurance signal must be deactivated and the emergency call must take priority.

## Non-Functional Metrics
*   **Performance:** Call setup time for Railway Emergency calls <2s (95% of cases). Network coverage of 95% area for 95% time for vehicle-mounted radios. Support for speeds up to 500 km/h.
*   **Reliability/Availability:** Mobile equipment must operate under defined climatic, physical, and mechanical stress (shock, vibration, contaminants). Battery life for handhelds: minimum 8 hours under defined usage cycle.
*   **Security:** Closed User Group (CUG) to limit network access. Call barring and restriction features to control calling capabilities. Protection against unauthorized functional number registration.
*   **Compliance:** Design and testing shall comply with ISO 9001. Must adhere to relevant European Norms for EMC and physical hazards. National standards can be stricter if they don't prevent interoperability.
*   **Observability:** Cab Radio must provide audible/visual indications for call status, network availability, and failures. Events (emergency calls, DSD alarms, faults) must be recordable on train-borne recorder.

## Milestones and Release Strategy
1.  Finalize and approve core functional requirements specification (Document Version 7.0).
2.  Develop and approve companion System Requirements Specification (SRS).
3.  Procure and develop network infrastructure compliant with FRS/SRS.
4.  Develop and certify the three mobile equipment types (Cab, General Purpose, Operational).
5.  Conduct field trials, particularly for emergency call timing and link assurance signal.
6.  Deploy EIRENE networks on international corridors, ensuring bilateral agreements for border areas.

## Risk List and Mitigation Strategies
1.  **Risk:** Interoperability failure at national borders due to network or configuration differences.
    *   **Mitigation:** Mandate standard numbering plans, priority levels, and group call definitions. Require bilateral agreements between network operators.
2.  **Risk:** Emergency call pre-emption not supported on public GSM networks used for roaming.
    *   **Mitigation:** Define fallback behavior in specification. Rely on special agreements with public operators where critical.
3.  **Risk:** Ambiguity or conflict in functional number registration (e.g., duplicate train numbers).
    *   **Mitigation:** Implement system-level checks to prevent duplicates. Define clear override procedures and user notifications.
4.  **Risk:** Safety compromise if shunting communications are interrupted or insecure.
    *   **Mitigation:** Define protected shunting groups, link assurance signal, and clear rules for external call intrusion.
5.  **Risk:** EMC interference from Cab Radio with sensitive train control systems.
    *   **Mitigation:** Specify stringent EMC requirements for Cab Radio beyond general mobile equipment. National railways responsible for validation.
6.  **Risk:** Inconsistent user experience and training due to national variations in MMI.
    *   **Mitigation:** Define core mandatory MMI requirements (colors, indications, emergency button). Allow national customization only where not conflicting.
7.  **Risk:** System cannot handle high density of trains requiring simultaneous data for ERTMS.
    *   **Mitigation:** Reference separate ERTMS communication requirements document. Ensure network dimensioning considers this use case.
8.  **Risk:** Loss of location-dependent addressing accuracy impacting controller call routing.
    *   **Mitigation:** Use network cell location as minimum. Define optional interface for external, more accurate location sources (balise, GPS).

## Undecided Issues and Responsible Parties
1.  **Automatic joining of group calls for entering mobiles (Req 3.5.7-8):** Requires further technical specification changes. *Responsible: EIRENE Technical Working Group.*
2.  **Precise duration of emergency call warning tone:** 5 seconds suggested but "to be confirmed by trials". *Responsible: Testing and Validation Team.*
3.  **Definition of different service classes for low/medium traffic rural areas:** To be determined on a national basis. *Responsible: National Railway Authorities.*
4.  **Specific languages to be supported on MMI:** A national decision, but at least 10 languages must be supported. *Responsible: National Railway Authorities.*
5.  **Time `t` for MMI configuration persistence after power-off (0-240 min):** Configurable as a maintenance function. *Responsible: System Maintainers / National Railway.*
6.  **Implementation of automatic vs. directed network selection for border crossing:** Directed is suitable; automatic is not. Choice may be national. *Responsible: National Railway Authorities.*
7.  **Format for alphanumeric train numbers used nationally:** National railways responsible for translation to numeric functional numbers. *Responsible: National Railway Authorities.*
8.  **Detailed specification of controller terminal interface:** Beyond EIRENE scope; defined by railway operator. *Responsible: Individual Railway Operators.*