# Software Requirements Specification (SRS)
## Black Start Capability Plan (BCP) Management System

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for a system to support the management of the California Independent System Operator's (CAISO) Black Start Capability Plan (BCP). The system will facilitate planning, testing, recordkeeping, and training activities essential for maintaining grid restoration capabilities following a major blackout, in compliance with WECC and NERC reliability standards.

#### 1.2 Scope
The system will support the end-to-end BCP lifecycle within the CAISO Balancing Authority Area. The scope includes:
*   Management of voluntary, interim, and Reliability Must-Run (RMR) contracted Black Start units.
*   Administration of the annual planning, contracting, and testing cycles.
*   Maintenance of a central repository for all BCP-related data.
*   Coordination with internal stakeholders (Grid Planners, Dispatchers) and external entities (Unit Owners, Transmission Owners, WECC).
*   Support for compliance reporting and audit readiness.

**Out of Scope:**
*   Real-time grid control or SCADA functionality.
*   Physical execution of Black Start tests.
*   Financial settlement or billing for RMR contracts.
*   Development of the underlying system simulator for training (integration only).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **BCP** | Black Start Capability Plan |
| **CAISO** | California Independent System Operator |
| **RMR** | Reliability Must-Run |
| **WECC** | Western Electricity Coordinating Council |
| **NERC** | North American Electric Reliability Corporation |
| **EOP** | Emergency Operations Procedure (NERC Standard) |
| **Cranking Path** | A designated transmission path to be energized by a Black Start unit to restore other generation or load. |

#### 1.4 References
1.  NERC Standard EOP-005: System Restoration from Blackstart Resources
2.  NERC Standard EOP-009: System Restoration Coordination
3.  WECC Regional Criteria
4.  CAISO Tariff and Business Practice Manuals

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the system and its stakeholders. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements. Appendices contain supporting information.

### 2. Overall Description

#### 2.1 Product Perspective
The BCP Management System is a new, standalone web-based application. It will integrate with existing CAISO systems via secure APIs for data exchange (e.g., unit master data, dispatch logs) and will generate reports for external entities like WECC.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics & Key Needs |
| :--- | :--- |
| **CAISO Grid Planner** | Performs complex studies. Needs analytical tools, scenario modeling, and reporting capabilities. |
| **CAISO Real-Time Dispatcher** | Operates in a high-pressure, time-sensitive environment. Requires immediate, clear notifications and quick access to unit status and cranking paths. |
| **Black Start Unit Owner/Operator** | External user. Needs a portal to submit test requests, results, and data; view contract terms; and receive notifications. |
| **CAISO Operations Support Test Administrator** | Manages processes. Needs workflow tools, form management, calculation engines, and tracking dashboards. |
| **Transmission Owner / Neighboring BA** | External reviewer. Needs secure, read-only access to relevant cranking path and coordination documents. |
| **WECC/NERC Auditor** | External auditor. Needs secure, read-only access to comprehensive compliance documentation and test records. |
| **CAISO System Administrator** | Maintains system health, manages user accounts and permissions. |

#### 2.3 Operating Environment
*   **Software:** Web-based interface compatible with modern browsers (Chrome, Firefox, Edge). Backend built on a standard enterprise stack (e.g., Java/.NET, SQL database).
*   **Hardware:** Hosted on CAISO's secure, fault-tolerant data centers.
*   **Networking:** Accessible via CAISO's corporate network and a secure external portal for stakeholders.

#### 2.4 Design and Implementation Constraints
1.  Must comply with CAISO cybersecurity policies (CIP) and NERC Critical Infrastructure Protection (CIP) standards.
2.  Must support electronic signatures for official documents where required.
3.  Data retention policies must align with regulatory requirements (minimum 5 years).
4.  Must provide APIs for future integration with a system simulator for training.

#### 2.5 User Documentation
The system shall provide:
*   Online help context-sensitive to user roles.
*   Administrator guides.
*   External user guides for Unit Owners and Transmission Owners.
*   API documentation for integrators.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Black Start Unit Owners will have reliable internet access to use the external portal.
*   **Dependency:** Accurate and timely data feeds from source CAISO systems (e.g., Generator Master Data).
*   **Dependency:** Continued evolution and publication of NERC/WECC standards will be tracked and incorporated.

### 3. System Features and Requirements

#### 3.1 Feature 1: BCP Planning & Contract Management
**3.1.1 Description**
This feature supports the annual evaluation of Black Start needs, contingency studies, and the management of RMR/Interim contracts.

**3.1.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-PLAN-01** | The system shall allow Grid Planners to create, manage, and archive Contingency Study records, including scenario description, outage magnitude, and required capacity. |
| **FR-PLAN-02** | The system shall provide tools to associate Black Start Units and Cranking Paths with specific Contingency Studies. |
| **FR-PLAN-03** | The system shall manage the lifecycle of RMR/Interim Contracts, including start/end dates, technical requirements, and availability limits. |
| **FR-PLAN-04** | The system shall generate alerts 90 days prior to contract expiration for renewal actions. |

#### 3.2 Feature 2: Black Start Test Lifecycle Management
**3.2.1 Description**
This feature manages the initiation, execution, reporting, and evaluation of Black Start tests.

