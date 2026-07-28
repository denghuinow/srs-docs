# Software Requirements Specification (SRS)
## Pontis 5.0 Bridge Management System (BMS)

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review  
**Prepared for:** AASHTO, Pontis Task Force, Technical Advisory Group  
**Prepared by:** [Your Organization/Author]

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Pontis 5.0 Bridge Management System. It serves as a comprehensive guide for stakeholders, project managers, designers, developers, and testers to understand the system's intended capabilities, constraints, and success criteria. The primary audience is the development contractor and the technical oversight groups.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Priority:** (H)igh, (M)edium, (L)ow.
*   **Keywords:** `MUST`, `SHALL`, `SHOULD`, `MAY` as per IETF RFC 2119.
*   **Style:** Professional, concise, and unambiguous.

#### 1.3 Project Scope
Pontis 5.0 is a next-generation, technologically updated Bridge Management System designed to replace the Pontis 4.x product line. It is a hybrid application with both web-based (thin-client) and standalone (thick-client) components, built on the Microsoft .NET framework. The system will manage the full lifecycle of bridge data, including inventory, inspection, condition analysis, preservation modeling, program simulation, and project development.

**In-Scope Items:**
*   Development of a .NET application with dual client architectures.
*   Core BMS functionalities (Inventory, Inspection, Modeling, Simulation, Project Development).
*   Data exchange via NBI, PDI, and TransXML schemas.
*   Integration with BRIDGEWare products (Virtis/Opis) and GIS.
*   Enhanced system administration and security features.

**Out-of-Scope Items:**
*   Software-as-a-Service (SaaS) hosting model.
*   Support for non-Microsoft browsers (e.g., Safari, Firefox) or non-.NET frameworks.
*   A ground-up redesign of the underlying BRIDGEWare database architecture.
*   Guaranteed full ADA/Section 508 compliance (subject to AASHTO decision).
*   Built-in, high-availability disaster recovery infrastructure.

#### 1.4 References
*   Pontis 4.x Technical Documentation & User Manuals
*   AASHTO BRIDGEWare Database Design Specifications
*   FHWA National Bridge Inventory (NBI) Coding Guide
*   FHWA Recording and Coding Guide for the Structure Inventory and Appraisal of the Nation's Bridges
*   TransXML Schemas

### 2. Overall Description

#### 2.1 Product Perspective
Pontis 5.0 is an evolutionary upgrade within the existing BRIDGEWare ecosystem. It is a standalone system that interacts with external systems through defined data exchange formats and integration points. It succeeds Pontis 4.x and must allow for migration of data and customizations.

#### 2.2 Product Functions (Summary)
The core functions of Pontis 5.0 are:
1.  **Bridge Inventory Management:** Create, read, update, and delete (CRUD) master bridge records and associated data.
2.  **Inspection Data Management:** Support the entry, validation, and management of field inspection data in both connected and disconnected modes.
3.  **Preservation & Deterioration Modeling:** Configure and maintain agency-specific preservation policies, costs, and condition state transition probabilities.
4.  **Program Simulation & Optimization:** Run network-level analyses to forecast future conditions, preservation needs, and optimal fund allocation under various budget scenarios.
5.  **Project & Program Development:** Create and manage improvement projects by assigning work recommendations from the simulation, tracking project status, and developing multi-year programs.
6.  **Reporting & Analysis:** Generate standard and ad-hoc reports, perform data browsing, filtering, and export.
7.  **System Administration:** Manage users, roles, permissions, and application configuration settings.
8.  **Data Exchange:** Import/export data using standard formats (NBI, PDI, TransXML).

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Primary Use Cases |
| :--- | :--- | :--- |
| **Inspector** | Field personnel; works in disconnected environments; uses handheld/tablet devices (potential). | Data entry, review, synchronization. |
| **Bridge Management Engineer** | Engineering staff; performs network-level analysis. | Run simulations, analyze needs, optimize budgets. |
| **Bridge Project Planner** | Program development staff; plans capital projects. | Create projects, assign work, track program development. |
| **Data Analyst** | Technical staff; monitors performance and trends. | Generate reports, ad-hoc queries, data export. |
| **Model Developer** | Advanced engineering/planning staff; configures system models. | Update policy costs, deterioration matrices. |
| **System Administrator** | IT staff; manages system health and access. | User/Role management, system configuration, log review. |

#### 2.4 Operating Environment
*   **Software:**
    *   **Server:** Microsoft Windows Server, Internet Information Services (IIS), .NET Framework.
    *   **Database:** Microsoft SQL Server, Oracle, or Sybase (as per agency deployment).
    *   **Client (Thick):** Windows OS with .NET Framework.
    *   **Client (Thin):** Microsoft Edge or Chrome browser (latest stable versions).
