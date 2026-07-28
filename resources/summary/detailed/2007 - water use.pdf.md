# Detailed Summary: Water Use Tracking (WUT) Project

## Background and Scope
The Water Use Tracking (WUT) System is a GIS-based application designed to spatially and temporally track and analyze key regulatory and water resource management data for the Southwest Florida Water Management District (SWFWMD). Its primary purpose is to support the implementation and validation of the Southern Water Use Caution Area (SWUCA) Management Plan and SWUCA II Rules by providing tools to monitor permitted and actual water use, track trends, and assess impacts on Minimum Flows and Levels (MFLs). The system will integrate data from existing District databases (Regulatory, Water Management, and GIS) into a unified decision-support platform accessible to internal staff and external customers. Non-goals include major hardware/software infrastructure changes, direct modifications to source legacy systems (e.g., mainframe DB2), and implementation of all identified requirements in the initial release.

## Stakeholders Matrix and Use Cases
*   **Executive Sponsors (e.g., Bruce Wirth, Gene Heath, John Heuer):** Provide executive oversight and strategic direction for the project.
*   **Co-Sponsors (e.g., B.J. Jarvis, Mark Barcelo):** Oversee data entry, groundwater modeling, and ensure project adherence to SWUCA rules.
*   **Science Business Experts (e.g., Albert Bond, Mike Beach, Rand Frahm):** Estimate water use, run models for MFL tracking, and identify planning department applications.
*   **Regulatory Business Experts (e.g., Christine Jackson, John Parker, Ken Weber):** Provide permitting expertise, ensure rule compliance, and monitor regulatory implementation.
*   **Technical Experts (e.g., Steven Dicks, Priscilla Thoopthong, Sherrie Kubis):** Provide GIS, database, and programming support for system design and development.
*   **Other Impacted Parties (e.g., Richard Owen, Kurt Fritsch):** Provide planning perspective and ensure project scope is maintained.
*   **General WUT User (Internal/External):** Accesses the system to view maps, run reports, and query water use permit information.
*   **WUT Administrator:** Manages system configuration, news, and business rule parameters.
*   **Water Use Estimator:** Maintains estimated water use data for unmetered permits.

**Main Use Case Scenarios:** View Map, View Report, View Water Use Permit, View Water Use Permit Search, Process Database Replication, View Compliance Information, View Net Benefit Summary, View Lapsed Quantities Summary.
**Exception Scenarios:** System startup failure, data replication errors, unauthorized access attempts.

## Business Process
**Main Process: Analyze Water Use Permit Impact**
1.  **Trigger:** User (e.g., Permit Evaluator) logs into WUT system.
2.  **Input:** User credentials, area of interest (e.g., permit number, geographic boundary).
3.  Search for relevant permits using spatial or attribute criteria.
4.  Select a specific permit to view detailed information (owner, quantities, wells).
5.  Access related data: view pumpage history, compliance status, and associated wells on a map.
6.  Analyze Net Benefit or lapsed quantities related to the permit.
7.  Generate a report or export map summarizing findings.
8.  **Output:** Decision support package for permit evaluation or trend analysis.

**Key Branch A: Data Integration & Update**
1.  **Trigger:** Scheduled nightly job.
2.  Replicate changed data from source DB2 systems (RDB, WMDB) to Oracle.
3.  Normalize and restructure replicated data for reporting.
4.  Update GIS layers as needed.
5.  **Output:** Updated, normalized read-only database for WUT application.

**Key Branch B: Maintain Estimated Water Use**
1.  **Trigger:** Water Use Estimator needs to update unmetered permit data.
2.  Import new water use estimate data from external sources (e.g., SAS datasets).
3.  Validate and store estimates in WUT database.
4.  **Output:** Updated water use estimates available for reporting and analysis.

## Domain Model
Core entities and their key fields/constraints:
1.  **WaterUsePermit:** PermitID (unique), PermitNumber (unique), Status, IssueDate, ExpirationDate, PermitteeID (reference), TotalPermittedQuantity.
2.  **Permittee:** PermitteeID (unique), Name, ContactInfo.
3.  **Well/WithdrawalPoint:** WellID (unique), UID (unique, reference), PermitID (reference), Aquifer, Location (coordinates), ConstructionDetails.
4.  **PumpageRecord:** RecordID (unique), WellID (reference), Month, Year, ReportedQuantity, EstimatedQuantity (derived).
5.  **ComplianceRecord:** ComplianceID (unique), PermitID (reference), ReportType, SubmissionDate, Status.
6.  **NetBenefitTransaction:** TransactionID (unique), SourcePermitID (reference), DestinationPermitID (reference), Quantity, Type (e.g., Relocation, Lapsed, Credit), EffectiveDate.
7.  **SpatialBoundary:** BoundaryID (unique), Type (e.g., SWUCA, MIA, County), Geometry.
8.  **BusinessRuleParameter:** ParameterID (unique), Name, Value, EffectiveDate.

