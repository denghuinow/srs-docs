# Software Requirements Specification (SRS)
## Virtual Company Dossier (VCD) System
### Version 1.0

**Document Status:** Draft  
**Prepared For:** PEPPOL Project Stakeholders  
**Date:** [Current Date]

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Virtual Company Dossier (VCD) system. The VCD is a core component of the Pan-European Public Procurement OnLine (PEPPOL) infrastructure, designed to facilitate cross-border electronic public procurement within the European Union. This document serves as a comprehensive guide for developers, testers, project managers, and other stakeholders involved in the system's implementation and validation.

### 1.2 Scope
The VCD system enables Economic Operators (suppliers) to electronically compile, manage, and submit structured packages of qualification documents ("evidences") to prove compliance with selection and exclusion criteria as defined in EU Directive 2004/18/EC, Articles 45-50. The system's scope is limited to the handling of these supporting evidentiary documents; it does **not** include the submission of the tender or bid itself. The system operates within a federated model, involving National VCD Service Providers, a central European mapping service, and interfaces with existing national registries and the PEPPOL transport infrastructure.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **VCD** | Virtual Company Dossier. The structured electronic package containing qualification evidences. |
| **Economic Operator (EO)** | A company or entity bidding on a public contract (supplier). |
| **Contracting Authority (CA)** | A public body procuring goods, works, or services. |
| **Issuing Body** | A national authority or registry (e.g., commercial register, tax office) that issues official attestations. |
| **PEPPOL** | Pan-European Public Procurement OnLine. The overarching interoperability infrastructure. |
| **Evidence** | A document or attestation proving compliance with a specific selection or exclusion criterion. |
| **WP8** | PEPPOL Work Package 8, responsible for the transport infrastructure. |

### 1.4 References
*   EU Directive 2004/18/EC of the European Parliament and of the Council.
*   PEPPOL Project Documentation, including WP1 (Validation) and WP8 (Transport Infrastructure) specifications.
*   National legislation of participating Member States regarding public procurement and electronic signatures.

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines the non-functional requirements. Appendices may include data models, interface specifications, or priority matrices.

## 2. Overall Description

### 2.1 Product Perspective
The VCD system is a middleware component within the larger PEPPOL ecosystem. It acts as an intermediary between:
*   **Data Sources:** National issuing bodies and registries.
*   **Service Providers:** National VCD Service Providers and a European mapping service.
*   **End Users:** Economic Operators and Contracting Authorities.
*   **External Systems:** National eTendering/procurement platforms.

The system relies on the PEPPOL transport infrastructure (WP8) for secure, cross-border document exchange and must interoperate with diverse national IT systems without mandating changes to them.

### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Economic Operator (EO)** | Varies in technical sophistication. Represents a company bidding across borders. | Compile a compliant VCD package with minimal effort. Submit it securely to any EU CA. Update and re-use dossiers. |
| **Contracting Authority (CA)** | Public administration employee. Subject to national procurement laws. | Specify required criteria. Receive and easily verify the validity and completeness of VCD packages. |
| **Issuing Body** | National authority or certified private entity. May have varying levels of IT maturity. | Provide attestations/data feeds. May not interact directly with VCD UI. |
| **National VCD Service Provider** | Trusted third-party entity within a Member State. Technically proficient. | Host and maintain national VCD compilation services. Ensure legal and technical compliance. |
| **European Service Provider** | Central entity (e.g., managed by EU Commission). | Maintain the central Pre-VCD mapping service. Ensure its accuracy and legal legitimacy. |

### 2.3 Operating Environment
*   **Technical Environment:** Distributed, service-oriented architecture. Must support integration via web services (SOAP/REST). Operates over the internet with PEPPOL network protocols.
*   **Organizational Environment:** Must comply with the legal frameworks of all participating EU Member States. Operates under the principle of mutual recognition.
*   **Security Environment:** Requires high-trust environment with support for advanced electronic signatures (QES), encryption, and secure access controls.

### 2.4 Design and Implementation Constraints
1.  **Legal:** Must adhere to EU Directive 2004/18/EC and national e-signature laws.
2.  **Technical:** Must interface with the existing PEPPOL WP8 transport infrastructure. Cannot assume machine-readable data from all issuing bodies.
3.  **Organizational:** Must utilize existing national evidence-issuing procedures; cannot mandate their change.
4.  **Architectural:** Federated model requires clear separation of concerns between central (mapping) and national (compilation) services.

