Purpose & Scope
The EIRENE system specifies a GSM-based digital radio standard for European railways to enable interoperable voice and data communications across national borders. It covers ground-train communications, trackside worker communications, and support for train operations, but does not cover public emergency calls (112) or non-railway applications.

Product Background/Positioning
The EIRENE system is built on the GSM standard with railway-specific extensions, designed to enable seamless communication across European railway networks. It serves as the standard for railway communications infrastructure, replacing national variations and enabling cross-border interoperability for trains and personnel.

Core Functional Overview
- Voice Group Call Service (VGCS) and Voice Broadcast Service (VBS) for group communications
- Enhanced Multi-Level Precedence and Pre-emption (eMLPP) for priority-based call handling
- Functional numbering to address users by role (e.g., train number) rather than device
- Location-dependent addressing for automatic routing based on train position
- Railway emergency calls with priority 0 for immediate response
- Shunting mode for specialized communication during shunting operations
- Direct mode as fallback when GSM infrastructure is unavailable

Key Users & Scenarios
- Train drivers use cab radios for operational communications, emergency calls, and multi-driver communications
- Shunting teams use operational radios with dedicated shunting group capabilities
- Controllers (primary, secondary, power supply) use radios to manage train movements
- Maintenance teams use general-purpose radios for support communications

Main External Interfaces
- GSM network infrastructure (BSS, NSS)
- ERTMS/ETCS train control systems
- Public address systems
- UIC intercom systems
- Driver safety devices
- Train-borne recorders

Key Non-Functional Requirements
- 95% coverage probability at specified signal strength levels (38.5 dBµV/m for voice)
- Handover success rate of 99.5% for train routes
- Maximum alerting duration of 60 seconds for high-priority calls
- Call setup times must be fast, especially for emergency calls
- Power classes: Cab radio (8W), General purpose/Operational (2W or 8W)

Constraints, Assumptions, Dependencies
- Must operate in specific frequency bands (876-880/921-925 MHz)
- Must comply with GSM standard specifications and ETSI standards
- Direct mode is optional but must follow specific technical requirements if implemented
- Requires coordination between national railway networks for interoperability

Priority & Acceptance
- Railway emergency calls have highest priority (eMLPP 0)
- Railway operations calls (e.g., driver-controller) have priority 2
- Railway information calls have priority 4
- Emergency calls must be automatically re-attempted if unsuccessful
- Acceptance requires compliance with all mandatory requirements (marked M)