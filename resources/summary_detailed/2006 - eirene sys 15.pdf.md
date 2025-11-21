# Detailed Summary

## Background and Scope
- The EIRENE System Requirements Specification defines a digital radio standard for European railways based on GSM technology to ensure interoperability across national borders.
- It covers ground-train voice/data communications and mobile communications for trackside workers, station staff, and administrative personnel.
- Non-goals include full implementation of field-level details and specification of national fixed network interfaces beyond interoperability requirements.

## Role Matrix and Use Cases
**Roles:** Driver (Cab Radio User), Controller, Shunting Team Member, Maintenance Worker, General Staff, Data Systems
**Main Scenarios:**
- Driver initiates emergency call to controllers and other drivers
- Controller broadcasts messages to train groups
- Shunting team establishes dedicated group communications
- User registers/deregisters functional numbers
- Driver conducts multiple driver communications on same train
- Mobile equipment enters/exits direct mode when GSM unavailable
**Exception Scenarios:**
- Railway emergency call setup failure with automatic retry
- Loss of functional number correlation requiring recovery
- Network selection failure during roaming

## Business Process
**Main Process - Emergency Call Initiation (8 steps):**
1. Driver activates emergency button (Trigger: User action)
2. Cab radio initiates VGCS call with priority 0
3. Network routes to predefined emergency group area
4. Controllers and trains in area receive call with auto-answer
5. Voice communication established
6. Call continues until terminated by authorized controller
7. Confirmation process initiated after call clear-down
8. Confirmation message sent to ground center (Output: Call record)

**Key Branch - Functional Number Registration (4 steps):**
1. User activates registration function
2. Mobile sends USSD message with functional number
3. Network validates and updates routing database
4. Success/failure indication returned to mobile

## Domain Model
**Entities:**
- Mobile Station (Fields: IMSI [required, unique], MSISDN [required, unique], Power Class)
- SIM Card (Fields: Access Classes [required], Network List [required])
- Functional Number (Fields: Call Type [required], User Identifier [required], Function Code [required])
- Group Call (Fields: Service Area [required], Group ID [required, unique], Priority Level)
- Controller Position (Fields: Location Number [required], Function Type [required])
- Train (Fields: Train Number [required], Engine Number, Coach Number)
- Emergency Call Record (Fields: Timestamp [required], Originating Mobile, Location)
- Shunting Group (Fields: Group Number [required], Member Count, Leader ID)

## Interfaces and Integrations
- **ERTMS/ETCS System** (Direction: Bidirectional) - Theme: Train control data exchange - Input: Movement authorities - Output: Train position - SLA: Safety-critical latency requirements
- **Public Networks** (Direction: Outbound) - Theme: External call routing - Input: Breakout codes - Output: MSISDN numbers - SLA: National telecom standards
- **Confirmation Center** (Direction: Inbound) - Theme: Emergency call confirmation - Input: UUS1 messages - Output: Acknowledgement - SLA: Store all confirmations
- **Train-borne Recorder** (Direction: Outbound) - Theme: Event logging - Input: Call records - Output: Storage confirmation - SLA: Non-volatile storage
- **Direct Mode System** (Direction: Peer-to-peer) - Theme: Fallback communications - Input: PTT activation - Output: Voice transmission - SLA: 1W power limit

## Acceptance Criteria
**Emergency Call Capability:**
- Given a driver activates the emergency button when GSM coverage exists
- When the system initiates a VGCS call
- Then all controllers and trains in the predefined area shall receive the call within 2 seconds

**Functional Number Registration:**
- Given a user enters a valid functional number
- When the registration USSD message is sent to the network
- Then the routing database shall be updated and success confirmation returned within 5 seconds

## Non-functional Metrics
- **Performance:** Call setup time ≤2 seconds for emergency calls; Handover success rate ≥99.5%
- **Reliability:** 95% coverage probability at specified field strength levels; Battery life ≥8 hours for handheld units
- **Security:** Authentication required; Encryption using standard algorithms
- **Compliance:** Conform to ETSI GSM standards and UIC specifications
- **Observability:** All emergency calls logged with confirmation; Network performance monitoring

## Milestones and Release Strategy
1. Core network infrastructure deployment
2. Cab radio certification and rollout
3. Cross-border interoperability testing
4. Operational radio deployment for shunting operations
5. Emergency call system validation
6. Full system operational acceptance

## Risk List and Mitigation Strategies
- **Interoperability failures** - Strict adherence to standardized interfaces and protocols
- **Network coverage gaps** - Comprehensive network planning with 95% coverage targets
- **Emergency call congestion** - eMLPP priority implementation with pre-emption
- **Functional number conflicts** - Centralized validation and forced de-registration procedures
- **Roaming complications** - Standardized SIM profiles with network priority lists
- **Direct mode interference** - Channel management and GSM priority enforcement
- **Equipment environmental failures** - Compliance with railway environmental standards
- **System capacity limitations** - Network dimensioning based on traffic studies

## Undecided Issues and Responsible Parties
- Implementation of adaptive multi-rate codec for group calls (GSM-R Operators Group)
- Final validation of ETCS coverage levels for high-speed lines (Functional Group)
- National allocation of service areas for group calls (National Railways)
- Bilateral agreements for cross-border service areas (Adjacent Network Operators)
- Selection of authentication algorithms (Individual Railways)
- Implementation of location-dependent addressing enhancements (Industry Group)
- Integration protocols with national fixed networks (Not mentioned)
- Migration strategies from legacy systems (Not mentioned)