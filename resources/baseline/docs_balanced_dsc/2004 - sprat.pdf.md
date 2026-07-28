# Software Requirements Specification (SRS)
## Security and Privacy Requirements Analysis Tool (SPRAT)

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Security and Privacy Requirements Analysis Tool (SPRAT). The intended audience includes project stakeholders, developers, testers, and project managers. This SRS serves as the definitive specification for the system's capabilities, constraints, and external interfaces.

#### 1.2 Scope
SPRAT is a web-based application designed to assist requirements analysts in systematically mining, reconciling, and managing goals and scenarios derived from privacy and security policies (e.g., P3P, EPAL). The core functionality centers on maintaining a traceable repository of analyzed artifacts (goals, scenarios, requirements) linked to their source documents. Key features include role-based access control, multi-user analysis with comparison capabilities, and an integrated module for formal access control analysis (RACAF). The tool is intended to support the early stages of secure systems development by providing structured analysis and conflict detection.

**In-Scope:**
*   User management and role-based project access.
*   Policy document ingestion and management.
*   Manual goal extraction, classification, and repository management.
*   Scenario creation and linkage to goals and requirements.
*   Search, query, and comparison of analysis artifacts.
*   Requirements-level Access Control Analysis Framework (RACAF).
*   Comprehensive audit logging.

**Out-of-Scope:**
*   Fully automated natural language processing for goal extraction.
*   Real-time collaborative editing of analysis artifacts.
*   Full lifecycle requirements management beyond the goal/scenario level.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SPRAT:** Security and Privacy Requirements Analysis Tool.
*   **RACAF:** Requirements-level Access Control Analysis Framework.
*   **P3P:** Platform for Privacy Preferences Project.
*   **EPAL:** Enterprise Privacy Authorization Language.
*   **Goal:** A high-level objective derived from a policy statement (e.g., "Protect user email from unauthorized access").
*   **Scenario:** A sequence of steps describing system behavior to satisfy one or more goals.
*   **Analyst:** A user role responsible for performing policy analysis within the tool.
*   **PK:** Primary Key (database identifier).

#### 1.4 References
*   Project Charter: "Balanced Summary: Security and Privacy Requirements Analysis Tool (SPRAT)"
*   P3P Specification 1.1, W3C.
*   EPAL Specification, IBM.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general product description. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements. Appendices contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
SPRAT is a standalone web application. It will interact with external components for advanced features:
*   **External Policy Editors:** The RACAF module will provide interfaces for tools like **Ponder** for policy specification.
*   **Formal Verification Tools:** The RACAF module will generate specifications for tools like **Alloy** for analysis.
*   **Policy Documents:** The system will parse and import structured policy documents (P3P, EPAL).

#### 2.2 Product Functions (Summary)
1.  **User & Access Management:** Secure authentication and authorization for distinct user roles.
2.  **Project & Document Management:** Creation of projects, ingestion of policy documents, and assignment of analysts.
3.  **Goal Management:** Extraction, classification, storage, and search of policy goals with traceability links.
4.  **Scenario Management:** Creation, editing, and association of scenarios with goals and system requirements.
5.  **Analysis & Reporting:** Flexible searching, detailed views, and comparison of analyses from multiple users.
6.  **Access Control Analysis (RACAF):** Specification of subjects, objects, actions, and rules for formal policy analysis.
7.  **Audit Logging:** Automatic recording of all critical user actions for security and compliance.

#### 2.3 User Characteristics
| Role | Skill Level | Primary Responsibility |
| :--- | :--- | :--- |
| **Administrator** | High technical skill | System configuration, user/group management. |
| **Project Manager** | Medium-High domain skill | Project lifecycle management, analyst assignment, access control. |
| **Analyst** | Medium domain skill (Privacy/Security) | Performing policy analysis, defining goals/scenarios/requirements. |
| **Guest** | Variable | Read-only review of published analysis results. |

