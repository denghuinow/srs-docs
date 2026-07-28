# Software Requirements Specification (SRS)
## Tachograph Card Information Exchange System (TCIES)
**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Tachograph Card Information Exchange System (TCIES). The primary purpose of this document is to provide a detailed description of the system to be developed, serving as a basis for agreement between stakeholders, developers, and quality assurance teams. It will guide the design, implementation, and verification phases of the project.

#### 1.2 Document Conventions
*   **Requirements:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** "Shall" indicates a mandatory requirement. "Should" indicates a recommendation. "May" indicates a permissible action.
*   **Acronyms:**
    *   **TCIES:** Tachograph Card Information Exchange System
    *   **MS-CIA:** Member State Card Issuing Authority
    *   **TESTA-II:** Trans-European Services for Telematics between Administrations - II

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Sponsors & EU Governance Bodies:** Focus on Sections 1 (Introduction), 2 (Overall Description), and 5 (Key Constraints & Compliance).
*   **System Architects & Developers:** Focus on Sections 3 (System Features), 4 (External Interface Requirements), and 5 (Key Constraints & Compliance).
*   **Quality Assurance & Test Engineers:** Focus on all sections, particularly Section 3 (System Features) for test case derivation.
*   **Project Managers:** Review the entire document for scope, assumptions, and dependencies.

#### 1.4 Project Scope
The TCIES is a secure, distributed network system that facilitates the exchange of driver tachograph card status and assignment information **exclusively** between authorized EU Member State Card Issuing Authorities (MS-CIAs). The system enables query-based information sharing to support regulatory compliance but is explicitly designed to prevent the creation of a centralized European tachograph card database. The system does **not** store consolidated card data, manage card issuance processes, or interface directly with drivers or transport companies.

### 2. Overall Description

#### 2.1 Product Perspective
The TCIES is a new, standalone system that will operate as a node-to-node messaging hub on the secure TESTA-II network. Each MS-CIA will host its own TCIES instance. The system interfaces with the national card registry of its host MS-CIA and communicates with peer TCIES instances in other Member States.

#### 2.2 Product Functions (Summary)
1.  Process cross-border requests to check the tachograph cards issued to a specific driver.
2.  Process cross-border requests to check or update the operational status (e.g., valid, lost, stolen, withdrawn) of a specific tachograph card.
3.  Generate and provide system usage and transaction statistics for operational monitoring and reporting.
4.  Enforce strict security, privacy, and data minimization protocols in all transactions.

#### 2.3 User Classes and Characteristics
*   **Authorized MS-CIA Official:** The primary user. They are trained personnel within a national Card Issuing Authority. They initiate queries and receive responses via a national interface. They are not technical system administrators.
*   **System Administrator (per MS-CIA):** Responsible for the operation, monitoring, and basic configuration (e.g., peer authority certificate management) of the national TCIES instance.
*   **EU-Level Monitoring Authority:** A supervisory body that may request anonymized, aggregated usage statistics for audit and oversight purposes.

#### 2.4 Operating Environment
*   **Network:** Must operate exclusively within the **TESTA-II** network infrastructure.
*   **Software Environment:** Each MS-CIA instance will be deployed within the respective national administrative IT environment, likely a secured data center.
*   **Security Environment:** Must integrate with national PKI (Public Key Infrastructure) for authentication and support the required cryptographic standards for TESTA-II.

#### 2.5 Design and Implementation Constraints
1.  **NFR-CONSTRAINT-01:** The system architecture **shall** be designed such that no single Member State or the system itself can reconstruct a complete, consolidated European database of tachograph cards from the message traffic.
2.  **NFR-CONSTRAINT-02:** All communication **shall** be conducted via the **TESTA-II** network facilities. No other transport mechanisms are permitted.
3.  **NFR-CONSTRAINT-03:** The system **shall** implement mechanisms to guarantee **non-repudiation** (sender cannot deny sending a message) and **data privacy** (confidentiality and integrity) for every transaction.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Each MS-CIA maintains its own accurate and accessible national registry of issued tachograph cards.
*   **Assumption:** All participating MS-CIAs possess and maintain valid digital certificates compliant with the EU-wide PKI used on TESTA-II.
*   **Dependency:** The system's functionality is dependent on the availability and performance of the TESTA-II network.
*   **Dependency:** The definition of a standardized message format (e.g., XML schema) for requests and responses is a prerequisite for development.

### 3. System Features

#### 3.1 Feature 1: Driver Card Check
**Description:** An authorized official in MS-CIA "A" can query the system to find which tachograph cards have been issued to a specific driver (identified by a unique driver identifier) across the EU.

**3.1.1 Functional Requirements**
*   `FR-101:` The system shall allow an authorized user to initiate a "Driver Card Check" request by providing a standardized driver identifier.
*   `FR-102:` Upon receiving a request, the system shall automatically and simultaneously broadcast the query to the TCIES instances of all other participating MS-CIAs via TESTA-II.
*   `FR-103:` The system shall receive responses from other MS-CIAs' TCIES instances.
*   `FR-104:` The system shall aggregate the received responses and present a consolidated list to the requesting user, indicating which Member State(s) have issued card(s) to the driver.
*   `FR-105:` The system shall **not** persistently store the aggregated results from the broadcast query beyond the user's session for the purpose of fulfilling the request.

