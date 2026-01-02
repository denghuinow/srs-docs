# Software Requirements Specification (SRS)
## Black Start Resource Management System (BSRMS)
**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Black Start Resource Management System (BSRMS). The primary purpose of the BSRMS is to provide a centralized platform for planning, verifying, contracting, testing, and maintaining an inventory of Black Start generators. This system is critical for ensuring the reliable and timely restoration of the electric grid following a complete or major blackout.

#### 1.2 Document Conventions
This document follows standard SRS conventions. Requirements are uniquely identified with tags (e.g., `FR-001`, `NFR-010`). Markdown is used for structure, with code blocks denoting system messages or structured data examples.

#### 1.3 Intended Audience and Reading Suggestions
*   **CAISO System Operators & Planners:** Focus on Sections 2 (Overall Description), 3.2 (Functional Requirements), and 5 (External Interface Requirements).
*   **Generator Owners/Operators:** Focus on Sections 3.2.3 (Testing Management) and 5.2 (User Interfaces).
*   **Software Developers & Architects:** Focus on all sections, particularly Section 3 (Specific Requirements) and Section 4 (System Features).
*   **QA Testers & Project Managers:** Focus on Section 3 (Specific Requirements) to derive test cases and project scope.

#### 1.4 Project Scope
The BSRMS is a planning, compliance, and operational data management system. It supports the end-to-end lifecycle of Black Start resource management—from strategic planning based on contingency studies to the annual verification of contracted capacity, scheduling and analysis of performance tests, and maintenance of a system-of-record database. The system does **not** include real-time grid control or the direct dispatch of generators during an actual blackout event.

#### 1.5 References
*   NERC Standard EOP-005-3: System Restoration from Blackstart Resources
*   CAISO Tariff, Section 40: Black Start Service
*   Internal CAISO Business Practice Manual: Black Start Planning and Compliance

### 2. Overall Description

#### 2.1 Product Perspective
The BSRMS is a new, standalone system that will integrate with existing CAISO enterprise systems. It will serve as the authoritative source for all Black Start resource data.

#### 2.2 Product Functions (High-Level Summary)
1.  **Contingency Analysis Support:** Store study inputs/results and calculate required Black Start resource quantity and location.
2.  **Contract & Capacity Management:** Track annual contracts, verify sufficiency against requirements, and manage financial/compliance data.
3.  **Testing Management:** Schedule tests, record results (start-up time, output performance), and determine certification status (Available/Unavailable).
4.  **Resource Database:** Maintain a comprehensive, auditable registry of all designated Black Start units, their capabilities, history, and status.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key System Interactions |
| :--- | :--- | :--- |
| **CAISO Planner** | Power systems engineer. Creates restoration plans and studies. | Inputs study data, defines requirements, analyzes resource adequacy. |
| **CAISO Contract Manager** | Business/regulatory analyst. Manages commercial agreements. | Manages contract data, verifies annual capacity, generates compliance reports. |
| **CAISO Operator** | Real-time grid operator. May need reference data during drills or events. | Views resource status, locations, and capabilities in a read-only format. |
| **Generator Owner** | External entity under contract to provide Black Start service. | Submits test results, updates unit technical data, views test schedules. |
| **Neighboring BA** | External balancing authority. Requires coordination data. | Accesses limited, shared data via secure portal (e.g., resource locations). |

#### 2.4 Operating Environment
*   **Software:** Web-based application accessible via standard browsers. Backend services running on Linux/Windows servers. Oracle/SQL Server database.
*   **Hardware:** Standard data center infrastructure with high availability (99.5% uptime).
*   **Integration:** Must interface with CAISO's Market Systems, GIS (Geographic Information System), and Document Management systems.

#### 2.5 Design and Implementation Constraints
1.  **Regulatory:** The system must enforce the business rule that the overall Black Start Plan is reviewed and updated at least every **five years** (`CON-001`).
2.  **Performance:** Must support the upload and processing of large contingency study datasets (multiple GB) within a defined batch window.
3.  **Security:** Must comply with NERC CIP standards for access control and audit logging.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Generator owners will have authenticated access to the system for data submission.
*   **Dependency:** Accurate and timely data feeds from the Transmission Planning contingency study tools.
*   **Dependency:** Legal/Contractual frameworks for data sharing with neighboring balancing authorities are in place.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **UI-01:** A dashboard for CAISO users showing key metrics: Total Contracted Capacity vs. Required Capacity, Upcoming Tests, Units with Expiring Certification.
*   **UI-02:** A map-based (GIS) interface to visualize generator locations relative to critical load pockets and transmission paths.
*   **UI-03:** Data entry forms for test results with validation (e.g., start time ≤ 30 minutes for hydro/gas).

##### 3.1.2 Hardware Interfaces
*   None specified beyond standard server/client architecture.

##### 3.1.3 Software Interfaces
*   **SI-01:** **Market Management System:** Import real-time unit identifiers and basic characteristics.
*   **SI-02:** **Document Management System:** Store and link signed contracts, test reports, and study documents.
*   **SI-03:** **Secure External Portal:** Provide limited, read-only access for Generator Owners and Neighboring BAs.

##### 3.1.4 Communications Interfaces
*   **CI-01:** HTTPS/SSL for all web traffic.
*   **CI-02:** SFTP for secure, automated transfer of large data files from study tools.

#### 3.2 Functional Requirements

