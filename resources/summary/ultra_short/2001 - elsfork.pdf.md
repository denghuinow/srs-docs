**Purpose & Scope**: Defines requirements for data communication between wind turbine control systems and remote SCADA systems. Covers single turbines and wind farms, specifying data transfer and handling but not SCADA usage. Excludes SCADA system specifications, HMI, control algorithms, and safety-critical functions. Communication system must not cause turbine malfunctions.

**Product Background / Positioning**: Addresses lack of standardization in wind turbine communication systems, where proprietary solutions prevent multi-vendor management. Developed by Danish-Swedish working group (Vattenfall, Sycon, Tech-wise, SEAS) to enable interoperability. Part of IEC TC88 standardization effort for wind turbine communication.

**Core Functional Overview**: Remote monitoring of turbine status and operational data; remote control (start/stop, set points); alarm management for abnormal conditions; event and log management; configuration data retrieval; disturbance/fault record retrieval; system management (network, time sync, self-checking); security management.

**Key Users & Usage Scenarios**: Wind farm operators (multi-turbine management), turbine operators (operation/maintenance), owners (oversight), external vendors. Different permission levels for access. Typical scenarios include routine monitoring, control operations, alarm response, and maintenance data retrieval.

**Major External Interfaces**: Interfaces with SCADA systems for remote monitoring; interfaces with wind turbine control systems; compatibility with existing proprietary systems via gateways; supports TCP/IP, MMS, IEC 60870-5, and TASE.2 protocols.

**Key Non-functional Requirements**: All data must be time-stamped with UTC time (accuracy ≥10ms); time-critical functions must have overall transfer time ≤0.5 seconds; data must be restorable with automatic recovery; redundant communication channels required; authentication, data integrity, and confidentiality mandatory; must operate in harsh environments (temperature, moisture, salinity, vibration).

**Constraints, Assumptions & Dependencies**: Communication system must not be used for safety-critical functions; faults must not cause turbine malfunctions; system must minimize subsystem interference; must interface with existing plants via gateways; designed for environments with wide temperature, moisture, salinity, and vibration ranges.

**Priorities & Acceptance Approach**: Primary focus on enabling multi-vendor interoperability for procurement guidance. Acceptance based on meeting specified functional and non-functional requirements. Document serves as foundation for IEC standardization (IEC TC88) without recommending specific protocols.