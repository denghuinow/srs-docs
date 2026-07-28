# Software Requirements Specification (SRS)
## Electronic Logbook Software System (ELSS) for UK Fishing Vessels

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional requirements for an Electronic Logbook Software System (ELSS) mandated for use on UK-registered fishing vessels exceeding 15 meters in overall length. Its purpose is to provide a complete, unambiguous specification for software developers (Suppliers) to create a system that complies with UK and EU fisheries regulations, enabling the secure recording and electronic transmission of fishing activity data to UK Fisheries Administrations.

#### 1.2 Document Conventions
*   **Requirements:** Functional requirements are uniquely identified with the label `FR-XXX`.
*   **Keywords:** The words "MUST", "MUST NOT", "SHALL", "SHALL NOT", "REQUIRED", and "WILL" indicate mandatory requirements as per regulatory compliance.
*   **Formatting:** Code and data examples are presented in `monospace` font. XML elements are denoted with angle brackets (e.g., `<Report>`).

#### 1.3 Intended Audience and Reading Suggestions
*   **ELSS Suppliers/Developers:** Primary audience. Should read the entire document.
*   **UK Fisheries Administrations:** Regulatory body. Focus on Sections 1, 2, 3, and 5.
*   **Vessel Owners & Masters:** End-users. Focus on Section 3 (Specific Requirements) for understanding system capabilities and constraints.
*   **Quality Assurance & Testers:** Focus on Section 3 to derive test cases.

#### 1.4 Project Scope
The ELSS is an onboard software application for recording fishing operations (catches, effort, transhipments, landings) and generating standardized XML reports for transmission to the UK's Electronic Recording and Reporting System (ERS). The system replaces the paper logbook and ensures timely, accurate, and secure data submission as required by law.

**In-Scope:**
*   Onboard data entry, validation, storage, and management of fishing trip data.
*   Generation of UK-specific XML messages for all mandatory report types and operations.
*   Secure transmission of encrypted XML reports via email.
*   User authentication, role-based access control, and electronic signing of reports.
*   Receipt, parsing, and storage of system acknowledgements.

**Out-of-Scope:**
*   Onshore use of the ELSS by agents, buyers, or port authorities.
*   The central ERS infrastructure and web interfaces operated by the UK Fisheries Administrations.
*   Internal software architecture, database design, or programming language selection (supplier-defined).
*   Localization for languages other than English (UK) or time zones other than UTC.

#### 1.5 References
1.  Council Regulation (EC) No 1966/2006 - Electronic recording and reporting of fishing activities.
2.  Commission Regulation (EC) No 1077/2008 - Detailed rules for the implementation of Council Regulation (EC) No 1966/2006.
3.  UK Fisheries Administrations - *Electronic Logbook Technical Specification vX.X* (Defining XML schemas, data dictionaries, and validation rules).
4.  UK Fisheries Administrations - *Product Profile Questionnaire for ELSS Approval*.

### 2. Overall Description

#### 2.1 Product Perspective
The ELSS is a standalone onboard system. Its primary external interactions are:
*   **Input:** Manual data entry from crew, and optionally, automated data from vessel sensors (GPS, gear sensors).
*   **Output:** Encrypted PGP email attachments containing XML reports sent to a designated UK ERS email address.
*   **Input:** Inbound emails containing XML acknowledgements from the UK ERS.
*   **Environment:** Must operate reliably in a marine environment with potential for limited or intermittent internet connectivity.

#### 2.2 Product Functions (Summary)
*   **User Management:** Create, modify, and disable user accounts with defined roles (Master, Crew).
*   **Trip Management:** Create, view, and manage fishing trip records.
*   **Data Entry & Validation:** Provide forms for entering catch, effort, transhipment, and landing data with real-time validation against UK data rules.
*   **Report Generation:** Construct and validate XML messages for Departure, Fishing Activity (Logbook), Transhipment, and Landing reports.
*   **Report Operations:** Support for three operations per report type: `Data` (new), `Correction`, and `Deletion`.
*   **Data Transmission:** Encrypt, send, and queue outgoing reports via email. Manage transmission schedules (daily, event-based).
*   **Acknowledgement Handling:** Receive, decrypt, parse, and store inbound acknowledgements, linking them to original reports.
*   **Printing:** Generate human-readable printouts of logbook entries and reports.
*   **Data Retention:** Securely store all data, reports, and transmissions for a minimum period as defined by regulation.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Vessel Master** | Ultimate authority onboard. Legally responsible for logbook accuracy. Not necessarily technically adept. | Final review and electronic signing of all reports. Managing user access for crew. Initiating transmissions. |
| **Onboard Crew (Authorized User)** | Assigned by the Master. Variable levels of technical skill. | Entering daily catch and fishing activity data. Preparing draft reports. |
| **Vessel Owner / Manager** | May not be physically onboard. Responsible for system procurement and setup. | Initial system configuration (vessel details). Creating the Master's user account. |
| **System Administrator (Supplier Role)** | Highly technical. | Initial software installation, configuration, and potential troubleshooting. |

