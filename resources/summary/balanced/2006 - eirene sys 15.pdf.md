# Balanced Summary: European Integrated Railway Radio Enhanced Network (EIRENE) System Requirements Specification

## Goals and Scope
The EIRENE System Requirements Specification defines a digital radio standard based on GSM to meet the mobile communications needs of European railways, ensuring interoperability for trains and staff crossing national borders. It covers ground-train voice and data communications, as well as ground-based mobile communications for trackside workers, station staff, and administrative personnel. The specification distinguishes between mandatory requirements for interoperability and optional features that, if selected, must be implemented consistently.

## Stakeholders and User Stories
- **GSM-R Operators Group**: Responsible for approving and maintaining the EIRENE specifications to ensure network interoperability.
- **Railway Network Infrastructure Providers**: Design and operate EIRENE-compliant GSM-R networks to provide required service levels to mobile equipment.
- **Mobile Equipment Manufacturers**: Develop Cab radios, General Purpose radios, and Operational radios that meet core and type-specific EIRENE requirements.
- **Train Drivers**: Use Cab radios for operational communications, emergency calls, and shunting mode while ensuring safety and efficiency.
- **Railway Controllers (Primary/Secondary/Power Supply)**: Manage train operations and communicate with drivers using standardized call types and priorities.
- **Trackside and Shunting Personnel**: Use Operational radios for maintenance, shunting operations, and emergency communications in harsh environments.

**User Stories:**
1. As a train driver, I want to initiate a Railway emergency call with a single button press so that I can quickly alert controllers and other trains of a dangerous situation.
2. As a railway controller, I want to receive location information for incoming emergency calls so that I can identify the incident location and coordinate responses.
3. As a shunting team member, I want to join a dedicated shunting group call so that I can communicate securely with my team during maneuvers.
4. As a maintenance worker, I want to register my functional number using USSD so that I can be reached by my role rather than a personal device number.
5. As a network planner, I want to design coverage meeting specified field strength criteria so that voice and safety-critical data services are reliably available.
6. As a mobile equipment manufacturer, I want clear environmental and interface specifications so that I can develop radios that operate reliably across different railway networks.

## Key Processes
1. **Mobile Registration (Trigger: Power-on)** – Mobile equipment performs self-test via GSM IMSI attach and registers with an authorized network based on SIM-stored priorities.
2. **Functional Number Registration (Trigger: User action or automatic detection)** – User registers a functional number (e.g., train number) via USSD, creating a mapping to their MSISDN in the network routing database.
3. **Call Initiation (Trigger: User selects function or dials number)** – Radio determines call type (point-to-point, group, broadcast), priority, and destination based on MMI input and initiates setup.
4. **Call Arbitration (Trigger: Incoming call during ongoing call or new outgoing request)** – Cab radio applies priority-based rules to manage multiple call requests, potentially pre-empting lower-priority communications.
5. **Emergency Call Handling (Trigger: Emergency button press)** – Radio initiates high-priority VGCS call to predefined group, with automatic retry on failure and confirmation message sent after call.
6. **Shunting Mode Entry (Trigger: User selects shunting mode)** – Radio activates common shunting group, registers functional number, and joins dedicated group call after coordination via common channel.
7. **Location-Dependent Addressing (Trigger: Short code dialing)** – Network routes call (e.g., to controller) based on caller's current cell location or external location data.

## Domain Data Elements
- **Mobile Station (MS)** – Primary Key: IMSI; Fields: MSISDN, Equipment Type (Cab/GP/Operational), Power Class, Registered Functional Number, Active Group IDs.
- **Functional Number (FN)** – Primary Key: Full EIRENE Number; Fields: Call Type (CT), User Identifier Number (UIN), Function Code (FC), Associated MSISDN, Registration Timestamp.
- **Train Journey** – Primary Key: Train Number; Fields: Engine Number, Registered Driver MSISDN, Route Information, Active On-Train Functions (e.g., ERTMS/ETCS).
- **Shunting Group** – Primary Key: Group ID (e.g., 501-520); Fields: Service Area, Team Leader, Member List, Status (Active/Inactive), Link Assurance Signal State.
- **Network Cell** – Primary Key: Cell ID; Fields: Geographic Coverage Area, Associated Controller Numbers, Neighbor Cells, Signal Strength Parameters.
- **Emergency Call Record** – Primary Key: Call Instance ID; Fields: Originating Functional Number, Group ID, Timestamp, Confirmation Status, Location (Cell).

## Non-Functional Requirements
1. **Coverage & Reliability**: 95% coverage probability with specified field strength levels; handover success rate ≥99.5% under design load.
2. **Call Setup Time**: Dependent on eMLPP priority, with authentication and ciphering enabled; network transit delays <250ms.
3. **Environmental Tolerance**: Equipment must operate from -20°C to +55°C (Cab radio to +70°C), withstand vibration/shock, and meet IP54 for Operational radios.
4. **EMC Compliance**: Emission and immunity per railway standards (ENV 50121 series), with GSM transmission masks taking precedence in-band.
5. **Battery Life**: Minimum 8 hours for handheld radios under defined duty cycles; Cab radio backup power for 6 hours on main failure.
6. **Interoperability**: Compliance with referenced GSM (EN 301 515) and railway-specific (MORANE) standards for services, interfaces, and protocols.

## Milestones and External Dependencies
1. **Approval of Specification Version 15** – Achieved on 17 May 2006 by GSM-R Operators, Functional, and Industry Groups.
2. **Frequency Band Allocation** – Dependent on national regulators assigning UIC band (876-880/921-925 MHz) per CEPT/ECC decisions.
3. **ERTMS/ETCS Integration** – Requires EURORADIO FFFIS interface implementation for train control communications.
4. **Cross-Border Network Interconnection** – Bilateral agreements needed for service area coordination and international call routing.
5. **Manufacturer Compliance** – Development and testing of mobile equipment against core and type-specific specifications.

## Risks and Mitigation Strategies
1. **Interoperability Failure** – Strict adherence to mandatory requirements and standardized interfaces; certification testing.
2. **Network Coverage Gaps** – Careful planning to meet field strength criteria; use of direct mode as fallback where allowed.
3. **Emergency Call Congestion** – Priority pre-emption (eMLPP) and confirmation message delay with random offset.
4. **Functional Number Conflicts** – Registration validation and forced de-registration procedures with user notification.
5. **EMC Interference with Legacy Systems** – Compliance with emission standards and coordination with railway operators.

## Undecided Issues
1. **Alphanumeric Train Numbers** – Handling of non-numeric identifiers may require terminal translation or national solutions.
2. **Automatic Network Selection** – Implementation optional; driver may deactivate with simple MMI actions.
3. **Direct Mode Implementation** – Optional feature; if implemented, must follow specified channel and protocol requirements.
4. **Text Messaging Applications** – No international standardization; left to national implementations using SMS.
5. **External Location Data Integration** – Optional enhancement to cell-dependent routing; requires compliance with eLDA specifications.
6. **Controller Display of Caller Location** – Optional feature; if provided, minimum location is current GSM cell.