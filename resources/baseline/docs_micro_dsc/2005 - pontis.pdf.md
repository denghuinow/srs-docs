# Software Requirements Specification (SRS)
## Next-Generation Bridge Management System (NGBMS)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review  
**Prepared for:** State Transportation Agency(s)  
**Prepared by:** [Your Organization Name]

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Next-Generation Bridge Management System (NGBMS). The NGBMS is intended to replace the legacy Pontis 4.x system, providing state transportation agencies with a modern, scalable, and flexible platform for managing bridge inventory, inspections, condition assessments, and capital project planning. This SRS serves as a contract between the stakeholders and the development team, establishing a foundation for design, development, and validation.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms "MUST," "MUST NOT," "REQUIRED," "SHALL," "SHALL NOT," "SHOULD," "SHOULD NOT," "RECOMMENDED," "MAY," and "OPTIONAL" are to be interpreted as described in IETF RFC 2119.
*   **Formatting:** User interface elements are denoted as `Button Text`. Database entities are *italicized*.

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Sponsors & Stakeholders:** Focus on Sections 1 (Introduction), 2 (Overall Description), and 5 (External Interface Requirements).
*   **Project Managers:** The entire document, with emphasis on scope and constraints.
*   **System Architects & Developers:** Focus on Sections 3 (System Features), 4 (Data Requirements), and 6 (Non-Functional Requirements).
*   **Quality Assurance Team:** Focus on Sections 3 (System Features) to derive test cases.

#### 1.4 Project Scope
The NGBMS is a comprehensive enterprise application for the management of highway bridge assets. Its scope includes:
*   The replacement of all core functionalities of the Pontis 4.x system.
*   Centralized management of bridge inventory, element-level data, and inspection records.
*   Automated calculation of condition ratings and health indices.
*   Advanced analytical tools for program simulation, lifecycle cost analysis, and work recommendation generation.
*   Management of preservation policies, treatment strategies, and multi-year project programs.
*   Support for data migration from existing Pontis 4.x databases.
*   Deployment in both connected (web-based) and disconnected (field/laptop) environments.

**Out of Scope:**
*   Real-time sensor data integration from structural health monitoring systems.
*   Management of non-bridge transportation assets (e.g., pavements, signs).
*   Financial management and accounting system integration beyond cost modeling.
*   CAD or BIM design tools.

#### 1.5 References
*   AASHTO Pontis 4.x User Manuals and Technical Specifications
*   *AASHTO Guide for Bridge Management Systems*
*   *FHWA Recording and Coding Guide for the Structure Inventory and Appraisal of the Nation's Bridges*
*   Microsoft .NET Framework and ASP.NET Core Documentation
*   Oracle, Microsoft SQL Server, and Sybase ASE Official Documentation

---

### 2. Overall Description

#### 2.1 Product Perspective
The NGBMS is a standalone product but must operate within the larger ecosystem of state DOT IT infrastructure. It will interface with existing Geographic Information Systems (GIS), asset management platforms, and financial systems. It succeeds the Pontis 4.x application, requiring data compatibility and user workflow familiarity.

#### 2.2 Product Functions (Summary)
1.  **Inventory & Inspection Management:** CRUD operations for bridges, elements, and inspection data.
2.  **Condition Assessment:** Derivation of element, bridge, and network-level condition ratings based on inspection input and defined algorithms.
3.  **Policy & Strategy Management:** Configuration of preservation policies, deterioration models, treatment effectiveness, and costs.
4.  **Analysis & Simulation:** Run "what-if" scenarios to optimize budget allocation and project sequencing over a long-term horizon.
5.  **Program Development:** Create and manage candidate project lists and multi-year work programs.
6.  **Reporting:** Generate standard (FHWA, state-specific) and ad-hoc reports.
7.  **System Administration:** User, role, and reference data management.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Field Inspector** | Works offline in remote locations. Uses ruggedized laptops/tablets. | Disconnected data entry, intuitive mobile forms, synchronization. |
| **Bridge Engineer/Analyst** | Office-based, data-savvy. Performs analysis and creates programs. | Powerful analytical tools, simulation modeling, detailed reporting. |
| **Program Manager** | Manages budgets and priorities. Makes strategic decisions. | High-level dashboards, summary reports, scenario comparison. |
| **System Administrator** | IT staff responsible for deployment, maintenance, and user support. | Easy installation, configuration management, user access control. |

