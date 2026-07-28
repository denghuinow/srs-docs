# Detailed Summary: Voucher Management System (VMUS)

## Background and Scope
The Voucher Management System (VMUS) is designed to automate the operations of the Voucher Management Unit (VMU) for Marie Stopes International Uganda (MSIU). Its primary purpose is to manage an Output-Based Aid (OBA) program that provides subsidized STD treatment vouchers to the sexually active population in Mbarara District. The system will track the entire voucher lifecycle—from creation and distribution to claim processing and provider reimbursement—while minimizing manual processes, controlling fraud, and ensuring timely payments. Non-goals include managing non-STD treatments, handling direct patient medical records beyond voucher claims, and operating outside the defined pilot geographical scope.

## Stakeholders Matrix and Use Cases
*   **MSIU Admin Team**: Oversees the entire OBA program, defines policies, approves payments, and reviews reports.
*   **VMU Staff (Field Office)**: Operates the system daily, processes voucher distributions, enters and validates claims, and handles client feedback.
*   **Distributor**: Purchases vouchers from MSIU for retail sale to end clients and may return unsold vouchers.
*   **Salesman/MSIU Sales Team**: Acts as the intermediary between MSIU and distributors, responsible for sales transactions.
*   **Voucher Service Provider (VSP)**: Approved healthcare provider (clinic/hospital) that treats patients using vouchers, submits claim forms for reimbursement.
*   **Client/Patient**: Purchases and uses the voucher for personal STD treatment or for a partner's treatment.
*   **System Administrator**: Manages system security, user privileges, and foundational master data.

**Main Scenarios**: 1) Authorized user creates a batch of unique, barcoded vouchers. 2) Salesman sells a batch of vouchers to a registered distributor, recording the transaction. 3) Client uses a voucher at a VSP for treatment; VSP submits a claim form. 4) Field office staff validates and enters a clean claim into the system for payment processing. 5) System generates financial and medical reports for the admin team to authorize payments.
**Exception Scenarios**: 1) A claim form is missing mandatory data, leading to its rejection and quarantine. 2) A distributor attempts to return vouchers that were not originally sold to them, which the system blocks. 3) Thumbprint verification fails for a voucher, triggering a fraud alert and potential VSP deactivation.

## Business Process
**Main Process: Voucher Lifecycle & Claim Payment**
1.  **Trigger/Input**: Program initiation. **Output**: Batch of unique, barcoded vouchers created in the system.
2.  MSIU salesman distributes vouchers to registered distributors, recording sales details.
3.  Client purchases voucher from distributor and seeks treatment at an approved VSP.
4.  VSP treats patient, completes claim form with voucher slip and thumbprint, and submits forms to VMU field office monthly/bi-monthly.
5.  Field office validates claim forms; clean claims are entered into the system, while incomplete/fraudulent ones are quarantined.
6.  System calculates reimbursement amount based on VSP agreement and treatment matrix.
7.  System generates payment and medical reports for the MSIU admin team.
8.  **Output**: Admin authorizes bank transfer to VSP; payment is completed.

**Key Branch A: Claim Rejection & Quarantine**
1.  **Trigger**: Claim form missing data or showing fraud indicators.
2.  Field office marks claim as "Rejected" in the system.
3.  Claim is moved to a quarantine area; form is returned to VSP for correction.
4.  If VSP resubmits satisfactory details, the claim can be processed in the next cycle.

**Key Branch B: Voucher Return**
1.  **Trigger**: Distributor returns unsold vouchers.
2.  Field office records return transaction, verifying vouchers were originally sold to that distributor.
3.  System updates inventory and calculates refund amount.
4.  **Output**: Return processed, voucher stock updated.

## Domain Model
Core entities and their key fields/constraints:
1.  **Voucher**: VoucherNumber (unique, required), BatchNumber, ProjectCode, ValidityDate, Status.
2.  **Distributor**: DistributorCode (unique, required), Name, BusinessType (required), Address (required), Status.
3.  **Salesman**: SalesmanCode (unique, required), Name (required), SalesTeam.
4.  **Voucher Service Provider (VSP)**: VSPCode (unique, required), Name (required), Address (required), PaymentTerms (reference), Status.
5.  **Claim**: ClaimNumber (unique, required), VoucherNumber (required, reference), VSPCode (required, reference), PatientDetails, VisitCount, ClaimAmount, ClaimStatus (required).
6.  **Client Feedback**: FeedbackID, VoucherNumber (required, reference), SatisfactionRatings.
7.  **User**: UserID (unique, required), UserGroup (required, reference), Password.
8.  **Master Data Tables**: e.g., Drug (DrugCode, RetailPrice), Syndrome, Diagnosis, GeographicLocation.

