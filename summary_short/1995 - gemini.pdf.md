# Short Summary

- **Background and objectives**: This document defines the operational requirements for the Gemini Control System software, aiming to guide development of controls and data acquisition systems consistent with Gemini System operation. It establishes general criteria and specific functional requirements for software and controls design.

- **In scope**:
  - Control and data acquisition systems for telescope and instruments
  - Remote operations capabilities including monitoring and diagnostics
  - Multiple observing modes (interactive, queue-based, service)
  - User interfaces and access control systems
  - Data flow specifications and archiving requirements

- **Out of scope**:
  - Commercial software packages used but not developed for control
  - Embedded software without software interfaces to Gemini system
  - External user-supplied data reduction tools
  - Hardware-specific embedded control software
  - Off-line data reduction facilities

- **Roles and core use cases**:
  - As an Astronomer, I want to collect science data efficiently so that I can focus on data quality assessment rather than control details
  - As a Telescope Operator, I want to control telescope and instruments so that I can ensure system integrity during observations
  - As a Developer, I want to design and test subsystems so that I can maintain and upgrade the control system

- **Success metrics**:
  - System availability with maximum 15 minutes downtime per night
  - Command acceptance/rejection within 2 seconds
  - Support for up to 6 active control nodes simultaneously
  - Data retention of 7 days from largest instrument

- **Major constraints**:
  - Use commercial packages and standards whenever feasible
  - All software must be version controlled and documented
  - Hardware independence for non-IOC software
  - Network transparency for remote operations
  - EPICS as foundation for control system

- **Undecided issues**:
  - Standard for acquisition and storage of detector data
  - Link chosen to transfer data
  - Desirable hardware specification
  - Standards for online software and development environment
  - Supportability plan