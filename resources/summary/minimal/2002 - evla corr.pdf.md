**Purpose & Scope**: The system provides the physical link and primary interface between the WIDAR Correlator hardware and the EVLA monitor & control system for configuration, operation, and servicing.

**Core Functions**:
*   Translate EVLA M&C configuration data into physical correlator hardware configuration.
*   Process and transfer dynamic control data and monitor data.
*   Monitor correlator and subsystem health and autonomously recover from faults where possible.

**Key Users**: Array Operators, Engineers and Technicians, Software Developers.

**Key Constraints**:
*   The system is a critical component; its unavailability results in loss of incoming astronomical data.
*   Interfaces shall use Ethernet (IEEE 802.3 compliant) at 100 Mbits/sec or better.
*   The MCCC to EVLA M&C network pathway penetrating the shielded room shall be fiber optic.