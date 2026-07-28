# Short Summary: Voucher Management System (VMUS)

## Background and Objectives
The Voucher Management System (VMUS) is being developed for Marie Stopes International Uganda (MSIU) to automate the Voucher Management Unit (VMU) processes for a pilot Output-Based Aid (OBA) program in Mbarara District. Its primary objective is to manage the lifecycle of STD treatment vouchers—from creation and distribution to claim processing and reimbursement—while minimizing fraud, ensuring timely payments to service providers, and providing data for program monitoring and quality improvement.

## In Scope
*   Automated voucher creation with unique, barcoded identifiers and security features.
*   Management of voucher distribution and sales transactions through authorized distributors and MSIU sales teams.
*   Processing and validation of treatment claims submitted by Voucher Service Providers (VSPs), including biometric verification.
*   Generation of standard financial, medical, and operational reports as specified in the program design.
*   Implementation of a role-based security system to control user access and privileges across all modules.

## Out of Scope
*   Development of the marketing and behavioral change campaign (BCC) itself.
*   Direct patient treatment or clinical decision-making at VSP facilities.
*   Long-term program expansion beyond the initial pilot phase and district.
*   Integration with external banking systems for automatic fund transfers.
*   Real-time, online claim submission by VSPs; the system processes batch submissions.

## Stakeholders and Core Use Cases
*   **MSIU Admin Team:** Manages the VMU program, oversees providers, authorizes payments, and reviews reports.
*   **VMU Field Office Staff:** Enters distributor sales, processes and validates VSP claims, and manages daily system operations.
*   **Voucher Service Provider (VSP):** Treats patients using vouchers, documents treatment, and submits claim forms for reimbursement.
*   **Distributor:** Sells vouchers to clients, maintains sales records, and may return unsold vouchers.
*   **Client/Patient:** Purchases and uses the voucher to receive subsidized STD treatment.
*   **System Administrator:** Configures user groups, manages security permissions, and maintains system masters.

**Core User Stories:**
1.  As an **MSIU Admin Team member**, I want to generate payment reports per VSP so that I can arrange timely reimbursements.
2.  As a **VMU Field Office Staff member**, I want to enter and validate claim data from paper forms so that only clean, complete claims are processed for payment.
3.  As a **Voucher Service Provider (VSP)**, I want to be reimbursed based on submitted and validated claims so that I receive payment for services rendered.
4.  As a **Distributor**, I want to purchase batches of vouchers from MSIU so that I can resell them to clients in my area.
5.  As a **System Administrator**, I want to define user roles with granular permissions so that system access is controlled and secure.
6.  As a **Client**, I want to use a purchased voucher at an approved provider so that I can receive free, quality STD treatment.

## Success Metrics
*   Accurate and timely processing of VSP claims leading to on-schedule reimbursement.
*   Effective detection and quarantine of fraudulent or erroneous claims through system validations.
*   Generation of all required standard reports (financial, medical, operational) to support program monitoring and decision-making.

## Major Constraints
*   The system must be developed using Oracle 9i database, Visual Basic front-end, and Crystal Reports 9.
*   Voucher sales are restricted to one voucher per person at a time to minimize fraud.
*   Voucher data (once created) cannot be edited or deleted, only withheld or have its validity date amended by authorized users.
*   The system must interface with barcode readers and thumb-print (biometric) scanners for data entry and verification.
*   The database design must be efficient and scalable to potentially support expansion beyond the pilot.

## Undecided Issues
*   The final minimum quantity of vouchers that must be created in one batch.
*   Specific details and format for capturing HIV-related information in claims.
*   The complete list and design of customized analytical reports beyond the standard set.
*   The exact process and criteria for reactivating a VSP that was automatically deactivated due to fraud flags.
*   Resolution of how to handle duplicate names for distributors and sales staff in reporting.