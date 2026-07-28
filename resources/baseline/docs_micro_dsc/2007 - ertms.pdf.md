# Software Requirements Specification (SRS)
## European Train Control System (ETCS) On-Board Unit (OBU)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the European Train Control System (ETCS) On-Board Unit (OBU). The primary purpose is to specify the software needed to supervise train and shunting movements safely across interoperable application levels, ensuring compatibility and safety across European rail networks.

#### 1.2 Scope
This specification covers the core software functionalities of the ETCS OBU, including driver information display, movement supervision, speed and distance monitoring, braking curve calculation, and multi-level application management. The system must operate seamlessly across ETCS Application Levels 0, 1, 2, 3, and STM (Specific Transmission Module), maintaining backward compatibility. The scope is limited to the on-board equipment software; trackside equipment and communication protocols are referenced only for interface definitions.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ETCS:** European Train Control System
*   **OBU:** On-Board Unit
*   **STM:** Specific Transmission Module
*   **MA:** Movement Authority
*   **SRS:** Software Requirements Specification (this document)
*   **RBC:** Radio Block Centre
*   **Euroloop / Eurobalise:** Trackside transmission equipment
*   **FS:** Functional Safety
*   **SIL:** Safety Integrity Level (per EN 50128/50129)
*   **Interoperability:** The ability of the system to function with different national rail systems without modification.

#### 1.4 References
*   ERA_ERTMS_015560: ERTMS/ETCS System Requirements Specification
*   EN 50128: Railway applications - Software for railway control and protection systems.
*   EN 50129: Railway applications - Safety related electronic systems for signalling.
*   CCS TSI: Control-Command and Signalling Technical Specification for Interoperability.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product and its operating environment. Section 3 details all specific requirements, including functional, interface, performance, safety, and design constraints.

### 2. Overall Description

#### 2.1 Product Perspective
The ETCS OBU is a mission-critical, safety-related software component embedded within the train's integrated control and protection system. It interfaces with:
*   **Trackside Systems:** Via GSM-R (Level 2/3), Eurobalise/Euroloop (Level 1), or STM for national systems.
*   **On-Board Systems:** Driver Machine Interface (DMI), Juridical Recording Unit (JRU), odometry/speed sensors, brake interface unit.
*   **Legacy Systems:** National ATP systems through the STM interface.

The system acts as a supervisory layer, providing permissive signals to the driver and initiating automatic emergency braking if safety limits are breached.

#### 2.2 Product Functions
The high-level functions of the ETCS OBU software are:
1.  **Movement Supervision:** Continuously monitor train position and speed against a granted Movement Authority (MA).
2.  **Speed Profile Management:** Calculate, display, and enforce dynamic speed profiles, including braking curves (Service Brake and Emergency Brake Intervention Curves).
3.  **Driver Information:** Present clear, unambiguous information to the driver via the DMI regarding target speed, permitted speed, distance-to-go, and system status.
4.  **Level Management:** Seamlessly manage transitions between ETCS application levels and national systems (via STM).
5.  **Safety Enforcement:** Automatically initiate a guaranteed train stop if the driver does not respect a critical safety intervention (e.g., overspeed).
6.  **Start-Up Self-Test:** Perform a comprehensive automatic integrity check of the OBU hardware and software upon system initialization.

#### 2.3 User Characteristics
*   **Train Driver:** Primary operator. Uses the DMI for information. Requires no detailed knowledge of internal system operation.
*   **Maintenance Technician:** Configures system parameters, retrieves data from the JRU, and performs diagnostics. Requires specialized training.
*   **Safety Assessor:** Reviews system logs and safety evidence. Requires expertise in railway safety standards.

#### 2.4 Constraints
*   **Performance:** Must correctly process data and execute supervision logic for train speeds **up to 500 km/h**.
*   **Compatibility:** Must operate concurrently with existing national train control systems **without mutual interference** when in STM or mixed-mode operation.
*   **Operational:** The on-board equipment **must perform an automatic self-test at start-up** before the system becomes operational.
*   **Regulatory:** Must comply with the relevant TSI (CCS) and CENELEC standards (EN 50128, SIL 2/3/4 as applicable).

#### 2.5 Assumptions and Dependencies
*   Accurate and reliable odometry/speed sensor input is assumed.
*   Trackside infrastructure (balises, RBC, GSM-R network) is assumed to be available and functioning correctly for the respective level.
*   The underlying real-time operating system and hardware platform provide the necessary determinism and performance.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Movement Authority Supervision (FUN-MA)
*   **FUN-MA-001:** The system shall acquire, decode, and validate Movement Authority data from the trackside (via RBC, Eurobalise, or STM).
*   **FUN-MA-002:** The system shall continuously calculate the train's most restrictive safe front position (MRSP) based on the MA, track profile, and train characteristics.
*   **FUN-MA-003:** The system shall supervise the remaining distance to the end of the MA (EoA) and provide continuous distance-to-go information to the DMI.

