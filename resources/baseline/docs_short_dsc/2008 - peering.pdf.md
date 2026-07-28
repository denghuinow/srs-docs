# Software Requirements Specification (SRS)
## Internetworking of Content Delivery Networks (CDNs) through Peering

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for a software infrastructure that enables internetworking between distinct Content Delivery Networks (CDNs) via peering. The purpose is to provide a clear, complete, and unambiguous specification for developers, testers, project managers, and stakeholders. This document will serve as the foundation for system design, implementation, and validation.

#### 1.2 Scope
This project encompasses the development of models, protocols, and policies for the autonomic management of service levels through inter-CDN resource negotiation. The system will facilitate coordinated content delivery across multiple administrative domains to improve performance, reduce costs, and handle demand volatility.

**In-Scope Elements:**
*   Autonomic management models for service level negotiation.
*   Protocols for resource discovery, negotiation, and operational coordination between CDNs.
*   Policies governing short-term (flash crowd) and long-term peering arrangements.
*   Components for mediation, peering agency, request redirection, and accounting.
*   Technical Service Level Agreement (SLA) specification and enforcement mechanisms.

**Out-of-Scope Elements:**
*   Design of underlying CDN hardware (caches, servers, network links).
*   Legal/business contract frameworks for peering (focus is on technical SLAs).
*   Proprietary internal CDN algorithms (caching, load balancing).
*   Comprehensive graphical user interfaces (GUIs) for administration.
*   Detailed specification of cryptographic auction frameworks (noted as a future consideration).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **CDN** | Content Delivery Network. A distributed network of servers that delivers web content efficiently. |
| **Peering** | A cooperative arrangement between two or more CDNs to share resources. |
| **Primary CDN** | The CDN that initiates a peering request to handle excess demand. |
| **Peering CDN** | A CDN that offers resources to a Primary CDN. |
| **PA** | Peering Agent. A software component responsible for discovery and negotiation with external CDNs. |
| **Mediator** | A software component that monitors internal CDN state and triggers peering based on policy. |
| **SLA** | Service Level Agreement. A technical contract defining expected performance metrics. |
| **QoS** | Quality of Service. The overall performance of a service, often measured by latency, throughput, availability. |
| **Flash Crowd** | A sudden, massive surge in user requests for specific content. |

#### 1.4 References
*   [RFC 3986] Uniform Resource Identifier (URI): Generic Syntax
*   [RFC 7230] Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
*   PlanetLab: An open, global network research testbed.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its perspective, functions, and constraints. Section 3 details specific requirements, including functional requirements, interface requirements, and non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
The CDN Peering Infrastructure is a middleware system that operates at the coordination layer between independent, proprietary CDNs. It is not a replacement for existing CDNs but an overlay system that enables them to interoperate. The system interfaces with a CDN's internal monitoring and request routing systems and communicates with external peer systems via defined protocols.

#### 2.2 Product Functions
The core functions of the system are:
1.  **Monitoring & Analysis:** Monitor internal CDN load and performance against SLAs.
2.  **Peering Trigger:** Automatically determine the need for peering based on policy thresholds.
3.  **Resource Discovery:** Discover potential peer CDNs and their available resource capabilities.
4.  **Negotiation:** Conduct automated negotiations to establish peering terms and technical SLAs.
5.  **Request Redirection:** Seamlessly redirect user requests to a peering CDN according to the established agreement.
6.  **Accounting & Monitoring:** Track resource usage and performance across the peering arrangement for billing and SLA enforcement.
7.  **Policy Management:** Allow administrators to define and update peering strategies, costs, and acceptable partners.

#### 2.3 User Characteristics
| Stakeholder | Expertise | Primary Interaction |
| :--- | :--- | :--- |
| **System Administrator** | Advanced networking, CDN operations. | Deploys components, defines and manages operational policies, monitors system health. |
| **CDN Operator (Primary/Peering)** | Business and technical CDN management. | Sets business-level peering policies, reviews SLA reports, authorizes long-term arrangements. |
| **Content Provider** | Manages web content and delivery contracts. | (Indirect) Benefits from improved performance; may set high-level delivery requirements. |
| **Researcher/Developer** | Distributed systems, networking. | Extends protocols, experiments with new negotiation models in testbed environments. |
| **End-User** | General web user. | (Indirect) Experiences improved page load times and video streaming quality. |

#### 2.4 Constraints
1.  **Technical:** Must utilize existing web services standards (HTTP/S, XML/JSON) for interoperability.
2.  **Business:** Must respect the proprietary and confidential nature of each CDN's internal state (e.g., exact cache contents, full network topology).
3.  **Implementation:** Must be modular for deployment on real-world testbeds like PlanetLab.
4.  **Architectural:** Design must rely on heuristics (e.g., inferred geographic location, measured RTT) due to limited information sharing.
5.  **Performance:** Virtualization of multiple providers must not introduce significant latency in the critical request-redirection path.

