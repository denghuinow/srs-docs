# Short Summary

- **Background and objectives**: The specification addresses the lack of standardized communication solutions for wind turbine control and monitoring, aiming to define functional requirements for data exchange between wind turbine controllers and remote SCADA systems to enable vendor-independent interoperability.

- **In scope**:
  - Data transfer and handling between wind turbine controllers and SCADA systems.
  - Support for both single turbines and wind farms.
  - Operational functions like supervision, control, and alarm management.
  - System management functions including configuration and time synchronization.
  - Communication security, reliability, and performance requirements.

- **Out of scope**:
  - SCADA system specifications, HMI design, or control algorithms.
  - Local functionality like temporary PC hook-ups or internet access.
  - Voice and visual communication (e.g., telephony, video).
  - Actor-specific functions unrelated to wind plant operation.
  - Safety-critical functions dependent on communication.

- **Roles and core use cases**:
  - As a wind turbine operator, I want to monitor and control turbines remotely so that I can optimize production and maintenance.
  - As a system administrator, I want to manage communication configurations so that the network remains secure and reliable.
  - As a maintenance technician, I want to retrieve historical data and alarms so that I can diagnose and resolve issues efficiently.

- **Success metrics**:
  - Overall transfer time for time-critical functions under 0.5 seconds.
  - System availability with minimal disruption during communication faults.
  - Support for redundant communication channels to prevent data loss.

- **Major constraints**:
  - Must operate in harsh environmental conditions (temperature, moisture, vibration).
  - No reliance on communication for safety functions; these must be self-contained.
  - Compatibility with existing systems via gateways.
  - Use of open, standardized protocols and interfaces.
  - Timestamp accuracy of at least 10 ms for all time-tagged data.

- **Undecided issues**:
  - Specific protocol recommendations (e.g., OPC, IEC 60870, IEC 61850).
  - Encryption methods for data confidentiality.
  - Exact redundancy requirements for physical media.
  - Not mentioned: Final selection of network topology.
  - Not mentioned: Detailed data list implementations beyond examples.