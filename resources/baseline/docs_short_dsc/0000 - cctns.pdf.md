# Software Requirements Specification (SRS)
## Crime & Criminal Tracking Network and Systems (CCTNS)

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional requirements for the Crime & Criminal Tracking Network and Systems (CCTNS). It serves as a comprehensive guide for developers, testers, project managers, and stakeholders to understand the system's intended capabilities, constraints, and behavior. The primary audience includes the development team, quality assurance, and the Ministry of Home Affairs (MHA) oversight committee.

#### 1.2 Scope
The CCTNS is an E-Governance Mission Mode Project designed to digitize and streamline police workflows from crime registration through investigation to prosecution. This SRS covers the functional requirements for the software application to be deployed at police stations and accessed by citizens online.

**In-Scope Functionality:**
*   Citizen complaint registration and initial police interaction.
*   Digital management of the investigation process, including updates and evidence logging.
*   Recording of court interactions, hearing dates, and prosecution outcomes.
*   Advanced search functionality for cases, persons, and crime patterns.
*   A citizen-facing portal for complaint registration, status tracking, and information exchange.

**Out-of-Scope Elements:**
*   Detailed physical database schema design and data structure specifications.
*   Procurement, installation, and configuration of specific hardware or network infrastructure.
*   Deep integration with external judicial, prison, or other government systems (only basic court interfacing is included).
*   Development of training materials, user manuals, or change management programs.
*   Policies and mechanisms for long-term data archival, purging, or migration beyond the active operational lifecycle.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **CCTNS:** Crime & Criminal Tracking Network and Systems
*   **IO:** Investigating Officer
*   **MHA:** Ministry of Home Affairs
*   **FIR:** First Information Report
*   **SOA:** Service-Oriented Architecture
*   **RTI:** Right to Information
*   **SRS:** Software Requirements Specification

#### 1.4 References
*   CCTNS Project Charter & Mission Statement, Ministry of Home Affairs.
*   National e-Governance Plan (NeGP) Guidelines.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its stakeholders, and operating environment. Section 3 details the specific functional requirements, organized by system features and linked to user stories.

### 2. Overall Description

#### 2.1 Product Perspective
The CCTNS is a new, standalone web-based application but is designed to be part of a larger national e-governance ecosystem. It will adhere to Open Standards and a Service-Oriented Architecture (SOA) to allow for future integration with other state and national systems (e.g., courts, prisons, transport databases). The system includes a backend application for police station personnel and a frontend portal for citizens.

#### 2.2 User Classes and Characteristics
| User Class | Key Characteristics | Primary Goals |
| :--- | :--- | :--- |
| **Citizen/Complainant** | Varied technical proficiency; access via public internet. | Report crimes, track case status, access information. |
| **Investigating Officer (IO)** | Police personnel; primary system user; may work in low-bandwidth areas. | Manage investigation lifecycle, record evidence, generate reports. |
| **Records Room Staff** | Police personnel; focused on data management and retrieval. | File and retrieve case records, respond to RTI queries, generate station reports. |
| **Police Constable (Court Duty)** | Police personnel; mobile user; interfaces with courts. | Record court dates, orders, and prosecution updates. |
| **System Administrator** | Technically skilled; operates at state/national level. | Manage users, roles, configure state-specific legal parameters (Acts, Sections), monitor system health. |
| **MHA (Ministry)** | Executive/oversight role; requires aggregated data views. | Monitor national crime trends, assess system performance, define policy. |

#### 2.3 Operating Environment
*   **Software:** Must operate on standard web browsers (Chrome, Firefox, Edge). The server-side shall be platform-agnostic (e.g., Java/.NET on Linux/Windows Server).
*   **Hardware:** Must be compatible with standard computing hardware available at police stations (desktops, laptops, basic printers).
*   **Network:** Must be functional in **both online and offline modes**. Must deliver usable performance in **low-bandwidth environments**.
*   **Security:** Must operate in a secure government network environment, requiring robust authentication, authorization, and audit trails.