### 2.5 Assumptions and Dependencies
*   **Assumption:** Contracting Authorities will specify required criteria in a machine-processable format within their Calls for Tender.
*   **Dependency:** The system's viability depends on the legal principle of mutual recognition of evidences across Member States.
*   **Dependency:** Successful operation is dependent on the availability and reliability of the PEPPOL transport infrastructure (WP8) and validation services (WP1).

## 3. System Features and Requirements

### 3.1 Feature 1: Pre-VCD Mapping Service
**Description:** A central service that maintains the authoritative mapping between standardized European selection/exclusion criteria and the corresponding national attestations or evidences available in each Member State.
**Priority:** 1 (Mandatory)

| ID | Requirement Description |
| :--- | :--- |
| **FR1.1** | The system shall provide a user interface (for authorized administrators) to create, read, update, and delete mappings between EU criteria codes and national evidence identifiers. |
| **FR1.2** | The system shall expose an API for National VCD Service Providers to query the mapping for a specific EU criterion and Member State. |
| **FR1.3** | The system shall maintain version history for each mapping, including effective dates and references to the legal basis. |
| **FR1.4** | The system shall allow the European Service Provider to publish and deprecate mapping sets for specific Member States. |

### 3.2 Feature 2: VCD Package Compilation
**Description:** A service (typically national) that guides an Economic Operator through the process of collecting all required evidences for a specific Call for Tender.
**Priority:** 2 (Pilot Core)

| ID | Requirement Description |
| :--- | :--- |
| **FR2.1** | The system shall allow an EO to input or select the EU criteria (by code) specified in a Call for Tender. |
| **FR2.2** | Based on the EO's country of registration and selected criteria, the system shall retrieve the relevant evidence mapping from the Pre-VCD Mapping Service and present a list of required national evidences. |
| **FR2.3** | The system shall support multiple evidence collection methods: <br> a) **Automated:** Fetch evidence directly from a national issuing body's API. <br> b) **Semi-Automated:** Provide a pre-filled form or generate a request to an issuing body. <br> c) **Manual:** Allow the EO to upload a scanned document (e.g., a self-declaration). |
| **FR2.4** | The system shall structure collected evidences into a defined VCD package schema (e.g., UBL-based). |
| **FR2.5** | The system shall allow the EO to preview the compiled VCD package before finalization. |

### 3.3 Feature 3: VCD Package Submission & Transport
**Description:** The secure electronic submission of a finalized VCD package from the EO (via the National Service Provider) to the foreign Contracting Authority.
**Priority:** 2 (Pilot Core)

| ID | Requirement Description |
| :--- | :--- |
| **FR3.1** | The system shall enable the EO to address the VCD package to a specific Contracting Authority (identified by a PEPPOL ID or similar). |
| **FR3.2** | The system shall sign the final VCD package with an electronic signature on behalf of the EO/National Service Provider to ensure non-repudiation of origin. |
| **FR3.3** | The system shall transmit the signed VCD package using the PEPPOL WP8 transport infrastructure. |
| **FR3.4** | The system shall provide delivery status notification (sent/received/delivered) to the EO. |

### 3.4 Feature 4: VCD Package Viewing & Verification
**Description:** Functionality for a Contracting Authority to access, open, and inspect the contents of a received VCD package.
**Priority:** 2 (Pilot Core)

| ID | Requirement Description |
| :--- | :--- |
| **FR4.1** | The system shall provide a user interface for the CA to list and select received VCD packages. |
| **FR4.2** | The system shall validate the electronic signature on a received VCD package and display the verification status. |
| **FR4.3** | The system shall render the contents of the VCD package in a human-readable view, showing the mapping between submitted evidences and the requested EU criteria. |
| **FR4.4** | The system shall allow the CA to download individual evidence documents from the package. |

### 3.5 Feature 5: VCD Re-compilation
**Description:** Allows an Economic Operator to update an existing VCD package, typically to renew expired evidences or add evidences for new criteria.
**Priority:** 3 (Advanced)

| ID | Requirement Description |
| :--- | :--- |
| **FR5.1** | The system shall allow an EO to import/load an existing VCD package (from their history). |
| **FR5.2** | The system shall identify evidences within the package that are expired or nearing expiry. |
| **FR5.3** | The system shall guide the EO through the process of collecting only the new or updated evidences. |
| **FR5.4** | The system shall create a new version of the VCD package, preserving a link to the previous version for audit purposes. |

### 3.6 Feature 6: Consortium VCD Merging
**Description:** Enables the creation of a single, unified VCD package for a bidding consortium by merging packages from multiple member Economic Operators.
**Priority:** 3 (Advanced)

