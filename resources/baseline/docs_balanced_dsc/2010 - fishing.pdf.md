# Software Requirements Specification (SRS)
## Electronic Logbook Software System (ELSS) for UK Fishing Vessels

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review
**Classification:** Public

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for an Electronic Logbook Software System (ELSS) mandated for use on United Kingdom (UK) fishing vessels exceeding 15 meters in length. The purpose is to provide a complete, unambiguous specification for developers, a basis for validation and approval, and a reference for all stakeholders to ensure the system fulfills its regulatory compliance objectives.

#### 1.2 Document Conventions
*   Requirements are uniquely identified (e.g., `FR-001`, `NFR-010`).
*   **Must/Shall:** Indicates a mandatory requirement.
*   **Should:** Indicates a recommended but not mandatory requirement.
*   **May/Could:** Indicates an optional capability.
*   Code and data elements are presented in `monospace` font.
*   Key terms are **bolded** upon first significant use.

#### 1.3 Intended Audience and Reading Suggestions
*   **ELSS Suppliers/Developers:** Primary audience. Should read entire document.
*   **Validation Authority:** Focus on Sections 2 (Overall Description), 3 (Specific Requirements), and 5 (Appendices).
*   **UK Fisheries Administrations (UKFAs):** Focus on Sections 1 (Introduction), 2 (Overall Description), and 3.5 (Non-Functional Requirements).
*   **Vessel Owners & Masters:** Focus on Section 2.2 (User Characteristics) and Section 3 (Specific Requirements) for operational understanding.

#### 1.4 Project Scope
The ELSS is an onboard software application for recording, validating, transmitting, and managing fishing activity data as required by EU Council Regulation (EC) No. 1966/2006 and Commission Regulation (EC) No. 1077/2008.

**In-Scope:**
*   Data entry via user interfaces for fishing trips, activities, catches, gear, and landings.
*   Real-time validation against the official UK XML schema.
*   Generation of compliant XML reports (DEP, FAR, LAN, COR, DEL).
*   Secure, encrypted transmission of reports via email to the UK's ERS.
*   Reception and processing of acknowledgment (RET) messages.
*   Onboard data retention and hard-copy printing.
*   User access control and authentication.

**Out-of-Scope:**
*   Onshore data submission by agents or representatives (this is a function of the ERS portal).
*   Direct integration with other vessel systems (e.g., GPS, scales) is noted as a future consideration but not specified herein.
*   The UK ERS receiving system and its web interfaces.
*   The product approval administration process (though the requirements to *gain* approval are in scope).

#### 1.5 References
| ID  | Document Title | Source |
| :--- | :--- | :--- |
| REF-01 | Council Regulation (EC) No 1966/2006 | Official Journal of the European Union |
| REF-02 | Commission Regulation (EC) No 1077/2008 | Official Journal of the European Union |
| REF-03 | UK Fisheries ERS XML Schema (XSD) & Technical Guidance | UK Fisheries Administrations |
| REF-04 | UK ERS Functional Specifications | UK Fisheries Administrations |

### 2. Overall Description

#### 2.1 Product Perspective
The ELSS is a standalone, vessel-based component within the broader EU/UK Electronic Reporting System (ERS) ecosystem. It interfaces externally with:
*   **UK ERS:** Via encrypted email for report submission and acknowledgment receipt.
*   **Onboard Printer:** For generating hard copies.
*   **Vessel Communication System:** For sending/receiving email.

It is independent but must conform precisely to the data formats and protocols defined by the UK ERS.

#### 2.2 User Characteristics
| User Role | Primary Responsibility | Skill Level / Assumptions |
| :--- | :--- | :--- |
| **Vessel Master** | Data entry, report submission, verification. | Proficient in fishing operations; basic computer literacy; works in a challenging maritime environment. |
| **Crew Member** | May assist with data entry under Master's supervision. | Variable computer literacy. |
| **Vessel Owner** | System procurement, installation, and maintenance. | Understands regulatory obligation; not necessarily a direct software user. |
| **System Administrator (Optional)** | User account management, software updates. | Higher technical proficiency. |

#### 2.3 Operating Environment
*   **Physical:** Must operate reliably on a moving fishing vessel at sea, subject to vibration, moisture, and variable power supply.
*   **Hardware:** Standard commercial off-the-shelf (COTS) PC hardware.
*   **Software:** Common operating systems (e.g., Windows, Linux). Must have network/email client capabilities.
*   **Localization:** English (UK) language. All timestamps in Coordinated Universal Time (UTC).

