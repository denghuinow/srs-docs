# Software Requirements Specification (SRS)
## For SPRAT: Security & Privacy Requirements Analysis Tool

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review  
**Authors:** [System Architects / Requirements Engineers]

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Security & Privacy Requirements Analysis Tool (SPRAT). It is intended for use by the project stakeholders, including developers, testers, project managers, and end-users (requirements engineers, privacy officers, and policy analysts), to ensure a common understanding of the system to be developed.

### 1.2 Scope
SPRAT is a specialized bench tool designed to assist analysts in mining, reconciling, and managing goals and scenarios derived from textual privacy and security policy documents. The system maintains a centralized repository of these elements to support systematic analysis, comparison, and conflict detection.

**In-Scope:**
*   User and project management with role-based access control.
*   Management of policy documents, goals, and scenarios.
*   Analytical functions for access control (via the integrated RACAF module) and privacy policy (P3P) evaluation.
*   Comparison of analysis results from multiple users.
*   Secure integration with external tools (Ponder, Alloy).

**Out-of-Scope:**
*   Automatic generation or writing of policy documents.
*   Automated legal compliance checking beyond the specified analytical comparisons.
*   Natural Language Processing (NLP) for fully automatic goal/scenario extraction (assumes analyst-driven extraction and classification).

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SPRAT** | Security & Privacy Requirements Analysis Tool |
| **RACAF** | Requirements-level Access Control Analysis Framework |
| **P3P** | Platform for Privacy Preferences Project |
| **Goal** | A high-level objective or constraint extracted from a policy document (e.g., "Patient data must be confidential"). |
| **Scenario** | A sequence of actions or steps describing an interaction related to a policy. |
| **Ponder** | An external policy specification language and editor. |
| **Alloy** | An external formal specification and analysis tool. |

### 1.4 References
*   Project Charter: SPRAT Development Initiative
*   RACAF Framework Specification v2.1
*   Ponder Policy Language Manual
*   Alloy Analyzer Documentation

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific requirements, including functional, non-functional, and external interface requirements.

## 2. Overall Description

### 2.1 Product Perspective
SPRAT is a standalone, client-server application that operates as a component within a larger tool bench for requirements engineering. It interfaces with a persistent relational database and is designed to integrate with external analytical tools.

**System Interfaces:**
*   **Database:** MySQL/PostgreSQL for persistent storage of all system data.
*   **Ponder Editor:** Interface for exporting/importing access control rule specifications.
*   **Alloy Analyzer:** Interface for passing formal models generated from access control specifications for verification.

**User Interfaces:** A web-based graphical user interface (GUI) with distinct views and capabilities based on user role.

### 2.2 Product Functions (Summary)
1.  **User & Access Management:** Securely manage accounts and permissions for Administrators, Project Managers, Analysts, and Guests.
2.  **Repository Management:** CRUD (Create, Read, Update, Delete) operations for Policy Documents, Goals, and Scenarios, including search and classification.
3.  **Project Management:** Create projects, assign policy documents and analysts, and manage guest access permissions.
4.  **Access Control Analysis (RACAF Module):** Define data hierarchies, organizational structures, roles, and rules for analysis.
5.  **Privacy Policy Analysis:** Extract and evaluate data-usage statements from P3P policies against user preferences.
6.  **Analysis Comparison:** Compare goal and scenario sets from multiple analysts to identify conflicts and differences.
7.  **Audit Logging:** Maintain a secure log of all critical user actions.

### 2.3 User Characteristics
| Role | Expertise | Primary Objective |
| :--- | :--- | :--- |
| **Administrator** | IT System Administration | Manage system users, groups, and overall system health. |
| **Project Manager** | Project Management, Domain Knowledge | Define analysis projects, allocate resources (documents, analysts), and oversee progress. |
| **Analyst** | Requirements Engineering, Policy Analysis | Extract, classify, and manage goals and scenarios from assigned policy documents. |
| **Guest** | Varies (e.g., Auditor, Reviewer) | Read-only access to repository content as permitted by a Project Manager. |

