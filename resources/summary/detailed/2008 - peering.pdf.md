# Detailed Summary: Internetworking of Content Delivery Networks through Peering

## Background and Scope
This document specifies the requirements for a software infrastructure enabling the internetworking of distinct Content Delivery Networks (CDNs) through peering. The system allows autonomous CDNs to coordinate and share resources to handle load spikes (e.g., flash crowds), extend geographic reach, and improve content delivery performance without requiring a single provider to over-provision. The scope includes developing models, protocols, and policies for autonomic management of service levels through on-demand resource negotiation. Non-goals include the detailed design of underlying CDN proprietary technologies and the legal/financial aspects of business agreements between providers.

## Stakeholders Matrix and Use Cases
*   **Primary CDN (Initiator):** The CDN that initiates a peering relationship due to insufficient capacity, responsible for triggering negotiation and managing the primary service requirements.
*   **Peering CDN (Participant):** An external CDN that shares its resources in a peering arrangement, responsible for accepting negotiated terms and serving redirected requests.
*   **Content Provider:** The owner of the content being delivered, an implicit beneficiary of improved service quality and reliability through peering.
*   **End-User:** The final consumer of content, an implicit beneficiary who experiences improved performance (e.g., reduced latency) due to peering.
*   **System Administrator:** Manages and monitors the software components (Mediator, PA, SR, PR) within a CDN.

**Main Scenarios:**
1.  A primary CDN under flash crowd load initiates peering.
2.  The Mediator creates service requirements and negotiates with peers via Peering Agents (PAs).
3.  Resources are discovered and a peering arrangement is established.
4.  Operational management ensures content delivery and policy enforcement.
5.  The arrangement is disbanded when conditions are no longer met.

**Exception Scenarios:**
1.  No suitable peer is found during resource discovery.
2.  A participating CDN fails to meet its SLA obligations.
3.  A resource fails after registration.

## Business Process
**Main Process: Establish & Operate Peering Arrangement**
1.  **Trigger:** Primary CDN Web Server detects inability to handle workload.
2.  **Input:** Load spike event. **Output:** Initiation request sent to Mediator.
3.  Mediator gathers resource info from Service Registry (SR) and policies from Policy Repository (PR).
4.  Mediator generates and validates service requirements.
5.  Mediator passes requirements to local Peering Agent (PA) for resource discovery.
6.  Local PA negotiates with external PAs to discover and acquire resources.
7.  Upon successful negotiation, a peering arrangement is established and protocols are configured.
8.  **Output:** Operational peering arrangement handling redirected requests.

**Key Branch A: Long-Term Peering Exists**
1.  PA checks for existing peering policies in the PR.
2.  If policies exist, they are returned to the Mediator.
3.  The existing arrangement is used or re-evaluated.
4.  Proceed to operational management.

**Key Branch B: Re-negotiation Required**
1.  Insufficient resources are acquired from initial peer discovery.
2.  Mediator re-evaluates service requirements.
3.  Local PA re-initiates negotiation with adjusted parameters.
4.  Loop back to main process step 6.

## Domain Model
*   **Web Server (WS):** `server_id (unique)`, `resource_capacity (required)`, `current_load`, `geographic_location`, `delegation_policy (reference)`.
*   **Mediator:** `mediator_id (unique)`, `associated_cdn_id (required, reference)`, `negotiation_policy`.
*   **Service Registry (SR):** `registry_id (unique)`, `cdn_id (required, reference)`, `registered_resources (list, required)`, `last_updated`.
*   **Policy Repository (PR):** `repository_id (unique)`, `policies (required)`: `PWS`, `PM`, `PPeering`.
*   **Peering Agent (PA):** `agent_id (unique)`, `associated_mediator_id (required, reference)`, `discovery_protocol`.
*   **Peering Arrangement:** `arrangement_id (unique)`, `participant_cdn_ids (list, required)`, `negotiated_sla (required)`, `status (active/inactive)`.
*   **Service Requirement:** `req_id (unique)`, `initiator_cdn_id (required, reference)`, `resource_needs`, `qos_constraints`.
*   **Content Request:** `request_id (unique)`, `end_user_id`, `content_id`, `assigned_peer_id (reference)`.

