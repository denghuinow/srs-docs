# Software Requirements Specification (SRS)
## Voucher Management System (VMUS)
**Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### **1. Introduction**

#### **1.1 Purpose**
This document defines the functional and non-functional requirements for the Voucher Management System (VMUS). The VMUS is intended to automate the operations of the Voucher Management Unit (VMU) for an Output-based Aid (OBA) program providing subsidized Sexually Transmitted Disease (STD) treatment in Mbarara District, Uganda. This SRS serves as a contract between the project stakeholders and the development team, providing a complete description of the system's behavior.

#### **1.2 Document Conventions**
*   **Bold text** is used for key terms and system entities.
*   *Italic text* is used for emphasis.
*   `Monospaced text` indicates data elements, field names, or code references.
*   Requirements are uniquely identified as `FR` (Functional) or `NFR` (Non-Functional).

#### **1.3 Project Scope**
The VMUS will manage the end-to-end lifecycle of treatment vouchers, including creation, distribution, claim submission, validation, payment processing, and reporting. The system will minimize manual data entry, prevent fraud through validation and biometric checks, and ensure timely reimbursement to service providers. It is scoped to support a one-year pilot program with an estimated volume of 20,000+ vouchers, with a database and architecture designed for future scalability and expansion.

**Out-of-Scope:**
*   Direct patient medical record management beyond the data required for claim validation.
*   Inventory management of medical supplies at Voucher Service Provider (VSP) facilities.
*   A public-facing website or mobile application for clients or distributors.
*   Integration with national health or financial databases.

#### **1.4 References**
*   Project Charter: Balanced Summary - Voucher Management System (VMUS)
*   OBA Program Operational Guidelines
*   STD Treatment Protocols (Uganda Ministry of Health)

#### **1.5 Definitions, Acronyms, and Abbreviations**
| Term | Definition |
| :--- | :--- |
| **OBA** | Output-Based Aid. A financing mechanism where subsidies are paid upon verification of service delivery. |
| **VMU** | Voucher Management Unit. The entity responsible for administering the voucher program. |
| **VSP** | Voucher Service Provider. A health facility approved to provide subsidized STD treatment using vouchers. |
| **VMUS** | Voucher Management System. The software system described in this document. |
| **MSIU** | Administering organization's management team. |
| **Claim** | A formal request for reimbursement submitted by a VSP for services rendered to a client using a voucher. |

---

### **2. Overall Description**

#### **2.1 Product Perspective**
The VMUS is a new, standalone client-server application. It will interface with external hardware devices (barcode readers, biometric scanners) and generate reports for analysis. The system does not replace but complements existing manual paper-based processes for claim form submission and feedback collection.

**Architecture:** The system will follow a modular 3-tier architecture:
*   **Front-end:** Visual Basic (VB) application providing the user interface.
*   **Back-end:** Oracle 9i database for data storage and business logic (via stored procedures).
*   **Reporting Layer:** Crystal Reports for generating standard and ad-hoc reports.

#### **2.2 User Classes and Characteristics**
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **System Administrator** | Technically proficient, manages IT infrastructure. | User account management, security configuration, system maintenance. |
| **MSIU Admin Team** | Managerial role, focuses on program performance and finance. | High-level reports, dashboard views, configuration of payment terms. |
| **VMU Field Office Staff** | Primary system users, perform data entry and validation. | Efficient data entry screens, clear validation messages, batch processing capabilities. |
| **Voucher Service Provider (VSP)** | External health worker, submits paper claims. | Clarity on claim status, transparency in payment calculations, simple correction process. |
| **Distributor** | External community-based seller, may have low tech literacy. | Simple inventory reconciliation process, clear sales reporting. |
| **Client/Patient** | Beneficiary of the program, does not directly use the system. | Assurance that their voucher is valid and their privacy is protected. |

#### **2.3 Operating Environment**
*   **Hardware:** Standard PCs, barcode printers & readers, biometric thumbprint scanners.
*   **Software:** Microsoft Windows OS, Oracle 9i Client & Server, Crystal Reports runtime.
*   **Network:** Local Area Network (LAN) within the VMU field office.

#### **2.4 Design and Implementation Constraints**
1.  The database must be designed in Oracle 9i.
2.  The user interface must be developed in Visual Basic (VB).
3.  Reporting must be implemented using Crystal Reports.
4.  The system must support the use of standard barcode readers (Code 128/39) and Windows-compatible biometric scanners.

#### **2.5 Assumptions and Dependencies**
*   **Assumption:** Master data (drug lists, syndrome codes, location data) will be finalized and provided prior to system configuration.
*   **Dependency:** Hardware (barcode and biometric devices) must be procured and available for integration testing.
*   **Dependency:** Payment terms (fee schedules) must be agreed upon and finalized with all VSPs before the payment module can be completed.
*   **Assumption:** Users will have basic computer literacy and will receive formal training.

