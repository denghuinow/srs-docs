# Software Requirements Specification (SRS)
## Pontis 5.0 Bridge Management System (BMS)

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review
**Prepared for:** AASHTO, Pontis Task Force, Technical Advisory Group
**Prepared by:** [Your Organization/Expert]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for Pontis 5.0, the next-generation Bridge Management System. It serves as a comprehensive agreement between stakeholders—including AASHTO, the Pontis Task Force, state DOT users, and the development contractor—on the capabilities, constraints, and quality attributes of the system. This document will guide the design, development, testing, and acceptance of Pontis 5.0.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Priority:** `(H)` High, `(M)` Medium, `(L)` Low. Assigned based on stakeholder input.
*   **Keywords:** "Shall" indicates a mandatory requirement. "Should" indicates a desirable but not mandatory feature. "May" indicates an optional capability.
*   **Formatting:** User inputs, system outputs, and data elements are denoted in `code blocks`.

#### 1.3 Project Scope
Pontis 5.0 is a comprehensive software application designed to replace the legacy Pontis 4.x series. Its core purpose is to serve as the authoritative repository for bridge inventory, inspection, and condition data, and to provide technically sound, network-level bridge management capabilities. The system will support the full lifecycle of bridge management, from field inspection and data collection to preservation policy development, program simulation, project planning, and regulatory reporting.

**In-Scope:**
*   Web-based and standalone client applications for all defined user roles.
*   Management of Structure, Inspection, Project, Policy, and Simulation data models.
*   Core processes of browsing, inspection entry, calculation, simulation, and project development.
*   Data import/export in standard formats (NBI, PDI, XML).
*   Integration with the BRIDGEWare database architecture.
*   User and role-based security management.

**Out-of-Scope:**
*   Real-time sensor data integration (IoT).
*   Advanced 3D visualization or BIM integration.
*   Detailed, bid-level construction management.
*   Financial/accounting system integration (e.g., SAP, Oracle).

#### 1.4 References
*   AASHTO Pontis 4.x User Manuals and Technical Documentation
*   FHWA Recording and Coding Guide for the Structure Inventory and Appraisal of the Nation's Bridges
*   NCHRP Report 713: "Bridge Preservation Guide"
*   COSMIC-FFP Functional Size Measurement Method
*   Project Charter: Pontis 5.0 Development

### 2. Overall Description

#### 2.1 Product Perspective
Pontis 5.0 is a successor to the client-server based Pontis 4.x system. It will adopt a modern, multi-tier architecture, featuring a web-based "thin client" for most users and a potential standalone application for specialized or offline functions. The system will interact with a central relational database (BRIDGEWare). It must comply with federal NBI reporting standards and is anticipated to support future TransXML schemas for data exchange.

#### 2.2 Product Functions (Summary)
1.  **Data Management:** Securely store and manage bridge inventory, inspection history, projects, and preservation models.
2.  **Inspection Support:** Provide interfaces for entering, validating, and editing field inspection data.
3.  **Analytical Calculation:** Automatically compute derived metrics such as NBI condition ratings and Sufficiency Ratings.
4.  **Preservation Modeling:** Allow engineers to define and update deterioration models, actions, costs, and transition probabilities.
5.  **Program Simulation:** Enable users to run "what-if" scenarios to forecast network condition, needs, and budget requirements.
6.  **Project Planning:** Facilitate the creation and management of improvement projects by assigning recommended work.
7.  **Reporting & Export:** Generate standard reports and export data in required formats for regulatory submission and analysis.
8.  **System Administration:** Configure users, roles, security, and application settings.

