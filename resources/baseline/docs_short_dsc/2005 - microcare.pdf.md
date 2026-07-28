# **Software Requirements Specification (SRS)**
**For the Voucher Management System (VMUS)**
**Version:** 1.0
**Date:** October 26, 2023
**Prepared for:** Marie Stopes International Uganda (MSIU)
**Prepared by:** [Your Organization/Team Name]

---

## **1. Introduction**

### **1.1 Purpose**
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Voucher Management System (VMUS). The intended audience includes MSIU stakeholders, project managers, system architects, developers, testers, and implementation teams. This document serves as the foundation for system design, development, testing, and acceptance.

### **1.2 Document Conventions**
*   **Bold text** is used for key terms and system entities.
*   *Italic text* is used for emphasis.
*   `Monospaced text` indicates system messages, field names, or code.
*   Requirements are uniquely identified as `FR-XXX` (Functional) or `NFR-XXX` (Non-Functional).

### **1.3 Project Scope**
The VMUS is a desktop application designed to automate the core processes of the Voucher Management Unit (VMU) for a pilot Output-Based Aid (OBA) program in Mbarara District. It will manage the end-to-end lifecycle of STD treatment vouchers, from creation and distribution to claim validation and reimbursement reporting. The system's primary goals are to enhance operational efficiency, minimize fraud, ensure accurate and timely payments to service providers, and provide robust data for program monitoring.

#### **1.3.1 In Scope**
*   Automated creation of uniquely identifiable, barcoded vouchers.
*   Management of voucher inventory, distribution, and sales transactions.
*   Processing and validation of paper-based claims submitted by Voucher Service Providers (VSPs).
*   Generation of a standard suite of financial, medical, and operational reports.
*   Implementation of a comprehensive, role-based access control system.
*   Integration with barcode scanners and biometric (thumbprint) devices.

#### **1.3.2 Out of Scope**
*   Design or execution of marketing and Behavioral Change Communication (BCC) campaigns.
*   Clinical decision support or patient management at VSP facilities.
*   Features supporting program expansion beyond the pilot district or phase.
*   Direct integration with banking systems for electronic fund transfers.
*   Real-time, online claim submission portal for VSPs. The system will process batch data entry from paper forms.

### **1.4 References**
*   MSIU OBA Program Design Document.
*   VMU Operational Manual and Procedures.
*   Oracle 9i Database Documentation.
*   Crystal Reports 9 Developer Guide.

---

## **2. Overall Description**

### **2.1 Product Perspective**
The VMUS is a new, standalone client-server application. It will serve as the central system of record for the VMU pilot program, replacing manual, paper-intensive processes. The system will interact with peripheral hardware (barcode scanners, fingerprint readers) but will not integrate with other enterprise systems (e.g., HR, Finance) at this stage.

### **2.2 Product Functions (Summary)**
1.  **Voucher Master Management:** Create, batch, and manage voucher inventory with security features.
2.  **Distribution & Sales Management:** Record purchases by distributors, track sales to clients, and manage returns.
3.  **Claim Processing:** Data entry, validation, and adjudication of treatment claims submitted by VSPs.
4.  **Reporting & Analytics:** Generate standardized reports for finance, medical outcomes, and program operations.
5.  **System Administration:** Manage users, roles, permissions, and reference data (e.g., VSP list, distributor list).
6.  **Audit & Security:** Maintain a complete audit trail and enforce data integrity and access controls.

### **2.3 User Classes and Characteristics**
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **System Administrator** | Configures the system, manages all user accounts and security. | High technical proficiency, understands program structure. |
| **MSIU Admin Team** | Oversees program, authorizes payments, reviews high-level reports. | Managerial role, needs summary data and approval workflows. |
| **VMU Field Office Staff** | Daily system operators; enter sales, process claims, run routine reports. | Primary users, require efficient data entry and validation screens. |
| **Voucher Service Provider (VSP)** | Submits claims for reimbursement (via paper forms). | External stakeholder, indirect user; system must validate their data. |
| **Distributor** | Purchases vouchers for resale (transaction recorded by VMU staff). | External stakeholder, indirect user. |
| **Client/Patient** | Purchases and uses voucher for treatment. | Beneficiary, no direct system interaction. |

### **2.4 Operating Environment**
*   **Software:**
    *   **Backend Database:** Oracle 9i
    *   **Frontend Application:** Microsoft Visual Basic 6.0 (or compatible .NET framework)
    *   **Reporting Engine:** Crystal Reports 9
    *   **Client OS:** Windows XP / 7
    *   **Server OS:** Windows Server 2003 / 2008
*   **Hardware:**
    *   Barcode scanners (USB or keyboard wedge).
    *   Biometric thumbprint scanners with SDK compatible with Visual Basic.

