# Detailed Summary: CCTNS Functional Requirements Specification V1.0

## Background and Scope
The Crime & Criminal Tracking Network and Systems (CCTNS) is an E-Governance Mission Mode Project under the Ministry of Home Affairs, Government of India. Its core scope for Version 1.0 is to deliver critical functionality that provides value to police personnel at the cutting edge, specifically to improve outcomes in "Investigation of Crime" and "Detection of Criminals." The system focuses on automating and streamlining police workflows related to crime registration, investigation, and prosecution, while also providing interfaces for citizens. Non-goals for this version include extensive integration with external judicial or prison systems beyond basic court interfacing, and full nationwide data unification without state-level configuration.

## Stakeholders Matrix and Use Cases
*   **Investigating Officer (IO):** Responsible for conducting crime investigations, updating case details, and managing evidence within the system.
*   **Records Room Staff:** Responsible for the initial registration of complaints, data entry, and maintenance of case records.
*   **Citizen/Complainant:** Uses the system to register complaints, track status, and receive acknowledgements or information from the police.
*   **Prosecution Constable:** Interfaces with courts and records prosecution-related updates and outcomes for cases.
*   **System Administrator:** Configures the application, manages user roles, access controls, and maintains state-specific data elements.
*   **Help Desk/Support Staff:** Manages user-reported defects, enhancement requests, and provides application support.

**Main Scenarios:** 1) Citizen registers an FIR online. 2) Records staff validates and creates a formal case. 3) IO is assigned, logs investigation steps and evidence. 4) IO uses search to find similar cases or criminal profiles. 5) Prosecution constable records court dates and judgments. 6) Citizen checks case status via the portal. 7) Administrator configures state-specific crime sections and categories.
**Exception Scenarios:** 1) User attempts to access a restricted case, triggering an audit log entry and access denial.

## Business Process
**Main Process: Crime Registration to Investigation**
1.  **Trigger:** Citizen submits a complaint (FIR) via the Citizen Interface or in person.
2.  **Input:** Complainant details, incident description, date/time, location.
3.  Records Room staff reviews and formally registers the case in the system.
4.  The case is assigned to an Investigating Officer (IO).
5.  IO logs investigation actions, interviews, evidence collected, and suspect information.
6.  IO may use the Search module to find links to other cases or criminals.
7.  Upon charge-sheet filing, the Prosecution module is updated with court details.
8.  **Output:** A digitally tracked case file with a full audit trail, accessible to authorized personnel.

**Key Branch A: Advanced Case Search**
1.  User (IO/Admin) initiates an advanced search.
2.  Inputs multiple criteria (person name, crime type, modus operandi, property).
3.  System queries the database and returns a filtered, customizable result set.
4.  User can view results by case or by criminal/accused profile.

**Key Branch B: Citizen Grievance Tracking**
1.  Citizen logs into the portal with complaint reference number.
2.  System fetches and displays the current case status and last action.
3.  Citizen can submit a follow-up query or request information.
4.  Designated police personnel receives an alert and responds via the portal.

## Domain Model
*   **Case/Complaint (required fields:** Case ID (unique), Registration Date/Time, Police Station, Crime Type, Status; **references:** Complainant, Accused, IO)
*   **Person (required fields:** Person ID (unique), Full Name, Gender; **references:** Role (Complainant, Witness, Accused, Suspect))
*   **Investigation Action (required fields:** Action ID, Date/Time, Type (e.g., Site Visit, Seizure), Description, IO; **references:** Case)
*   **Evidence (required fields:** Evidence ID, Type, Description, Seizure Date; **references:** Case, Seized By)
*   **Court Hearing (required fields:** Hearing ID, Date, Court Name, Purpose; **references:** Case)
*   **User (required fields:** User ID (unique), Name, Role, Police Station; **references:** User Group)
*   **Configuration Item (e.g.,** Crime Section, Property Type, State-specific lists) **(required fields:** Item Code, Item Type, Value; **constraint:** unique per type)
*   **Audit Log (required fields:** Log ID, Timestamp, User ID, Action, Entity Type, Entity ID) **(constraint:** unalterable)

## Interfaces and Integrations
*   **Citizen Portal (External, Inbound):** Theme: Complaint registration and status tracking. **Input:** Citizen details, complaint text. **Output:** Acknowledgement, status updates. **SLA:** Availability during defined citizen service hours.
*   **Police User Interface (Internal):** Theme: Primary application for all police workflows (Registration, Investigation, Prosecution, Search). **Input:** All case-related data. **Output:** Case records, search results, dashboards. **SLA:** High availability per System Availability requirements.
*   **Configuration Module (Internal):** Theme: Administration interface for state-specific setup. **Input:** Acts/Sections, user roles, data lists. **Output:** Configured application parameters.
*   **Support/Help Desk Module (Internal/External):** Theme: Logging and tracking defects/requests. **Input:** User issue description. **Output:** Ticket status, alerts. **SLA:** Accessible both within and outside the main application.
*   **Authentication Service (Internal):** Theme: Centralized user access and Single Sign-On. **Input:** Credentials. **Output:** Authentication token, role permissions. **SLA:** Must support multi-tier authentication and SSL.
*   **Audit Service (Internal):** Theme: Logging all critical system actions. **Input:** Action metadata. **Output:** Immutable audit trail. **SLA:** Data must be retained for the life of the case.
*   **Reporting Engine (Internal):** Theme: Generation of standard reports (monthly, RTI). **Input:** Search criteria, date ranges. **Output:** Formatted reports. **SLA:** Performance tied to search performance requirements.
*   **(Future) Court Systems (External, Outbound):** Theme: Basic data exchange for prosecution tracking. **Input:** Charge sheet details, hearing dates. **Output:** (Planned for future versions, not core V1.0).

