# Pontis 5.0 Bridge Management System - Detailed Summary

## Background and Scope
Pontis 5.0 is the next-generation Bridge Management System (BMS) designed to replace the existing Pontis 4.x product line. Its primary purpose is to provide licensing agencies with an up-to-date tool for comprehensive bridge management, including data management, condition assessment, model development, needs analysis, reporting, and system integration. The system will build upon and preserve existing agency investments while incorporating modern software technologies and new functional capabilities. Non-goals include not assuming a uniform operating environment, not designing as a hosted application (though it may operate in such environments), and not providing specialized support for tablet/handheld computers at this time.

## Stakeholders Matrix and Use Cases
**Stakeholders:**
*   **Pontis Users (Inspectors, Bridge Project Planners, Bridge Management Engineers, etc.):** Day-to-day users responsible for data entry, analysis, project planning, and system operation.
*   **Pontis Task Force:** Oversees product quality, technical correctness, and project requirements.
*   **Pontis 5.0 Requirements Technical Advisory Group (TAG):** Develops requirements, architecture, and implementation plans.
*   **BRIDGEWare Integration TAG:** Coordinates impacts assessment, database design, and technology integration with other BRIDGEWare products.
*   **AASHTO:** Owns the software product, manages the project, and handles licensing and marketing.
*   **Contractor:** Responsible for the software design and development.

**Main Use Case Scenarios (≤8):**
1.  **Browse Bridge & Project Data:** Users find, filter, and select structures or projects to view detailed information, including via map-based queries.
2.  **Bridge Inventory & Inspection:** Users create/edit structure inventory and inspection records, including calculating derived ratings (e.g., NBI condition, Sufficiency Rating).
3.  **Preservation Model Development:** Advanced users update deterioration probabilities and action costs to develop optimal preservation policies and perform health index targeting.
4.  **Program Simulation:** Users configure and run network-level simulations to generate long-term work recommendations and budget needs.
5.  **Bridge Analysis:** Users perform structure-level simulations to assess the impact of specific work items on future condition.
6.  **Project & Program Development:** Users create and edit programs and projects, assigning work recommendations and managing funding.
7.  **Data Management:** Users perform data validation, import/export data (NBI, PDI, XML), archive data, and integrate with other BRIDGEWare systems.
8.  **System Administration:** Administrators manage user roles, authentication, application configuration, and system functionalities.

## Business Process
**Main Process: Bridge Management Cycle**
1.  **Trigger:** Scheduled inspection date or ad-hoc need.
2.  **Input:** Field inspection data.
3.  **Step 1 - Data Collection & Entry:** Inspector creates/edits inspection records in Pontis (UC-6).
4.  **Step 2 - Data Validation & Calculation:** System validates data and calculates derived ratings (e.g., NBI, Sufficiency) (UC-7, UC-15).
5.  **Step 3 - Preservation Modeling:** Engineer reviews and updates preservation models based on new data (UC-8).
6.  **Step 4 - Needs Analysis:** Engineer runs program simulations to generate network-level work recommendations and budget forecasts (UC-11).
7.  **Step 5 - Project Planning:** Planner creates projects by selecting simulation recommendations or inspector work candidates (UC-14).
8.  **Step 6 - Program Development:** Planner assigns projects to programs and funding sources (UC-13).
9.  **Output:** Funded bridge work program, condition reports, performance metrics.

**Key Branch A: Bridge-Level Analysis (from Step 4)**
1.  **Trigger:** Need to analyze a specific structure.
2.  **Input:** Selected bridge and potential work items.
3.  **Step B1:** User performs bridge analysis to see condition impact of work (UC-12).
4.  **Step B2:** User assigns selected work items to a project (UC-14).
5.  **Output:** Project plan for a specific bridge.

