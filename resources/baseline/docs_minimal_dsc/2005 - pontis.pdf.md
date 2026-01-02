# Software Requirements Specification (SRS) for Pontis 5.0 Bridge Management System

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Pontis 5.0 Bridge Management System. It serves as a comprehensive guide for stakeholders, developers, testers, and project managers throughout the system's development lifecycle. The primary audience includes the development team, quality assurance, and the client's technical and management staff.

### 1.2 Scope
Pontis 5.0 is a comprehensive, web-enabled bridge management system designed to replace the existing Pontis 4.x product line. The system will provide state transportation agencies with tools for data management, condition assessment, preservation modeling, needs analysis, and reporting. The scope includes migrating core functionality to a modern web architecture while ensuring backward compatibility with existing agency data, processes, and investments in the BRIDGEWare ecosystem.

**In-Scope:**
*   Web-based user interface accessible via specified browsers.
*   Core data management for bridge inventory and inspection records.
*   Preservation modeling and deterioration analysis engines.
*   Program simulation and work recommendation generation.
*   Project and program management workflows.
*   Integration with existing BRIDGEWare databases and products.
*   User and system administration modules.
*   Reporting and data export capabilities.

**Out-of-Scope:**
*   Development of new, unrelated GIS functionality (integration only).
*   Major re-architecture of the underlying BRIDGEWare data model.
*   Mobile-native applications for field inspection (though the web interface must be usable for data collection).

### 1.3 Definitions, Acronyms, and Abbreviations
*   **BMS:** Bridge Management System
*   **GIS:** Geographic Information System
*   **RDBMS:** Relational Database Management System
*   **ASA:** Sybase Adaptive Server Anywhere
*   **IE:** Internet Explorer
*   **.NET:** Microsoft .NET Framework
*   **UI:** User Interface
*   **NBI:** National Bridge Inventory (standardized data set)

### 1.4 References
*   Pontis 4.x User and Technical Documentation
*   BRIDGEWare Database Design Specification
*   AASHTO Pontis Manuals and Guidelines
*   Project Charter for Pontis 5.0 Migration

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its user classes, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements including performance, security, and constraints.

## 2. Overall Description

### 2.1 Product Perspective
Pontis 5.0 is a major evolution within the established BRIDGEWare product suite. It is a standalone web application that must interoperate seamlessly with other BRIDGEWare components and external systems like GIS platforms. It replaces the desktop-based Pontis 4.x client while connecting to the same or migrated backend databases.

**System Interfaces:**
*   **Database:** Direct connection to BRIDGEWare-compliant RDBMS (Sybase ASA, Oracle, MS SQL Server).
*   **GIS:** Must support interaction with external GIS systems for map-based visualization and selection (e.g., launching GIS with a specific bridge location).
*   **Other BRIDGEWare Products:** Must maintain data consistency and support workflows that span multiple products in the suite.

### 2.2 User Classes and Characteristics
| User Class | Primary Responsibilities | Key Characteristics & Skill Level |
| :--- | :--- | :--- |
| **Inspector** | Collect and validate field inspection data. | Field personnel; uses tablets/laptops; moderate computer skill; requires intuitive data entry forms with validation. |
| **Bridge Engineer/Planner** | Perform engineering analysis, update preservation models, run simulations, interpret results. | High technical expertise in bridge engineering and Pontis methodology; power user of analytical tools. |
| **Highway Program Planner** | Integrate bridge-level work recommendations into agency-wide capital programs. | Managerial role; focuses on high-level reports, cost summaries, and program integration; needs robust filtering and export. |
| **System Administrator** | Manage user accounts, roles, permissions, and system configuration settings. | IT professional; understands network, database, and application security principles. |

### 2.3 Operating Environment
*   **Server:** Microsoft Windows Server with Internet Information Services (IIS) and .NET Framework.
*   **Client:** Windows XP or later operating system.
*   **Browser:** Microsoft Internet Explorer (specific version to be determined based on XP compatibility and security standards).
*   **Database:** Must support concurrent connections to:
    *   Sybase Adaptive Server Anywhere (ASA)
    *   Oracle Database
    *   Microsoft SQL Server
*   **Network:** Standard HTTP/HTTPS over agency intranet/internet.

