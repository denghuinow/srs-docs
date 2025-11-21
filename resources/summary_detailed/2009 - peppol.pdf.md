# Detailed Summary

## Background and Scope
The Virtual Company Dossier (VCD) aims to enable economic operators across Europe to electronically submit qualification documents to any public contracting authority, supporting cross-border eProcurement interoperability. It addresses the current fragmented landscape where national attestations and procedures differ significantly. The scope covers four maturity stages from basic mapping to advanced networked solutions, focusing on evidence for selection/exclusion criteria per Directive 2004/18/EC Articles 45–50. Non-goals include creating new attestation standards or altering national legal frameworks.

## Role Matrix and Use Cases
**Roles:** Economic Operator, Contracting Authority, Issuing Body, National VCD Service Provider, European Service Provider, Translator.  
**Main Scenarios:**  
- Economic operator compiles VCD for foreign tender using mapping tool.  
- Contracting authority validates submitted VCD against criteria.  
- Issuing bodies provide electronic attestations to VCD system.  
**Exception Scenarios:**  
- Missing attestations handled via candidate statements.  
- Conflict resolution for "on-demand" evidence retrieval failures.

## Business Process
**Main Process (VCD Compilation):**  
1. Economic operator authenticates to VCD system.  
2. System retrieves tender criteria via pre-VCD mapping.  
3. Operator selects/confirms evidence compilation.  
4. System collects attestations from issuing bodies.  
5. Operator uploads manual evidences/translations.  
6. System compiles VCD package.  
7. Operator submits VCD to contracting authority via PEPPOL infrastructure.  
8. Authority reviews VCD validity and contents.  
**Key Branches:**  
- **Recompilation:** Update expired evidences; reuse valid ones.  
- **Consortium Handling:** Merge multiple operator VCDs into single package.

## Domain Model
**Entities:**  
- VCD Package (ID, issueDate, validityPeriod; required/unique).  
- Economic Operator (VAT, registrationNumber; required/unique).  
- Attestation (type, issuer, issueDate, expiry; required).  
- Criteria (article, description; required).  
- Tender (TED-ID, criteriaSubset; required).  
- Issuing Body (name, type; required).  
- Translation (language, certifiedFlag; required for foreign submissions).  
- Context Data (keyValues, schemaVersion; reference to Attestation).

## Interfaces and Integrations
- **Pre-VCD Mapping Tool:** Direction: Both; Theme: Criteria-evidence mapping; Input: Tender criteria; Output: Mapped attestations list; SLA: 5-day update on legal changes.  
- **National Issuing Bodies:** Direction: Inbound; Theme: Evidence retrieval; Input: Operator identifiers; Output: Structured attestations; SLA: High availability for automated services.  
- **PEPPOL Transport:** Direction: Outbound; Theme: Secure VCD delivery; Input: VCD package; Output: Delivery confirmation; SLA: Non-repudiation and integrity.  
- **Tendering Platforms:** Direction: Outbound; Theme: VCD submission; Input: VCD package; Output: Receipt acknowledgment; SLA: Compatibility with platform APIs.

## Acceptance Criteria
- **Given** a foreign tender with specified criteria, **when** an economic operator uses the VCD system, **then** the system suggests compliant national attestations.  
- **Given** a compiled VCD, **when** a contracting authority reviews it, **then** they can verify evidence validity and criteria fulfillment.  
- **Given** outdated evidences, **when** an operator requests recompilation, **then** the system updates expired items while retaining valid ones.

## Non-Functional Metrics
- **Performance:** VCD compilation under 10 minutes; mapping queries under 5 seconds.  
- **Reliability:** 99.5% uptime for VCD services; secure storage with audit trails.  
- **Security:** PKI-based authentication; data encryption in transit and at rest.  
- **Compliance:** Adherence to EU data protection laws and eSignature directives.  
- **Observability:** Logging of all VCD transactions; monitoring for SLA breaches.

## Milestones and Release Strategy
1. Finalize pre-VCD mapping tool specification (Q3 2009).  
2. Pilot Stage 2 VCD simple package in Austria and Italy (Q4 2009).  
3. Develop Stage 3 context-data schemas (Q1 2010).  
4. Implement Stage 4 "on-demand" features in select pilots (Q2 2010).  
5. Expand to additional Member States (Q3 2010).  
6. Full operational rollout with governance model (2011).

## Risk List and Mitigation Strategies
- **Legal Heterogeneity:** Mitigation: Align with DG MARKT for mutual recognition agreements.  
- **Technical Interoperability:** Mitigation: Adopt CEN BII and PEPPOL infrastructure standards.  
- **Stakeholder Adoption:** Mitigation: Phased rollout with training and support.  
- **Data Security:** Mitigation: Implement end-to-end encryption and access controls.  
- **Translation Costs:** Mitigation: Promote context-data to reduce need for full translations.  
- **Sustainability:** Mitigation: Establish European service provider for long-term maintenance.  
- **Liability Issues:** Mitigation: Define clear roles for national VCD providers.  
- **Scope Creep:** Mitigation: Prioritize Articles 45–46 evidences initially.

## Undecided Issues and Responsible Parties
- Governance model for European VCD service provider (PEPPOL Steering Committee).  
- Funding mechanism for long-term maintenance (European Commission).  
- Legal equivalence of context-data vs. certified translations (National legal experts).  
- Integration with Article 52 approved lists (Not mentioned).  
- Standardization of context-data schemas (CEN BII/WP2 collaboration).  
- Liability for VCD service providers (National legislatures).  
- Handling of non-EU/EEA economic operators (Not mentioned).  
- Dispute resolution procedures for cross-border conflicts (PEPPOL Legal Team).