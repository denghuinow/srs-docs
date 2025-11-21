Purpose & Scope
The EIRENE system provides a GSM-R (GSM for Railway) standard for European railways, enabling voice and data communications for train operations, staff, and controllers across national borders. It covers ground-train voice and data communications, mobile communications for trackside workers, station staff, and railway administrative personnel. The system does not cover physical implementation of radio equipment itself, which is specified separately in mobile equipment requirements.

Product Background / Positioning
EIRENE is an extension of GSM standard for railway use, developed within UIC Project EIRENE to ensure technical interoperability for cross-border train operations. It builds upon GSM standards with railway-specific enhancements including functional addressing, location-dependent routing, and emergency call handling. The system integrates with existing railway infrastructure including ERTMS/ETCS for train control and safety systems.

Core Functional Overview
1. Voice Group Call Service (VGCS) and Voice Broadcast Service (VBS) for group communications across railway personnel
2. Enhanced Multi-Level Precedence and Pre-emption (eMLPP) for priority-based call handling across railway operations
3. Functional addressing allowing calls to be placed by role (e.g., train number, driver) rather than specific user
4. Location-dependent addressing routing calls based on train location within the railway network
5. Railway emergency calls with highest priority (level 0) to stop train movements in safety-critical situations
6. Shunting mode for specialized communication during train shunting operations
7. Direct mode as fallback communication without network infrastructure for remote areas or network failures

Key Users & Usage Scenarios
- Train drivers use Cab radio for operational communications (priority level 2), emergency calls, and multiple driver communications
- Primary, secondary, and power supply controllers use operational radios for train movement coordination (priority level 3)
- Shunting team leaders and members use operational radios in shunting mode (priority level 2)
- Trackside workers, station staff, and maintenance personnel use general purpose radios for operational communications
- All users require emergency call functionality with automatic retry on failure

Major External Interfaces
- GSM network infrastructure (BSS, NSS) for standard mobile services
- ERTMS/ETCS systems for train control and safety communications
- Public Address systems for passenger announcements
- UIC Intercom for on-train communication
- Driver's Safety Device for alertness monitoring
- Train Borne Recorder for call logging
- Train Interface Unit (TIU) for connecting on-train systems to radio equipment

Key Non-functional Requirements
- Coverage: 95% probability at 38.5 dBµV/m for voice (95% at 41.5 dBµV/m for ETCS levels 2/3)
- Handover success rate: Minimum 99.5% over train routes
- Call setup time: Must be achieved with authentication/ciphering enabled
- Alerting duration: Maximum 60 seconds for priority calls
- Direct mode: 1W maximum transmit power, simplex operation
- Battery life: Minimum 8 hours operation based on specific usage profile

Constraints, Assumptions & Dependencies
- Must comply with GSM standards (ETSI EN 301 515) with railway-specific enhancements
- Requires implementation of eMLPP for priority handling across all network elements
- Functional addressing requires network-level translation of functional numbers to MSISDNs
- Depends on standardization of numbering plans (National and International EIRENE Numbers)
- Requires interoperability between national railway networks through GMSC interconnection
- Relies on cell-dependent routing as primary location addressing method

Priorities & Acceptance Approach
- Railway emergency calls: Priority level 0 (highest priority, must be processed immediately)
- Railway operation calls: Priority level 2 (e.g., driver-controller communications)
- Railway information calls: Priority level 4 (standard communications)
- Acceptance criteria: Must meet coverage requirements (95% at specified signal strength), handover success rate (99.5%), and call setup time requirements
- Emergency call confirmation must be automatically sent to confirmation center using UUS1
- All priority levels must be consistently implemented across all national railway networks