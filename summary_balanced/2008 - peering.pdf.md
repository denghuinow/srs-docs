# Balanced Summary

**Goals and scope**
This system enables internetworking of Content Delivery Networks (CDNs) through peering to allow coordinated content delivery across multiple providers. It aims to handle flash crowds and demand spikes by sharing resources between CDNs while maintaining individual service level agreements. The scope includes developing peering models, protocols for cooperative service delivery, and autonomic management policies.

**Roles and user stories**
- *Primary CDN Operator*: I want to trigger peering during traffic surges so that I can maintain service quality for my customers
- *Peering CDN Operator*: I want to negotiate resource sharing terms so that I can monetize my excess capacity
- *Content Provider*: I want my content delivered reliably so that end-users receive consistent quality of service
- *End-user*: I want fast content access so that I have a positive browsing experience
- *System Administrator*: I want to monitor peering arrangements so that I can ensure operational efficiency

**Key processes**
1. Service registration triggered when CDN resources become available or need updating
2. Peering initiation triggered when a CDN cannot handle its workload
3. Relationship negotiation triggered by mediator receiving initiation request
4. Resource discovery triggered by service requirements passed to Peering Agent
5. Protocol configuration triggered after peering arrangement establishment
6. Operational management triggered when peering becomes active
7. Disband/re-arrangement triggered when termination conditions are met

**Domain data elements**
- *Web Server*: server_id, capacity, current_load, location, content_cache
- *Service Registry*: registry_id, resource_list, access_policies, update_timestamp
- *Policy Repository*: policy_id, policy_type, rules, validity_period, scope
- *Mediator*: mediator_id, negotiation_capabilities, service_requirements
- *Peering Agent*: agent_id, discovery_capabilities, peer_contacts
- *Peering Arrangement*: arrangement_id, participants, terms, duration, status

**Non-functional requirements**
- Support for both short-term (automated) and long-term (human-directed) peering
- Policy-driven resource discovery with privacy preservation
- Modular implementation approach for testing and validation
- Integration with existing Web services technologies
- Cryptographic security for content replication
- Distributed load measurement and dissemination

**Milestones and external dependencies**
- Development of peering protocols and negotiation mechanisms
- Implementation of resource discovery and load distribution
- Integration with existing CDN infrastructures
- Testing on real-world platforms like PlanetLab
- Leveraging inspiration from systems like CoDeeN, Coral, and MotusNet

**Risks and mitigation strategies**
- Limited information sharing between proprietary CDNs: Use policy-driven visibility controls
- Dynamic attribute variability: Implement heuristic-based decision making
- Complex multi-provider coordination: Develop standardized interaction protocols
- SLA violations in peering arrangements: Define clear consequence policies
- Rapid response requirements for flash crowds: Automate short-term negotiations

**Undecided issues**
- Specific cryptographic framework for secure auctions
- Exact load measurement and dissemination mechanism
- Detailed request assignment and redirection algorithms
- Comprehensive user documentation structure
- Final implementation technology stack
- Not mentioned