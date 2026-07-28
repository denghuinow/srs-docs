# Short Summary: OpenSG EIM System Requirements Specification

## Background and Objectives
This document defines the system requirements for an Enterprise Information Management (EIM) strategy to address interoperability challenges in the Smart Grid. It aims to establish a consistent framework for managing and sharing information across business processes and systems.

## In Scope
- Defining an EIM framework and reference architecture based on TOGAF 9.0.
- Establishing business, application, data, and technical architecture views.
- Incorporating the IEC Common Information Model (CIM) for semantic interoperability.
- Addressing information security within each architectural component.
- Creating governance structures through an EIM Competency Center.

## Out of Scope
- Detailed implementation processes for specific systems.
- Expansion of individual data structures beyond the enterprise semantic model.
- Specific hardware or software product selections.
- Non-Smart Grid data management treated in isolation.
- Project-level architectural requirements without enterprise context.

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Utility Companies (e.g., AEP, ONCOR):** Provide business requirements and operational insights for Smart Grid data management.
- **Technology Providers (e.g., Xtensible Solutions):** Contribute technical expertise for system architecture and integration.
- **Standards Bodies (e.g., The Open Group):** Offer frameworks like TOGAF for guiding architecture development.
- **End Consumers (B2C):** Require secure and reliable access to their energy data.
- **EIM Competency Center:** Governs the adoption and maintenance of the EIM strategy across the organization.
- **System Integrators:** Implement and maintain the EIM framework to ensure interoperability.

**Core Use Cases:**
1. As a utility company, I want to share a common data model with external entities so that we achieve semantic interoperability.
2. As a technology provider, I want to incorporate IEC CIM into the EIM so that messaging and data stores are standards-based.
3. As an end consumer, I want secure access to my energy usage data so that I can manage consumption effectively.
4. As the EIM Competency Center, I want to introduce data movement patterns and tools so that the organization can reuse logical data models.
5. As a system integrator, I want clear architectural requirements so that I can design self-healing and discoverable interfaces.
6. As a business unit, I want joint Smart Grid and non-Smart Grid data management so that operational processes are unified.

## Success Metrics
- Achievement of semantic interoperability across all integrated systems.
- Successful incorporation of IEC CIM into enterprise data architecture.
- Establishment of a governed EIM Competency Center with adopted patterns.

## Major Constraints
- Dependence on existing standards and frameworks like TOGAF and IEC CIM.
- Need to integrate both Smart Grid and non-Smart Grid data requirements.
- Requirement to address information security across all architectural views.
- Organizational resistance to new data management patterns and tools.
- Balancing centralized vs. localized data store requirements.

## Undecided Issues
- Resolution of EIM support for process-oriented information perspectives.
- Definition of patterns for interfacing new technologies with legacy systems.
- Specific approaches for initiating and maintaining enterprise semantic management.
- Detailed breakdown of logical EIM capabilities like data validation.
- Methods for enhancing logical data model creation and reuse.