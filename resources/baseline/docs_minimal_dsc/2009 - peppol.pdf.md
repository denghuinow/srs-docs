# Software Requirements Specification (SRS)
## European Single Procurement Document (ESPD) Service Platform

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the European Single Procurement Document (ESPD) Service Platform. The purpose of this system is to enable Economic Operators (EOs) to electronically assemble, manage, and submit qualification documents required for EU public procurement procedures to any Contracting Authority (CA) across Member States. This document serves as a comprehensive guide for stakeholders, developers, testers, and project managers throughout the system's lifecycle.

#### 1.2 Document Conventions
*   **Requirements IDs:** Follow the format `FR-XXX` for Functional Requirements and `NFR-XXX` for Non-Functional Requirements.
*   **Priority Levels:**
    *   **P0 (Critical):** Must be implemented for the system to be operational.
    *   **P1 (High):** Core functionality, essential for user acceptance.
    *   **P2 (Medium):** Important but can be deferred to a later release.
    *   **P3 (Low):** Nice-to-have enhancements.
*   **Keywords:** `MUST`, `SHALL`, `WILL` indicate mandatory requirements. `SHOULD`, `MAY`, `COULD` indicate desirable but not mandatory features.

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Sponsors & Management:** Focus on Sections 1 (Introduction), 2 (Overall Description), and 5 (Non-Functional Requirements).
*   **Business Analysts & Product Owners:** The entire document, with emphasis on Sections 3 (System Features) and 4 (External Interface Requirements).
*   **Development Team:** Sections 3, 4, 5, and 6 (Other Requirements) for implementation details.
*   **Quality Assurance Team:** All sections, particularly for creating test plans and cases.

#### 1.4 Project Scope
The **ESPD Service Platform** is an EU-wide digital service that facilitates the mutual recognition of qualification documents in public procurement. The system is **in-scope** for:
*   Providing a central repository and mapping engine for national qualification documents against EU selection/exclusion criteria.
*   Enabling the creation, signing, submission, and validation of structured electronic qualification dossiers (Virtual Company Dossier - VCD).
*   Offering automated decision-support tools for Contracting Authorities based on processed document data.
*   Managing user roles, authentication, and audit trails for all transactions.

The system is **out-of-scope** for:
*   Hosting or managing the actual tender notices or submission processes for specific calls for tender (these remain with national eProcurement portals).
*   Legally certifying or guaranteeing the authenticity of documents provided by Issuing Bodies.
*   Replacing national eProcurement systems or eSignature services.

#### 1.5 References
1.  Directive 2004/18/EC of the European Parliament and of the Council on the coordination of procedures for the award of public works contracts, public supply contracts and public service contracts.
2.  Directive 2004/17/EC coordinating the procurement procedures of entities operating in the water, energy, transport, and postal services sectors.
3.  European Standard EN 16310:2013 - eProcurement - Virtual Company Dossier.
4.  EU Regulation 910/2014 on electronic identification and trust services (eIDAS).

### 2. Overall Description

#### 2.1 Product Perspective
The ESPD Service Platform is a standalone, web-based system that will integrate as a middleware component within the broader European eProcurement ecosystem. It will interface with:
*   **National eProcurement Portals:** For tender discovery and final bid submission.
*   **Trust Service Providers:** For advanced electronic signatures/seals (eIDAS compliant).
*   **Issuing Body Registries:** For validating the provenance of qualification documents.
*   **European Commission Services:** For master data (NUTS codes, CPV, etc.) and reporting.

#### 2.2 Product Functions (High-Level Summary)
1.  **Document Mapping & Management:** Map diverse national documents to standardized EU criteria.
2.  **VCD Compilation & Packaging:** Guide users in assembling a complete, structured electronic dossier.
3.  **Submission & Exchange:** Securely transmit the VCD to designated Contracting Authorities.
4.  **Automated Analysis:** Extract and process data from documents to support CA decision-making.
5.  **User & Service Management:** Administer roles, permissions, and VCD Service Provider integrations.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Economic Operator (EO)** | Varies from SMEs to large corporations; diverse technical skill levels; operates in one or multiple Member States. | Minimize administrative burden; reuse documents for multiple tenders; prove compliance efficiently. |
| **Contracting Authority (CA)** | Public sector officials; primary focus on compliance and risk mitigation; may have legal/procurement expertise. | Quickly assess EO eligibility; ensure audit-compliant process; reduce manual document checking. |
| **Issuing Body (IB)** | Banks, courts, social security institutions; produces official documents; requires secure, authenticated access. | Issue verifiable electronic documents; update document status (e.g., revocation). |
| **VCD Service Provider (VSP)** | Commercial software vendors; provide value-added services (e.g., advanced analytics, consultancy). | Integrate with core platform via API; offer specialized tools to EOs and CAs. |
| **System Administrator** | Technical staff of the platform operator. | Manage system health, user support, master data, and monitor integrations. |

