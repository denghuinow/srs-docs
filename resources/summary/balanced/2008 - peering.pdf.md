# Balanced Summary: Internetworking of CDNs through Peering

## Goals and Scope
This software infrastructure enables distinct Content Delivery Networks (CDNs) to coordinate and cooperate through peering, allowing providers to scale resources to meet demand spikes like flash crowds. It focuses on developing models, protocols, and policies for autonomic management of service levels through on-demand resource negotiation, while ensuring individual provider SLAs are met within a cooperative environment.

## Stakeholders and User Stories
*   **Primary CDN (Initiator):** The CDN that initiates a peering relationship due to resource constraints.
*   **Peering CDN (Provider):** A CDN that shares its resources with the initiator under a negotiated agreement.
*   **Content Provider:** The entity that owns the content being delivered; an implicit beneficiary of improved delivery.
*   **End-User:** The final consumer of content; an implicit beneficiary of improved performance and reliability.
*   **System Administrator:** Manages and monitors the peering software infrastructure and its components.
*   **Policy Manager:** Defines and maintains the business and technical rules governing peering interactions.

**User Stories:**
1.  As a **Primary CDN**, I want to trigger peering when facing a flash crowd so that I can maintain my SLA with customers.
2.  As a **Peering CDN**, I want to negotiate service terms and compensation so that resource sharing is beneficial and governed.
3.  As a **Content Provider**, I want my content delivered reliably during traffic surges so that my end-users have a good experience.
4.  As an **End-User**, I want low-latency access to content so that my browsing experience is not degraded.
5.  As a **System Administrator**, I want to monitor the health and load of all peered CDN components so that I can ensure operational stability.
6.  As a **Policy Manager**, I want to define rules for information sharing and resource delegation so that business privacy and objectives are preserved.

## Key Processes
1.  **Service Registration (Trigger:** Resource availability/change): Web Servers publish their resource and service information (e.g., CPU, storage) to the local Service Registry.
2.  **Request Initiation (Trigger:** Unhandled workload): A Web Server detects it cannot handle excess load and sends an initiation request to its Mediator to trigger peering.
3.  **Negotiation Invocation (Trigger:** Initiation request): The Mediator generates service requirements using data from the Service Registry and Policy Repository, then passes them to the local Peering Agent (PA).
4.  **Resource Discovery (Trigger:** Service requirements from Mediator): The local PA communicates with external PAs to discover and negotiate for resources from potential peer CDNs.
5.  **Protocol Configuration & Operational Start (Trigger:** Peering arrangement established): Configuration and content availability information is exchanged, and request redirection to optimal peers begins.
6.  **Operational Management (Trigger:** Peering is active): Peers cooperate on content delivery, exchange accounting data, and enforce negotiated policies for effective operations.
7.  **Disband/Re-arrangement (Trigger:** Termination condition holds): The peering arrangement is disbanded or reconfigured if it is no longer beneficial or circumstances change.

## Domain Data Elements
*   **Web Server (WS)**
    *   **Primary Key:** Server ID
    *   **Key Fields:** Resource Capacity (CPU, Storage), Current Load, Geographic Location, Hosted Content IDs, Status.
*   **Service Registry (SR)**
    *   **Primary Key:** Registry ID / CDN Domain
    *   **Key Fields:** Registered Resource List (Server IDs), Resource Metadata, Access Policies, Last Update Timestamp.
*   **Mediator**
    *   **Primary Key:** Mediator ID / CDN Domain
    *   **Key Fields:** Associated CDN ID, Negotiation Policies, Current Service Requirements, Active Peering Arrangement IDs.
*   **Policy Repository (PR)**
    *   **Primary Key:** Policy Set ID
    *   **Key Fields:** Web Server Policies (PWS), Mediator Policies (PM), Peering Policies (PPeering), SLA Templates, Delegation Rules.
*   **Peering Agent (PA)**
    *   **Primary Key:** Agent ID / CDN Domain
    *   **Key Fields:** Associated Mediator ID, Discovered Peer List, Negotiation History, Communication Endpoints.
*   **Peering Arrangement**
    *   **Primary Key:** Arrangement ID
    *   **Key Fields:** Participating CDN IDs, Negotiated SLA Terms, Start/End Time, Resource Allocations, Status (Active/Disbanded).

## Non-functional Requirements
1.  **Scalability:** The system must support peering arrangements across globally distributed CDNs.
2.  **Performance:** Must decrease latency, reduce server load, and lower bandwidth consumption for participating CDNs.
3.  **Resilience & Agility:** Components must adapt to changing circumstances (agility) and achieve objectives in a dynamic environment (resilience).
4.  **Security & Privacy:** Must handle malicious requests and provide divergent policies to preserve business privacy during interactions.
5.  **Interoperability:** Must leverage existing Web services technologies and standard protocols (e.g., HTTP, TCP/IP).
6.  **Manageability:** Must allow for both automated short-term and human-directed long-term peering arrangements.

## Milestones and External Dependencies
1.  Development and validation of core peering protocols and negotiation mechanisms.
2.  Prototype deployment in a real-world test bed (e.g., PlanetLab) for global testing.
3.  Integration with existing CDN infrastructure and Web service technologies.
4.  Dependence on the analysis and inspiration from related systems (CoDeeN, Coral, Globule, MotusNet).
5.  Creation of comprehensive user documentation and administration guides.

## Risks and Mitigation Strategies
1.  **Risk:** Proprietary nature of CDNs limits information sharing (e.g., real-time load, cost), hindering optimal request-redirection.
    *   **Mitigation:** Use heuristic-based models and aggregated load information disseminated through hierarchical gateways.
2.  **Risk:** Complex, multi-dimensional constraints from individual providers may conflict within a peering arrangement.
    *   **Mitigation:** Implement policy-driven negotiation and autonomic management to balance local SLAs with cooperative obligations.
3.  **Risk:** Short-term peering requires automation to react within tight timeframes, increasing complexity.
    *   **Mitigation:** Develop semi-autonomous logic for components and pre-define policies for rapid, automated negotiation.
4.  **Risk:** Implementation relies on attributes (e.g., network delay, geographic location) with no single authoritative source.
    *   **Mitigation:** Base decisions on heuristics and periodic updates from participating CDN gateways.
5.  **Risk:** Ensuring fair compensation and billing among participants in a dynamic peering environment.
    *   **Mitigation:** Use a cryptographically secure auction-based framework and exchange detailed accounting information.

## Undecided Issues
1.  The specific cryptographic framework or auction mechanism for secure resource negotiation and incentives.
2.  The exact distributed load index mechanism (e.g., specific DHT variation) for load measurement and dissemination.
3.  The detailed heuristic algorithms for attributes like geographic proximity and expected network delay.
4.  The precise balance between automated decision-making and human oversight for long-term arrangements.
5.  The standard format for service information description and service requirement specifications.
6.  The concrete interaction protocols between all major components (e.g., Mediator-PA, PA-PA, Web Server-SR).