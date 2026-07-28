# Software Requirements Specification (SRS)
## Pontis 5.0 Bridge Management System (BMS)

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for Pontis 5.0, the next-generation Bridge Management System. It is intended for use by the development team, project managers, quality assurance, and stakeholders from AASHTO and state highway agencies to ensure a common understanding of the system to be developed.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Priority:** (H)igh, (M)edium, (L)ow.
*   **Keywords:** `MUST`, `SHALL`, `WILL` indicate mandatory requirements. `SHOULD`, `MAY` indicate desirable but not mandatory features.

#### 1.3 Project Scope
Pontis 5.0 is a comprehensive Bridge Management System that provides state highway agencies with a central repository and analytical tools for managing the entire bridge lifecycle. Its core capabilities include inventory management, inspection data collection, preservation modeling, program simulation, and project planning. It is the designated successor to the Pontis 4.x product line.

**Out-of-Scope:**
*   Provision of hosted application services (Software as a Service).
*   Implementation of disaster recovery procedures for client agencies.
*   Guaranteed support for non-Microsoft web browsers.
*   Development of new, unrelated BRIDGEWare suite products.

#### 1.4 References
*   Pontis 4.x Technical Documentation
*   AASHTO BRIDGEWare Architecture Guide
*   NCHRP Project 12-67 Final Report
*   National Bridge Inventory (NBI) Coding Guide
*   TransXML Schemas

### 2. Overall Description

#### 2.1 Product Perspective
Pontis 5.0 is a core component of the AASHTO-owned BRIDGEWare software suite. It must integrate seamlessly with other suite products (e.g., Virtis/Opis for design and construction). The system exists within an ecosystem that includes state agency databases, GIS platforms, and national data standards (NBI, PDI).

#### 2.2 Product Functions (Summary)
The system shall provide the following high-level functions:
1.  Data browsing, filtering, and selection (tabular and map-based).
2.  Bridge inventory and inspection data management (CRUD operations).
3.  Preservation policy modeling (deterioration, cost, Health Index targeting).
4.  Network-level program simulation and bridge-level analysis.
5.  Program and project management with work item assignment.
6.  Standardized data import/export (NBI, PDI, XML).
7.  Comprehensive system administration and security.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Inspector** | Field-based; works in disconnected environments; uses mobile devices. | Efficient, intuitive data entry; offline capability; synchronization. |
| **Bridge Management Engineer / Power User** | Deep domain expertise; performs complex analysis. | Advanced modeling tools; flexible simulation; detailed reporting. |
| **Project Planner** | Manages budgets and schedules. | Project creation tools; cost forecasting; program integration. |
| **Casual User / Analyst** | Needs information for reports or decisions. | Easy browsing; predefined reports; map visualization. |
| **System Administrator** | IT-focused; manages system health. | User/role management; application configuration; security controls. |

#### 2.4 Operating Environment
*   **Server:** Windows Server 2003 or later; Microsoft IIS; .NET Framework.
*   **Thick Client:** Windows XP Professional or later; .NET Framework.
*   **Thin Client:** Microsoft Internet Explorer.
*   **Database:** Sybase Adaptive Server Anywhere, Oracle, Microsoft SQL Server.
*   **GIS Compatibility:** ESRI ArcGIS, Intergraph GeoMedia, Open GIS standards.

