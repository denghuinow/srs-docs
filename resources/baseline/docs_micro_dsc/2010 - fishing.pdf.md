# Software Requirements Specification (SRS)
## Electronic Logbook Software System (ELSS)
### For UK Fishing Vessels

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Approval

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Electronic Logbook Software System (ELSS). The primary purpose of this system is to enable UK fishing vessel operators to digitally record, validate, and report fishing activity, transhipment, and landing data in full compliance with European Commission (EC) regulations. This document serves as the basis for system design, development, testing, and formal product approval by the relevant UK fisheries administration.

### 1.2 Scope
The ELSS is an onboard software application to be installed and used exclusively on UK-registered fishing vessels. The system will:
*   Replace or supplement paper-based logbook reporting.
*   Capture fishing operations data directly from the user.
*   Perform real-time validation against regulatory business rules.
*   Generate structured XML reports conforming to the official UK fisheries schema.
*   Transmit reports and receive acknowledgements via available onboard communication systems.
*   Maintain a secure, tamper-evident record of all submitted data and system activity.

**Out of Scope:**
*   Use by onshore agents or processing companies.
*   Integration with vessel engine or gear sensors (though this is a potential future extension).
*   Management or reporting for non-UK fishing zones unless required by UK regulations.
*   Business functions unrelated to regulatory reporting (e.g., crew payroll, inventory management).

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **EC** | European Commission |
| **ELSS** | Electronic Logbook Software System |
| **FAR** | Fishing Activity Report |
| **LDR** | Landing Declaration Report |
| **TXR** | Transhipment Report |
| **XML** | eXtensible Markup Language |
| **XSD** | XML Schema Definition |
| **ACK/NACK** | Positive/Negative Acknowledgement |
| **UKFA** | UK Fisheries Administration |

### 1.4 References
*   EC Council Regulation (EC) No 1224/2009
*   Commission Implementing Regulation (EU) No 404/2011
*   **UK Fisheries Administration - Electronic Logbook XML Schema Definition (XSD) vX.x** (To be provided by approving authority)
*   **UK Fisheries Administration - Technical Interface Specification vY.y** (To be provided by approving authority)

### 1.5 Overview
The remainder of this document describes the overall description of the product (Section 2) and the specific requirements (Section 3). It details user characteristics, constraints, assumptions, and the functional requirements necessary for compliance and approval.

## 2. Overall Description

### 2.1 Product Perspective
The ELSS is a standalone onboard application. It will interact with:
*   **Users:** Vessel Master, Mate, or designated crew member.
*   **External Systems:** The UK Fisheries Administration's central reporting system via a designated communication gateway (e.g., satellite, cellular).
*   **Platform:** Onboard computer hardware (supplied by vessel or integrator).

The system architecture is conceptually simple:
```
[User] <-> [ELSS Application] <-> [Communication Module] <-> [UKFA Gateway]
                              |-> [Local Encrypted Database]
```

### 2.2 Product Functions
The high-level functions of the ELSS are:
1.  **Data Capture:** Provide intuitive forms for entering fishing trips, catches, transhipments, and landings.
2.  **Business Rule Validation:** Apply all relevant EC and UK validation rules at entry and prior to submission.
3.  **Report Management:** Create, save, edit (pre-submission), view, and delete draft and submitted reports.
4.  **XML Generation & Validation:** Transform stored data into XML format strictly compliant with the official UK XSD schema.
5.  **Secure Transmission:** Send XML reports to the UKFA gateway and receive/process acknowledgements.
6.  **Data Integrity & Security:** Maintain an immutable local log of all actions and transmitted data.

### 2.3 User Characteristics
*   **Primary User (Vessel Operator):** Possesses practical fishing knowledge but may have limited computer literacy. Must be able to perform tasks under challenging onboard conditions (vessel motion, weather). Understands fishing terminology (species codes, gear types, locations).
*   **Assumed Training:** Users will receive basic operational training on the ELSS.

### 2.4 Constraints
1.  **Regulatory Compliance:** The system's data output **must** validate without error against the officially provided UK XML Schema Definition (XSD). This is the paramount constraint.
2.  **Deployment Constraint:** The software is **for onboard use only**. It must not contain features designed for or accessible to onshore agents.
3.  **Update & Approval Constraint:** Any software update that modifies data handling, validation logic, or XML structure **must not invalidate compliance**. If an update potentially affects compliance, the product **requires re-submission and re-approval** by the UKFA before distribution.
4.  **Operational Environment:** Must function reliably in a marine environment with potential for intermittent, low-bandwidth, or high-latency connectivity.

