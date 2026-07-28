# Software Requirements Specification (SRS)
## TACHOnet System
**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the TACHOnet system. It serves as a formal agreement between stakeholders, developers, and project managers, providing a comprehensive description of the system's intended capabilities, constraints, and external interfaces. The primary audience includes the development team, quality assurance, TCN administrators, and Member State Card Issuing Authority (CIA) representatives.

#### 1.2 Scope
TACHOnet is a secure, distributed network system facilitating information exchange between European Member States' Card Issuing Authorities (CIAs) concerning driver smart cards and tachograph cards. The system's core purpose is to support administrative and enforcement tasks while explicitly preventing the technical possibility of reconstructing a consolidated European database of card information.

**In-Scope Elements:**
*   Secure, XML-based message exchange between CIAs via the TACHOnet hub.
*   Administrative functions: checking a driver's issued cards, verifying tachograph card status, and declaring card status modifications (e.g., lost, stolen).
*   Generation and presentation of system usage statistics for monitoring.
*   Management of Member State configurations and system parameters.
*   Provision of phonetic search key computation and transliteration services (initially for Greek/Latin scripts).

**Out-of-Scope Elements:**
*   User management *within* a Member State's CIA (management of clerks, enforcers).
*   Business logic validation for card status transitions (remains the responsibility of each Member State's internal systems).
*   Research and development of new cryptographic or transliteration algorithms.
*   Any functionality that could enable the reconstruction of a pan-European cardholder database.
*   Direct intervention in the internal organizational structures of Member States.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **CIA** | Card Issuing Authority. The national authority in a Member State responsible for issuing driver/tachograph cards. |
| **TCN** | TACHOnet. The central system described in this document. |
| **TESTA-II** | Trans-European Services for Telematics between Administrations. The secure private network infrastructure mandated for communication. |
| **MOM** | Microsoft Operations Manager. A monitoring and management system. |
| **Non-Repudiation** | Assurance that a sender cannot deny having sent a message and that the recipient cannot deny having received it. |

#### 1.4 References
*   [To be populated with relevant EU regulations, XML schema definitions (XSD), TESTA-II compliance documents, and security policy documents.]

#### 1.5 Overview
The remainder of this SRS is structured as follows:
*   **Section 2:** Provides a general description of the product, its perspective, functions, user characteristics, and constraints.
*   **Section 3:** Specifies detailed functional and non-functional requirements.
*   **Appendix A:** May contain supplementary information such as data dictionaries or preliminary designs.

### 2. Overall Description

#### 2.1 Product Perspective
TACHOnet is an independent middleware system acting as a secure message broker. It interfaces externally with:
1.  **CIA Applications:** One per Member State, which connect via the TESTA-II network.
2.  **TESTA-II Network:** The mandatory communication infrastructure providing a secure backbone.
3.  **Central Monitoring Console (MOM):** For system health and performance monitoring (configuration details pending).

The system is not a database repository but a message router with logging and statistical capabilities.

#### 2.2 Product Functions
The high-level functions of TACHOnet are:
1.  **Message Exchange Hub:** Route secure XML messages between CIA applications.
2.  **Administrative Query Processor:** Handle requests for driver card lists and tachograph card status checks.
3.  **Status Declaration Handler:** Accept and broadcast notifications of card status changes.
4.  **Statistics Engine:** Generate aggregate data on message volume, types, errors, and response times.
5.  **Configuration Manager:** Maintain system parameters and Member State connection details.
6.  **Support Service Provider:** Compute phonetic search keys and perform script transliteration.

#### 2.3 User Characteristics
| Actor | Description | Technical Skill Level |
| :--- | :--- | :--- |
| **CIA Application** | Automated system representing a Member State. Sends/receives XML messages. | High (System-to-System) |
| **CIA User (Clerk/Enforcer)** | End-user within a Member State using the national CIA application. Interacts indirectly with TACHOnet. | Variable (Assumed low for TACHOnet design) |
| **CIA Administrator** | Single point of contact per Member State. Configures the national CIA application connection and views TACHOnet usage statistics for their state. | Medium-High |
| **TCN Administrator** | Central operator responsible for the overall health, configuration, and monitoring of the TACHOnet hub. | High |

#### 2.4 Constraints
1.  **Regulatory & Infrastructure:** Must operate exclusively over the TESTA-II network.
2.  **Security:** Must guarantee non-repudiation, data privacy, and integrity for all transactions using approved cryptographic standards.
3.  **Compatibility:** Must support heterogeneous technical environments across all EU Member States.
4.  **Standards Compliance:** Must adhere to existing, specified XML messaging schemas and communication protocols.
5.  **Longevity:** Must be designed for maintainability and extensibility to ensure operational capability for many years without major architectural redesign.
6.  **Architectural:** The system design must actively prevent the permanent storage or reconstruction of a consolidated European card database.

#### 2.5 Assumptions and Dependencies
*   Each Member State will have a single, functional CIA Application capable of connecting via TESTA-II and processing the defined XML messages.
*   Member States are responsible for the validity and correctness of the data they send.
*   The TESTA-II network provides a baseline level of availability and security.
*   Success is dependent on all Member States implementing compatible interfaces.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Message Exchange (ME)
*   **ME-1:** The system shall send and receive XML messages conforming to the official TACHOnet XSD schema via the TESTA-II network.
*   **ME-2:** The system shall validate the syntactic and cryptographic integrity of every incoming message before processing.
*   **ME-3:** The system shall route an incoming message from a source CIA to the correct destination CIA application based on message headers.
*   **ME-4:** The system shall provide guaranteed, once-only delivery of messages.
*   **ME-5:** The system shall generate a unique tracking ID and timestamp for every message transaction, storing it for an auditable period *(duration TBD)*.

##### 3.1.2 Administrative Queries (AQ)
*   **AQ-1:** Upon receiving a valid "Driver Card List Request" from a CIA, the system shall forward the request to the CIA of the issuing Member State identified in the request.
*   **AQ-2:** Upon receiving a valid "Tachograph Card Status Request" from a CIA, the system shall forward the request to the CIA of the issuing Member State identified in the request.
*   **AQ-3:** The system shall relay the corresponding response (card list or status) from the issuing CIA back to the requesting CIA.

##### 3.1.3 Status Declaration (SD)
*   **SD-1:** Upon receiving a valid "Card Status Modification Declaration" (e.g., lost, stolen, defective) from an issuing CIA, the system shall broadcast this declaration to all other Member State CIAs.

##### 3.1.4 Statistics and Monitoring (ST)
*   **ST-1:** The system shall automatically generate aggregate statistics, including but not limited to: message counts by type and Member State, average response times, and error rates.
*   **ST-2:** The CIA Administrator shall be able to view statistical reports pertaining to their own Member State's message activity via a secure web interface or API.
*   **ST-3:** The TCN Administrator shall be able to view system-wide statistical reports and real-time dashboards.
*   **ST-4:** The system shall generate alerts for critical system errors (e.g., service downtime, persistent delivery failures).

##### 3.1.5 Support Services (SS)
*   **SS-1:** The system shall expose a service that computes a standardized phonetic search key from a provided driver's name (according to a specified algorithm).
*   **SS-2:** The system shall expose a transliteration service to convert text between Greek and Latin scripts.

##### 3.1.6 System Administration (SA)
*   **SA-1:** The TCN Administrator shall be able to add, modify, or deactivate Member State configurations (e.g., connection endpoints, cryptographic certificates).
*   **SA-2:** The TCN Administrator shall be able to manage global system parameters.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
*   **PER-1:** For enforcement-related requests (Tachograph Card Status Request), the system's processing and routing latency (excluding network transit and destination CIA processing) shall be under **1 minute** for the 95th percentile of transactions.
*   **PER-2:** The system shall support peak loads of **[X] concurrent messages** and **[Y] messages per hour]** (values TBD based on Member State estimates).

