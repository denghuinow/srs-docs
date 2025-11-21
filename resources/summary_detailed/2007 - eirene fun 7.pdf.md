# Detailed Summary

## Background and Scope
- The EIRENE Functional Requirements Specification defines requirements for a GSM-based digital radio system to meet European railways' mobile communication needs, supporting interoperability across national borders.
- It covers ground-train voice/data communications and ground-based mobile communications for trackside workers, station staff, and administrative personnel.
- Non-goals include detailed implementation of field-level components and standardization of pre-defined messaging applications.

## Role Matrix and Use Cases
**Roles:** Driver (Cab Radio User), General Purpose Radio User, Operational Radio User, Primary Controller, Secondary Controller, Power Supply Controller  
**Main Scenarios:**  
- Driver initiates Railway Emergency Call  
- Controller establishes group call to drivers in an area  
- User registers/deregisters functional number  
- Shunting team establishes link assurance signal  
**Exception Scenarios:**  
- Network connection failure during emergency call  
- Duplicate functional number registration attempt  
- Mobile moves out of group call area during communication

## Business Process
**Main Process - Railway Emergency Call (8 steps):**  
1. User presses emergency button (Trigger: emergency situation)  
2. System establishes high-priority connection to predefined recipients  
3. 5-second warning tone played to all parties  
4. Speech connection established for emergency information  
5. Continuous visual indication maintained  
6. Call continues until termination by authorized party  
7. Automatic confirmation message generated  
8. Confirmation transmitted to ground-based system  
**Key Branch - Call Setup Failure (4 steps):**  
1. System retries connection for 30 seconds  
2. User receives ongoing attempt indication  
3. If unsuccessful after 30s, failure indication provided  
4. User may attempt alternative communication method

## Domain Model
**Entities:**  
- Mobile Equipment (required fields: equipmentID/unique, type, networkStatus)  
- User (required fields: userID/unique, role, functionalNumbers)  
- Functional Number (required fields: number/unique, type, assignedUser/reference)  
- Call (required fields: callID/unique, priority, participants, status)  
- Controller (required fields: controllerID/unique, type, controlArea)  
- Train (required fields: trainNumber/unique, engineNumber, location)  
- Shunting Group (required fields: groupID/unique, members, status)  
- Emergency Call Record (required fields: recordID/unique, timestamp, originator, recipients)

## Interfaces and Integrations
- **ERTMS/ETCS System** (Direction: Bidirectional; Theme: Train control data exchange; Input: Location data, train control messages; Output: Safety-critical data; SLA: High reliability for safety messages)
- **Public Telephone Networks** (Direction: Inbound; Theme: External call routing; Input: Standard telephone numbers; Output: Routed calls to EIRENE users; SLA: Standard telephony reliability)
- **Train-borne Recorder** (Direction: Outbound; Theme: Event logging; Input: Emergency call events, system faults; Output: Recorded event data; SLA: Non-interference with primary functions)
- **Driver Safety Device** (Direction: Inbound; Theme: Driver alertness monitoring; Input: DSD activation signals; Output: Alarm messages to controllers; SLA: Immediate transmission on activation)

## Acceptance Criteria
**Given** a driver has pressed the emergency call button **When** the system establishes the connection **Then** all designated recipients receive warning tone within 2 seconds  
**Given** a train is moving between network coverage areas **When** the train enters a new emergency call area **Then** the cab radio automatically joins any ongoing emergency call with appropriate indications

## Non-functional Metrics
- **Performance:** Call setup times ≤2s for emergency calls (95% cases), support for speeds up to 500 km/h  
- **Reliability:** 95% coverage over designated area, 99% confirmation message delivery within 5 minutes  
- **Security:** Closed user group enforcement, call restriction capabilities  
- **Compliance:** ISO 9001 quality procedures, CENELEC standards for driver-machine interface  
- **Observability:** System diagnostics, event logging to train-borne recorder

## Milestones and Release Strategy
1. Core voice services implementation  
2. Emergency call functionality deployment  
3. Data services integration  
4. Cross-border interoperability testing  
5. Shunting mode implementation  
6. Full EIRENE compliance certification

## Risk List and Mitigation Strategies
- Network failure during critical operations: Direct mode fallback capability  
- Duplicate functional number assignment: Registration validation procedures  
- Radio interference with train systems: EMC compliance testing  
- International roaming complications: Standardized network selection lists  
- Emergency call confirmation failure: Redundant transmission mechanisms  
- Shunting communication integrity: Link assurance signal implementation  
- Controller overload during emergencies: Priority-based call queuing  
- Equipment environmental durability: Ruggedized design specifications

## Undecided Issues and Responsible Parties
- Duration of emergency call warning tone (to be confirmed by trials) - Testing Authority  
- Specific languages to be supported in each country - National Railways  
- Additional controller equipment interface specifications - Network Operators  
- Automatic test equipment support requirements - Maintenance Teams  
- Alternative link assurance indication methods - National Railways  
- Directed network selection implementation details - Technical Committee  
- Public network pre-emption agreements for emergency calls - Regulatory Bodies  
- Detailed environmental condition thresholds - Standards Organizations