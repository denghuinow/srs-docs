# Balanced Summary: Management Processes for an Integrated Library System

## Goals and Scope
This specification defines the requirements for the Management Processes module of an Integrated Library System (ILS) for the Georgia PINES consortium. The module aims to replace and enhance the current Evergreen ILS reporting capabilities to support library management activities such as collection analysis, demographic studies, staff productivity tracking, and financial transaction verification. It presupposes the general data structures of a full ILS and focuses on functional characteristics for management, with data structures and interfaces to be refined through iterative development.

## Stakeholders and User Stories
*   **Patron**: A Georgia resident who uses PINES member library resources, either with or without a library card.
*   **Staff**: Paid employees of PINES libraries involved in designing and providing library services.
*   **Local System Administrator**: Management staff who oversee library processes at a system level.
*   **Library Manager**: Supervisors of single organizational units who provide input on library service design.
*   **Library Director**: Members of the executive team who plan and direct library services and priorities.
*   **Global System Administrator**: Consortium-level managers who implement software changes and generate statistical reports for PINES.

**User Stories:**
1.  As a **Staff** member, I want to use a user-friendly query tool to design reports against all record types so that I can analyze library data without deep technical knowledge.
2.  As a **Local System Administrator**, I want to create reliable report templates with controlled filters for staff use so that reports are dependable and consistent across the system.
3.  As a **Library Director**, I want pre-defined board reports with basic statistics and activity metrics so that I can inform library boards and meet state reporting requirements.
4.  As a **Global System Administrator**, I want fine-grained permissions to control who can create, clone, and run reports on specific data sets so that data access is secure and manageable.
5.  As a **Library Manager**, I want reports on material volume, shelf space, and collection capacity per branch so that I can optimize collection distribution and manage inventory.
6.  As a **Staff** member, I want to see my report's position in a processing queue and receive output in formats like Excel or CSV so that I can manage my workflow and use the data effectively.

## Key Processes
1.  **User Authentication & Authorization**: Staff log in (potentially via streamlined methods like card swipe) and the system enforces role-based permissions for report access and creation. *(Trigger: Staff attempts to access the Management Processes module.)*
2.  **Report Design & Template Management**: Administrators create and manage shared report templates; authorized users can run, modify, or create ad-hoc queries using a graphical interface. *(Trigger: User initiates report creation or template configuration.)*
3.  **Data Query Execution**: The system processes user-defined or templated queries against ILS data (patrons, items, transactions, finances) to generate result sets. *(Trigger: User submits a query or schedules a report.)*
4.  **Report Generation & Output**: Query results are formatted into reports (e.g., for boards, inventory, finances) and can be exported in multiple formats (HTML, CSV, Excel). *(Trigger: Query execution completes successfully.)*
5.  **Report Distribution & Scheduling**: Reports can be run on-demand, scheduled (hourly, daily, monthly), and emailed to designated recipients. *(Trigger: Scheduled time arrives or user requests immediate distribution.)*
6.  **Data Maintenance & Archiving**: The system archives transaction data in an anonymized form for demographic statistics and purges item/patron records based on configurable criteria. *(Trigger: Scheduled archival job or administrator runs a cleanup utility.)*
7.  **Financial Reconciliation**: The system maintains a detailed audit trail of patron payments and applied charges to facilitate financial auditing and reporting. *(Trigger: Financial transaction occurs or reconciliation report is requested.)*

## Domain Data Elements
*   **Patron Record**: (Primary Key: Patron ID). Key fields: Home Library, County of Residence, Zip Code, Patron Type, Age Range.
*   **Item Record**: (Primary Key: Item Barcode/ID). Key fields: Shelving Location, Circulation Modifier, Status (e.g., Checked Out, Missing), Price/Value, Last Circulation Date.
*   **Bibliographic (Bib) Record**: (Primary Key: Title Control Number). Key fields: MARC Fields, Subject Headings, Call Number, Format/Genre.
*   **Transaction Record**: (Primary Key: Transaction ID). Key fields: Transaction Type (Check-out, Check-in, Renewal), Date/Time, Terminal ID, Staff ID, Associated Patron & Item IDs.
*   **Financial Record**: (Primary Key: Transaction ID). Key fields: Charge Type (Fine, Lost Item), Amount, Payment Method, Payment Date, Waiver Reason.
*   **Hold/Request Record**: (Primary Key: Hold ID). Key fields: Patron ID, Item/Bib ID, Pickup Library, Status (Active, Frozen), Placement Method (OPAC, Staff).

## Non-Functional Requirements
1.  **Performance & Scalability**: Must support a large consortium (286 locations, 17M annual circulations) without disrupting other system functions during open hours.
2.  **Accessibility**: Must be accessible via web browsers (IE 6.0+, Firefox 2.0+) and compatible with screen-reading and magnification software.
3.  **Security & Compliance**: Must protect patron privacy as defined by State Law in archived data and comply with standard accounting and government auditing requirements.
4.  **Reliability & Data Integrity**: Must use a fully relational database backend and produce standards-compliant HTML output.
5.  **Maintainability**: Must provide a separate development/training environment with the ability to migrate configurations to production.
6.  **Usability**: Must provide an online, hierarchical, cross-linked help system in HTML describing all functions.

## Milestones and External Dependencies
1.  Completion of requirements specification and approval by the PINES Reports Working Group.
2.  Development of prototypes for user interface and iterative review with end-users.
3.  Integration with the core Evergreen ILS data structures and functionality.
4.  Dependency on the development of Acquisitions and Cataloging modules for complete ILS functionality.
5.  Dependency on interfaces with vendor websites via APIs or standard data file transfers (e.g., MARC21, EDIFACT).

## Risks and Mitigation Strategies
1.  **Risk**: Performance degradation when running complex reports during peak operational hours.
    *   **Mitigation**: Implement report queuing with prioritization and the ability to schedule resource-intensive reports for off-peak times.
2.  **Risk**: Inability to meet the diverse reporting needs of 275+ libraries with a single interface.
    *   **Mitigation**: Use an iterative, prototype-oriented development process with ongoing feedback from the PINES Reports Working Group and library staff.
3.  **Risk**: Compromising patron privacy in archived demographic data.
    *   **Mitigation**: Architect data archiving processes to anonymize records strictly, removing all personally identifiable information as defined by law.
4.  **Risk**: Complexity in administering fine-grained permissions for numerous staff roles across many libraries.
    *   **Mitigation**: Design a role-based security model that is easy for Global System Administrators to manage through groups and templates.
5.  **Risk**: Reports failing to meet state, county, and municipal auditing standards for financial data.
    *   **Mitigation**: Involve financial officers from member libraries in designing and validating financial report requirements and audit trails.

## Undecided Issues
1.  The specific implementation details for the "open template reporting" interface and its full set of queryable attributes.
2.  The exact configurable time period (X days) for archiving detailed transaction history while maintaining aggregate data indefinitely.
3.  The final list and format of all "canned reports" to be delivered with the system.
4.  The precise mechanisms and criteria for the item transfer utility's automatic reversion of items to their original location.
5.  The method for achieving "real-time reporting" versus "historical reporting" from a data warehouse and the associated technical architecture.
6.  How to optimally display MARC record fields (like multiple subject headings) on a single row in report output without data duplication.