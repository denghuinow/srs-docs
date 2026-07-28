# Software Requirements Specification (SRS)
## Black Start Capability Plan (BCP) Management System
**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the system supporting the California Independent System Operator's (CAISO) formal **Black Start Capability Plan (BCP)**. The purpose of the system is to ensure the reliable planning, testing, maintenance, and documentation of Black Start generators, enabling the restoration of the CAISO-controlled grid following a complete or major blackout.

#### 1.2 Scope
The system encompasses the end-to-end management of Black Start capability, including:
*   Strategic planning for the required quantity and location of Black Start resources.
*   Administration of contracts with generator owners/operators (Reliability Must Run (RMR), Interim, or voluntary).
*   Scheduling, execution, and documentation of performance tests.
*   Maintenance of a master database of designated Black Start units and associated cranking paths.
*   Support for annual operator training on system restoration procedures.

**Out of Scope:**
*   Direct control of grid assets during a real blackout event (executed via SCADA/EMS).
*   Management of generators that can only "safely reject load down to their auxiliary load" but cannot start without external power.
*   The physical execution of generator tests (performed by Generator Owners).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **Black Start** | The capability of a generating unit to start from a completely de-energized state without relying on the external electric power transmission network. |
| **BCP** | Black Start Capability Plan. The formal CAISO plan governed by this system. |
| **CAISO** | California Independent System Operator. |
| **NERC** | North American Electric Reliability Corporation. |
| **WECC** | Western Electricity Coordinating Council. |
| **RMR** | Reliability Must Run. A contract mechanism for essential reliability services. |
| **Cranking Path** | A designated, pre-studied transmission path used to energize the grid from a Black Start unit to the next generator(s) in the restoration sequence. |
| **SCADA** | Supervisory Control and Data Acquisition. The system used for real-time grid control. |

#### 1.4 References
1.  NERC Reliability Standard EOP-005-3: System Restoration from Blackstart Resources
2.  WECC Regional Reliability Standard: System Restoration
3.  CAISO Tariff: Sections related to Reliability Services and Black Start

#### 1.5 Overview
The remainder of this document describes the overall product perspective, specific system features, external interfaces, and non-functional requirements. It is structured to provide a complete specification for developers, testers, and project stakeholders.

### 2. Overall Description

#### 2.1 Product Perspective
The BCP Management System is a mission-critical administrative and planning system within the CAISO's suite of reliability tools. It interfaces with external entities (Generator Owners, Regulators) and internal systems (Market Systems, Grid Models) to ensure compliance and readiness for a grid blackout event.

#### 2.2 Product Functions (High-Level)
1.  **Planning & Analysis:** Determine and validate the required Black Start resource portfolio.
2.  **Contract & Unit Management:** Maintain the registry of contracted Black Start units and their attributes.
3.  **Test Management:** Schedule, track, and document performance tests and their results.
4.  **Cranking Path Documentation:** Create and maintain records of validated restoration paths.
5.  **Reporting & Compliance:** Generate reports for internal review and regulatory submission (WECC/NERC).
6.  **Training Support:** Provide data and scenarios for annual grid operator restoration training.

#### 2.3 User Characteristics
| User Class | Description | Key Responsibilities |
| :--- | :--- | :--- |
| **CAISO Planner** | Power system engineer specializing in restoration planning. | Runs contingency studies, determines Black Start requirements, validates cranking paths. |
| **CAISO Test Administrator** | Coordinator responsible for the Black Start testing program. | Schedules tests, coordinates with Generator Owners, reviews and logs test results. |
| **CAISO System Operator** | Personnel responsible for real-time grid management. | Uses the plan and database for training and, potentially, during an actual restoration event. |
| **Generator Owner/Operator** | External entity under contract to provide Black Start service. | Receives test notifications, submits test results and reports, maintains unit capability. |
| **Compliance Analyst** | CAISO staff responsible for regulatory reporting. | Compiles data from the system to fulfill WECC/NERC data requests. |

#### 2.4 Constraints
*   The system design and outputs must comply with **NERC and WECC reliability standards**.
*   **Hydroelectric unit tests** cannot be scheduled during periods of legally or environmentally constrained water availability.
*   The system must accommodate the contractual and operational differences between **RMR, Interim, and voluntary** Black Start providers.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** A statistical percentage of Black Start units will fail to start or perform correctly during an actual blackout event; the plan must account for this.
*   **Dependency:** The system relies on **Generator Owners/Operators** to accurately perform tests and promptly submit results.
*   **Dependency:** The system requires up-to-date **grid models and contingency analysis tools** to perform valid planning studies.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Planning & Analysis (PLN)
*   **PLN-FR1:** The system shall allow planners to initiate and document the results of annual **contingency studies** used to determine the required quantity and geographical location of Black Start units.
*   **PLN-FR2:** The system shall provide a workflow to **annually verify** that the portfolio of contracted Black Start units meets or exceeds the requirements defined by the latest WECC criteria and study results.
*   **PLN-FR3:** The system shall maintain a library of **documented cranking paths**, linking each Black Start unit to specific "next" generators in the restoration sequence, including path details and study assumptions.

##### 3.1.2 Unit & Contract Management (UCM)
*   **UCM-FR1:** The system shall maintain a **master database** of all designated Black Start generators, including attributes: Unit ID, Location, Owner, Contract Type (RMR/Interim/Voluntary), Fuel Type, Capacity, Start-up Time, Voltage Capability, and Status (Active/Inactive/Under Remediation).
*   **UCM-FR2:** The system shall track key contract dates, performance test history, and any outstanding corrective action plans for each unit.