#### 2.3 User Classes and Characteristics
| User Class | Primary Goal | Characteristics & Skill Level |
| :--- | :--- | :--- |
| **Inspector** | Accurately record field conditions. | Field personnel; uses mobile/tablet devices; familiar with bridge elements and condition states. |
| **Bridge Management Engineer** | Optimize long-term network performance. | Civil engineer; understands Markovian deterioration modeling and lifecycle cost analysis. |
| **Bridge Project Planner** | Develop feasible capital programs. | Planner/engineer; works with budgets, schedules, and project constraints. |
| **Data Analyst** | Extract insights and generate reports. | Analyzes data trends; creates ad-hoc queries and standard reports. |
| **System Administrator** | Maintain system security and configuration. | IT professional; manages user accounts, roles, and application settings. |

#### 2.4 Operating Environment
*   **Server:** Microsoft Windows Server; Database: SQL Server (BRIDGEWare compatible); Web Server: Microsoft IIS (primary).
*   **Web Client:** Designed for Microsoft Internet Explorer; shall be compatible with other modern browsers (Chrome, Firefox, Edge) where feasible.
*   **Standalone Client:** Requires Windows XP or later and .NET Framework [Version TBD].
*   **Field Devices:** Support for tablet or handheld computers is an undecided issue (see Section 8).

#### 2.5 Design and Implementation Constraints
1.  **Backward Compatibility:** Must support migration of data and, where possible, logic from existing Pontis 4.x implementations.
2.  **Regulatory Compliance:** Must adhere to current FHWA NBI coding standards and be adaptable to future changes.
3.  **Integration:** Database schema must align with the broader BRIDGEWare architecture.
4.  **Technology:** Initial web client release targeted for Microsoft Internet Explorer.

#### 2.6 Assumptions and Dependencies
*   **D-1:** The Functional Requirements Specification will be approved before detailed development begins.
*   **D-2:** The BRIDGEWare Integration TAG will provide timely database schema coordination.
*   **D-3:** Results from NCHRP Project 12-67 (Multiple-Objective Optimization) will be available for incorporation.
*   **D-4:** A stable TransXML schema from NCHRP Project 20-64 will be available post-initial release.
*   **Assumption:** Agency IT environments will support the specified server and client configurations.

### 3. System Features and Requirements

#### 3.1 Feature: Data Browsing and Selection
**Description:** Users shall be able to find, filter, view, and select bridge structures and project records.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-010** | The system shall provide a search interface to find structures by `Structure ID`, `Feature Intersected`, `Location`, or `Route`. | H |
| **FR-011** | The system shall allow users to apply multiple filters (e.g., `Construction Date` range, `NBI Rating` threshold) to the inventory list. | H |
| **FR-012** | The system shall display a summary view of a selected structure, including key inventory fields and the most recent `Inspection Date`. | H |
| **FR-013** | The system shall allow users to browse and filter `Project` records by `Program`, `Status`, and `Budget` range. | M |

#### 3.2 Feature: Inventory and Inspection Management
**Description:** Inspectors shall create and maintain accurate structure inventory and inspection records.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-020** | The system shall provide forms for creating and editing a `Structure` record, including all mandatory NBI inventory items. | H |
| **FR-021** | The system shall allow an authorized user to create a new `Inspection` record linked to a specific `Structure ID`. | H |
| **FR-022** | The inspection entry interface shall guide the user through recording `Element Conditions` using standardized condition states. | H |
| **FR-023** | The system shall perform basic validation on inspection data entry (e.g., valid date ranges, numeric limits). | H |
| **FR-024** | Upon saving an inspection, the system shall automatically trigger the **Calculate Derived Results** process (FR-030). | H |

#### 3.3 Feature: Analytical Calculations
**Description:** The system shall automatically compute key engineering and regulatory metrics.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-030** | The system shall calculate the four NBI Condition Ratings (Deck, Superstructure, Substructure, Culvert) based on entered element conditions and defined rules. | H |
| **FR-031** | The system shall calculate the Sufficiency Rating (SR) according to the latest FHWA formula. | H |
| **FR-032** | All calculated ratings shall be stored with the `Inspection` record and be clearly marked as system-generated. | H |

