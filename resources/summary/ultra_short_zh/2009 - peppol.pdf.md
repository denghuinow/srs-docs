Purpose & Scope  
The VCD enables economic operators to submit cross-border evidence for public procurement under Directive 2004/18/EC. It focuses on evidence for selection/exclusion criteria (Articles 45-50), not on creating common attestations. The solution follows a staged approach (pre-VCD mapping, simple, advanced, network packages) to handle varying national interoperability maturity. It does not replace national evidence systems or handle document translation.

Product Background  
Part of PEPPOL's pan-European eProcurement initiative to address market fragmentation. Builds on existing national systems rather than replacing them. Targets public procurement processes where economic operators must prove qualification across EU borders, particularly addressing the current manual evidence collection burden.

Core Functionality  
1. Pre-VCD mapping: Semantic mapping of national evidence to European criteria (Stage 1)  
2. VCD simple package: Structured container for evidence with basic metadata (Stage 2)  
3. VCD advanced package: Adds context-specific data for decision support (Stage 3)  
4. VCD network package: "On-demand" evidence retrieval via national service providers (Stage 4)  
5. Support for self-declarations as evidence alternative  
6. Multi-language evidence handling with translation requirements  
7. Integration with PEPPOL infrastructure for transport  

Key Users & Scenarios  
Primary users: Economic operators (submitting evidence), Contracting authorities (receiving evidence), National VCD service providers (hosting systems). Main scenario: Economic operator from one Member State submitting evidence to contracting authority in another Member State for public tender. Secondary scenario: Economic operator using self-declarations when official evidence unavailable.

Main External Interfaces  
PEPPOL infrastructure (for VCD transport), National issuing systems (for evidence retrieval), Tendering platforms (for submission), Identity management systems (for authentication). Interfaces must support semantic interoperability and data integrity.

Key Non-Functional Requirements  
- Must ensure mutual recognition of evidence across Member States  
- Must maintain data integrity during transport  
- Must support authentication and non-repudiation  
- Must handle evidence in multiple languages  
- Must comply with Directive 2004/18/EC requirements  

Constraints, Assumptions & Dependencies  
- Must align with Directive 2004/18/EC Articles 45-50  
- Depends on national implementation of pre-VCD mapping  
- Relies on national service providers for VCD implementation  
- Assumes national systems provide evidence access  
- Requires legal alignment for self-declarations as evidence  

Priority & Acceptance  
Highest priority: Pre-VCD mapping (Stage 1) as foundational requirement. Stage 2 (simple package) as minimum viable product for cross-border evidence submission. Stage 3 (advanced) and Stage 4 (network) as future enhancements. Acceptance depends on legal alignment with procurement directives and national implementation of pre-VCD mapping.