**3.2.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-TEST-01** | The system shall allow the Test Administrator to issue a formal Black Start Test Notice, specifying unit, date, and requirements. |
| **FR-TEST-02** | The system shall provide an external portal for Unit Owners to submit a Black Start Test Request Form. |
| **FR-TEST-03** | Upon test completion, the system shall prompt the Unit Owner (via portal) to submit a formal Test Result Letter and ambient temperature data. |
| **FR-TEST-04** | The system shall automatically log a phone notification event to the dispatcher (time/date) and link it to the test record. |
| **FR-TEST-05** | The system shall calculate unit availability percentage based on submitted output MWh versus requested output during the standard 4-hour test window. |

#### 3.3 Feature 3: Centralized Data Repository & Recordkeeping
**3.3.1 Description**
This feature maintains the system of record for all BCP-related domain entities.

**3.3.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-DATA-01** | The system shall maintain a master list of Black Start Units with all associated attributes (ID, Owner, Location, Capacity, Type, Latest Test Date). |
| **FR-DATA-02** | The system shall store all Test records, linking them to the specific Unit and Contract. |
| **FR-DATA-03** | The system shall store Cranking Path documentation, including diagrams (as references or uploads) and switching requirements. |
| **FR-DATA-04** | The system shall enforce referential integrity (e.g., a Test must be associated with a valid Unit ID). |
| **FR-DATA-05** | The system shall provide a bulk data update utility for annual reviews, with full audit logging. |

#### 3.4 Feature 4: Compliance Reporting & Stakeholder Coordination
**3.4.1 Description**
This feature enables the generation of reports and provides secure access to external stakeholders.

**3.4.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-REP-01** | The system shall generate a standardized annual BCP summary report for WECC submission. |
| **FR-REP-02** | The system shall allow authorized WECC/NERC users to view and download test documentation and compliance evidence. |
| **FR-REP-03** | The system shall provide a secure, view-only portal for Transmission Owners to access Cranking Paths relevant to their assets. |
| **FR-REP-04** | The system shall generate ad-hoc reports on test history, unit status, and contract coverage. |

#### 3.5 Feature 5: Training & Awareness
**3.5.1 Description**
This feature tracks operator training related to system restoration and Black Start procedures.

**3.5.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-TRN-01** | The system shall maintain Training Records for each session, including date, participants, scenario, and critique. |
| **FR-TRN-02** | The system shall alert managers when an operator's annual restoration training is due or overdue. |
| **FR-TRN-03** | The system shall provide a repository for storing and versioning training materials and simulation scenarios. |

### 4. Non-Functional Requirements

#### 4.1 Performance
| ID | Requirement |
| :--- | :--- |
| **NFR-PER-01** | The system shall support at least 50 concurrent users with an average response time of <2 seconds for standard UI interactions. |
| **NFR-PER-02** | Generation of standard compliance reports shall complete within 5 minutes. |

#### 4.2 Reliability & Availability
| ID | Requirement |
| :--- | :--- |
| **NFR-REL-01** | The system shall achieve 99.5% operational availability during business hours (0600-2000 PT). |
| **NFR-REL-02** | All data transactions shall be logged to ensure recoverability in case of failure. |

#### 4.3 Security
| ID | Requirement |
| :--- | :--- |
| **NFR-SEC-01** | The system shall implement role-based access control (RBAC) as defined in Section 2.2. |
| **NFR-SEC-02** | All external portal access shall require multi-factor authentication (MFA). |
| **NFR-SEC-03** | All data in transit and at rest shall be encrypted using industry-standard protocols. |
| **NFR-SEC-04** | The system shall maintain a complete audit trail of all data changes, including user, timestamp, and changed values. |

#### 4.4 Usability
| ID | Requirement |
| :--- | :--- |
| **NFR-USA-01** | The user interface shall conform to CAISO's internal design standards for consistency. |
| **NFR-USA-02** | Critical dispatcher notifications (e.g., test completion) shall be presented prominently on the dispatcher's landing page. |

#### 4.5 Compliance
| ID | Requirement |
| :--- | :--- |
| **NFR-COM-01** | The system shall facilitate compliance with NERC EOP-005 and EOP-009 by managing required evidence. |
| **NFR-COM-02** | The system shall support data retention policies that meet or exceed regulatory minimums. |

### 5. Appendices

#### Appendix A: Data Model (Entity-Relationship Diagram Snippet)
```sql
-- Core Table Definitions
TABLE BlackStartUnit {
  unit_id PK VARCHAR(20)
  owner VARCHAR(100)
  location VARCHAR(255)
  capacity_mw DECIMAL
  unit_type VARCHAR(50)
  latest_test_date DATE
}

TABLE BlackStartTest {
  test_id PK VARCHAR(30)
  unit_id FK VARCHAR(20)
  test_date DATE
  duration_hours DECIMAL
  status VARCHAR(20) -- SUCCESS, FAILURE, CANCELLED
  output_mwh DECIMAL
  ambient_temp DECIMAL
  result_letter_url VARCHAR(255)
}

TABLE CrankingPath {
  path_id PK VARCHAR(20)
  source_unit_id FK VARCHAR(20)
  diagram_reference VARCHAR(255)
}
```

#### Appendix B: Open Issues & TBDs
The following items from the input summary are noted as unresolved and require future business decision:
1.  The specific failure percentage for planning reliability (to be determined by CAISO studies).
2.  Negotiated start time limits for unspecified technologies or external units.
3.  Protocol for unannounced CAISO performance tests on RMR/Interim units.
4.  Integration specification for a future system simulator.
5.  Standardization (or lack thereof) for corrective action plans.
6.  Method for CAISO to independently source ambient temperature data.

*These issues will be tracked in the project's issue log and resolved prior to the final design phase.*