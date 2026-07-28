# Software Requirements Specification (SRS)
## TACHOnet System
**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the TACHOnet system. It serves as a comprehensive guide for stakeholders, developers, testers, and project managers, ensuring a common understanding of the system's capabilities, constraints, and goals.

#### 1.2 Document Conventions
- Requirements are uniquely identified (e.g., `FR-001`, `NFR-001`).
- **Bold** text highlights key terms or system components.
- *Italic* text denotes references to external documents or artifacts.
- `Monospace` text indicates data fields, code, or technical values.

#### 1.3 Project Scope
The TACHOnet system is a secure, distributed European network facilitating the exchange of tachograph card information between Member States' Card Issuing Authorities (CIAs). Its core purpose is to enable automated card status checks, declarations of card modifications, and statistical reporting **without** creating a consolidated central European database. The system acts as a message router and broker, ensuring data privacy and sovereignty for each participating nation.

**In-Scope:**
- Secure XML message exchange via the TESTA-II network.
- Routing of requests and aggregation of responses.
- System monitoring, logging, and statistical reporting.
- Administration interfaces for TCN and CIA Administrators.
- Management of Member State configurations and digital certificates.

**Out-of-Scope:**
- The internal business logic of Member State CIA applications.
- Physical tachograph card issuance or personalization.
- Direct end-user interfaces for drivers or enforcement officers (handled by national CIA applications).

#### 1.4 References
- *TCN XML Messaging Reference Guide*
- *TESTA-II Network Technical Specifications*
- *EU Regulation (EU) No 165/2014 on tachographs*

### 2. Overall Description

#### 2.1 Product Perspective
TACHOnet is a middleware system interfacing with external CIA applications from each EU Member State. It is dependent on the TESTA-II network for secure transport and relies on predefined XML schemas for all communications. The system is monitored via Microsoft Operations Manager (MOM) and uses SQL Reporting Services for statistics.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **CIA Application** | Automated system, interacts via XML/SOAP over TESTA-II. | Reliable, secure, and standards-compliant messaging interface. |
| **CIA Administrator** | Single point of contact per Member State, technical role. | Access to national usage statistics, configuration management for their CIA endpoint. |
| **TCN Administrator** | Central system operator, high-privilege role. | Full system monitoring, configuration of all Member States, performance dashboards, alert management. |
| **CIA User** (Indirect) | Clerk or enforcement officer within a Member State. | Uses national CIA application; performance and reliability of TACHOnet indirectly affect their work. |

#### 2.3 Operating Environment
- **Network:** TESTA-II (Trans-European Services for Telematics between Administrations).
- **Platform:** Microsoft Windows Server-based ecosystem.
- **Middleware:** Microsoft BizTalk Server for orchestration and messaging.
- **Database:** Microsoft SQL Server for transactional data, logging, and reporting.
- **Monitoring:** Microsoft Operations Manager (MOM).
- **Reporting:** SQL Server Reporting Services (SSRS).

#### 2.4 Design and Implementation Constraints
1. All cross-border communications **must** use the TESTA-II network.
2. Message formats **must** adhere to the *TCN XML Messaging Reference Guide*.
3. The system **must not** persist a complete, queryable European database of cardholder information.
4. The architecture **must** support the integration of 27+ Member State systems with varying technical maturity.

#### 2.5 Assumptions and Dependencies
- Member States will develop and maintain compatible CIA applications.
- TESTA-II network provides the required availability and security.
- Digital certificates for encryption and non-repudiation are managed and provided by competent authorities.
- The *TCN XML Messaging Reference Guide* is the definitive standard for all interfaces.

### 3. System Features and Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Message Handling & Processing
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-001** | The system shall receive encrypted XML/SOAP requests from CIA applications via the TESTA-II network. | High |
| **FR-002** | The system shall decrypt the incoming message and validate its XML syntax against the defined XSD schema. | High |
| **FR-003** | Upon receipt, the system shall assign a unique tracking identifier (`TCNRefId`) to the request and log the full original message. | High |
| **FR-004** | The system shall parse the request to identify the target Member State(s) based on the `IssuingMemberStateCode`(s) contained within. | High |
| **FR-005** | For each target Member State, the system shall construct a new valid XML request and forward it to the corresponding CIA Application URL. | High |
| **FR-006** | The system shall collect responses from each queried CIA application. | High |
| **FR-007** | The system shall implement a timeout mechanism (e.g., 30 seconds) for responses from each CIA. Late responses shall be handled according to a defined rule (e.g., logged but not included in the main reply). | High |
| **FR-008** | The system shall aggregate all received (and on-time) responses into a single, consolidated XML response message. | High |
| **FR-009** | The system shall encrypt and send the consolidated response back to the original requesting CIA application. | High |

##### 3.1.2 Request Types
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-010** | The system shall process **Card Status Check** requests (`GetCardStatus`). | High |
| **FR-011** | The system shall process **Issued Cards Check** requests (`GetIssuedCards`) to find cards issued to drivers with similar personal data. | High |
| **FR-012** | The system shall process **Card Status Modification** declarations (`DeclareCardStatus`) for lost, stolen, withdrawn, or confiscated cards. | High |
| **FR-013** | The system shall process **Card/Driving License Assignment** notifications (`NotifyCardAssignment`). | High |

##### 3.1.3 Administration & Monitoring
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-014** | The system shall provide a secure web interface for the **TCN Administrator** to view system health, message throughput, and error rates. | High |
| **FR-015** | The system shall provide a secure web interface for the **CIA Administrator** to view statistics and reports relevant to their own Member State only. | Medium |
| **FR-016** | The TCN Administrator shall be able to configure and manage the list of Member States, including their CIA endpoints, digital certificates, and contact information. | High |
| **FR-017** | The system shall generate and make available pre-defined statistical reports (e.g., requests per country, error rates, response times) via SQL Reporting Services. | Medium |
| **FR-018** | The system shall integrate with Microsoft Operations Manager (MOM) to raise alerts for critical failures, performance degradation, or security events. | High |

##### 3.1.4 Error Handling
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-019** | For syntactically invalid incoming messages, the system shall immediately return a negative acknowledgment (NegativeReceipt) to the sender and alert the TCN Administrator. | High |
| **FR-020** | In case of network failure when sending to a CIA, the system shall retry the transmission up to 3 times with a configurable delay between attempts. | High |
| **FR-021** | All errors and warnings shall be logged with sufficient detail (timestamp, `TCNRefId`, involved parties, error code) for auditing and troubleshooting. | High |

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
| ID | Requirement |
| :--- | :--- |
| **NFR-001** | The end-to-end processing time for a request (from receipt to sending the final response) shall be under 1 minute for 95% of transactions under normal load, regardless of concurrent background tasks. |
| **NFR-002** | The system shall support a peak load of [TBD] concurrent transactions. |

##### 3.2.2 Reliability & Availability
| ID | Requirement |
| :--- | :--- |
| **NFR-003** | The system shall be designed for an operational lifetime of 10+ years with minimal unplanned interruptions. |
| **NFR-004** | The system shall achieve 99.5% availability, 24 hours a day, 7 days a week, excluding planned maintenance windows. |

##### 3.2.3 Security
| ID | Requirement |
| :--- | :--- |
| **NFR-005** | All messages in transit between TACHOnet and CIA applications **must** be encrypted using mutually recognized digital certificates. |
| **NFR-006** | The system shall provide non-repudiation of origin and receipt for all messages. |
| **NFR-007** | Access to administrative functions shall be strictly controlled via role-based access control (RBAC). |
| **NFR-008** | All system access shall require authentication. Passwords shall be stored as hashed values. |

##### 3.2.4 Usability
| ID | Requirement |
| :--- | :--- |
| **NFR-009** | The administrative web interfaces shall be intuitive, require minimal training, and provide clear guidance and feedback to users. |
| **NFR-010** | User actions with significant consequences (e.g., disabling a Member State) shall require confirmation. |

##### 3.2.5 Supportability
| ID | Requirement |
| :--- | :--- |
| **NFR-011** | The system shall be designed to be easily maintainable and extensible (e.g., to add new message types). |
| **NFR-012** | The system shall be capable of migrating to new hardware and software platforms with reasonable effort. |

