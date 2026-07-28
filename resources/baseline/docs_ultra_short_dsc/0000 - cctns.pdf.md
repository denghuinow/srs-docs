# Software Requirements Specification (SRS)
## National Crime and Criminal Tracking Network (NCCTN)
**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the National Crime and Criminal Tracking Network (NCCTN). It is intended for use by project stakeholders, including police department leadership, system architects, developers, testers, and implementation teams, to ensure a common understanding of the system's capabilities and constraints.

#### 1.2 Scope
The NCCTN is a centralized, state-level E-Governance application designed to standardize and integrate core police workflows related to crime tracking across Indian states. The system's scope encompasses the end-to-end process from the registration of a crime complaint (First Information Report - FIR) through investigation, to prosecution tracking.

**In-Scope:**
*   Citizen complaint registration and status tracking.
*   Management of the criminal investigation lifecycle.
*   Recording of court interactions, hearings, and outcomes.
*   Search and retrieval of cases, persons (victims, accused, witnesses), and property.
*   Role-based dashboards, task management, and alerts for police personnel.
*   State-specific configuration of data and business rules.
*   Secure, auditable access for authorized users.

**Out-of-Scope:**
*   Broader law enforcement functions such as traffic management, personnel HR, payroll, or inventory management.
*   Real-time surveillance or predictive policing analytics.
*   Direct integration with national databases (though the architecture should allow for future integration).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **FIR** | First Information Report. The formal document to register a criminal complaint. |
| **IO** | Investigating Officer. The police officer responsible for a case. |
| **SOA** | Service-Oriented Architecture. |
| **RBAC** | Role-Based Access Control. |
| **PDA** | Personal Digital Assistant; refers to mobile data terminals. |
| **ISO 9241** | International standard for Ergonomics of Human-System Interaction. |

#### 1.4 References
*   ISO/IEC/IEEE 29148:2018 - Systems and software engineering — Life cycle processes — Requirements engineering.
*   ISO 9241-11:2018 - Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts.
*   Draft project charter and stakeholder interviews.

#### 1.5 Overview
The remainder of this SRS is structured as follows: Section 2 provides a general description of the product. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements. Appendices contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The NCCTN is a new, self-contained system intended to replace or augment disparate legacy systems used across state police forces. It will operate as a centralized application within a state, accessible to all police stations and authorized personnel.

**System Interfaces:**
*   **Citizen Web Portal:** A public-facing interface for complaint filing and status checks.
*   **Court System Interface:** A secure, standards-based interface (e.g., web services) for exchanging data with court management systems.
*   **Mobile/PDA Interface:** A simplified or responsive interface for access via authorized mobile data terminals.

#### 2.2 Product Functions
The high-level functional modules are:
1.  **Complaint Registration:** Digitally register and log FIRs and other complaints.
2.  **Investigation Management:** Manage the complete case diary, evidence, arrests, chargesheets, and IO assignments.
3.  **Prosecution Tracking:** Record court dates, public prosecutor inputs, and final case dispositions.
4.  **Search & Analysis:** Provide basic (quick) and advanced (parameterized) search across all entities.
5.  **Citizen Interface:** Facilitate online complaint submission, acknowledgment generation, and status tracking.
6.  **Dashboard & Task Management:** Provide role-specific home screens with pending tasks, alerts, and key performance indicators.
7.  **System Administration:** Configure state-specific workflows, data dictionaries, user roles, and security policies.

#### 2.3 User Characteristics
| User Category | Skill Level | Key Responsibilities |
| :--- | :--- | :--- |
| **Investigating Officer (IO)** | Moderate computer literacy. | Case investigation, updating case diaries, recording evidence, filing chargesheets. |
| **Records Room Clerk** | Basic to Moderate computer literacy. | Data entry, verification of registered complaints, archival management. |
| **Court Constable / Clerk** | Basic computer literacy. | Updating court hearing dates and outcomes in the system. |
| **Police Supervisor (e.g., SHO, DSP)** | Moderate computer literacy. | Monitoring case progress, assigning/reassigning IOs, reviewing reports. |
| **Citizen** | Varies widely. | Filing complaints online, checking complaint status. |
| **System Administrator** | High technical expertise. | User management, role configuration, system monitoring, state-specific customization. |

#### 2.4 Constraints
*   **Architectural:** Must be built on Open Standards and a Service-Oriented Architecture (SOA).
*   **Deployment:** Must support centralized state-level deployment with per-state customization (e.g., local languages, specific legal forms).
*   **Infrastructure:** Must function effectively in low-bandwidth environments (e.g., rural police stations).
*   **Client:** Must be primarily browser-based with minimal client-side software requirements (no heavy plugins).
*   **Legal:** Must adhere to Indian evidence law and criminal procedure code requirements for data integrity and audit.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Police stations will have access to basic computing infrastructure and intermittent internet connectivity.
*   **Assumption:** Adequate training will be provided to all police personnel users.
*   **Dependency:** Availability of standardized data exchange formats from court systems for integration.
*   **Dependency:** State governments will provide the necessary hosting infrastructure and security clearances.

### 3. Specific Requirements

