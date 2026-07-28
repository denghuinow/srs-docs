**Purpose & Scope**: This document defines the operational requirements for the Gemini Control System software, which controls the Gemini 8-meter telescopes and their instruments for astronomical data acquisition.

**Core Functions**:
*   Support multiple observing modes (interactive, queue-based, remote, service).
*   Provide a virtual telescope simulator for science planning and testing.
*   Acquire, store, and transfer astronomical data in FITS format.

**Key Constraints**:
*   Must use the EPICS toolkit and VxWorks real-time OS for Input/Output Controller (IOC) subsystems.
*   All software must be developed using standard methodologies and a version control system (CVS).
*   Must support remote operations from multiple facility types, with functionality limited by communication link bandwidth.