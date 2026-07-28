# Software Requirements Specification (SRS)
## Virtual Company Dossier (VCD) System
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Virtual Company Dossier (VCD) system, a core component of the PEPPOL (Pan-European Public Procurement Online) project. The VCD system enables economic operators to electronically compile, manage, and submit standardized company dossiers to prove selection and exclusion criteria in cross-border public procurement procedures within the European Union, as mandated by Directive 2004/18/EC.

#### 1.2 Document Conventions
*   **Shall / Must:** Indicates a mandatory requirement.
*   **Should:** Indicates a recommended, but not mandatory, requirement.
*   **May / Could:** Indicates an optional feature or capability.
*   **Bold:** Used for key terms and entity names.
*   `Code blocks`: Used for technical data examples or interface definitions.

#### 1.3 Scope
The VCD system provides an interoperable framework for the electronic submission of company qualification data. Its scope includes:
*   A staged maturity model for implementation, from basic criteria-evidence mapping to advanced networked evidence retrieval.
*   Services for economic operators to compile VCD packages against specific tender criteria.
*   Services for contracting authorities to receive and evaluate VCD packages.
*   Integration with national and European systems for evidence mapping, retrieval, and secure transport.
*   Respect for national legal variations in procurement evidence requirements.

**Out of Scope:**
*   Creation of new attestation or certification standards.
*   Alteration of existing national legal frameworks for public procurement.
*   Direct provision of attestations by issuing bodies (the system retrieves existing documents).

#### 1.4 References
*   Directive 2004/18/EC of the European Parliament and of the Council.
*   PEPPOL Project Architecture and Technical Specifications.
*   CEN BII (Business Interoperability Interfaces) Profiles.
*   Relevant national public procurement acts.

### 2. Overall Description

#### 2.1 Product Perspective
The VCD system is a component within the larger PEPPOL interoperability infrastructure. It interacts with several external systems as shown in the context diagram below.

```
[Economic Operator] <--> [National VCD System] <--> [PEPPOL Transport Infrastructure] <--> [Contracting Authority/Tendering Platform]
        ^                           ^                              ^
        |                           |                              |
[Pre-VCD Mapping Tool]     [Issuing Body Interfaces]      [Identity Management]
    (European Service)         (Public/Private Registries)   (National/EU Systems)
```

#### 2.2 User Classes and Characteristics
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **Economic Operator** | A company (or consortium) bidding for a public contract. | Primary system user. Varies in technical sophistication. Requires clear guidance. Needs to submit dossiers to authorities in different Member States. |
| **Contracting Authority** | A public body issuing a call for tender. | Evaluates submitted VCDs. Needs a structured, reliable, and verifiable view of the dossier. May use a local eProcurement system. |
| **Officer (System Admin)** | Personnel at the National VCD Service Provider. | Manages user identities, access rights, and system configuration. Requires administrative controls and audit capabilities. |
| **National VCD Service Provider** | Entity hosting and operating the national VCD system instance. | Acts as a trusted third party. Responsible for system availability, security, and compliance with national law. |
| **European Service Provider** | Entity maintaining the central pre-VCD mapping tool. | Maintains the cross-border mapping database. Requires interfaces for updates and queries. |
| **Issuing Body** | Source of official attestations (e.g., business registers, tax authorities). | Provides data via existing interfaces (APIs, registries). Not a direct user of the VCD system but a critical data source. |
| **Translator** | Provides certified translations of evidence documents. | Interacts with the system to upload certified translations linked to original evidence. |

#### 2.3 Operating Environment
*   **Software:** The system shall operate on standard application servers. It shall support interaction via web browsers and machine-to-machine (M2M) APIs.
*   **Hardware:** Standard server infrastructure capable of 99.5% availability.
*   **Networks:** Must operate over the public internet and integrate securely with the PEPPOL transport infrastructure (AS4).
*   **Standards:** Must comply with PEPPOL, CEN BII, and relevant XML standards (e.g., UBL, XAdES).

#### 2.4 Design and Implementation Constraints
1.  The system **shall** adhere to the data structures and exchange formats defined by the PEPPOL project and CEN BII.
2.  The system **must** comply with EU and national data protection regulations (e.g., GDPR).
3.  National implementations **may** add country-specific extensions, provided core interoperability is maintained.
4.  The system **shall** support electronic signatures as per eIDAS regulation.