| ID | Requirement Description |
| :--- | :--- |
| **FR6.1** | The system shall allow a designated lead EO to select multiple existing VCD packages (from different EOs) for merging. |
| **FR6.2** | The system shall consolidate evidences, resolving duplicates and presenting a unified view of criteria compliance for the consortium. |
| **FR6.3** | The system shall generate a new VCD package for the consortium, clearly identifying the contributing members. |

### 3.7 Feature 7: Context-Specific Data Handling
**Description:** (Advanced) Extracts key machine-interpretable data points from evidence documents to enable automated pre-validation by CA systems.
**Priority:** 3 (Advanced)

| ID | Requirement Description |
| :--- | :--- |
| **FR7.1** | For evidences obtained via automated feeds, the system shall extract and tag key data (e.g., company registration number, date of issue, expiry date) according to a defined syntax. |
| **FR7.2** | The system shall embed this structured data within the VCD package metadata alongside the original evidence. |

### 3.8 Feature 8: On-Demand Evidence Retrieval
**Description:** (Network Stage) Allows a Contracting Authority to retrieve the original, authoritative evidence from a trusted national repository using a secure reference contained in the VCD.
**Priority:** Future Enhancement

| ID | Requirement Description |
| :--- | :--- |
| **FR8.1** | The system shall allow a VCD package to contain secure, time-limited references (URLs/digital tokens) to original evidences stored at the National Service Provider or Issuing Body. |
| **FR8.2** | The system shall provide a secure channel for the CA to resolve these references and retrieve the original evidence upon request, with proper authentication and audit logging. |

## 4. Non-Functional Requirements

### 4.1 Security Requirements
| ID | Requirement Description |
| :--- | :--- |
| **NFR-S1** | **Confidentiality & Integrity:** All VCD packages in transit (via PEPPOL) and at rest (in national repositories) must be encrypted using industry-standard algorithms (e.g., AES-256, TLS 1.2+). |
| **NFR-S2** | **Authentication & Authorization:** Access to compilation and viewing services must require strong user authentication. Role-based access control (RBAC) must be implemented for all user classes. |
| **NFR-S3** | **Non-Repudiation:** The system must support advanced electronic signatures (QES as per eIDAS) applied to VCD packages to guarantee origin and integrity. |
| **NFR-S4** | **Audit Logging:** All critical actions (package compilation, submission, signature verification, access to on-demand evidence) must be logged in an immutable audit trail, including timestamp, user identity, and action performed. |

### 4.2 Reliability & Availability
| ID | Requirement Description |
| :--- | :--- |
| **NFR-RA1** | The Pre-VCD Mapping Service shall have an availability of 99.5% during European business hours (CET). |
| **NFR-RA2** | National VCD compilation services shall have availability defined in national SLAs, targeting 99% uptime during local business hours. |
| **NFR-RA3** | The PEPPOL transport infrastructure delivery success rate for VCD packages shall exceed 99.9%. |

### 4.3 Performance
| ID | Requirement Description |
| :--- | :--- |
| **NFR-P1** | The response time for loading the compilation interface and retrieving initial mapping data shall be under 3 seconds for 95% of requests. |
| **NFR-P2** | The process of fetching an evidence from an automated national issuing body shall complete within 30 seconds. |

### 4.4 Maintainability & Supportability
| ID | Requirement Description |
| :--- | :--- |
| **NFR-M1** | The Pre-VCD Mapping Service database and UI shall be designed to allow authorized legal experts (non-developers) to update mapping rules with minimal technical support. |
| **NFR-M2** | All system interfaces (APIs) shall be fully documented according to OpenAPI/Swagger standards. |

### 4.5 Legal & Compliance
| ID | Requirement Description |
| :--- | :--- |
| **NFR-L1** | The system design and operation shall comply with EU Directive 2004/18/EC and the principle of mutual recognition. |
| **NFR-L2** | The system shall not store original evidence documents longer than required by national archival laws, relying on references (FR8) where possible. |

## 5. Acceptance Approach
*   **Primary Method:** Historical tender reprocessing. Successful acceptance will be demonstrated by taking real, completed Calls for Tender from pilot Member States, using the VCD system to compile the required qualification dossiers for the winning bidders, and verifying that the resulting VCD package contains all valid, mapped evidences that would have led to a compliant bid.
*   **Criteria:** A VCD package is deemed **accepted** if it demonstrably contains a valid set of evidences that correctly map to the selection and exclusion criteria specified in the Call for Tender, and if the package can be successfully transmitted, received, and verified by the designated Contracting Authority system.

---
*Document End*