**Purpose & Scope**
The system is a standardized communication solution for remote monitoring and control (SCADA) of wind turbines and wind farms. It defines the data exchange between turbine controllers and remote computers, specifying what data is transferred and how, but not how the data is used by the SCADA system. It does not cover SCADA system characteristics, HMI design, control algorithms, local temporary connections (e.g., portable PCs), voice/video communication, or actor-specific functions like energy accounting.

**Product Background / Positioning**
The system addresses the lack of open standards in wind turbine communication, where each supplier's proprietary solution is incompatible with others. It is intended as a procurement guide to enable vendor-independent, interoperable solutions for supervising and controlling turbines from multiple manufacturers. The specification is a foundational step toward an international communication standard within IEC TC88.

**Core Functional Overview**
1.  Remote supervision of wind turbine status and state changes.
2.  Remote control of equipment (e.g., switchgear, start/stop commands).
3.  Management and acknowledgment of alarms from abnormal states.
4.  Recording and retrieval of chronological event logs.
5.  Changing operational parameters and set points.
6.  Retrieval of configuration data, settings, and historical data (e.g., fault records).
7.  System management functions (network management, time synchronization, software/configuration management).

**Key Users & Usage Scenarios**
Primary users are the wind turbine operator (for operation & maintenance) and the owner. For wind farms, the electrical network operator is also a key user. Users access the system via remote SCADA stations for daily monitoring, issuing control commands, responding to alarms, and retrieving operational data. Access to functions and data is controlled by user authentication and authorization rules.

**Major External Interfaces**
The core interface is between the wind turbine's control system and the remote SCADA computers. For wind farms, an intermediate interface may exist with a Wind Farm Main Controller (WFMC). The system must interface with existing, proprietary turbine control systems via gateways. It does not define the physical transmission media (e.g., phone line, internet, radio).

**Key Non-functional Requirements**
*   **Performance:** Time-critical functions (e.g., power control set points, start/stop commands) must have an overall transfer time not exceeding 0.5 seconds. System management functions should have a response delay not exceeding 2 seconds.
*   **Security:** Requires client and server authentication, data integrity (acceptable residual error rate), and support for data confidentiality (encryption).
*   **Reliability & Availability:** The communication system shall not be critical for personnel, plant, or network safety; all safety functions must be self-contained in the turbine. The system should support redundant communication channels and components.
*   **Environmental:** Must operate in a wide span of temperature, moisture, salinity, and vibration levels.
*   **Data Quality:** All data must be timestampable with UTC time, with an accuracy and resolution of at least 10 ms.

**Constraints, Assumptions & Dependencies**
*   The wind turbine is autonomously controlled; the communication system is for supervision and coordination, not for safety-critical functions.
*   The system must be based on open, widely accepted communication methods.
*   It must be compatible with existing wind power plants via gateway solutions.
*   The specification assumes a hierarchical, object-based data model for wind turbine components and signals.

**Priorities & Acceptance Approach**
Time-critical operational functions (control, set points, alarms) are highest priority, followed by routine supervision and system management. Acceptance is based on fulfilling the specified functional requirements, performance metrics (e.g., 0.5s transfer time), security features, and interoperability goals. The specification itself is intended for use as a baseline in procurement and tendering processes.