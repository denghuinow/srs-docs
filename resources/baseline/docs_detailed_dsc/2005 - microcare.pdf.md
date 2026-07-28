# Software Requirements Specification (SRS)
## Voucher Management System (VMUS)
### For Marie Stopes International Uganda (MSIU)

**Document Version:** 1.0  
**Date:** [Date of Creation]  
**Authors:** [System Analyst/Development Team]  
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Voucher Management System (VMUS). The intended audience includes MSIU stakeholders, project managers, system architects, developers, testers, and the implementation team. This document serves as the foundation for system design, development, testing, and user acceptance.

### 1.2 Project Scope
The VMUS is an automation solution for the Voucher Management Unit (VMU) of Marie Stopes International Uganda. Its core purpose is to manage the complete lifecycle of subsidized STD treatment vouchers under an Output-Based Aid (OBA) program targeting the sexually active population in Mbarara District.

**In-Scope:**
*   Management of the voucher lifecycle (creation, distribution, sale, use, claim, reimbursement).
*   Tracking of distributors, sales agents, and Voucher Service Providers (VSPs).
*   Processing and validation of claims with integrated fraud detection (thumbprint verification).
*   Financial calculation for provider reimbursements based on agreed terms.
*   Generation of standard medical, financial, and statistical reports as per the Programme Design Study (PDS).
*   Management of user access and system security.

**Out-of-Scope (Non-Goals):**
*   Management of medical treatments not covered by the STD voucher program.
*   Functioning as a comprehensive Electronic Medical Record (EMR) or Patient Management System.
*   Operations outside the pilot geographical scope (Mbarara District).
*   Direct management of bank transfer execution (initiation only).

### 1.3 Definitions, Acronyms, and Abbreviations
*   **MSIU:** Marie Stopes International Uganda
*   **VMU:** Voucher Management Unit
*   **VMUS:** Voucher Management System
*   **OBA:** Output-Based Aid
*   **VSP:** Voucher Service Provider (Approved healthcare clinic/hospital)
*   **STD:** Sexually Transmitted Disease
*   **PDS:** Programme Design Study
*   **TA-OBA:** Treatment Algorithms for Output-Based Aid
*   **SLA:** Service Level Agreement

### 1.4 References
*   Programme Design Study (PDS) Document
*   TA-OBA Treatment Algorithms
*   MSIU OBA Program Operational Manual

### 1.5 Document Overview
This SRS is structured to provide a comprehensive view of the VMUS requirements, covering stakeholder needs, system features, interface specifications, and constraints.

## 2. Overall Description

### 2.1 Product Perspective
The VMUS is a new, standalone desktop application that will interface with external hardware (barcode scanner, biometric reader) and a reporting engine. It will replace and automate existing manual and semi-automated processes within the VMU.

### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **System Administrator** | Technical expert, manages access. | User account management, role assignment, master data maintenance, system configuration. |
| **MSIU Admin Team** | Managerial, decision-making role. | Program oversight, policy definition, payment authorization, review of high-level reports. |
| **VMU Field Staff** | Primary daily operator, data entry. | Distributor/VSP registration, voucher batch/sales entry, claim validation & data entry, handling returns. |
| **Salesman/Sales Team** | Field agent, interacts with distributors. | Physically distributes vouchers, records sales transactions in the system. |
| **Distributor** | External retailer, limited system access. | Purchases vouchers from MSIU, sells to clients, may request returns (via field staff). |
| **VSP Staff** | External healthcare provider, limited access. | Submits claim details (via physical forms), may view claim status/payment history. |
| **Client/Patient** | End-beneficiary, no direct system access. | Purchases and uses voucher for treatment. |

### 2.3 Operating Environment
*   **Software:** Client application compatible with Windows OS. Oracle 9i Database. Crystal Reports runtime/integration.
*   **Hardware:** Standard PCs, barcode scanners, biometric thumbprint readers.
*   **Network:** Local Area Network (LAN) for database connectivity.

### 2.4 Design and Implementation Constraints
1.  Database must be Oracle 9i compatible.
2.  System must integrate with specified barcode and biometric hardware.
3.  User interface must be designed for efficiency, minimizing keyboard use through dropdowns and scanners.
4.  Must comply with all reporting formats and treatment algorithms specified in the PDS.

### 2.5 Assumptions and Dependencies
*   MSIU will provide accurate and timely master data (drug lists, treatment matrices, VSP agreements).
*   Hardware (scanners, readers) will be procured and available for integration testing.
*   Users will receive adequate training on system procedures.

## 3. System Features and Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Management & Security (FR-UC)
*   **FR-UC-01:** The system shall allow System Administrators to create, modify, and deactivate user accounts.
*   **FR-UC-02:** The system shall implement role-based access control (RBAC), granting permissions based on user groups (Admin, Field Staff, Sales, etc.).
*   **FR-UC-03:** Users shall be required to authenticate with a unique UserID and password.