#### 2.5 Assumptions and Dependencies
*   The PEPPOL transport infrastructure (WP8) will be available, secure, and reliable.
*   Member States will establish National VCD Service Providers.
*   Issuing bodies will provide (or will develop) machine-readable interfaces for evidence retrieval.
*   The European Service Provider will maintain an accurate and up-to-date pre-VCD mapping database.

### 3. System Features and Requirements

#### 3.1 Feature: VCD Compilation and Management
**3.1.1 Description**
Allows an Economic Operator to initiate, compile, review, and manage a VCD package for a specific tender.

**3.1.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-010** | The system **shall** allow an authenticated Economic Operator to initiate a new **VCD Package** linked to a specific **Tender** (via its reference). |
| **FR-011** | Upon initiation, the system **shall** query the **Pre-VCD Mapping Tool** to retrieve the list of required **Evidence** types mapped from the tender's **Criteria**. |
| **FR-012** | The system **shall** present the Economic Operator with a clear list of required evidences, distinguishing between those that can be retrieved automatically and those that must be uploaded manually. |
| **FR-013** | The system **shall**, where interfaces exist, automatically retrieve **Evidence** documents from registered **Issuing Bodies** upon operator authorization. |
| **FR-014** | The system **shall** allow the Economic Operator to upload digital copies of evidence documents not available for automatic retrieval. |
| **FR-015** | The system **shall** highlight missing or expired evidences and allow the insertion of placeholder self-declarations where permissible (e.g., in two-phase tendering). |
| **FR-016** | The system **shall** allow the Economic Operator to request and attach certified **Translations** to original evidence documents. |
| **FR-017** | The system **shall** generate a structured, machine-readable **VCD Package** containing all evidences, metadata (IDs, dates), and a manifest. |
| **FR-018** | The system **shall** allow the Economic Operator to save a VCD as a draft, preview the final package, and edit it before finalization. |

#### 3.2 Feature: VCD Submission and Transport
**3.2.1 Description**
Enables the secure, non-repudiable submission of a finalized VCD Package from the Economic Operator to the Contracting Authority.

**3.2.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-020** | The system **shall** allow the Economic Operator to digitally sign the finalized **VCD Package**. |
| **FR-021** | The system **shall** transmit the signed **VCD Package** to the target **Contracting Authority** using the PEPPOL transport infrastructure. |
| **FR-022** | The system **shall** provide the Economic Operator with a delivery confirmation receipt from the transport infrastructure. |
| **FR-023** | The system **shall** log all submission events (timestamp, sender, receiver, package ID) in an immutable audit trail. |

#### 3.3 Feature: VCD Reception and Evaluation
**3.3.1 Description**
Allows a Contracting Authority to receive, open, and evaluate the contents of a submitted VCD Package.

**3.3.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-030** | The system **shall** receive **VCD Packages** via the PEPPOL transport infrastructure and validate their integrity and signature. |
| **FR-031** | The system **shall** present the Contracting Authority with a structured overview of the received **VCD Package**, including the submitting **Economic Operator** and linked **Tender**. |
| **FR-032** | The system **shall** allow the Contracting Authority to view the manifest and navigate/access all individual **Evidence** documents within the package. |
| **FR-033** | The system **shall** display metadata for each evidence (type, issuer, issue date, expiry date). |
| **FR-034** | The system **shall** indicate if a certified **Translation** is available for an evidence document and allow it to be viewed. |

#### 3.4 Feature: Consortium VCD Handling
**3.4.1 Description**
Supports the merging of VCDs from multiple Economic Operators into a single package for consortium bids.

**3.4.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-040** | The system **shall** allow an Economic Operator (lead partner) to initiate a consortium VCD. |
| **FR-041** | The system **shall** allow the lead partner to invite other Economic Operators (via their identifiers) to contribute their individual VCDs or evidences. |
| **FR-042** | The system **shall** merge the contributed evidences into a single **VCD Package** with a clear demarcation of the evidence source per consortium member. |
| **FR-043** | The merged package **shall** be submitted as a single entity following the standard submission process (FR-020 to FR-023). |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Web Portal:** A responsive, accessible web interface for Economic Operators, Contracting Authorities, and Officers. It shall be available in at least English and the national language(s) of the service provider.
*   **API Interface:** A RESTful API with JSON/XML payloads for system-to-system integration (e.g., with national eProcurement platforms).

#### 4.2 Hardware Interfaces
None specified. Standard server hardware is assumed.