#### 2.4 Operating Environment
*   **Hardware:** Must run on standard PC hardware suitable for the marine environment.
*   **Software:** Must operate on a common operating system (e.g., Windows, Linux). Must include or interface with a PGP encryption tool and an email client/service.
*   **Connectivity:** Must function with intermittent satellite-based email connectivity.
*   **Localization:** All user interfaces MUST be in English (UK). All dates and times MUST be displayed, entered, and transmitted in Coordinated Universal Time (UTC).

#### 2.5 Design and Implementation Constraints
1.  **Regulatory Compliance:** The system SHALL implement data validation and business logic as specified in the UK Technical Specification, derived from EU Regulations 1966/2006 and 1077/2008.
2.  **Data Format:** All transmitted reports SHALL be valid XML conforming to the published UK XML schemas.
3.  **Security:** All reports containing fishing activity data SHALL be encrypted using PGP before transmission via email.
4.  **Transmission Schedule:** The system SHALL be capable of transmitting reports at least once per calendar day by 24:00 UTC, and immediately upon the occurrence of reportable events (e.g., port departure, fishing operation completion).
5.  **Onboard Restriction:** The software SHALL be designed for use exclusively at sea on the vessel for which it is configured. It SHALL NOT be used from onshore locations.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** The vessel will have a means of sending and receiving email while at sea.
*   **Assumption:** The user (Master/Crew) has been trained in basic software operation and data entry principles.
*   **Dependency:** The UK Fisheries Administrations will maintain a stable ERS email gateway and provide valid PGP public keys for encryption.
*   **Dependency:** Approval of the software is contingent on successful completion of the official Product Profile questionnaire and validation testing by the UK Fisheries Administrations.

### 3. System Features and Requirements

#### 3.1 User Management & Authentication
**Description:** This feature controls access to the ELSS through unique user accounts and enforces role-based permissions.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-010** | The system SHALL require user authentication via a unique username and password to access any functionality beyond a login screen. | High |
| **FR-011** | The system SHALL support at least two user roles: **Master** and **Crew**. | High |
| **FR-012** | A user with the **Master** role SHALL be able to: create, modify, enable, and disable accounts for **Crew** users. | High |
| **FR-013** | A **Crew** user SHALL ONLY be able to enter and save logbook data and prepare draft reports. They SHALL NOT be able to electronically sign or transmit reports. | High |
| **FR-014** | The **Master** user SHALL be required to provide an electronic signature (e.g., re-entering password) to finalize and sign any report (`Data`, `Correction`, `Deletion`) before it can be transmitted. | High |
| **FR-015** | User passwords SHALL adhere to a configurable security policy (minimum length, complexity). | Medium |

#### 3.2 Trip and Logbook Data Management
**Description:** This feature allows users to create fishing trips and record daily catch and fishing effort data.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-020** | The system SHALL allow the Master to create a new Fishing Trip record, including mandatory data: Vessel ID, Departure Port, and Departure Date/Time. | High |
| **FR-021** | The system SHALL provide data entry screens for daily **Fishing Operations**, including: gear type, mesh size, target species, catch quantities (by species), and fishing effort data (location, date/time). | High |
| **FR-022** | The system SHALL validate all entered data in real-time against the rules and code lists in the UK Technical Specification (e.g., valid species codes, gear codes, location formats). | High |
| **FR-023** | The system SHALL conditionally display data fields based on context (CIF - Conditional Information). For example, specific fields SHALL only be required if the fishing activity occurs in Norwegian waters. | High |
| **FR-024** | The system SHALL allow for the entry of **Transhipment** declarations (catch received from or given to another vessel) and **Landing** declarations. | High |
| **FR-025** | The system SHALL allow a user to print a human-readable version of any logbook entry or declaration. | Medium |

#### 3.3 Report Generation & XML Output
**Description:** This feature constructs, validates, and prepares XML reports for transmission.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-030** | The system SHALL generate XML reports for the following types: `DEP` (Departure), `FAR` (Fishing Activity), `TRA` (Transhipment), `LAN` (Landing). | High |
| **FR-031** | For each report type, the system SHALL support three operations: `DAT` (Data - new report), `COR` (Correction), `DEL` (Deletion). | High |
| **FR-032** | The generated XML MUST strictly conform to the structure, element names, and data types defined in the official UK XML schemas. | High |
| **FR-033** | The system SHALL perform schema validation on the generated XML before allowing it to be signed or transmitted. | High |
| **FR-034** | Each report SHALL include a unique `ReportID` generated by the ELSS and the relevant `TripID`. | High |
| **FR-035** | For `COR` and `DEL` operations, the user SHALL be required to specify the `ReportID` of the original report being corrected or deleted. | High |

