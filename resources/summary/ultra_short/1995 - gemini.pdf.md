**Purpose & Scope**
The system is the control and data acquisition software for the Gemini 8-meter Telescopes. Its purpose is to enable the efficient acquisition of astronomical data by controlling the telescope, its instruments, and auxiliary systems. It does not cover commercial or public-domain software used, except for defining the required interfaces to such software.

**Product Background / Positioning**
This software is the core control system for the Gemini telescopes. It logically follows the project's Operational Concepts document and is intended for developers of control systems, not the end-user astronomers. It integrates with and controls telescope hardware, instruments, and must interface with external systems like archives and data reduction packages.

**Core Functional Overview**
1.  Support multiple observing modes: interactive, queue-based, remote, and service observing.
2.  Provide a scheduler and sequencer to execute pre-programmed science observations with minimal human interaction.
3.  Enable remote operations, including monitoring, control, and diagnostics from designated off-site facilities.
4.  Control and coordinate multiple instruments mounted on the telescope concurrently, with one active at a time.
5.  Acquire, compress, store, and transmit astronomical detector data and engineering data.
6.  Maintain a system-wide database of telescope and instrument parameters and status.
7.  Implement comprehensive fault notification, logging, and recovery procedures.

**Key Users & Usage Scenarios**
*   **Astronomer:** Uses the system to collect data. Interacts via a sequencer/scheduler, not direct control.
*   **Science Observer:** On-site personnel monitoring data acquisition and integrity.
*   **Telescope Operator:** On-site controller with direct command privileges for telescope and instruments during observations.
*   **Support/Developer:** Personnel responsible for maintenance, testing, and software development, with high-level system access.
Typical scenarios include executing a queued observing program, an astronomer remotely monitoring an observation, and an operator conducting maintenance during daylight hours.

**Major External Interfaces**
*   **User Interfaces:** Must provide a homogeneous "look and feel" across subsystems, portable across hardware platforms, and network transparent.
*   **Hardware Interfaces:** Standard interfaces (e.g., VME) and software skeletons for control electronics and embedded microprocessors.
*   **Software Interfaces:** Interfaces to external software including quick-look analysis packages (e.g., PV-Wave/IDL), archive systems (STARCAT), star catalogs, and commercial DBMS.
*   **Communication Interfaces:** LAN/WAN based on standard protocols (TCP/IP). Internal networks include a control LAN, a time distribution bus, and specialized data buses.

**Key Non-functional Requirements**
*   **Performance:** System must support up to 6 active control nodes and 2 monitoring nodes simultaneously. Command acceptance/rejection within 2 seconds. Local status display updates within 4 seconds.
*   **Reliability/Availability:** Goal of 1-2% total system downtime. Recovery/reconfiguration from an error condition within 5 minutes.
*   **Data Capacity:** System must retain 7 days of data from the largest instrument, with the last 3 days available interactively from disk.
*   **Security:** Protection against unauthorized access and intrusion, particularly from the WAN. Security based on user privileges and operational levels.
*   **Maintainability:** All software must be modular, documented, and version-controlled. Subsystems must include self-test and simulation modules.

**Constraints, Assumptions & Dependencies**
*   Must use commercial and public-domain software where feasible.
*   Development must use defined standards: UNIX (POSIX), X-windows, Tcl/Tk, VxWorks on IOCs, and the EPICS toolkit.
*   Dependent on the definition of external standards (e.g., for detector data storage and transfer links), which are listed as unresolved action items.
*   Assumes sufficient hardware bandwidth is available to support remote operations functionality.
*   Software must be portable and hardware-independent where possible.

**Priorities & Acceptance Approach**
Interactive observing is the top-priority mode and must be implemented first. Queue-based observing is the primary intended operational mode. Acceptance will involve formal testing against specified performance criteria (response times, capacity), reliability measures, and the execution of built-in test procedures for all modules. System must demonstrate support for all required observing modes and user roles.