##### 3.2.2 Availability & Reliability
*   **REL-1:** The system shall achieve **24x7 operational availability** with a target uptime of 99.5% in any calendar month, excluding scheduled maintenance windows.
*   **REL-2:** The system shall be designed for high reliability, targeting fewer than **Z significant interruptions** in the first operational year.

##### 3.2.3 Security
*   **SEC-1:** All messages shall be digitally signed and encrypted using EU-approved algorithms to ensure non-repudiation, confidentiality, and integrity.
*   **SEC-2:** Access to administrative functions (statistics, configuration) shall be protected by strong authentication and role-based access control (RBAC).
*   **SEC-3:** All system logs and message tracking data shall be protected from unauthorized access, modification, or deletion.

##### 3.2.4 Maintainability
*   **MNT-1:** The system shall be designed modularly to allow for updates to individual components (e.g., transliteration rules, monitoring agents) without a full system redeployment.

#### 3.3 External Interface Requirements

##### 3.3.1 CIA Application Interface
*   **Protocol:** Web Services (SOAP/HTTPS) or secure file transfer over TESTA-II.
*   **Data Format:** XML strictly validated against the official TACHOnet XSD.
*   **Authentication:** Mutual TLS (X.509 certificates) or equivalent TESTA-II mandated mechanism.

##### 3.3.2 Administrator Interfaces
*   **TCN Admin Console:** Secure web-based application for full system administration.
*   **CIA Admin Portal:** Restricted web-based interface for Member State-specific statistics and connection parameter viewing.

#### 3.4 Undecided / TBD Issues
1.  The retention period for message tracking data in the operational database.
2.  The specific configuration of BizTalk monitoring rules for integration with the central MOM console.
3.  The detailed firewall rule set between TACHOnet application servers and the central monitoring network.
4.  The final decision on whether monitoring agents will push data to MOM or if MOM will pull/poll data from TACHOnet servers.
5.  The implementation roadmap for adding transliteration standards for scripts beyond Greek and Latin.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| Quality Assurance | | | |