#### 3.1 Functional Requirements
##### 3.1.1 Complaint Registration Module (FIR)
*   **FR-01:** The system shall allow authorized police personnel (e.g., Records Clerk) to digitally register a new FIR based on a complainant's statement.
*   **FR-02:** The system shall generate a unique, non-modifiable Case ID (FIR Number) following the state's prescribed numbering scheme.
*   **FR-03:** The system shall allow the attachment of scanned documents (e.g., handwritten complaint, identification) to the electronic FIR.
*   **FR-04:** The system shall automatically route the registered FIR to the designated Police Station In-charge and assign an Investigating Officer (IO).

##### 3.1.2 Investigation Management Module
*   **FR-05:** The system shall provide a Case Diary for the IO to chronologically record all investigation steps, findings, and expenses.
*   **FR-06:** The system shall allow the IO to record details of accused persons, victims, witnesses, and seized property, linking them to the case.
*   **FR-07:** The system shall track the status of an accused (e.g., wanted, arrested, released) and property (e.g., seized, returned to court).
*   **FR-08:** The system shall facilitate the digital preparation and submission of the Chargesheet, linking it to the case and accused.

##### 3.1.3 Search Module
*   **FR-09:** The system shall provide a "Basic Search" allowing users to find a case using its unique FIR number or name of a involved person. Results must be returned within **5-8 seconds**.
*   **FR-10:** The system shall provide an "Advanced Search" with multiple parameters (crime type, date range, location, property details, etc.). Results must be returned within **10-15 seconds**.
*   **FR-11:** Search results for cases shall provide a summary view, with the option to drill down to the full case details.

##### 3.1.4 Citizen Interface Module
*   **FR-12:** The system shall provide a public website where citizens can file a complaint online by filling a structured form.
*   **FR-13:** Upon successful online submission, the system shall generate an immediate electronic acknowledgment with a unique tracking number.
*   **FR-14:** Citizens shall be able to check the status of their complaint using the tracking number and a registered mobile number for OTP authentication.

##### 3.1.5 Security & Audit Module
*   **FR-15:** The system shall maintain a complete, unalterable audit trail logging every user login, data creation, modification, deletion, and view (for sensitive records) with timestamp and user identity.
*   **FR-16:** The system shall implement Role-Based Access Control (RBAC). Access to functions and data shall be determined strictly by the user's assigned role(s).
*   **FR-17:** The system shall support multi-tier authentication (e.g., User ID/Password + OTP on registered mobile) for police personnel.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
*   **NFR-PER-01:** The system shall retrieve a recently accessed, full case record from the database and display it within **5-8 seconds**.
*   **NFR-PER-02:** Response times for all standard data entry transactions (e.g., saving a case diary entry) shall be under **3 seconds** under normal load.

##### 3.2.2 Reliability & Availability
*   **NFR-REL-01:** The system must have an "offline mode" capability. Critical functions like data entry for new FIRs and case diaries must be available when the network is disconnected, with automatic synchronization when connectivity is restored.
*   **NFR-AVA-01:** The system shall have defined, quantifiable targets for both planned maintenance windows and unplanned downtime (e.g., 99.5% availability). Specific thresholds are to be defined during architectural design.
*   **NFR-REL-02:** The system shall employ mechanisms to prevent data loss during network or local hardware failure.

##### 3.2.3 Security
*   **NFR-SEC-01:** All data in transit between the client and server, and between integrated systems, shall be encrypted using SSL/TLS (HTTPS) or VPN.
*   **NFR-SEC-02:** Audit trails shall be stored in a secure, write-once medium and shall be non-repudiable.
*   **NFR-SEC-03:** The system shall be designed to prevent common web vulnerabilities (OWASP Top 10), including SQL injection, cross-site scripting (XSS), and unauthorized direct object access.

##### 3.2.4 Usability
*   **NFR-USA-01:** The user interface shall conform to the usability principles defined in **ISO 9241**, including suitability for the task, learnability, and error tolerance.
*   **NFR-USA-02:** The interface shall be accessible, providing support for screen readers and keyboard navigation to meet standard accessibility guidelines.
*   **NFR-USA-03:** Role-based dashboards shall be clear, showing pending tasks, critical alerts, and relevant summary statistics without information overload.

##### 3.2.5 Design Constraints
*   **NFR-DES-01:** The system shall be designed with a responsive web interface to be usable on standard desktop browsers and PDAs/mobile data terminals.
*   **NFR-DES-02:** The application architecture shall be service-oriented (SOA), exposing core functionalities as independent, reusable web services.

### 4. Appendices

#### 4.1 Priority Classification
*   **Priority 1 (Critical):** Requirements essential for core police workflow. Must be delivered in the first release. (e.g., FR-01, FR-02, FR-05, FR-09, FR-15).
*   **Priority 2 (High):** Important requirements that add significant value but the system can function minimally without them in initial rollout. (e.g., FR-12 Citizen Interface, FR-10 Advanced Search).
*   **Priority 3 (Medium):** Enhancements and reporting features that can be delivered in subsequent phases.

#### 4.2 Acceptance Criteria
Formal system acceptance will be contingent upon:
1.  Successful demonstration of all **Priority 1** functional requirements.
2.  Verification that performance metrics (Section 3.2.1) are met under simulated load.
3.  Successful completion of a security audit validating the unalterable audit trail, RBAC implementation, and vulnerability assessment.
4.  Validation of offline mode functionality and data synchronization.
5.  Usability testing confirming alignment with ISO 9241 principles for key user roles.

---
*Document End*