#### 4.3 Software Interfaces
| Interface | Purpose | Direction | Key Protocol/Standard |
| :--- | :--- | :--- | :--- |
| **Pre-VCD Mapping Tool** | Retrieve mapping of EU criteria to national evidence types. | Outbound | REST/JSON, HTTPS |
| **Issuing Body Interfaces** | Automatically retrieve attestations (e.g., business registration). | Outbound | Varies (OASIS, REST, SOAP). System must be adaptable. |
| **PEPPOL Transport** | Send/Receive VCD packages securely. | Both | AS4, ebMS3, SBDH |
| **National Identity Management** | Authenticate users (Single Sign-On). | Inbound | SAML 2.0, eIDAS node compatible. |
| **Tendering Platforms** | Receive VCD packages from transport layer. | Inbound | PEPPOL AS4, with defined VCD business document type. |

#### 4.4 Communications Interfaces
All external communications **shall** use encrypted channels (TLS 1.2 or higher). Message-level security (encryption/signing) is required for VCD package exchange via the PEPPOL infrastructure.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   The response time for a **Pre-VCD Mapping** query **shall** be ≤ 10 seconds under normal load.
*   The time to **compile a standard VCD Package** (excluding manual uploads) **shall** be ≤ 5 minutes.
*   The system **shall** support concurrent compilation requests from at least 100 Economic Operators.

#### 5.2 Safety Requirements
Not applicable.

#### 5.3 Security Requirements
*   The system **shall** enforce strong user authentication.
*   All sensitive data **must** be encrypted at rest and in transit.
*   The system **shall** implement role-based access control (RBAC) defining permissions for each user class.
*   The system **shall** maintain a secure audit log of all significant actions (login, evidence retrieval, compilation, submission).
*   The system **must** be designed to comply with GDPR and national data protection laws.

#### 5.4 Software Quality Attributes
*   **Availability:** 99.5% uptime during business hours (defined per Member State).
*   **Reliability:** Data integrity **shall** be ensured through validation checks and transactional integrity for compilation processes.
*   **Maintainability:** The system **shall** be modular to allow for independent updates to mapping, evidence retrieval, and transport components.
*   **Observability:** The system **shall** provide monitoring endpoints and logs for performance, errors, and usage statistics.
*   **Compliance:** The system **shall** adhere to the legal requirements of Directive 2004/18/EC and relevant national procurement acts.

### 6. Data Model
The core domain entities and their key attributes are defined below. This is a logical model.

```xml
<!-- Conceptual representation of core entities -->
<VCDPackage id="UUID" creationDate="timestamp" serviceProviderId="required">
  <tenderReference>...</tenderReference>
  <economicOperator ref="CompanyID"/>
  <contains>
    <Evidence id="DocID" type="attestation|statement" issuer="BodyID" issueDate="date" expiryDate="date"/>
    <!-- Evidence may have Translation child -->
  </contains>
</VCDPackage>

<EconomicOperator id="CompanyID" vatNumber="..." legalName="required" country="..."/>
<Criteria id="EU_Criterion_Code" nationalMapping="local_code" description="required"/>
<IssuingBody id="BodyID" type="public|private" country="required" name="..."/>
```

*(Note: A full physical data model or XML schema will be developed in subsequent technical design documents.)*

### 7. Appendices

#### Appendix A: Glossary
*   **Attestation:** An official document issued by a competent body (e.g., business register extract).
*   **Economic Operator:** Any natural or legal person offering goods, works, or services on the market.
*   **Evidence:** A document or data set used to prove fulfillment of a selection/exclusion criterion.
*   **Pre-VCD Mapping:** The process of translating European procurement criteria into specific national evidence requirements.
*   **VCD Package:** The final electronic container (with metadata and manifest) holding all evidences for a specific tender.

#### Appendix B: Analysis Models
*Use Case Diagrams, Activity Diagrams for the main and branched business processes, and State Machine Diagrams for VCD Package status (Draft, In Compilation, Finalized, Submitted, Archived) would be included here in a full SRS.*

#### Appendix C: To Be Determined / Open Issues
The successful implementation of the VCD system depends on resolving the following issues, which are outside the direct scope of this SRS but are critical dependencies:

1.  **Governance & Funding:** A sustainable governance and funding model for the European Service Provider and long-term maintenance must be established.
2.  **Legal Liability:** The legal liability of National Service Providers in case of errors or omissions in the compiled VCD must be clarified per national law.
3.  **Dynamic Legal Changes:** A process for updating the Pre-VCD mapping tool in response to changes in national or EU procurement law must be defined.
4.  **Cost Allocation:** The principles for cost allocation (who pays for the VCD service) must be decided at the national/EU level.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Architect | | | |
| Project Manager | | | |