*   **Hardware:** Specifications to be determined based on agency deployment scale.
*   **Network:** Must support both LAN/WAN (for connected clients) and offline operation (for thick client in field).

#### 2.5 Design and Implementation Constraints
1.  `NFR-CON-001` (H): The application **MUST** be developed using the Microsoft .NET technology stack.
2.  `NFR-CON-002` (H): The database schema **MUST** be consistent with and approved by the BRIDGEWare Database TAG.
3.  `NFR-CON-003` (H): The system **MUST** maintain functional consistency with Pontis 4.x core workflows. Any deviation requires explicit justification and approval.
4.  `NFR-CON-004` (H): The architecture **MUST** support both connected (web client) and disconnected (thick client) operational modes.
5.  `NFR-CON-005` (M): The data model **MUST** be extensible to accommodate future changes to Federal NBI coding standards.

#### 2.6 Assumptions and Dependencies
*   Agencies possess the necessary IT infrastructure to deploy and host the application.
*   Existing Pontis 4.x data is valid and migratable.
*   The BRIDGEWare Integration TAG will provide timely specifications for integration points.
*   A third-party .NET reporting tool will be selected and licensed for the project.

### 3. System Features and Requirements

#### 3.1 Feature 1: Bridge Inventory & Inspection Management
**Description:** This feature allows users to manage core bridge data and perform the inspection lifecycle.

*   `FR-INV-001` (H): The system **SHALL** allow authorized users to create, view, edit, and delete bridge inventory records.
*   `FR-INV-002` (H): The system **SHALL** support the creation and management of inspection records for each bridge, including dates, types, and assigned personnel.
*   `FR-INSP-001` (H): The thick client **SHALL** allow Inspectors to download bridge data, perform inspections offline, and synchronize data upon reconnection.
*   `FR-INSP-002` (H): The system **SHALL** enforce data validation rules consistent with NBI and agency-specific coding guides during data entry.
*   `FR-INSP-003` (M): The system **SHALL** provide a user interface for attaching photos, documents, and sketches to inspection records.

#### 3.2 Feature 2: Preservation Modeling & Analysis
**Description:** This feature enables the configuration of the underlying optimization models and the execution of program simulations.

*   `FR-MOD-001` (H): The system **SHALL** provide a secure interface for Model Developers to define and update preservation policy costs and details.
*   `FR-MOD-002` (H): The system **SHALL** provide a secure interface for Model Developers to update condition state deterioration probability matrices.
*   `FR-SIM-001` (H): The system **SHALL** allow Bridge Management Engineers to configure and run multi-year program simulations with variable budget constraints and optimization goals.
*   `FR-SIM-002` (H): The system **SHALL** generate simulation results showing forecasted network condition, recommended preservation actions, and associated costs over the analysis period.

#### 3.3 Feature 3: Project & Program Development
**Description:** This feature supports the translation of simulation recommendations into actionable projects and programs.

*   `FR-PROJ-001` (H): The system **SHALL** allow Bridge Project Planners to create projects and assign one or more work recommendations from simulation results.
*   `FR-PROJ-002` (M): The system **SHALL** allow users to track project status (e.g., Planned, Funded, In Design, Under Construction, Completed).
*   `FR-PROJ-003` (M): The system **SHALL** support the grouping of projects into multi-year improvement programs.

#### 3.4 Feature 4: Reporting & Data Exchange
**Description:** This feature provides tools for data extraction, analysis, and interoperability.

*   `FR-REP-001` (H): The system **SHALL** include a suite of standard reports (e.g., NBI Report, Sufficiency Rating, Project Lists).
*   `FR-REP-002` (M): The system **SHALL** provide a tool for browsing, filtering, and exporting bridge and project data to common formats (e.g., CSV, Excel).
*   `FR-EX-001` (H): The system **SHALL** be able to import from and export to the current NBI and PDI file formats.
*   `FR-EX-002` (M): The system's data exchange architecture **SHALL** be designed to support future TransXML schema implementations.

#### 3.5 Feature 5: System Administration & Security
**Description:** This feature manages application access, configuration, and health.

