# Software Requirements Specification (SRS)
## Pontis 5.0 Bridge Management System

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review
**Prepared for:** AASHTO, Pontis Task Force, Technical Advisory Group (TAG)
**Prepared by:** [Your Name/Organization]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for Pontis 5.0, the next-generation Bridge Management System (BMS). It serves as a comprehensive guide for stakeholders, developers, testers, and project managers to understand the system's capabilities, constraints, and interfaces. The primary audience includes the Pontis Task Force, the Technical Advisory Group (TAG), AASHTO, and the development contractor.

#### 1.2 Scope
Pontis 5.0 is a comprehensive software application designed to replace the Pontis 4.x product line. Its core purpose is to enable transportation agencies to manage bridge inventory, conduct condition inspections, develop preservation models, perform network-level and structure-level analyses, plan projects and programs, and generate regulatory reports.

**In-Scope:**
*   Modernization of the existing Pontis application using current Microsoft .NET technologies.
*   Core bridge management functionalities: data browsing, inventory, inspection, modeling, simulation, analysis, project/program development, and reporting.
*   Integration with external systems (GIS, other BRIDGEWare products, NBI reporting).
*   Data management operations (validation, import/export, archiving).
*   System administration and configuration.
*   Phased release strategy to manage complexity and risk.

**Out-of-Scope (Non-Goals):**
*   Assuming a uniform operating environment across all user agencies.
*   Being designed exclusively as a hosted (SaaS) application, though it must be capable of operating in such environments.
*   Providing specialized, native support for tablet or handheld computers in the initial releases.
*   Mandating a specific, single web server technology other than core compatibility.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **AASHTO:** American Association of State Highway and Transportation Officials
*   **BMS:** Bridge Management System
*   **FHWA:** Federal Highway Administration
*   **GIS:** Geographic Information System
*   **NBI:** National Bridge Inventory
*   **PDI:** Pontis Data Interchange
*   **SD/FO:** Structurally Deficient / Functionally Obsolete
*   **SLA:** Service Level Agreement
*   **SSO:** Single Sign-On
*   **TAG:** Technical Advisory Group
*   **TransXML:** AASHTO's XML-based data exchange standard for transportation data.

#### 1.4 References
*   FHWA National Bridge Inventory Coding Guide
*   AASHTOWare BRIDGEWare Program Documentation
*   TransXML Schema Definitions
*   Pontis 4.x Technical and User Documentation

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its stakeholders, and operating environment. Section 3 details specific system requirements, including functional, interface, and non-functional requirements. Appendices may contain supplementary diagrams or data models.

### 2. Overall Description

#### 2.1 Product Perspective
Pontis 5.0 is a major evolution within the AASHTOWare BRIDGEWare suite. It is a standalone application that must integrate with companion products like Virtis (load rating) and Opis, as well as external systems such as agency GIS platforms and enterprise authentication services. It replaces the legacy Pontis 4.x system, requiring consideration for data migration and user transition.

#### 2.2 Stakeholders and User Characteristics
| Stakeholder Group | Primary Interest / Role |
| :--- | :--- |
| **Pontis Users** (Inspectors, Engineers, Planners) | Day-to-day system operation: data entry, analysis, planning, reporting. Varies in technical proficiency. |
| **Pontis Task Force** | Oversees overall product quality, technical correctness, and validates that requirements are met. |
| **Pontis 5.0 Requirements TAG** | Defines detailed requirements, architecture, and implementation plans outlined in this SRS. |
| **BRIDGEWare Integration TAG** | Ensures compatible design and data integration with other BRIDGEWare products (Virtis, Opis). |
| **AASHTO** | Product owner; manages project, licensing, marketing, and final decisions on policy issues. |
| **Development Contractor** | Responsible for detailed design, development, testing, and delivery based on this SRS. |