#### 3.1.2 Master Data Management (FR-MD)
*   **FR-MD-01:** The system shall maintain master tables for Drugs (Code, Name, Retail Price), Syndromes, Diagnoses, and Geographic Locations.
*   **FR-MD-02:** Authorized users shall be able to add, edit (with audit trail), and deactivate records in master tables.
*   **FR-MD-03:** The system shall maintain a treatment matrix linking diagnoses to approved drugs, lab tests, and other measures, used for claim calculation.

#### 3.1.3 Voucher Lifecycle Management (FR-VL)
*   **FR-VL-01:** The system shall allow authorized users to create batches of unique, barcoded vouchers. Each voucher shall have a unique Voucher Number, Batch ID, Project Code, Validity Date, and initial status (e.g., 'Created').
*   **FR-VL-02:** The system shall record the sale of voucher batches from MSIU (via a Salesman) to a registered Distributor, linking vouchers to the distributor.
*   **FR-VL-03:** The system shall allow Field Staff to process the return of unsold vouchers from a Distributor, subject to validation that the vouchers were originally sold to that distributor.
*   **FR-VL-04:** Voucher status shall automatically update through its lifecycle: Created -> In Stock -> Sold -> Redeemed -> Claimed -> Paid.

#### 3.1.4 Partner Management (FR-PM)
*   **FR-PM-01:** The system shall maintain a registry of Distributors (Code, Name, Business Type, Address, Status).
*   **FR-PM-02:** The system shall maintain a registry of Voucher Service Providers (VSPs) (Code, Name, Address, Payment Terms, Status).
*   **FR-PM-03:** The system shall track a fraud counter for each VSP.

#### 3.1.5 Claim Processing (FR-CP)
*   **FR-CP-01:** The system shall provide an interface for Field Staff to enter claim data from submitted claim forms, using barcode scanners for voucher number input where possible.
*   **FR-CP-02:** During claim entry, the system shall validate that the voucher is valid, unredeemed, and presented within its validity period.
*   **FR-CP-03:** The system shall integrate with a biometric reader to capture and verify patient thumbprints. It shall compare the new print against any previous print associated with the same voucher number.
*   **FR-CP-04:** If a thumbprint mismatch is detected, the system shall increment the fraud counter for the submitting VSP and display an alert to the user.
*   **FR-CP-05:** If a VSP's fraud counter exceeds two (2), the system shall automatically change the VSP's status to "Inactive" and notify the MSIU Admin Team.
*   **FR-CP-06:** The system shall calculate the reimbursement amount for an accepted claim based on the VSP's Payment Terms and the treatment matrix (drugs, tests, other measures administered).
*   **FR-CP-07:** The system shall allow claims to be marked as "Rejected" and moved to a quarantine area if mandatory data is missing or fraud is suspected. Quarantined claims can be corrected and resubmitted.

#### 3.1.6 Reporting (FR-REP)
*   **FR-REP-01:** The system shall generate standard financial reports (e.g., Payment Registers, VSP Statements).
*   **FR-REP-02:** The system shall generate standard medical/statistical reports (e.g., Disease Prevalence, Voucher Utilization).
*   **FR-REP-03:** The system shall allow authorized users to generate ad-hoc reports using a integrated reporting engine (Crystal Reports).

### 3.2 External Interface Requirements

#### 3.2.1 User Interfaces
*   Graphical User Interface (GUI) shall be intuitive, form-based, and consistent across all modules.
*   Heavy use of dropdown lists, checkboxes, and radio buttons to minimize manual data entry.
*   Clear validation messages and error notifications.

#### 3.2.2 Hardware Interfaces
*   **HI-01:** The system shall accept input from standard USB barcode scanners to populate voucher and form identification fields.
*   **HI-02:** The system shall interface with a biometric thumbprint reader to capture, store, and verify fingerprint data for fraud detection.

#### 3.2.3 Software Interfaces
*   **SI-01:** The system shall connect to an **Oracle 9i** database for all data persistence.
*   **SI-02:** The system shall integrate with **Crystal Reports** or a compatible reporting engine for report generation and formatting.

### 3.3 System Attributes (Non-Functional Requirements)

#### 3.3.1 Performance
*   The system shall be designed to efficiently handle an initial volume of 20,000 vouchers with linear scalability for future increases.
*   Claim entry transactions shall be optimized for speed, with a target of under 3 seconds for saving a validated claim.

#### 3.3.2 Reliability & Availability
*   The database shall be designed for storage efficiency, supporting periodic maintenance tasks like defragmentation without significant downtime.
*   Core system functions shall be available during standard business hours (99% uptime).

#### 3.3.3 Security
*   The system shall enforce granular, role-based access controls on all screens and functions.
*   User passwords shall be stored using industry-standard encryption.
*   All access to the system shall be logged for audit purposes.
*   Sensitive health data (e.g., patient details linked to vouchers) shall be protected from unauthorized access.