#### 3.2 Feature 2: Card Status Inquiry & Update
**Description:** An authorized official can check the current status of a specific tachograph card or report a change in its status (e.g., lost, stolen).

**3.2.1 Functional Requirements**
*   `FR-201:` The system shall allow a user to initiate a "Card Status Inquiry" by providing a unique card identifier.
*   `FR-202:` The system shall determine the issuing MS-CIA from the card identifier and route the inquiry request directly to that specific MS-CIA's TCIES instance via TESTA-II.
*   `FR-203:` The system shall receive the status response (e.g., "Valid", "Lost", "Stolen", "Withdrawn") from the issuing MS-CIA and display it to the user.
*   `FR-204:` The system shall allow a user from the **issuing** MS-CIA to initiate a "Card Status Update" for a card in their national registry.
*   `FR-205:` Upon a valid status update, the system shall automatically generate and send a "Status Change Notification" message to the TCIES instance of **every other** MS-CIA via TESTA-II. This message will contain the card identifier and new status **only**.
*   `FR-206:` Receiving MS-CIA systems shall process the notification to update their local "status cache" for that card but shall not store this information in a way that facilitates database reconstruction.

#### 3.3 Feature 3: Usage Statistics & Monitoring
**Description:** The system provides aggregated data on its own usage for performance monitoring and regulatory oversight.

**3.3.1 Functional Requirements**
*   `FR-301:` The system shall log all incoming and outgoing transactions (success and failure) with essential metadata (e.g., timestamp, type, partner MS-CIA, result, no personal/card data).
*   `FR-302:` The system shall generate pre-defined statistical reports (e.g., number of queries by type per day/week/month, number of queries per partner MS-CIA, system availability).
*   `FR-303:` The system shall provide an interface for the local System Administrator to view and export these statistics.
*   `FR-304:` The system shall be capable of generating an anonymized, aggregated subset of statistics for submission to an EU-Level Monitoring Authority upon authorized request.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   A secure, web-based administrative interface for MS-CIA officials (for query input and results display).
*   A separate, restricted web-based interface for System Administrators (for monitoring, statistics, and certificate management).

#### 4.2 Hardware Interfaces
*   The system shall be deployable on standard server hardware meeting the performance and security standards of national government data centers.

#### 4.3 Software Interfaces
1.  **National Card Registry Interface:** A secure, national-specific adapter/API to query the local MS-CIA's database of issued cards (`FR-203`, `FR-204`).
2.  **TESTA-II Network Interface:** The system shall implement the required protocols and security gateways (e.g., sTESTA) to send and receive messages over TESTA-II.

#### 4.4 Communication Interfaces
*   All inter-Member State communication **shall** use the TESTA-II network.
*   Message formats shall be standardized (e.g., using XML schemas) and shall include necessary headers for routing, security, and non-repudiation.
*   Communication shall employ TLS/mTLS as mandated by TESTA-II, with digital signatures on payloads to ensure non-repudiation (`NFR-CONSTRAINT-03`).

### 5. Non-Functional Requirements & Key Constraints

#### 5.1 Security Requirements
*   `NFR-SEC-01:` **Non-Repudiation:** All messages shall be digitally signed by the sending MS-CIA instance. The system shall validate signatures on all incoming messages.
*   `NFR-SEC-02:` **Data Privacy:** All data in transit shall be encrypted using strong cryptography as prescribed for TESTA-II. Personal data shall be minimized in all messages.
*   `NFR-SEC-03:` **Authentication & Authorization:** All user access to the national TCIES interface shall require strong authentication (e.g., smart card). All system-to-system communication shall be authenticated via mTLS and/or digital certificates.
*   `NFR-SEC-04:` **Prevention of Database Reconstruction:** The system shall be designed to comply with `NFR-CONSTRAINT-01`. This shall be achieved through:
    *   Query broadcasting (`FR-102`) without revealing which MS-CIA holds data.
    *   Direct, point-to-point status inquiries (`FR-202`).
    *   Prohibition of bulk data queries or "list all cards" functionalities.
    *   Strict limits on data retention in logs and caches.

#### 5.2 Network Compliance
*   `NFR-NET-01:` The system shall be certified for operation on the **TESTA-II** network and shall comply with all its technical and security policies (`NFR-CONSTRAINT-02`).

#### 5.3 Performance Requirements
*   `NFR-PER-01:` The system shall process and route a broadcast query to all Member States within 5 seconds under normal load.
*   `NFR-PER-02:` A point-to-point status inquiry/response cycle shall be completed within 10 seconds, 95% of the time.

#### 5.4 Availability Requirements
*   `NFR-AVAIL-01:` The system shall achieve 99.5% operational availability during standard EU business hours (CET).

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| Quality Assurance Lead | | | |