# Software Requirements Specification (SRS)
## Crime & Criminal Tracking Network and Systems (CCTNS) - Version 1.0

**Document Version:** 1.0  
**Date:** [Date of Issue]  
**Prepared for:** Ministry of Home Affairs, Government of India  
**Prepared by:** [Project Team/Consultant Name]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for Version 1.0 of the Crime & Criminal Tracking Network and Systems (CCTNS). It serves as the authoritative specification for developers, testers, project managers, and stakeholders, ensuring a common understanding of the system to be delivered.

#### 1.2 Scope
**In-Scope for V1.0:**
*   Automation of core police workflows for "Investigation of Crime" and "Detection of Criminals."
*   Citizen-facing interface for complaint (FIR) registration and status tracking.
*   Core modules: Crime Registration, Case Investigation, Prosecution Tracking, Advanced Search, and System Configuration.
*   State-level configurability for data elements and workflows.
*   Robust access control, audit logging, and security mechanisms.
*   Basic interfaces for future court system integration.

**Out-of-Scope for V1.0:**
*   Extensive, real-time integration with external judicial, prison, or other government systems.
*   Full nationwide data unification without state-specific configuration.
*   Mobile/PDA interface rollout.
*   Advanced analytics and predictive policing modules.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **CCTNS:** Crime & Criminal Tracking Network and Systems
*   **FIR:** First Information Report
*   **IO:** Investigating Officer
*   **MHA:** Ministry of Home Affairs
*   **SLA:** Service Level Agreement
*   **UAT:** User Acceptance Testing
*   **WCAG:** Web Content Accessibility Guidelines
*   **RTO:** Recovery Time Objective

#### 1.4 References
*   [List any governing policies, previous documents, or standards referenced]

#### 1.5 Overview
The remainder of this SRS is organized as follows: Section 2 provides an overall description of the product. Section 3 details specific system requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
CCTNS V1.0 is a state-configurable, web-based application designed to operate within a secure police intranet with a controlled external interface for citizens. It is a mission-critical system that must interact with users (police personnel, citizens, administrators) and will be designed to accommodate future integration with external systems (e.g., Courts).

#### 2.2 User Classes and Characteristics
| User Class | Primary Responsibilities | Key Characteristics |
| :--- | :--- | :--- |
| **Citizen/Complainant** | Register complaints, track case status. | External user, varying technical proficiency. Requires simple, guided interface. |
| **Records Room Staff** | Validate & formally register complaints, data entry. | Internal user. Requires efficient data capture and validation screens. |
| **Investigating Officer (IO)** | Conduct investigation, log actions/evidence, search for links. | Internal, mobile user. Needs quick data entry, offline capability, and powerful search. |
| **Prosecution Constable** | Record court hearings, judgments, and prosecution updates. | Internal user. Requires integration with case timeline. |
| **System Administrator** | Configure application, manage users/roles, maintain state data. | Technical internal user. Requires granular control and configuration tools. |
| **Help Desk/Support Staff** | Manage defect/enhancement tickets, provide user support. | Internal/External facing. Requires ticketing system access separate from main app. |

#### 2.3 Operating Environment
*   **Software:** Standard web browsers (Chrome, Firefox latest stable versions), Java/.NET application server, RDBMS (Oracle/PostgreSQL).
*   **Hardware:** Servers as per centralized/state data center specifications. Client machines in police stations.
*   **Network:** Secure police intranet (NICNET/state network) with controlled internet gateway for citizen portal. Must support low-bandwidth and offline operation scenarios.

#### 2.4 Design and Implementation Constraints
1.  **Security:** Must comply with MHA security policies. Data in transit must use HTTPS/SSL.
2.  **Accessibility:** User interfaces must comply with ISO 9241 and WCAG 1.0 guidelines.
3.  **Configurability:** Core data models and UIs must support state-specific customization without code changes.
4.  **Auditability:** An immutable audit trail for all critical actions is mandatory.
5.  **Legacy Data:** Must provide utilities for migration and validation of data from legacy records.

#### 2.5 Assumptions and Dependencies
*   Adequate network connectivity (with allowances for offline mode) will be available at police stations.
*   State police departments will provide timely inputs for state-specific configuration.
*   User training will be conducted prior to rollout.

