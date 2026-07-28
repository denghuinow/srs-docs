# Software Requirements Specification (SRS)
## PEPPOL Virtual Company Dossier (VCD) System

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the PEPPOL Virtual Company Dossier (VCD) system. The intended audience includes project stakeholders, system architects, developers, testers, and implementation teams. This document serves as the foundation for design, development, and validation.

#### 1.2 Project Scope
The VCD system is a pan-European initiative designed to standardize and digitize the submission of company information (certificates, attestations) as evidence for selection and exclusion criteria in public procurement, in accordance with Directive 2004/18/EC. Its primary objective is to reduce administrative burdens and facilitate cross-border tendering through interoperability and mutual recognition of documents.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **VCD**: Virtual Company Dossier.
*   **PEPPOL**: Pan-European Public Procurement Online.
*   **EO**: Economic Operator (e.g., company bidding for a tender).
*   **CA**: Contracting Authority (e.g., government body issuing a tender).
*   **IB**: Issuing Body (e.g., chamber of commerce, court registry).
*   **NVSP**: National VCD Service Provider.
*   **ESP**: European Service Provider.
*   **WP8**: PEPPOL Work Package 8 (eDelivery Network for secure document exchange).

#### 1.4 References
*   Directive 2004/18/EC of the European Parliament and of the Council.
*   PEPPOL eDelivery Network (WP8) Specifications.
*   Relevant national e-Government interoperability frameworks.

#### 1.5 Document Overview
This SRS is structured to present an overall description of the product, followed by specific external interface, functional, and non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
The VCD system is a component within the broader PEPPOL ecosystem. It relies on the existing PEPPOL eDelivery network (WP8) for secure, cross-border transport of packages. It interfaces with national e-Government systems, issuing body registries, and service providers.

#### 2.2 Product Functions (Summary)
1.  **Pre-VCD Mapping:** Provide a tool to map national attestations to standardized EU procurement criteria.
2.  **VCD Compilation:** Enable the creation of Simple, Advanced, and Network VCD packages containing digital evidence and metadata.
3.  **VCD Submission & Validation:** Facilitate the secure submission of VCD packages to CAs and support their validation.
4.  **Evidence Retrieval:** Allow on-demand, authorized retrieval of attestations from issuing bodies (Network Package).
5.  **Package Management:** Support the re-compilation and updating of VCDs for reuse in new tenders.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Economic Operator (EO)** | Varies in technical sophistication. Seeks efficiency. | Prove eligibility with minimal effort, especially for cross-border tenders. |
| **Contracting Authority (CA)** | Public official. Requires legal compliance and auditability. | Efficiently and reliably verify EO suitability for a tender. |
| **Issuing Body (IB)** | Source of official data (e.g., tax authority). Has existing systems. | Provide electronic attestations securely and reliably. |
| **National VCD Service Provider (NVSP)** | Technical/legal entity. Provides trusted national services. | Offer VCD compilation/hosting services and ensure system trust. |
| **European Service Provider (ESP)** | Central governance/technical body. | Maintain and govern the pre-VCD mapping tool and core semantics. |
| **Translator** | Certified language professional. | Provide legally accepted translations of evidentiary documents. |

#### 2.4 Operating Environment
*   **Technical:** Must operate across heterogeneous IT environments in EU Member States. Web-based interfaces. Integrates with PEPPOL Access Points.
*   **Legal:** Must comply with EU and national data protection regulations (e.g., GDPR), eIDAS regulations for trust services, and national procurement laws.
*   **Organizational:** Operates within a multi-stakeholder governance model involving EU, national, and private entities.

#### 2.5 Design and Implementation Constraints
1.  **Legal/Regulatory:** Must accommodate diverse national legal frameworks and attestation formats.
2.  **Technical:** Dependent on the existing PEPPOL WP8 infrastructure for secure transport. Cannot mandate changes to national IT infrastructure.
3.  **Data:** Must handle limited availability of native electronic attestations in some Member States (scans/PDFs must be supported).
4.  **Linguistic:** Must provide mechanisms (context data, translation interfaces) to address language barriers.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Mutual recognition agreements for attestations will be established between Member States.
*   **Assumption:** A sufficient number of Issuing Bodies will be capable of providing electronic attestations.
*   **Dependency:** The continued operation and support of the PEPPOL eDelivery network.
*   **Dependency:** Secure and standardized electronic identities (eID) for user authentication where required.

### 3. System Features and Requirements

#### 3.1 Pre-VCD Mapping Tool (Managed by ESP)
**3.1.1 Description**
A central reference tool that allows EOs and NVSPs to understand how national documents map to EU-standard selection/exclusion criteria.

**3.1.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-MAP-01** | The system shall provide a publicly accessible repository of EU procurement criteria (selection & exclusion). | High |
| **FR-MAP-02** | The system shall allow authorized national representatives to submit and maintain mappings between national attestation types and EU criteria. | High |
| **FR-MAP-03** | The system shall allow users (EOs, CAs) to search and browse these mappings by country and criteria. | High |
| **FR-MAP-04** | The system shall display the mapping information, including the national document name, issuing body, and its validity for proving specific EU criteria. | Medium |

#### 3.2 VCD Package Compilation & Management
**3.2.1 Description**
Core functionality for creating, updating, and managing the three types of VCD packages (Simple, Advanced, Network).

