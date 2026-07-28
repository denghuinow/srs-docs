# Detailed Summary: EIRENE System Requirements Specification

## Background and Scope
The European Integrated Railway Radio Enhanced Network (EIRENE) System Requirements Specification defines a digital radio standard based on GSM to meet the mobile communications needs of European railways. It ensures interoperability for trains and staff crossing national borders and provides manufacturing economies of scale. The specification covers ground-train voice/data communications and ground-based mobile communications for trackside workers, station staff, and administrative personnel. Non-goals include detailed field-level implementations and specifications for non-interoperable fixed network components.

## Stakeholders Matrix and Use Cases
- **GSM-R Network Operator**: Manages network infrastructure and ensures service delivery.
- **Train Driver**: Uses Cab radio for operational communications and emergency calls.
- **Railway Controller (Primary/Secondary/Power Supply)**: Coordinates train movements and handles emergency communications.
- **Shunting Team Member**: Uses Operational radio for shunting operations and group communications.
- **Maintenance Personnel**: Uses General Purpose radio for support communications.
- **ERTMS/ETCS System**: Interfaces with Cab radio for train control data transmission.
- **Network Maintenance Staff**: Manages subscriber data and network configuration.
- **Regulatory Body**: Allocates frequencies and numbering resources.

**Main Scenarios**: Driver initiates emergency call; Controller broadcasts to trains in area; Shunting team establishes dedicated group call; Driver registers train number; Mobile roams between networks; ERTMS data transmission; Driver calls controller via short code; User sends/receives SMS.
**Exception Scenarios**: Network failure triggers direct mode; Registration conflict resolution; Emergency call confirmation failure; Handover failure at high speed.

## Business Process
**Main Process: Driver Initiates Emergency Call**
1. Trigger: Driver presses emergency button.
2. Cab radio sends group call setup with priority 0.
3. Network routes call to predefined emergency group area.
4. Controllers and trains in area receive call with auto-answer.
5. Conversation: Driver describes emergency.
6. Call termination by controller or driver.
7. Confirmation: Cab radio sends UUS1 message to confirmation centre.
8. Logging: Call details stored in train-borne recorder.

**Key Branch: Shunting Mode Activation**
1. Trigger: User selects shunting mode.
2. Radio activates common shunting group (ID 500).
3. Leader registers dedicated group (e.g., ID 501).
4. Members join dedicated group via functional registration.

**Key Branch: Functional Number Registration**
1. Trigger: Driver enters train number.
2. Cab radio sends USSD registration message.
3. Network validates and updates routing database.
4. Confirmation sent to mobile.

## Domain Model
- **Mobile Station**: MSISDN (unique), IMSI (unique), Power Class, SIM data.
- **Functional Number**: Call Type (required), User Identifier Number (required), Function Code (required).
- **Train**: Train Number (unique), Engine Number (unique), Coach Number (unique).
- **Shunting Group**: Group ID (unique), Area ID, Member List.
- **Controller**: Location Number, Function Code (e.g., 01=primary).
- **Emergency Call**: Group ID, Anchor MSC, Timestamp, Confirmation Status.
- **Network Cell**: Cell ID, Service Area, Coverage Level.
- **Subscriber Profile**: Priority Level, Access Classes, Closed User Groups.

