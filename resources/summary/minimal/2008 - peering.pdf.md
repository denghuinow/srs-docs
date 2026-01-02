**Purpose & Scope**
The system enables distinct Content Delivery Networks (CDNs) to peer and share resources to handle load spikes, such as flash crowds, through coordinated, policy-driven internetworking.

**Core Functions**
*   Register CDN resource and service information.
*   Trigger peering initiation when a CDN cannot handle its workload.
*   Discover and negotiate for external resources from peer CDNs.
*   Operate and manage established peering arrangements.

**Key Users**
*   Primary CDN (initiator).
*   Peering CDNs (resource providers).
*   Content providers.
*   End-users.

**Key Constraints**
*   Peering must occur without full information from proprietary CDNs.
*   Request redirection and resource selection rely on heuristics for attributes like geographic location.