#### 2.4 Operating Environment
*   **Software:** Platform-independent web application. Backend: Java/.NET stack. Frontend: Responsive HTML5/JS framework. Database: SQL-based RDBMS (e.g., PostgreSQL).
*   **Hardware:** Deployed on scalable cloud infrastructure (e.g., EU-compliant cloud services) to ensure high availability across Member States.
*   **Networks:** Accessible via the public internet over HTTPS. Must support integration via RESTful APIs and/or web services.

#### 2.5 Design and Implementation Constraints
1.  **Legal & Regulatory Compliance (P0):** The system MUST adhere to Directives 2004/18/EC and 2004/17/EC, their national transpositions, and the eIDAS regulation.
2.  **Semantic Interoperability (P0):** The data model and document processing SHALL be based on EU-standard ontologies and vocabularies (e.g., COS, CPV) to enable cross-border understanding.
3.  **Mutual Recognition (P0):** The system SHALL NOT impose additional requirements that contradict the principle of mutual recognition of documents and procedures across Member States.
4.  **Multilingualism (P1):** The user interface and key metadata SHALL be available in all 24 official EU languages.
5.  **Security (P0):** Must comply with ISO/IEC 27001 standards and EU cybersecurity frameworks.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Member States will provide and maintain accurate registries of authorized Issuing Bodies.
*   **Assumption:** Economic Operators and Contracting Authorities have access to eIDAS-compliant electronic identification means.
*   **Dependency:** The successful adoption and implementation of the VCD standard (EN 16310) across national systems.
*   **Dependency:** Availability of stable and documented APIs from national eProcurement portals for integration.

### 3. System Features

#### 3.1 Feature 1: Document Mapping & Criteria Management
**Description:** Provides a central mapping engine that links national document types to the EU's standardized selection and exclusion criteria.

**Sub-features & Requirements:**
*   **FR-101 (P0): Maintain Criteria Master List.** The system SHALL maintain an authoritative, version-controlled list of all EU selection and exclusion criteria derived from the Directives.
*   **FR-102 (P0): Document-Type Registry.** The system SHALL allow administrators to register and describe national qualification document types (e.g., Italian "DURC," French "Attestation de vigilance").
*   **FR-103 (P0): Mapping Engine.** The system SHALL allow authorized users (e.g., legal experts) to create and manage mappings between a registered document type and one or more EU criteria.
    > **Example Mapping:** Document Type: `Italian DURC` -> Satisfies Criteria: `Compliance with social security contributions` AND `Compliance with tax obligations`.
*   **FR-104 (P1): Mapping Search & Visualization.** Users SHOULD be able to search and view mappings by country, document type, or EU criterion.

#### 3.2 Feature 2: VCD Compilation & Assembly
**Description:** Guides the Economic Operator through a step-by-step process to create a complete Virtual Company Dossier.

**Sub-features & Requirements:**
*   **FR-201 (P0): Dossier Creation Wizard.** The system SHALL provide an interactive wizard that asks the EO to specify the target country and procurement procedure type, then presents a checklist of required criteria.
*   **FR-202 (P0): Document Upload & Association.** The EO SHALL be able to upload electronic documents (PDF, XML, etc.) and associate each document with the specific EU criterion/criteria it fulfills, based on the pre-defined mappings.
*   **FR-203 (P0): Metadata Generation.** The system SHALL automatically generate structured metadata for the VCD, including EO identifier, dossier creation date, list of contained documents, and associated criteria map.
*   **FR-204 (P0): Electronic Sealing/Signing.** The system SHALL integrate with eIDAS trust services to allow the EO to apply an advanced electronic signature or seal to the final VCD package.
*   **FR-205 (P1): Dossier Versioning & Storage.** The system SHOULD store draft and submitted dossiers in a personal workspace for the EO, allowing for reuse and updates.

#### 3.3 Feature 3: Submission, Validation & Decision Support
**Description:** Manages the secure submission of the VCD to a CA and provides tools for the CA to validate and analyze its contents.