##### 3.1.3 Test Management (TST)
*   **TST-FR1:** The system shall allow administrators to **schedule periodic performance tests** (e.g., every 3-5 years as per contract) for each contracted Black Start unit.
*   **TST-FR2:** The system shall support the creation of **unscheduled test events** to address failures or specific investigations.
*   **TST-FR3:** The system shall provide a portal or structured data interface for **Generator Owners to submit formal test results**, including:
    *   Actual start and synchronization time.
    *   Voltage profile from no load to full load.
    *   Actual output vs. requested output during the sustained test period (e.g., 4 hours).
*   **TST-FR4:** The system shall record the test outcome (Pass/Fail) based on configurable criteria against submitted data and shall automatically flag units that fail.

##### 3.1.4 Reporting & Compliance (RPT)
*   **RPT-FR1:** The system shall generate the **annual BCP document** for internal review and approval.
*   **RPT-FR2:** The system shall be able to compile and export **test records, unit capability data, and deficiency/corrective action plans** in a format suitable for submission to WECC/NERC within 30 calendar days of a request.
*   **RPT-FR3:** The system shall provide dashboards and alerts showing overall Black Start capability status, upcoming test dates, and units with overdue corrective actions.

##### 3.1.5 Training Support (TRN)
*   **TRN-FR1:** The system shall be able to export a **snapshot of current Black Start resources and cranking paths** for use in annual grid operator restoration training simulations.

#### 3.2 External Interface Requirements

##### 3.2.1 User Interfaces
*   A secure, web-based interface for CAISO staff (Planners, Administrators, Operators).
*   A restricted external portal for Generator Owners to view test schedules and submit results.

##### 3.2.2 Hardware Interfaces
*   None specified beyond standard server infrastructure.

##### 3.2.3 Software Interfaces
*   **SI-1:** Grid Model & Contingency Analysis Tool: The system shall import study results to populate planning requirements and cranking path data.
*   **SI-2:** Market Scheduling System: The system shall interface to schedule and account for **test energy** used during Black Start unit tests.
*   **SI-3:** CAISO SCADA/EMS (Read-Only): The system may display real-time status of Black Start units for context (not for control).

##### 3.2.4 Communication Interfaces
*   Secure email or API-based notifications to Generator Owners for test scheduling and results acknowledgment.
*   Secure file transfer capability for exchanging formal documents with WECC/NERC.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **PER-1:** The system shall support concurrent use by at least 20 CAISO users without significant degradation in response time (< 2 seconds for standard queries).
*   **PER-2:** Generation of the annual BCP report for a portfolio of ~100 Black Start units shall complete within 4 hours.

##### 3.3.2 Safety & Reliability Requirements
*   **REL-1:** The database shall have a minimum availability of 99.5% during business hours.
*   **REL-2:** All data shall be backed up daily with point-in-time recovery capability.

##### 3.3.3 Security Requirements
*   **SEC-1:** Access shall be role-based (RBAC), enforcing strict segregation between CAISO internal users and external Generator Owners.
*   **SEC-2:** All data transmissions containing reliability-critical or market-sensitive information shall be encrypted in transit (TLS 1.2+).
*   **SEC-3:** The system shall maintain a full audit log of all changes to unit status, test results, and plan documents.

##### 3.3.4 Business Rules & Compliance
*   **BR-1:** **Unit Performance:** A Black Start unit must maintain voltage within emergency limits (e.g., +/-10%) from no load to full load during testing.
*   **BR-2:** **Start Time:** Designated start-up times must be verified during testing:
    *   Hydroelectric & Gas Turbine Units: ≤ 30 minutes from start command to synchronization.
    *   Hot Steam Turbine Units: ≤ 2.5 hours from start command to synchronization.
*   **BR-3:** **Test Success Criteria:** A unit passes a performance test if it maintains at least **99% of its requested output** for the duration of the sustained load test (e.g., 4 hours).
*   **BR-4:** **Plan Currency:** The BCP and its supporting database **must be reviewed and updated at least annually**.
*   **BR-5:** **Regulatory Response:** Complete test records and deficiency plans for any unit must be retrievable and deliverable to WECC/NERC **within 30 calendar days** of a formal request.

##### 3.3.5 Data Requirements
*   All historical test data, unit attributes, and plan versions must be retained for a minimum of **10 years** to meet regulatory audit requirements.

### 4. Acceptance Criteria
The system will be considered accepted upon successful demonstration of the following:

1.  **Portfolio Verification:** The system correctly identifies whether the current portfolio of Black Start units meets the annual WECC/study-derived requirements.
2.  **Test Lifecycle:** A full test cycle—from scheduling, through simulated result submission by a Generator Owner, to automatic Pass/Fail assessment based on BR-1, BR-2, and BR-3—is executed successfully.
3.  **Compliance Reporting:** The system generates a compliant data package for a simulated WECC/NERC request within the 30-day window (BR-5).
4.  **Data Integrity:** All master data for Black Start units is accurately maintained, versioned, and auditable (SEC-3).
5.  **Annual Process:** The system supports the complete workflow for generating, reviewing, and approving the annual BCP update (BR-4).

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead System Analyst | | | |
| Development Lead | | | |
| Quality Assurance Lead | | | |