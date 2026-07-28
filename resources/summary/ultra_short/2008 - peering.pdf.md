**Purpose & Scope**
The system enables distinct Content Delivery Networks (CDNs) to peer and share resources to handle sudden load spikes (e.g., flash crowds) and scale capacity. It coordinates content delivery across multiple autonomous CDN providers. It does not replace or manage the internal proprietary operations of individual CDNs.

**Product Background / Positioning**
This is a software infrastructure layer that sits atop existing, autonomous CDNs to virtualize them into a cooperative federation. It interacts with CDN components (Web Servers, mediators, registries) to form peering arrangements, but does not control the CDNs' internal infrastructure.

**Core Functional Overview**
*   Detect overload conditions in a CDN and automatically trigger a peering process.
*   Generate and negotiate service requirements and policies between CDNs to form a peering arrangement.
*   Discover available resources (e.g., storage, bandwidth) from potential peer CDNs.
*   Establish and configure peering protocols to enable request redirection and content replication between peered CDNs.
*   Operationally manage an active peering arrangement, including redirecting user requests and exchanging accounting data.
*   Disband or re-arrange peering based on termination conditions like expired need or SLA violations.

**Key Users & Usage Scenarios**
Primary users are the CDN providers themselves, acting as initiators (primary CDN) or resource contributors (peering CDNs). Usage scenarios are automated, short-term peering to react to flash crowds, and human-directed, long-term strategic peering arrangements. End-users and content providers are implicit beneficiaries but do not directly interact with the system.

**Major External Interfaces**
Interfaces are between the system's components (Mediator, Peering Agent, Service Registry) and the existing components of each participating CDN (their Web Servers, policy stores). Communication between peered CDNs occurs via their respective Peering Agents over an IP network.

**Key Non-functional Requirements**
*   The system must enable peering negotiations and request redirection to complete quickly enough to handle sudden flash crowds.
*   It must operate with limited, non-proprietary information shared between autonomous CDN providers.
*   It must ensure individual CDN providers can meet their own SLAs while participating in the peering group.
*   The prototype must be deployable and testable on a global real-world test bed like PlanetLab.

**Constraints, Assumptions & Dependencies**
*   Constraint: Cannot rely on full visibility or control over the internal load, cost, or performance data of participating CDNs.
*   Constraint: Implementation models for attributes like geographic location or network delay will likely be heuristic-based.
*   Assumption: Existing web services technologies and protocols (e.g., HTTP, TCP/IP) can be leveraged for the implementation.
*   Dependency: Design inspiration will be taken from related systems like CoDeeN, Coral, and MotusNet.

**Priorities & Acceptance Approach**
The highest priority is the core peering lifecycle: automatic trigger, negotiation, resource discovery, and operational management for short-term load spikes. Acceptance will be based on the prototype's ability to form a peering arrangement between distinct CDNs in a test bed and successfully redirect user requests to share load.