### 2.4 Constraints
*   The system must process standard textual document formats (e.g., PDF, DOCX, TXT).
*   Development priority is on implementing the core database and High/Medium priority requirements for SPRAT and the RACAF module.
*   The system's access control analysis is dependent on the external Ponder policy editor.
*   Formal verification features are dependent on the external Alloy analyzer.

### 2.5 Assumptions and Dependencies
*   Users (Analysts) are trained in goal/scenario modeling techniques.
*   Policy documents provided for analysis are in a machine-readable text format.
*   The external tools (Ponder, Alloy) are available, installed, and accessible in the target deployment environment.
*   The system assumes a single organization/tenant model.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Management (UM)
*   **UM-1 (High):** The system shall allow an Administrator to create, view, update, and disable user accounts.
*   **UM-2 (High):** The system shall assign one of four roles to each user: Administrator, Project Manager, Analyst, or Guest.
*   **UM-3 (High):** The system shall authenticate users via a secure login mechanism (username and password).
*   **UM-4 (High):** The system shall store user passwords using a strong, salted cryptographic hash (e.g., bcrypt).
*   **UM-5 (Medium):** The system shall allow an Administrator to create and manage user groups for bulk permissions management.

#### 3.1.2 Policy Document Management (PDM)
*   **PDM-1 (Medium):** The system shall allow a Project Manager or Analyst to upload a policy document, storing its metadata (title, source, upload date, uploader).
*   **PDM-2 (Medium):** The system shall allow a user to classify a document into one or more domains (e.g., Healthcare, E-commerce, Financial).
*   **PDM-3 (Medium):** The system shall allow users with appropriate permissions to view, search, and delete policy documents.

#### 3.1.3 Goal & Scenario Management (GSM)
*   **GSM-1 (High):** The system shall allow an Analyst to create a new Goal, specifying at minimum: a unique ID, a descriptive name, a classification type (e.g., Security, Privacy, Functional), the source policy document, and a free-text description.
*   **GSM-2 (High):** The system shall allow an Analyst to create a new Scenario linked to one or more Goals.
*   **GSM-3 (High):** The system shall provide full CRUD operations for Goals and Scenarios to the user who created them (or a Project Manager/Admin).
*   **GSM-4 (Medium):** The system shall provide advanced search functionality for Goals and Scenarios by keyword, classification, document source, and date range.

#### 3.1.4 Project & Assignment Management (PAM)
*   **PAM-1 (Medium):** The system shall allow a Project Manager to create a Project, defining its name, description, and timeframe.
*   **PAM-2 (Medium):** The system shall allow a Project Manager to assign one or more Policy Documents and one or more Analysts to a Project.
*   **PAM-3 (Medium):** The system shall allow a Project Manager to grant Guest users view access to specific Projects, Documents, or Goal/Scenario sets.

#### 3.1.5 Access Control Analysis (RACAF Module - ACA)
*   **ACA-1 (Medium):** The system shall allow an Analyst to define a data hierarchy (e.g., MedicalRecord -> Diagnosis -> Treatment).
*   **ACA-2 (Medium):** The system shall allow an Analyst to define an organizational structure (e.g., departments, teams).
*   **ACA-3 (Medium):** The system shall allow an Analyst to define roles within the organizational structure.
*   **ACA-4 (Medium):** The system shall provide an interface to export the defined structures and rules to the Ponder policy editor for detailed rule specification.
*   **ACA-5 (Low):** The system shall provide an interface to generate an Alloy model from the Ponder specification and invoke the Alloy analyzer for verification.

#### 3.1.6 Privacy Policy Analysis (PPA)
*   **PPA-1 (Low):** The system shall parse a P3P privacy policy file to extract data-usage statements.
*   **PPA-2 (Low):** The system shall allow an Analyst to define or import a set of user privacy preferences.
*   **PPA-3 (Low):** The system shall compare the extracted P3P statements against the user preferences and highlight discrepancies.