#### 2.4 Operating Environment
*   **Software:**
    *   **Server:** Windows Server 2019/2022; IIS or self-hosted .NET Core runtime; Supported RDBMS: Oracle 19c/21c, Microsoft SQL Server 2019/2022, Sybase ASE 16.0.
    *   **Client (Web):** Modern browsers (Chrome, Edge, Firefox, Safari) with JavaScript enabled.
    *   **Client (Standalone):** Windows 10/11 with .NET Desktop Runtime.
*   **Hardware:** Specifications will scale based on agency size (number of bridges). A typical mid-sized state deployment requires a dedicated application/database server.

#### 2.5 Design and Implementation Constraints
1.  **Technology Stack:** The application MUST be developed using the Microsoft .NET 6+ framework (or later). The frontend for the connected environment MUST be developed using ASP.NET Core (Razor Pages or MVC).
2.  **Database Independence:** The data access layer MUST abstract RDBMS-specific SQL to support Oracle, SQL Server, and Sybase from a single codebase.
3.  **Pontis Compatibility:** Data models and business rules MUST maintain consistency with Pontis 4.x to ensure a reliable migration path. Legacy data import/export utilities ARE REQUIRED.
4.  **Dual Deployment:** The system architecture MUST support a fully functional web application and a synchronized, standalone desktop application for field use.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Agencies will provide clean, validated Pontis 4.x data for migration.
*   **Assumption:** Users in the disconnected environment will have periodic access to network connectivity for synchronization.
*   **Dependency:** Availability of commercial RDBMS licenses (Oracle, SQL Server, Sybase) from the client agency.
*   **Dependency:** .NET runtime is approved for use within the client agency's IT infrastructure.

---

### 3. System Features

#### 3.1 Feature 1: Bridge Inventory and Inspection Management
**3.1.1 Description**
This feature provides the core capability to create, read, update, and delete (CRUD) all data related to bridge structures and their inspections, serving as the system's system of record.

**3.1.2 Requirements**
*   `FR-101`: The system SHALL allow authorized users to create and maintain a hierarchical inventory of Bridges, Spans, and Elements as defined by the AASHTO/FHWA standards.
*   `FR-102`: The system SHALL support the entry and management of inspection records, including dates, inspectors, conditions, photos, and notes.
*   `FR-103`: The system SHALL automatically calculate derived condition ratings (Element Condition State, Bridge Health Index, Sufficiency Rating) upon saving inspection data, based on configured algorithms.
*   `FR-104`: The system SHALL provide a synchronization module to seamlessly merge inspection data collected in the disconnected (standalone) environment with the central database.

#### 3.2 Feature 2: Preservation Policy and Analysis Configuration
**3.2.1 Description**
This feature allows analysts to define the business rules that drive the system's analytical engine, including deterioration models, treatment options, and cost parameters.

**3.2.2 Requirements**
*   `FR-201`: The system SHALL allow administrators to define and manage Preservation Policies, which link Element Types with possible Treatments.
*   `FR-202`: The system SHALL support the configuration of Markovian or other deterministic deterioration models for each Element Type within a Policy.
*   `FR-203`: The system SHALL allow users to define Treatment effectiveness (condition state transition), costs (unit, fixed, variable), and service life.
*   `FR-204`: The system SHALL enable the management of global and project-level economic parameters (discount rate, analysis period).

#### 3.3 Feature 3: Program Simulation and Work Recommendation
**3.3.1 Description**
This is the core analytical feature, enabling users to simulate long-term bridge performance under different budget scenarios to generate optimal work recommendations.

**3.3.2 Requirements**
*   `FR-301`: The system SHALL perform a network-level program simulation over a user-defined analysis period (e.g., 10-50 years).
*   `FR-302`: The system SHALL generate a recommended program of projects (list of bridges, proposed treatments, timing, and estimated costs) that maximizes condition or minimizes lifecycle cost within specified budget constraints.
*   `FR-303`: The system SHALL allow users to create and compare multiple "what-if" simulation scenarios.
*   `FR-304`: The system SHALL provide bridge-level analysis, showing detailed condition projection and treatment timing for an individual structure.

#### 3.4 Feature 4: Project Program Development
**3.4.1 Description**
This feature facilitates the transition from analytical recommendations to actionable capital programs, allowing management of candidate projects and multi-year plans.

