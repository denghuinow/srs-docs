# Software Requirements Specification (SRS)
## TACHOnet System
### Version 1.0

**Prepared by:** [Name/Organization]
**Date:** [Date]
**Document Status:** Draft / For Review / Approved

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the TACHOnet system. The intended audience includes project stakeholders, system architects, developers, testers, and the commissioning authority, DG TREN. This document serves as the definitive source of requirements for the system's design, implementation, and verification.

### 1.2 Scope
TACHOnet is a central messaging hub that facilitates the secure exchange of information regarding driver tachograph smart cards between the Card Issuing Authorities (CIAs) of European Union Member States.

**In-Scope:**
*   Acting as a Single Point of Contact (SPOC) for cross-border queries and notifications.
*   Routing standardized XML messages between Member State CIAs.
*   Providing web-based utility services (phonetic search, transliteration).
*   Generating and presenting system usage statistics.
*   Ensuring secure, reliable, and logged message exchange with non-repudiation.
*   Maintaining configuration for Member State SPOCs.

**Out-of-Scope:**
*   Managing individual CIA user accounts within Member States.
*   Storing or reconstructing a consolidated European database of card holders.
*   Imposing specific technology constraints on Member States' internal backend systems.
*   Validating business rules (e.g., permissible card status transitions) for Member States.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **CIA** | Card Issuing Authority. The national authority in an EU Member State responsible for issuing driver tachograph cards. |
| **DG TREN** | Directorate-General for Transport and Energy (European Commission). |
| **SPOC** | Single Point of Contact. The designated CIA system for a Member State that connects to TACHOnet. |
| **TESTA-II** | Trans-European Services for Telematics between Administrations. The secure private network used for communication. |
| **TCN** | TACHOnet. The central system described in this document. |
| **Phonex** | A phonetic algorithm for indexing names by their sound. |
| **Non-repudiation** | The assurance that a message sender cannot deny having sent the message and that the recipient cannot deny having received it. |

### 1.4 References
*   EU Regulation (EC) No 561/2006 & 165/2014 (concerning tachographs).
*   Technical Specifications for TACHOnet XML Message Formats (External Document).
*   TESTA-II Network Security and Usage Policies.

### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Overall description of the product, its users, and operating environment.
*   **Section 3:** Specific system requirements, detailing functional, interface, and non-functional requirements.

## 2. Overall Description

### 2.1 Product Perspective
TACHOnet is an independent, central system that operates as a messaging hub. It mediates communication between sovereign, heterogeneous national systems. It is not a master database but a router and processor of requests and notifications.

**System Interfaces:**
```
[Member State Backend System] <--> [CIA Application/SPOC] <--TESTA-II/XML--> [TACHOnet Hub] <--TESTA-II/XML--> [Other CIA SPOCs]
                                                                      ^
                                                                      |
                                                              [Secure Web Portal]
                                                                      |
                                                        [CIA User, CIA Admin, TCN Admin]
```

### 2.2 Product Functions (Summary)
1.  **Message Routing & Processing:** Receive, validate, route, and deliver XML messages between CIAs.
2.  **Card Information Services:** Process queries for card existence and status.
3.  **Card Status Management:** Process notifications for card status changes (lost, stolen, etc.).
4.  **License-Card Assignment Notification:** Forward notifications linking a tachograph card to a driving license.
5.  **Data Utility Services:** Provide Phonetic (Phonex) key generation and script transliteration (e.g., Greek to Latin).
6.  **Reporting & Statistics:** Generate logs and aggregate usage data for administrators.
7.  **System Administration:** Manage Member State SPOC configurations and monitor system health.

### 2.3 User Characteristics
| User Class | Description | Technical Proficiency | Key Activities |
| :--- | :--- | :--- | :--- |
| **CIA Application** | Automated system representing a Member State. | N/A (System-to-System) | Send/receive XML messages in bulk, often triggered by backend processes. |
| **CIA User (Clerk/Enforcer)** | Individual operator within a national CIA. | Moderate. Uses web forms and may trigger backend processes. | Use web utilities (Phonex), initiate card checks via national interface. |
| **CIA Administrator** | Single designated admin per Member State. | Moderate. Understands basic statistics. | Access TACHOnet usage statistics for their own Member State via web portal. |
| **TCN Administrator** | Central system operator. | High. Skilled in system monitoring and configuration. | Manage SPOC accounts, monitor message flows, generate system-wide reports, configure system parameters. |

