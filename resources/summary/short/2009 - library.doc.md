# Short Summary: Management Processes for Integrated Library System

## Background and Objectives
This specification defines requirements for management reporting and analytics modules within the Evergreen Integrated Library System (ILS) used by Georgia's PINES consortium. The objective is to enhance the existing system's capabilities to support data-driven management of library services, collections, and patron demographics across a large, multi-branch consortium.

## In Scope
*   Development of a user-friendly query and reporting interface with configurable templates and permissions.
*   Generation of management reports for inventory control, financial records, transaction analysis, and patron demographics.
*   Implementation of data archiving for transactions that protects patron privacy while enabling statistical analysis.
*   Support for predefined "canned" reports, on-demand reports, and open-template ad-hoc reporting.
*   Provision of utilities for batch item transfers and identification of records for purging.

## Out of Scope
*   Detailed specification of data structures or user interface design, which will follow an iterative development process.
*   Functionality or features of the Online Public Access Catalog (OPAC) module.
*   Requirements for Acquisitions and Cataloging modules, which are being specified separately.
*   Prescriptive definition of software development processes based on provided flowcharts.
*   Alteration of the core enterprise-level ILS data structures and functionality upon which these management processes depend.

## Stakeholders and Core Use Cases
*   **Patron**: A Georgia resident who uses PINES library resources, either with or without a library card.
*   **Staff**: Paid employees of member libraries involved in designing and providing library services.
*   **Local System Administrator**: Management staff who oversee library processes at a system level.
*   **Library Manager**: Supervisor of a single organizational unit who provides input on service design.
*   **Library Director**: Member of the executive team who plans and directs library services and priorities.
*   **Global System Administrator**: Consortium-level manager who implements software changes and generates statistical reports for PINES.

**Core User Stories:**
1.  As a **Library Manager**, I want to analyze collection use and shelf space by genre so that I can optimize collection distribution.
2.  As a **Staff** member, I want to run pre-defined report templates for weeding or holds so that I can perform routine tasks efficiently.
3.  As a **Local System Administrator**, I want fine-grained control over which reports and data fields staff can access so that I can ensure data integrity and appropriate use.
4.  As a **Library Director**, I want pre-defined board reports with key statistics like circulation and holds so that I can inform strategic planning.
5.  As a **Global System Administrator**, I want to archive transaction data in an anonymized form so that I can produce demographic statistics while protecting patron privacy.
6.  As a **Staff** member, I want a utility to transfer batches of items between branches so that I can manage collections for outreach programs or mobile libraries.

## Success Metrics
*   Management Processes can generate required reports during open hours without disrupting other system functions for the 286-location consortium.
*   The reporting interface is accessible and usable by defined staff user classes through standard web browsers and assistive software.
*   Generated financial reports and data archiving comply with standard accounting practices and state auditing requirements.

## Major Constraints
*   The system must operate on a Linux or Solaris server and be accessible via web browser or Windows-compatible client.
*   It must use a fully relational database back-end and produce standards-compliant HTML.
*   User rights and privileges must be controllable through security groups or roles.
*   A development and training environment must be provided with the ability to migrate configurations to production.
*   The system must interface with vendor websites via APIs and standard data formats (e.g., MARC21, EDIFACT).

## Undecided Issues
*   Specific implementation details for the user-friendly query tool interface and report template designer.
*   The exact configurable duration (X days) for maintaining detailed transaction history before archiving.
*   Final determination of all pre-defined "canned" reports to be delivered with the system.
*   The specific method and criteria for the item transfer utility to revert items to their original location.
*   Detailed mechanisms for prioritizing reports in the processing queue.