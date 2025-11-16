# Short Summary

- **Background and objectives**: The EVLA Correlator Monitor & Control System provides the physical link between the WIDAR Correlator hardware and the EVLA monitor & control system, enabling configuration, operation, and servicing of the correlator. Its primary goal is to ensure reliable, real-time monitoring, control, and autonomous recovery for astronomical data processing.

- **In scope**:
  - Receive and translate configuration data from EVLA M&C into correlator hardware setup.
  - Process and transfer dynamic control and monitor data.
  - Monitor correlator health and perform autonomous recovery from faults.
  - Provide real-time data processing tools like auto-correlation display.
  - Enable remote system access for testing and debugging.

- **Out of scope**:
  - Not mentioned.
  - Not mentioned.
  - Not mentioned.
  - Not mentioned.
  - Not mentioned.

- **Roles and core use cases**:
  - As an Array Operator, I want to receive status and error messages through the M&C system so that I can monitor correlator operations.
  - As an Engineer/Technician, I want remote access to inspect and troubleshoot CMIB devices so that I can perform rapid diagnosis and repair.
  - As a Software Developer, I want remote system access for troubleshooting so that I can ensure software functionality during non-working hours.

- **Success metrics**:
  - System meets all real-time processing deadlines without data loss or corruption.
  - Correlator operates with high reliability and minimal downtime.
  - System autonomously recovers from hardware and software faults.

- **Major constraints**:
  - The system is critical to the astronomical data path; unavailability results in data loss.
  - Hardware and network stability are essential for reliability and availability.
  - Software must provide full access and high data integration for a coherent user interface.
  - System must support modular, hot-swappable components for serviceability.
  - Must comply with Ethernet and physical standards (e.g., PC104+ for CMIB).

- **Undecided issues**:
  - Actions for CPCC hard failures are TBD.
  - Specific delay for standby mode resumption is TBD.
  - Not mentioned.
  - Not mentioned.
  - Not mentioned.