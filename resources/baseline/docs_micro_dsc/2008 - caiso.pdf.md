# Software Requirements Specification (SRS)
## Black Start Resource Management System (BSRMS)
**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Black Start Resource Management System (BSRMS). The purpose of the BSRMS is to provide a centralized, automated platform for ensuring a reliable and effective Black Start capability across the electrical grid. The system will support the planning, testing, and maintenance of designated Black Start generators to enable rapid and secure restoration of the power system following a complete or partial blackout.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms "MUST," "MUST NOT," "SHALL," "SHALL NOT," "SHOULD," and "MAY" are used as defined in IETF RFC 2119.
*   **Priority:** (H)igh, (M)edium, (L)ow.

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Sponsors & Grid Planners:** Review Sections 1 (Introduction) and 2 (Overall Description) for project scope and objectives.
*   **System Architects & Developers:** Focus on Sections 3 (System Features) and 4 (External Interface Requirements) for detailed functional specifications.
*   **QA Testers & Validation Engineers:** Use Section 3 (System Features) to derive test cases and Section 5 (Non-Functional Requirements) for performance and compliance criteria.
*   **Database Administrators & IT Operations:** Refer to Section 4.3 (Communications Interfaces) and Section 5 for system integration and operational needs.

#### 1.4 Project Scope
The BSRMS is a planning, compliance, and operational data management system. Its core scope includes:
*   Facilitating annual contingency studies to determine the required quantity and optimal geographical location of Black Start resources.
*   Managing the lifecycle of Black Start capability testing, including scheduling, recording results, and validating performance against strict technical constraints.
*   Maintaining a secure, auditable, and up-to-date master database of all designated Black Start generators, their attributes, and their status.
*   Ensuring that all planning and testing activities adhere to regulatory and internal policy constraints, particularly the mandatory five-year review cycle.

**Out of Scope:**
*   Direct real-time control of generators during an actual Black Start event.
*   Real-time Energy Management System (EMS) or Supervisory Control and Data Acquisition (SCADA) functionality.
*   Physical maintenance scheduling of generator hardware.

### 2. Overall Description

#### 2.1 Product Perspective
The BSRMS is a standalone system that will integrate with existing enterprise systems.
*   **Parent System:** The broader Grid Restoration Management suite.
*   **Interfaces:**
    *   **Inputs:** Study data from contingency analysis tools, test results from field demonstrations, generator technical data from asset management systems.
    *   **Outputs:** Approved Black Start Plan, compliance reports, test schedules, alerts for expiring certifications.
*   **User Classes:** Grid Planning Engineers, System Operators (Read-Only), Compliance Officers, Database Administrators.

#### 2.2 Product Functions (High-Level Summary)
1.  **Contingency Study Management:** Support the annual process of defining and running studies to evaluate Black Start resource adequacy.
2.  **Generator Testing & Certification Workflow:** Manage the end-to-end process of scheduling tests, documenting results, and certifying units based on performance against technical criteria.
3.  **Centralized Resource Database:** Serve as the single source of truth for all Black Start generator data, with full version history and audit trails.
4.  **Plan Management & Compliance Tracking:** Maintain the official Black Start Plan, track review cycles, and ensure all activities comply with the mandated five-year review policy.

#### 2.3 User Characteristics
*   **Grid Planning Engineer:** Expert in power system stability and restoration procedures. Needs advanced analytical tools and data visualization.
*   **Compliance Officer:** Focused on documentation, audit trails, and regulatory deadlines. Needs robust reporting and alerting features.
*   **System Operator:** Needs quick, reliable, read-only access to the current list of certified Black Start resources and their key parameters during restoration drills or events.

#### 2.4 Constraints
1.  **Regulatory & Policy Constraints:**
    *   `CON-1`: The system MUST enforce the rule that Black Start units are capable of starting and energizing a transmission path **without any external electrical system assistance**.
    *   `CON-2`: The system MUST validate that unit start-up and synchronizing times do not exceed technology-specific caps (e.g., 30 minutes for hydro and gas turbines).
    *   `CON-3`: The system MUST track and flag for review the overall Black Start Plan and individual generator test demonstrations at least every five years.
2.  **Technical Constraints:** Must integrate with existing corporate authentication (e.g., Active Directory). Database must comply with internal data retention policies (e.g., 10 years for test records).

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Reliable generator technical data (e.g., fuel type, capacity) will be available via feed from the corporate Asset Management System.
*   **Dependency:** The system depends on the accuracy of external contingency analysis software for study inputs and results.
*   **Assumption:** Qualified personnel will be available to perform physical generator tests and input results into the BSRMS.

### 3. System Features

#### 3.1 Feature 1: Contingency Study & Resource Planning
**Description:** This feature allows planners to define, execute, and analyze annual studies to determine the required quantity and location of Black Start generators.

