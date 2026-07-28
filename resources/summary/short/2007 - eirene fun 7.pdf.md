# Short Summary: EIRENE Functional Requirements Specification

## Background and objectives
The EIRENE (European Integrated Railway Radio Enhanced Network) Functional Requirements Specification defines the requirements for a digital radio system based on GSM standards to meet the mobile communications needs of European railways. Its primary objective is to ensure interoperability along international lines and provide manufacturing economies of scale.

## In scope
- Voice services including point-to-point, emergency, broadcast, group, and multi-party calls
- Data services for text messaging, general applications, fax, and train control
- Railway-specific services like functional addressing, location-dependent addressing, and shunting mode
- Three mobile radio types: Cab radio, General purpose radio, and Operational radio
- Network requirements for coverage, performance, and call setup times

## Out of scope
- Detailed specification of controller equipment interfaces
- Pre-defined messaging applications (national implementations may define these)
- Public emergency calls (handling of '112' calls)
- National control/command system interfaces (though interfaces may be required)
- Detailed environmental specifications beyond core requirements

## Stakeholders and core use cases
**Stakeholders:**
- **Train drivers:** Use Cab radios for operational communications and safety-critical functions
- **Railway controllers (primary, secondary, power supply):** Manage train operations and emergency communications
- **Shunting team members:** Use Operational radios for shunting operations with link assurance signals
- **General railway staff:** Use General purpose radios for support communications
- **On-train staff (conductors, catering):** Communicate via train systems or dedicated radios
- **Network operators:** Maintain EIRENE-compliant networks for interoperability

**Core use cases:**
1. As a train driver, I want to initiate Railway emergency calls with a single action so that I can quickly alert all relevant personnel during emergencies
2. As a primary controller, I want to establish group calls to all drivers in a specific area so that I can coordinate train movements efficiently
3. As a shunting team member, I want to transmit a link assurance signal so that the driver knows the communication link remains intact during critical maneuvers
4. As a train driver crossing borders, I want the radio to automatically select the appropriate network so that I maintain continuous communication
5. As a railway staff member, I want to call users by functional numbers (like train numbers) rather than equipment numbers so that I reach the right person regardless of their specific device
6. As a maintenance worker, I want to use direct mode communications so that I can communicate in areas without network coverage

## Success metrics
- Railway emergency calls established within 2 seconds in 95% of cases
- Group calls between drivers in same area established within 5 seconds in 95% of cases
- System supports train speeds up to 500 km/h with seamless communication

## Major constraints
- Must comply with CENELEC standards for driver-machine interfaces
- Environmental specifications must withstand railway operating conditions (temperature, vibration, EMC)
- Five priority levels must be consistently implemented across all networks
- Functional numbers must be unique across all networks for interoperability
- Equipment must operate in designated railway frequency bands around 900 MHz

## Undecided issues
- Specific implementation of automatic joining for calls to all drivers in same area (requires further technical specification)
- National decisions on language support beyond the minimum 10 languages
- Whether different classes of service need to be defined for low to medium traffic rural areas
- Exact responsibilities split between Primary and Secondary Controllers (determined nationally)
- Implementation of directed network selection via external devices like balises