### **2.5 Design and Implementation Constraints**
1.  `CON-001`: The system **must** be developed using the Oracle 9i database, a Visual Basic front-end, and Crystal Reports 9.
2.  `CON-002`: The business logic must enforce a **"one voucher per person at a time"** rule to prevent fraud.
3.  `CON-003`: Voucher data, once saved, **cannot be edited or deleted**. Authorized users may only "withhold" a voucher or amend its validity date, with both actions logged.
4.  `CON-004`: The database schema must be designed for **efficiency and scalability**, anticipating future expansion.
5.  `CON-005`: All financial calculations must use fixed decimal arithmetic to prevent rounding errors.

### **2.6 Assumptions and Dependencies**
*   VMU field offices will have stable electrical power and basic computer literacy among staff.
*   VSPs will submit complete, legible paper claim forms.
*   The system administrator will be trained to manage user roles and system parameters.
*   Success depends on accurate initial population of master data (VSPs, Distributors, Treatment codes).

---

## **3. System Features**

### **3.1 Feature 1: Voucher Lifecycle Management**
#### **3.1.1 Description and Priority**
This feature covers the creation, status tracking, and inventory management of vouchers. It is a **High** priority core feature.

#### **3.1.2 Functional Requirements**
*   `FR-101`: The system shall allow an authorized user to create a new batch of vouchers.
    *   `FR-101.1`: The user must specify the batch quantity, voucher value, and validity period.
    *   `FR-101.2`: The system shall auto-generate a unique, sequential voucher number for each voucher in the batch.
    *   `FR-101.3`: The system shall generate a corresponding barcode for each voucher number.
*   `FR-102`: The system shall assign an initial status of "**In Stock**" to all newly created vouchers.
*   `FR-103`: The system shall maintain a complete, unchangeable history of every status change for each voucher (e.g., In Stock -> Sold -> Used -> Paid).
*   `FR-104`: An authorized user shall be able to "withhold" a batch or individual voucher, changing its status to "**Withheld**" and preventing its sale or use.
*   `FR-105`: An authorized user shall be able to amend the expiry date of a voucher that is "In Stock" or "Sold" but not yet "Used".

### **3.2 Feature 2: Distribution & Sales Management**
#### **3.2.1 Description and Priority**
This feature manages the movement of vouchers from MSIU to distributors and finally to clients. It is a **High** priority.

#### **3.2.2 Functional Requirements**
*   `FR-201`: The system shall record a transaction when a distributor purchases a batch of vouchers from MSIU.
    *   `FR-201.1`: Transaction entry shall be facilitated by scanning the voucher batch barcode.
    *   `FR-201.2`: Voucher status shall change from "In Stock" to "**With Distributor**".
*   `FR-202`: The system shall record the sale of a voucher by a distributor to a client.
    *   `FR-202.1`: The VMU staff shall enter the sale by scanning the voucher barcode.
    *   `FR-202.2`: The system shall require the client's **thumbprint** to be scanned and linked to the voucher.
    *   `FR-202.3`: The system shall enforce `CON-002` by checking if the client's thumbprint is already linked to an active ("Sold" or "Used") voucher.
    *   `FR-202.4`: Upon successful validation, the voucher status shall change to "**Sold**".
*   `FR-203`: The system shall allow for the return of unsold vouchers from a distributor, changing their status back to "In Stock".

### **3.3 Feature 3: Claim Processing & Validation**
#### **3.3.1 Description and Priority**
This is the core feature for processing paper-based claims from VSPs. It includes data entry, automated validation, and fraud checks. **High** priority.

#### **3.3.2 Functional Requirements**
*   `FR-301`: The system shall provide an interface for VMU staff to enter data from the VSP paper claim form.
    *   `FR-301.1`: Primary voucher data (number, patient details) shall be entered by scanning the voucher barcode.
    *   `FR-301.2`: The system shall verify the scanned voucher is in "**Sold**" status and is valid (not expired).
*   `FR-302`: The system shall perform a **biometric verification** during claim entry.
    *   `FR-302.1`: The system shall prompt the staff to scan the patient's thumbprint.
    *   `FR-302.2`: The system shall match this scan against the print recorded during the voucher sale (`FR-202.2`).
*   `FR-303`: The system shall perform a series of validations and flag claims that:
    *   `FR-303.1`: Have mismatched biometric data (potential fraud).
    *   `FR-303.2`: Are for vouchers already used in a previous claim (duplicate claim).
    *   `FR-303.3`: Have missing or invalid treatment codes or dates.
*   `FR-304`: Claims that pass all validations shall be marked "**Validated**" and the voucher status updated to "**Used**".
*   `FR-305`: Flagged claims shall be moved to a "**Quarantine**" queue for manual review by the MSIU Admin Team.