#### 2.5 Design and Implementation Constraints
1.  **Technology:** MUST be developed using Microsoft .NET technologies (C#, ASP.NET).
2.  **Database:** All database schema changes require review and approval by the BRIDGEWare Database Technical Advisory Group (TAG).
3.  **Backward Compatibility:** MUST provide a reliable migration path for existing Pontis 4.x databases and maintain functional consistency where appropriate.
4.  **Standards:** Design MUST be informed by outcomes of NCHRP Project 12-67 and accommodate future NBI coding standard changes.

#### 2.6 Assumptions and Dependencies
*   Client agencies will provide and manage their own server infrastructure.
*   The system will be deployed within an agency's secure network.
*   Successful completion is dependent on final results from NCHRP research projects (12-67, 20-64).
*   Required GIS and database interfaces are available and supported by the agency.

### 3. System Features and Requirements

#### 3.1 Data Management and Browsing
**Description:** Users shall be able to locate, view, filter, and select bridge records and project data through both tabular interfaces and a map-based visual interface.

**Requirements:**
*   `FR-101` (H): The system shall allow users to filter the bridge inventory based on a comprehensive set of NBI and agency-defined criteria.
*   `FR-102` (H): The system shall provide a interactive map view displaying bridge locations, with symbology reflecting key attributes (e.g., Health Index, deficiency status).
*   `FR-103` (M): The system shall allow users to select bridges from the map or list view for inclusion in analysis sets or projects.

#### 3.2 Inventory and Inspection Data Management
**Description:** Authorized users shall create, read, update, and delete bridge inventory and element-level inspection data.

**Requirements:**
*   `FR-201` (H): The system shall provide forms for entering and editing all standard NBI record items and Pontis-specific element data.
*   `FR-202` (H): The system shall support disconnected data collection, allowing inspectors to download bridge data, perform inspections offline, and upload results.
*   `FR-203` (H): The system shall enforce data validation rules consistent with NBI and Pontis policy standards.

#### 3.3 Preservation Policy Modeling and Analysis
**Description:** Power users shall configure deterioration models, cost profiles, and performance targets to simulate bridge condition over time.

**Requirements:**
*   `FR-301` (H): The system shall allow users to define and calibrate Markovian deterioration models for bridge elements.
*   `FR-302` (H): The system shall allow users to define preservation actions, associated costs, and effectiveness.
*   `FR-303` (H): The system shall support Health Index calculation and allow engineers to set network-wide or group-specific target Health Index values.

#### 3.4 Program Simulation and Bridge Analysis
**Description:** The system shall run computational models to forecast future conditions, preservation needs, and budget requirements at both network and individual bridge levels.

**Requirements:**
*   `FR-401` (H): The system shall execute a program simulation for a selected set of bridges over a user-defined analysis period (e.g., 20 years).
*   `FR-402` (H): The system shall generate reports and charts showing forecasted condition, recommended actions, and budget requirements.
*   `FR-403` (M): The system shall allow "what-if" analysis at the individual bridge level to evaluate alternative treatment strategies.

#### 3.5 Program and Project Management
**Description:** Users shall create multi-year programs and specific projects, assigning proposed work items generated from simulations or other sources.

**Requirements:**
*   `FR-501` (H): The system shall allow creation and management of capital programs and projects, including scheduling and budgeting.
*   `FR-502` (H): The system shall allow work candidates from simulations, inspections, or manual entry to be assigned to projects.
*   `FR-503` (M): The system shall track the status of projects and their impact on bridge condition forecasts.

#### 3.6 Data Exchange
**Description:** The system shall import from and export to external systems using standard transportation data formats.

**Requirements:**
*   `FR-601` (H): The system shall import and export bridge inventory data in the official NBI format.
*   `FR-602` (H): The system shall import and export element-level inspection data in PDI format.
*   `FR-603` (M): The system shall support import and export of project and analysis data using XML, aligned with TransXML schemas where applicable.

#### 3.7 System Administration
**Description:** Administrators shall configure the application, manage user access, and control security settings.

**Requirements:**
*   `FR-701` (H): The system shall provide role-based access control (RBAC), allowing permissions to be assigned by user role.
*   `FR-702` (H): The system shall support integration with enterprise authentication systems (e.g., Active Directory, LDAP) for single sign-on.
*   `FR-703` (M): The system shall provide an interface for configuring system parameters, code tables, and default policies.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Thick Client:** A Windows .NET application with a standard menu, toolbar, and form-based interface.
*   **Thin Client:** A web application optimized for Microsoft Internet Explorer, providing core browsing, reporting, and inspection data entry.

#### 4.2 Hardware Interfaces
*   Must operate on standard server and client hardware meeting the specified operating system requirements.

#### 4.3 Software Interfaces
*   `INT-DB-01`: The system shall connect to and operate with Sybase ASA, Oracle, and Microsoft SQL Server databases.
*   `INT-GIS-01`: The system shall be GIS-aware, capable of exchanging spatial data with ESRI, Intergraph, or standard Open GIS systems.
*   `INT-SUITE-01`: The system shall provide integration points (e.g., shared data schemas, APIs) for other BRIDGEWare applications like Virtis/Opis.

#### 4.4 Communications Interfaces
*   Client-server communication shall use standard HTTP/HTTPS (thin client) and TCP/IP (thick client) protocols over the agency's network.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-PER-01`: The system shall support a database containing inventory and historical data for up to **50,000 bridges**.
*   `NFR-PER-02`: User login and logout actions shall complete within **2 seconds** under normal load.
*   `NFR-PER-03`: A program simulation for a set of **100 bridges** over a 20-year period shall complete in **less than 30 seconds**.

#### 5.2 Reliability and Availability
*   `NFR-REL-01`: The system shall target an availability of **98%** during its defined operating window (18 hours per day, 353 days per year). Scheduled maintenance periods are excluded.

#### 5.3 Security Requirements
*   `NFR-SEC-01`: The system shall enforce role-based application security, controlling access to functions and data based on user roles.
*   `NFR-SEC-02`: The system shall support database-level security integrated with the application security model.
*   `NFR-SEC-03`: All sensitive data transmission shall be encrypted.

#### 5.4 Maintainability
*   `NFR-MAIN-01`: All source code shall be adequately documented following AASHTO development standards.
*   `NFR-MAIN-02`: The complete source code and build instructions shall be deliverable to AASHTO.

#### 5.5 Operational
*   Deployment and operational procedures shall assume an agency-managed infrastructure, as outlined in Section 2.4.

### 6. Acceptance Criteria
Formal acceptance of Pontis 5.0 will be based on:
1.  Successful verification of all `FR-XXX` and `NFR-XXX` requirements marked as (H)igh priority.
2.  Demonstrated achievement of the performance benchmarks defined in Section 5.1.
3.  Successful execution of a standardized migration test, moving a representative Pontis 4.x database to Pontis 5.0 without data loss or corruption.
4.  Completion of formal Alpha (internal) and Beta (limited pilot agency) release cycles with addressed feedback.

---
*This document is the proprietary information of AASHTO and the Pontis development consortium.*