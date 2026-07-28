**Purpose & Scope**
The system automates the voucher management for a one-year STD treatment pilot program in Mbarara District. It handles the lifecycle of vouchers from creation and distribution to claim processing and provider reimbursement. It does not provide medical treatment, manage provider clinical operations, or handle direct patient medical records.

**Product Background / Positioning**
The system is the core IT system for the Voucher Management Unit (VMU) within the Marie Stopes International Uganda (MSIU) Output-Based Aid program. It interfaces with voucher service providers (VSPs), distributors, and MSIU administrative teams to replace manual processes.

**Core Functional Overview**
1.  Generate and print unique, barcoded vouchers in batches.
2.  Manage distributor networks and record bulk sales of vouchers to distributors.
3.  Process medical claims submitted by service providers, including validation against treatment algorithms.
4.  Calculate reimbursement amounts for providers based on agreed fees and drug costs.
5.  Manage the return of unsold vouchers from distributors.
6.  Record and analyze client feedback on treatments.
7.  Generate standard financial, medical, and statistical reports for program management.
8.  Control system access through configurable user groups and permissions.

**Key Users & Usage Scenarios**
Primary users are MSIU administrative staff and field office operators. They manage distributor and provider master data, enter voucher sales and returns, and process claim forms submitted by providers. Voucher Service Providers (VSPs) are external users who submit paper claim forms for entry. Distributors are external entities that purchase vouchers for resale. User permissions vary by role, controlling access to functions like voucher creation, claim entry, and report generation.

**Major External Interfaces**
The system interfaces with a barcode reader to scan voucher numbers on claim forms. It interfaces with a thumbprint reader to capture and verify patient biometric data from claim forms. It generates data for bank transfers to reimburse providers.

**Key Non-functional Requirements**
The database must be structurally efficient to support expansion beyond the initial 20,000 vouchers. The system must include high intrusion controls and granular user access controls. It must automatically deactivate a provider's account if more than two fraud indicators (e.g., mismatched thumbprints) are detected from their claims.

**Constraints, Assumptions & Dependencies**
The system will be developed using Oracle 9i database, Visual Basic front end, and Crystal Reports 9. It assumes VSPs will follow the defined MSIU treatment algorithms and submit complete paper claim forms with attached voucher slips and thumbprints. A key dependency is the accuracy and completeness of data on manually submitted claim forms.

**Priorities & Acceptance Approach**
Core priorities are voucher lifecycle management and fraud-controlled claim processing. Acceptance will be based on the system correctly generating vouchers, validating and processing claims according to business rules, calculating accurate reimbursements, and producing the mandated standard reports.