#### 3.1.7 Comparison & Reporting (CR)
*   **CR-1 (Medium):** The system shall allow a user to select two or more sets of Goals/Scenarios (e.g., from different Analysts on the same document) for comparison.
*   **CR-2 (Medium):** The system shall generate a report highlighting additions, deletions, modifications, and potential conflicts between the compared sets.

#### 3.1.8 Audit Logging (AL)
*   **AL-1 (High):** The system shall automatically log all successful and failed login attempts (timestamp, username, IP address).
*   **AL-2 (High):** The system shall automatically log all add, edit, and delete actions performed on core entities (Users, Documents, Goals, Scenarios, Projects), including the user ID, action, entity ID, and timestamp.

### 3.2 Non-Functional Requirements

#### 3.2.1 Security
*   **SEC-1:** All authentication shall occur over an encrypted connection (TLS 1.2+).
*   **SEC-2:** Passwords shall not be stored in plaintext and must be hashed using a modern, adaptive algorithm (e.g., Argon2, bcrypt).
*   **SEC-3:** The system shall enforce session timeouts after a period of inactivity (configurable, default 30 minutes).
*   **SEC-4:** Audit logs shall be write-protected and accessible only to users with the Administrator role.

#### 3.2.2 Reliability
*   **REL-1:** The system shall have a measured uptime of 99.5% during business hours.
*   **REL-2:** User data (Goals, Scenarios, Documents) shall never be deleted as a side effect of disabling a user account or removing a user from a project.
*   **REL-3:** All database transactions for create, update, and delete operations shall be atomic to prevent data corruption.

#### 3.2.3 Usability
*   **USA-1:** A trained Analyst shall be able to add and classify a new Goal from a document within 3 minutes using the system interface.
*   **USA-2:** The web interface shall be consistent and conform to WCAG 2.1 Level AA guidelines for accessibility.

#### 3.2.4 Integration & Compatibility
*   **INT-1:** The system shall be capable of interfacing with Ponder2 policy editor via its standard file-based or API interface.
*   **INT-2:** The system shall be deployable on standard Java/Tomcat or Python/Django application servers.

### 3.3 External Interface Requirements

#### 3.3.1 User Interfaces
*   **UI-1:** A role-based dashboard presenting relevant tasks and information upon login.
*   **UI-2:** Intuitive forms for creating and editing Goals and Scenarios, with clear fields for classification.
*   **UI-3:** A visual comparison screen for side-by-side analysis of Goal/Scenario sets.

#### 3.3.2 Hardware Interfaces
*   None specified. The system is software-based.

#### 3.3.3 Software Interfaces
*   **SI-1 (Database):** The system shall connect to a MySQL (v8.0+) or PostgreSQL (v12+) database using standard JDBC/ODBC connectors.
*   **SI-2 (Ponder):** The system shall generate and read XML files compliant with the Ponder2 schema for policy specification.
*   **SI-3 (Alloy):** The system shall generate `.als` files and be able to invoke the Alloy analyzer command-line tool, capturing its output.

#### 3.3.4 Communications Interfaces
*   **CI-1:** The client and server shall communicate via HTTPS.

### 3.4 Priority & Acceptance

Requirements are prioritized as follows:
*   **High Priority:** UM-1 to UM-4, GSM-1 to GSM-3, AL-1, AL-2, SEC-1 to SEC-4, REL-2. **System acceptance is contingent on the correct implementation of all High Priority requirements.**
*   **Medium Priority:** PDM-1 to PDM-3, GSM-4, PAM-1 to PAM-3, ACA-1 to ACA-4, CR-1, CR-2. Required for core analytical workflows.
*   **Low Priority:** UM-5, ACA-5, PPA-1 to PPA-3. Desirable enhancements for future releases.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| Quality Assurance | | | |