### 2.4 Constraints
*   **Network:** Must operate exclusively over the TESTA-II network.
*   **Protocol & Format:** Must adhere to predefined XML message formats and technical communication rules.
*   **Architecture:** The system's design must prevent any entity, including the TCN Administrator, from technically reconstructing a consolidated European database of all card holders from the message traffic or logs.
*   **Software:** Should utilize pre-existing or commercial off-the-shelf (COTS) software components where feasible to reduce development risk and cost.

### 2.5 Assumptions and Dependencies
*   Each EU Member State will designate one SPOC CIA to connect to TACHOnet.
*   Member States are responsible for developing or adapting their internal CIA Application to generate/consume the standard TACHOnet XML messages.
*   Member State backend systems will maintain high availability (24x7) to meet the 1-minute response time requirement for enforcement-related queries.
*   The predefined XML schema and TESTA-II network specifications are stable and will be provided.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 CIA Application Interface
*   **Type:** System-to-System (S2S), Machine-Readable.
*   **Communication Protocol:** Secure messaging over TESTA-II.
*   **Data Format:** Well-formed XML, conforming to the official TACHOnet XML Schema Definition (XSD).
*   **Security:** All messages must be digitally signed for non-repudiation and encrypted for confidentiality using TESTA-II and application-level mechanisms as specified.
*   **Interaction Pattern:** Primarily request/response and asynchronous notifications.

#### 3.1.2 Web Portal Interface
*   **Type:** Human-Readable, Web-based.
*   **Access:** Via HTTPS over TESTA-II or a similarly secured channel.
*   **User Roles:** Distinct login and views for CIA User, CIA Administrator, and TCN Administrator.
*   **Content:** Forms for utility services (Phonex, transliteration) and dashboards/reports for statistics.

### 3.2 Functional Requirements

#### **FR-1: Message Exchange Core**
*   **FR-1.1:** The system shall receive an XML message from a source CIA SPOC.
*   **FR-1.2:** The system shall validate the syntactic and semantic structure of the incoming XML message against the official XSD and business rules.
*   **FR-1.3:** The system shall route the message to the one or more target CIA SPOCs based on the message type and content (e.g., a card check request is routed to the issuing Member State).
*   **FR-1.4:** The system shall deliver the XML message to the target CIA SPOC's designated endpoint.
*   **FR-1.5:** The system shall manage message acknowledgements (technical receipt) and delivery statuses.

#### **FR-2: Card Information Services**
*   **FR-2.1 - Multi-Issue Check:** Upon receiving a `CardExistenceQuery` for a driver's personal data, the system shall route the query to all other Member State CIAs and aggregate their `CardExistenceResponse` messages (indicating yes/no) for return to the requester.
*   **FR-2.2 - Card Status Check:** Upon receiving a `CardStatusQuery` for a specific card number, the system shall route the query to the CIA of the Member State that issued the card and forward the `CardStatusResponse` (e.g., VALID, LOST, STOLEN, EXPIRED) back to the requester.

#### **FR-3: Card Status Management**
*   **FR-3.1 - Status Declaration:** Upon receiving a `CardStatusUpdate` notification (e.g., card reported lost), the system shall route the notification to all other Member State CIAs.

#### **FR-4: License-Card Assignment Notification**
*   **FR-4.1:** Upon receiving a `LicenseCardAssignment` notification, the system shall route the notification to the CIA of the Member State that issued the driving license referenced in the message.

#### **FR-5: Data Utility Services (Web Portal)**
*   **FR-5.1 - Phonex Generation:** The system shall provide a web form where a user can input a name (e.g., "Smith") and receive the corresponding Phonex phonetic code.
*   **FR-5.2 - Transliteration:** The system shall provide a web form where a user can input text in a supported script (e.g., Greek) and receive the transliterated text in US-ASCII.