#### 2.4 Design and Implementation Constraints
1.  **Architecture:** Must be developed using Open Standards and a Service-Oriented Architecture (SOA).
2.  **Connectivity:** The application logic must support offline data entry and subsequent synchronization when connectivity is restored.
3.  **Performance:** The system must be scalable to handle the caseload variance between small and large police stations.
4.  **Security:** The system must implement safeguards against common vulnerabilities including SQL Injection, Cross-Site Scripting (XSS), and unauthorized data access, in compliance with government security standards.
5.  **Usability:** The interface must be intuitive for police personnel with varying levels of computer literacy.

#### 2.5 User Documentation
*   Online help text and tooltips integrated within the application.
*   Context-sensitive user guides for major workflows (to be developed separately, as per out-of-scope).

#### 2.6 Assumptions and Dependencies
*   Police stations will have access to basic computer hardware and intermittent internet connectivity.
*   State governments will provide the necessary legal data (Acts, Sections, Police Station Jurisdictions) for system configuration.
*   User acceptance training will be conducted by a separate change management team.

### 3. System Features and Requirements

This section details the functional requirements, mapped to the core user stories and in-scope functionalities.

#### 3.1 Feature: Citizen Complaint Registration & Interaction
**Description:** This feature allows citizens to register complaints online and enables police personnel to record complaints received in person.

**3.1.1 User Story:** *As a Citizen, I want to register a complaint online so that I can report a crime without visiting the police station.*
*   **FR-1.1:** The system shall provide a public web portal for citizen access.
*   **FR-1.2:** The portal shall present a form for registering a complaint, capturing: Complainant Details (Name, Address, Contact, ID Proof), Incident Details (Type, Time, Location, Description), and Accused/Victim/Suspect details (if known).
*   **FR-1.3:** Upon submission, the system shall generate a unique tracking number (e.g., CCTNS-XXXXX) and provide it to the citizen.
*   **FR-1.4:** The system shall assign the complaint to the relevant police station based on the incident location (jurisdiction).

**3.1.2 Related Requirements:**
*   **FR-1.5:** The system shall allow police personnel at the station to view, verify, and convert an online complaint into a formal station record (e.g., FIR).
*   **FR-1.6:** The system shall allow personnel to directly register a complaint received in person at the police station, using the same data fields as the online form.

#### 3.2 Feature: Investigation Process Management
**Description:** This feature supports the Investigating Officer (IO) in managing the entire investigation lifecycle of a case digitally.

**3.2.1 User Story:** *As an Investigating Officer, I want to log investigation updates and evidence digitally so that the case file is complete and accessible.*
*   **FR-2.1:** The system shall provide an "Investigation Dashboard" for the IO to view all assigned cases.
*   **FR-2.2:** For each case, the IO shall be able to log chronological "Case Diaries" or updates.
*   **FR-2.3:** The system shall allow the IO to digitally attach evidence records to the case file. This includes:
    *   **FR-2.3.1:** Uploading documents (PDF, Images, Scans).
    *   **FR-2.3.2:** Recording details of physical evidence seized.
    *   **FR-2.3.3:** Recording witness statements.
*   **FR-2.4:** The system shall allow the IO to update the status of the case (e.g., Under Investigation, Chargesheet Filed, Undetected, Closed).
*   **FR-2.5:** The system shall support offline mode, allowing the IO to enter data without connectivity and queue it for synchronization.

#### 3.3 Feature: Prosecution Support
**Description:** This feature enables tracking of a case's progress through the judicial system.

**3.3.1 User Story:** *As a Police Constable, I want to record court hearing dates and outcomes so that the prosecution status of a case is tracked accurately.*
*   **FR-3.1:** The system shall provide an interface to link a case to court proceedings.
*   **FR-3.2:** For each court hearing, the user shall be able to record: Court Name, Hearing Date, Judge Name, Purpose of Hearing, and Outcome/Order.
*   **FR-3.3:** The system shall maintain a history of all hearings for a case.
*   **FR-3.4:** The system shall allow the final disposal of the case to be recorded (e.g., Convicted, Acquitted, Compounded).

#### 3.4 Feature: Search and Retrieval
**Description:** This feature provides powerful search capabilities across all system data.