#### 3.4 Data Transmission
**Description:** This feature handles the secure, scheduled sending of reports to the UK ERS.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-040** | The primary transmission method SHALL be email. The system SHALL interface with an onboard email system to send messages. | High |
| **FR-041** | Before transmission, the system SHALL encrypt the XML report file using PGP encryption with the UK Fisheries Administrations' public key. | High |
| **FR-042** | The system SHALL attach the encrypted XML file to an email addressed to the designated UK ERS email gateway. | High |
| **FR-043** | The system SHALL allow the Master to trigger an immediate ("on-demand") transmission of any signed, pending report. | High |
| **FR-044** | The system SHALL provide an automated function to transmit all pending reports at least once per calendar day, by 24:00 UTC. | High |
| **FR-045** | If a transmission attempt fails (e.g., no connectivity), the system SHALL queue the report and retry according to a defined logic (e.g., at next scheduled send, when connectivity is detected). | High |
| **FR-046** | The system SHALL maintain a local transmission log recording the date/time, report ID, and status (Sent, Failed, Queued) for every transmission attempt. | High |

#### 3.5 Acknowledgement Processing
**Description:** This feature manages the reception and handling of automated acknowledgements from the UK ERS.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-050** | The system SHALL monitor a designated email inbox for incoming messages from the UK ERS. | High |
| **FR-051** | The system SHALL be able to decrypt incoming PGP-encrypted acknowledgement messages. | High |
| **FR-052** | The system SHALL parse the acknowledgement XML, extracting the referenced `ReportID` and the acknowledgement status (e.g., `ACK` for accepted, `REJ` for rejected with error details). | High |
| **FR-053** | The system SHALL clearly display the status of all transmitted reports (e.g., "Pending", "Received by ERS", "Rejected - Error: Invalid Species Code") to the user. | High |
| **FR-054** | For rejected (`REJ`) reports, the system SHALL present the error message to the user to facilitate correction. | High |

#### 3.6 System Configuration & Data Retention
**Description:** This feature handles initial setup and long-term data storage.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-060** | The system SHALL provide a configuration section, accessible only to a privileged user (Owner/Master/Installer), to enter and store static vessel data (e.g., CFR number, vessel name, registration port). | High |
| **FR-061** | The system SHALL retain all logbook data, generated reports, transmission logs, and acknowledgements locally for a minimum period of **three years** from the date of creation, or as otherwise mandated by regulation. | High |
| **FR-062** | The system SHALL provide a secure data export/backup function to protect against data loss. | Medium |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   All screens SHALL be in English (UK).
*   All date/time pickers SHALL display and input UTC.
*   Data entry forms SHALL provide clear labels, validation messages, and context-sensitive help where codes are used (e.g., hovering over a species field shows the code list).

#### 4.2 Hardware Interfaces (Optional)
*   The system MAY interface with onboard GPS/NMEA data to auto-populate position and time fields.
*   The system MAY interface with onboard weighing systems to auto-populate catch weight data.
*   *Note: Implementation of these interfaces is at the supplier's discretion and does not affect core compliance.*

#### 4.3 Software Interfaces
*   **Email Client/Service:** The system MUST be able to invoke the send/receive functions of a standard email application or service via API or command line.
*   **PGP Encryption Tool:** The system MUST integrate with a PGP tool (e.g., GnuPG) to perform encryption and decryption operations.

#### 4.4 Communications Interfaces
*   **Protocol:** SMTP for sending email, POP3/IMAP for receiving email.
*   **Data Format:** Outbound: PGP-encrypted XML file attachment. Inbound: PGP-encrypted XML acknowledgement file attachment.
*   **Address:** The destination email address SHALL be configurable but default to the official UK ERS gateway address.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   Data entry and screen navigation SHALL have a response time of less than 2 seconds under normal operating conditions.
*   The system SHALL be capable of generating and encrypting an XML report in under 30 seconds.

#### 5.2 Safety Requirements
*   Not applicable (software does not control physical vessel systems).

#### 5.3 Security Requirements
*   User passwords SHALL be stored in a hashed, non-reversible format.
*   Local data files SHALL be protected from casual inspection or modification by standard users.
*   The system SHALL not store the PGP private key passphrase in plain text.

#### 5.4 Software Quality Attributes
*   **Reliability:** The system MUST be capable of operating for extended periods (weeks) without restarting. Data loss due to unexpected shutdown (e.g., power loss) MUST be prevented.
*   **Usability:** The user interface MUST be intuitive for users with basic computer literacy. Training time for core data entry functions should not exceed 4 hours.
*   **Maintainability:** The supplier SHALL provide a mechanism to update the software (e.g., to incorporate new code lists or schema changes) subject to re-approval by the UK Fisheries Administrations.

### 6. Other Requirements

#### 6.1 Approval & Certification
*   The software product MUST successfully pass the validation process defined by the UK Fisheries Administrations, including submission of a completed Product Profile questionnaire.
*   Upon approval, the product will be listed on the Approved Product Register.

#### 6.2 Appendices
*   **Appendix A:** Glossary of Terms (e.g., CFR, ERS, PGP, CIF, UTC).
*   **Appendix B:** Mapping of User Stories to Functional Requirements.
*   **Appendix C:** References to full UK XML schemas and data dictionaries (provided as external documents).

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner (UK Fisheries Admin) | | | |
| Lead Developer (ELSS Supplier) | | | |
| Quality Assurance Manager | | | |