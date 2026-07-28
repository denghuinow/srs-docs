# Short Summary: EIRENE System Requirements Specification

## Background and objectives
The EIRENE (European Integrated Railway Radio Enhanced Network) System Requirements Specification defines a digital radio standard based on GSM to meet the mobile communications needs of European railways, ensuring interoperability for trains and staff crossing national borders. It aims to provide a unified system for ground-train voice/data communications and ground-based mobile communications for railway personnel.

## In scope
- GSM-based network infrastructure and mobile equipment (Cab, General Purpose, Operational radios)
- Railway-specific services: functional addressing, location-dependent addressing, emergency calls, shunting mode
- Core GSM services: telephony, group/broadcast calls, SMS, data services
- Numbering plan and subscriber management for interoperability
- Environmental and physical requirements for railway operational environments

## Out of scope
- Public emergency calls (e.g., "112" calls) for non-railway emergencies
- Detailed implementation of national fixed networks or external interfaces
- Specific controller equipment designs beyond basic functional requirements
- Pre-defined text messaging applications (optional national implementations)
- Direct mode implementation (optional feature)

## Stakeholders and core use cases
**Stakeholders:**
- **GSM-R Operators Group**: Oversees network standards and interoperability.
- **Railway administrations**: Deploy and operate EIRENE networks.
- **Train drivers**: Use Cab radios for operational and emergency communications.
- **Controllers (Primary/Secondary/Traffic/Power supply)**: Manage train operations and safety.
- **Trackside workers (shunting/maintenance teams)**: Use Operational radios for ground operations.
- **General railway staff**: Use General Purpose radios for administrative communications.

**User stories:**
1. As a train driver, I want to initiate a railway emergency call with a single button press so that I can quickly alert controllers and other trains of a dangerous situation.
2. As a controller, I want to receive location information with emergency calls so that I can identify the exact train and area involved.
3. As a shunting team member, I want to join a dedicated shunting group call so that I can communicate safely during shunting operations.
4. As a train driver, I want to call the appropriate controller based on my current location so that I reach the correct controller without manual number lookup.
5. As a railway administrator, I want to use functional numbering (e.g., train numbers) so that I can reach personnel by their current role rather than personal devices.
6. As a maintenance worker, I want to use direct mode communications when GSM coverage is unavailable so that I can maintain safety-critical communications.

## Success metrics
- Call setup times meeting eMLPP priority requirements (e.g., emergency calls within 2 seconds)
- Network coverage providing 95% probability of specified field strength levels for voice and safety-critical data
- Handover success rate of at least 99.5% under design load conditions
- Interoperability achieved for all mandatory features across different national networks

## Major constraints
- Must operate within designated railway GSM frequency bands (876-880/921-925 MHz)
- Must maintain backward compatibility with referenced GSM standards
- Environmental conditions: equipment must operate from -20°C to +55°C (storage to -40°C)
- Must support functional numbering within ITU-T E.164 limitations
- Authentication and ciphering must not compromise required call setup times

## Undecided issues
- Specific implementation of location-dependent addressing using external systems (optional)
- National variations in numbering plan implementation for alphanumeric train numbers
- Detailed protocols for recovery from loss of functional number correlation
- Specific testing procedures for General Purpose and Operational radios beyond core requirements
- Implementation of directed network selection mechanisms (optional)