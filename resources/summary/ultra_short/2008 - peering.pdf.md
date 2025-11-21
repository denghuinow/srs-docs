Purpose & Scope: Enables CDNs to share resources during traffic spikes via automated peering, solving flash crowd handling without over-provisioning. Excludes single-CDN operations, content creation, and non-traffic-based scaling. Boundaries: Limited to resource sharing between cooperating CDNs; excludes end-user content delivery management.

Product Background / Positioning: Research prototype for global CDN resource virtualization, deployed on PlanetLab. Builds on existing CDN research (e.g., MotusNet) but does not integrate with commercial CDN systems directly.

Core Functional Overview:  
- Service registration of CDN resources and policies to local registries.  
- Automated initiation of peering during unanticipated traffic surges.  
- Negotiation of resource-sharing terms between CDNs.  
- Discovery of external resources via peer-to-peer policy exchange.  
- Operational management of content delivery and billing during active peering.  
- Disbanding or re-arranging peering based on termination conditions.

Key Users & Usage Scenarios: Primary CDNs initiate peering; peer CDNs respond to resource requests. Short-term peering requires fully automated negotiation (no human input); long-term peering involves human-directed policy alignment. Content providers and end-users benefit passively.

Major External Interfaces: Web service APIs for component communication (mediator, PA, SR, PR). DNS-based request redirection to optimal CDN peers during operational management.

Key Non-functional Requirements: Must handle flash crowds with automated short-term peering (no human intervention). Cryptographic security for policy exchange. Agile adaptation to changing load conditions during active peering.

Constraints, Assumptions & Dependencies: No centralized geographic data repository. Limited resource visibility between CDNs. Requires existing CDN infrastructure (e.g., Web servers, SLAs) as-is. Depends on PlanetLab for prototype testing.

Priorities & Acceptance Approach: Short-term peering automation is critical; long-term negotiation is secondary. Acceptance: Successful peering initiation within 5 minutes of traffic surge detection, with SLA-compliant resource allocation.