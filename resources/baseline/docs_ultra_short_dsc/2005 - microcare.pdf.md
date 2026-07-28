# Software Requirements Specification (SRS)
## Voucher Management System (VMS)
### For the STD Treatment Pilot Program, Mbarara District

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Prepared for:** Marie Stopes International Uganda (MSIU)  
**Prepared by:** [Your Name/Organization]  
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Voucher Management System (VMS). The VMS is the core information technology system designed to automate the end-to-end management of treatment vouchers for the one-year Sexually Transmitted Disease (STD) pilot program in Mbarara District. This document is intended for use by the project stakeholders, developers, testers, and project managers to guide the development, testing, and acceptance of the system.

### 1.2 Scope
The VMS will manage the complete lifecycle of a treatment voucher, including:
*   Generation and physical printing of unique, barcoded vouchers.
*   Management of distributor networks and recording bulk sales.
*   Processing of medical claims submitted by Voucher Service Providers (VSPs).
*   Calculation of provider reimbursements.
*   Management of voucher returns from distributors.
*   Recording and analysis of client feedback.
*   Generation of standard management reports.
*   Administration of system users and access controls.

**Out of Scope:**
*   Provision of medical treatment or clinical decision support.
*   Management of provider clinical operations or electronic medical records (EMRs).
*   Direct patient interaction or patient-facing portals.
*   Direct entry of claims by VSPs (claims are submitted on paper forms).

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **VMS** | Voucher Management System |
| **MSIU** | Marie Stopes International Uganda |
| **VMU** | Voucher Management Unit |
| **VSP** | Voucher Service Provider (Medical Clinic/Hospital) |
| **STD** | Sexually Transmitted Disease |
| **OBA** | Output-Based Aid |

### 1.4 References
*   MSIU STD Pilot Program Operational Manual
*   MSIU Treatment Algorithms & Fee Schedule
*   Project Charter & Statement of Work

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and constraints. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, security, and design constraints.

## 2. Overall Description

### 2.1 Product Perspective
The VMS is a standalone, client-server application that serves as the central system for the VMU. It replaces existing manual, paper-based processes for voucher tracking, claim validation, and reimbursement. It interfaces with external hardware devices and generates output files for financial systems.

### 2.2 Product Functions (Summary)
1.  **Voucher Master Data Management:** Create, batch-generate, and print vouchers.
2.  **Partner Management:** Maintain master data for Distributors and VSPs.
3.  **Inventory & Sales Tracking:** Record bulk sales of vouchers to distributors and manage returns of unsold stock.
4.  **Claims Processing:** Validate and enter claims submitted by VSPs, including fraud checks.
5.  **Reimbursement Calculation:** Automatically compute payment amounts based on treatment provided and drugs dispensed.
6.  **Feedback Management:** Record and categorize client feedback on treatments received.
7.  **Reporting:** Generate standard financial, operational, and medical statistics reports.
8.  **System Administration:** Manage user accounts, roles, and permissions.

### 2.3 User Characteristics
| User Class | Description | Key Tasks | Skill Level |
| :--- | :--- | :--- | :--- |
| **VMU Administrator** | MSIU central office staff. | System configuration, user management, master data maintenance, generating voucher batches, processing complex returns, overseeing all reports. | High computer literacy, understands business rules thoroughly. |
| **Field Operator** | MSIU field office staff. | Daily entry of distributor sales/returns, data entry of paper claim forms from VSPs, recording client feedback, running routine reports. | Moderate computer literacy, trained on specific data entry workflows. |
| **VSP (External)** | Healthcare provider staff. | *Submit paper claim forms* with vouchers and patient thumbprints. They do **not** directly interact with the VMS software. | N/A (External to system) |
| **Distributor (External)** | Voucher sales agents. | Purchase voucher batches for resale, return unsold physical vouchers. They do **not** directly interact with the VMS software. | N/A (External to system) |

### 2.4 Constraints
*   **Technology Stack:** The system must be developed using:
    *   **Database:** Oracle 9i
    *   **Front-end Application:** Visual Basic
    *   **Reporting Tool:** Crystal Reports 9
*   **Interface:** The primary user interface will be a Windows desktop application.
*   **Data Input:** A significant portion of claim data originates from manually filled paper forms, introducing a dependency on data quality and completeness.

### 2.5 Assumptions and Dependencies
*   **Assumption:** VSPs will follow the MSIU-defined treatment algorithms and correctly fill out all required fields on the paper claim form.
*   **Assumption:** The attached voucher slip and patient thumbprint on claim forms will be legible and scannable.
*   **Dependency:** Availability and proper functioning of barcode scanners and thumbprint readers.
*   **Dependency:** The agreed-upon fee schedule and drug cost list will be provided and remain stable during the pilot period.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 Hardware Interfaces
*   **H-INT-1:** The system shall interface with a standard USB barcode scanner to read voucher numbers from claim forms.
*   **H-INT-2:** The system shall interface with a biometric thumbprint reader to capture and verify patient fingerprint data from claim forms.

