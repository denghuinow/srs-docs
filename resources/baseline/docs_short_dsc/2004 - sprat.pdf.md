# Software Requirements Specification (SRS)
## Security and Privacy Requirements Analysis Tool (SPRAT)

**Document Version:** 1.0  
**Date:** [Date of Creation]  
**Authors:** [Author Names]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Security and Privacy Requirements Analysis Tool (SPRAT). It is intended for use by the project stakeholders, including the development team, project sponsors, and end-users, to ensure a common understanding of the system's capabilities, constraints, and objectives.

#### 1.2 Scope
SPRAT is a web-based application designed to assist requirements analysts in systematically extracting, managing, and reconciling security and privacy goals and scenarios from formal policy documents. Its core purpose is to ensure system requirements align with stated policies, prevent conflicts, and maintain a fully traceable repository of analysis artifacts to support compliance and foster stakeholder trust.

**In-Scope Features:**
*   Implementation of a four-tiered user access control model.
*   Core modules for creating, managing, and tracing goals, scenarios, and policies.
*   Integration of the Requirements-level Access Control Analysis Framework (RACAF).
*   Provision of structured templates for common policy and analysis artifacts.
*   Support for multi-user analysis comparison and basic conflict identification.

**Out-of-Scope Items:**
*   Full implementation of low-priority functional requirements (e.g., dynamic goal classification).
*   Complete automation of formal verification (e.g., full Ponder-to-Alloy translation).
*   Support for non-web-based systems or unrelated document types.
*   A comprehensive, production-ready demo version.
*   Detailed statistical analysis modules without further consultation.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SPRAT:** Security and Privacy Requirements Analysis Tool.
*   **RACAF:** Requirements-level Access Control Analysis Framework.
*   **P3P:** Platform for Privacy Preferences Project.
*   **EPAL:** Enterprise Privacy Authorization Language.
*   **Goal:** A high-level objective related to security or privacy, extracted from a policy.
*   **Scenario:** A concrete narrative or use case that operationalizes a goal.
*   **Policy:** A formal document (e.g., P3P, EPAL, Ponder, natural language) specifying rules and constraints.
*   **Analyst:** A user role responsible for performing the core analysis work.
*   **Traceability:** The ability to link derived requirements (goals, scenarios) back to their source policy statements.

#### 1.4 References
*   Project Charter: "Security and Privacy Requirements Analysis Tool (SPRAT)"
*   RACAF Framework Documentation
*   P3P 1.1 Specification
*   EPAL 1.2 Specification

#### 1.5 Overview
The remainder of this SRS is organized as follows: Section 2 provides a general product description. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
SPRAT is a standalone, web-based application. It must support integration with external tools for enhanced functionality, specifically:
*   **Import/Export Interface** for policy files from tools like the Ponder policy editor.
*   **Data Export** capability to feed specifications into formal verification tools like Alloy.

#### 2.2 Product Functions (Summary)
1.  **User & Project Management:** Secure authentication and role-based management of users, projects, and document assignments.
2.  **Policy Management:** Upload, store, categorize, and view policy documents.
3.  **Goal & Scenario Analysis:** Create, classify, tag, and manage goals and scenarios using provided templates.
4.  **Traceability Management:** Establish and visualize explicit links between policy statements, goals, scenarios, and derived access control rules.
5.  **RACAF Integration:** Guided process for performing data, task, and organizational analysis to derive access control requirements.
6.  **Multi-User Analysis & Comparison:** Allow multiple analysts to work on the same policy and provide mechanisms to compare their classifications and identify conflicts.
7.  **Reporting & Logging:** Generate access logs and traceability reports.