#### 2.4 Constraints
1.  **Technical:** Must support parsing of standard P3P and EPAL policy formats.
2.  **Security:** Must implement secure password hashing (e.g., bcrypt) and role-based access control.
3.  **Dependency:** RACAF module functionality is partially dependent on external formal methods tools.

#### 2.5 Assumptions and Dependencies
*   Users have a modern web browser.
*   Analysts have basic training in goal/scenario modeling.
*   The successful integration of the RACAF module depends on the stable definition of its external interfaces with Ponder and Alloy.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
*   **3.1.1 User Interfaces:** Web-based, responsive interface. Key screens include: Login, Dashboard (role-specific), Project Workspace, Policy Viewer, Goal/Scenario/Requirement Entry Forms (with templates), Search/Comparison Results.
*   **3.1.2 Software Interfaces:**
    *   **RACAF to Ponder:** The system shall provide an export function to generate a Ponder policy specification stub based on RACAF-defined rules.
    *   **RACAF to Alloy:** The system shall generate a partial Alloy model from the RACAF organizational structure and rule specification to aid formal verification.

#### 3.2 Functional Requirements

**3.2.1 User Authentication & Authorization (UAA)**
*   **UAA-1:** The system shall require username and password for user authentication.
*   **UAA-2:** The system shall store passwords using a strong, salted cryptographic hash.
*   **UAA-3:** The system shall enforce role-based permissions (Administrator, Project Manager, Analyst, Guest) upon login.
*   **UAA-4:** An Administrator shall be able to create, modify, enable, disable, and delete user accounts and user groups.

**3.2.2 Project & Document Management (PDM)**
*   **PDM-1:** A Project Manager shall be able to create a new project, defining its name and domain.
*   **PDM-2:** A Project Manager shall be able to upload or import a policy document (plain text, P3P, EPAL) into a project repository.
*   **PDM-3:** The system shall automatically calculate and store a Flesch Readability Score for uploaded text-based policy documents.
*   **PDM-4:** A Project Manager shall be able to assign one or more Analysts to a project.
*   **PDM-5:** A Project Manager shall be able to set view permissions for Guest users on a per-project or per-document basis.

**3.2.3 Goal Mining & Management (GMM)**
*   **GMM-1:** An Analyst shall be able to select an assigned policy document and create a new Goal artifact.
*   **GMM-2:** When creating a Goal, the Analyst shall be required to provide a Description and classify it using a system-defined taxonomy (e.g., Policy/Scenario, Protection/Vulnerability, Functional/Non-Functional).
*   **GMM-3:** The system shall automatically and immutably link the Goal to its Source Policy Document (DocID).
*   **GMM-4:** The system shall provide a template-driven form for Goal entry to ensure consistency.
*   **GMM-5:** An Analyst shall be able to search for Goals using flexible, user-defined conditions (e.g., by keyword, taxonomy, source policy, actor).

**3.2.4 Scenario & Requirement Management (SRM)**
*   **SRM-1:** An Analyst shall be able to create a Scenario, specifying its Name, Actors, Sequence of Events/Actions, and Pre/Post-Conditions.
*   **SRM-2:** An Analyst shall be able to link a Scenario to one or more existing Goals.
*   **SRM-3:** An Analyst shall be able to create a Requirement, providing a Description and linking it to one or more Goals and/or Scenarios.
*   **SRM-4:** An Analyst shall be able to search for and reuse existing Scenarios across different Goals or projects where permissions allow.

**3.2.5 Analysis & Comparison (AC)**
*   **AC-1:** The system shall allow users to view a detailed breakdown of any Goal, including its classification, source policy, and linked Scenarios/Requirements.
*   **AC-2:** To prevent bias, the system shall withhold an Analyst's goal classifications from other Analysts working on the same document until the Project Manager marks the Analyst's analysis as "Complete."
*   **AC-3:** A Project Manager shall be able to initiate a comparison report showing the goal classifications from multiple Analysts for the same policy document, highlighting areas of agreement and disagreement.
*   **AC-4:** Guests shall be able to view policy information and analysis results for which they have been granted explicit view permission by a Project Manager.

