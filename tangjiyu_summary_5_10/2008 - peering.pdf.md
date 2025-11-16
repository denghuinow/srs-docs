# Software Requirements Specification for Internetworking of Content Delivery Networks through Peering

## 1. Introduction

### 1.1 Purpose
This document describes the requirements specification (SRS) for the software infrastructure enabling the internetworking of Content Delivery Networks (CDNs) through peering, termed as 'CDN peering'. It presents a means for distinct CDNs to coordinate and cooperate by investigating and developing:
- Models for effective internetworking between CDNs through peering
- Protocols for service delivery in a cooperative environment of CDNs
- Concrete examples (technology trends) exhibiting the notion of content networking
- Policies for autonomic management of service level through resource negotiation on-demand

### 1.2 Document Conventions and Terminology
- Web server (WS): Container of content comprising overlay (Web service host, SLA-allocator, policy agent) and core (underlying hardware infrastructure)
- Mediator: Policy-driven entity authoritative for policy negotiation and management
- Service registry (SR): Discovers and stores resource and policy information in local domain
- Peering Agent (PA): Resource discovery module in the peering CDNs environment
- Policy repository (PR): Storage of Web server, mediator and peering policies
- PWS: Set of Web server-specific rules for content storage and management
- PM: Set of mediator-specific rules for interaction and negotiation
- PPeering: Set of rules for creation and growth of the peering arrangement

### 1.3 Intended Audience and Reading Suggestions
This document is written for researchers, software developers, advanced practitioners, documentation writers, and users involved in the CDN domain to initiate open discussion for exploring development opportunities regarding internetworking between CDNs.

### 1.4 Project Scope
The final product enabling CDN peering assists in coordinated and cooperative content delivery via internetworking among distinct CDNs to allow providers to rapidly "scale-out" to meet both flash crowds and anticipated increases in demand, removing the need for a single CDN to provision resources. An ad-hoc or planned peering of CDNs requires fundamental research to address core problems of measuring and disseminating load information, performing request assignment and redirection, enabling content replication, and determining appropriate compensation among participants on a geographically distributed "Internet" scale.

### 1.5 References
- An introduction to CDN technologies
- The research problem for internetworking of CDNs
- The architecture for CDN peering
- The performance models to demonstrate effects of peering and predict user perceived performance
- CDN peering models along with challenges for implementation

## 2. Overall Description

### 2.1 Product Perspective
CDN peering allows different CDN providers to share resources to provide larger scale and/or reach to each participant than they could achieve otherwise. It is formed by a set of autonomous CDNs that cooperate through a mechanism providing facilities and infrastructure for cooperation to virtualize multiple providers.

Effective peering arrangement between CDNs requires multiple steps:
1. Initiation: Triggered by initialization request sent to mediator under exceptional circumstances (e.g., flash crowds) when primary CDN realizes it cannot handle part of workload on its Web Servers
2. Negotiated relationship: Creation of relationship through legal document or technical terms (SLAs) specifying interactions among entities including service administration, coordination and disband/re-arrangement
3. Resource discovery: Mediator passes service requirements to local PA to discover external resources from peers
4. CDN peering protocols: Configure protocols at conduit of respective CDNs to technically support terms and policies specified through negotiated relationships
5. Operational management: Deploy and administer functional policies when primary CDN acquires sufficient resources from peers
6. Disband or re-arrangement: Existing arrangement may need to disband or re-arrange if circumstances change, peering is no longer beneficial, arrangement needs expansion, or participating CDNs are not meeting contributions

### 2.2 Product Features
The software infrastructure enabling peering between CDNs features the following major goals:
- Development and validation of peering and manage complexity of content delivery across Web servers of multiple CDNs that scale across the globe
- Decrease cost of Web access, increase QoS through reduced latency, reduce server load and bandwidth consumption
- Assist existing CDN to alleviate congestions by detecting and handling short-term load spikes (flash crowds) effectively

Component-wise major functions:
- Web server(s): Replicate content on-demand, initiate peering requests, ensure content delivery based on negotiated policies, determine resource delegation conditions, provision/reserve resources to satisfy SLAs, perform on-demand caching, content selection, and routing
- Mediator: Generate service requirements, pass requirements to PA, discover external resources, control traffic redirection and content replication, ensure adaptation to changing circumstances
- Service Registry: Encapsulate resource/service information, help discover local resources, supply local resource information during traffic surges, create instances encapsulating local and delegated external resources
- Policy Repository: Virtualize all policies within peering arrangement, provide rules for administering/accessing resources, return existing peering policies for long-term arrangements
- Peering Agent: Act as policy-driven resource discovery module, exchange policy/resource information with external PAs, establish negotiations with PAs of other peers

Architectural features:
- Content replication through cooperative pull-based approach extending to participating servers from peers
- Load distribution through hierarchical approach measuring and disseminating load information
- Request assignment and redirection at multiple levels (DNS, gateways, between servers)

### 2.3 User Classes and Characteristics
Users can be differentiated by membership and contributions to the system:
- Explicit members: Primary CDN (initiator) and peering CDNs cooperating for resource sharing
- Implicit members: Content providers and end-users (transparent but benefit from arrangement)
Users can vary based on purpose, size, scope, and duration of peering. Short-term arrangements require automation for tight timeframes, while long-term arrangements require human-directed agents. Users can receive preferential treatment based on policy and business logic. Individual users can have dynamic QoS requirements resulting in "customized" content delivery.

### 2.4 Operating Environment
The product is expected to be deployed in real-world test beds such as PlanetLab for global testing and performance evaluation. Implementation could be developed on top of existing standard application layers (Apache, Tomcat) and protocols (HTTP, CDI, HTPC). A cryptographically secure auction-based framework will assist content replication among peered CDNs. Load information could be measured and disseminated using distributed load indices such as Distributed Hash Table (DHT). Request assignment and redirection could rely on DNS-level end-user assignment combined with rudimentary policies like weighted round-robin or least-loaded-first.