##### 3.2.1 Contingency Study & Planning Module
*   `FR-001`: The system shall allow CAISO Planners to input or import the results of contingency studies, including required Black Start capacity (MW) and optimal geographic locations (substations/buses).
*   `FR-002`: The system shall calculate and maintain a historical record of the total Black Start capacity **required** for the system, derived from the latest approved study.
*   `FR-003`: The system shall flag the Black Start Plan for mandatory review every five years from its last approval date (`CON-001`).

##### 3.2.2 Contract & Capacity Management Module
*   `FR-004`: The system shall maintain a record of all active Black Start service contracts, including unit(s), contracted capacity (MW), effective dates, and the responsible Generator Owner.
*   `FR-005`: The system shall **annually** compare the total **contracted** capacity against the total **required** capacity and highlight any shortfall.
*   `FR-006`: The system shall generate alerts and reports for contracts nearing expiration (e.g., 90, 60, 30 days prior).

##### 3.2.3 Testing Management Module
*   `FR-007`: The system shall allow CAISO staff to schedule a Black Start capability test for a specific unit, defining the test date and requested output level.
*   `FR-008`: The system shall allow Generator Owners to submit test results, including:
    *   Actual start-up time (from initiation to synchronization).
    *   Actual output (MW) measured at 15-minute intervals over a 4-hour sustained period.
*   `FR-009`: The system shall automatically evaluate test results against performance criteria:
    *   **Start-up Time Criterion:** For hydro and gas turbine units, start-up time must be ≤ **30 minutes**.
    *   **Output Criterion:** The unit must achieve ≥ **99%** of the requested output for the duration of the 4-hour test.
*   `FR-010`: Based on the evaluation in `FR-009`, the system shall automatically update the unit's certification status to either **"Fully Available"** or **"Test Failed"** and record the certification expiry date (typically one year from test date).

##### 3.2.4 Resource Database Module
*   `FR-011`: The system shall maintain a master database of all designated Black Start units with the following core attributes: Unit ID, Name, Type (e.g., Hydro, Gas Turbine), Location (GPS/GIS), Maximum Capacity, Owner, and Current Certification Status.
*   `FR-012`: The system shall maintain a complete, immutable audit log of all changes to unit data, contract terms, and test results.
*   `FR-013`: The system shall generate standard and ad-hoc reports, including but not limited to: System-Wide Black Start Capacity Report, Unit Test History Report, and Compliance Status Report for regulatory submission.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   `NFR-001`: Dashboard and key summary reports shall load in < 3 seconds for 95% of user requests.
*   `NFR-002`: The system shall support at least 50 concurrent users without degradation in performance.

##### 3.3.2 Safety Requirements
*   Not directly applicable (this is a planning system, not a real-time control system).

##### 3.3.3 Security Requirements
*   `NFR-003`: The system shall implement role-based access control (RBAC) aligning with the user classes defined in Section 2.3.
*   `NFR-004`: All user actions (create, read, update, delete) on critical data (contracts, test results) shall be recorded in a tamper-evident audit log.
*   `NFR-005`: All external communications (especially with Generator Owners) shall be encrypted in transit using TLS 1.2 or higher.

##### 3.3.4 Software Quality Attributes
*   **Availability:** `NFR-006` The system shall achieve 99.5% operational availability during business hours (06:00 - 22:00 PT).
*   **Reliability:** `NFR-007` Data loss due to system failure shall be zero. All transactions must be committed reliably.
*   **Maintainability:** `NFR-008` The system shall provide administrative interfaces for managing reference data (e.g., unit types, test criteria) without code deployment.

### 4. System Features (Use Cases - Examples)
*   **UC-01: Annual Capacity Verification**
    *   **Actor:** CAISO Contract Manager
    *   **Flow:** System runs automated check comparing `FR-002` (Required) vs. `FR-004` (Contracted). Report generated highlighting shortfall/surplus. Manager reviews and initiates contracting process if needed.
*   **UC-02: Process Test Results**
    *   **Actor:** Generator Owner
    *   **Flow:** Owner logs in, navigates to scheduled test, uploads results file (`FR-008`). System validates format, evaluates against `FR-009` criteria, updates unit status (`FR-010`), and notifies CAISO. CAISO reviewer approves the automated assessment.

### 5. Appendices

#### 5.1 Data Dictionary (Sample)
| Field Name | Description | Data Type | Constraints |
| :--- | :--- | :--- | :--- |
| `unit_startup_time` | Measured time from start initiation to grid synchronization. | Integer (minutes) | Must be ≥ 0 |
| `test_requested_output` | The MW output level required for the 4-hour sustainability test. | Decimal | Must be ≤ unit_max_capacity |
| `test_actual_output_pct` | The percentage of requested output achieved, calculated as (avg_actual/requested)*100. | Decimal | 0 - 150 |
| `certification_status` | Current operational status of the unit. | Enum | ['Fully Available', 'Test Failed', 'Pending Test', 'Decommissioned'] |

#### 5.2 Acceptance Criteria
The system will be considered acceptable when it successfully executes the core business process:
1.  A CAISO Planner imports a new contingency study, updating the system-wide requirement.
2.  The system flags a capacity shortfall based on existing contracts.
3.  A new contract is added, resolving the shortfall.
4.  A test is scheduled for a unit.
5.  The Generator Owner submits a test report where the unit starts in 25 minutes and sustains 99.5% of requested output.
6.  The system automatically certifies the unit as "Fully Available" for the next 12 months.
7.  All steps are recorded in the audit log and appropriate reports can be generated.