## Interfaces and Integrations
1.  **Barcode Scanner**: Direction: Input to VMUS. Interaction: Scanning voucher numbers and claim form data. Input: Barcode data. Output: Populates voucher/claim fields. SLA: Real-time validation required.
2.  **Biometric (Thumbprint) Reader**: Direction: Input to VMUS. Interaction: Capturing and verifying patient thumbprints on claim forms. Input: Thumbprint image/data. Output: Verification result, fraud alert. SLA: High accuracy for fraud detection.
3.  **Reporting Engine (Crystal Reports)**: Direction: Output from VMUS. Interaction: Generating standard and customized financial/medical reports. Input: System data. Output: Formatted reports. SLA: Batch processing, on-demand generation.
4.  **Database (Oracle 9i)**: Direction: Bidirectional. Interaction: All data persistence and retrieval. Input/Output: All application data. SLA: High availability, referential integrity, efficient storage.

## Acceptance Criteria
**Capability: Process a Clean Claim**
*   Given a submitted claim form with all mandatory data and a valid voucher,
    When the field office staff enters the claim into the system,
    Then the claim is accepted, its status is set to "Accepted," and the reimbursement amount is calculated based on the VSP's payment terms and treatment matrix.
**Capability: Detect and Handle Fraud**
*   Given a claim form where the patient's thumbprint does not match the one from a previous visit for the same voucher,
    When the claim is entered,
    Then the system increments a fraud counter for the VSP and, if the counter exceeds two, automatically inactivates the VSP and alerts the user.

## Non-functional Metrics
*   **Performance**: System must support the initial batch of 20,000 vouchers with provision for scaling. Claim entry transactions must be efficient with minimal keyboard use (extensive dropdowns).
*   **Reliability**: Database must be designed for storage efficiency and periodic defragmentation. High intrusion controls and access-level security are required.
*   **Security**: Granular, role-based user access controls for all modules and screens. Secure handling of user credentials and sensitive health data.
*   **Compliance**: Must adhere to the treatment algorithms (TA-OBA) and reporting requirements defined in the Programme Design Study (PDS).
*   **Observability**: System must generate all required standard reports (medical, financial, statistical) and allow for future custom report design.

## Milestones and Release Strategy
1.  Finalize and approve Software Requirements Specification (SRS).
2.  Complete database design and core module development (Voucher Creation, VSP/Distributor Masters).
3.  Develop and integrate Claim Entry/Processing module with validation logic.
4.  Implement reporting module based on PDS requirements.
5.  System integration testing with barcode and biometric interfaces.
6.  User Acceptance Testing (UAT) with MSIU staff, followed by pilot deployment.

## Risk List and Mitigation Strategies
1.  **Risk**: Fraudulent claims through voucher misuse or duplicate claims.
    **Mitigation**: Implement thumbprint verification, unique voucher tracking, and automatic VSP deactivation upon multiple fraud flags.
2.  **Risk**: System complexity leading to user errors during claim entry.
    **Mitigation**: Design user-friendly interfaces with dropdowns from master data, minimize manual typing, and provide clear validation messages.
3.  **Risk**: Inaccurate or outdated master data (e.g., drug prices, VSP details) affecting claim calculations.
    **Mitigation**: Implement strict change controls for master data, with audit trails and validity period management for critical fields like payment terms.
4.  **Risk**: Poor performance or scalability as voucher volume grows beyond the pilot.
    **Mitigation**: Use efficient database design with surrogate keys and plan for periodic maintenance (defragmentation). Design with modularity for future upgrades.
5.  **Risk**: Integration failures with barcode or biometric hardware.
    **Mitigation**: Early prototyping of hardware interfaces, selection of reliable hardware vendors, and clear error handling in the software.
6.  **Risk**: Insufficient reporting for program management decisions.
    **Mitigation**: Ensure all reports mandated in the PDS are prioritized in development and include flexibility for future customized reports.

## Undecided Issues and Responsible Parties
1.  **Defining the exact "minimum quantity" of vouchers that can be created in one batch.** (Responsible: MSIU Admin Team)
2.  **Finalizing the specific format and data points for the HIV details capture mentioned in claim entry.** (Responsible: MSIU Medical Advisor / System Design Team)
3.  **Establishing the precise schedule and process for database defragmentation and performance maintenance.** (Responsible: Microcare Development Team / MSIU IT)
4.  **Determining the full list of "other measures" beyond drugs and lab tests to be included in the treatment matrix and masters.** (Responsible: MSIU Medical Advisor)
5.  **Clarifying the reconciliation process between "Mentioned Forms" and "Available Forms" during claim submission by VSPs.** (Responsible: VMU Field Office Manager)
6.  **Defining the escalation and reactivation process for a VSP that has been automatically inactivated due to fraud flags.** (Responsible: MSIU Admin Team).