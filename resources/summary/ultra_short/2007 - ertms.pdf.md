Purpose & Scope: The system enables safe train movement across European railways with speed supervision up to 500 km/h. It defines operational states (e.g., Full/Partial Supervision, Shunting) and ensures compatibility with national train control systems. It does not specify implementation methods or cover non-train-control functions like passenger services.

Product Background / Positioning: ERTMS/ETCS is a European interoperability standard for train control, replacing fragmented national systems. It integrates with existing infrastructure via STM (Specific Transmission Module) and operates within CCS TSI (Technical Specifications for Interoperability) frameworks.

Core Functional Overview:  
- Mandatory train data entry before movement initiation.  
- Driver-acknowledged transitions between operational states (e.g., Full → Partial Supervision).  
- Shunting operation without track data or movement authority.  
- Supervision of movement authorities and speed limits with 5-second warning before brake intervention.  
- Emergency brake application for train trip (passing stop signal) and roll-away protection.  
- Train integrity monitoring and RBC handover during movement.  
- Reversing operation with speed/distance supervision per national values.

Key Users & Usage Scenarios: Drivers (primary), railway control centers (RBC operators), and train operators. Drivers require acknowledgment for state transitions; RBC operators manage movement authorities. Typical scenarios include shunting operations, level transitions, and emergency brake responses.

Major External Interfaces: Interfaces with RBC (for movement authorities and train location), trackside equipment (balises/loops for intermittent transmission), and national train control systems via STM. All interfaces use standardized ETCS protocols.

Key Non-functional Requirements:  
- Supports maximum train speed of 500 km/h.  
- Brake intervention required ≥5 seconds before speed limit exceedance.  
- Accident data retention: ≥24 hours; operational data: ≥1 week.  
- Mandatory use of harmonized default values for national parameters.

Constraints, Assumptions & Dependencies: Must support all ETCS application levels (0–3) with backward compatibility. Requires STM for national system integration. Depends on trackside infrastructure (balises, RBC) for full functionality.

Priorities & Acceptance Approach: All (M) requirements are mandatory; no optional features accepted as critical. Acceptance requires compliance with ETCS SRS and lower-level mandatory specifications. No acceptance criteria beyond requirement fulfillment.