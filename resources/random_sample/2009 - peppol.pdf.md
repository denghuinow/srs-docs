# Balanced Summary

## Goals and Scope
The Virtual Company Dossier (VCD) aims to enable economic operators to electronically submit qualification documents to any European public contracting authority. It focuses on interoperability solutions for cross-border public procurement by providing a structured package of required attestations and certificates. The scope covers four maturity stages from basic mapping to advanced networked solutions, addressing mutual recognition of documents across member states.

## Roles and User Stories
- **Economic Operator**: I want to compile required qualification documents electronically so that I can efficiently bid for public contracts across Europe.
- **Contracting Authority**: I want to receive and verify standardized company dossiers so that I can assess supplier suitability consistently.
- **Issuing Body**: I want to provide attestations through automated interfaces so that economic operators can access up-to-date certificates.
- **VCD Service Provider**: I want to operate trusted compilation services so that all parties can rely on dossier completeness and validity.
- **Translator**: I want to submit certified translations of documents so that language barriers don't hinder cross-border procurement.

## Key Processes
1. **Contract Notice Publication** (trigger: contracting authority initiates procurement)
2. **Criteria-Evidence Mapping** (trigger: economic operator identifies required documents)
3. **Document Collection** (trigger: VCD compilation request)
4. **VCD Package Compilation** (trigger: all documents collected)
5. **Secure Submission** (trigger: economic operator approves package)
6. **Document Verification** (trigger: contracting authority receives VCD)
7. **On-Demand Retrieval** (trigger: additional document request during evaluation)

## Domain Data Elements
- **VCD Package** (Primary Key: VCD-ID; Fields: CreationDate, ValidityPeriod, TenderReference, EconomicOperatorID, ServiceProviderID)
- **Economic Operator** (Primary Key: CompanyID; Fields: LegalName, VATNumber, RegistrationNumber, Address, ContactDetails)
- **Attestation** (Primary Key: DocumentID; Fields: Type, IssuingBody, IssueDate, ExpiryDate, ContentHash)
- **Tender** (Primary Key: TenderID; Fields: ContractingAuthority, PublicationDate, CriteriaList, SubmissionDeadline)
- **Issuing Body** (Primary Key: IssuerID; Fields: Name, AuthorityType, Country, ServiceEndpoint)
- **Translation** (Primary Key: TranslationID; Fields: OriginalDocumentID, TargetLanguage, TranslatorID, CertificationDate)

## Non-functional Requirements
- Secure document transmission with integrity protection
- Multi-language support for key document metadata
- System availability during business hours across time zones
- Compliance with data protection regulations
- Scalability to handle peak procurement periods
- Audit trail for all dossier access and modifications

## Milestones and External Dependencies
- Completion of pre-VCD mapping tool specification
- Pilot implementations in Austria and Italy
- Alignment with CEN/BII standardization activities
- Integration with PEPPOL transport infrastructure
- Coordination with DG MARKT mutual recognition initiatives

## Risks and Mitigation Strategies
- **Legal Recognition Differences**: Establish common interpretation guidelines and mutual recognition agreements
- **Technical Interoperability Issues**: Implement standardized interfaces and conduct conformance testing
- **Stakeholder Adoption Resistance**: Provide clear benefits demonstration and phased implementation approach
- **Data Security Concerns**: Implement robust authentication and encryption mechanisms
- **System Sustainability**: Define clear governance and funding models for long-term operation

## Undecided Issues
- Centralized vs decentralized pre-VCD mapping architecture
- Liability models for VCD service providers
- Funding mechanism for European-level service provision
- Standardization approach for context-specific data formats
- Integration strategy with existing national eProcurement systems
- Not mentioned