**Key Branch B: Data Exchange (from any step)**
1.  **Trigger:** Need to import legacy data or export for reporting.
2.  **Input/Output:** Data files (NBI, PDI, XML).
3.  **Step C1:** User imports data, with system performing validation (UC-16, UC-15).
4.  **Step C2:** User exports data for external systems or reporting (UC-16).
5.  **Output:** Updated database or external data file.

## Domain Model (Key Entities ≤8)
1.  **Structure:** Represents a physical bridge. Fields: StructureID (Key, Unique), Name, Location, Inventory Data (Various, Required).
2.  **Inspection:** A condition assessment event for a structure. Fields: InspectionID (Key), InspectionDate (Required), InspectorID (Reference), Element Data.
3.  **Element:** A component of a structure (e.g., deck, girder). Fields: ElementID (Key), Type, Environment, Quantity, Condition State.
4.  **Work Recommendation:** A suggested action for a structure/element. Fields: RecommendationID (Key), ActionType, Priority, Estimated Cost.
5.  **Project:** A planned set of work items. Fields: ProjectID (Key, Unique), Name, Status, Budget, ProgramID (Reference).
6.  **Program:** A funding and time framework for projects. Fields: ProgramID (Key), Name, Timeframe, FundingSource.
7.  **User:** An individual with system access. Fields: UserID (Key, Unique), Role (Reference), Authentication Info.
8.  **Scenario/Simulation Run:** A set of parameters and results for an analysis. Fields: ScenarioID (Key), Parameters, Results, RunDate.

## Interfaces and Integrations (≤8)
1.  **System:** GIS (e.g., ESRI, Intergraph). **Direction:** Bidirectional. **Theme:** Spatial display and selection. **Input:** Bridge/Project selections or spatial queries. **Output:** Map displays or lists of selected records. **SLA:** Responsive display refresh (<5 sec).
2.  **System:** Other BRIDGEWare Products (Virtis/Opis). **Direction:** Bidirectional. **Theme:** Data integration (e.g., load ratings). **Input:** Rating data from Virtis. **Output:** Updated bridge data in Pontis. **SLA:** Transaction integrity, coordinated releases.
3.  **System:** External via TransXML. **Direction:** Bidirectional. **Theme:** Standardized data exchange. **Input:** XML files following TransXML schema. **Output:** Pontis data in XML format. **SLA:** Schema compliance, successful import/export.
4.  **System:** National Bridge Inventory (NBI). **Direction:** Output. **Theme:** Regulatory reporting. **Input:** Pontis bridge data. **Output:** NBI-format file. **SLA:** Compliance with FHWA NBI coding guide.
5.  **System:** PDI Format. **Direction:** Bidirectional. **Theme:** Pontis-specific data exchange. **Input:** PDI files. **Output:** PDI files. **SLA:** Backward compatibility with Pontis 4.x.
6.  **System:** Authentication Service (e.g., Active Directory, LDAP). **Direction:** Input. **Theme:** User authentication. **Input:** User credentials. **Output:** Authentication token/verification. **SLA:** Secure, fast login (<2 sec).
7.  **System:** .NET Report Generator. **Direction:** Integrated. **Theme:** Reporting. **Input:** Data selections, report parameters. **Output:** Formatted reports (PDF, HTML, XML). **SLA:** Report generation (<20 sec for standard reports).
8.  **System:** Database (Oracle, SQL Server, Sybase). **Direction:** Integrated. **Theme:** Data persistence. **Input:** All application data transactions. **Output:** Stored data. **SLA:** High availability (98% uptime), transaction integrity.

## Acceptance Criteria
**Capability: Inspection Data Entry & Validation**
*   **Given** an inspector is logged in with appropriate privileges, **when** they enter a new inspection and save it, **then** the system shall validate the data against configured rules and highlight any errors before saving.
*   **Given** inspection data has been entered, **when** the user triggers the rating calculation, **then** the system shall correctly compute the NBI condition ratings, Sufficiency Rating, and SD/FO status per the defined algorithms.

