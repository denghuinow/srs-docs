**Purpose & Scope**: Software infrastructure to enable distinct Content Delivery Networks (CDNs) to coordinate and cooperate through peering for scalable content delivery.

**Core Functions**:
*   Initiate peering when a CDN cannot handle its workload.
*   Discover and negotiate for external resources from peer CDNs.
*   Operate and manage an established peering arrangement for content delivery.

**Key Constraints**:
*   Request redirection must occur across distributed servers of multiple providers without full system information.
*   Implementation models for attributes like server load or network delay are based on heuristics.
*   The system must satisfy individual provider SLAs while meeting obligations to the peering group.