**3.2.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-COMP-01** | The system shall allow an EO or NVSP to create a new VCD Simple Package by uploading digital evidence files (PDF, XML, etc.) and associating them with specific EU criteria. | High |
| **FR-COMP-02** | The system shall automatically generate and embed structural metadata (VCD ID, creator, creation date, criteria list, evidence hash) into the VCD package. | High |
| **FR-COMP-03** | For a VCD Advanced Package, the system shall allow the addition of context-specific data (e.g., explanatory notes, references) to evidences. | High |
| **FR-COMP-04** | The system shall support the re-compilation of an existing VCD for a new tender, allowing the EO to select still-valid evidences and add new ones. | High |
| **FR-COMP-05** | The system shall allow an EO/NVSP to request a certified translation for an evidence item and link the translated document to the original in the package. | Medium |
| **FR-COMP-06** | The system shall support the creation of a VCD Network Package, where an evidence item is a secure pointer (URI) to an attestation held by an Issuing Body, retrievable on-demand by the CA. | High |

#### 3.3 VCD Submission & Validation
**3.3.1 Description**
Process for securely sending a VCD to a CA and enabling the CA to validate its contents and integrity.

**3.3.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-SUB-01** | The system shall enable the sender (EO/NVSP) to transmit a VCD package to a designated CA recipient via the PEPPOL eDelivery network (WP8). | High |
| **FR-SUB-02** | The system shall provide the CA with a user interface to receive, list, and view incoming VCD packages. | High |
| **FR-SUB-03** | The system shall allow the CA to validate the structural integrity and metadata of the VCD package (e.g., verify hash, check completeness). | High |
| **FR-SUB-04** | The system shall present the CA with a clear view of the VCD contents: mapped EU criteria and the associated evidence documents/pointers. | High |
| **FR-SUB-05** | For a VCD Network Package, the system shall allow the CA to securely retrieve the actual attestation from the Issuing Body's endpoint using the provided pointer. | High |

#### 3.4 Trust & Security Services
**3.4.1 Description**
Underpinning requirements to ensure the legal validity, non-repudiation, and trustworthiness of the VCD ecosystem.

**3.4.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-SEC-01** | The system shall support the application of qualified electronic signatures/seals to VCD packages and/or individual attestations as per eIDAS. | High |
| **FR-SEC-02** | All data exchanges between system components (EO->NVSP, NVSP->CA, CA->IB) shall occur over secure, authenticated channels (PEPPOL eDelivery). | High |
| **FR-SEC-03** | The system shall maintain an immutable audit log for each VCD package, recording creation, modification, submission, and access events. | High |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Web Portal for EOs/NVSPs:** Intuitive interface for mapping, compilation, and management of VCDs.
*   **Web Portal for CAs:** Clean interface for receiving, validating, and evaluating VCD packages.
*   **Administrative Interface for ESP/IBS:** For managing mapping data and attestation endpoints.

#### 4.2 Hardware Interfaces
None specified. The system is software-based and operates on standard server infrastructure.

#### 4.3 Software Interfaces
*   **PEPPOL eDelivery Network (WP8):** Mandatory interface for all cross-border and inter-party document exchange. Must comply with PEPPOL AS4 profile.
*   **National e-Government/IB Systems:** Interfaces (APIs, web services) will be required for the Network Package to retrieve attestations. These will be nationally specific.

#### 4.4 Communications Interfaces
*   **Protocols:** AS4, RESTful APIs, SOAP web services.
*   **Security:** TLS 1.2+ for all web communications. S/MIME or PKI-based signing for documents.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   The compilation of a standard VCD Simple Package shall be completed within 2 minutes for up to 20 evidence documents.
*   The system shall support concurrent access and package compilation for at least 1000 users per Member State during peak tender periods.

#### 5.2 Safety Requirements
Not applicable.

#### 5.3 Security Requirements
*   All personal and company data shall be protected in accordance with GDPR.
*   The system shall implement role-based access control (RBAC) for all functions.
*   VCD packages at rest shall be encrypted.

#### 5.4 Software Quality Attributes
*   **Availability:** 99.5% uptime for central components (ESP tool). National systems define their own SLAs.
*   **Interoperability:** The system shall be based on open standards (XML, UBL, etc.) to ensure semantic and technical interoperability.
*   **Maintainability:** The system shall be modular to allow independent updates to mapping, compilation, and validation components.
*   **Usability:** Key user tasks (upload evidence, map to criteria) shall be achievable with minimal training.

### 6. Other Requirements

#### 6.1 Success Metrics
The success of the VCD system will be measured by:
1.  **Adoption:** XX% increase in cross-border tender submissions by EOs within 3 years of rollout.
2.  **Efficiency:** Reduction of average time spent by CAs on eligibility verification by YY%.
3.  **Trust:** ZZ% of surveyed CAs report high confidence in the validity of VCD-submitted evidence.

#### 6.2 Undecided and Open Issues
1.  The governance and funding model for the European pre-VCD mapping tool (ESP) is TBD.
2.  Liability clauses for National VCD Service Providers in case of compilation errors need legal definition.
3.  The technical specification for standardizing "context-specific data" in Advanced Packages requires further analysis.
4.  The long-term funding and sustainability model for VCD services post-pilot phase is not yet established.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| SRS Author | | | |