*   `FR-ADMIN-001` (H): The system **SHALL** provide a comprehensive interface for System Administrators to create, modify, and deactivate user accounts.
*   `FR-ADMIN-002` (H): The system **SHALL** support role-based access control (RBAC), allowing administrators to define roles (e.g., Inspector, Engineer, Viewer) and assign granular permissions.
*   `FR-ADMIN-003` (M): The system **SHALL** provide configuration settings for application behavior, default values, and agency-specific parameters.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The web-based interface **SHALL** be clean, intuitive, and follow modern UI/UX principles.
*   The thick-client interface **SHALL** be functionally comparable to the web interface, optimized for offline use.
*   Both interfaces **SHALL** maintain a consistent look-and-feel with core Pontis 4.x workflows to aid user transition.

#### 4.2 Hardware Interfaces
*   The system **MAY** interface with handheld or tablet computers for field inspection. Specifications are TBD.

#### 4.3 Software Interfaces
*   **Database:** Interface with SQL Server/Oracle/Sybase via ADO.NET or equivalent ORM.
*   **BRIDGEWare Integration:** Interface via shared database schema and/or defined API endpoints with Virtis, Opis, and other BRIDGEWare products.
*   **GIS:** Support integration through map services (e.g., WMS, WFS) or by exporting geospatial data for consumption in external GIS platforms.
*   **Single Sign-On (SSO):** The architecture **SHALL** accommodate a future SSO mechanism for BRIDGEWare products. Implementation details are TBD.

#### 4.4 Communications Interfaces
*   The thick client **SHALL** communicate with the application server via secure HTTP/S (or a proprietary sync protocol) for data synchronization.
*   The web client **SHALL** communicate via HTTP/S.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-PER-001`: User login authentication **SHALL** complete in less than 2 seconds under normal load.
*   `NFR-PER-002`: Displaying a list of 250 bridges in the inventory browser **SHALL** complete within 5-10 seconds.
*   `NFR-PER-003`: A standard program simulation for a medium-sized agency (e.g., ~5,000 bridges over 10 years) **SHOULD** complete within 20 minutes.

#### 5.2 Safety Requirements
*   Not applicable (software does not control physical safety systems).

#### 5.3 Security Requirements
*   `NFR-SEC-001`: All user authentication **SHALL** occur over encrypted connections.
*   `NFR-SEC-002`: User passwords **SHALL** be stored using strong, salted, one-way hashing algorithms.
*   `NFR-SEC-003`: The system **SHALL** log all user authentication attempts (success and failure) and critical data modification events.

#### 5.4 Software Quality Attributes
*   **Reliability:** The system **SHOULD** have a mean time between failures (MTBF) of 99% uptime during business hours for core modules.
*   **Maintainability:** The codebase **SHALL** be well-documented and structured to allow for efficient debugging and future enhancement.
*   **Portability:** While client-specific, the server components **SHOULD** be deployable on any supported database platform (SQL Server, Oracle, Sybase) with minimal configuration changes.
*   **Usability:** As per success metrics, routine users **SHOULD** achieve comfort with core tasks after two days of training; casual users **SHOULD** be able to perform basic data viewing within two hours.

### 6. Success Metrics & Acceptance Criteria
1.  **Data Migration:** Successful automated migration of at least 95% of data from a provided Pontis 4.x sample database, with all critical relationships intact.
2.  **Performance Benchmarks:** All specified performance requirements (`NFR-PER-001`, `NFR-PER-002`) are met during load testing.
3.  **User Acceptance:** A pilot group of representative users from each class reports high satisfaction (>80% on a standardized survey) and confirms core user stories are fulfilled after training.
4.  **Functional Completeness:** 100% of High-priority (H) functional requirements are implemented and verified.

### 7. Appendices

#### 7.1 Glossary
*   **BMS:** Bridge Management System.
*   **NBI:** National Bridge Inventory.
*   **PDI:** Pontis Data Interchange.
*   **TransXML:** A set of XML schemas for transporting transportation data.
*   **TAG:** Technical Advisory Group.

#### 7.2 Analysis Models
*   (To be populated with relevant UML diagrams: Use Case Diagrams, Data Flow Diagrams, etc., in subsequent revisions).

#### 7.3 Issues List (Undecided/TBD)
1.  **ADA/Section 508 Compliance:** The specific level of compliance and implementation approach is pending an AASHTO decision.
2.  **Reporting Tool:** The specific third-party .NET reporting component to be used is TBD.
3.  **Field Device Support:** The extent of support and testing for handheld/tablet computers is TBD.
4.  **Single Sign-On (SSO):** Implementation details for cross-BRIDGEWare authentication are TBD.
5.  **"Waiting Room" Requirements:** Requirements such as electronic signatures on inspection reports and advanced configuration wizards are deferred. They are documented separately for future consideration.

---
*This document is considered the authoritative source for Pontis 5.0 software requirements. Any changes must follow the approved change control process.*