#### 3.4 Feature: Preservation Model Development
**Description:** Engineers shall maintain the deterioration and cost models that drive simulation.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-040** | The system shall provide an interface for defining and updating `Preservation Policy` records, including `Element`, `Action`, and `Cost`. | H |
| **FR-041** | The system shall allow an engineer to define a matrix of transition probabilities (deterioration model) for each element. | H |
| **FR-042** | The system shall version preservation policies to track changes over time and associate policies with specific `Simulation Scenario` runs. | M |

#### 3.5 Feature: Program Simulation
**Description:** Users shall configure and execute network-level simulations to forecast conditions and needs.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-050** | The system shall allow a user to create a `Simulation Scenario` by defining a `Timeframe`, budget constraints, and selecting which preservation policies to apply. | H |
| **FR-051** | The system shall execute a Markov-based simulation across the selected network of structures. | H |
| **FR-052** | The system shall generate results including forecasted condition trends, recommended actions by year, and estimated costs. | H |
| **FR-053** | Simulation `Results` shall be stored and associated with the `Scenario ID` for later review and use in project development. | H |

#### 3.6 Feature: Project Development
**Description:** Planners shall create and manage projects based on simulation outputs or inspector recommendations.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-060** | The system shall allow a user to create a new `Project` record, assigning a `Project Name`, `Program`, `Budget`, and `End Date`. | H |
| **FR-061** | The system shall provide a mechanism to assign recommended work items from a `Simulation Scenario` or an inspection report to a `Project`. | H |
| **FR-062** | The system shall track project `Status` (e.g., Planned, Funded, In Progress, Completed). | M |

#### 3.7 Feature: Data Exchange and Management
**Description:** The system shall support import, export, and validation of data in standard formats.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-070** | The system shall export bridge inventory and inspection data in the official FHWA NBI submission format. | H |
| **FR-071** | The system shall import data from PDI (Pontis Data Interchange) files to support migration from Pontis 4.x. | H |
| **FR-072** | The system shall support the import and export of data using an XML schema, with future alignment to TransXML. | M |
| **FR-073** | The system shall provide data validation tools to check for consistency and compliance with NBI rules before export. | M |

#### 3.8 Feature: System Administration and Security
**Description:** Administrators shall manage users, roles, and system configurations.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-080** | The system shall integrate with agency Single Sign-On (SSO) systems where available. | H |
| **FR-081** | The system shall provide application-level security controls, allowing administrators to define `User` `Roles` (e.g., Inspector, Engineer, Admin) and assign specific permissions. | H |
| **FR-082** | The system shall allow setting `Access Filters` based on user role (e.g., an inspector may only see structures in their assigned district). | M |
| **FR-083** | The system shall provide an interface for managing application-wide configurations and settings. | M |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The web interface shall be clean, intuitive, and task-oriented, using a consistent navigation scheme.
*   Data entry forms shall provide clear labels, input validation, and contextual help.
*   All graphical user interfaces shall be designed to meet ADA Section 508 compliance standards to the level determined in Section 8.

#### 4.2 Hardware Interfaces
*   The system shall operate on standard server hardware meeting the specified software requirements.
*   Support for barcode scanners, digital cameras, or GPS units connected to field inspection devices is TBD (see Undecided Issues).

#### 4.3 Software Interfaces
*   **BRIDGEWare Database:** Pontis 5.0 shall read from and write to the shared BRIDGEWare database schema as defined by the integration TAG.
*   **Authentication Service:** Shall interface with LDAP/Active Directory or other SSO providers.
*   **Reporting Engine:** May integrate with a third-party reporting tool (e.g., SQL Server Reporting Services) for advanced report generation.

