# Detailed Summary: Virtual Company Dossier (VCD) Requirements Specification

## Background and Scope
The Virtual Company Dossier (VCD) is a key component of the PEPPOL project, aiming to enable cross-border electronic public procurement by providing interoperable solutions for economic operators to submit required company information electronically. The VCD serves as a container for documents and data needed to prove selection and exclusion criteria as per Directive 2004/18/EC. The scope includes developing a staged maturity model from basic mapping to advanced networked solutions, focusing on interoperability while respecting national variations. Non-goals include creating new attestation standards or altering national legal frameworks.

## Stakeholders Matrix and Use Cases
- **Economic Operator**: Submits VCD to prove qualification; uses VCD services to compile and submit dossiers.
- **Contracting Authority**: Receives and evaluates VCDs; specifies criteria in calls for tender.
- **Issuing Body**: Provides attestations and certificates (public/private).
- **National VCD Service Provider**: Hosts VCD systems, acts as trusted third party.
- **European Service Provider**: Maintains pre-VCD mapping tool for cross-border interoperability.
- **Translator**: Provides certified translations of evidences when required.
- **Publication Body**: Publishes contract notices and tender details.
- **Officer**: Manages identity and access for VCD accounts.

**Main Scenarios**: Economic operator compiles VCD for foreign tender; contracting authority evaluates foreign VCD; pre-VCD mapping consultation.
**Exception Scenarios**: Missing attestations handled via declarations; consortium VCD merging; on-demand evidence retrieval.

## Business Process
**Main Process (VCD Creation & Submission)**:
1. Contracting authority publishes call for tender with criteria.
2. Economic operator retrieves tender details.
3. Economic operator uses pre-VCD mapping to identify required national evidences.
4. Economic operator requests VCD compilation via national service provider.
5. VCD system collects evidences from issuing bodies and economic operator.
6. VCD system compiles package with metadata and translations.
7. Economic operator submits VCD to contracting authority via transport infrastructure.
8. Contracting authority reviews VCD for compliance.

**Key Branch A (Two-Phase Tendering)**: Economic operator submits self-declarations first, followed by full evidences upon request.
**Key Branch B (Consortium Bidding)**: Multiple economic operators merge their VCDs into a single package for joint submission.

## Domain Model
Entities (≤8):
- **VCD Package**: Unique ID, creation date, service provider ID (required), tender reference (reference).
- **Economic Operator**: Company ID, VAT number, registration details (required/unique).
- **Evidence**: Document ID, type (attestation/statement), issuer, issue date, expiry date (required).
- **Criteria**: European criterion ID, national mapping, description (required/unique).
- **Issuing Body**: Body ID, type (public/private), country (required).
- **Contracting Authority**: Authority ID, country, contact details (required).
- **Tender**: Tender ID, publishing date, criteria list (required/unique).
- **Translation**: Translation ID, original evidence reference, language, certification status (required/reference).

## Interfaces and Integrations
1. **Pre-VCD Mapping Tool**: System: European Service Provider; Direction: Both; Interaction: Criteria-evidence mapping; Input: Tender criteria; Output: Mapped national evidences; SLA: High availability, daily updates.
2. **National VCD System**: System: National Service Provider; Direction: Inbound; Interaction: Evidence collection; Input: Evidence requests; Output: Compiled VCD; SLA: Secure, reliable compilation.
3. **PEPPOL Transport Infrastructure**: System: WP8 Infrastructure; Direction: Both; Interaction: VCD submission; Input: VCD package; Output: Delivery confirmation; SLA: Secure, non-repudiable transport.
4. **Issuing Body Interface**: System: Public/Private Registries; Direction: Inbound; Interaction: Evidence retrieval; Input: Access requests; Output: Evidence documents; SLA: Variable per issuer.
5. **Tendering Platform**: System: eProcurement Systems; Direction: Inbound; Interaction: VCD receipt; Input: VCD package; Output: Integration confirmation; SLA: Compatibility with VCD format.
6. **Identity Management**: System: National/EU Systems; Direction: Both; Interaction: Authentication; Input: Credentials; Output: Access rights; SLA: Single sign-on support.

## Acceptance Criteria
**Capability: VCD Compilation**
- Given an economic operator with valid credentials, when they request a VCD for a specific tender, then the system suggests required evidences based on pre-VCD mapping.
- Given incomplete evidence collection, when the VCD is compiled, then the system highlights missing items and allows placeholder insertion.

**Capability: Cross-Border Submission**
- Given a compiled VCD, when the economic operator submits it to a foreign contracting authority, then the VCD is delivered intact via secure transport.
- Given a received VCD, when the contracting authority reviews it, then they can view all evidences and metadata in a structured format.

## Non-Functional Metrics
- **Performance**: VCD compilation within 5 minutes; mapping queries under 10 seconds.
- **Reliability**: System availability 99.5%; data integrity ensured via validation.
- **Security**: Secure authentication; encrypted transport; compliance with data protection laws.
- **Compliance**: Adherence to Directive 2004/18/EC; national procurement act alignment.
- **Observability**: Audit trails for VCD actions; monitoring of service performance.

## Milestones and Release Strategy
1. Finalize pre-VCD mapping specification (Stage 1).
2. Develop VCD simple package prototype (Stage 2).
3. Pilot implementations in Austria and Italy (Stages 2-3).
4. Integrate with PEPPOL transport infrastructure.
5. Expand to additional Member States (Stage 4 pilots).
6. Establish governance model for long-term maintenance.

## Risk List and Mitigation Strategies
1. **Legal Fragmentation**: Mitigation: Align with EU directives; use mutual recognition principles.
2. **Technical Interoperability**: Mitigation: Adopt common standards (CEN BII, XML).
3. **Stakeholder Resistance**: Mitigation: Engage early via forums; demonstrate benefits.
4. **Data Privacy Concerns**: Mitigation: Implement strict access controls; comply with national laws.
5. **Translation Complexity**: Mitigation: Use context-specific data; allow certified translations.
6. **Sustainability Post-Project**: Mitigation: Define governance and funding models early.
7. **Varying National Maturity**: Mitigation: Staged approach allows incremental adoption.
8. **Security Threats**: Mitigation: Regular audits; use trusted infrastructure.

## Undecided Issues and Responsible Parties
1. **Governance Model for European Service Provider**: Responsible: PEPPOL Steering Committee.
2. **Funding for Long-Term Maintenance**: Responsible: European Commission and Member States.
3. **Legal Liability of National Service Providers**: Responsible: National legal authorities.
4. **Standardization of Context-Specific Data**: Responsible: CEN BII and WP2 team.
5. **Integration with Article 52 Lists**: Responsible: Member States with existing implementations.
6. **Handling of Dynamic Legal Changes**: Responsible: European Service Provider.
7. **Acceptance of Electronic Signatures Across Borders**: Responsible: WP1 and legal experts.
8. **Cost Allocation for VCD Services**: Responsible: National service providers and users.