---

### **3. System Features and Requirements**

#### **3.1 User Management & Security**
**Description:** This module controls access to the system based on user roles and permissions.
*   **FR-01:** The system shall allow a **System Administrator** to create, modify, and deactivate user accounts.
*   **FR-02:** The system shall support the definition of **User Groups** (e.g., Admin, Field Officer, Data Entry Clerk).
*   **FR-03:** The system shall allow the assignment of granular permissions (New, Edit, Delete, View, Print) **by individual screen or function** to User Groups or individual users.
*   **FR-04:** All users shall be required to authenticate with a unique username and password to access the system.
*   **NFR-01 (Security):** The system shall implement role-based access control (RBAC) to ensure users can only access functions and data pertinent to their role.

#### **3.2 Voucher Master Data Management**
**Description:** This module manages core reference data for Distributors and VSPs.
*   **FR-05:** The system shall allow authorized users to maintain a registry of **Distributors** (`Distributor Code`, Name, Business Type, Address, Contact, Status).
*   **FR-06:** The system shall allow authorized users to maintain a registry of **Voucher Service Providers (VSPs)** (`VSP Code`, Provider Name, Facility Details, Payment Terms, Status).
*   **FR-07:** The system shall prevent the deletion of a Distributor or VSP if they have associated vouchers or claims in the system.

#### **3.3 Voucher Creation and Batch Management**
**Description:** This module handles the generation and initial tracking of vouchers.
*   **FR-08:** The system shall allow authorized users to **create batches of vouchers**. Each batch requires: Project Code, Quantity, Validity Start/End Date.
*   **FR-09:** For each voucher in a batch, the system shall **automatically generate** a unique `Voucher Number`, a `Security Code`, and a corresponding barcode.
*   **FR-10:** The system shall allow the printing of voucher slips (format TBD - see Undecided Issues) containing the Voucher Number, Security Code, Barcode, and Validity Date.
*   **FR-11:** The initial status of a created voucher shall be "**In Stock**".

#### **3.4 Voucher Distribution and Inventory**
**Description:** This module tracks the movement of vouchers from the VMU to Distributors.
*   **FR-12:** The system shall record the **sale/distribution** of voucher batches or individual vouchers to a specific Distributor, changing the voucher status to "**With Distributor**".
*   **FR-13:** The system shall allow a Distributor's inventory to be reconciled, recording the **return of unsold vouchers**, changing their status back to "**In Stock**".
*   **FR-14:** The system shall provide reports showing voucher inventory status by batch and distributor.

#### **3.5 Claim Entry and Validation**
**Description:** This is the core module where VMU staff enter and validate claims submitted by VSPs.
*   **FR-15:** The system shall allow entry of a new **Claim** by scanning the voucher barcode or manually entering the `Voucher Number`.
*   **FR-16:** Upon scanning/entry, the system shall automatically validate:
    *   `Voucher Number` exists and is valid.
    *   Voucher status is "With Distributor" or "Sold".
    *   Voucher validity date has not expired.
*   **FR-17:** The system shall prompt the user to link the claim to a specific `VSP Code` (provider where service was delivered).
*   **FR-18:** The claim entry screen shall capture clinical and administrative data from the claim form via dropdowns from master tables: Patient Details (age, sex), Diagnosis (syndrome), Services Provided (consultation, drugs, lab tests), Visit Count.
*   **FR-19:** The system shall require the entry or scanning of a **client thumbprint** (biometric data) as a fraud prevention measure.
*   **FR-20:** The system shall check for **duplicate claims** using the voucher number and thumbprint data. If a duplicate is suspected, it shall flag the claim for review.
*   **FR-21:** Upon successful validation and saving, the voucher status shall change to "**Redeemed**" and the claim status shall be "**Entered**".

#### **3.6 Claim Quarantine and Correction**
**Description:** This module manages claims that fail validation.
*   **FR-22:** If a claim fails validation (missing data, invalid voucher, duplicate thumbprint), the system shall place it in "**Quarantined**" status.
*   **FR-23:** The system shall generate a quarantine report/list for the VMU staff, detailing the error(s) for each claim.
*   **FR-24:** The system shall allow VMU staff to print or electronically send a correction request to the relevant VSP.
*   **FR-25:** The system shall allow a quarantined claim to be edited and re-validated once corrected information is received.