## Interfaces and Integrations
*   **Web Server to Service Registry:** Direction: WS → SR. **Theme:** Resource registration/update. **Input:** Resource metrics (CPU, storage, bandwidth). **Output:** Registration acknowledgement/ID. **SLA:** Periodic updates on resource status.
*   **Mediator to Policy Repository:** Direction: Mediator ↔ PR. **Theme:** Policy retrieval for negotiation. **Input:** Query for PPeering, PM policies. **Output:** Applicable policy rules. **SLA:** Low-latency access during initiation.
*   **Peering Agent to External Peering Agent:** Direction: PA ↔ PA. **Theme:** Resource discovery & negotiation. **Input:** Service requirements, capabilities. **Output:** Resource offer, acceptance/rejection. **SLA:** Secure, authenticated message exchange.
*   **Mediator to Service Registry:** Direction: Mediator → SR. **Theme:** Resource information query. **Input:** Request for available local resources. **Output:** List of resources and capacities. **SLA:** Real-time response during traffic surges.
*   **CDN Gateway to DNS:** Direction: CDN (via PA) → DNS. **Theme:** Request redirection. **Input:** Updated server IP/health records. **Output:** DNS record updates. **SLA:** TTL-based update propagation.

## Acceptance Criteria
**Capability: Handle Flash Crowd via Peering**
*   **Given** a primary CDN is experiencing a flash crowd, **when** its Web Server load exceeds threshold, **then** an initiation request is sent to its Mediator to trigger peering.
*   **Given** service requirements have been generated, **when** the local PA discovers and negotiates with a suitable peer, **then** a peering arrangement is established and user requests are redirected.

**Capability: Operational Management of Peering**
*   **Given** an active peering arrangement, **when** a content request arrives at the primary CDN, **then** the request is redirected to the optimal peer's Web Server based on load and content availability.
*   **Given** a participating CDN fails to meet its SLA, **when** termination conditions are evaluated, **then** the peering arrangement is disbanded or re-arranged.

## Non-functional Metrics
*   **Performance:** Peering negotiation should complete within seconds to handle flash crowds. Request redirection latency should not add significant overhead to user-perceived delay.
*   **Reliability:** The system must maintain availability of content delivery even if one peering component fails. Peering arrangements should have graceful degradation and failover.
*   **Security:** All inter-CDN communications (PA-PA, policy exchange) must be authenticated and encrypted. Malicious request detection and rejection is required.
*   **Compliance:** Adherence to common web service standards and protocols (HTTP, TCP/IP) for interoperability.
*   **Observability:** Load information and resource usage must be measurable and disseminated among participants. Audit logs for accounting and billing must be maintained.

## Milestones and Release Strategy
1.  Core component specification and interface protocol design.
2.  Implementation of Service Registry and Policy Repository modules.
3.  Implementation of Mediator and Peering Agent with basic negotiation.
4.  Integration testing of peering lifecycle (initiation, discovery, establishment) in a controlled environment.
5.  Deployment and testing on a real-world testbed (e.g., PlanetLab).
6.  Iterative refinement based on performance evaluation and feedback.

## Risk List and Mitigation Strategies
1.  **Risk:** Proprietary nature of CDNs limits information sharing for optimal decision-making. **Mitigation:** Use heuristic-based models and agreed-upon protocols for limited, policy-driven information exchange.
2.  **Risk:** Negotiation overhead may negate the benefits for very short-lived spikes. **Mitigation:** Implement caching of pre-negotiated terms for long-term partners and optimize short-term protocol efficiency.
3.  **Risk:** Incentive misalignment or cheating among peers (e.g., not honoring SLAs). **Mitigation:** Implement cryptographically secure accounting and auditing, with clear policies for penalties and renegotiation.
4.  **Risk:** Increased complexity in request routing leading to performance degradation. **Mitigation:** Use hierarchical load distribution and validate redirection algorithms through simulation before deployment.
5.  **Risk:** Dependence on external systems (other CDNs' PAs) creates a single point of failure. **Mitigation:** Design Mediator/PA to handle timeouts and fallback to alternative peers or degrade gracefully.
6.  **Risk:** Scalability of the PA discovery mechanism with a large number of potential peers. **Mitigation:** Employ distributed discovery mechanisms (e.g., DHT-based) and aggregate load information.

## Undecided Issues and Responsible Parties
1.  **Issue:** Specific cryptographic framework and standards for secure auctions and accounting. **Responsible:** Security Architecture Team.
2.  **Issue:** Detailed heuristic algorithms for performance prediction and optimal peer selection. **Responsible:** Algorithms Research Team.
3.  **Issue:** Standardized data format for exchanging service requirements and resource capabilities between heterogeneous CDNs. **Responsible:** Protocol Design Team.
4.  **Issue:** Quantifiable thresholds for triggering peering (load metrics) and for SLA violation. **Responsible:** Performance Modeling Team.
5.  **Issue:** Integration strategy with existing CDN request-routing mechanisms (e.g., specific DNS update methods). **Responsible:** Systems Integration Team.