##### 3.1.2 Speed Supervision & Braking Curve Calculation (FUN-SP)
*   **FUN-SP-001:** The system shall calculate two independent braking curves:
    *   **Service Brake Intervention Curve (SBIC):** The point at which the driver must begin braking to stop at the target.
    *   **Emergency Brake Intervention Curve (EBIC):** The point at which the system will automatically apply the emergency brake if the driver has not responded.
*   **FUN-SP-002:** The system shall supervise the current train speed against the permitted speed profile (PBP, CSP, etc.) and the calculated braking curves.
*   **FUN-SP-003:** If the train speed exceeds the EBIC, the system shall immediately and irrevocably trigger an emergency brake application.

##### 3.1.3 Driver Machine Interface (FUN-DMI)
*   **FUN-DMI-001:** The system shall provide a standardized interface to the DMI for displaying, at a minimum: current speed, target speed, permitted speed, distance-to-go, and system mode/level.
*   **FUN-DMI-002:** The system shall provide audible and visual warnings to the driver upon approaching the SBIC.
*   **FUN-DMI-003:** All displayed information shall be unambiguous and conform to ERA DMI specifications.

##### 3.1.4 Level Management & Interoperability (FUN-LVL)
*   **FUN-LVL-001:** The system shall be capable of operating in ETCS Application Levels 0, 1, 2, 3, and in STM mode.
*   **FUN-LVL-002:** The system shall manage transitions between levels (e.g., Level 1 to Level 2) without loss of safety or MA.
*   **FUN-LVL-003:** When operating with an STM, the system shall process national system data and supervise the train accordingly, while preventing interference between the ETCS and national system logic.

##### 3.1.5 System Integrity & Start-Up (FUN-SYS)
*   **FUN-SYS-001:** Upon application of power (start-up), the OBU shall perform an **automatic self-test** covering critical hardware components (CPU, memory, communication interfaces) and core software integrity.
*   **FUN-SYS-002:** The system shall only transition to an operational state if the self-test completes successfully. Any failure shall be reported and the system shall remain in a safe, restrictive state.
*   **FUN-SYS-003:** The system shall continuously perform runtime monitoring (watchdog, code checksum) to detect latent faults.

#### 3.2 Interface Requirements

##### 3.2.1 External Hardware Interfaces (IF-HW)
*   **IF-HW-001:** Odometry Interface: Shall accept inputs from multiple, redundant speed and distance sensors (e.g., tachometers, radar).
*   **IF-HW-002:** Brake Interface: Shall provide a fail-safe output signal to trigger the train's emergency braking system.
*   **IF-HW-003:** DMI Interface: Shall communicate via a defined serial or network protocol (e.g., Euroradio FFFIS).

##### 3.2.2 Communication Interfaces (IF-COM)
*   **IF-COM-001:** GSM-R Interface (Level 2/3): Shall implement the Euroradio protocol stack for communication with the RBC.
*   **IF-COM-002:** Balise Transmission Module Interface (Level 1): Shall decode telegrams from Eurobalises.
*   **IF-COM-003:** STM Interface: Shall provide a standardized interface for connecting vendor-specific STMs for national systems.

#### 3.3 Performance Requirements
*   **PER-001:** All critical supervision calculations (position, speed, braking curves) shall be updated and evaluated with a maximum cycle time of **1 second**.
*   **PER-002:** The system shall be capable of processing balise telegrams correctly when passing at speeds up to **500 km/h**.
*   **PER-003:** The reaction time from detection of an EBIC violation to the activation of the emergency brake output shall be less than **500 ms**.

#### 3.4 Safety & Reliability Requirements
*   **SAF-001:** The system shall be developed to a Safety Integrity Level (SIL) as defined in EN 50128, commensurate with the highest safety-related function (likely SIL 2 or higher).
*   **SAF-002:** The design shall ensure fail-safe operation. Any detected internal failure shall lead to a restrictive output (e.g., trigger emergency brake or enforce a zero Movement Authority).
*   **SAF-003:** The software shall include protection against common cause failures and shall be designed for high availability (>99.99%).

#### 3.5 Design Constraints
*   **CON-001:** The software shall be designed for a real-time, deterministic execution environment.
*   **CON-002:** The software architecture shall clearly separate safety-critical and non-safety-critical functions.
*   **CON-003:** The design shall allow for the independent certification of core ETCS functions and STM integration functions.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Author | | | |
| Reviewer | | | |
| Approver | | | |