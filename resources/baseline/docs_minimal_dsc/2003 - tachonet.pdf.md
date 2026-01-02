# Software Requirements Specification (SRS)
## European Card Information Exchange System (ECIES)
**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the European Card Information Exchange System (ECIES). The primary purpose of this document is to provide a detailed description of the system to be developed, serving as a basis for mutual agreement between stakeholders, developers, and quality assurance teams. It will guide the design, implementation, and testing phases of the project.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms "MUST," "MUST NOT," "SHALL," "SHALL NOT," "SHOULD," and "MAY" are used as defined in IETF RFC 2119.
*   **Acronyms:**
    *   **CIA:** Card Issuing Authority (of a Member State)
    *   **ECIES:** European Card Information Exchange System
    *   **TCN:** Tachograph Card Network (administrative entity)
    *   **TESTA-II:** Trans-European Services for Telematics between Administrations, second generation.

#### 1.3 Project Scope
The ECIES is a secure, distributed information exchange platform. Its core purpose is to enable European Member States' Card Issuing Authorities (CIAs) to query and update the status of driver smart cards and tachograph cards in a standardized manner, without creating a centralized European database. The system is designed to prevent fraud (e.g., multiple card issuances to the same driver) and facilitate efficient card lifecycle management (e.g., reporting lost/stolen cards) across national borders.

**In-Scope:**
*   Secure, peer-to-peer query/response mechanisms between Member State systems.
*   Standardized XML-based message protocols for all card-related transactions.
*   A central hub for routing messages, auditing transactions, and generating aggregated, anonymized statistics.
*   Administrative interfaces for user management, log viewing, and statistical reporting.
*   Phonetic key generation service for cross-lingual name matching.

**Out-of-Scope:**
*   The actual issuance, personalization, or physical management of driver/tachograph cards.
*   Direct access to or management of Member States' national card registries.
*   Enforcement actions or business logic decisions based on query results (these remain the responsibility of the requesting CIA).

#### 1.4 References
*   EU Regulation (EU) No 165/2014 concerning tachographs in road transport.
*   Commission Implementing Regulation (EU) 2016/799 (technical specifications for tachographs).
*   TESTA-II Network Security and Service Level Policies.
*   ISO/IEC/IEEE 29148:2018 - Systems and software engineering — Life cycle processes — Requirements engineering.

### 2. Overall Description

#### 2.1 Product Perspective
ECIES is a middleware system operating within the secure TESTA-II network. It acts as an intermediary between the back-end applications of participating Member State CIAs. The system does not store a consolidated cardholder database but facilitates queries against the distributed national databases. A central ECIES hub manages routing, security, non-repudiation, and auditing.

#### 2.2 Product Functions
The high-level functions of ECIES are:
1.  **Cross-Border Card Inquiry:** Allow a CIA to check if a driver already holds a valid card in another Member State.
2.  **Card Status Management:** Allow a CIA to declare changes to a card's status (e.g., Lost, Stolen, Withdrawn, Malfunctioning).
3.  **Tachograph Card Check:** Allow a CIA to verify the current status of a specific tachograph card.
4.  **Statistical Reporting:** Provide authorized administrators with tools to generate and view system usage statistics.
5.  **Phonetic Key Service:** Provide a standardized algorithm to compute phonetic search keys from driver names to aid matching across different languages and transliterations.
6.  **System Administration:** Manage users, roles, certificates, and audit logs.

#### 2.3 User Classes and Characteristics
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **CIA Administrator** | Personnel within a Member State's Card Issuing Authority. | Operates a national GUI client connected to ECIES. Initiates card checks and status updates. Requires strong authentication. |
| **CIA Application** | Automated back-end system of a Member State. | Integrates via ECIES web service APIs. Sends and receives XML messages automatically as part of national card issuance workflows. |
| **TCN Administrator** | Central system overseer at the Tachograph Card Network level. | Has read-only or supervisory access to cross-Member State audit logs and aggregated statistics. Cannot view individual transaction content. |

#### 2.4 Operating Environment
*   **Network:** MUST operate exclusively on the secure TESTA-II sTESTA network.
*   **Platform:** The central hub and services must be deployable on a standard JEE or .NET application server environment.
*   **Client:** CIA administrative clients can be a web-based application or a thick client compatible with modern operating systems (Windows, Linux).
*   **Database:** RDBMS (e.g., Oracle, PostgreSQL, SQL Server) for storing audit trails, statistics, and system data (not cardholder data).

#### 2.5 Design and Implementation Constraints
1.  **Architectural Constraint:** The system design MUST prevent any single Member State or system administrator from reconstructing a complete, consolidated European database of cardholders through the ECIES hub or its logs.
2.  **Security Constraint:** All transactions MUST guarantee **non-repudiation** (sender cannot deny sending a message) and **data privacy** (message content is only readable by the intended recipient CIA and the hub for routing/auditing).
3.  **Network Constraint:** All communication MUST comply with TESTA-II protocols and security policies.
4.  **Regulatory Constraint:** Message formats and data elements MUST comply with relevant EU regulations (e.g., 2016/799).

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Each Member State maintains its own accurate and up-to-date national registry of issued driver and tachograph cards.
*   **Assumption:** All participating CIAs possess and maintain valid digital certificates issued by a trusted PKI recognized within the TESTA-II domain.
*   **Dependency:** The availability and performance of the TESTA-II network are outside the control of this project but are critical to system operation.