## Interfaces and Integrations
1.  **Regulatory Database (RDB):** Direction: Inbound. Interaction: Data replication. Input: Changed permit data. Output: Normalized permit data in Oracle. SLA: Nightly replication.
2.  **Water Management Database (WMDB):** Direction: Inbound. Interaction: Data replication. Input: Changed water level, flow, quality data. Output: Normalized resource data in Oracle. SLA: Nightly replication.
3.  **GIS (ArcSDE/Oracle):** Direction: Bi-directional. Interaction: Spatial data service. Input: Permit polygons, well points, base layers. Output: Map rendering and spatial queries. SLA: Concurrent access during business hours.
4.  **External Web Clients (Browser):** Direction: Outbound. Interaction: User interface delivery. Input: User requests. Output: HTML, maps, reports. SLA: Sub-second response for simple pages.
5.  **Water Use Estimates Source (SAS/Excel):** Direction: Inbound. Interaction: File import. Input: Estimation data files. Output: Records in WUT database. SLA: On-demand or scheduled import.
6.  **District Authentication System:** Direction: Inbound. Interaction: User authentication. Input: Credentials. Output: Authentication token/role. SLA: Real-time validation.

## Acceptance Criteria
**Capability: Spatial Permit Search**
*   Given a user is on the map view, When they draw a polygon around an area of interest, Then the system shall display all active water use permits within that boundary.
*   Given a user has searched for permits, When they click on a permit symbol on the map, Then a pop-up shall show basic permit details and a link to the full permit view.

**Capability: Net Benefit Reporting**
*   Given a user is viewing a specific permit, When they navigate to the Net Benefit summary, Then the system shall display all transactions (relocations, credits) where this permit was a source or destination.
*   Given a user runs the Net Benefit report for a geographic area, When they specify a date range, Then the report shall aggregate all net benefit quantities gained or lost in that area during the period.

## Non-functional Metrics
*   **Performance:** Map rendering for standard views completes within 5 seconds; permit search queries return results within 3 seconds.
*   **Reliability:** System availability of 99% during core business hours (7 AM - 6 PM); data replication process succeeds 99.9% of scheduled runs.
*   **Security:** Role-based access control enforced for all data and functions; all user authentication integrated with District system.
*   **Compliance:** System must support defensible permit decisions in line with SWUCA rules; metadata shall be FGDC compliant.
*   **Observability:** All system errors are logged with sufficient detail for debugging; usage statistics for key reports and maps are tracked.

## Milestones and Release Strategy
1.  Complete Elaboration Phase: Architectural proof-of-concepts and detailed design for core use cases.
2.  Initial Release (Construction Phase): Core functionality including Permit Search, View Map, View Permit, basic Reporting, and Data Replication.
3.  User Acceptance Testing: Internal stakeholder validation against prioritized requirements.
4.  Deployment to Production: Release to District intranet for internal users.
5.  Subsequent Release Planning: Prioritize and design remaining requirements (e.g., advanced MFL analysis, external user portal).
6.  Post-Deployment Support & Training: Ongoing maintenance and user training rollout.

## Risk List and Mitigation Strategies
1.  **Risk:** Source system changes (RDB/WMDB) not completed in time, blocking WUT requirements.
    *   **Mitigation:** Collaborate closely with IRD; scope contingency to implement needed data structures within WUT if necessary.
2.  **Risk:** Unclear or evolving SWUCA rule interpretations affecting requirements.
    *   **Mitigation:** Maintain regular dialogue with Regulatory stakeholders; design configurable business rules.
3.  **Risk:** Performance issues with large spatial datasets or complex queries.
    *   **Mitigation:** Prototype and load test early; optimize database schema and indexing; consider data aggregation for summaries.
4.  **Risk:** Insufficient user adoption due to complexity or lack of training.
    *   **Mitigation:** Involve power-users in design reviews; develop comprehensive training materials and phased rollout.
5.  **Risk:** Data quality issues in source systems leading to inaccurate WUT outputs.
    *   **Mitigation:** Implement data validation reports within WUT; establish process for reporting source data errors.
6.  **Risk:** Scope creep from numerous stakeholder requirements.
    *   **Mitigation:** Strict change control process; clear prioritization by project sponsors; defer non-core features to subsequent releases.
7.  **Risk:** Integration failures between DB2, Oracle, and GIS systems.
    *   **Mitigation:** Develop robust error handling and monitoring for replication jobs; have rollback procedures.
8.  **Risk:** Technical dependencies on specific versions of ArcGIS or .NET.
    *   **Mitigation:** Adhere to District standards; confirm compatibility with planned IT infrastructure upgrades.

## Undecided Issues and Responsible Parties
1.  **Final prioritization of requirements for the subsequent release.** (Responsible: Project Manager with Co-Sponsors)
2.  **Detailed security model and access control list for external users.** (Responsible: Technical Team Lead with Information Security)
3.  **Specific SLA for external (public) access, if offered.** (Responsible: Executive Sponsors)
4.  **Ownership and maintenance process for the "Quick Links" feature.** (Responsible: WUT Administrator)
5.  **Definitive process for correcting source data errors discovered via WUT.** (Responsible: Process Owner from Records & Data)
6.  **Training curriculum development and delivery responsibility.** (Responsible: Project Manager & Training Department)
7.  **Formal metadata management and librarian role assignment.** (Responsible: Mapping & GIS Manager)
8.  **Decision on implementation of specific advanced analytical tools (e.g., "heat maps").** (Responsible: Science Business Experts & Technical Lead)