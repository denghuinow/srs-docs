**Purpose & Scope**  
The Gemini Control System software manages telescope and instrument control for the Gemini 8-meter Telescopes project. It enables efficient astronomical data acquisition through multiple observing modes, supporting both on-site and remote operations. The system does not handle scientific data analysis or telescope mechanical maintenance.

**Product Background / Positioning**  
Built on EPICS (Experimental Physics and Industrial Control System), the system integrates telescope control, instrument management, and data acquisition across two telescopes. It serves as the operational backbone for the Gemini project, interfacing with commercial software, star catalogs, and external instruments.

**Core Functional Overview**  
- Telescope and instrument control across observing, maintenance, and test operational levels  
- Support for queue-based observing as primary operational mode  
- Multi-user access with privilege-based security across remote sites  
- Data acquisition, storage, and transmission in FITS format  
- Fault tolerance with 5-minute recovery goal from error detection  
- Visitor instrument interface providing status, observing sequences, and telescope offset  
- Remote operations capability from partner sites with varying bandwidth  

**Key Users & Usage Scenarios**  
Astronomers submit observation programs via queue-based system; science observers validate data integrity. Telescope operators manage real-time control during observations. Support staff handle maintenance and diagnostics. Developers work at test level for system upgrades. Remote users access system from partner sites with bandwidth-dependent capabilities.

**Major External Interfaces**  
User interfaces include command line (CLUI) and graphical (GUI) tools. Hardware interfaces connect to control electronics via VME systems. Software interfaces support EPICS, FITS data format, STARCAT star catalogs, and commercial databases. Communication uses TCP/IP over LAN/WAN.

**Key Non-functional Requirements**  
System availability ≤15 minutes per night (2% downtime). Command response time ≤2 seconds. LAN data transfer rate 20-40 Mbits/second. System retains 7 days of data with last 3 days available interactively. Fault recovery completed within 5 minutes of error detection.

**Constraints, Assumptions & Dependencies**  
Must use EPICS as foundational control system. Hardware must meet altitude/humidity specifications. Remote operations capability depends on site bandwidth. No full redundancy required; only cost-effective redundancy implemented. Software must be POSIX-compliant UNIX-based.

**Priorities & Acceptance Approach**  
Highest priority: Queue-based observing capability. Critical: Remote operations and fault recovery. Acceptance criteria: Meeting availability, response time, and recovery requirements. Testing includes component, integration, and system-level validation.