### 3. System Features and Requirements

#### 3.1 Secure Message Exchange
**Description:** This feature handles the core secure communication between CIAs via the ECIES hub.
*   `FR-101` The system SHALL provide a secure (TLS 1.2+) web service endpoint for receiving XML messages from CIA Applications.
*   `FR-102` The system SHALL validate the digital signature and certificate of the sending entity for every incoming message.
*   `FR-103` The system SHALL route the message to the correct destination Member State's service endpoint based on message headers.
*   `FR-104` The system SHALL apply a digital signature and timestamp to all routed messages to ensure non-repudiation at the hub level.
*   `FR-105` The system SHALL maintain a complete, immutable audit log of every message transaction (message ID, sender, receiver, timestamp, type, result). The log MUST NOT contain the full cardholder data from the message payload.

#### 3.2 Driver Card Check
**Description:** Allows a CIA to inquire if a driver (identified by name, date of birth, etc.) holds a valid card in another Member State.
*   `FR-201` The system SHALL accept a `DriverCheckRequest` message containing driver identification data.
*   `FR-202` The system SHALL invoke the phonetic key service (`FR-501`) on driver name fields to generate search keys included in the request.
*   `FR-203` The system SHALL forward the request to the hub, which broadcasts it to all other connected Member State CIAs (or a targeted subset).
*   `FR-204` The system SHALL aggregate responses from queried CIAs into a single `DriverCheckResponse` message.
*   `FR-205` The response SHALL indicate for each responding Member State: a `Match`/`NoMatch` status and, in case of a match, only the card status (e.g., `Valid`, `Blocked`) and card number—NOT the full driver identity.

#### 3.3 Card Status Declaration
**Description:** Allows a CIA to notify all other Member States about a change in a card's status.
*   `FR-301` The system SHALL accept a `CardStatusUpdateRequest` message containing the card number, type, and new status (e.g., `Lost`, `Stolen`, `Withdrawn`).
*   `FR-302` The system SHALL validate that the requesting CIA is the issuer of the card in question.
*   `FR-303` The system SHALL broadcast the status update to all other Member State CIAs.
*   `FR-304` The system SHALL send a confirmation message back to the requesting CIA upon successful broadcast.

#### 3.4 Statistics and Reporting
**Description:** Provides administrators with views of system usage metrics.
*   `FR-401` The system SHALL generate daily, weekly, monthly, and yearly aggregated statistics (counts of message types by Member State, success/failure rates, average response times).
*   `FR-402` TCN Administrators SHALL be able to view statistics for all Member States.
*   `FR-403` CIA Administrators SHALL be able to view statistics only for their own Member State's transactions.
*   `FR-404` Statistics SHALL be presented via both on-screen tables and exportable reports (PDF, CSV).

#### 3.5 Phonetic Key Service
**Description:** A utility service to standardize name matching.
*   `FR-501` The system SHALL provide an algorithm (e.g., based on Soundex, Metaphone, or a defined EU standard) to generate a phonetic key from a textual name string.
*   `FR-502` The algorithm SHALL be configurable to support different European language characteristics.
*   `FR-503` The service SHALL be available as a library for integration into CIA national systems and as a function within the ECIES hub for request preprocessing.

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   `NFR-601` **Response Time:** 95% of all user-initiated requests (via GUI) SHALL return a response within **60 seconds**. This includes network latency, hub processing, and query broadcast/aggregation time.
*   `NFR-602` **System Throughput:** The hub SHALL be capable of processing a peak load of 100 concurrent message exchange transactions per second.

#### 4.2 Safety & Security Requirements
*   `NFR-701` **Authentication:** All access to the system (GUI or API) SHALL require strong authentication using TESTA-II recognized X.509 client certificates.
*   `NFR-702` **Authorization:** Role-Based Access Control (RBAC) SHALL be enforced. CIA users cannot access data or functions of another Member State.
*   `NFR-703` **Data Privacy:** Message payloads SHALL be encrypted end-to-end between originating and destination CIA applications. The hub SHALL decrypt only the routing headers.
*   `NFR-704` **Non-Repudiation:** Every message SHALL be digitally signed by its sender. The hub SHALL also sign all routed messages and acknowledgments.

#### 4.3 Availability Requirements
*   `NFR-801` The system SHALL be designed for **24 hours a day, 7 days a week** operation.
*   `NFR-802` The scheduled availability of the core hub services SHALL be 99.5% per calendar month, excluding planned maintenance windows communicated at least 72 hours in advance.

#### 4.4 Maintainability & Support Requirements
*   `NFR-901` All system components SHALL have comprehensive logging (INFO, WARN, ERROR, DEBUG levels).
*   `NFR-902` The system SHALL provide a health check endpoint for monitoring tools.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| Quality Assurance Manager | | | |