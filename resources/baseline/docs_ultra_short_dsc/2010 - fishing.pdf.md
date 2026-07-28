Here is a comprehensive Software Requirements Specification (SRS) document for the Electronic Logbook Software System (ELSS), structured according to professional standards and formatted in Markdown.

```markdown
# Software Requirements Specification (SRS)
## Electronic Logbook Software System (ELSS) for UK Fishing Vessels

**Document Version:** 1.0  
**Date:** [Date of Creation]  
**Status:** Draft / For Approval  
**Author:** [Author Name/Team]  
**Stakeholders:** UK Fisheries Administrations, Vessel Owners, Vessel Masters, Software Suppliers

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Electronic Logbook Software System (ELSS). The ELSS is a mandatory onboard software system for UK-registered fishing vessels over 15 meters in length, designed to replace paper logbooks. Its primary purpose is to capture, validate, and transmit fishing activity data electronically to the UK Fisheries Administrations' Electronic Recording and Reporting System (ERS) to ensure compliance with EU Council Regulation (EC) No. 1966/2006.

### 1.2 Scope
The scope of the ELSS includes:
*   Onboard data entry, validation, and management of fishing logbooks, transhipment declarations, and landing declarations.
*   Generation and encrypted transmission of 12 specific XML report types to the central ERS.
*   Management of report lifecycles (new, correct, delete).
*   User authentication and audit trail maintenance.
*   Printing of hard copies for onboard records.

**Out of Scope:**
*   Onshore data entry by agents or representatives (this must be performed via separate, approved ERS web or offline methods).
*   Vessel tracking or Vessel Monitoring System (VMS) functionality.
*   Business management functions (e.g., invoicing, crew payroll).

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **ELSS** | Electronic Logbook Software System. The subject of this SRS. |
| **ERS** | Electronic Recording and Reporting System. The central UK Fisheries Administrations' system that receives ELSS reports. |
| **XML** | eXtensible Markup Language. The standard format for data exchange. |
| **XSD** | XML Schema Definition. The schema against which ELSS XML reports must be validated. |
| **PGP** | Pretty Good Privacy. The encryption standard required for securing transmissions. |
| **UTC** | Coordinated Universal Time. The required time standard for all date/time data. |
| **DAT** | Data Report. A new report submission. |
| **COR** | Correction Report. A report correcting a previously sent DAT. |
| **DEL** | Deletion Report. A report deleting a previously sent DAT. |
| **RET** | Return Acknowledgement. An acknowledgement message received from the ERS. |
| **Vessel Master** | The captain or responsible person aboard the vessel who oversees fishing operations and data entry. |
| **Vessel Owner** | The legal owner of the vessel, responsible for system setup and user management. |

### 1.4 References
1.  EU Council Regulation (EC) No. 1966/2006 on electronic recording and reporting of fishing activities.
2.  UK Fisheries Administrations' ELSS Approval Programme Guidelines.
3.  UK ERS Interface Control Document (ICD) and XML Schema Definitions (XSDs).
4.  UK Fisheries Code Lists (e.g., species, gear types, ports).

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall product description. Section 3 details specific system requirements, including functional, external interface, and non-functional requirements. Section 4 covers constraints, assumptions, and dependencies.

## 2. Overall Description

### 2.1 Product Perspective
The ELSS is a standalone onboard software application that operates within a larger regulatory and technological ecosystem.
*   **Parent System:** The UK Fisheries Management regulatory framework.
*   **Interfaces:**
    *   **ERS (Primary):** Via email for sending encrypted XML reports and receiving RET acknowledgements.
    *   **Onboard Systems (Optional):** May interface with GPS, fish finders, or weighing systems to auto-populate data fields (e.g., position, catch weight).
    *   **Printer:** For generating mandatory hard copies.
    *   **Email Client:** For sending and receiving emails via the vessel's satellite/cellular communication system.

### 2.2 Product Functions
The core functions of the ELSS are:
1.  **User Management:** Secure authentication and role-based access (Owner, Master, Crew).
2.  **Data Capture:** Provide intuitive screens for entering logbook, transhipment, and landing data.
3.  **Data Validation:** Perform real-time validation against business rules and UK XSDs.
4.  **Report Generation:** Construct the 12 mandated XML report types from entered data.
5.  **Report Management:** Store, view, edit, and manage reports (DAT, COR, DEL) for the current fishing trip.
6.  **Secure Communication:** Encrypt (PGP) and transmit XML reports via email; receive and process RET acknowledgements.
7.  **Printing:** Generate legible hard copies of logbook and landing data.
8.  **Data Retention:** Securely store all reports and related data at least until the end of the fishing trip.

### 2.3 User Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Vessel Owner** | Technically capable; understands regulatory obligations. Has ultimate responsibility for compliance. | Initial system setup and configuration. Creation and management of user accounts (especially for the Vessel Master). |
| **Vessel Master** | Primary daily user. Expert in fishing operations but may have limited computer literacy. Works in a demanding, time-pressured environment at sea. | Daily data entry of fishing activities. Submitting departure, transhipment, and landing reports. Reviewing system acknowledgements. |
| **Crew Member** (Optional) | Assigned by the Master. May enter data under the Master's supervision. | Assisting with data entry for specific operations (e.g., catch details). |

### 2.4 Operating Environment
*   **Hardware:** Approved onboard computer system (marine-grade, resilient to shipboard conditions).
*   **Software:** Compatible operating system (e.g., Windows, Linux). Requires a functional email client and network connectivity.
*   **Physical:** Must be operable in the marine environment (variable lighting, motion, potential for moisture).
*   **Network:** Dependent on intermittent satellite or cellular connectivity for email transmission.

### 2.5 Design and Implementation Constraints
1.  **Regulatory:** The system's core data model, report types, and validation logic are strictly defined by the UK ERS XSDs and code lists. No deviation is permitted.
2.  **Platform:** Must be approved for use at sea on specific onboard systems.
3.  **Operational:** Corrections (COR) and deletions (DEL) can only be generated for reports from the **current** fishing trip, and only until an "End of Fishing" report is submitted.
4.  **Security:** Must implement PGP encryption as specified by the UK Fisheries Administrations.

### 2.6 Assumptions and Dependencies
*   **Assumption:** The fishing vessel has a functional onboard email system (e.g., satellite comms) capable of sending/receiving emails with attachments.
*   **Assumption:** The Vessel Owner and Master will receive adequate training to operate the ELSS.
*   **Dependency:** The UK Fisheries Administrations will maintain and provide access to the ERS, the definitive XML schemas (XSDs), and updated code lists. Any changes to these may require ELSS software updates.
*   **Dependency:** The system relies on the vessel's internal clock being set correctly to derive UTC timestamps.

## 3. System Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Management & Security (FUN-UC)
*   **FUN-UC-001:** The system shall require user authentication via a unique username and password to access all primary functions.
*   **FUN-UC-002:** The system shall allow a user with "Owner" role to create, modify, and disable user accounts for the "Master" and "Crew" roles.
*   **FUN-UC-003:** The system shall record the unique user ID of the person who creates or modifies a report within the XML data of that report.

#### 3.1.2 Data Entry & Validation (FUN-DE)
*   **FUN-DE-001:** The system shall provide data entry screens for all 12 mandated report types (e.g., Departure, Fishing Activity, Transhipment, Landing, End of Fishing).
*   **FUN-DE-002:** The system shall validate all entered data in real-time against the current UK ERS XSDs and code lists, providing clear error messages.
*   **FUN-DE-003:** The system shall, where possible, auto-populate fields from connected onboard systems (e.g., GPS for position, time).
*   **FUN-DE-004:** The system shall enforce that all dates and times are stored and transmitted in UTC format.
*   **FUN-DE-005:** The User Interface (UI) shall use English (UK) localization for all text, labels, and formats.

#### 3.1.3 Report Management (FUN-RM)
*   **FUN-RM-001:** The system shall allow the user to save a report as a draft before final submission.
*   **FUN-RM-002:** The system shall allow the user to generate a new report (DAT), a correction (COR) to a prior report, or a deletion (DEL) of a prior report.
*   **FUN-RM-003:** The system shall maintain a local database of all reports for the current fishing trip, accessible for view and correction.
*   **FUN-RM-004:** The system shall prevent the creation of COR or DEL reports for any report submitted prior to the current fishing trip.

#### 3.1.4 Communication & Transmission (FUN-COM)
*   **FUN-COM-001:** The system shall generate a valid XML file for any submitted report, compliant with the UK ERS XSD.
*   **FUN-COM-002:** The system shall encrypt the XML file using PGP encryption before transmission.
*   **FUN-COM-003:** The system shall transmit the encrypted XML file as an email attachment to the designated ERS email address. This shall be the primary transmission method.
*   **FUN-COM-004:** The system shall automatically trigger transmission at specified events (e.g., immediately after the last fishing operation of the day is entered, immediately upon creating a Departure report).
*   **FUN-COM-005:** The system shall receive email acknowledgements (RET) from the ERS, match them to the original sent report, and display the status (Accepted/Rejected) clearly to the user.
*   **FUN-COM-006:** The system shall store a local copy of both the sent XML and any received RET message.

#### 3.1.5 Printing (FUN-PRN)
*   **FUN-PRN-001:** The system shall generate a printable, human-readable hard copy of any logbook or landing declaration report.
*   **FUN-PRN-002:** The printed copy shall clearly display all key data, the report reference number, and the date/time of printing.

### 3.2 External Interface Requirements

#### 3.2.1 User Interfaces
*   **UI-001:** Graphical User Interface (GUI) shall be designed for clarity and ease of use under typical vessel conditions.
*   **UI-002:** All data entry screens shall follow a logical tab order and provide clear field labels and instructions.

#### 3.2.2 Hardware Interfaces
*   **HW-001:** The system shall support communication with standard serial/USB ports for integration with optional onboard equipment (GPS, scales).
*   **HW-002:** The system shall support output to a standard Windows/Linux compatible printer.

#### 3.2.3 Software Interfaces
*   **SI-001:** The system shall interface with the computer's default MAPI-compliant email client (e.g., Outlook) or have a built-in SMTP client configured by the user.
*   **SI-002:** The system shall integrate with the operating system's print spooler.

#### 3.2.4 Communication Interfaces
*   **CI-001:** The system shall communicate via standard internet protocols (SMTP, POP3/IMAP) for email transmission and reception.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PER-001:** Report transmission via email shall be initiated automatically within **5 seconds** of the triggering event (e.g., user finalizing a report with "Send Now" flag).
*   **PER-002:** The user interface shall respond to any user input (e.g., button click, field entry) within **2 seconds** under normal operating conditions.

#### 3.3.2 Safety & Security Requirements
*   **SEC-001:** All external XML transmissions **must** be encrypted using PGP. Use of unencrypted transmission is prohibited.
*   **SEC-002:** User passwords shall be stored in a hashed, non-reversible format.
*   **SEC-003:** The system shall log all user login attempts (success and failure) and major system events (transmission success/failure).

#### 3.3.3 Reliability & Availability
*   **REL-001:** The system shall have an uptime requirement of 99.5% during a fishing trip, excluding failures of underlying hardware or OS.
*   **REL-002:** The system shall retain all logbook reports and corrections in its local database at least until a successful "End of Fishing" report is submitted and acknowledged. Data shall be recoverable after an unexpected application shutdown.

#### 3.3.4 Maintainability & Support
*   **MAIN-001:** Software updates shall be possible without corrupting existing trip data.
*   **MAIN-002:** If a software update modifies the core data validation, transmission format, or encryption method, the updated product **must** be re-submitted for approval under the ELSS Approval Programme.

#### 3.3.5 Compliance Requirements
*   **COMP-001:** The system shall be fully compliant with the data requirements and validation rules specified in the UK ERS XSDs and associated documentation.
*   **COMP-002:** The system shall be developed and approved in accordance with the UK Fisheries Administrations' ELSS Approval Programme.

## 4. Appendices

### 4.1 Mandated Report Types
The system must generate the following 12 report types as per UK specification:
1.  Departure
2.  Fishing Activity
3.  Transhipment
4.  Landing
5.  End of Fishing
6.  [List all 12 as per official docs]

### 4.2 Acceptance Approach
Formal acceptance of the ELSS is not solely based on this SRS but is governed by the **ELSS Approval Programme**. Final acceptance requires:
1.  Completion of the supplier Product Profile questionnaire.
2.  Submission of a signed Self-Declaration Form by the supplier.
3.  Successful auditing and conformance testing by or on behalf of the UK Fisheries Administrations against the full regulatory specification, of which this SRS is a summary.
```