#### 2.5 Assumptions and Dependencies
*   Participating CDNs have a basic capability to measure their own load and performance.
*   A minimal level of trust exists between peering CDNs to engage in automated negotiation.
*   The system depends on underlying network stability and DNS/HTTP protocols functioning correctly.
*   It is assumed that content is replicable and not bound by strict geo-licensing that would prevent cross-CDN delivery.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 Mediator Component**
*   **FR-MED-01:** The Mediator shall continuously monitor internal CDN metrics (e.g., request rate, cache hit ratio, server load, response latency).
*   **FR-MED-02:** The Mediator shall compare monitored metrics against predefined SLA thresholds and internal policy rules.
*   **FR-MED-03:** Upon detecting an impending or current SLA violation (e.g., flash crowd), the Mediator shall trigger the peering process.
*   **FR-MED-04:** The Mediator shall formulate a **Service Request** specifying required resources (e.g., bandwidth: 10 Gbps, duration: 2 hours, geographic region: EU).

**3.1.2 Peering Agent (PA) Component**
*   **FR-PA-01:** The PA shall discover potential peer CDNs through a configurable mechanism (e.g., static list, dynamic registry service).
*   **FR-PA-02:** The PA shall receive a Service Request from the Mediator and initiate negotiation with one or more candidate Peering CDNs.
*   **FR-PA-03:** The PA shall exchange negotiation messages with peer PAs, conveying resource requirements and capabilities.
*   **FR-PA-04:** The PA shall evaluate received offers based on local policy (cost, performance history, trust) and select the optimal peer(s).
*   **FR-PA-05:** The PA shall finalize the peering arrangement by establishing a mutually agreed-upon **Technical SLA** with the peer PA.

**3.1.3 Operational Management**
*   **FR-OP-01:** The system shall redirect a defined portion of user requests (e.g., based on URL prefix, client IP geolocation) to the Peering CDN.
*   **FR-OP-02:** Redirection shall be transparent to the end-user (e.g., using HTTP 302/307 redirects or DNS-based redirection).
*   **FR-OP-03:** The system shall log all redirected requests and resources consumed (e.g., bytes served, number of requests).
*   **FR-OP-04:** The system shall monitor the performance (latency, throughput) of the Peering CDN against the agreed Technical SLA.
*   **FR-OP-05:** Upon detecting an SLA violation by the peer, the system shall trigger a renegotiation or termination procedure as per policy.

**3.1.4 Policy & Administration**
*   **FR-POL-01:** The system shall provide a configuration interface (e.g., file-based, API) to define peering policies.
*   **FR-POL-02:** Policies shall include parameters for trigger thresholds, preferred/blocked peers, cost limits, and negotiation timeouts.
*   **FR-POL-03:** The system shall generate reports on peering activity, including usage statistics, costs incurred/earned, and SLA compliance.

#### 3.2 Non-Functional Requirements

**3.2.1 Performance**
*   **NFR-PER-01:** The decision-to-redirect latency (from Mediator trigger to first request being redirected) shall be less than 5 seconds for short-term peering.
*   **NFR-PER-02:** The overhead of the peering coordination system shall not increase average end-user latency by more than 10%.
*   **NFR-PER-03:** The system must scale to manage simultaneous peering arrangements with up to 10 different CDN partners.

**3.2.2 Reliability & Availability**
*   **NFR-REL-01:** The Mediator and PA components shall have an availability of 99.9%.
*   **NFR-REL-02:** The system shall implement graceful degradation; failure of the peering system shall not disrupt the core CDN's ability to serve content from its own resources.

**3.2.3 Security**
*   **NFR-SEC-01:** All inter-CDN communication (PA-to-PA) shall be authenticated and encrypted (e.g., using TLS).
*   **NFR-SEC-02:** The system shall prevent unauthorized peering initiation or resource consumption.
*   **NFR-SEC-03:** Accounting data shall be tamper-evident.

**3.2.4 Maintainability**
*   **NFR-MAIN-01:** The system shall be modular, allowing independent updates to the Mediator, PA, or policy engine.
*   **NFR-MAIN-02:** All protocols and data formats shall be well-documented to facilitate integration by new CDN partners.

#### 3.3 Interface Requirements

**3.3.1 Software Interfaces**
*   **INT-SW-01:** **Mediator-PA Interface:** An API (e.g., RESTful HTTP) for passing Service Requests and receiving negotiation status.
*   **INT-SW-02:** **PA-PA Protocol:** A defined application-layer protocol over HTTP/TLS for discovery, negotiation, and SLA management between CDNs. *(Format TBD - see Undecided Issues)*.
*   **INT-SW-03:** **CDN Redirection Interface:** The system must interface with the CDN's request router (e.g., via configuration API or plugin) to enact redirection rules.

**3.3.2 Communication Interfaces**
*   The system shall communicate using standard TCP/IP networks.
*   Primary application-layer protocol shall be HTTP/1.1 or HTTP/2.

#### 3.4 Undecided Issues & Open Questions
1.  The specific message schema and state machine for the **PA-PA Protocol** requires detailed definition.
2.  The **format for describing service capabilities and requirements** (e.g., using a schema like TOSCA, custom JSON) is not finalized.
3.  Detailed procedures differentiating **short-term (dynamic) negotiation** from the application of **pre-negotiated long-term policy** need to be elaborated.
4.  The **consequences and remedies for SLA violations** (e.g., penalty payments, automatic termination) require clear technical specification.
5.  The integration of an **incentive mechanism** (e.g., cryptographic auction) for content replication is anticipated but not scoped for the current version.

---
*Document End*