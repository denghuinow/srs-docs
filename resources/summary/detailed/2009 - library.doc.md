# Detailed Summary: Management Processes for an Integrated Library System

## Background and Scope
This specification defines the requirements for the Management Processes module of an Integrated Library System (ILS) for the Georgia PINES consortium. It aims to replace and enhance the current Evergreen ILS reporting capabilities to support data-driven management of library services, collections, and patrons across 275+ locations. The scope includes reporting, analytics, and inventory tools for demographics, transactions, financials, and collection management, but excludes detailed specifications for the OPAC, Acquisitions, and Cataloging modules, as well as field-level UI/UX design, which will be handled iteratively.

## Stakeholders Matrix and Use Cases
*   **Patron**: A Georgia resident who uses library resources; provides usage data for anonymized analytics.
*   **Staff**: Library employees who provide services; run operational reports and manage daily workflows.
*   **Local System Administrator**: Library management staff overseeing processes; configure report templates and permissions for their system.
*   **Library Manager**: Supervisor of an organizational unit; uses reports for collection analysis and staff productivity.
*   **Library Director**: Executive planning and directing services; consumes high-level board and financial reports.
*   **Global System Administrator**: Consortium-level manager; implements system configurations and generates consortium-wide statistical reports.

**Main Scenarios**: 1) Administrator creates a secure, templated report for branch staff. 2) Manager analyzes collection use to inform weeding. 3) Director runs a pre-defined financial report for the library board. 4) Staff runs an on-demand report for items in transit.
**Exception Scenarios**: 1) A long-running report is queued and its status is monitored. 2) A report needs to be canceled after submission. 3) Data must be queried from a historical point-in-time snapshot. 4) A report filters on uncataloged material transactions.

## Business Process
**Main Process: Generate Management Report**
1.  **Trigger/Input**: Staff/administrator login with appropriate permissions.
2.  User selects report type (canned, on-demand, open template).
3.  User defines criteria (e.g., date range, location, item type) and output format.
4.  System validates permissions and query complexity.
5.  Report job is submitted to a processing queue.
6.  System executes query against operational or historical data warehouse.
7.  Results are compiled, anonymized where required, and formatted.
8.  **Output**: Report is delivered via UI or email in specified format (CSV, HTML, Excel).

**Key Branch A: Manage Report Templates**
1.  **Trigger**: Administrator needs to standardize a report.
2.  Administrator creates/clones a report template, defining fixed and editable fields.
3.  Template is saved to a shared folder with assigned permissions.
4.  **Output**: Template is available for authorized staff to run or modify within limits.

**Key Branch B: Execute Batch Inventory Action**
1.  **Trigger**: Need to transfer a batch of items between branches.
2.  Administrator uses utility to query candidate items and save the query.
3.  Items are selected and their location fields are updated.
4.  **Output**: Pull list is generated and item records are modified; reversion can be scheduled.

## Domain Model
*   **Report Template** (ID, Name, Description, Creator, Creation Date, SQL/Definition, isRecurring, Schedule, Output Format) - Required: Name, Creator.
*   **Report Job** (ID, Template_ID, Parameters, Requestor, Request Time, Status, Priority, Output File Path) - Required: Template_ID, Requestor, Status. Reference: Template.
*   **Library Entity** (ID, Name, Type [System/Branch], Capacity Metrics) - Required: Name, Type. Unique: ID.
*   **Item Record** (Barcode, Bib_ID, Location, Status, Circ_Modifier, Price, Last_Circ_Date, Total_Use_Count) - Required: Barcode, Status. Reference: Bib_ID, Location.
*   **Patron Record** (ID, Home Library, Type, Registration Date, Demographic Category [Age, Zip]) - Required: ID, Home Library.
*   **Financial Transaction** (ID, Patron_ID, Item_ID, Type [Fine, Payment], Amount, Date, Payment Method) - Required: Type, Amount, Date. Reference: Patron_ID.
*   **Circulation Transaction** (ID, Item_ID, Patron_ID, Type [Checkout, Renewal], DateTime, Terminal, Location) - Required: Type, DateTime, Item_ID. Reference: Item_ID, Patron_ID.
*   **Hold Transaction** (ID, Patron_ID, Item_ID, Status, Place_Date, Fulfill_Date, Pickup Location) - Required: Patron_ID, Status. Reference: Patron_ID, Item_ID.

## Interfaces and Integrations
*   **Evergreen ILS Core**: Internal. Direction: Bi-directional. Interaction: Data access for reports. Input: Query parameters. Output: Result sets. SLA: Reports must not disrupt core circulation functions during peak hours.
*   **Staff Client/Web Interface**: Internal. Direction: To system. Interaction: Report design and execution UI. Input: User selections and filters. Output: Rendered reports and status queues. SLA: Must be accessible via specified browsers (IE6+, Firefox 2+) and screen readers.
*   **Email Server**: External. Direction: From system. Interaction: Report distribution. Input: Report file and recipient list. Output: Email with attachment. SLA: Configurable scheduling for recurring reports.
*   **Vendor APIs/Data Feeds** (e.g., for auditing): External. Direction: From system. Interaction: Automated file transfer. Input: Standard format reports (MARC21, EDIFACT). Output: Data files. SLA: Adherence to published vendor API specifications.