**3.4.2 Requirements**
*   `FR-401`: The system SHALL allow users to create, edit, and manage a Candidate Project List from simulation results or manual entry.
*   `FR-402`: The system SHALL support the development of a Multi-Year Improvement Program (MYIP), allowing users to schedule candidate projects into specific fiscal years.
*   `FR-403`: The system SHALL track the status of projects (e.g., recommended, funded, completed) and update inventory/condition upon project completion.

---

### 4. Data Requirements

#### 4.1 Logical Data Model
The system SHALL be based on a logical data model that extends the core Pontis 4.x schema. Key entities include:
*   *Bridge*: Master record for each structure.
*   *Element*: Instance of an Element Type (e.g., Concrete Deck) on a specific bridge.
*   *Inspection*: Event recording the condition state of elements.
*   *Policy*: Set of rules defining deterioration and viable treatments for an element type.
*   *Simulation*: Parameters and results of an analysis run.
*   *Project*: A proposed or approved set of treatments on one or more bridges.

#### 4.2 Data Migration
*   `FR-501`: The system SHALL provide utilities to import all critical data entities (bridges, elements, inspections, policies) from a standard Pontis 4.x database export.
*   `FR-502`: The migration utility SHALL generate a validation report detailing any data inconsistencies or required transformations.

---

### 5. External Interface Requirements

#### 5.1 User Interfaces
*   **Web Interface:** A clean, responsive web application following WCAG 2.1 AA guidelines. Primary navigation shall include modules: Dashboard, Inventory, Inspections, Analysis, Programs, Reports, Admin.
*   **Standalone Interface:** A Windows desktop application with a similar look, feel, and functionality to the web interface, optimized for offline use.

#### 5.2 Hardware Interfaces
*   The standalone client MUST operate on standard and ruggedized Windows laptops/tablets.
*   The system SHOULD support the attachment of digital cameras and GPS units for field data collection.

#### 5.3 Software Interfaces
*   **Database:** ADO.NET or Entity Framework Core providers for Oracle, SQL Server, and Sybase.
*   **GIS:** REST API endpoints (JSON) to provide bridge location and summary data to external web mapping applications.
*   **Reporting:** Integration with a reporting engine (e.g., SQL Server Reporting Services, Telerik) for formatted report generation.

#### 5.4 Communications Interfaces
*   The system SHALL use HTTPS (TLS 1.2+) for all web communication.
*   The data synchronization between standalone and central systems SHALL use a secure, transactional web service (REST API) over HTTPS.

---

### 6. Non-Functional Requirements

#### 6.1 Performance Requirements
*   `NFR-601`: The system SHALL support concurrent use by at least 100 online users and 250 standalone users.
*   `NFR-602`: Inventory and inspection data entry screens SHALL have a response time of < 2 seconds for 95% of transactions.
*   `NFR-603`: A network-level simulation over a 20-year period for 10,000 bridges SHALL complete in under 30 minutes.

#### 6.2 Safety Requirements
*   Not applicable (software does not control physical systems).

#### 6.3 Security Requirements
*   `NFR-701`: The system SHALL implement role-based access control (RBAC) with configurable permissions for all major functions.
*   `NFR-702`: All user passwords SHALL be hashed and salted in the database.
*   `NFR-703`: The standalone client SHALL encrypt its local database using a user-specific key.
*   `NFR-704`: All audit-logged actions (data changes, logins, etc.) SHALL be immutable.

#### 6.4 Software Quality Attributes
*   **Availability:** The web application SHALL have 99.5% uptime during business hours.
*   **Maintainability:** The code SHALL be modular, documented, and adhere to .NET coding standards.
*   **Portability:** The application layer SHALL be deployable on-premises or in a cloud IaaS environment (e.g., Azure VM, AWS EC2).
*   **Usability:** The system SHALL be designed to minimize training time for existing Pontis 4.x users. A task shall be learnable by a new user within 30 minutes of guided use.

---

### 7. Appendices

#### Appendix A: Glossary
*   **Element:** A discrete, measurable component of a bridge (e.g., steel girder, concrete deck).
*   **Condition State:** A numeric rating (typically 1-5, with 1 being worst) of an element's physical condition.
*   **Policy:** A set of rules that defines how an element type deteriorates and what treatments can be applied.
*   **Program Simulation:** An analytical process that forecasts future bridge conditions and recommends optimal preservation actions over time.

#### Appendix B: Analysis Models
*UML Use Case Diagrams, Activity Diagrams for key workflows (e.g., "Perform Field Inspection," "Run Simulation"), and Entity-Relationship Diagrams are to be developed during the design phase and referenced here.*