### **3.4 Feature 4: Reporting**
#### **3.4.1 Description and Priority**
This feature enables the generation of standard reports for monitoring and decision-making. **Medium** priority.

#### **3.4.2 Functional Requirements**
*   `FR-401`: The system shall generate a **VSP Payment Report** listing all validated claims per provider within a date range, ready for reimbursement processing.
*   `FR-402`: The system shall generate **Inventory Reports** showing voucher status counts (In Stock, Sold, Used, Withheld) by batch.
*   `FR-403`: The system shall generate **Medical Summary Reports** aggregating treated conditions by demographic data (age, gender).
*   `FR-404`: The system shall generate **Distributor Performance Reports** showing sales and returns by distributor.
*   `FR-405`: All reports shall be exportable to PDF and Excel formats.

### **3.5 Feature 5: System Administration & Security**
#### **3.5.1 Description and Priority**
This feature manages system access, user roles, and reference data. **High** priority.

#### **3.5.2 Functional Requirements**
*   `FR-501`: The system shall implement role-based access control (RBAC) with the following pre-defined roles: System Admin, MSIU Admin, VMU Staff (Data Entry), VMU Staff (Supervisor).
*   `FR-502`: The System Administrator shall be able to create/modify user accounts and assign them to one or more roles.
*   `FR-503`: The System Administrator shall be able to define granular permissions (Create, Read, Update, Delete, Withhold, Approve) for each system module and assign them to roles.
*   `FR-504`: The system shall maintain an **audit log** recording key user actions (login attempts, voucher status changes, claim validations, financial transactions).

---

## **4. External Interface Requirements**

### **4.1 User Interfaces**
*   The UI shall be a Windows Forms application with a clear, menu-driven navigation.
*   Data entry forms shall be tab-sequential and optimized for keyboard and scanner input.
*   List views shall include filtering and sorting capabilities.

### **4.2 Hardware Interfaces**
*   `NFR-HW-001`: The system shall interface with standard USB barcode scanners using keyboard wedge emulation.
*   `NFR-HW-002`: The system shall integrate with biometric fingerprint scanners using the manufacturer's provided Windows SDK/API.

### **4.3 Software Interfaces**
*   `NFR-SW-001`: The application shall connect to a central **Oracle 9i** database via OLE DB or ODBC connection.
*   `NFR-SW-002`: Report generation shall be handled by **Crystal Reports 9** runtime engine, called from the Visual Basic application.

---

## **5. Non-Functional Requirements**

### **5.1 Performance Requirements**
*   `NFR-PER-001`: Batch creation of 1000 vouchers shall complete within 2 minutes.
*   `NFR-PER-002`: Searching for a voucher by number or barcode scan shall return results in less than 3 seconds.
*   `NFR-PER-003`: The system shall support up to 10 concurrent users in the field office.

### **5.2 Security Requirements**
*   `NFR-SEC-001`: All user passwords shall be stored encrypted in the database.
*   `NFR-SEC-002`: User sessions shall timeout after 15 minutes of inactivity.
*   `NFR-SEC-003`: Access to the application shall be restricted to computers within the MSIU network domain or via approved VPN.
*   `NFR-SEC-004`: The system shall comply with MSIU's data privacy policy regarding patient health information.

### **5.3 Software Quality Attributes**
*   **Reliability:** The system shall have 99% uptime during core business hours (8:00 AM - 6:00 PM).
*   **Usability:** A trained user shall be able to enter a standard claim form in under 3 minutes.
*   **Maintainability:** The code shall be well-commented, and the database shall have a documented data dictionary.

---

## **6. Other Requirements**

### **6.1 Success Metrics**
The system will be deemed successful if:
1.  It processes 95% of clean VSP claims within 5 working days of receipt, enabling on-schedule reimbursement.
2.  It successfully identifies and quarantines 100% of claims failing the biometric mismatch or duplicate voucher validation rules.
3.  It generates 100% of the required standard reports accurately and on demand.

### **6.2 Undecided Issues (To Be Resolved)**
1.  The final **minimum batch quantity** for voucher creation.
2.  The specific data fields and UI format for capturing **HIV-related information** on the claim form.
3.  The final list, design, and specification for **custom analytical reports** beyond the standard set.
4.  The detailed workflow and authorization criteria for **reactivating a VSP** that was auto-deactivated due to fraud flags.
5.  The business rule for handling **duplicate names** among distributors and sales staff in reports (e.g., use of unique ID codes).

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| MSIU Project Sponsor | | | |
| MSIU Technical Lead | | | |
| Development Lead | | | |
| Quality Assurance Lead | | | |