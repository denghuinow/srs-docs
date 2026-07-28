# Short Summary: Software Requirements Specification for Internetworking of CDNs through Peering

## Background and Objectives
This document specifies requirements for a software infrastructure enabling internetworking between distinct Content Delivery Networks (CDNs) through peering. The primary objective is to allow CDNs to coordinate and cooperate, enabling providers to scale resources dynamically to handle flash crowds and demand spikes without requiring a single CDN to over-provision.

## In Scope
- Development of models, protocols, and policies for autonomic management of service levels through resource negotiation.
- Enabling coordinated content delivery across multiple CDNs to improve performance and reduce costs.
- Handling both short-term (e.g., flash crowds) and long-term peering arrangements.
- Resource discovery and negotiation between CDNs via Peering Agents (PAs).
- Operational management of established peering arrangements, including request redirection and accounting.

## Out of Scope
- Detailed design of underlying hardware infrastructure for individual CDNs.
- Full specification of legal or business documents for negotiated relationships (though technical SLAs are considered).
- Implementation of proprietary CDN algorithms for caching or load balancing within a single provider.
- Comprehensive user interface design (to be documented separately).
- Specific cryptographic or auction-based frameworks for incentives (though noted as anticipated).

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Primary CDN:** Initiates peering to handle excess load and meet SLAs.
- **Peering CDNs:** Cooperate by sharing resources to gain scale/reach.
- **Content Providers:** Benefit transparently from improved content delivery.
- **End-Users:** Experience better QoS through reduced latency and improved performance.
- **Researchers/Developers:** Explore and implement CDN peering technologies.
- **System Administrators:** Deploy and manage the peering infrastructure.

**Core Use Cases:**
1. As a **Primary CDN**, I want to trigger peering when facing flash crowds so that I can meet my SLAs without over-provisioning.
2. As a **Peering CDN**, I want to negotiate resource sharing terms so that I can gain additional scale or revenue.
3. As a **Mediator**, I want to generate service requirements based on current load and policies so that I can initiate appropriate peering negotiations.
4. As a **Peering Agent (PA)**, I want to discover external resources from other CDNs so that I can establish a peering arrangement.
5. As a **System Operator**, I want to manage operational policies in a peering arrangement so that content delivery remains effective and SLAs are enforced.
6. As a **Content Provider**, I want my content delivered reliably during traffic surges so that end-users experience consistent performance.

## Success Metrics
- Reduction in latency and bandwidth consumption for content delivery.
- Effective handling of flash crowds without SLA violations.
- Successful establishment and management of both short-term and long-term peering arrangements.

## Major Constraints
- Limited information sharing between proprietary CDNs complicates request redirection and load balancing.
- Implementation models rely on heuristics for attributes like geographic location and network delay.
- Need to virtualize multiple providers while respecting individual business policies and SLAs.
- Must leverage existing Web services technologies and protocols (e.g., HTTP, TCP/IP).
- Deployment intended for real-world test beds like PlanetLab, requiring modular implementation.

## Undecided Issues
- Specific interaction protocols between components (e.g., Web Server-SR, Mediator-PA) need definition.
- Formats for service information description and initiation requests are not yet finalized.
- Procedures for short-term negotiation versus long-term peering policy application require further detail.
- Consequences of SLA violations and renegotiation policies need clearer specification.
- The exact cryptographic auction-based framework for content replication incentives is anticipated but not defined.