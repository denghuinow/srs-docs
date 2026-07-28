# Software Requirements Specification (SRS)
## Black Start Capability Plan (BCP) Management System

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review  
**Prepared for:** California Independent System Operator (CAISO)  
**Prepared by:** [Your Organization/Department Name]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for a system to support the administration, planning, testing, and compliance tracking of the CAISO Black Start Capability Plan (BCP). The purpose of this system is to provide a centralized, reliable platform for managing all aspects of Black Start resource assurance in alignment with WECC and NERC reliability standards.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are prefixed with `FR-` and non-functional requirements with `NFR-`.
*   **Priority:** `(H)` High, `(M)` Medium, `(L)` Low.
*   **Keywords:** `SHALL`, `SHOULD`, `MAY`, `WILL` are used as defined in IETF RFC 2119.

#### 1.3 Intended Audience and Reading Suggestions
*   **CAISO Project Sponsors & Management:** For scope approval and high-level feature alignment.
*   **System Architects & Developers:** For designing and implementing the system based on detailed requirements.
*   **Quality Assurance Team:** For creating test plans and validation procedures.
*   **End Users (Planners, Operators, Test Administrators):** For understanding system capabilities and providing feedback.
*   **Compliance Auditors (WECC/NERC):** For understanding how the system supports regulatory compliance.

#### 1.4 Project Scope
The BCP Management System is a software platform designed to facilitate the planning, testing, record-keeping, training coordination, and compliance reporting for CAISO's Black Start resources. It serves as the system of record for all designated Black Start generators and the primary tool for managing the annual lifecycle of the BCP.

**In-Scope (System Support):**
*   Management of the Black Start generator database (capacity, location, status, test history).
*   Scheduling, tracking, and documenting results of mandatory Black Start unit tests.
*   Supporting annual planning studies by providing resource data and compliance status.
*   Managing the workflow for contract (RMR/Interim) establishment and review.
*   Tracking completion of annual operator restoration training and simulations.
*   Generating compliance reports for internal and external (WECC/NERC) audit purposes.

**Out-of-Scope:**
*   Real-time control systems for actual grid restoration during a blackout event.
*   Physical generator protection or control system design.
*   Day-to-day energy market bidding or scheduling functions.
*   Environmental, Health, and Safety (EHS) management software.
*   The system will not execute physical tests; it manages the administrative process surrounding them.

#### 1.5 References
*   WECC Reliability Standard: System Restoration (PLAN-SR-1)
*   NERC Reliability Standard: EOP-005-3 – System Restoration from Blackstart Resources
*   CAISO Tariff: Section 40 – Reliability Must-Run (RMR) Service
*   CAISO Business Practice Manual (BPM) for Reliability Requirements

### 2. Overall Description

#### 2.1 Product Perspective
The BCP Management System is a new, standalone application within the CAISO enterprise architecture. It will integrate with existing systems through defined interfaces:
*   **Generator Data Source:** To import basic generator characteristics and ownership data.
*   **CAISO Operator Training Simulator (OTS):** To schedule training sessions and record participation (future dependent on simulator availability).
*   **Document Management System (DMS):** To archive test reports, contracts, and audit documentation.
*   **External Portal:** For secure data submission by Generator Owners.

#### 2.2 Product Functions (High-Level)
1.  **Generator Portfolio Management:** Maintain a master database of all Black Start designated units.
2.  **Test Lifecycle Management:** Administer the end-to-end process for scheduling, executing, documenting, and analyzing Black Start tests.
3.  **Planning & Analysis Support:** Provide data and tools to assist Grid Planners in annual contingency studies and resource adequacy verification.
4.  **Compliance & Reporting:** Track compliance metrics, generate standard reports, and support audit requests.
5.  **Training Administration:** Schedule, track attendance, and manage materials for annual operator restoration training.
6.  **Contract Management Workflow:** Track the status of RMR and Interim contracts related to Black Start services.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **CAISO Grid Planner** | Power systems engineer. Uses planning tools. Needs accurate, current data. | Access to unit capabilities, test history, and location data for studies. Ability to mark units for annual review. |
| **CAISO Real-time Dispatcher** | Certified grid operator. Works in control room under time pressure. | Clear view of unit test schedules and status. Simple interface to request/dispatch tests. Access to unit start-up time limits. |
| **Generator Owner/Operator** | External entity. Varying levels of IT sophistication. | Secure portal to submit test data and documentation. Clear instructions on requirements and schedules. |
| **CAISO Test Administrator** | Operations support staff. Detail-oriented. Manages process compliance. | Dashboard to monitor all test activities. Workflow to review, validate, and record test results. Tools to calculate availability. |
| **Compliance Auditor (WECC/NERC)** | External regulator. Focused on evidence and traceability. | Read-only access to generate standardized compliance reports. Ability to drill down to source documentation (test reports, contracts). |
| **System Administrator** | IT staff. Manages user access and system health. | Tools for user role management, system configuration, and log monitoring. |