**Capability: Program Simulation**
*   **Given** a set of bridges, a preservation policy, and a budget constraint are configured in a scenario, **when** a user runs a program simulation, **then** the system shall generate a multi-year schedule of recommended work actions and associated costs for the network.
*   **Given** a simulation has been run, **when** a user views the results, **then** they shall be able to see trends in network condition and the impact of different budget levels.

**Capability: Project Creation**
*   **Given** work recommendations exist from simulations or inspections, **when** a planner selects recommendations and creates a project, **then** the system shall create a project record with the associated work items, costs, and link to the affected structure(s).
*   **Given** a project exceeds its assigned program budget, **when** the planner attempts to save it, **then** the system shall warn the user of the budget overrun.

## Non-Functional Metrics
*   **Performance:** User login/logout in <2 seconds; Generate a standard report for 250 bridges in <20 seconds.
*   **Reliability/Availability:** 98% uptime during operational hours (18 hrs/day, 353 days/year).
*   **Security:** Support role-based access control, field-level security, and integration with enterprise single sign-on (SSO).
*   **Compliance:** Support data export in FHWA NBI format; Accommodate future NBI coding guide changes.
*   **Observability:** Adhere to .NET logging and exception handling standards; Provide administrator diagnostic reports.

## Milestones and Release Strategy (Recommended: Dedicated Design & Phased Release)
1.  **Design Completion & Prototypes:** June 2006 (Detailed design document and three prototypes).
2.  **Pontis 5.0 Release (Core + Inspection):** June 2007.
3.  **Pontis 5.1 Release (Project Planning + Gateway):** June 2008.
4.  **Pontis 5.2 Release (Preservation + Program Simulation + Configuration + Results):** June 2010.
5.  **Alpha/Beta Testing:** Preceding each major release (e.g., Alpha Nov 2006 for 5.0).
6.  **Final Release & Cutover:** Per phased schedule, allowing incremental agency adoption.

## Risk List and Mitigation Strategies
1.  **Requirement Creep:** Manage with a formal, approved requirements document (this FRS) and strict change control.
2.  **Technology Obsolescence:** Mitigate by using mainstream Microsoft .NET technologies and adopting a phased development approach to incorporate updates.
3.  **Development Cost/Schedule Overrun:** Use COSMIC-FFP estimation, phased delivery, and fixed-price contracting where possible.
4.  **NBI Coding Guide Changes:** Design for flexibility; allocate contingency in schedule/budget for incorporating changes.
5.  **Migration of Custom Agency Forms:** Develop a sunset strategy for PowerBuilder dependency; provide .NET plug-in architecture and migration tools.
6.  **User Dissatisfaction:** Engage users early via prototypes (in design phase) and phased releases for feedback.
7.  **BRIDGEWare Integration Complexity:** Coordinate closely with Virtis/Opis team and the BRIDGEWare Integration TAG throughout design and development.
8.  **Maintaining Pontis 4.x During Development:** Plan for limited, essential maintenance releases under a fixed-price agreement.

## Undecided Issues and Responsible Parties
1.  **Level of ADA/Section 508 Compliance:** To be determined by AASHTO in consultation with member agencies.
2.  **Selection of .NET-compliant Report Generator to replace InfoMaker:** AASHTO to provide a list of suggested tools.
3.  **Final Policy on Licensing/Enforcement for Web Application Users:** AASHTO to determine.
4.  **Specific Support for HTTP servers other than Microsoft IIS:** TAG to resolve technology consideration.
5.  **Implementation of Electronic Signatures (legal/policy aspects):** Dependent on state law and agency policy; AASHTO/agencies to determine.
6.  **Detailed Strategy for Integrating Single Sign-On across AASHTOWare:** Requires coordination with SCOJD and TAA committees.
7.  **Prioritization and Implementation of "Waiting Room" (may) requirements:** TAG and Pontis Task Force to review post-initial release.
8.  **Final Versions of all supporting software (.NET Framework, RDBMS, etc.):** To be determined during detailed design and implementation planning.