#### 2.4 Design and Implementation Constraints
1.  **Regulatory Compliance:** The system's design is wholly constrained by the XML schemas and business rules defined in REF-01, REF-02, and REF-03.
2.  **Transmission Protocol:** Initial implementation must support PGP-encrypted email transmission.
3.  **Approval Process:** The final product must pass conformance testing by the designated Validation Authority.
4.  **Data Integrity:** No user-modifiable configuration shall allow the generation of non-compliant XML.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The vessel will have periodic, albeit potentially unreliable, email connectivity.
*   **Assumption:** The Master is ultimately responsible for the accuracy of submitted data.
*   **Dependency:** The UKFA must provide and maintain a stable ERS, test environment, and current XML schemas.
*   **Dependency:** The Validation Authority must be operational to test and approve products.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 Email Interface**
*   `FR-001`: The ELSS shall be able to send emails with XML report files as PGP-encrypted attachments to the designated UK ERS email address.
*   `FR-002`: The ELSS shall be able to receive emails from the UK ERS, specifically Return (RET) messages.
*   `FR-003`: The system shall use PGP encryption as specified by the UKFA. Public/private key management details are TBD (see Undecided Issues).

**3.1.2 Print Interface**
*   `FR-004`: The ELSS shall be capable of generating legible hard-copy prints of logbook data and reports via a standard Windows/system printer driver.

#### 3.2 Functional Requirements
**3.2.1 User Management & Security**
*   `FR-010`: The ELSS shall require user authentication (username and password) to access all functions.
*   `FR-011`: The system shall maintain a record of the user who creates or modifies any logbook entry or report.

**3.2.2 Fishing Trip Management**
*   `FR-020`: The system shall allow the user to create a new Fishing Trip record, generating a unique `GBRLOGNO`.
*   `FR-021`: A trip record shall include, at minimum: Vessel RSS Number, Master Name, Trip Start Date/Time, and Sequence Number.

**3.2.3 Data Capture & Validation**
*   `FR-030`: The ELSS shall provide data entry screens/forms for: Departure (DEP), Fishing Activity (FAR), Species Catch (SPE), Gear Deployment (GEA), and Landing (LAN) data.
*   `FR-031`: The system shall perform real-time validation on all entered data against the rules defined in the UK XML Schema (XSD).
*   `FR-032`: If validation fails, the ELSS shall prevent the user from saving the invalid data and display a clear error message indicating the nature of the failure.
*   `FR-033`: The system shall guide users through conditional (CIF) requirements based on entered data (e.g., fishing zone).

**3.2.4 Report Generation & Management**
*   `FR-040`: The ELSS shall format validated data into the correct UK XML report structure (e.g., `FAR.xml`).
*   `FR-041`: Each report message shall be assigned a unique `GBRRN`.
*   `FR-042`: The system shall store all generated, transmitted, and acknowledged reports locally for the duration of the fishing trip at a minimum.
*   `FR-043`: The user shall be able to view a list of all reports for the current trip, including their type, status (e.g., draft, sent, acknowledged, error), and timestamp.

**3.2.5 Transmission & Acknowledgment**
*   `FR-050`: The ELSS shall transmit reports either manually (user-initiated) or automatically based on configurable triggers (e.g., daily at a set time, upon completing a haul entry).
*   `FR-051`: The system shall track the transmission status of each report (e.g., "Queued", "Sent", "Acknowledged", "Error").
*   `FR-052`: Upon receiving a RET message via email, the ELSS shall automatically match it to the original report using the `GBRRN` and update the report's status.
*   `FR-053`: If a RET message indicates an error (e.g., schema validation failure at ERS), the ELSS shall alert the user and make the relevant report available for correction.
*   `FR-054`: For unacknowledged reports, the ELSS shall periodically alert the user and provide a means to re-transmit.

**3.2.6 Corrections and Deletions**
*   `FR-060`: The user shall be able to generate a Correction (COR) or Deletion (DEL) message for any report from the **current** fishing trip.
*   `FR-061`: A COR/DEL message shall cause the ELSS to generate and transmit a new, full XML report reflecting the corrected data or deletion instruction.

**3.2.7 Printing**
*   `FR-070`: The user shall be able to generate a printed copy of any logbook entry or report for onboard verification and as a regulatory backup.