**Sub-features & Requirements:**
*   **FR-301 (P0): Secure Submission Channel.** The system SHALL provide a mechanism for the EO to securely address and transmit a signed VCD to a specific Contracting Authority (e.g., via a unique submission code or integration with a national portal).
*   **FR-302 (P0): VCD Validation.** Upon receipt, the system SHALL automatically validate the VCD's structure, signature integrity, and completeness against the requested criteria.
*   **FR-303 (P0): Contextual Data Extraction.** The system SHALL process documents within the VCD (where machine-readable, e.g., XML) to extract key data points (e.g., date of issue, expiry, company identification number).
*   **FR-304 (P1): Automated Compliance Dashboard.** For the CA, the system SHOULD present a dashboard summarizing the EO's compliance status per criterion, highlighting expired documents, missing information, or potential discrepancies.
*   **FR-305 (P1): Audit Trail.** The system SHALL log all key actions (creation, modification, submission, access) on a VCD with timestamp and user identity for full auditability.

#### 3.4 Feature 4: User & Service Management
**Description:** Handles authentication, authorization, and administration for all user classes and integrated service providers.

**Sub-features & Requirements:**
*   **FR-401 (P0): eIDAS Authentication.** The system SHALL support login for all user classes using eIDAS-compliant electronic identification schemes.
*   **FR-402 (P0): Role-Based Access Control (RBAC).** Access to features and data SHALL be strictly controlled based on user roles (EO, CA, IB, VSP, Admin).
*   **FR-403 (P0): Issuing Body Portal.** IBs SHALL have a dedicated interface to register issued documents, update their status (valid/revoked), and respond to verification requests from CAs.
*   **FR-404 (P1): VSP API Management.** The system SHOULD provide a secure API (using OAuth 2.0) for registered VCD Service Providers to access platform services (e.g., retrieve mappings, validate VCD structures) on behalf of their clients.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Primary UI:** A responsive, accessible web application compatible with major browsers (Chrome, Firefox, Edge, Safari) from the last two stable versions.
*   **Language:** Interface shall be dynamically switchable between all official EU languages.
*   **Accessibility:** Shall strive to meet WCAG 2.1 AA standards.

#### 4.2 Hardware Interfaces
None specified. The system is cloud-based and accessed via standard web protocols.

#### 4.3 Software Interfaces
1.  **SI-01: eIDAS Node Interface:** For cross-border user authentication.
2.  **SI-02: National eProcurement Portal Interface:** For receiving tender context and final submission routing (format: REST API / OASIS UBL).
3.  **SI-03: Trust Service Provider API:** For connecting to qualified timestamp and signature/seal validation services.
4.  **SI-04: Issuing Body Registry Interface:** For real-time validation of document issuers.

#### 4.4 Communications Interfaces
*   **Protocols:** HTTPS/TLS 1.2+ for all external communications.
*   **Data Formats:** JSON for REST APIs, XML for formal document exchange (VCD schema based on EN 16310).

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NFR-001 (Response Time):** 95% of all user-facing web transactions shall complete in under 3 seconds under normal load.
*   **NFR-002 (Throughput):** The system shall support the concurrent assembly and submission of VCDs by at least 10,000 EOs during peak procurement periods.
*   **NFR-003 (VCD Processing):** Automated validation and initial data extraction of a standard VCD shall complete within 30 seconds.

#### 5.2 Safety Requirements
Not applicable.

#### 5.3 Security Requirements
*   **NFR-010 (Data Confidentiality):** All Personally Identifiable Information (PII) and commercial-in-confidence data shall be encrypted at rest and in transit.
*   **NFR-011 (Integrity):** The system shall ensure the integrity of all stored VCDs and audit logs using cryptographic measures.
*   **NFR-012 (Availability):** System availability shall be 99.5% during core business hours (07:00-19:00 CET).
*   **NFR-013 (Non-Repudiation):** The use of eIDAS advanced electronic signatures/seals shall provide non-repudiation for VCD submissions.

#### 5.4 Software Quality Attributes
*   **Maintainability:** The codebase shall have a comprehensive unit test coverage (>80%) and be documented to allow for efficient onboarding of new developers.
*   **Interoperability:** The system shall be designed based on open standards to facilitate integration with heterogeneous national systems.
*   **Scalability:** The architecture shall allow for horizontal scaling of components to handle increasing loads without redesign.
*   **Usability:** The process for compiling a VCD shall be achievable by a novice user with basic digital skills within 30 minutes, guided by the system.

### 6. Other Requirements

#### 6.1 Legal & Compliance
The system operator shall be responsible for maintaining compliance with evolving EU regulations, including the eventual transition to directives 2014/24/EU and 2014/25/EU. A data processing agreement in line with GDPR shall govern all personal data handled by the platform.

#### 6.2 Documentation
The following documentation shall be produced:
*   User manuals for EO, CA, and IB user classes.
*   Technical API documentation for VCD Service Providers and system integrators.
*   System administration and operations guide.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Architect | | | |
| Quality Assurance Manager | | | |