### 2.5 Design and Implementation Constraints
Challenges include virtualization of multiple providers and offloading end-user requests from primary CDN to peers based on cost, performance, and load. Due to proprietary nature of existing CDNs, limited information about response time or service cost is typically available. Request-redirections must occur over distributed sets of Web servers belonging to multiple CDN providers without full information available. Implementation model could be based on complex combination of attributes such as Web server responsiveness, expected network delay, or geographic location. Several attributes vary over time with no single repository listing values for all Internet-connected systems.

### 2.6 User Documentation
A user manual would be written to help people understand working methodology and usage of the developed prototype system. It would be written for non-technical individuals with content/terminology differing from technical guides. The manual would follow common user documentation styles capturing purpose/scope, key features/operations, step-by-step instructions, conventions, messaging structures, quick references, tips for errors/malfunctions, pointers to reference documents, and glossary of terms.

### 2.7 Assumptions and Dependencies
The product would build on leveraging existing systems. Inspirations could be obtained by analyzing related systems such as CoDeeN, Coral, Globule, and MotusNet. The design and implementation approach of MotusNet could be helpful to draw a clear guideline for developing the intended prototype.

## 3. System Features

### 3.1 Service Registration
Associated with registration of resource and service information of each CDN to its SR.

Actors:
- WS: Publishes resource and service information to SR
- SR: Registers available local resources and updates them
- Mediator: Collects up-to-date resource information from SR

Trigger: Service registration triggered when resources are available as provider starts operating, previously registered resource information needs updating, available local resource information is required during traffic surges, or local and delegated external resource information is to be encapsulated in SR instance

Functional Requirements:
- REQ-1: Format for service information description is defined
- REQ-2: Interaction protocol between Web Server-SR, SR-mediator is defined
- REQ-3: Resource provisioning, delegation and reservation policies are in place
- REQ-4: Established norm that any resource failure will be reported
- REQ-5: Interaction protocol between Web Server-SR, SR-mediator is defined

### 3.2 Request Initiation to Trigger Peering
Relates to initialization of peering between CDNs.

Actors:
- End-user: Requests for content
- Mediator: Receives initiation request from WS to trigger peering

Trigger: Invoked when primary CDN realizes it cannot handle part of workload on its WS(s), considering expected and unexpected load increases

Functional Requirements:
- REQ-1: Malicious requests are detected and rejected
- REQ-2: Web servers have already replicated necessary content
- REQ-3: Both anticipated and unanticipated user requests (traffic) are considered
- REQ-4: Format of initiation request is defined

### 3.3 Mediator Invokes Creation of Negotiated Relationship
Upon receipt of initialization request, mediator of primary CDN invokes negotiation.

Actors:
- SR: Sends resource and access information
- PR: Sends policy information for establishing negotiated relationships
- PA: Receives service requirements from mediator

Trigger: Upon receiving initialization request to trigger peering, mediator generates service requirements and passes to local PA

Functional Requirements:
- REQ-1: Format of service requirements is defined
- REQ-2: Mediator-SR, mediator-PR, mediator-PA interaction protocols are defined
- REQ-3: Mediator works in conjunction with PA to establish negotiation

### 3.4 Resource Discovery through PA
PA of primary CDN negotiates with PAs of peers to perform external resource discovery.

Actors:
- External PA: Negotiates with PA of primary CDN
- PR: Receives negotiated policies from local PA

Trigger: Local PA communicates with PAs of peers to discover external resources

Functional Requirements:
- REQ-1: Interaction protocols between PAs are identified
- REQ-2: Malicious requests are identified and acted upon
- REQ-3: Existing policies for long-term peering arrangement
- REQ-4: Procedure to perform short-term negotiation

### 3.5 Operational Management
Responsible for inter-CDN protocol configuration, resource initialization, and ensuring effective operations of established peering arrangement.

Actors:
- External PA: Exchanges configurations and content availability information, accepts requests to optimal peer
- PR: Assists in enforcing negotiated policies

Trigger: Once policies are negotiated and peering arrangement is established, PAs interact in execution of common goals

Functional Requirements:
- REQ-1: Negotiation is established between selected CDN peers
- REQ-2: Primary CDN has already acquired sufficient external resources
- REQ-3: Malicious requests are identified and acted upon
- REQ-4: Functional policies are identified and deployed
- REQ-5: Effective content delivery is ensured through SLA satisfaction

### 3.6 Disband or Re-arrangement
Circumstances under which peering arrangement may need to disband or re-arrange.

Actors:
- External PA: Interactions with local PA of primary CDN

Trigger: Any termination condition holds

Functional Requirements:
- REQ-1: Policies identifying consequences of SLA violation are defined
- REQ-2: Policies are in place to perform renegotiation for problem resolution
- REQ-3: Administrative policies are deployed for operations in peering arrangement

## 4. External Interface Requirements

### 4.1 User Interfaces
Describes logical characteristics of each interface between intended software product and users. Common GUI standards will be followed with keyboard shortcuts, error message display standards, standard buttons and functions appearing on every screen. Details intended to be documented in separate user interface specification.

### 4.2 Communications Interfaces
Intended product exploits existing Web service technologies to leverage existing infrastructures through building overlay. Communication among software components performed through message passing over IP network using TCP/IP as transport protocol. Each CDN server establishes TCP connection to network elements using well-known port number. Messages consist of fixed length-header containing total data length and request followed by reply or acknowledgement. Interaction among surrogates performed using HTTP or FTP.