#### 4.4 Communications Interfaces
*   Client-server communication shall use HTTPS for all web traffic to ensure data security in transit.
*   The system shall be capable of operating in environments with intermittent connectivity (for field data collection, functionality TBD).

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NFR-001:** The system shall allow 95% of users to successfully log in within 2 seconds under normal load conditions.
*   **NFR-002:** The system shall generate a standard formatted report (e.g., Structure Inventory Report) within 20 seconds for 95% of requests.
*   **NFR-003:** A program simulation run for a typical state-sized network (e.g., 5,000 structures over 20 years) shall complete within 15 minutes.

#### 5.2 Safety Requirements
*   Not directly applicable. Safety is governed by the engineering processes and data accuracy supported by the system.

#### 5.3 Security Requirements
*   **NFR-010:** All user authentication shall be performed via SSO or the application's secure login.
*   **NFR-011:** User sessions shall timeout after [30] minutes of inactivity.
*   **NFR-012:** All sensitive data, including inspection records and user credentials, shall be encrypted at rest and in transit.
*   **NFR-013:** The system shall maintain an audit log of all user actions that create, modify, or delete critical data (e.g., inventory, inspections, policies).

#### 5.4 Software Quality Attributes
*   **Usability (NFR-020):** A user familiar with bridge management concepts shall be able to perform core operations (browse, create inspection, run a simple report) with no more than two days of formal training.
*   **Maintainability (NFR-021):** Source code shall be modular and include inline comments. A comprehensive technical design document shall be delivered.
*   **Reliability (NFR-022):** The system shall achieve 99% operational availability during standard business hours (8 AM - 6 PM local time).
*   **Portability (NFR-023):** The database layer shall be designed to be independent of the application logic to facilitate potential future migration to other database platforms.

### 6. Data Model (Entity-Attribute Summary)
The following core entities shall be supported. This is a logical model; the physical schema will be defined in the Database Design Document.

*   **Structure** (`structure_id` PK, name, feature_intersected, location_details, construction_date, ...)
*   **Inspection** (`inspection_id` PK, `structure_id` FK, inspection_date, inspector_id, deck_cond_rating, sufficiency_rating, ...)
*   **Inspection_Element** (`inspection_id` FK, `element_id` FK, condition_state, quantity, ...)
*   **Project** (`project_id` PK, project_name, program_code, status, total_budget, end_date, ...)
*   **Preservation_Policy** (`policy_id` PK, element_code, action_code, estimated_cost, effective_date, ...)
*   **Transition_Matrix** (`policy_id` FK, from_state, to_state, probability)
*   **Simulation_Scenario** (`scenario_id` PK, scenario_name, timeframe_years, budget_constraint, run_date, results_summary, ...)
*   **User** (`user_id` PK, username, role, email, district_filter, ...)

### 7. Appendices

#### 7.1 Glossary
*   **BMS:** Bridge Management System.
*   **NBI:** National Bridge Inventory.
*   **PDI:** Pontis Data Interchange.
*   **SR:** Sufficiency Rating.
*   **TAG:** Technical Advisory Group.
*   **TransXML:** AASHTO transportation data exchange standard.

#### 7.2 Analysis Models
*   **State Transition Diagrams:** To be developed for element deterioration models.
*   **Use Case Diagrams:** To be developed detailing interactions for each key process in Section 3.

### 8. Undecided Issues and TBDs
The following issues require resolution by the governing stakeholders (Pontis Task Force, TAG, AASHTO) prior to or during the design phase:
1.  The specific level of ADA (Section 508) compliance and the implementation approach.
2.  The strategy for migrating user-customized PowerBuilder forms and reports from Pontis 4.x.
3.  Final decision on official support for web servers other than Microsoft IIS (e.g., Apache).
4.  Resolution of "may" requirements (Waiting Room): electronic signatures on inspections, GIS mapping interface, detailed data archiving/purging policies.
5.  The licensing model and fee structure for web application users.
6.  Requirements and design for support of tablet/handheld computers in the field inspection process.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Pontis Task Force Lead** | | | |
| **AASHTO Representative** | | | |
| **Technical Advisory Group Lead** | | | |
| **Development Contractor Lead** | | | |