#### **FR-6: Logging and Non-Repudiation**
*   **FR-6.1:** The system shall create an immutable log record for every message exchanged, containing at minimum: timestamp, message ID, sender CIA, receiver CIA(s), message type, and a secure hash of the message content.
*   **FR-6.2:** Logs shall be retained for a period defined by regulatory requirements (e.g., 5 years) and be cryptographically protected against tampering.

#### **FR-7: Reporting and Statistics**
*   **FR-7.1:** The system shall generate aggregated, anonymized usage statistics (e.g., number of queries per message type per CIA, system uptime).
*   **FR-7.2 - CIA Admin View:** The CIA Administrator shall be able to view statistics related only to their own Member State's message traffic.
*   **FR-7.3 - TCN Admin View:** The TCN Administrator shall be able to view system-wide statistics and generate custom reports within the bounds of privacy constraints (see NFR-2).

#### **FR-8: System Administration**
*   **FR-8.1 - SPOC Management:** The TCN Administrator shall be able to register, configure, enable, and disable CIA SPOC endpoints (URL, certificates).
*   **FR-8.2 - Monitoring:** The system shall provide a dashboard for the TCN Administrator showing system health, queue status, and error alerts.

### 3.3 Non-Functional Requirements

#### **NFR-1: Performance**
*   **NFR-1.1:** The central TACHOnet hub shall process and route a received message to the next hop within 10 seconds under normal load.
*   **NFR-1.2:** The end-to-end response time for an enforcement-related query (e.g., Card Status Check) from the initiating CIA to the receipt of the response shall be less than 1 minute. *[This is dependent on Member State system responsiveness.]*
*   **NFR-1.3:** The web portal interfaces shall render and respond to user interactions within 3 seconds.

#### **NFR-2: Security & Privacy**
*   **NFR-2.1:** All data in transit between CIAs and TACHOnet shall be encrypted using industry-standard protocols (e.g., via TESTA-II and WS-Security).
*   **NFR-2.2:** All messages shall be digitally signed to guarantee non-repudiation of origin and receipt.
*   **NFR-2.3 (Critical Privacy Constraint):** The system shall be designed and implemented such that it is **technically impossible** for any user, including the TCN Administrator with full system access, to query, extract, or reconstruct a complete dataset of all tachograph cards or drivers across Europe from the system's logs, messages, or databases.
*   **NFR-2.4:** Access to the web portal shall be governed by role-based access control (RBAC) with strong authentication.

#### **NFR-3: Reliability & Availability**
*   **NFR-3.1:** The TACHOnet central system shall achieve 99.5% operational availability per calendar month, excluding scheduled maintenance windows.
*   **NFR-3.2:** The system shall be tolerant to malformed but non-malicious input messages, handling them gracefully with appropriate error responses to the sender without crashing.
*   **NFR-3.3:** Message queues shall be persistent, ensuring no message is lost in case of a subsystem failure.

#### **NFR-4: Supportability**
*   **NFR-4.1:** The system shall be designed modularly to allow for the replacement of the underlying network communication layer (e.g., migration from TESTA-II to a successor network).
*   **NFR-4.2:** The system shall be deployable on new hardware or updated operating system versions with minimal re-engineering.
*   **NFR-4.3:** All configuration shall be external to the application code.

#### **NFR-5: Compatibility**
*   **NFR-5.1:** The system shall communicate successfully with CIA Applications regardless of their underlying technology stack (Java, .NET, etc.), relying solely on the standardized XML interface.
*   **NFR-5.2:** The web portal shall be accessible from common web browsers (e.g., latest versions of Chrome, Firefox, Edge).

### 3.4 System Priorities
| Requirement Category | Priority | Justification |
| :--- | :--- | :--- |
| Core Messaging (FR-1, FR-2, FR-3) | **High (Mandatory)** | Fundamental to the system's purpose of cross-border information exchange. |
| Security & Privacy (NFR-2) | **High (Mandatory)** | Legal and regulatory imperative, especially the non-consolidation principle. |
| Reliability (NFR-3) | **High** | Required for operational trust and effectiveness in enforcement scenarios. |
| Utility Services (FR-5) | **Medium** | Supports data quality and interoperability. |
| Reporting (FR-7) | **Medium/Low** | Important for oversight and monitoring but not core to real-time operations. |

---
*Document End*