**3.2.6 Access Control Analysis - RACAF (RAC)**
*   **RAC-1:** An Analyst shall be able to define Data Objects (e.g., CustomerEmail, MedicalRecord) within the RACAF module.
*   **RAC-2:** An Analyst shall be able to define an Organizational Structure (e.g., roles like Doctor, Nurse; groups like Cardiology Dept.).
*   **RAC-3:** An Analyst shall be able to specify Access Control Rules linking Subjects (roles/groups), Objects, and Actions (Read, Write, Delete).
*   **RAC-4:** The system shall provide partial, automated support for translating the defined RACAF rules into a format suitable for external formal verification tools.

**3.2.7 System Auditing (SA)**
*   **SA-1:** The system shall automatically log all user actions involving the addition, modification, or deletion of any core artifact (User, Policy Document, Goal, Scenario, Requirement, RACAF Policy).
*   **SA-2:** Audit logs shall be viewable only by Administrators and Project Managers within their project scope.

#### 3.3 Non-Functional Requirements

**3.3.1 Security**
*   The system shall use HTTPS for all communications.
*   Passwords shall be hashed using a modern, adaptive algorithm (e.g., Argon2id, bcrypt).
*   Session management shall be secure against common attacks (e.g., session fixation, hijacking).

**3.3.2 Usability**
*   The system shall provide intuitive, template-based forms for entering Goals, Scenarios, and Requirements.
*   The average Analyst shall be able to perform basic goal extraction and classification with less than 30 minutes of training.

**3.3.3 Reliability & Data Integrity**
*   The system shall maintain referential integrity for all traceability links (e.g., a Goal cannot be deleted if it is linked to a Requirement).
*   The system shall ensure an audit trail is never altered or deleted by standard users.

**3.3.4 Performance**
*   Search operations on the Goal repository shall return results within 3 seconds for repositories of up to 10,000 goals.

**3.3.5 Interoperability**
*   The RACAF module shall provide export functionality compatible with Ponder2 syntax.
*   The system shall successfully parse and import valid P3P 1.1 and EPAL 1.2 policy files.

### 4. Supporting Information

#### 4.1 Data Dictionary (Entity-Attribute Summary)
*   **User:** `UserID` (PK), `Username`, `Role`, `PasswordHash`, `Email`, `GroupMemberships`, `IsActive`
*   **PolicyDocument:** `DocID` (PK), `ProjectID`, `FileName`, `DocumentType`, `RawText`, `FleschScore`, `UploadDate`, `UploadedBy`
*   **Goal:** `GoalID` (PK), `DocID` (FK), `Description`, `TaxonomyClass`, `SubjectClassification`, `Actor`, `CreatedBy`, `CreatedDate`, `AnalysisStatus`
*   **Scenario:** `ScenarioID` (PK), `Name`, `NarrativeText`, `PreConditions`, `PostConditions`, `CreatedBy`, `LinkedGoalIDs`
*   **Requirement:** `ReqID` (PK), `Description`, `Priority`, `LinkedGoalIDs`, `LinkedScenarioIDs`, `Constraints`
*   **RACAF_Policy:** `PolicyID` (PK), `Subject`, `Object`, `Action`, `RuleType` (Allow/Deny), `RuleSpecification`
*   **AuditLog:** `LogID` (PK), `Timestamp`, `UserID`, `Action`, `EntityType`, `EntityID`, `Details`

#### 4.2 Open Issues / TBDs
1.  The specific statistical algorithms (e.g., Cohen's Kappa) to be used for the multi-user analysis comparison report.
2.  The detailed user interface workflow and data model for the dedicated EPAL analysis section.
3.  The precise mechanism and scope for "dynamic" addition of new goal classification types by Administrators.
4.  The final access control matrix defining which analytical metrics (e.g., goal occurrence counts) are visible to the Guest role.
5.  The complete specification for the "partial translation" of Ponder policies to Alloy, including error handling for unsupported constructs.

---
*This document is approved by:*
**Sponsor:** Dr. Annie I. Antón
**Development Lead:** Qingfeng He / William Stufflebeam