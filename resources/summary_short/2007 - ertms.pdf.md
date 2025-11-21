# Short Summary

- **Background and objectives**: This document defines the functional requirements for the European Rail Traffic Management System / European Train Control System (ERTMS/ETCS), primarily focusing on operational needs to enable safe train movement and supervision across European railways.

- **In scope**:
  - Definition of ETCS application levels (0, 1, 2, 3, STM) and their interoperability.
  - Supervision of train movements, including speed, distance, and operational states.
  - Driver-machine interface (DMI) requirements for displaying ETCS information.
  - Compatibility with existing national train control systems via STM.
  - Functions for handling failures, transitions, and special operations (e.g., shunting, reversing).

- **Out of scope**:
  - Detailed technical specifications and data structures (deferred to SRS).
  - Driver training procedures and curriculum.
  - Environmental specifications and RAMS (Reliability, Availability, Maintainability, Safety) details.
  - Specific implementation processes for national systems.
  - Non-ETCS system failures and external incident management.

- **Roles and core use cases**:
  - As a **Driver**, I want to receive clear speed and movement authority information so that I can operate the train safely and efficiently.
  - As a **Railway Operator**, I want ETCS to supervise train movements and enforce safety rules so that rail traffic is managed reliably across borders.
  - As a **Maintenance Technician**, I want fault indications and recorded data so that I can diagnose and address system issues promptly.

- **Success metrics**:
  - ETCS functionality up to 500 km/h train speed.
  - Seamless transitions between application levels and operational states without safety compromise.
  - Compliance with mandatory (M) requirements in all ETCS applications.

- **Major constraints**:
  - Mandatory (M) requirements must be implemented in every ETCS application.
  - Optional (O) functions may be required under specific CCS TSI conditions.
  - Use of harmonised default values where national values are unavailable.
  - On-board equipment must perform self-test at start-up without driver action.
  - Train data must be entered before movement is permitted.

- **Undecided issues**:
  - Not mentioned
  - Not mentioned
  - Not mentioned
  - Not mentioned
  - Not mentioned