## Acceptance Criteria
**For Capability: Crime Registration**
*   **Given** a citizen is on the complaint registration page, **When** they submit a valid complaint with mandatory details, **Then** the system must generate a unique reference number and an acknowledgement receipt.
*   **Given** a complaint is registered, **When** a Records Room staff member reviews it, **Then** they must be able to formally create a case and assign it to an IO, updating the status accordingly.

**For Capability: Case Investigation**
*   **Given** an IO is viewing an assigned case, **When** they add a new investigation action (e.g., "Evidence Seized"), **Then** the action must be timestamped, linked to the case, and recorded in the audit log.
*   **Given** an IO performs an advanced search, **When** they apply filters for crime type and date range, **Then** the system must return relevant case results within 10-15 seconds.

**For Capability: Access Control**
*   **Given** a user without access rights, **When** they attempt to search for or open a restricted case, **Then** the system must not display the case in results (or indicate its existence based on config) and must log the violation.

## Non-Functional Metrics
*   **Performance:** Simple search within 5-8 seconds; retrieve recently accessed case within 5-8 seconds. System must be scalable for varying police station sizes.
*   **Reliability/Availability:** Planned downtime not to exceed defined hours; unplanned downtime and incident frequency limits as specified. Must support offline mode for critical functions.
*   **Security:** Mandatory unalterable audit trail for all critical actions; role-based access control; prevention of SQL injection and cross-site scripting; data transmission over HTTPS/SSL.
*   **Compliance:** User interfaces must comply with ISO 9241 standards (usability, accessibility - including WCAG 1.0 for content).
*   **Observability:** System must provide audit reports organized by case, user, and chronology. Support module must enable tracking and reporting of defects.

## Milestones and Release Strategy
1.  Finalization of Core Functional Specifications (FRS V1.0).
2.  Design and approval of state-configurable architecture and data model.
3.  Development and unit testing of core modules (Registration, Investigation, Search, Configuration).
4.  Alpha deployment and testing in a pilot police station.
5.  Beta deployment in a select district, incorporating feedback.
6.  State-wide rollout V1.0, followed by planning for state-specific customizations and future integrations.

## Risk List and Mitigation Strategies
1.  **Risk:** Low user adoption due to resistance to change or complexity. **Mitigation:** Focus on user-intuitive design per usability standards, provide extensive context-sensitive help, and involve police personnel in UAT.
2.  **Risk:** Data quality issues during migration from legacy records. **Mitigation:** Implement robust data validation rules in the registration module; plan for phased data entry and verification.
3.  **Risk:** Network connectivity issues in remote police stations affecting online operation. **Mitigation:** Design system to work in an offline mode with critical functionality and sync when connected.
4.  **Risk:** Performance degradation with increasing data volume. **Mitigation:** Adhere to architectural recommendations (caching, indexing, batch data fetching, paged results).
5.  **Risk:** Security breaches or unauthorized data access. **Mitigation:** Implement stringent access control, audit trails, encryption (SSL, selective data encryption), and regular security audits.
6.  **Risk:** Inability to meet diverse requirements of different states. **Mitigation:** Build a highly configurable core system with a separate customization layer for state-specific extensions.
7.  **Risk:** Project delays due to scope creep. **Mitigation:** Strict adherence to the defined V1.0 core scope focused on investigation and detection value.
8.  **Risk:** Insufficient training leading to incorrect usage. **Mitigation:** Develop comprehensive training modules and manuals, and establish a dedicated support desk.

## Undecided Issues and Responsible Parties
1.  **Specific system availability hours and downtime thresholds (`<xx:00>`, `<xx hours>`):** To be finalized by Ministry of Home Affairs (MHA) in consultation with state police heads.
2.  **Detailed data exchange format and protocol with external court systems:** Responsibility of MHA/Technical Committee for future phase planning.
3.  **Final list of state-specific configuration items and their default values:** Responsibility of respective State Police departments to provide requirements.
4.  **Bandwidth specifications and minimum requirements for "low-bandwidth" police stations:** To be determined by the implementing agency's infrastructure team.
5.  **Specific encryption standards and protocols for data at rest:** Responsibility of Security Architecture team.
6.  **Detailed disaster recovery procedures and Recovery Time Objective (RTO):** To be defined by the Infrastructure and Operations team.
7.  **Policies for data retention and archival beyond the "life of the case":** Responsibility of MHA/Policy wing.
8.  **Mobile/PDA interface specifications and rollout plan:** Deferred to a future release; responsible party TBD.