#### 2.3 Operating Environment
*   **Software:** Built on the Microsoft .NET Framework. Client components may be Windows-based; server components must support web services.
*   **Database:** Must support Oracle, Microsoft SQL Server, and Sybase RDBMS.
*   **Authentication:** Must integrate with enterprise directory services (e.g., Active Directory, LDAP).
*   **Interoperability:** Must interface with GIS mapping libraries (e.g., ESRI, Intergraph) and support standard data exchange formats (TransXML, PDI, NBI).

#### 2.4 Design and Implementation Constraints
1.  **Technology:** Primary development must use mainstream Microsoft .NET technologies.
2.  **Backward Compatibility:** Must support import/export of Pontis 4.x PDI format data.
3.  **Regulatory Compliance:** Must generate FHWA NBI report files that comply with the current coding guide.
4.  **Architecture:** Must allow for a phased release strategy (core, planning, simulation modules).

#### 2.5 User Documentation
Comprehensive user manuals, online help, and administrator guides must be delivered with the software. Documentation must cover all functional modules, data import/export procedures, and system administration tasks.

#### 2.6 Assumptions and Dependencies
*   User agencies possess the necessary hardware and database licenses.
*   AASHTO will provide guidance on selected undecided issues (e.g., report generator tool, ADA compliance level) prior to impacted development phases.
*   The system depends on the continued maintenance and availability of key third-party technologies (.NET Framework, supported RDBMS).

### 3. System Requirements

#### 3.1 Functional Requirements
The system shall provide the following core functional capabilities, aligned with the main use cases.

**FR-1: Browse Bridge & Project Data**
*   **FR-1.1:** The system shall allow users to search and filter the inventory of structures and projects based on a configurable set of criteria (e.g., location, condition, project status).
*   **FR-1.2:** The system shall provide a map-based interface (via GIS integration) to visually select structures and projects and view their locations.
*   **FR-1.3:** Upon selection, the system shall display detailed information for a single structure or project.

**FR-2: Bridge Inventory & Inspection Management**
*   **FR-2.1:** The system shall allow authorized users to create, view, edit, and delete inventory records for bridge structures.
*   **FR-2.2:** The system shall allow inspectors to create, view, edit, and delete inspection records for a specific structure, including element-level condition state data.
*   **FR-2.3:** The system shall perform real-time validation on entered inspection data against configurable business rules and highlight errors/warnings before saving.
*   **FR-2.4:** The system shall calculate derived ratings (NBI condition ratings, Sufficiency Rating, SD/FO status) based on the latest inspection data using defined algorithms.

**FR-3: Preservation Model Development**
*   **FR-3.1:** The system shall allow advanced users (e.g., engineers) to view and update deterioration probability matrices for bridge elements.
*   **FR-3.2:** The system shall allow users to define and update action costs for preservation, rehabilitation, and replacement work.
*   **FR-3.3:** The system shall support the development of optimal preservation policies based on updated models and allow for health index targeting exercises.

**FR-4: Program Simulation (Network-Level Analysis)**
*   **FR-4.1:** The system shall allow users to configure simulation scenarios, including selecting a network of bridges, defining a preservation policy, and setting budget constraints over a multi-year period.
*   **FR-4.2:** Upon execution, the system shall generate a long-term (e.g., 10+ year) schedule of recommended work actions for the entire network, with associated annual and total costs.
*   **FR-4.3:** The system shall present simulation results showing trends in network condition, budget needs, and the impact of varying budget levels.

**FR-5: Bridge Analysis (Structure-Level Analysis)**
*   **FR-5.1:** The system shall allow a user to select a specific bridge and model the future condition impact of applying one or more potential work items.
*   **FR-5.2:** The analysis shall project changes in element condition states and overall bridge ratings over time based on the selected work.

**FR-6: Project & Program Development**
*   **FR-6.1:** The system shall allow planners to create projects by selecting work recommendations from simulations or from inspector-generated work candidates.
*   **FR-6.2:** The system shall create a project record encapsulating selected work items, estimated costs, and links to affected structures.
*   **FR-6.3:** The system shall warn a user if the cost of a project exceeds the budget of the assigned program.
*   **FR-6.4:** The system shall allow users to create and manage funding programs, define their timeframes and funding sources, and assign projects to them.

