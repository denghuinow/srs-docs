# Software Requirements Specification (SRS)
## Voucher Management System (VMS) for STD Treatment Pilot Program

**Document Version:** 1.0
**Date:** 2023-10-27
**Project:** Mbarara District STD Treatment Pilot - Voucher Management System
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Voucher Management System (VMS). The VMS is designed to automate the end-to-end lifecycle management of treatment vouchers for a one-year Sexually Transmitted Disease (STD) pilot program in Mbarara District. The primary purpose is to ensure accurate tracking, validation, and financial reconciliation of vouchers from creation through distributor sales, patient/provider use, to final reimbursement of healthcare providers.

#### 1.2 Scope
The in-scope system, the Voucher Management System (VMS), will be a desktop application with a centralized database. It will manage the creation of uniquely identified, barcoded voucher pairs, track their sale and distribution, validate medical claims submitted by certified service providers, and facilitate the reimbursement process. The system will interface with external hardware (barcode scanners, thumbprint readers) and will be used by three primary user groups: System Administrators, Distributors, and Healthcare Providers.

**Out of Scope:**
*   Direct patient medical records or treatment history.
*   Inventory management of medical supplies or pharmaceuticals.
*   General financial accounting or payroll systems beyond voucher reimbursement.
*   Mobile or web-based client applications for patients.
*   Long-term archival of data beyond the pilot's operational needs.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **Voucher** | A physical, barcoded ticket entitling the bearer to a specific STD treatment service at a participating healthcare facility. |
| **Voucher Pair** | Two linked vouchers: one for the "Client" and one for the "Partner," sold together as a single unit. |
| **Distributor** | An authorized agent or outlet responsible for selling voucher pairs to the public. |
| **Provider** | A certified healthcare facility or clinic authorized to accept vouchers, provide treatment, and submit claims for reimbursement. |
| **Claim** | A formal submission by a Provider to request reimbursement for treatment services rendered using a voucher. |
| **SRS** | Software Requirements Specification. |
| **VMS** | Voucher Management System. |
| **STD** | Sexually Transmitted Disease. |

#### 1.4 References
*   Mbarara District STD Pilot Program - Project Charter
*   Data Privacy and Protection Act, [Country]

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its user classes, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements including performance, security, and design constraints.

---

### 2. Overall Description

#### 2.1 Product Perspective
The VMS is a new, standalone system. It will require interfaces to the following external components:
*   **Barcode Scanner:** For reading voucher IDs during sale, return, and claim submission.
*   **Thumbprint Reader:** For biometric verification of Distributors and potentially Providers during sensitive transactions (e.g., bulk sales, claim submission).
*   **Database Server:** A centralized SQL database (e.g., PostgreSQL, MySQL) that will serve as the system of record.

#### 2.2 Product Functions (Summary)
1.  **Voucher Lifecycle Management:** Generate, activate, track status (created, sold, used, reimbursed, voided), and archive vouchers.
2.  **Distributor Management:** Manage distributor accounts, record sales transactions of voucher pairs, and process returns.
3.  **Claim Adjudication:** Receive, validate, and approve or reject treatment claims submitted by Providers based on voucher validity and program rules.
4.  **Reimbursement Processing:** Generate reimbursement reports and payment instructions for approved claims.
5.  **Reporting & Auditing:** Provide operational, financial, and audit trail reports for program management.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **System Administrator** | Technical staff. Manages system configuration, user accounts, and overall data integrity. | Create voucher batches, manage user roles (Distributors/Providers), run reports, handle system exceptions. |
| **Distributor** | Non-technical field agent. May have limited literacy. Operates in a low-bandwidth environment. | Sell voucher pairs to clients, process returns, perform end-of-day reconciliation. |
| **Healthcare Provider** | Clinic staff (e.g., nurse, administrator). Primary goal is to submit claims accurately and get reimbursed. | Validate patient vouchers, submit treatment claims, check claim status. |

#### 2.4 Operating Environment
*   **Hardware:** Standard PCs/laptops for administrative functions; basic PCs for distributors and providers. External barcode scanners and thumbprint readers.
*   **Software:** Windows 10/11 OS. Database server (to be specified) running on a centralized server.
*   **Network:** Intermittent internet connectivity expected at distributor and provider locations. System must support offline transaction caching with synchronization.

#### 2.5 Design and Implementation Constraints
1.  **Database Scalability:** The database schema and indexing strategy must be designed to efficiently handle the initial 20,000 vouchers and scale seamlessly to support at least 200,000 vouchers without significant performance degradation or architectural change.
2.  **Voucher Pair Logic:** The core business logic must enforce that vouchers are **only sold in pairs** (Client & Partner). A single voucher cannot be sold independently.
3.  **One-Per-Person Limit:** The system must implement controls to prevent the sale of more than one voucher (i.e., one voucher pair per person) to the same individual within the pilot period. (Note: Specific identification method TBD but must be supported logically).
4.  **Hardware Interface:** The application must be capable of integrating with standard USB/HID barcode scanners and thumbprint readers via defined APIs.

#### 2.6 Assumptions and Dependencies
*   Assumes distributors and providers will have access to basic computing hardware and periodic internet connectivity.
*   Dependent on the procurement and compatibility of standard barcode and biometric hardware.
*   Program rules (treatment covered, reimbursement rates) are stable for the pilot duration.

---

### 3. System Features (Functional Requirements)