#### 2.3 User Characteristics
| Role | Skill Level | Key Responsibilities |
| :--- | :--- | :--- |
| **Administrator** | Expert in system administration. | Manage user accounts, reset passwords, configure system-wide settings, maintain system security. |
| **Project Manager** | Proficient in project management and requirements engineering. | Create/manage projects, assign analysts to policies, manage guest access permissions, oversee analysis progress. |
| **Analyst** | Knowledgeable in security/privacy policies and requirements analysis. | Perform core analysis: extract and classify goals/scenarios, use RACAF, define access rules, resolve conflicts. |
| **Guest** | Variable; may have limited technical knowledge. | Read-only access to view policy documents, associated goals, and scenarios as permitted by a Project Manager. |
| **Project Sponsor** | Strategic oversight. | Provides direction, funding, and final requirement approval. Typically does not interact directly with the tool. |

#### 2.4 Constraints
1.  **Security:** Must enforce secure password storage (e.g., hashing with salt) and encrypted login procedures.
2.  **Integrity:** Multi-user comparison features must withhold other analysts' classifications until a user submits their own analysis to prevent bias.
3.  **Development Priority:** Initial development phase focuses on database implementation and high/medium priority requirements, with RACAF integration as a key milestone.
4.  **Compatibility:** Must support integration points for external tools (Ponder editor, Alloy analyzer).
5.  **Access Control:** A strict role-based access control (RBAC) model with four distinct privilege levels must be enforced throughout the application.

#### 2.5 Assumptions and Dependencies
*   Users have a modern web browser.
*   Analysts possess basic training in security/privacy concepts and the SPRAT methodology.
*   Policy documents provided for analysis are in a supported format (text, PDF, or specific XML formats for P3P/EPAL).
*   Success of the RACAF module is dependent on clear framework documentation.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
*   **UI-01:** A responsive web interface compatible with major browsers (Chrome, Firefox, Safari Edge).
*   **UI-02:** Dashboard view tailored to user role (Admin, Project Manager, Analyst, Guest).
*   **UI-03:** Modal forms and side-by-side panels (e.g., for rule specification alongside scenarios) to minimize context switching.

**3.1.2 Software Interfaces**
*   **SI-01:** Database: A relational database (e.g., PostgreSQL, MySQL) for persistent storage of all artifacts and user data.
*   **SI-02:** Application Server: A backend framework (e.g., Django, Spring Boot, Node.js) to host business logic and API.
*   **SI-03:** File System: Secure storage for uploaded policy documents.

#### 3.2 Functional Requirements
**3.2.1 User Management Module**
*   **FR-UM-01:** The system shall allow Administrators to create, enable, disable, and delete user accounts.
*   **FR-UM-02:** The system shall assign one of four roles (Administrator, Project Manager, Analyst, Guest) to each user upon creation.
*   **FR-UM-03:** The system shall allow users to authenticate via a username and secure password.
*   **FR-UM-04:** The system shall allow Administrators to reset passwords for any user.
*   **FR-UM-05:** Disabling a user account shall prevent login but preserve all historical data created by that user.

**3.2.2 Project & Policy Management Module**
*   **FR-PM-01:** The system shall allow Project Managers to create, archive, and delete projects.
*   **FR-PM-02:** The system shall allow Project Managers to upload, categorize, and store policy documents within a project.
*   **FR-PM-03:** The system shall allow Project Managers to assign one or more Analysts to a specific policy document for analysis.
*   **FR-PM-04:** The system shall allow Project Managers to grant Guest users view access to specific projects or policy documents.

**3.2.3 Goal & Scenario Analysis Module**
*   **FR-GS-01:** The system shall provide a template for creating a Goal, including fields for: ID, Description, Classification (Security/Privacy), Priority, and multiple Subject Tags.
*   **FR-GS-02:** The system shall provide a template for creating a Scenario, including fields for: ID, Description, linked Goal(s), and Actors.
*   **FR-GS-03:** The system shall allow an Analyst to create a traceability link from a Goal or Scenario back to a specific section of a source policy document.
*   **FR-GS-04:** The system shall allow an Analyst to view all Scenarios associated with a selected Goal.
*   **FR-GS-05:** The system shall provide dedicated form templates for specifying P3P statements and EPAL rules.