### 3. System Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Crime Registration Module
*   **FR-REG-01:** The system shall provide a citizen portal for online submission of complaints (FIRs).
*   **FR-REG-02:** Upon valid submission, the system shall generate a unique reference number and an acknowledgement receipt for the citizen.
*   **FR-REG-03:** The system shall provide an interface for Records Room staff to review, validate, and formally register a complaint into a system Case.
*   **FR-REG-04:** During case registration, the system shall capture mandatory details: Complainant info, incident description, date/time, location, crime type.
*   **FR-REG-05:** The system shall allow a supervisor or Records staff to assign a registered case to an Investigating Officer (IO).

##### 3.1.2 Case Investigation Module
*   **FR-INV-01:** The system shall provide an interface for the IO to view all cases assigned to them.
*   **FR-INV-02:** The IO shall be able to log Investigation Actions (e.g., Site Visit, Witness Interview, Evidence Seizure) against a case. Each action must be timestamped and linked to the IO.
*   **FR-INV-03:** The system shall allow the IO to record Evidence details (Type, Description, Seizure Date, Seized By) and link it to a case.
*   **FR-INV-04:** The IO shall be able to add Persons (Accused, Suspects, Witnesses) to a case and define their roles.
*   **FR-INV-05:** The system shall maintain a chronological timeline of all activities for a case.

##### 3.1.3 Search and Analysis Module
*   **FR-SRH-01:** The system shall provide an Advanced Search interface with multiple filter criteria (Person Name, Crime Type, Date Range, MO, Property, Location).
*   **FR-SRH-02:** Search results shall be displayable as a list of Cases or as aggregated Criminal/Accused profiles.
*   **FR-SRH-03:** The system shall return search results for simple queries within 5-8 seconds and for complex advanced queries within 10-15 seconds (see performance requirements).

##### 3.1.4 Prosecution Tracking Module
*   **FR-PRO-01:** The system shall allow the Prosecution Constable to record Court Hearing details (Date, Court Name, Purpose, Outcome) linked to a case.
*   **FR-PRO-02:** The system shall track the final judgment/disposal status of a case.

##### 3.1.5 System Administration & Configuration Module
*   **FR-ADM-01:** The system shall provide an interface to create, modify, and disable user accounts with assignment of roles and police stations.
*   **FR-ADM-02:** The system shall implement Role-Based Access Control (RBAC), where permissions are determined by the user's role.
*   **FR-ADM-03:** The system shall provide a configuration interface to manage state-specific lists (Crime Sections, Property Types, Location Hierarchies) as defined in the Domain Model.
*   **FR-ADM-04:** The Administrator shall be able to define which data fields are mandatory or configurable per state.

##### 3.1.6 Citizen Interface Module
*   **FR-CIT-01:** A citizen shall be able to track the status of their complaint by logging into the portal with their unique reference number.
*   **FR-CIT-02:** The system shall allow citizens to submit follow-up queries or information requests against their case, generating an alert for designated police personnel.

##### 3.1.7 Audit & Security Module
*   **FR-SEC-01:** The system shall log all critical user actions (login, case view, data modification, search) to an immutable Audit Log (User ID, Timestamp, Action, Entity, Entity ID).
*   **FR-SEC-02:** The system shall enforce access controls. If a user attempts to access a case without authorization, access shall be denied, and the attempt shall be logged without revealing unauthorized information.
*   **FR-SEC-03:** All data transmission between client and server shall be encrypted using SSL/TLS.

##### 3.1.8 Support & Help Desk Module
*   **FR-SUP-01:** The system shall provide a ticketing mechanism for users to report defects or request enhancements.
*   **FR-SUP-02:** Support staff shall be able to track, update, and resolve tickets, with notifications to the reporting user.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements
*   **PERF-01:** Simple search operations shall complete within **5-8 seconds** (90th percentile).
*   **PERF-02:** Advanced search with multiple filters shall complete within **10-15 seconds** (90th percentile).
*   **PERF-03:** Retrieval of a recently accessed case record shall complete within **5-8 seconds**.
*   **PERF-04:** The system architecture shall be scalable to support the data and user load from small to large police stations.

