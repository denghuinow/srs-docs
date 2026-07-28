# Software Requirements Specification (SRS)
## PEPPOL Virtual Company Dossier (VCD) System

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the PEPPOL Virtual Company Dossier (VCD) system. The VCD is a pan-European interoperability solution designed to standardize and digitalize the exchange of company qualification documents in public procurement. This document serves as a foundation for system architects, developers, testers, project managers, and stakeholders involved in the implementation.

#### 1.2 Scope
The VCD system enables Economic Operators (EOs) across the European Union to electronically compile, submit, and maintain a standardized dossier of company information and attestations. This dossier is used to prove compliance with selection and exclusion criteria defined in public tender notices (Directive 2004/18/EC). The system facilitates interactions between EOs, Contracting Authorities (CAs), Issuing Bodies, and service providers, reducing administrative burden and fostering cross-border procurement.

**In-Scope:**
*   Pre-VCD mapping of EU procurement criteria to national evidence types.
*   Compilation, validation, and submission of VCD packages.
*   Automated and manual evidence collection from trusted sources.
*   Secure cross-border transport and viewing of VCD packages.
*   Evaluation of VCD contents against tender criteria.
*   Update and reuse of existing VCD packages for new tenders.

**Out-of-Scope:**
*   The actual eTendering or eSubmission of bids (complementary to these processes).
*   The internal business processes of Issuing Bodies (integration only).
*   The financial transaction aspects of procurement.
*   Mandating the adoption by Member States (system supports voluntary use).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **VCD** | Virtual Company Dossier. The standardized electronic package of company data and evidences. |
| **EO** | Economic Operator. A company or entity seeking a public contract. |
| **CA** | Contracting Authority. A public body issuing a tender. |
| **PEPPOL** | Pan-European Public Procurement Online. The overarching network and standards framework. |
| **CEN BII** | European Committee for Standardization Business Interoperability Interfaces. A set of standardized profiles for eProcurement. |
| **TED** | Tenders Electronic Daily. The EU's official journal for public procurement. |
| **SME** | Small and Medium-sized Enterprise. |
| **WP8** | Work Package 8 of the PEPPOL project, relevant for infrastructure alignment. |

#### 1.4 References
*   Directive 2004/18/EC of the European Parliament and of the Council on public procurement.
*   PEPPOL Architecture Specifications.
*   CEN/BII Workshop Agreements and Profiles.
*   Relevant EU Data Protection Regulations (e.g., GDPR).

#### 1.5 Overview
The remainder of this SRS is structured as follows: Section 2 provides a general description of the product, its stakeholders, and operating environment. Section 3 details the specific functional and data requirements. Section 4 outlines all non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
The VCD system is a component within the larger PEPPOL eProcurement ecosystem. It interfaces with:
*   **External Systems:** National business registries, eTendering platforms, the TED, and Issuing Body backend systems.
*   **PEPPOL Core Infrastructure:** The PEPPOL transport infrastructure (Access Points) for secure document exchange.
*   **Supporting Tools:** The pre-VCD mapping tool maintained by the European Service Provider.

It is designed as a decentralized system, with National VCD Service Providers offering services within their jurisdictions, interconnected via common standards.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Economic Operator (EO)** | Varies from SMEs to large corporations. May have limited IT resources. | Compile and submit qualification documents efficiently; reduce repetitive administrative work. |
| **Contracting Authority (CA)** | Public administration staff. Evaluates many bids. | Receive standardized, verifiable qualification data; accelerate bidder suitability checks. |
| **Issuing Body** | Public or private registry (e.g., commercial court, tax authority). Custodian of official data. | Provide authenticated data feeds/services; maintain control and integrity of their data. |
| **National VCD Service Provider** | IT service provider or government agency. Operates national VCD node. | Offer reliable, compliant VCD services; ensure national legal and technical adherence. |
| **European Service Provider** | EU-level entity (e.g., managed by DG MARKT). | Maintain central mapping tools and standards; ensure cross-border interoperability. |
| **Translator** | Certified translation service. | Provide legally recognized translations of evidentiary documents. |