#### **3.7 Payment Processing**
**Description:** This module calculates reimbursements and generates payment instructions.
*   **FR-26:** The system shall allow authorized users (e.g., MSIU Admin) to **define payment terms** (fee schedules) linked to VSPs or provider types.
*   **FR-27:** The system shall **automatically calculate the claim amount** based on the services recorded in the claim and the applicable payment terms.
*   **FR-28:** The system shall allow users to select a batch of "Entered" claims and mark them as "**Approved for Payment**".
*   **FR-29:** The system shall generate a **Payment Report** for approved claim batches, summarizing total amounts payable per VSP, with supporting detail.
*   **FR-30:** Upon final payment confirmation, the claim status shall be updated to "**Paid**".

#### **3.8 Reporting and Analytics**
**Description:** This module provides insights into program operations.
*   **FR-31:** The system shall generate standard reports including, but not limited to:
    *   Voucher Status Report (In Stock, Distributed, Redeemed, Expired)
    *   Claims Processing Report (Entered, Quarantined, Approved, Paid)
    *   **Provider Comparison Report** (Number of clients, services rendered, claim amounts by VSP)
    *   Payment Summary Report (By period, by VSP)
    *   Distributor Performance Report (Sales, returns)
*   **FR-32:** The system shall allow for the entry of **Client Feedback** data linked to the voucher number, capturing satisfaction scores.
*   **FR-33:** Reports should be exportable to common formats (PDF, Excel).

#### **3.9 System Administration**
*   **FR-34:** The system shall maintain an audit log of critical user actions (login attempts, voucher creation, claim approval, payment runs).
*   **FR-35:** The system shall allow for the management of all master tables (syndromes, drugs, locations).

---

### **4. Non-Functional Requirements**

#### **4.1 Usability**
*   **NFR-02:** The user interface shall be designed for users with basic computer skills. Data entry shall be minimized through the extensive use of dropdown lists, checkboxes, and barcode scanning.
*   **NFR-03:** The system shall be trainable to a proficient level by field staff within one week of dedicated training.

#### **4.2 Reliability**
*   **NFR-04:** The system shall include validation checks at the point of data entry to prevent errors (e.g., date formats, numeric ranges, mandatory fields).
*   **NFR-05:** The system shall have a claimed data uptime of 99% during standard business hours (8:00 AM - 5:00 PM, Mon-Fri).

#### **4.3 Performance**
*   **NFR-06:** The database shall be designed using surrogate keys and normalized schemas to efficiently handle a minimum of 20,000 voucher records and their associated transactions.
*   **NFR-07:** Critical operations (claim entry via barcode scan, voucher validation) shall have a response time of less than 2 seconds under normal load.

#### **4.4 Supportability**
*   **NFR-08 (Maintainability):** The system shall be built using a modular design (separate modules for Voucher Mgmt., Claims, Payments, etc.) to facilitate independent testing, debugging, and future updates.
*   **NFR-09:** The system shall provide comprehensive help text or tooltips for all data entry fields and functions.

#### **4.5 Security**
*   **NFR-10:** User passwords shall be stored in the database using industry-standard hashing algorithms (e.g., SHA-256 with salt).
*   **NFR-11:** The system shall detect and log multiple failed login attempts, potentially locking the account after a defined threshold.

---

### **5. Appendices**

#### **5.1 Data Dictionary (Partial)**
| Entity | Attribute | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| **Voucher** | `Voucher_Number` | VARCHAR2(20) | Unique voucher identifier. Primary Key. | System-generated. |
| | `Batch_Number` | VARCHAR2(15) | Identifier for the creation batch. | |
| | `Validity_End_Date` | DATE | Date after which the voucher is invalid. | Must be > creation date. |
| | `Status` | VARCHAR2(20) | In Stock, With Distributor, Redeemed, Expired. | |
| **Claim** | `Claim_Number` | NUMBER | System-generated claim ID. Primary Key. | Auto-increment. |
| | `Voucher_Number` | VARCHAR2(20) | FK to Voucher. | NOT NULL. |
| | `VSP_Code` | VARCHAR2(10) | FK to VSP. | NOT NULL. |
| | `Claim_Amount` | NUMBER | Calculated reimbursement due. | |
| | `Status` | VARCHAR2(20) | Entered, Quarantined, Approved, Paid. | |

#### **5.2 Undecided Issues (TBD)**
The following items require stakeholder resolution and will impact detailed design:
1.  Final physical format of voucher slips (e.g., sticker, pre-printed card).
2.  Minimum and maximum quantity for a single voucher batch creation.
3.  Specific business rules and thresholds for automatic fraud detection flags and VSP deactivation.
4.  Detailed data fields and form layout for the HIV details capture module.
5.  Final list of customized analytical reports beyond the standard set.
6.  Operational procedure and system action for claims that remain in "Quarantined" status beyond a specified period (e.g., 60 days).

---
**Document Approval:**

| Name | Role | Signature | Date |
| :--- | :--- | :--- | :--- |
| | Project Sponsor | | |
| | Lead Developer | | |
| | System Architect | | |