**3.2.4 RACAF Module**
*   **FR-RC-01:** The system shall provide a guided interface for performing Data Analysis (identifying data objects and their sensitivity).
*   **FR-RC-02:** The system shall provide a guided interface for performing Task Analysis (identifying tasks and required data).
*   **FR-RC-03:** The system shall provide a guided interface for performing Organizational Analysis (defining roles and hierarchies).
*   **FR-RC-04:** The system shall synthesize inputs from FR-RC-01, RC-02, and RC-03 to support the specification of access control policy rules.

**3.2.5 Multi-User Analysis & Comparison Module**
*   **FR-MC-01:** When multiple Analysts are assigned to the same policy, the system shall store each analyst's classifications (goals, scenarios, tags) separately.
*   **FR-MC-02:** The system shall prevent an Analyst from seeing another Analyst's classifications for a policy until they have marked their own analysis as "complete."
*   **FR-MC-03:** Once analyses are complete, the system shall provide a comparison view highlighting areas of agreement and conflict (e.g., differing goal classifications or tags).
*   **FR-MC-04:** The system shall automatically identify and flag potential conflicts based on predefined rules (e.g., the same text classified as both a Security and Privacy goal).

**3.2.6 System Logging & Reporting**
*   **FR-SL-01:** The system shall automatically log all critical user actions (Add, Edit, Delete) on core artifacts (Users, Projects, Policies, Goals, Scenarios, Rules), recording user ID, timestamp, and action details.
*   **FR-SL-02:** The system shall generate traceability reports showing the links between a policy document and all derived Goals and Scenarios.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   **PER-01:** The system shall support up to 50 concurrent users.
*   **PER-02:** Dashboard load time for an authenticated user shall be less than 3 seconds under normal load.

**3.3.2 Safety & Security Requirements**
*   **SEC-01:** All passwords shall be stored using a strong, salted cryptographic hash function.
*   **SEC-02:** All user sessions shall be conducted over HTTPS.
*   **SEC-03:** The system shall enforce role-based permissions on every user request; users shall only see and perform actions allowed by their role.
*   **SEC-04:** Access logs (FR-SL-01) shall be readable only by Administrators.

**3.3.3 Usability Requirements**
*   **USA-01:** A user with the Analyst role shall be able to add and classify a new Goal using the template within 2 minutes of locating the relevant policy text.
*   **USA-02:** The system shall provide contextual help or tooltips for form fields within the RACAF module.

**3.3.4 Reliability & Availability**
*   **REL-01:** The system shall have an uptime of 99.5% during core business hours (8 AM - 8 PM EST).

### 4. Appendices

#### 4.1 User Story Mapping to Functional Requirements
| User Story | Mapped Functional Requirements |
| :--- | :--- |
| 1. As a **Project Manager**, I want to assign analysts... | FR-PM-03 |
| 2. As an **Analyst**, I want to add and classify a new goal... | FR-GS-01 |
| 3. As an **Administrator**, I want to disable a user's access... | FR-UM-01, FR-UM-05 |
| 4. As an **Analyst**, I want to view all scenarios associated with a goal... | FR-GS-04 |
| 5. As a **Guest**, I want to view policy documents... | FR-PM-04 (implied) |
| 6. As an **Analyst**, I want to specify access control rules side-by-side... | UI-03, FR-RC-04 |

#### 4.2 Undecided Issues & TBDs
1.  The specific statistical algorithms (e.g., Cohen's Kappa, percentage agreement) to be used for quantifying inter-analyst agreement in the multi-user comparison module.
2.  The detailed workflow and user interface for the automated conflict resolution mechanism (beyond simple identification).
3.  The definitive feature list and functional limitations for the demo/trial version of SPRAT.
4.  The exhaustive set of input fields and UI widgets for the P3P statement and EPAL rule templates.
5.  The complete logic for handling all edge cases when a P3P policy is evaluated against a set of user preferences.