**FR-7: Data Management**
*   **FR-7.1:** The system shall validate data integrity according to configurable rules.
*   **FR-7.2:** The system shall import data from standard formats: NBI files, PDI files (Pontis 4.x), and TransXML schema files.
*   **FR-7.3:** The system shall export data to standard formats: NBI files, PDI files, and TransXML schema files.
*   **FR-7.4:** The system shall provide functionality to archive and retrieve historical data.
*   **FR-7.5:** The system shall support data integration workflows with other BRIDGEWare products (e.g., receiving load rating data from Virtis).

**FR-8: System Administration**
*   **FR-8.1:** The system shall provide role-based access control (RBAC). Administrators shall be able to manage users, assign roles, and define permissions at the functional and field level.
*   **FR-8.2:** The system shall integrate with enterprise authentication services (e.g., Active Directory/LDAP) for user login.
*   **FR-8.3:** Administrators shall be able to configure system parameters, business rules, and reference data (e.g., element types, action types).

#### 3.2 External Interface Requirements

**EI-1: GIS Interface**
*   **Type:** Bidirectional, Component Integration
*   **Purpose:** Spatial visualization and query.
*   **Input:** Bridge/Project selections from Pontis; spatial queries (e.g., "select all bridges within county X") from GIS.
*   **Output:** Map display in Pontis with bridge locations; list of records in Pontis from a GIS spatial selection.
*   **Performance:** Map refresh or selection result display in <5 seconds.

**EI-2: BRIDGEWare Integration (Virtis/Opis)**
*   **Type:** Bidirectional, Data Exchange
*   **Purpose:** Synchronize related bridge data (e.g., load ratings, operational data).
*   **Input:** Data updates from Virtis/Opis.
*   **Output:** Data updates from Pontis.
*   **Constraint:** Must ensure transaction integrity and support coordinated software release cycles.

**EI-3: TransXML Data Exchange**
*   **Type:** Bidirectional, File-based
*   **Purpose:** Standardized import/export of bridge data with external systems.
*   **Input:** XML file conforming to the TransXML bridge schema.
*   **Output:** Pontis data exported as a TransXML-compliant XML file.
*   **Constraint:** Must successfully validate against and comply with the published TransXML schema.

**EI-4: National Bridge Inventory (NBI) Reporting**
*   **Type:** Output, File-based
*   **Purpose:** Generate regulatory submission files for the FHWA.
*   **Input:** Pontis bridge inventory and inspection data.
*   **Output:** A correctly formatted file adhering to the current FHWA NBI Coding Guide.
*   **Constraint:** The system design must accommodate updates to the NBI Coding Guide with minimal re-engineering.

**EI-5: Authentication Service**
*   **Type:** Input, Service Call
*   **Purpose:** Verify user credentials.
*   **Input:** User ID and password (or security token).
*   **Output:** Authentication success/failure and user role/group information.
*   **Performance:** Login authentication process completes in <2 seconds.
*   **Security:** Must support secure (encrypted) communication.

#### 3.3 Non-Functional Requirements

**NF-1: Performance**
*   **NF-1.1:** User login and logout operations shall complete within 2 seconds under normal load.
*   **NF-1.2:** Generation of a standard condition summary report for 250 bridges shall complete within 20 seconds.
*   **NF-1.3:** The GIS map interface shall refresh or respond to selection queries within 5 seconds.

**NF-2: Reliability & Availability**
*   **NF-2.1:** The system shall maintain 98% operational availability during defined agency business hours (18 hours/day, 353 days/year), excluding scheduled maintenance windows.

**NF-3: Security**
*   **NF-3.1:** The system shall implement Role-Based Access Control (RBAC) to restrict functionality based on user roles.
*   **NF-3.2:** The system shall support field-level security to control read/write access to specific data fields.
*   **NF-3.3:** The system shall integrate with enterprise Single Sign-On (SSO) solutions where configured.
*   **NF-3.4:** All authentication traffic shall be encrypted.