### 2.4 Design and Implementation Constraints
1.  **Technology Stack:** The application must be developed using Microsoft .NET technologies (e.g., ASP.NET, C#).
2.  **Legacy Compatibility:** The UI and workflow must maintain a high degree of consistency with Pontis 4.x to minimize retraining. The database schema shall not deviate from the BRIDGEWare design without explicit justification and approval.
3.  **Browser Compatibility:** The application must be fully functional and tested on Internet Explorer running on Windows XP.
4.  **Database Agnosticism:** Data access layer must abstract RDBMS-specific syntax to support the three mandated databases.

### 2.5 Assumptions and Dependencies
*   Agencies will have the necessary database licenses and server infrastructure.
*   The existing Pontis 4.x database is structurally sound and contains valid data.
*   Users will have received appropriate training on bridge management concepts.
*   Integration with GIS is assumed to be via published APIs or URL-based protocols.

## 3. System Features and Requirements

### 3.1 Feature 1: Bridge Inventory and Inspection Data Management
**Description:** This module allows authorized users to create, view, edit, and delete bridge inventory records and associated inspection data. The system shall calculate derived condition ratings based on entered element-level data.

**3.1.1 Functional Requirements:**
*   **FR-1.1:** The system shall provide forms for entering and editing all NBI and agency-specific bridge inventory items.
*   **FR-1.2:** The system shall provide structured forms for recording element-level condition inspections, including defect quantities, units, and condition states.
*   **FR-1.3:** The system shall automatically calculate derived component and overall bridge condition ratings (e.g., Sufficiency Rating, Health Index) upon inspection save, according to Pontis algorithms.
*   **FR-1.4:** The system shall enforce data validation rules (e.g., value ranges, mandatory fields) consistent with Pontis 4.x and AASHTO standards.
*   **FR-1.5:** The system shall maintain a complete audit history of all changes to inventory and inspection data.

### 3.2 Feature 2: Preservation Modeling
**Description:** This module allows bridge engineers to define and update Markovian deterioration models, action effectiveness, and associated costs for bridge elements.

**3.2.1 Functional Requirements:**
*   **FR-2.1:** The system shall allow users to view and update deterioration probability matrices for all defined element types.
*   **FR-2.2:** The system shall allow users to define preservation actions (e.g., repair, replace) and associate them with cost distributions and condition state transitions.
*   **FR-2.3:** The system shall allow model parameters to be calibrated based on historical inspection data via integrated tools.
*   **FR-2.4:** All model updates shall be version-controlled and require appropriate engineering approval workflows.

### 3.3 Feature 3: Program Simulation and Analysis
**Description:** This module runs simulation engines to generate long-term network-level funding needs and optimal work recommendations for individual bridges.

**3.3.1 Functional Requirements:**
*   **FR-3.1:** The system shall allow users to configure simulation scenarios by defining analysis periods, budget constraints, and performance goals.
*   **FR-3.2:** The system shall execute a network-level simulation and produce reports showing recommended work programs, forecasted condition, and funding needs over time.
*   **FR-3.3:** The system shall provide bridge-level analysis tools to generate optimal preservation plans for a single bridge given multiple strategies.
*   **FR-3.4:** Simulation results shall be exportable to standard formats (PDF, Excel).

### 3.4 Feature 4: Project and Program Management
**Description:** This module allows planners to create and manage capital projects and multi-year programs by grouping recommended work items.

**3.4.1 Functional Requirements:**
*   **FR-4.1:** The system shall allow users to create projects, assign bridge work items from simulation results or manual selection, and estimate costs.
*   **FR-4.2:** The system shall allow projects to be grouped into larger capital programs across multiple fiscal years.
*   **FR-4.3:** The system shall track the status of work items (recommended, proposed, approved, completed).
*   **FR-4.4:** The system shall allow "what-if" analysis by adjusting project scope, timing, and costs.

### 3.5 Feature 5: System Administration
**Description:** This module allows administrators to manage user access, system settings, and data dictionaries.

**3.5.1 Functional Requirements:**
*   **FR-5.1:** The system shall provide a role-based access control (RBAC) interface for creating users and assigning roles (Inspector, Engineer, Planner, Admin).
*   **FR-5.2:** The system shall allow administrators to manage reference data tables (e.g., element types, defect types, agency lists).
*   **FR-5.3:** The system shall provide database connection management and log viewing utilities.

## 4. Non-Functional Requirements

### 4.1 Performance Requirements
*   **PR-1:** The system shall support up to 100 concurrent users during peak inspection periods.
*   **PR-2:** Inventory data entry and edit forms shall load in less than 3 seconds over a standard agency WAN connection.
*   **PR-3:** Network-level simulations for an agency with up to 10,000 bridges shall complete within 30 minutes.

### 4.2 Safety and Security Requirements
*   **SR-1:** All user authentication shall occur over encrypted channels (HTTPS).
*   **SR-2:** User passwords shall be stored using industry-standard hashing algorithms.
*   **SR-3:** The system shall prevent unauthorized access to data based on user role and, where applicable, organizational unit (e.g., district).
*   **SR-4:** All data modifications must be attributable to a specific user and timestamp.

### 4.3 Software Quality Attributes
*   **Availability:** The system shall target 99.5% uptime during business hours.
*   **Usability:** The user interface shall be consistent with Pontis 4.x paradigms to ensure ease of adoption for existing users. New web-based workflows shall follow WCAG 2.1 Level AA guidelines where possible.
*   **Maintainability:** The code shall be modular, well-documented, and follow .NET best practices to facilitate future updates.
*   **Portability:** The application shall be easily deployable on standard Windows Server/IIS environments.

### 4.4 Business Rules
*   Business logic for rating calculations, deterioration modeling, and simulation shall be identical to that in Pontis 4.x, unless a change is explicitly requested and documented.
*   All financial calculations shall respect agency-defined fiscal year boundaries.

### 4.5 Compliance
The system shall comply with agency IT security policies and relevant AASHTO guidelines for bridge management data.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance | | | |