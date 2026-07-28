# Software Requirements Specification (SRS)
## For: CDN Peering Federation System (CPFS)
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the CDN Peering Federation System (CPFS). The CPFS is a software infrastructure layer designed to enable autonomous Content Delivery Networks (CDNs) to form dynamic, cooperative federations for the purpose of sharing resources to handle sudden load spikes (e.g., flash crowds) and scale capacity. This SRS is intended for use by the project stakeholders, developers, testers, and project managers to guide the design, implementation, and verification of the system.

### 1.2 Scope
The CPFS coordinates content delivery across multiple independent CDN providers by virtualizing them into a single logical federation. Its scope includes:
*   Detecting overload conditions within a participating CDN.
*   Facilitating the discovery, negotiation, and establishment of peering arrangements between CDNs.
*   Managing the operational lifecycle of a peering arrangement, including request redirection and data exchange.
*   Terminating peering arrangements based on predefined conditions.

**Out of Scope:**
*   Managing or replacing the internal proprietary operations, routing algorithms, or caching strategies of any individual CDN.
*   Direct interaction with end-users or content providers.
*   Billing or financial settlement between CDN providers (though accounting data is exchanged).
*   Guaranteeing the performance or resources of any individual CDN provider.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **CDN** | Content Delivery Network. A distributed network of servers that delivers web content based on geographic proximity. |
| **CPFS** | CDN Peering Federation System. The system described in this document. |
| **Primary CDN** | The CDN experiencing load stress that initiates a peering request. |
| **Peer CDN** | A CDN that offers resources to a Primary CDN. |
| **Peering Arrangement** | A formalized, temporary agreement between CDNs to share resources, governed by policies and SLAs. |
| **Mediator** | A CPFS component responsible for brokering peering agreements. |
| **Peering Agent (PA)** | A CPFS component deployed within a CDN that acts on its behalf in the federation. |
| **Service Registry** | A CPFS component that maintains a directory of CDNs available for peering and their advertised capabilities. |
| **SLA** | Service Level Agreement. A contract defining the expected level of service. |
| **Flash Crowd** | A sudden, dramatic increase in traffic to a specific website or service. |

### 1.4 References
*   Design inspiration from related systems: CoDeeN, CoralCDN, MotusNet.
*   Project Charter and Vision Document.
*   IEEE Std 830-1998: Recommended Practice for Software Requirements Specifications.

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, security, and design constraints.

## 2. Overall Description

### 2.1 Product Perspective
The CPFS is a middleware layer that sits atop existing, autonomous CDN infrastructures. It interacts with CDN components via defined interfaces but operates as a separate logical system. The CPFS virtualizes multiple CDNs into a cooperative federation, allowing them to appear as a unified, larger-capacity delivery network for handling transient overload conditions.

### 2.2 Product Functions (High-Level)
1.  **Overload Detection & Triggering:** Monitor CDN state and automatically initiate peering when overload thresholds are breached.
2.  **Peer Discovery & Selection:** Discover potential peer CDNs with available resources that match policy requirements.
3.  **Policy Negotiation & Agreement:** Facilitate the exchange and agreement on service requirements, policies, and SLAs between CDNs.
4.  **Peering Establishment:** Configure the necessary protocols and pathways for request redirection and content replication between peered CDNs.
5.  **Operational Management:** During an active peering arrangement, redirect user requests, manage content replication, and exchange operational/accounting data.
6.  **Peering Lifecycle Management:** Monitor peering health, and disband or renegotiate arrangements based on termination conditions (e.g., load normalizes, SLA violation).

### 2.3 User Characteristics
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **CDN Operator (Initiator)** | Administrators of a CDN under load stress. | Technical experts. Primary goal: maintain their own SLA by acquiring external resources. Interact with the system to approve/initiate peering and monitor status. |
| **CDN Operator (Contributor)** | Administrators of a CDN with surplus resources. | Technical experts. Primary goal: monetize/utilize idle capacity without jeopardizing their own performance. Interact with the system to set peering policies and approve/reject peering requests. |
| **System Administrator** | Responsible for deploying and maintaining the CPFS infrastructure (Mediator, Registry). | Deep technical knowledge of the CPFS and network operations. Does not represent a single CDN. |

### 2.4 Constraints
1.  **Information Opacity:** The CPFS cannot rely on full visibility or control over the internal load, cost, or performance metrics of participating CDNs. It must operate on limited, voluntarily shared data.
2.  **Modeling Heuristics:** Implementation models for critical attributes (e.g., geographic proximity, network latency between CDN edges) will be heuristic-based due to the lack of complete network topology data.
3.  **Autonomy Preservation:** The system must not dictate the internal operational decisions of any CDN. Peering is voluntary and advisory.
4.  **Test Bed Deployment:** The prototype must be deployable and testable on a global, real-world distributed test bed such as PlanetLab.

### 2.5 Assumptions and Dependencies
*   **Assumption:** Participating CDNs have existing components (web servers, policy stores) with which the CPFS Peering Agent can interface using standard web services technologies (HTTP/S, REST, etc.).
*   **Assumption:** Underlying network connectivity (TCP/IP) exists between Peering Agents of different CDNs.
*   **Dependency:** The design and protocols will be inspired by concepts from prior research systems (CoDeeN, Coral).
*   **Assumption:** CDN providers are motivated to participate for mutual benefit during asymmetric load events.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 Software Interfaces (APIs)
*   **PA-to-CDN Interface:** The Peering Agent must provide a RESTful API for the local CDN's components to:
    *   Report health/load metrics (e.g., `POST /api/v1/metrics`).
    *   Receive redirection instructions (e.g., `GET /api/v1/redirect-rules`).
    *   Submit local peering policies (e.g., `PUT /api/v1/policy`).
*   **PA-to-Mediator/Registry Interface:** The Peering Agent must communicate with central CPFS components using a secure, defined protocol (e.g., HTTPS with JSON payloads) for:
    *   Registration and advertisement of capabilities.
    *   Participation in negotiation sequences.
    *   Reporting peering session data.
*   **PA-to-PA Interface:** Peering Agents of different CDNs must establish a direct, secure channel (e.g., mutually authenticated TLS) for:
    *   Exchanging real-time request redirection traffic.
    *   Transferring accounting records.
    *   Sending heartbeat/health-check messages during an active peering session.

#### 3.1.2 Communication Protocols
*   All external communication will use standard Internet protocols (TCP/IP, HTTP/1.1 or HTTP/2).
*   Internal messaging between CPFS components may use a more efficient protocol (e.g., gRPC, AMQP) but must be encapsulated for transport over the test bed network.

### 3.2 Functional Requirements

#### **FR-1: Overload Detection and Peering Trigger**
*   **FR-1.1:** The Peering Agent (PA) shall monitor key performance indicators (KPIs) from its local CDN (e.g., request rate, server load, cache miss ratio) via the PA-to-CDN interface.
*   **FR-1.2:** The PA shall compare monitored KPIs against configurable thresholds defined in the local CDN's peering policy.
*   **FR-1.3:** When a threshold is breached, the PA shall automatically trigger the peering process by notifying the CPFS Mediator.
*   **FR-1.4:** The system shall support a manual trigger initiated by the CDN Operator (Initiator).

#### **FR-2: Resource and Peer Discovery**
*   **FR-2.1:** The Service Registry shall allow CDNs (via their PA) to register and advertise their peering capabilities (e.g., available bandwidth, geographic regions, supported content types).
*   **FR-2.2:** The Mediator shall query the Service Registry to discover candidate peer CDNs that match the high-level requirements submitted by the Primary CDN's PA.
*   **FR-2.3:** The discovery process shall filter candidates based on heuristic models of geographic and network proximity.

#### **FR-3: Policy Negotiation and Agreement Formation**
*   **FR-3.1:** The Mediator shall facilitate a negotiation protocol between the Primary PA and one or more candidate Peer PAs.
*   **FR-3.2:** The negotiation shall involve the exchange of proposed SLA terms, including:
    *   Resource commitment (e.g., max bandwidth, request/sec).
    *   Duration of peering.
    *   Acceptable content types.
    *   Redirection protocol details.
    *   Accounting and reporting frequency.
*   **FR-3.3:** The Mediator shall generate a formal **Peering Agreement** document upon successful negotiation, signed (cryptographically) by all participating PAs.
*   **FR-3.4:** The system shall allow CDN Operators to manually approve or reject a negotiated agreement before it becomes active.

#### **FR-4: Peering Establishment and Configuration**
*   **FR-4.1:** Upon agreement, the system shall instruct participating PAs to establish direct communication channels (PA-to-PA) as specified in the agreement.
*   **FR-4.2:** The Primary PA shall configure its local CDN's edge servers (via the PA-to-CDN interface) with rules to redirect a defined portion of incoming requests to the Peer PA's endpoint.
*   **FR-4.3:** The Peer PA shall be configured to accept and service redirected requests from the Primary CDN.

#### **FR-5: Operational Management of Active Peering**
*   **FR-5.1:** During an active peering session, the Primary PA shall redirect user requests to the Peer PA according to the agreed-upon strategy (e.g., weighted round-robin, least-connections).
*   **FR-5.2:** The Peer PA shall forward received requests to its local CDN infrastructure for servicing and return the response to the Primary PA or directly to the user (as per protocol).
*   **FR-5.3:** Participating PAs shall exchange accounting data (e.g., volume of bytes/requests served) at intervals defined in the Peering Agreement.
*   **FR-5.4:** All PAs in a session shall monitor the health of the peering link and the performance against the agreed SLA.

#### **FR-6: Peering Termination and Rearrangement**
*   **FR-6.1:** The system shall disband the peering arrangement automatically when:
    *   The agreed duration expires.
    *   The Primary PA detects its load has fallen below the sustain threshold for a stable period.
    *   A critical SLA violation is detected and not remedied.
*   **FR-6.2:** Upon termination, all PAs shall be notified, redirection rules shall be removed, and accounting records shall be finalized.
*   **FR-6.3:** The Mediator shall support re-negotiation of an existing peering arrangement to scale resources up or down based on changing load.

### 3.3 Non-Functional Requirements

#### **NFR-1: Performance**
*   **NFR-1.1 (Negotiation Speed):** The time from overload trigger to an established, operational peering arrangement shall be less than **60 seconds** for 95% of automated flash-crowd scenarios, as measured in the test bed.
*   **NFR-1.2 (Redirection Latency):** The overhead added by the CPFS to redirect a user request from the Primary to the Peer CDN shall be less than **50 ms** (excluding network transit time between CDNs).

#### **NFR-2: Reliability & Availability**
*   **NFR-2.1:** The failure of a single CPFS central component (Mediator or Registry) shall not disrupt already-established peering sessions. (PA-to-PA communication must persist).
*   **NFR-2.2:** The Peering Agent shall have an availability of 99.9% to ensure it can respond to triggers and manage sessions.

#### **NFR-3: Security**
*   **NFR-3.1:** All communication between different administrative domains (PA-to-Mediator, PA-to-PA) shall be authenticated and encrypted in transit (using TLS 1.3 or equivalent).
*   **NFR-3.2:** Peering Agreements shall be digitally signed to ensure non-repudiation.
*   **NFR-3.3:** The system shall not become a vector for attacks (e.g., DDoS amplification). Peer CDNs must be able to authenticate and rate-limit redirected requests.

#### **NFR-4: Privacy & Autonomy**
*   **NFR-4.1:** The system shall be designed to share the minimum necessary information required for peering. CDNs shall have fine-grained control over what capabilities and metrics are advertised.
*   **NFR-4.2:** The CPFS shall not provide a participant with direct insight into another CDN's internal topology, customer list, or detailed performance data beyond what is contractually agreed in the SLA.

#### **NFR-5: Usability**
*   **NFR-5.1:** CDN Operators shall be able to configure their local peering policies (triggers, resource limits, SLA templates) via a declarative configuration file or a simple web UI provided by the local PA.
*   **NFR-5.2:** The system shall provide clear logs and dashboards for Operators to view the status of active/previous peering sessions and key metrics.

#### **NFR-6: Deployment & Testability**
*   **NFR-6.1:** The prototype system shall be packaged for deployment on heterogeneous, geographically distributed nodes as found in the PlanetLab test bed.
*   **NFR-6.2:** The system shall include instrumentation and hooks for collecting performance and behavioral data during test bed experiments.

## 4. Appendices

### 4.1 Acceptance Criteria
The prototype will be considered acceptable upon successful demonstration of the following core scenario in a controlled test bed environment (e.g., PlanetLab):
1.  Two distinct, autonomous CDN test clusters are deployed, each running the CPFS Peering Agent.
2.  A simulated flash crowd is generated against **CDN-A**, causing it to breach its load threshold.
3.  **CDN-A's** PA automatically triggers peering, discovers **CDN-B** via the Registry/Mediator, and negotiates a peering agreement.
4.  A peering arrangement is established, and **CDN-A** begins redirecting a portion of user requests to **CDN-B**.
5.  **CDN-B** successfully services the redirected requests, reducing the effective load on **CDN-A**.
6.  Accounting data is exchanged between the PAs.
7.  Upon cessation of the simulated load, the peering arrangement is cleanly terminated.

### 4.2 Open Issues
*   The specific heuristic algorithms for geographic/network proximity matching require further research and specification.
*   The exact format and schema of the digital Peering Agreement (SLA) document are to be defined.
*   The protocol for secure content pre-positioning/replication between peered CDNs is deferred to a future phase.