#### 2.4 Operating Environment
*   **Software:** Web-based application accessible via standard browsers (Chrome, Edge, Firefox). Backend built on Java/.NET/Node.js stack. Relational database (Oracle, PostgreSQL).
*   **Hardware:** Hosted on CAISO's secure internal servers or approved cloud environment (e.g., AWS GovCloud, Azure Government).
*   **Networks:** Accessible via CAISO corporate intranet. External access for Generator Owners via a secure, authenticated portal over HTTPS.

#### 2.5 Design and Implementation Constraints
1.  **Security:** System SHALL comply with CAISO cybersecurity policies and NERC CIP standards. All external data exchanges SHALL be encrypted.
2.  **Data Retention:** Test records, contracts, and compliance reports SHALL be retained for a minimum of seven years, per regulatory requirements.
3.  **Availability:** The system SHALL maintain 99.5% operational availability during business hours (0600-2000 PT).
4.  **Integration:** The system SHALL use CAISO-approved enterprise service bus (ESB) or API gateways for all system-to-system integrations.
5.  **Auditability:** All data changes (CRUD operations) for compliance-related entities (units, tests, contracts) SHALL be logged with user ID, timestamp, and change detail.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Generator Owners will have internet access and basic capability to upload documents via a web portal.
*   **Assumption:** Accurate and timely generator characteristic data will be available from the source system.
*   **Dependency:** Finalization of the "failure to start" percentage parameter by CAISO management for planning studies.
*   **Dependency:** Availability and schedule of the system simulator for integrated operator training exercises.

### 3. System Features and Requirements

#### 3.1 Feature: Black Start Generator Database Management
**Description:** Maintain a centralized, authoritative database of all generators designated for Black Start service.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-010** | The system SHALL allow authorized users (Test Admins, Planners) to create, read, update, and deactivate records for Black Start generators. | H |
| **FR-011** | Each generator record SHALL store: Unique ID, Name, Owner, Location (GPS/Bus), Technology Type, Certified Capacity (MW), Contract Type (RMR/Interim/Voluntary), Designation Date, and Status (Active/Inactive/Under Review). | H |
| **FR-012** | The system SHALL maintain a full version history for each generator record, capturing all changes to critical fields. | M |
| **FR-013** | The system SHALL provide filtered views and search capabilities for users to find generators by criteria such as location, technology, contract type, or test status. | M |

#### 3.2 Feature: Test Lifecycle Management
**Description:** Manage the end-to-end process for mandatory Black Start capability tests.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-020** | The system SHALL allow the Test Administrator to generate an annual test schedule, targeting at least one-third of RMR/Interim units, respecting constraints (e.g., no hydro tests during water constraints). | H |
| **FR-021** | The system SHALL allow a Real-time Dispatcher to request a test for a specific unit, logging the request time and operator. | H |
| **FR-022** | The system SHALL provide a portal for Generator Owners to submit test results, including: Test Date/Time, Start-up Time, Synchronization Time, Max Capacity Achieved, Ambient Temperature, and a signed test report (PDF). | H |
| **FR-023** | The system SHALL automatically calculate the unit's "availability" based on submitted start-up/sync times against technology-specific limits (e.g., 30 min for gas, 2.5 hours for hot steam). | H |
| **FR-024** | The system SHALL enforce a workflow where the Test Administrator must review and officially "Certify" or "Fail" a submitted test. | H |
| **FR-025** | For failed tests, the system SHALL require the Generator Owner to submit a root cause explanation and a corrective action plan via the portal. | H |
| **FR-026** | The system SHALL track the next required test date for each unit based on its last successful test date (not to exceed 5 years). | M |