## Interfaces and Integrations
- **ERTMS/ETCS to Cab Radio**: Direction: Bi-directional; Theme: Safety-critical data; Input: Movement authorities; Output: Acknowledgements; SLA: High reliability, <0.5s latency.
- **Public Address Interface**: Direction: Cab radio to PA system; Theme: Passenger announcements; Input: Audio stream; Output: Amplified audio; SLA: Synchronized audio, <100ms delay.
- **Train-Borne Recorder**: Direction: Cab radio to recorder; Theme: Call logging; Input: Call details, confirmations; Output: Stored records; SLA: Non-volatile storage, continuous logging.
- **GSM Network (A Interface)**: Direction: BSS to NSS; Theme: Call control and mobility; Input: Handover requests; Output: Call setup commands; SLA: 99.5% handover success.
- **Direct Mode Air Interface**: Direction: Mobile to mobile; Theme: Fallback communications; Input: Voice packets; Output: Voice packets; SLA: 1W power, simplex mode.
- **USSD Gateway**: Direction: Mobile to network; Theme: Functional registration; Input: USSD strings; Output: Confirmation/error; SLA: <2s response time.
- **Short Message Service Centre**: Direction: Network to mobile; Theme: Text messaging; Input: SMS packets; Output: Delivery reports; SLA: 95% delivery within 10s.
- **External PSTN/ISDN**: Direction: GSM-R to public network; Theme: Breakout calls; Input: Dialled digits; Output: Call routing; SLA: <250ms call setup addition.

## Acceptance Criteria
**Capability: Emergency Call Initiation**
- Given a driver with registered functional number, when pressing the emergency button, then a group call with priority 0 is established to all controllers and trains in the area within 2 seconds.
- Given an ongoing emergency call, when a higher priority emergency occurs, then the existing call is pre-empted and the new call is connected.

**Capability: Shunting Mode**
- Given a shunting leader in the common group, when registering a dedicated group, then members can join using the announced group number and functional registration.
- Given a shunting operation in progress, when a shunting emergency is initiated, then all shunting members receive the emergency call on group ID 599.

**Capability: Functional Number Management**
- Given a driver entering a train number, when registration is attempted with a conflicting existing registration, then the driver can force de-registration and register successfully.
- Given a roaming train entering a new network, when crossing the border, then the functional number is automatically re-registered in the new network.

## Non-Functional Metrics
- **Performance**: Call setup time ≤2s for emergency calls; Handover break ≤300ms.
- **Reliability**: Network availability 99.95%; Handover success rate ≥99.5%.
- **Security**: Authentication and encryption per GSM standards; Closed User Group support.
- **Compliance**: Conformance to ETSI EN 301 515; Frequency band 876-915/921-960 MHz.
- **Observability**: Call detail recording for emergency calls; Network performance monitoring via OMC.

## Milestones and Release Strategy
1. Core GSM-R network deployment with voice services.
2. Cab radio and ERTMS interface implementation.
3. Functional numbering and location-dependent addressing rollout.
4. Shunting mode and direct mode feature release.
5. Cross-border interoperability testing and validation.
6. Full operational capability with all mandatory features.

## Risk List and Mitigation Strategies
1. **Frequency Interference**: Coordinate with national regulators; use standardized UIC band.
2. **Interoperability Failures**: Conduct cross-border testing; adhere to mandatory specifications.
3. **Emergency Call Congestion**: Implement eMLPP pre-emption; optimize group call areas.
4. **Handover at High Speed**: Optimize handover algorithms; consider synchronous handover.
5. **Functional Number Conflicts**: Implement forced de-registration; manual override procedures.
6. **Direct Mode Interference**: Enforce GSM-R priority; automatic fallback to GSM-R when available.
7. **Legacy System Integration**: Develop gateway interfaces; phased migration plans.
8. **Security Breaches**: Use GSM authentication; restrict external network access.

## Undecided Issues and Responsible Parties
1. **Alphanumeric Train Number Support**: To be determined by national railways.
2. **Enhanced Location Determination Integration**: Responsibility of eLDA working group.
3. **Specific EMC Emission Limits for Cab Radios**: Further testing required by manufacturers.
4. **Cross-Border Emergency Call Routing Optimization**: Bilateral agreements needed between operators.
5. **Battery Life Standards for Extreme Temperatures**: Additional testing by environmental committees.
6. **Public Network Access Security Policies**: National regulatory bodies to define.
7. **ERTMS/ETCS Coverage Validation at High Speeds**: Post-implementation review by ERTMS group.
8. **Direct Mode Channel Expansion**: Frequency management authorities to decide.