#### 3.3.4 Compliance
*   The system's claim calculation logic shall strictly adhere to the Treatment Algorithms (TA-OBA) defined by MSIU.
*   All report formats and data points shall comply with the requirements outlined in the Programme Design Study (PDS).

## 4. Detailed Domain Model & Data Requirements

### 4.1 Entity Relationship Overview
The core data model revolves around the `Voucher` entity, linked to `Distributor` (via sales), `Claim` (via use), and `VSP`. `Claim` details are governed by master data (`Drug`, `Syndrome`, etc.).

### 4.2 Key Data Entities & Attributes
| Entity | Key Attribute | Constraints | Description |
| :--- | :--- | :--- | :--- |
| **Voucher** | VoucherNumber | Primary Key, Unique, Not Null | Unique identifier for each physical voucher. |
| | BatchNumber | Not Null | Links voucher to its creation batch. |
| | Status | Not Null | Tracks lifecycle (Created, Sold, Redeemed, etc.). |
| **Distributor** | DistributorCode | PK, Unique, Not Null | Unique code for the retail outlet. |
| | Name, Address, BusinessType | Not Null | Basic business information. |
| **VSP** | VSPCode | PK, Unique, Not Null | Unique code for the healthcare provider. |
| | PaymentTerms | Foreign Key | References payment agreement for reimbursement. |
| | FraudCounter | Default 0 | Tracks thumbprint verification failures. |
| **Claim** | ClaimNumber | PK, Unique, Not Null | Auto-generated claim ID. |
| | VoucherNumber | FK, Not Null | References the voucher used. |
| | VSPCode | FK, Not Null | References the submitting provider. |
| | ClaimStatus | Not Null | (Entered, Accepted, Rejected, Quarantined, Paid). |
| | ThumbprintData | | Encrypted storage of biometric data. |

## 5. Acceptance Criteria (Examples)
Presented in Gherkin-style format for clarity.

**AC-01: Successful Claim Acceptance**
```
Feature: Process Clean Claim
  Scenario: Accept a valid claim
    Given a claim form with all mandatory fields completed
    And the voucher number is valid and has status 'Sold'
    And the patient's thumbprint is verified (or is a first-time use)
    When the VMU staff submits the claim via the data entry screen
    Then the system saves the claim with status "Accepted"
    And the calculated reimbursement amount is displayed and saved
    And the voucher status is updated to "Redeemed"
```

**AC-02: Fraud Detection and Escalation**
```
Feature: Detect Fraudulent Activity
  Scenario: VSP commits a third fraud violation
    Given a VSP with a fraud counter value of 2
    And a new claim is submitted by this VSP
    And the patient's thumbprint fails verification against the voucher's history
    When the VMU staff attempts to save the claim
    Then the system increments the VSP's fraud counter to 3
    And the system automatically changes the VSP's status to "Inactive"
    And an alert is displayed to the user and logged for the admin
    And the claim is placed in "Quarantine" status
```

## 6. Project Planning (Annex)

### 6.1 Milestones & Release Strategy
1.  **Milestone 1:** SRS Finalization & Approval.
2.  **Milestone 2:** Database Design & Core Module Completion (User Mgmt, Master Data, Voucher/Distributor/VSP CRUD).
3.  **Milestone 3:** Claim Processing Module Development & Integration (with validation and fraud logic).
4.  **Milestone 4:** Reporting Module Implementation (Standard PDS Reports).
5.  **Milestone 5:** System Integration Testing (Hardware & Software).
6.  **Milestone 6:** User Acceptance Testing & Pilot Deployment in Mbarara VMU.

### 6.2 Risk Management
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Fraudulent Claims | Medium | High | Thumbprint verification, unique voucher tracking, automatic VSP deactivation. |
| User Data Entry Errors | High | Medium | Intuitive UI with dropdowns, field validation, scanner integration, comprehensive training. |
| Poor System Performance | Medium | High | Efficient DB design, use of indexes, planning for periodic maintenance (defragmentation). |
| Hardware Integration Failure | Medium | High | Early prototype testing, select reliable vendors, implement robust error handling. |

### 6.3 Open Issues & Decisions Pending
| # | Issue Description | Responsible Party |
| :--- | :--- | :--- |
| 1. | Define minimum voucher batch creation quantity. | MSIU Admin Team |
| 2. | Finalize HIV details data points and format in claims. | MSIU Medical Advisor |
| 3. | Establish schedule for DB defragmentation/performance tuning. | Microcare Dev Team / MSIU IT |
| 4. | Determine complete list of "other measures" for treatment matrix. | MSIU Medical Advisor |
| 5. | Clarify reconciliation process for VSP claim form submissions. | VMU Field Office Manager |
| 6. | Define reactivation process for a VSP inactivated for fraud. | MSIU Admin Team |

---
*Document End*