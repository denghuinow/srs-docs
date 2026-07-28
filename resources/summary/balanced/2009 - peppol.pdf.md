# Balanced Summary: PEPPOL Virtual Company Dossier (VCD) Requirements

## Goals and Scope
The Virtual Company Dossier (VCD) aims to enable economic operators across Europe to electronically submit standardized company information and qualification documents to any public contracting authority, facilitating cross-border public procurement. It focuses on interoperability solutions for proving selection and exclusion criteria as per Directive 2004/18/EC, reducing administrative burden through a staged maturity model.

## Stakeholders and User Stories
- **Economic Operator**: A company seeking public contracts; responsible for providing qualification documents.
- **Contracting Authority**: Public entity procuring goods/services; evaluates bids and qualification documents.
- **Issuing Body**: Organization (public/private) that issues certificates/attestations (e.g., commercial registers).
- **National VCD Service Provider**: Hosts VCD systems and services within a Member State.
- **European Service Provider**: Maintains the pre-VCD mapping tool for cross-border interoperability.
- **Translator**: Provides certified translations of documents when required.

**User Stories** (≤6):
1. As an economic operator, I want to compile a VCD package from existing registries so that I can prove my qualifications for a foreign tender.
2. As a contracting authority, I want to receive and interpret VCD packages electronically so that I can efficiently evaluate bidders' suitability.
3. As an issuing body, I want to provide attestations through automated services so that economic operators can include them in their VCD.
4. As a national VCD service provider, I want to offer compilation and validation services so that economic operators can create trusted VCD packages.
5. As a European service provider, I want to maintain a mapping of criteria to national evidences so that cross-border tender requirements are transparent.
6. As an economic operator, I want to reuse and update existing VCD packages so that I can reduce effort for new tenders.

## Key Processes
1. **Pre-VCD Mapping (Trigger: Tender publication)**: European criteria are mapped to national attestations via a mapping tool.
2. **VCD Compilation (Trigger: Economic operator decides to bid)**: The economic operator uses national VCD services to collect and assemble required documents.
3. **Evidence Collection (Trigger: Compilation request)**: Attestations are retrieved from issuing bodies, manually added, or translated.
4. **Package Submission (Trigger: VCD completion)**: The VCD is sent to the contracting authority via transport infrastructure.
5. **VCD Viewing (Trigger: Receipt by contracting authority)**: The authority accesses and reviews the VCD contents.
6. **Suitability Evaluation (Trigger: VCD review)**: The authority checks documents against tender criteria.
7. **VCD Re-compilation (Trigger: Document expiry or new tender)**: Existing VCDs are updated or reused for efficiency.

## Domain Data Elements
- **VCD Package** (Primary Key: VCD ID): Structural package data, tender-specific data, economic operator data.
- **Evidence** (Primary Key: Document ID): Document content, structural metadata (issuer, date, expiry), context-specific data.
- **Economic Operator** (Primary Key: Company ID): Name, registration number, VAT number, legal status.
- **Issuing Body** (Primary Key: Issuer ID): Name, type (public/private), service endpoints.
- **Tender** (Primary Key: TED ID): Criteria subset, contracting authority, publication date.
- **Translation** (Primary Key: Translation ID): Original document reference, target language, translator certification.

## Non-Functional Requirements
1. **Security**: VCD transport must ensure confidentiality, integrity, and non-repudiation.
2. **Reliability**: Systems must be highly available and deliver documents reliably.
3. **Interoperability**: Solutions must align with European standards (e.g., CEN BII profiles).
4. **Usability**: Services should support organizations of any size, including SMEs.
5. **Maintainability**: Mapping tools and VCD schemas must be easily updatable.
6. **Legal Compliance**: Must adhere to data protection, e-signature, and procurement directives.

## Milestones and External Dependencies
1. **Stage 1 Implementation**: Pre-VCD mapping tool deployment (dependent on DG MARKT collaboration).
2. **Pilot Rollouts**: Austrian and Italian VCD implementations (dependent on national infrastructures).
3. **Stage 2+ Pilots**: Expansion to other Member States (dependent on PEPPOL enlargement).
4. **Standards Alignment**: Integration with CEN BII profiles and PEPPOL infrastructure (WP8).
5. **Legal Harmonization**: Mutual recognition agreements across Member States.

## Risks and Mitigation Strategies
1. **Legal Fragmentation**: Divergent national laws may hinder mutual recognition; mitigate through legal analysis and EU-level agreements.
2. **Technical Complexity**: Heterogeneous systems increase integration costs; mitigate by using staged maturity and existing standards.
3. **Stakeholder Resistance**: Issuing bodies may be reluctant to automate; mitigate by demonstrating benefits and phased adoption.
4. **Data Privacy Concerns**: Cross-border data exchange raises privacy issues; mitigate with strict access controls and compliance with data protection laws.
5. **Sustainability**: Post-project maintenance risks; mitigate by establishing clear governance models and funding mechanisms.

## Undecided Issues
1. Governance model for European and national service providers (liability, funding).
2. Scope of mutual recognition for candidate statements and Article 52 implementations.
3. Technical approach for context-specific data schemas (e.g., use of XBRL, OWL).
4. Handling of two-phased tendering within VCD processes.
5. Long-term strategy for translating attestations versus using context-specific data.
6. Integration details with existing eTendering platforms and PEPPOL transport infrastructure.