**3.1.1 Requirements**
*   `FR-101` (H): The system SHALL allow users to define study scenarios, including grid topology, outage assumptions, and restoration paths.
*   `FR-102` (H): The system SHALL integrate with or import results from external contingency analysis tools to identify gaps in Black Start coverage.
*   `FR-103` (M): The system SHALL provide visualization tools (e.g., geographical maps, single-line diagrams) to display study results and proposed resource locations.
*   `FR-104` (H): The system SHALL allow users to formally approve and version a finalized annual Black Start Plan based on study outcomes.

#### 3.2 Feature 2: Generator Testing & Certification Management
**Description:** This feature manages the end-to-end workflow for testing designated Black Start units and certifying their capability.

**3.2.1 Requirements**
*   `FR-201` (H): The system SHALL allow scheduling of generator test demonstrations, assigning responsible personnel, and setting deadlines.
*   `FR-202` (H): The system SHALL provide a structured form for inputting test results, **including mandatory fields for:**
    *   Actual start-up time.
    *   Actual synchronization time.
    *   Recorded voltage stability during cranking and loading.
    *   Recorded frequency stability during cranking and loading.
*   `FR-203` (H): The system SHALL automatically validate input test results against key constraints `CON-1` and `CON-2`.
    *   *Example Validation Logic:*
        ```sql
        IF (test_result.startup_time > generator_type.max_startup_time)
            THEN certification_status = 'FAIL';
        IF (test_result.required_external_power > 0)
            THEN certification_status = 'FAIL';
        ```
*   `FR-204` (M): Based on validation (`FR-203`), the system SHALL automatically assign a certification status (e.g., "Certified," "Failed - Retest Required," "Conditional").
*   `FR-205` (H): The system SHALL calculate and track the next required test date based on the five-year review cycle (`CON-3`) and send automated alerts 6 months and 1 month prior.

#### 3.3 Feature 3: Black Start Resource Database
**Description:** This feature maintains a comprehensive, secure, and auditable database of all designated Black Start resources.

**3.3.1 Requirements**
*   `FR-301` (H): The system SHALL store a complete profile for each generator, including: ID, Name, Location (GPS), Owner, Technology Type, Capacity, Designated Cranking Path, Certification Status, and Historical Test Records.
*   `FR-302` (H): The system SHALL maintain a full audit log of all changes made to generator records or the Black Start Plan (who, what, when).
*   `FR-303` (M): The system SHALL support the annual update process, allowing mass updates or confirmations of generator data, with change tracking.
*   `FR-304` (H): The system SHALL provide role-based search, filter, and export capabilities (e.g., "Show all certified hydro units in Region X").

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **UI-1:** A modern, web-based interface accessible via standard browsers (Chrome, Edge, Firefox).
*   **UI-2:** Dashboard views for planners, compliance officers, and operators.
*   **UI-3:** Standardized, printable reports for compliance audits.

#### 4.2 Hardware Interfaces
*   **HI-1:** The system shall be hosted on standard enterprise server hardware. No direct hardware interfaces to field devices are required.

#### 4.3 Software Interfaces
*   **SI-1:** **Asset Management System Interface:** SOAP/REST API to synchronize generator static data (owner, type, capacity).
*   **SI-2:** **Contingency Analysis Tool Interface:** Ability to import/export data files (e.g., CSV, CIM/XML format) for study scenarios and results.
*   **SI-3:** **Corporate Authentication Service:** Integration with LDAP/Active Directory for user authentication and role management.

#### 4.4 Communications Interfaces
*   **CI-1:** All client-server communications shall use HTTPS (TLS 1.2 or higher).
*   **CI-2:** The system shall support email (SMTP) for sending automated alerts and notifications.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-101`: The database search and report generation for any single region shall complete in < 5 seconds for 95% of queries under normal load.
*   `NFR-102`: The system shall support concurrent access by up to 50 planning and compliance users.

#### 5.2 Safety & Security Requirements
*   `NFR-201`: The system shall be compliant with NERC CIP standards relevant to planning data (e.g., CIP-003, CIP-010).
*   `NFR-202`: All access shall be role-based (RBAC). Only authorized planners shall modify the Black Start Plan or certification status.
*   `NFR-203`: All audit logs shall be immutable and retained for a minimum of 10 years.

#### 5.3 Software Quality Attributes
*   **Availability:** 99.5% uptime during business hours (0700-1800, Mon-Fri).
*   **Reliability:** Data integrity and referential integrity MUST be maintained across all transactions.
*   **Maintainability:** The system shall be designed with modular components to allow for updates to study algorithms or constraint rules without major re-architecture.

---
*This document is the proprietary information of the System Operator and is subject to change.*