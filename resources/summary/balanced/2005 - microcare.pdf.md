# Balanced Summary: Voucher Management System (VMUS)

## Goals and Scope
The Voucher Management System (VMUS) is designed to automate the operations of the Voucher Management Unit (VMU) for an Output-based Aid (OBA) program providing subsidized STD treatment in Mbarara District, Uganda. Its primary goals are to manage the lifecycle of vouchers—from creation and distribution to claim processing and provider reimbursement—while minimizing fraud and manual errors. The system aims to support the pilot program for one year with scalability for future expansion, ensuring timely payments to service providers and generating necessary medical and financial reports.

## Stakeholders and User Stories
*   **MSIU Admin Team:** Manages the overall program, defines payment terms, and reviews reports for decision-making.
*   **VMU Field Office Staff:** Processes voucher claims submitted by service providers, validates data, and handles reimbursements.
*   **Voucher Service Provider (VSP):** Delivers treatment to clients, submits claim forms for reimbursement, and maintains patient records.
*   **Distributor:** Sells vouchers to clients in the community and reports sales data back to the VMU.
*   **Client/Patient:** Purchases and uses vouchers to receive STD treatment from approved providers.
*   **System Administrator:** Manages user access, security settings, and system configuration.

**User Stories:**
1.  As a **VMU Field Office Staff**, I want to **scan voucher barcodes during claim entry** so that **data is captured accurately and quickly**.
2.  As a **Voucher Service Provider (VSP)**, I want to **submit claim forms monthly** so that **I can receive timely reimbursement for services rendered**.
3.  As an **MSIU Admin Team member**, I want to **generate provider comparison reports** so that **I can monitor treatment quality and program performance**.
4.  As a **Distributor**, I want to **return unsold vouchers to the VMU** so that **my inventory is accurately reconciled**.
5.  As a **System Administrator**, I want to **define granular user permissions by screen and function** so that **system access is controlled based on roles**.
6.  As a **Client**, I want to **use a voucher at any approved provider** so that **I can access convenient and subsidized STD treatment**.

## Key Processes
1.  **Voucher Creation (Trigger: Program need)** – Authorized users generate unique, barcoded voucher batches with security codes and validity dates.
2.  **Voucher Distribution/Sales (Trigger: Distributor request)** – The VMU sales team allocates voucher batches to distributors, recording sales transactions.
3.  **Claim Submission (Trigger: Monthly/Bi-monthly payment cycle)** – VSPs submit completed treatment forms with attached voucher slips to the field office.
4.  **Claim Entry & Validation (Trigger: Receipt of claim forms)** – Field office staff enter claim data, validating voucher numbers, thumbprints, and mandatory clinical information.
5.  **Claim Quarantine/Rejection (Trigger: Missing/fraudulent data)** – Claims with errors are quarantined and sent back to the VSP for correction.
6.  **Payment Processing (Trigger: Clean claim batch approval)** – The system calculates reimbursements based on agreed fees and generates payment reports.
7.  **Client Feedback Entry (Trigger: Collection of feedback forms)** – MSIU staff enter client satisfaction data, which is linked to treatment records via voucher number.

## Domain Data Elements
*   **Voucher** (Primary Key: Voucher Number)
    *   Project Code, Batch Number, Validity Date, Security Code, Status
*   **Distributor** (Primary Key: Distributor Code)
    *   Name, Business Type, Address, Contact Number, Status
*   **Voucher Service Provider (VSP)** (Primary Key: VSP Code)
    *   Provider Name, Facility Address, Level/Type of Facility, Payment Terms, Status
*   **Claim** (Primary Key: Claim Number)
    *   Voucher Number, VSP Code, Visit Count, Patient Details, Diagnosis, Claim Amount, Status
*   **Client Feedback** (Primary Key: Feedback ID - inferred)
    *   Voucher Number, Treatment Satisfaction, Counseling Satisfaction, Privacy Satisfaction
*   **User** (Primary Key: User Name)
    *   User Group, Password, Associated Permissions (New, Edit, Delete, View, Print)

## Non-Functional Requirements
1.  **Security:** Implement granular, role-based access controls and intrusion detection mechanisms.
2.  **Usability:** Design a user-friendly interface with dropdown menus to minimize keyboard entry and training time for users with basic computer skills.
3.  **Reliability:** Include validation checks (e.g., duplicate entries, thumbprint matching) to prevent and detect fraudulent claims.
4.  **Performance:** Ensure efficient database design with surrogate keys to manage data for 20,000+ vouchers and allow for future expansion.
5.  **Interoperability:** Interface with external hardware including barcode readers and thumbprint (biometric) scanners.
6.  **Maintainability:** Use a modular design (Oracle 9i backend, VB frontend, Crystal Reports) for easier development, testing, and updates.

## Milestones and External Dependencies
1.  Finalization of master data (e.g., drug lists, syndrome codes, geographic locations).
2.  Procurement and integration of barcode printers/readers and biometric thumbprint scanners.
3.  Agreement on standardized treatment algorithms and claim form design with medical stakeholders.
4.  Definition of payment terms (fees for consultation, lab tests, drugs) with all VSPs.
5.  Training program for VMU field staff, VSPs, and distributors on system use.

## Risks and Mitigation Strategies
1.  **Risk:** Fraudulent claims through voucher duplication or impersonation.
    *   **Mitigation:** Implement unique barcodes, thumbprint verification, and system flags for suspicious activity (e.g., automatic VSP deactivation after multiple fraud alerts).
2.  **Risk:** Data entry errors leading to incorrect payments or reports.
    *   **Mitigation:** Design forms with extensive dropdown selections from master tables, automate calculations, and implement mandatory field validation.
3.  **Risk:** System downtime disrupting claim processing and provider payments.
    *   **Mitigation:** Employ robust database management practices (e.g., defragmentation) and ensure the system is easily trainable for backup operators.
4.  **Risk:** Low adoption or incorrect use by VSPs and distributors.
    *   **Mitigation:** Provide simple step-by-step manuals and design an intuitive interface to minimize training overhead.
5.  **Risk:** Scope creep or changing requirements during the pilot year.
    *   **Mitigation:** Design the database and system architecture to be scalable and adaptable for future needs beyond the pilot.

## Undecided Issues
1.  The final format of voucher slips (e.g., whether they will be stickers).
2.  The minimum quantity of vouchers that can be created in one batch.
3.  Specific algorithms and thresholds for the system's automatic fraud detection and VSP deactivation.
4.  The exact structure and fields for the HIV details capture form.
5.  The full set of customized analytical reports required beyond the standard ones listed.
6.  Procedures for handling "quarantined" claims if the VSP does not return them with corrections.