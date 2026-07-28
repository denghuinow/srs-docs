**Purpose & Scope**
The system is a Virtual Company Dossier (VCD) solution to enable cross-border electronic public procurement. It allows economic operators (suppliers) to electronically collect and submit the required qualification documents (evidences) to prove selection and exclusion criteria to any European contracting authority. The system does not handle the tender/bid submission itself, only the supporting evidentiary documents. It focuses on criteria derived from EU Directive 2004/18/EC, Articles 45-50.

**Product Background / Positioning**
The VCD is a component of the broader Pan-European Public Procurement OnLine (PEPPOL) infrastructure, aiming to overcome market fragmentation. It sits between national company registries/issuing bodies (sources of evidence) and contracting authorities' eTendering systems. It must interoperate with existing national procedures and the PEPPOL transport infrastructure (WP8).

**Core Functional Overview**
1.  **Pre-VCD Mapping:** Provides a mapping service between European selection/exclusion criteria and the national attestations/evidences available in each Member State.
2.  **VCD Package Compilation:** Assists economic operators in collecting required evidences (documents) from various issuing services (automated, semi-automated, manual) into a structured package.
3.  **VCD Package Submission:** Enables the secure electronic submission of the compiled VCD package to a foreign contracting authority.
4.  **VCD Package Viewing:** Allows contracting authorities to view and check the contents of a received VCD package.
5.  **VCD Re-compilation:** Supports updating an existing VCD package with new or renewed evidences.
6.  **Consortium VCD Merging:** Enables the creation of a single VCD package for a bidding consortium by merging data from multiple economic operators.
7.  **Context-Specific Data Handling:** (Advanced stage) Extracts and includes machine-interpretable key data from evidences to support automated decision-making.
8.  **On-Demand Evidence Retrieval:** (Network stage) Allows contracting authorities to retrieve original evidences from a trusted repository upon request, based on references in the VCD.

**Key Users & Usage Scenarios**
*   **Economic Operators:** Companies bidding on public contracts. They use the VCD service to compile and submit their qualification documents. They may act as manual "issuing bodies" for self-declarations.
*   **Contracting Authorities:** Public bodies procuring goods/services. They specify required criteria, receive VCD packages, and check them for compliance.
*   **Issuing Bodies:** Public or private entities (e.g., commercial registers, tax offices) that provide official attestations. They may provide automated data feeds to the VCD system.
*   **National VCD Service Providers:** Trusted entities that host the VCD compilation and related services within a Member State.
*   **European Service Provider:** Entity hosting the central pre-VCD mapping tool/service.

**Major External Interfaces**
*   Interface to **national issuing bodies** (registries, authorities) for automated evidence retrieval.
*   Interface to the **PEPPOL transport infrastructure** for secure cross-border delivery of VCD packages.
*   Interface to **eTendering platforms/procurement systems** for receiving VCD packages.
*   Interface to the **pre-VCD mapping service** (European level) for criteria-evidence mapping data.

**Key Non-functional Requirements**
*   **Security & Confidentiality:** VCD package transport and storage must prevent unauthorized access, interception, or modification. Non-repudiation of origin is required.
*   **Reliability & Availability:** The VCD service and transport infrastructure must ensure documents are delivered. Service-level agreements for "on-demand" retrieval are needed.
*   **Data Integrity:** It must be assured that VCD contents are not altered during transport or validation.
*   **Legal Validity:** The system must support electronic signatures with legal equivalence to handwritten signatures where required by law.
*   **Trust:** National VCD Service Providers must operate as trusted third parties. The pre-VCD mapping must be legally legitimate and mutually recognized.
*   **Maintainability:** The pre-VCD mapping must be easily updatable to reflect legal changes in Member States.

**Constraints, Assumptions & Dependencies**
*   **Legal Dependency:** The solution depends on the principle of mutual recognition of evidences/certificates as per EU Directive 2004/18/EC.
*   **Infrastructure Dependency:** Relies on the PEPPOL transport infrastructure (WP8) and validation services (WP1) for secure cross-border operation.
*   **Organisational Constraint:** Must utilize existing national procedures and evidence-issuing infrastructures where possible; cannot mandate their change.
*   **Technical Constraint:** Cannot assume all issuing bodies provide machine-interpretable data; system must handle manual and semi-automated evidence collection.
*   **Assumption:** Contracting authorities will formally specify the required selection/exclusion criteria in a machine-processable format within the Call for Tender.

**Priorities & Acceptance Approach**
*   **Priority 1 (Mandatory):** Implementation of the pre-VCD mapping tool (Stage 1) by all participating Member States as the foundation for interoperability.
*   **Priority 2 (Pilot Core):** Implementation of VCD simple package compilation and submission (Stage 2) by piloting Member States (e.g., Austria, Italy).
*   **Priority 3 (Advanced):** Implementation of re-compilation, merging, and context-data features (Stages 3 & 4) as optional enhancements based on national readiness.
*   **Acceptance:** Solutions will be tested by reprocessing historical tenders. A VCD package is accepted if it demonstrably contains valid evidences that map to the criteria specified in the Call for Tender.