**NF-4: Compliance**
*   **NF-4.1:** The system shall comply with data export requirements for the FHWA NBI.
*   **NF-4.2:** The system architecture shall be designed to accommodate changes in the NBI Coding Guide.

**NF-5: Maintainability & Observability**
*   **NF-5.1:** The application shall adhere to standard .NET logging practices (e.g., using a framework like log4net or NLog).
*   **NF-5.2:** The system shall provide diagnostic reports and logs for administrator use in troubleshooting.

#### 3.4 Acceptance Criteria
*   **Inspection Data Entry:** Given an inspector is logged in, when they submit a new inspection with invalid data (e.g., condition state out of bounds), then the system shall prevent saving and clearly highlight the specific errors.
*   **Rating Calculation:** Given a complete inspection is saved, when the rating calculation function is executed, then the computed NBI ratings and Sufficiency Rating shall match the results from an independent, verified calculation engine.
*   **Program Simulation:** Given a defined network of 100 bridges and a 10-year budget constraint, when a program simulation is run, then the system shall produce a non-empty list of recommended work actions for each year of the analysis period, with a total cost not exceeding the defined budget constraint.
*   **Project Budget Warning:** Given a project with an estimated cost of $1.5M is assigned to a program with a remaining budget of $1.0M, when the user saves the project assignment, then the system shall display a clear warning message about the budget overrun before finalizing the save.

### 4. Appendices

#### 4.1 Domain Model (Key Entities)
1.  **Structure:** `StructureID* (PK), Name, Location, ...Inventory Fields`
2.  **Inspection:** `InspectionID* (PK), StructureID (FK), InspectionDate, InspectorID (FK), ...`
3.  **Element:** `ElementID* (PK), StructureID (FK), Type, Environment, Quantity, ConditionState`
4.  **Work Recommendation:** `RecommendationID* (PK), StructureID (FK), ElementID (FK), ActionType, Priority, EstimatedCost, Source (Simulation/Inspection)`
5.  **Project:** `ProjectID* (PK), Name, Description, Status, TotalBudget, ProgramID (FK)`
6.  **Program:** `ProgramID* (PK), Name, StartYear, EndYear, TotalFunding, FundingSource`
7.  **User:** `UserID* (PK), UserName, Role, ...AuthenticationData`
8.  **Scenario/SimulationRun:** `ScenarioID* (PK), Name, Parameters (JSON/XML), RunDate, Results`

#### 4.2 Release Strategy & Milestones (Summary)
1.  **Phase 1 - Design & Prototype:** June 2006. Deliver detailed design document and functional prototypes for key areas.
2.  **Phase 2 - Pontis 5.0 (Core + Inspection):** June 2007. Core framework, browsing, inventory, inspection, and basic reporting.
3.  **Phase 3 - Pontis 5.1 (Project Planning + Gateway):** June 2008. Project/Program development, enhanced data exchange gateways.
4.  **Phase 4 - Pontis 5.2 (Preservation + Simulation):** June 2010. Preservation model development, program simulation, bridge analysis, advanced configuration.
5.  **Testing:** Alpha and Beta testing periods scheduled prior to each major release.

#### 4.3 Open Issues and Decisions Pending
| Issue | Responsible Party | Notes |
| :--- | :--- | :--- |
| Level of ADA/Section 508 Compliance | AASHTO / Member Agencies | Will determine required conformance level. |
| Selection of .NET Report Generator | AASHTO | To provide a list of approved/recommended tools. |
| Licensing Policy for Web Users | AASHTO | Final decision on licensing model for web application access. |
| Support for non-IIS HTTP Servers | Technical Advisory Group (TAG) | To resolve based on technology assessment. |
| Electronic Signatures Implementation | AASHTO / Agencies | Dependent on state law and agency policy. |
| Single Sign-On (SSO) Integration Strategy | AASHTO (SCOJD/TAA) | Requires cross-committee coordination. |