**Purpose & Scope**: The system is an Electronic Logbook Software System (ELSS) required for UK fishing vessels over 15 meters (phased implementation: 24m+ by Jan 2010, 15m+ by July 2011) to replace paper logbooks. It captures and transmits fishing activity data to UK fisheries administrations' ERS system per Council Regulation (EC) No. 1966/2006. It does not cover onshore data entry or non-fishing vessel operations.

**Product Background / Positioning**: The ELSS is part of the UK Fisheries Administration's ELSS Approval Programme to comply with EU fishing regulations. It integrates with the UK fisheries administrations' ERS system as the primary data transmission channel for fishing vessel reporting requirements.

**Core Functional Overview**: 
- Capture 12 mandatory report types (Departure, Fishing Activity, Relocation, Transhipment, Entry/Exit Zone, Control Point Area, Discard, Prior Notification, End of Fishing, Return to Port, Landing Declaration)
- Transmit data via email with PGP encryption using specific filename and subject formats
- Support data corrections and deletions for current trips only
- Provide on-board printing of logbook data in hard copy
- Retain all logbook reports until end of trip
- Implement user authentication with master and subsidiary user roles
- Validate data against UK XML/XSD before transmission
- Support automatic daily transmissions with specific event-based triggers

**Key Users & Usage Scenarios**: Vessel masters (primary users for data entry and transmission), vessel owners (set up subsidiary users), and UK fisheries administrators (receive and process data). Usage scenarios include daily fishing activity reporting, transhipment events, landing declarations, and port entries/exits with specific transmission timing requirements.

**Major External Interfaces**: UK Fisheries Administrations' ERS system (primary data transmission interface), onboard email systems (for data transmission), onboard GPS/weighing systems (for data population), and ERS website (for onshore agent access).

**Key Non-functional Requirements**: All dates/times must use UTC format; data must be transmitted in XML format validated against UK XML/XSD; data must be encrypted using PGP; must retain all logbook reports until end of trip; must support test transmissions for validation; software updates must not impact compliance with regulatory requirements.

**Constraints, Assumptions & Dependencies**: ELSS must only be supplied for onboard use (not for onshore use by agents); must comply with Council Regulation (EC) No. 1966/2006 and Commission Regulation (EC) No. 1077/2008; must use UK Fisheries' defined XML/XSD schema; must not interfere with mandatory data capture and submission functions.

**Priorities & Acceptance Approach**: Mandatory features required for ELSS approval (C and CIF status items); acceptance requires completion of Product Profile questionnaire and validation against UK Fisheries' requirements; product must be resubmitted for re-approval if software updates impact regulatory compliance.