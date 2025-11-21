**Purpose & Scope**: The EIRENE system provides a standardized GSM-R based digital radio network for European railways, enabling interoperable voice and data communications across national borders. It supports train drivers, controllers, and railway staff for operational communications, emergency calls, and train control applications. The system excludes terminals and does not cover non-railway public communications.

**Product Background / Positioning**: Developed within UIC Project EIRENE, the system replaces national radio systems (UIC fiche 751-3) to enable international interoperability for high-speed rail traffic. It integrates with ERTMS/ETCS train control systems and serves as a foundation for future railway communications across Europe.

**Core Functional Overview**: Railway emergency calls (train and shunting modes), functional addressing by role/number, location-dependent addressing, shunting mode with link assurance signal, multi-driver communications within trains, priority-based call handling (5 levels), voice group/broadcast calls, and direct mode for local set-to-set operation.

**Key Users & Usage Scenarios**: Train drivers (Cab radio), controllers (primary, secondary, power supply), shunting teams, operational staff (operational radio), and general staff (general purpose radio). Key scenarios include emergency calls, train operations, shunting maneuvers, and maintenance communications.

**Major External Interfaces**: Interfaces with ERTMS/ETCS train control systems, controller equipment, public networks, and train-borne systems (driver safety device, train-borne recorder). Supports standardized data interfaces for external applications.

**Key Non-functional Requirements**: Call set-up time <2s for railway emergency calls, <5s for group calls between drivers; 95% coverage over 95% of designated area; supports speeds up to 500 km/h; battery life minimum 8 hours (20% talk, 60% group calls, 20% standby); 95% of calls within required time, 99% within 1.5x required time.

**Constraints, Assumptions & Dependencies**: Mandatory interoperability for international traffic, functional addressing must be implemented across networks, integration with ERTMS/ETCS required, shunting mode with link assurance mandatory, and support for 5 priority levels for call handling.

**Priorities & Acceptance Approach**: Mandatory requirements are critical for interoperability; railway emergency calls have highest priority; acceptance based on meeting call set-up time requirements, coverage specifications, and priority handling performance metrics.