#### 3.1 Feature 1: Voucher Creation and Management
**3.1.1 Description:** The System Administrator shall be able to generate batches of unique, barcoded voucher pairs.
**3.1.2 Requirements:**
*   **FR1.1:** The system shall generate vouchers with a unique, system-assigned ID encoded in a Code 128 barcode.
*   **FR1.2:** Vouchers shall be created in linked pairs (Client Voucher and Partner Voucher), with a shared Pair ID.
*   **FR1.3:** The system shall allow the administrator to define the batch size, starting number, and print batch details to a PDF format for physical printing.
*   **FR1.4:** The system shall maintain the status of each voucher (e.g., `CREATED`, `ACTIVE`, `SOLD`, `USED`, `REIMBURSED`, `VOID`, `RETURNED`).

#### 3.2 Feature 2: Distributor Sales and Inventory
**3.2.1 Description:** Distributors shall sell voucher pairs to clients and manage their local inventory.
**3.2.2 Requirements:**
*   **FR2.1:** Distributors must authenticate (via login/password and/or thumbprint) to access the sales module.
*   **FR2.2:** The system shall only allow the sale of a complete **voucher pair** (one client, one partner). Single voucher sales shall be prohibited.
*   **FR2.3:** The sale transaction shall record: Distributor ID, Timestamp, Voucher Pair ID, and Sale Price.
*   **FR2.4:** The system shall update the status of both vouchers in the pair from `ACTIVE` to `SOLD`.
*   **FR2.5:** The system shall allow a distributor to process a return of an unsold or `SOLD` voucher pair, resetting its status appropriately, following authentication.

#### 3.3 Feature 3: Claim Submission and Validation
**3.3.1 Description:** Healthcare Providers shall submit claims for treatment provided using a voucher.
**3.3.2 Requirements:**
*   **FR3.1:** Providers shall authenticate to access the claim submission module.
*   **FR3.2:** Claim entry shall be initiated by scanning the barcode of the used voucher.
*   **FR3.3:** Upon scan, the system shall validate the voucher in real-time (status=`SOLD`, not expired, not already used).
*   **FR3.4:** For a valid voucher, the system shall present a form for the provider to enter required treatment details (e.g., date of service, diagnosis code, treatment given).
*   **FR3.5:** The provider shall submit the claim, changing the voucher status to `SUBMITTED` or `PENDING_VALIDATION`.

#### 3.4 Feature 4: Claim Adjudication and Reimbursement
**3.4.1 Description:** The System Administrator shall review, validate, and approve claims for payment.
**3.4.2 Requirements:**
*   **FR4.1:** The system shall present a queue of submitted claims for review.
*   **FR4.2:** The administrator shall be able to approve or reject a claim, with a mandatory reason for rejection.
*   **FR4.3:** Upon approval, the voucher status shall change to `APPROVED_FOR_REIMBURSEMENT` and the claim marked as payable.
*   **FR4.4:** Upon rejection, the voucher status shall change to `REJECTED` and the provider notified (if functionality exists).
*   **FR4.5:** The system shall generate periodic (e.g., weekly) reimbursement reports listing all approved claims, totals, and provider banking details for finance processing.

#### 3.5 Feature 5: Reporting and Monitoring
**3.5.1 Description:** The system shall provide comprehensive reporting for program management.
**3.5.2 Requirements:**
*   **FR5.1:** Generate real-time dashboard showing: Total vouchers created, sold, used, reimbursed; claims pending.
*   **FR5.2:** Generate audit trail reports for any voucher, showing all status changes and associated users/timestamps.
*   **FR5.3:** Generate distributor performance reports (sales volume, returns).
*   **FR5.4:** Generate provider performance reports (claims submitted, approval rate).

---

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **Response Time:** Critical transactions (voucher validation on scan, sale completion) shall have a response time of < 2 seconds under normal load, even in offline-cached mode.
*   **Concurrent Users:** The system shall support up to 50 concurrent users (mix of administrators, distributors, providers).
*   **Data Volume:** As per constraint 2.5.1.

#### 4.2 Safety Requirements
*   No specific safety-critical functions identified.

#### 4.3 Security Requirements
*   **SR1:** All user access shall require authentication.
*   **SR2:** Sensitive operations (bulk sales, claim approval, financial report generation) shall require re-authentication or biometric (thumbprint) verification.
*   **SR3:** All data transmissions between client and server (during sync) shall be encrypted using TLS 1.2 or higher.
*   **SR4:** Database shall store passwords using strong, salted hashing algorithms.
*   **SR5:** System shall maintain a complete audit log of all financial and status-changing transactions.

#### 4.4 Software Quality Attributes
*   **Reliability:** System uptime shall be 99% during core business hours (8:00 AM - 6:00 PM, Mon-Sat).
*   **Usability:** The distributor and provider interfaces shall be simple, with minimal text, large buttons, and clear visual cues. Training required for new users shall not exceed 4 hours.
*   **Maintainability:** The system shall be modular with clear documentation to allow for future modifications by another development team.
*   **Portability:** The client application shall run on standard Windows 10/11 installations.

---

### 5. Other Requirements

#### 5.1 Database Design
*   The database shall be normalized to at least 3rd Normal Form (3NF).
*   Key tables shall include: `Vouchers`, `VoucherPairs`, `Distributors`, `Providers`, `SalesTransactions`, `Claims`, `Users`, `AuditLog`.
*   Indexes shall be created on frequently queried fields (Voucher ID, Pair ID, Status, Dates).

#### 5.2 Appendices
*   **Appendix A: Preliminary Data Dictionary** (To be developed)
*   **Appendix B: Preliminary UI Mockups** (To be developed)
*   **Appendix C: Hardware Interface Specifications** (To be developed upon hardware selection)

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| System Architect | | | |