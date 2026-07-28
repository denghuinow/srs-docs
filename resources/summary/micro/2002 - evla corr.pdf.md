**Purpose & Scope**: The system provides the physical link between the WIDAR Correlator hardware and the EVLA monitor & control system for configuration, operation, and servicing.

**Core Functions**:
*   Translate configuration data from the EVLA M&C system into physical correlator hardware configuration.
*   Monitor correlator and subsystem health and autonomously recover from hardware and computing system faults where possible.
*   Process and transfer dynamic control data and monitor data.

**Key Constraints**:
*   The system is a critical component; its unavailability results in loss of incoming astronomical data.
*   The interface between the MCCC and external EVLA M&C networks shall be Ethernet of 100 Mbits/sec or better.
*   The system must be self-monitoring and capable of automatic recovery from processor failures, OS crashes, and internal communications failures.