### 4. External Interface Requirements

#### 4.1 User Interfaces
- **TCN Administrator Portal:** Web-based dashboard for monitoring, configuration, and global reporting.
- **CIA Administrator Portal:** Web-based portal restricted to national statistics and endpoint status.

#### 4.2 Hardware Interfaces
The system will interface with standard server hardware, load balancers, and network infrastructure within the hosting data center.

#### 4.3 Software Interfaces
1.  **TESTA-II Network:** Interface via web services (SOAP/HTTPS) as per TESTA-II specifications.
2.  **Member State CIA Applications:** Interface via defined XML/SOAP web service endpoints.
3.  **Microsoft SQL Server:** For all data persistence.
4.  **Microsoft Operations Manager (MOM):** Via MOM agents and management packs for monitoring.
5.  **SQL Server Reporting Services (SSRS):** For generating and rendering statistical reports.

#### 4.4 Communications Interfaces
- Primary Protocol: SOAP over HTTPS via TESTA-II.
- Encryption: X.509 digital certificates.
- Message Format: XML compliant with the *TCN XML Messaging Reference Guide*.

### 5. System Data Requirements

#### 5.1 Logical Data Model
Key entities include:
- **Transaction:** Core record of each request/response cycle. (`TCNRefId`, `RequestType`, `SenderCIA`, `Timestamp`, `Status`)
- **MemberState:** Configuration for each participating country. (`CountryCode`, `CIAApplicationURL`, `DigitalCertificate`, `IsActive`)
- **MessageLog:** Immutable audit log of all raw messages. (`MessageID`, `OriginalMessage`, `Direction`, `Timestamp`)
- **UserAccount:** For TCN and CIA Administrators. (`Username`, `Role`, `MemberState`, `PasswordHash`)
- **StatisticsReport:** Generated report metadata. (`ReportID`, `Period`, `ReportType`, `GeneratedDate`)

*(Note: The `Card` entity is **not** persisted centrally within TACHOnet; card data exists only transiently in messages and in the national CIA databases.)*

#### 5.2 Data Retention
- Transactional data and message logs shall be retained in the operational database for a period of **[Duration TBD - See Undecided Issues]** before being archived to long-term storage.
- Statistical aggregate data shall be retained indefinitely for trend analysis.

### 6. Other Non-Functional Requirements

#### 6.1 Compliance
The system shall comply with all relevant EU regulations concerning data protection (e.g., GDPR principles), tachograph legislation, and cross-border data exchange.

### 7. Appendices

#### 7.1 Glossary
- **CIA:** Card Issuing Authority. National authority responsible for issuing tachograph cards.
- **TCN:** TACHOnet.
- **TESTA-II:** Trans-European Services for Telematics between Administrations, the secure EU communication network.
- **TCNRefId:** A unique identifier generated by TACHOnet for tracking each transaction.

#### 7.2 Undecided Issues (Open Items)
1.  The specific duration for keeping detailed message logs in the operational tracking database.
2.  The exact set of BizTalk monitoring rules and thresholds to be configured in Microsoft Operations Manager.
3.  Firewall configuration specifications between the TACHOnet application servers and the central MOM console.
4.  The data model and interface for handling multiple hierarchical contact points per Member State.
5.  Requirements for supporting character set transliterations beyond the current Greek/Latin requirement (e.g., Cyrillic).
6.  The detailed operational procedure for securely removing a Member State from the live TACHOnet configuration.

#### 7.3 Risk Management
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Member State CIA non-compliance | Medium | High | Provide clear specs, a reference implementation, and a mandatory conformance testing phase before go-live. |
| Performance degradation under load | Low | High | Design for scalability (load-balanced front ends), implement continuous monitoring, and define performance benchmarks. |
| Security breach of message flow | Low | Critical | Enforce end-to-end encryption, regular certificate audits, and strict access controls to administrative functions. |
| TESTA-II network outage | Low | Critical | Implement graceful degradation: queue outgoing messages and provide clear status alerts to administrators. |