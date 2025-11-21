# Short Summary

- **Background and objectives**: This specification defines requirements for enabling internetworking between distinct Content Delivery Networks (CDNs) through peering, allowing providers to scale resources cooperatively and handle flash crowds or demand spikes more effectively.

- **In scope**:
  - Models and protocols for CDN peering and service delivery in a cooperative environment.
  - Resource discovery and negotiation mechanisms between peered CDNs.
  - Operational management of peering arrangements including content replication and request routing.
  - Policies for autonomic management of service levels and resource negotiation.
  - Disbanding or re-arrangement of peering arrangements under defined conditions.

- **Out of scope**:
  - Full details of proprietary CDN internal algorithms and architectures.
  - Implementation of underlying network infrastructure or hardware.
  - Detailed financial or legal aspects of service agreements.
  - User interface design specifications.
  - Specific cryptographic or security protocol implementations.

- **Roles and core use cases**:
  - As a **primary CDN**, I want to initiate peering with other CDNs so that I can handle unexpected traffic surges.
  - As a **peering CDN**, I want to share resources and policies so that I can participate in cooperative content delivery.
  - As an **end-user**, I want to access content seamlessly so that I experience reduced latency and improved QoS.

- **Success metrics**:
  - Reduced content delivery latency and improved QoS for end-users.
  - Effective handling of flash crowds and traffic spikes without service degradation.
  - Successful establishment and operational management of peering arrangements.

- **Major constraints**:
  - Limited visibility into proprietary CDN performance and load information.
  - Need to support both short-term and long-term peering arrangements.
  - Reliance on heuristic-based attributes for implementation decisions.
  - Requirement to interoperate with existing Web services and protocols.
  - Ensuring SLA compliance across multiple autonomous providers.

- **Undecided issues**:
  - Specific performance prediction models for peer selection.
  - Exact formats for service requirement and policy descriptions.
  - Detailed interaction protocols between all system components.
  - Not mentioned.
  - Not mentioned.