**Purpose & Scope**
The system is the Management Processes module for an Integrated Library System (ILS). It provides reporting and analysis tools for managing library collections, patrons, transactions, and finances within a large, multi-branch consortium. It does not cover the core functions of the Online Public Access Catalog (OPAC), Acquisitions, or Cataloging modules, which are separate dependencies.

**Product Background / Positioning**
This module is an enhancement to the existing Evergreen ILS used by the Georgia PINES consortium, a network of over 275 libraries. It is intended to replace and extend the current reporting capabilities to support centralized management of the statewide shared collection and its operations.

**Core Functional Overview**
*   Provide a user-friendly query tool for designing reports against all library data types.
*   Allow system administrators to create and manage secure, templated reports with controlled customization.
*   Generate pre-defined and ad-hoc reports for collection analysis (e.g., usage, capacity, weeding).
*   Generate pre-defined and ad-hoc reports for patron demographic and activity analysis.
*   Generate pre-defined and ad-hoc reports for all transaction types (check-ins, check-outs, holds).
*   Generate pre-defined and ad-hoc financial reports (fines, payments, collection value) compliant with auditing standards.
*   Provide utilities for batch inventory management, such as transferring items between branches.
*   Archive transaction data in an anonymized form for longitudinal statistical analysis.

**Key Users & Usage Scenarios**
Primary users are library staff with tiered permissions: frontline Staff run templated reports; Local System Administrators and Library Managers create and manage reports for their branches; Global System Administrators configure system-wide reports and permissions. Typical scenarios include generating daily circulation stats, monthly financial summaries, collection weeding lists, and analyzing patron demographics for service planning.

**Major External Interfaces**
The module interfaces with the core ILS database for all library records. It must interface with vendor websites via APIs or standard data file transfers (e.g., MARC, EDIFACT). It is separate from but interacts with the patron-facing OPAC. It must be accessible via web browsers (Internet Explorer 6.0+, Firefox 2.0+) or a Windows client.

**Key Non-functional Requirements**
*   Must support a consortium of 286 locations with 17 million annual circulations without disrupting other system functions during operational hours.
*   Must be accessible with screen-reading and screen-magnification software.
*   Must operate on a Linux or Solaris server.
*   Must use a fully relational database back-end and produce standards-compliant HTML.
*   Must provide a distinct development/training environment with configuration migration to production.
*   User rights and privileges must be controlled through configurable security groups or roles.

**Constraints, Assumptions & Dependencies**
The module is an integral part of an enterprise-level ILS. It is centrally hosted and serves multiple locations. It is fundamentally dependent on the data structures and functionality of the core ILS, including its Acquisitions and Cataloging modules. It assumes the user has a general understanding of library services and terminology.

**Priorities & Acceptance Approach**
All specified requirements are marked as Priority 1. Acceptance will involve the designated user group testing all new reports development. The system must demonstrably support the specific reporting examples and fine-grained requirements detailed in the appendices of the source document.