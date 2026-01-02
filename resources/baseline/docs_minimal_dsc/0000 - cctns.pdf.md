# Software Requirements Specification (SRS)
## National Crime Tracking and Management System (NCTMS)

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft for Review  
**Authors:** [System Architects/BA Team]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the National Crime Tracking and Management System (NCTMS). The primary purpose of this document is to provide a detailed description of the system's capabilities, interfaces, and performance characteristics. It serves as a contractual agreement between the stakeholders (National Police Agency, Police Personnel, and Citizens) and the development team, and will be the foundation for system design, implementation, and testing.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms **MUST**, **SHALL**, **REQUIRED**, **WILL**, **SHOULD**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in IETF RFC 2119.
*   **Formatting:** `Monospace` is used for system elements, file names, and database entities.

#### 1.3 Project Scope
The NCTMS is a centralized, national-level software application designed to create a unified network for tracking criminal activity and offender information. Its scope encompasses:
*   **In-Scope:**
    *   A citizen portal for online crime complaint registration and status tracking.
    *   A comprehensive case management system for police personnel to record, investigate, and prosecute crimes.
    *   Interfaces for managing interactions with judicial courts (e.g., filing charges, recording verdicts).
    *   Advanced search capabilities across cases, persons (victims, suspects, witnesses), and property.
    *   Secure, role-based access control and a complete audit trail.
    *   Offline operational capability for critical functions.
*   **Out-of-Scope:**
    *   Hardware provisioning for police stations.
    *   Direct integration with external forensic lab equipment software.
    *   Real-time facial recognition or predictive policing algorithms.
    *   Mobile applications for field officers (though the web system must be responsive).

#### 1.4 References
*   IETF RFC 2119: Key words for use in RFCs to Indicate Requirement Levels.
*   National Police Agency IT Security Policy v3.1.
*   Data Protection and Privacy Act [Jurisdiction-Specific Law].

### 2. Overall Description

#### 2.1 Product Perspective
The NCTMS is a new, self-contained system that will replace or integrate with legacy station-level records management systems. It will operate as a centralized web application accessible via secure national police intranet for personnel and via a public internet portal for citizens. It must interface with existing national identity databases (for person verification) and court management systems for data exchange.

#### 2.2 Product Functions
The high-level functions of the NCTMS are:
1.  **Citizen Complaint Management:** Receive, register, and acknowledge crime reports.
2.  **Investigation Workflow Management:** Guide and document steps from First Information Report (FIR) to case closure.
3.  **Prosecution & Court Management:** Track case progress through the judicial system.
4.  **Master Data Management:** Maintain centralized repositories for Persons, Properties, Vehicles, and Modus Operandi.
5.  **Information Retrieval:** Provide powerful search tools for analysis and reporting.
6.  **Communication Hub:** Facilitate secure messaging and notification between police and citizens.
7.  **System Administration:** Manage users, roles, permissions, and system configuration.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Citizen** | Computer literate; accesses via public web; requires simplicity and clarity. | File complaint easily, track status, receive updates, submit information securely. |
| **Records Clerk** | Police staff; primary data entry role; works at station. | Efficiently register complaints and persons, generate standard reports, manage documents. |
| **Investigation Officer (IO)** | Senior police personnel; manages active cases. | Full case overview, log investigative actions (interviews, evidence collection), assign tasks, prepare charge sheets. |
| **Superintendent/SP** | Supervisory role; oversees multiple cases and IOs. | Analytical dashboards, monitor case progress, approve sensitive actions, access all cases in jurisdiction. |
| **System Administrator** | IT staff at national/regional HQ. | User/role lifecycle management, system monitoring, audit log review, configuration. |

#### 2.4 Operating Environment
*   **Software:** Modern web browsers (Chrome, Firefox, Edge); Central application server (Linux/Windows); RDBMS (e.g., PostgreSQL, Oracle).
*   **Network:** Access via National Police Intranet (high-security zone) and public Internet (for citizen portal, via secure gateway).
*   **Hardware:** Must be scalable to support thousands of concurrent users across hundreds of police stations.

#### 2.5 Design and Implementation Constraints
1.  **Security:** Must comply with National Police Agency IT Security Policy.
2.  **Data Sovereignty:** All data must reside on servers within the national territory.
3.  **Audit Trail:** As per key constraints, an unalterable audit log is mandatory.
4.  **Legacy Integration:** Must support batch import from legacy systems in specified formats (CSV, XML).

#### 2.6 Assumptions and Dependencies
*   **Assumption:** All police stations will have stable, albeit sometimes limited, internet connectivity.
*   **Assumption:** Adequate training will be provided to all police personnel.
*   **Dependency:** Availability of national identity database APIs for person verification.
*   **Dependency:** Procurement and setup of application servers and database infrastructure by a separate IT project.

### 3. System Features and Requirements