##### 3.2.2 Reliability & Availability
*   **RELY-01:** The system shall support an offline mode allowing IOs to perform critical functions (view assigned cases, log actions) without network connectivity, with automatic synchronization upon reconnection.
*   **RELY-02:** Planned maintenance downtime shall not exceed thresholds to be defined by MHA/state policy.
*   **RELY-03:** Unplanned downtime and incident frequency shall be minimized as per operational SLAs.

##### 3.2.3 Security Requirements
*   **SEC-01:** The system shall prevent common vulnerabilities (e.g., SQL Injection, Cross-Site Scripting).
*   **SEC-02:** Authentication shall support multi-tier mechanisms (User ID/Password, potentially OTP).
*   **SEC-03:** Sensitive data at rest shall be encrypted as per standards to be defined by the Security Architecture team.
*   **SEC-04:** Audit log data shall be retained for at least the life of the associated case, as per policy.

##### 3.2.4 Usability & Compliance
*   **USAB-01:** The user interface shall comply with ISO 9241 standards for usability.
*   **USAB-02:** Public-facing content (Citizen Portal) shall meet WCAG 1.0 Level A accessibility guidelines.
*   **USAB-03:** Context-sensitive help shall be available for all major workflows.

##### 3.2.5 Observability & Support
*   **OBS-01:** The system shall generate pre-defined audit reports filterable by case, user, and date range.
*   **OBS-02:** The support module shall provide metrics on defect frequency, type, and resolution time.

### 4. System Interfaces

#### 4.1 User Interfaces
*   **Citizen Portal:** A public-facing, themed web portal for complaint registration and tracking.
*   **Police Application:** A comprehensive, role-based internal web application for all police workflows.
*   **Administration Console:** A dedicated interface for system configuration and user management.

#### 4.2 Software Interfaces
*   **Authentication Service:** Internal service for user login and session management.
*   **Audit Service:** Internal service for writing immutable log entries.
*   **Reporting Engine:** Internal service for generating standard and ad-hoc reports.
*   **Future Court System Interface:** A defined API/stub for outbound data exchange (Charge-sheet, hearing updates). Specification deferred.

#### 4.3 Communication Interfaces
*   All external communication (Citizen Portal) shall use HTTPS.
*   Internal service communication shall use secure protocols.

### 5. Appendices

#### 5.1 Data Model (Entity-Attribute Summary)
```
Case: {Case_ID(PK), Registration_DateTime, Police_Station, Crime_Type, Status, Complainant_ID(FK), IO_Assigned_ID(FK), ...}
Person: {Person_ID(PK), Full_Name, Gender, Father_Name, Address, ...}
Investigation_Action: {Action_ID(PK), Case_ID(FK), DateTime, Type, Description, IO_ID(FK), ...}
Evidence: {Evidence_ID(PK), Case_ID(FK), Type, Description, Seizure_Date, Seized_By_ID(FK), ...}
User: {User_ID(PK), Name, Role, Police_Station, ...}
Audit_Log: {Log_ID(PK), Timestamp, User_ID(FK), Action, Entity_Type, Entity_ID, ...}
```

#### 5.2 Acceptance Criteria (Gherkin Format)
*   **Feature:** Crime Registration
    ```
    Scenario: Successful Citizen Complaint Submission
        Given a citizen is on the complaint registration page
        When they submit a valid complaint with all mandatory details
        Then the system must generate a unique reference number
        And display a downloadable acknowledgement receipt
    ```

*   **Feature:** Access Control
    ```
    Scenario: Unauthorized Case Access Attempt
        Given user "X" does not have view rights for Case "C-123"
        When user "X" attempts to open Case "C-123" via its direct URL
        Then the system must display an "Access Denied" message
        And the attempt must be recorded in the Audit Log
        And no case details must be revealed
    ```

#### 5.3 Undecided Issues & Open Items
1.  **System Availability SLA:** Specific hours and downtime thresholds (`<xx:00>`, `<xx hours>`) - **Owner: MHA/State Police Heads**.
2.  **Data Encryption at Rest:** Specific standards and protocols - **Owner: Security Architecture Team**.
3.  **Infrastructure Specifications:** Bandwidth minima for low-bandwidth stations, Disaster Recovery RTO - **Owner: Infrastructure & Operations Team**.
4.  **State Configuration:** Final list of configurable items and defaults - **Owner: Respective State Police Departments**.
5.  **Data Retention Policy:** Archival rules beyond case life - **Owner: MHA Policy Wing**.

---
*Document End*