#### 3.3 Domain Data Model (Key Elements)
The following core data entities must be managed by the ELSS:
```xml
<!-- Conceptual Overview -->
<FishingTrip (LOG)>
    PK: GBRLOGNO
    Attributes: VesselRSS, MasterName, StartDate, SequenceNumber
    Contains: <ReportMessage (ERS)>*

<ReportMessage (ERS)>
    PK: GBRRN
    Attributes: MessageDateTime, OperationType (DAT/DEL/COR), VesselID
    Contains: <FishingActivity (FAR)>* OR <LandingDeclaration (LAN)>* etc.

<FishingActivity (FAR)>
    Attributes: ActivityDateTime, Position
    Contains: <SpeciesCatch (SPE)>*, <GearDeployment (GEA)>*

<SpeciesCatch (SPE)>
    Attributes: SpeciesCode (FAO), LiveWeight, NumberOfFish, RelevantArea

<GearDeployment (GEA)>
    Attributes: GearType, MeshSize, DeploymentDateTime, FishingDepth
```

#### 3.4 User Stories & Acceptance Criteria
| ID | User Story | Key Acceptance Criteria |
| :--- | :--- | :--- |
| US-01 | As a **Vessel Master**, I want to enter fishing activity data so I can comply with daily reporting regulations. | `FR-030`, `FR-031`, `FR-040` are met. Data can be saved and a valid `FAR.xml` is generated. |
| US-02 | As a **Vessel Master**, I want to receive acknowledgements for my transmissions to confirm successful data delivery. | `FR-052` is met. The system clearly shows when a report status changes from "Sent" to "Acknowledged". |
| US-03 | As an **ELSS Supplier**, I want a clear specification to develop compliant software. | This SRS document, coupled with REF-03, provides all necessary details for implementation. |

#### 3.5 Non-Functional Requirements
*   `NFR-001` **(Usability):** The user interface must be clear, intuitive, and designed for use in a marine environment (e.g., large buttons, legible text).
*   `NFR-002` **(Reliability):** The system must retain all data locally. No single point of failure in data capture shall cause the loss of a full day's records.
*   `NFR-003` **(Security):** Data transmissions must be encrypted using PGP (`FR-001`). User access control is required (`FR-010`).
*   `NFR-004` **(Performance):** Data validation (`FR-031`) must occur with negligible delay from the user's perspective.
*   `NFR-005` **(Maintainability):** Software updates must be possible without corrupting existing trip data. Significant updates affecting compliance require re-approval.
*   `NFR-006` **(Legal/Compliance):** The product must be submitted to and approved by the Validation Authority before it can be legally deployed on a UK >15m vessel.

### 4. Supporting Information

#### 4.1 Milestones & Dependencies
| Date | Milestone / Dependency | Impact on ELSS |
| :--- | :--- | :--- |
| 01 Jan 2010 | Mandate for vessels >24m. | Defines initial market for ELSS suppliers. |
| 01 Jul 2011 | Mandate extends to vessels >15m. | Expands market. ELSS must be ready for this user base. |
| Ongoing | UKFA maintains ERS & Schema. | ELSS must adapt to schema updates via a managed process (TBD). |
| Pre-deployment | Validation Authority Approval. | ELSS cannot be legally used without a valid certificate of conformity. |

#### 4.2 Risks and Mitigations
| Risk | Probability | Impact | Mitigation Requirement |
| :--- | :--- | :--- | :--- |
| Poor Communications | High | Medium | `FR-054` (Alert on unacknowledged messages; local storage). |
| Incorrect Data Entry | Medium | High | `FR-031`, `FR-033` (Real-time schema & business rule validation). |
| System Failure at Sea | Low | Critical | `FR-070` (Print capability provides paper backup). |
| Non-Compliant Update | Medium | High | `NFR-005` (Re-approval process for significant changes). |

#### 4.3 Undecided Issues (TBD)
These issues require resolution by the UK Fisheries Administrations and stakeholders:
1.  **Alternative Transmission Protocols:** Final specifications for methods other than email (e.g., web services, satellite direct).
2.  **Onshore Agent Submission:** Clear functional separation between ELSS (onboard) and ERS portal (onshore agent functions).
3.  **Integration API:** Standardized interface specifications for automatic data feed from GPS, catch weighing systems, etc.
4.  **Conditional Requirements:** Final resolution of all CIF rules pending international agreements.
5.  **Schema Version Management:** Formal process for rolling out new XSD versions, including grace periods and ELSS update obligations.
6.  **PGP Key Management:** Detailed procedures for key generation, distribution, revocation, and renewal.

---
*This document is considered a formal part of the UK Electronic Logbook specification framework.*