## Acceptance Criteria
*   **Capability: Secure, Templated Reporting**
    *   Given an administrator with template creation rights, when they create a report template and assign it to a staff role, then staff in that role can run the report but cannot alter the locked filter criteria.
    *   Given a staff member without ad-hoc query permissions, when they attempt to access the open query tool, then they are denied access.
*   **Capability: Collection Analysis**
    *   Given a library manager, when they request a shelf space report for their branch, then the system provides a comparison of circulation percentage, collection percentage, and shelf space percentage per material genre/format.
    *   Given a cataloger, when they run the "last copy" report for their system, then they receive a list of items that are the last copy in PINES to facilitate WorldCat updates.
*   **Capability: Financial Auditing**
    *   Given an auditor, when they request a payment ledger for a date range, then the system provides a report showing each payment and which specific charges it was applied to, compliant with standard accounting practice.

## Non-functional Metrics
*   **Performance**: 1) Complex reports shall be queued and processed asynchronously to avoid UI blocking. 2) System must support concurrent report generation for 286 locations.
*   **Reliability**: 1) Report definitions and historical data snapshots must be recoverable. 2) Scheduled reports must have a configurable retry mechanism on failure.
*   **Security**: 1) Fine-grained permissions must control access to tables, fields, and report folders. 2) Demographic reports must use anonymized data to protect patron privacy as per state law.
*   **Compliance**: 1) All financial reporting must meet state, county, and municipal auditing requirements. 2) Output must include accessibility-compliant HTML.
*   **Observability**: 1) Users must be able to see their report's position in the processing queue. 2) System must provide high-level error reporting to users and low-level diagnostic feedback to administrators.

## Milestones and Release Strategy
1.  Finalize and approve this SRS with stakeholders.
2.  Develop prototype for core reporting interface (canned & on-demand reports).
3.  Implement foundational reporting engine with queue management and basic templates.
4.  Develop and test open template reporting tool with full attribute selection.
5.  Implement inventory control utilities (batch transfer, purging reports).
6.  Deploy full Management Processes module to PINES production environment, preceded by training and pilot testing.

## Risk List and Mitigation Strategies
1.  **Risk**: Performance degradation of core ILS during report execution.
    *   **Mitigation**: Implement robust job queuing, prioritize reports, and use a separate reporting data warehouse for historical queries.
2.  **Risk**: Overly complex permission model becomes difficult to administer.
    *   **Mitigation**: Use role-based groups, provide clear admin UI, and develop comprehensive documentation.
3.  **Risk**: Inability to generate specific legacy reports critical for state compliance.
    *   **Mitigation**: Conduct a detailed gap analysis using Appendices A & B early in development to ensure all required reports are covered.
4.  **Risk**: Data privacy breach via detailed reports.
    *   **Mitigation**: Enforce anonymization in demographic reports, audit permission assignments, and implement data access logs.
5.  **Risk**: Scope creep from extensive "wish list" of reports.
    *   **Mitigation**: Strictly prioritize requirements (all listed as Priority 1), and define a clear MVP for initial release.
6.  **Risk**: High dependency on completion of Acquisitions/Cataloging module specs.
    *   **Mitigation**: Coordinate closely with parallel specification teams and define clear integration APIs.
7.  **Risk**: User resistance to new interface.
    *   **Mitigation**: Employ iterative, user-centered design with prototypes reviewed by the Reports Working Group.
8.  **Risk**: Inadequate historical reporting capability.
    *   **Mitigation**: Design the data archiving strategy (PINES-006) and reporting warehouse (Appendix B) as a foundational component.

## Undecided Issues and Responsible Parties
1.  **Precise technical architecture for the historical data warehouse/reporting snapshot.** (Responsible: Development Team & Global System Administrators)
2.  **Detailed prioritization within the large list of Priority 1 requirements for phased development.** (Responsible: Project Manager & PINES Reports Working Group)
3.  **Specific schedule and retention policy for anonymized transaction archives (PINES-006, PINES-025).** (Responsible: PINES Leadership & Legal/Compliance)
4.  **Final set of pre-defined "canned report" templates to be delivered with the system.** (Responsible: PINES Reports Working Group)
5.  **Exact definition of "real-time" vs. "historical" reporting thresholds and performance expectations.** (Responsible: Development Team & Global System Administrators)
6.  **Integration API specification with pending Acquisitions and Cataloging modules.** (Responsible: Cross-module Architecture Team)
7.  **Training strategy and resource development for library staff.** (Responsible: PINES Staff Facilitators & Training Team)
8.  **Ownership and process for maintaining/adding report templates post-launch.** (Responsible: PINES Reports Working Group & Global System Administrators)