### 2.5 Assumptions and Dependencies
*   The vessel will have access to a suitable computing device and a power supply.
*   The vessel will have an available communication method (satellite, cellular) capable of data transmission to the UKFA gateway.
*   The UKFA will provide and maintain a stable XSD schema and gateway interface.
*   The user is responsible for ensuring data entry is accurate and timely.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 Data Capture and Management
*   **FR-01:** The system shall allow the user to create a new Fishing Activity Report (FAR) for a fishing trip.
*   **FR-02:** The system shall provide input fields for all mandatory data elements as per the UK schema, including but not limited to: Vessel ID, Trip Start Date/Time, Location (ICES rectangle), Gear Type, Target Species, Catches (by species, weight).
*   **FR-03:** The system shall allow the user to save a report as a draft and resume editing it at a later time.
*   **FR-04:** The system shall allow the user to create Landing Declaration Reports (LDR) and Transhipment Reports (TXR) linked to a relevant FAR.

#### 3.1.2 Validation
*   **FR-05:** The system shall perform field-level validation during data entry (e.g., date format, numeric ranges, code list values).
*   **FR-06:** The system shall perform cross-field and business logic validation upon user command to "Validate" or "Submit" a report (e.g., catch weight consistency, chronological order of events, permitted fishing zones).
*   **FR-07:** The system shall present clear, actionable error messages to the user if validation fails, indicating the specific field and nature of the error.

#### 3.1.3 Report Generation and Export
*   **FR-08:** Upon successful validation and user confirmation, the system shall generate an XML document for the report.
*   **FR-09:** The generated XML **must** be well-formed and **must** validate successfully against the official UKFA XSD schema using a local schema validator.
*   **FR-10:** The system shall store a local copy of the exact XML generated for every submission.

#### 3.1.4 Communication and Acknowledgement
*   **FR-11:** The system shall transmit the validated XML report to the designated UKFA gateway using the protocol specified in the Technical Interface Specification.
*   **FR-12:** The system shall receive and parse acknowledgement messages (ACK/NACK) from the UKFA gateway.
*   **FR-13:** The system shall clearly display the status of each report (Draft, Validated, Submitted, Accepted, Rejected).
*   **FR-14:** If a NACK (negative acknowledgement) is received, the system shall alert the user and display the rejection reason provided by the UKFA.

#### 3.1.5 System Management and Security
*   **FR-15:** The system shall maintain an encrypted local database of all user data, reports, and transmission logs.
*   **FR-16:** The system shall prevent alteration or deletion of any report after it has been successfully submitted and acknowledged.
*   **FR-17:** The system shall provide a secure login mechanism (e.g., username/password) to identify the submitting user.

### 3.2 Non-Functional Requirements

#### 3.2.1 Usability
*   **NFR-01:** The user interface shall be designed for clarity and simplicity, usable in low-light conditions. Critical buttons shall be large and distinct.
*   **NFR-02:** The system shall provide contextual help or tooltips for all data entry fields, explaining the required format and source (e.g., "Enter ICES rectangle code, e.g., 39F0").

#### 3.2.2 Reliability
*   **NFR-03:** The system shall have a mean time between failures (MTBF) of not less than 1000 hours of operation.
*   **NFR-04:** In the event of a system crash or power loss during data entry, the system shall recover all draft data up to the last manual save or auto-save point.

#### 3.2.3 Performance
*   **NFR-05:** The system shall respond to user inputs (button presses, screen changes) in less than 2 seconds under normal operating conditions.
*   **NFR-06:** Validation of a complex report (e.g., a multi-species FAR) shall complete in less than 10 seconds.

#### 3.2.4 Supportability
*   **NFR-07:** The system shall include a diagnostic function that allows the user to generate a support package containing logs and recent reports (excluding sensitive data) for troubleshooting.

### 3.3 Compliance Requirements
*   **CR-01:** The software vendor shall provide the UKFA with a complete test suite demonstrating that the system generates XML that validates against the official XSD for all supported report types and edge cases.
*   **CR-02:** The vendor shall have a documented software update process. This process must include a compliance impact assessment step. Any update flagged as affecting compliance triggers the re-approval process before release.

---

## 4. Appendices

### Appendix A: XML Schema Compliance
*(This section will be populated with the specific UK XSD reference, example XML snippets, and a compliance matrix mapping data fields to schema elements once the official schema is provided.)*

### Appendix B: Data Field Glossary
*(This section will list all required data fields, their definitions, formats, and allowed code lists (e.g., FAO 3-alpha species codes, ICES rectangles).)*

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Developer | | | |
| Approval Authority (UKFA Rep) | | | |