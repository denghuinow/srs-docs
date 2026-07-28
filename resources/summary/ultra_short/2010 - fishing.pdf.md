**Purpose & Scope**
The system is an Electronic Logbook Software System (ELSS) for UK fishing vessels, mandated to replace paper logbooks for vessels over 15 meters. It captures, validates, and transmits fishing activity data to the UK Fisheries Administrations' Electronic Recording and Reporting System (ERS) to comply with EU regulations. It does not provide for onshore data entry by agents or representatives; that must be done via separate ERS web or offline methods.

**Product Background / Positioning**
The system is a mandatory onboard software component for UK-registered fishing vessels, driven by EU Council Regulation (EC) No. 1966/2006. It interfaces directly with the UK's central ERS for regulatory reporting. It exists within an ecosystem that may include other onboard systems (e.g., GPS, weighing systems) for data population.

**Core Functional Overview**
1.  Capture and validate logbook, transhipment, and landing declaration data via onboard screens.
2.  Generate and transmit 12 specific report types (e.g., Departure, Fishing Activity, Landing) as XML.
3.  Support data operations for new reports (DAT), corrections (COR), and deletions (DEL).
4.  Receive, match, and display acknowledgements (RET) from the ERS.
5.  Print hard copies of logbook and landing data.
6.  Encrypt and transmit XML data via email as the primary method.
7.  Enforce user authentication and record the user ID for each report.

**Key Users & Usage Scenarios**
Primary users are the Vessel Owner and the Vessel Master. The Owner sets up the system and creates a unique ID for the Master. The Master (and potentially other crew with IDs) enters fishing data during a voyage. Typical scenarios include daily reporting of catches, reporting immediately after a transhipment, and submitting a landing declaration upon return to port.

**Major External Interfaces**
The system must interface with the UK Fisheries Administrations' ERS via email (primary method), sending encrypted XML attachments. It may interface with other onboard systems (e.g., GPS) to auto-populate data. It outputs to an onboard printer.

**Key Non-functional Requirements**
*   **Performance:** Must transmit reports automatically at specified events (e.g., immediately after last fishing operation, immediately on departing port).
*   **Security:** All XML transmissions must be encrypted using PGP. The system must enforce user authentication (username/password) and record the user ID in each report.
*   **Reliability:** Must retain all logbook reports and corrections at least until the end of the fishing trip.
*   **Maintainability:** Software updates must not impact compliance with the core regulations; if they do, the product requires re-approval.
*   **Compliance:** Data must be validated against the UK XML/XSD before transmission. All dates and times must be in UTC, and the UI must use English (UK) localization.

**Constraints, Assumptions & Dependencies**
*   **Constraint:** The system is only for use at sea on approved onboard systems.
*   **Constraint:** Corrections and deletions can only be sent for reports from the current fishing trip, up to the End of Fishing report.
*   **Dependency:** Relies on the UK Fisheries Administrations providing and maintaining the ERS, the official XML schemas (XSDs), and valid code lists.
*   **Assumption:** An onboard email system is available for data transmission.

**Priorities & Acceptance Approach**
All specified functional and non-functional requirements are compulsory for regulatory compliance. Acceptance is governed by a formal ELSS Approval Programme, where suppliers must complete a Product Profile questionnaire and a Self-Declaration Form. Conformance is validated through auditing and testing against this specification.