#### 3.1.2 Software Interfaces
*   **S-INT-1:** The system shall connect to an **Oracle 9i** database for all data persistence.
*   **S-INT-2:** The system shall generate a structured data file (e.g., CSV) containing validated reimbursement details for approved claims, suitable for import by the MSIU financial system for bank transfers.

### 3.2 Functional Requirements

#### 3.2.1 Voucher Management (VM)
*   **VM-1:** The system shall allow an authorized user to generate a batch of unique, sequential voucher numbers.
*   **VM-2:** Each voucher shall have a unique identifier, a corresponding barcode, and a pre-printed issue date.
*   **VM-3:** The system shall print vouchers in a pre-defined, secure format on designated stock.
*   **VM-4:** The system shall track the status of each voucher (e.g., Printed, Sold to Distributor, Returned, Claimed, Reimbursed).

#### 3.2.2 Distributor & Sales Management (DSM)
*   **DSM-1:** The system shall maintain a master list of authorized distributors.
*   **DSM-2:** The system shall record the bulk sale of a specific range of voucher numbers to a specific distributor, including date, quantity, and responsible MSIU user.
*   **DSM-3:** The system shall allow for the recording of returns of unsold physical vouchers from a distributor, updating inventory status accordingly.

#### 3.2.3 Claims Processing (CP)
*   **CP-1:** The system shall allow an operator to enter data from a paper claim form submitted by a VSP.
*   **CP-2:** The system shall use the barcode scanner to populate the voucher number field, minimizing manual entry.
*   **CP-3:** The system shall validate the entered voucher number (checking if it exists, is active, and has not already been claimed).
*   **CP-4:** The system shall validate the claimed treatment and drugs against the MSIU treatment algorithms for the diagnosed STD.
*   **CP-5:** The system shall capture and store the patient's thumbprint data from the claim form via the thumbprint reader.
*   **CP-6:** The system shall compare the newly captured thumbprint against previously stored thumbprints for the same voucher number to detect potential fraud (duplicate claims).
*   **CP-7:** The system shall flag claims that fail validation (CP-3, CP-4, CP-6) for review by a supervisor.

#### 3.2.4 Reimbursement Calculation (RC)
*   **RC-1:** For a validated claim, the system shall automatically calculate the total reimbursement amount based on:
    *   A fixed service fee for the treatment.
    *   Cost of drugs dispensed as per the master drug list.
*   **RC-2:** The system shall maintain a configurable fee schedule and drug cost list.

#### 3.2.5 Reporting (REP)
*   **REP-1:** The system shall generate a standard set of reports including, but not limited to:
    *   Voucher Status Report (by status, distributor, period)
    *   Claims Processing Report (approved, rejected, pending)
    *   Financial Reimbursement Summary (by VSP, by period)
    *   Medical Statistics Report (STD type, treatment counts, demographics)
    *   Client Feedback Summary Report

#### 3.2.6 System Administration & Security (SAS)
*   **SAS-1:** The system shall require user authentication via username and password.
*   **SAS-2:** The system shall implement role-based access control (RBAC) with configurable user groups (e.g., Administrator, Operator, Supervisor).
*   **SAS-3:** Permissions shall be granular, controlling access to specific functions (e.g., Create Voucher, Enter Claim, Approve Claim, Run Financial Reports).
*   **SAS-4:** The system shall automatically log all user actions (audit trail) including logins, data modifications, and claim approvals.
*   **SAS-5:** **FRAUD-1:** The system shall automatically and permanently deactivate a VSP's account if more than two (2) fraud indicators (e.g., mismatched thumbprints, algorithm violations) are confirmed from claims submitted under their provider ID.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PER-1:** The database schema shall be designed for structural efficiency to support scaling beyond the initial pilot of 20,000 vouchers without significant performance degradation.
*   **PER-2:** Data entry and validation of a standard claim form shall be completed within 3 minutes by a trained operator under normal system load.

#### 3.3.2 Security Requirements
*   **SEC-1:** The system shall employ high intrusion controls, including password policies (length, complexity, expiration) and account lockout after repeated failed login attempts.
*   **SEC-2:** All sensitive data (e.g., financial calculations, patient biometric data hashes) shall be stored securely in the database.
*   **SEC-3:** The audit trail (SAS-4) shall be non-editable by any user.

#### 3.3.3 Design Constraints
*   **DC-1:** The application shall be developed as a desktop client using Visual Basic 6.0 (or compatible .NET framework).
*   **DC-2:** All reporting shall be implemented using Crystal Reports 9.

## 4. Acceptance Criteria
System acceptance will be contingent upon the successful demonstration of the following core workflows:
1.  Generation and printing of a secure, barcoded voucher batch.
2.  Accurate recording of voucher sales to a distributor and subsequent returns.
3.  End-to-end processing of a valid paper claim form: scanning, data entry, algorithmic validation, thumbprint check, accurate reimbursement calculation, and approval.
4.  Correct detection and flagging of an invalid claim (using a test case with a duplicate voucher or treatment violation).
5.  Automatic deactivation of a provider account upon the third confirmed fraud indicator.
6.  Generation of all standard reports with accurate data aggregation.
7.  Enforcement of role-based permissions, preventing unauthorized access to functions.