**3.4.1 User Story:** *As a Records Room Staff, I want to search for cases by various criteria so that I can quickly retrieve information for reporting or RTI requests.*
*   **FR-4.1:** The system shall provide an advanced search interface with multiple filter criteria, including but not limited to: Case Number, Complainant Name, Accused Name, Date Range, Crime Type, Police Station, Investigating Officer, Case Status.
*   **FR-4.2:** The system shall allow for wildcard and partial matching in text-based searches.
*   **FR-4.3:** Search results shall be displayed in a configurable list, allowing the user to select which columns to view.
*   **FR-4.4:** The user shall be able to export search results to standard formats (e.g., PDF, Excel) for reporting.
*   **FR-4.5:** The system shall provide "person search" functionality to find all cases associated with a specific individual (as complainant, accused, witness, victim).

#### 3.5 Feature: Citizen Interface - Status Tracking & Services
**Description:** This feature allows citizens to interact with the police post-registration.

**3.5.1 User Story:** *As a Citizen, I want to check the status of my registered complaint so that I am informed about the progress of my case.*
*   **FR-5.1:** The citizen portal shall provide a "Track Complaint" function.
*   **FR-5.2:** Using the unique tracking number, the citizen shall be able to view the current status of their complaint (e.g., Registered, Under Investigation, Chargesheet Filed) and the assigned police station.
*   **FR-5.3:** The system may provide secure, read-only access to certain non-sensitive documents (e.g., a copy of the FIR) based on configurable policy.

#### 3.6 Feature: System Administration & Configuration
**Description:** This feature allows administrators to manage the system, its users, and state-specific data.

**3.6.1 User Story:** *As a System Administrator, I want to configure state-specific data like acts and sections so that the application is tailored to local legal requirements.*
*   **FR-6.1:** The system shall provide an admin console for managing users, roles, and permissions (RBAC - Role-Based Access Control).
*   **FR-6.2:** The admin shall be able to configure master data, including:
    *   **FR-6.2.1:** Indian Penal Code (IPC) and other local Acts and Sections.
    *   **FR-6.2.2:** Police Station jurisdictions and hierarchies (State, District, Station).
    *   **FR-6.2.3:** Crime types and classifications.
*   **FR-6.3:** The system shall log all critical user activities (login, case modification, data export) for audit purposes.

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   The system shall support concurrent access by multiple users from a single police station.
*   **Search Operations:** A complex search with 5+ filters shall return results within **10 seconds** under normal load (TBR - To Be Refined per Undecided Issues).
*   The system shall be designed to handle a peak load of [X] concurrent transactions per police station (TBR).

#### 4.2 Safety & Security Requirements
*   All access shall require authentication via username and strong password.
*   All data transmission shall be encrypted using TLS 1.2 or higher.
*   The system shall prevent SQL Injection and Cross-Site Scripting attacks.
*   Access to case data shall be strictly controlled by user role and police station jurisdiction.
*   All data exports shall be logged and may require supervisory approval.

#### 4.3 Software Quality Attributes
*   **Availability:** The system shall aim for high availability. Specific uptime SLAs and downtime windows are TBR (see Undecided Issues).
*   **Reliability:** The system shall have a mean time between failures (MTBF) of not less than 720 hours.
*   **Maintainability:** The code shall be modular, well-documented, and adhere to the defined SOA for ease of future modification.
*   **Portability:** The application shall be browser-based, ensuring compatibility across major browsers on standard operating systems.
*   **Scalability:** The architecture shall allow for horizontal scaling of application servers to accommodate increasing numbers of users and stations.

### 5. Appendices

#### 5.1 Success Metrics (Key Performance Indicators - KPIs)
*   **Task Efficiency:** 50% reduction in average time to register a complaint compared to manual process.
*   **User Adoption:** >80% satisfaction rate among police personnel in pilot stations after 3 months of operation.
*   **Data Quality:** >95% accuracy in key crime data fields used for monthly state-level reporting.

#### 5.2 Undecided Issues & TBD (To Be Determined)
The following items require further stakeholder discussion and resolution:
1.  Specific system availability hours (24/7 vs. scheduled maintenance windows) and allowable planned/unplanned downtime thresholds.
2.  Exact response time requirements for all common functions under defined peak load conditions.
3.  Finalized details of the data backup frequency, recovery point objective (RPO), recovery time objective (RTO), and disaster recovery plans.
4.  Specific technical protocols (e.g., REST/SOAP) and data formats (e.g., JSON/XML) for potential future integration with external judicial or prison systems.
5.  The detailed implementation approach for multi-lingual support (e.g., full UI translation, data entry in local language).

---
*Document End*