#### 3.1 Feature: Case Management
**Description:** This feature allows police personnel to create, view, update, and manage criminal cases throughout their lifecycle.

**3.1.1 Functional Requirements**
*   `FR-101` The system SHALL allow an authorized Records Clerk or IO to create a new case record from a registered complaint.
*   `FR-102` The system SHALL capture case details including: Unique Case ID, crime type, date/time of incident, location, description, assigned IO, and current status (e.g., Registered, Under Investigation, Charged, Closed).
*   `FR-103` The system SHALL link persons (victims, suspects, witnesses) and property records to a case.
*   `FR-104` The system SHALL allow the assigned IO to log investigative actions (entries) with date, time, officer, and details.
*   `FR-105` The system SHALL enforce role-based access control (`NFR-201`) for viewing and editing case details.

#### 3.2 Feature: Citizen Complaint Portal
**Description:** This feature provides citizens with a secure interface to report crimes and interact with the police.

**3.2.1 Functional Requirements**
*   `FR-201` The system SHALL provide a public web form for citizens to register a crime complaint.
*   `FR-202` Upon submission, the system SHALL generate a unique, confidential tracking number for the complainant.
*   `FR-203` The system SHALL allow citizens to view the status of their complaint (using the tracking number) with appropriate privacy guards.
*   `FR-204` The system SHALL provide a secure messaging interface for citizens to submit additional information to the assigned IO.

#### 3.3 Feature: Search and Analysis
**Description:** This feature enables users to find cases, persons, and property using various filters.

**3.3.1 Functional Requirements**
*   `FR-301` The system SHALL provide a basic "quick search" across case numbers, person names, and property IDs.
*   `FR-302` The system SHALL provide an advanced search interface with multiple criteria (date range, crime type, location, suspect attributes, property details).
*   `FR-303` The system SHALL return search results as a paginated list, displaying key identifiers and summaries.
*   `FR-304` The system's search performance MUST meet the timing constraints specified in `NFR-401`.

#### 3.4 Feature: Audit and Security
**Description:** This feature ensures all actions are logged and access is strictly controlled.

**3.4.1 Functional Requirements**
*   `FR-401` The system SHALL automatically create an audit entry for every CREATE, UPDATE, DELETE, and VIEW (of sensitive data) action on a case, person, or property entity.
*   `FR-402` Audit entries SHALL be stored in a separate, write-once database table and SHALL include: timestamp, user ID, action type, entity ID, and a description of the change (old/new values).
*   `FR-403` The system SHALL implement a Role-Based Access Control (RBAC) model where permissions to view, edit, or close cases are defined by user roles and, where necessary, specific user/group assignments.

### 4. Non-Functional Requirements

#### 4.1 Security Requirements
*   `NFR-201` **Access Control:** The system SHALL implement RBAC. Access to a specific case MUST be restrictable to a defined set of users or groups (e.g., only the assigned IO and their superiors in the same station).
*   `NFR-202` **Audit Trail:** The system SHALL maintain a complete, cryptographically secured, and unalterable audit trail of all critical actions as defined in `FR-401`. Logs must be tamper-evident.

#### 4.2 Performance Requirements
*   `NFR-401` **Search Performance:**
    *   Simple search operations (single criterion) SHALL return a result list within **5 seconds** under peak load.
    *   Complex search operations (multiple criteria across large datasets) SHALL return a result list within **15 seconds**.
    *   Retrieval and full display of a single case record, with all linked data, SHALL occur within **5-20 seconds**, proportional to the complexity/size of the case.
*   `NFR-402` **Concurrent Users:** The system SHALL support at least 5000 concurrent authenticated users with acceptable response times (page load < 3s).

#### 4.3 Availability & Reliability Requirements
*   `NFR-301` **Availability:** The core system for police personnel SHALL be available 99.5% during business hours (06:00 - 22:00 local time, 7 days a week). Planned downtime for maintenance MUST NOT exceed 2 hours per month and must be scheduled during off-peak hours (02:00 - 04:00).
*   `NFR-302` **Offline Mode:** Critical functions, including **creating a new case entry** and **recording a basic investigative action**, SHALL be available in a degraded offline mode when network connectivity is lost. Data entered offline SHALL be synchronized automatically when connectivity is restored.

#### 4.4 Usability Requirements
*   `NFR-501` The user interface for Police Personnel SHALL be designed for efficiency, allowing an experienced Records Clerk to register a standard complaint in under 5 minutes.
*   `NFR-502` The Citizen Portal SHALL be usable by individuals with basic digital literacy, achieving a target System Usability Scale (SUS) score of 75+.

---
**APPROVAL**

| Name | Role | Signature | Date |
| :--- | :--- | :--- | :--- |
| [Police IT Head] | Product Owner | | |
| [Lead Architect] | Development Authority | | |
| [QA Manager] | Testing Authority | | |