#### 2.3 Operating Environment
*   **Technical:** System components must operate in a heterogeneous IT landscape across EU Member States. Must support web-based interfaces and machine-to-machine (M2M) web services (SOAP/REST).
*   **Legal:** Must operate under the legal frameworks of multiple jurisdictions, including data protection (GDPR), eIDAS (e-signatures), and national procurement laws.
*   **Organizational:** Relies on the cooperation of disparate national and European organizations.

#### 2.4 Design and Implementation Constraints
1.  **Standards Compliance:** Must implement CEN BII profiles and PEPPOL specifications for document formats and transport.
2.  **Staged Maturity Model:** Implementation must follow a phased approach (Stage 1, Pilot, Stage 2+).
3.  **Decentralized Governance:** Architecture cannot assume a single central database; data sovereignty remains with national entities/EOs.
4.  **Legacy System Integration:** Must accommodate integration with existing national registries and eGovernment systems.

### 3. System Features and Requirements

#### 3.1 Functional Requirements

**FR-1: Pre-VCD Mapping Management**
*   **FR-1.1:** The European Service Provider's mapping tool shall allow the mapping of EU-wide procurement selection/exclusion criteria (from TED notices) to nationally recognized types of evidence/attestations.
*   **FR-1.2:** The mapping shall be publicly accessible to EOs and CAs to ensure transparency of cross-border requirements.

**FR-2: VCD Compilation & Assembly**
*   **FR-2.1:** The system shall allow an EO (or a service provider on their behalf) to initiate a new VCD package for a specific tender (identified by TED ID).
*   **FR-2.2:** The system shall present the EO with a list of required evidences based on the tender criteria and the pre-VCD mapping.
*   **FR-2.3:** The system shall support multiple evidence collection methods:
    *   **FR-2.3.1:** Automated retrieval from registered Issuing Body web services.
    *   **FR-2.3.2:** Manual upload of scanned documents by the EO.
    *   **FR-2.3.3:** Request and inclusion of certified translations.

**FR-3: Evidence Validation & Package Signing**
*   **FR-3.1:** The National VCD Service Provider's system shall validate the structural integrity and metadata (issuer, date, expiry) of all evidences added to a VCD.
*   **FR-3.2:** The completed VCD package shall be digitally signed by the EO (or the National Service Provider acting on their authority) to ensure authenticity and non-repudiation.

**FR-4: VCD Submission & Transport**
*   **FR-4.1:** The system shall package the VCD according to the PEPPOL VCD schema (e.g., UBL format).
*   **FR-4.2:** The VCD package shall be transmitted to the designated Contracting Authority via the PEPPOL transport infrastructure (via Access Points), ensuring end-to-end confidentiality and integrity.

**FR-5: VCD Reception & Viewing**
*   **FR-5.1:** The CA's system shall receive and acknowledge VCD packages via the PEPPOL network.
*   **FR-5.2:** The system shall provide the CA with a user interface to view the contents of the VCD, including EO data, the list of evidences, and the ability to open/view individual evidentiary documents.

**FR-6: Suitability Evaluation Support**
*   **FR-6.1:** The system shall allow the CA to mark evidences as "reviewed" and record an evaluation status (e.g., compliant, non-compliant, pending) against each tender criterion.
*   **FR-6.2:** The system shall maintain an audit log of all access and evaluation actions performed on a VCD by the CA.

**FR-7: VCD Lifecycle Management**
*   **FR-7.1:** The system shall allow an EO to save a "master" VCD copy independent of any specific tender.
*   **FR-7.2:** The system shall allow an EO to clone and update an existing VCD (master or previous submission) for a new tender, triggering re-validation of expired or updated evidences.
*   **FR-7.3:** The system shall manage the retention period of VCD packages in accordance with national and EU archival regulations.

#### 3.2 Data Requirements & Domain Model
Core data entities and their key attributes:

```xml
<!-- Conceptual Schema Example -->
<Entities>
    <VCD_Package VCD_ID="[UUID]">
        <TenderReference>TED_ID</TenderReference>
        <CompilationDate/>
        <EO_Reference>Company_ID</EO_Reference>
        <DigitalSignature/>
        <Contains>Evidence_ID(s)</Contains>
    </VCD_Package>

    <Evidence Document_ID="[UUID]">
        <Type>e.g., BusinessRegistrationCertificate</Type>
        <Issuer>Issuer_ID</Issuer>
        <IssueDate/>
        <ExpiryDate/>
        <Content>Base64 or URL reference</Content>
        <ContextSpecificData/> <!-- e.g., XBRL snippet -->
    </Evidence>

    <Economic_Operator Company_ID="[Legal Identifier]">
        <LegalName/>
        <RegistrationNumber/>
        <VATNumber/>
        <LegalStatus/>
    </Economic_Operator>

    <Issuing_Body Issuer_ID="[Code]">
        <Name/>
        <Type>Public/Private</Type>
        <ServiceEndpoint/>
    </Issuing_Body>
</Entities>
```

### 4. Non-Functional Requirements

#### 4.1 Security Requirements
*   **SEC-1:** All cross-border VCD transmissions shall use the PEPPOL transport infrastructure, which provides PKI-based encryption (confidentiality) and digital signatures (integrity & non-repudiation).
*   **SEC-2:** Access to VCD compilation services shall require strong electronic identification (eIDAS compliant).
*   **SEC-3:** The system shall implement role-based access control (RBAC) to ensure CAs can only access VCDs submitted to their tenders.
*   **SEC-4:** All personal data within VCDs shall be handled in accordance with GDPR principles (lawfulness, minimization, storage limitation).

#### 4.2 Reliability & Availability
*   **REL-1:** National VCD service platforms shall target 99.5% operational availability during core business hours.
*   **REL-2:** The system shall provide reliable delivery receipts for all VCD submissions.
*   **REL-3:** Critical evidence retrieval services from Issuing Bodies shall implement retry mechanisms for transient failures.

#### 4.3 Interoperability & Compliance
*   **INT-1:** VCD document syntax shall conform to the future CEN BII VCD profile and UBL schema.
*   **INT-2:** Machine-to-machine interfaces (for evidence retrieval) shall be described using standard web service definitions (WSDL/OpenAPI).
*   **INT-3:** The system shall be compatible with the PEPPOL SMP (Service Metadata Publisher) and SML (Service Metadata Locator) for dynamic discovery of participant endpoints.

#### 4.4 Usability
*   **USA-1:** The EO and CA web interfaces shall be designed for clarity, requiring minimal training for users familiar with basic procurement concepts.
*   **USA-2:** Interfaces shall be available in multiple EU languages.
*   **USA-3:** The compilation process shall provide clear guidance, especially for SME users, on what evidences are required and how to obtain them.

#### 4.5 Maintainability & Scalability
*   **MNT-1:** The pre-VCD mapping tool shall allow administrators to update criteria-evidence mappings without requiring software code changes.
*   **MNT-2:** The VCD schema shall be versioned. Systems shall be capable of handling multiple schema versions during transition periods.
*   **SCA-1:** The architecture shall support scaling to accommodate all EU Member States and a high volume of tenders.

#### 4.6 Legal & Regulatory
*   **LAW-1:** The system's operational model (liability of service providers, data ownership) shall be defined in a governance agreement.
*   **LAW-2:** The legal validity of electronically obtained evidences and VCD signatures must be recognized across participating jurisdictions (mutual recognition).

---
**Appendix A: Open / Undecided Issues**
1.  The definitive governance and funding model for European and National Service Providers.
2.  The technical standard for expressing context-specific data within evidences (XBRL, OWL, other).
3.  The detailed process integration with two-phase tendering procedures.
4.  The long-term strategy for handling language barriers (machine-readable data vs. human translation).
5.  Final integration specifications with major eTendering platforms.

**Appendix B: Assumptions & Dependencies**
*   Successful collaboration with DG MARKT on the pre-VCD mapping tool.
*   Availability and cooperation of national IT infrastructures in pilot countries (Austria, Italy).
*   Continued evolution and adoption of the PEPPOL network and CEN BII standards.
*   Progress on EU-level legal harmonization regarding the mutual recognition of electronic attestations.