#### 3.3 Feature: Planning & Compliance Support
**Description:** Provide tools and data to support annual planning and demonstrate compliance.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-030** | The system SHALL generate a standard annual report confirming that Black Start resources meet WECC restoration needs, incorporating current unit data and status. | H |
| **FR-031** | The system SHALL provide Grid Planners with an export function to extract generator data (location, capacity, availability) for use in external contingency study tools. | H |
| **FR-032** | The system SHALL maintain a dashboard showing key performance indicators (KPIs): % of units tested YTD, % of tests passed, overall plan compliance status. | M |
| **FR-033** | The system SHALL allow Compliance Auditors to generate on-demand reports listing all units, their test history for a given period, and certification status. | H |

#### 3.4 Feature: Training Administration
**Description:** Coordinate and track annual system restoration training for CAISO operators.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-040** | The system SHALL allow an administrator to schedule training sessions (classroom, simulation) and define a roster of required attendees. | M |
| **FR-041** | The system SHALL track operator attendance and mark training as "Completed" for each individual on their record. | M |
| **FR-042** | The system SHALL alert management and the individual operator if annual training is nearing its due date or is overdue. | L |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Primary UI:** A responsive, web-based interface with role-based dashboards.
*   **Generator Portal:** A simplified, branded external interface for data submission by Generator Owners.
*   **Reports UI:** A dedicated module for generating and downloading pre-formatted reports (PDF, Excel).

#### 4.2 Hardware Interfaces
*   None specified. The system is software-based.

#### 4.3 Software Interfaces
*   **SI-01: Corporate Generator Database:** SOAP/REST API to periodically synchronize basic generator static data (ID, Name, Location, Technology).
*   **SI-02: Document Management System (DMS):** API to deposit finalized, certified test reports and contracts for long-term archival.
*   **SI-03: Training Simulator (Future):** Interface to exchange schedule and attendance data (format and protocol TBD based on simulator).

#### 4.4 Communications Interfaces
*   All external communications (especially with the Generator Portal) SHALL use TLS 1.2 or higher.
*   The system SHALL support email notifications for workflow events (e.g., test request sent, results submitted, certification complete).

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **Response Time:** 95% of all user interface interactions SHALL complete in less than 2 seconds under normal load.
*   **Report Generation:** Standard compliance reports SHALL be generated within 30 seconds.
*   **Concurrent Users:** The system SHALL support up to 50 concurrent active users.

#### 5.2 Safety Requirements
*   The system SHALL not issue direct control commands to generators. All test dispatches are requests that must be manually actioned by plant personnel.
*   The system SHALL clearly display safety warnings and operational constraints (e.g., "Hydro test not permitted during declared water constraint") to users scheduling tests.

#### 5.3 Security Requirements
*   Authentication SHALL integrate with CAISO's central Active Directory/LDAP.
*   Authorization SHALL be role-based (RBAC) with permissions defined per the user classes in Section 2.3.
*   All sensitive data at rest (e.g., test reports) SHALL be encrypted.
*   The system SHALL undergo annual security vulnerability assessments.

#### 5.4 Software Quality Attributes
*   **Reliability:** Mean Time Between Failures (MTBF) > 720 hours.
*   **Maintainability:** Code SHALL adhere to CAISO development standards and include documentation for all core functions.
*   **Usability:** The system SHALL achieve a System Usability Scale (SUS) score of >75 after initial user training.
*   **Availability:** 99.5% availability during core business hours (0600-2000 PT), as per constraint 2.5.

### 6. Other Requirements

#### 6.1 Appendices
*   **Appendix A: Glossary**
    *   **Black Start:** The ability of a generating unit to start without an external electrical supply.
    *   **Cranking Path:** A designated transmission path used to energize the grid from a Black Start unit.
    *   **RMR (Reliability Must-Run):** A contractually obligated generator required for grid reliability.
    *   **WECC/NERC:** Western Electricity Coordinating Council / North American Electric Reliability Corporation.
*   **Appendix B: Data Models** *(To be developed during design phase)*
*   **Appendix C: Detailed Report Specifications** *(To be developed during design phase)*

#### 6.2 Undecided Issues (TBD)
1.  The specific system parameter for "Expected Failure to Start Percentage" (`FR-030` dependency).
2.  The technical interface specification for integration with the Operator Training Simulator (`SI-03`).
3.  The negotiation protocol and data fields for handling Black Start units in another Reliability Coordinator's area.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead System Architect | | | |
| SRS Author | | | |