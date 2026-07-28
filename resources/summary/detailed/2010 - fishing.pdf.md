# Detailed Summary: UK Fishing Vessel’s Electronic Logbook (ELSS)

## Background and Scope
This document specifies the functional requirements for an Electronic Logbook Software System (ELSS) for UK fishing vessels exceeding 15 meters in length, mandated by EU regulations (EC No. 1966/2006 and 1077/2008). The system must capture, validate, and transmit fishing activity data to the UK Fisheries Administrations' Electronic Recording and Reporting System (ERS) via XML. It includes a Product Profile for supplier conformance declaration and a Self-Declaration Form. Non-goals include onshore use by agents (handled via ERS website) and support for non-UK regulatory formats beyond specified third-country requirements (e.g., Norway).

## Stakeholders Matrix and Use Cases
*   **UK Fisheries Administrations (UKFA):** Define requirements, validate submissions, and operate the ERS for compliance monitoring.
*   **ELSS Supplier/Developer:** Builds and maintains the ELSS software, completes the Product Profile, and seeks approval via the ELSS Approval Programme.
*   **Vessel Owner:** Purchases and installs the ELSS, sets up user accounts, and ensures the vessel operates with an approved system.
*   **Vessel Master:** Uses the ELSS to record and submit all mandatory fishing reports, manages subordinate users, and ensures timely transmissions.
*   **Onboard Crew/Users:** May input data under the Master's supervision, with actions tied to their unique user ID.
*   **Validation Authority (e.g., NCC Group):** Independently tests and validates ELSS products against the specification for approval.
*   **Third-Country Authorities (e.g., Norway):** Require specific additional data (e.g., haul-by-haul) when UK vessels operate in their waters.

**Main Scenarios:**
1.  **Daily Fishing Report:** Master submits a daily Fishing Activity Report (FAR) by midnight UTC.
2.  **Departure & Return:** System prompts for Departure (DEP) and Return to Port (RTP) reports.
3.  **Event-Driven Reporting:** System allows manual triggering of reports for events like Transhipment (TRA), Discard (DIS), or Zone Entry/Exit (COE/COX).
4.  **Correction/Deletion:** Master corrects or deletes a report from the current trip before submitting the End of Fishing (EOF) report.
5.  **Landing Declaration:** Master submits a Landing Declaration (LAN) after landing catch.

**Exception Scenarios:**
1.  **Transmission Failure:** System alerts the Master if an acknowledgment (RET) is not received within a preset time.
2.  **Inspection:** Master flags and submits a report immediately prior to an inspection at sea.
3.  **Third-Country Fishing:** System captures and reports additional data fields required for operations in specific zones (e.g., Norwegian waters).

## Business Process
**Main Process: Record and Submit Fishing Report**
1.  **Trigger:** A fishing event occurs (e.g., daily catch, departure, landing).
2.  **Input:** User (Master/crew) logs in and enters data via ELSS capture screens.
3.  **Validate:** ELSS validates data against the UK XML/XSD schema.
4.  **Generate:** ELSS formats the data into a structured XML file with a unique GBRRN (RSSNo+Date+Seq).
5.  **Transmit:** ELSS encrypts (PGP) the XML file, attaches it to an email with a specific subject, and sends it to the UK ERS.
6.  **Acknowledge:** UK ERS sends a return acknowledgment (RET); ELSS matches it to the original message.
7.  **Store:** ELSS retains the report locally at least until the end of the trip (after LAN or TRA).
8.  **Output:** Successful transmission record and/or error message from RET displayed to user.

**Key Branch A: Correct a Previous Report**
1.  **Trigger:** Master identifies an error in a previously sent report from the current trip.
2.  **Input:** Master selects the report to correct and enters corrected data.
3.  **Process:** ELSS generates a Correction (COR) operation containing the *entire* corrected report.
4.  **Output:** COR message is transmitted, replacing the original in ERS.

**Key Branch B: Handle Test Transmission**
1.  **Trigger:** Master or supplier initiates a system test.
2.  **Input:** User activates test mode.
3.  **Process:** ELSS generates a test message (with TS flag) and transmits it to the test ERS address.
4.  **Output:** Test acknowledgment is received; no data is stored by ERS.

## Domain Model
Core entities and their key fields:
1.  **Vessel:** RSS Number (required, unique), CFR Number, Name, Flag State.
2.  **Voyage/Logbook:** GBRLOGNO (required, unique: RSSNo+Year+Seq), Start Date/Time, Master Name (required).
3.  **Report:** Type (e.g., DEP, FAR, LAN) (required), GBRRN (required, unique: RSSNo+Date+Seq), Date/Time (required, UTC).
4.  **Operation:** Type (DAT, DEL, COR, RET) (required), Operation Number (required).
5.  **Catch/Species:** Species Code (required, reference to FAO list), Weight (required if not counted), Number of Fish (required if counted).
6.  **Gear:** Gear Type (required, reference to FAO codes), Mesh Size, Deployment Details.
7.  **Position:** Latitude (required), Longitude (required), based on WGS84.
8.  **User:** Username (required, unique per system instance), Role, associated with each report entry.

## Interfaces and Integrations
| System | Direction | Interaction Points / Theme | Input Key Points | Output Key Points | SLA Key Points |
| :--- | :--- | :--- | :--- | :--- | :--- |
| UK ERS | Outbound | Email transmission of XML reports | Encrypted PGP attachment, Subject: `ERS – <GBRRN>` | Acknowledgment (RET) message with status | Daily reports by 24:00 UTC; immediate for events like departure, transhipment |
| Onboard GPS/Navigation | Inbound | Populate report date, time, position | Latitude, Longitude, UTC Timestamp | Auto-filled fields in POS and report headers | Accuracy as per vessel's navigation system |
| Onboard Weighing Systems | Inbound | Populate catch weight data | Weight measurements by species | Auto-filled weight fields in SPE declarations | Calibration to meet regulatory standards |
| ELSS Supplier Update Server | Inbound | Software updates & patches | Update packages | Updated ELSS software version | Must not break approved functionality; may require re-approval |
| UK Fisheries Website | Outbound | Approved Product Register listing | Supplier-provided commercial description | Public listing of approved product name & supplier | Updated upon successful approval |

## Acceptance Criteria
**Capability: Submit Daily Fishing Activity Report (FAR)**
*   **Given** the vessel has conducted fishing activity, **when** the Master submits the daily FAR before 24:00 UTC, **then** the ELSS validates the data, generates a valid XML (DAT operation), and transmits it to UK ERS.
*   **Given** a transmitted FAR report has an error, **when** the Master corrects it before the EOF report, **then** the ELSS sends a COR message with the complete corrected FAR.

**Capability: Transmit and Receive Acknowledgment**
*   **Given** any report (DAT, DEL, COR) is sent, **when** the UK ERS processes it, **then** the ELSS receives and matches a RET message, displaying success or error to the user.
*   **Given** a report is sent, **when** no RET is received within the Master-set time limit, **then** the ELSS alerts the Master.

## Non-Functional Metrics
*   **Performance:** System must allow data entry and report generation without significant delay under typical onboard conditions. Must support generation and queuing of reports during potential communication outages.
*   **Reliability:** ELSS must retain all trip data locally until a successful LAN or TRA report is sent. Must have a test mode to verify end-to-end communication.
*   **Security:** All XML transmissions must be PGP encrypted. System access must require user authentication (username/password). Each ELSS instance must have a unique identifier included in transmissions.
*   **Compliance:** Must adhere to EU regulations (EC 1966/2006, 1077/2008) and UK-specific XSD schemas. Software updates must not violate approved functionality without re-approval.
*   **Observability:** System must provide clear status on transmitted and acknowledged reports. User interface must clearly identify corrected or deleted records.

## Milestones and Release Strategy
1.  **Supplier Development:** ELSS product developed against specification v1.2.
2.  **Conformance Submission:** Supplier completes Product Profile and Self-Declaration Form.
3.  **Validation & Testing:** Independent validation by the appointed authority.
4.  **Approval & Listing:** Product added to the UKFA's Approved Product Register.
5.  **Vessel Rollout (Phase 1):** Installation on vessels >24m (by 1 Jan 2010).
6.  **Vessel Rollout (Phase 2):** Installation on vessels >15m (by 1 Jul 2011).

## Risk List and Mitigation Strategies
1.  **Communication Failure:** Mitigation: ELSS queues reports and retries transmission; alerts Master.
2.  **Data Entry Errors:** Mitigation: Built-in validation against XSD; clear UI; ability to send COR messages.
3.  **Software Updates Breaking Compliance:** Mitigation: Requirement for re-approval if updates impact core functions; version control.
4.  **Onshore Use by Agents:** Mitigation: ELSS is restricted to onboard use; agents use the separate ERS web portal.
5.  **Third-Country Regulation Changes:** Mitigation: Specification includes conditional (CIF) fields for known requirements (e.g., Norway); future updates may be needed.
6.  **Hardware/OS Incompatibility:** Mitigation: Supplier must declare supported operating systems in the Product Profile.
7.  **User Authentication Issues:** Mitigation: Requirement for unique user IDs and password protection.
8.  **Incorrect Transmission Frequency:** Mitigation: System prompts and can automate daily reports; Master override capability.

## Undecided Issues and Responsible Parties
1.  **Support for alternative transmission protocols** (other than email): To be evaluated by UKFA based on supplier proposals.
2.  **Detailed interface specifications for onboard weighing/GPS systems:** To be defined by ELSS suppliers based on vessel equipment.
3.  **Process for handling major changes to the EU ERS data standard:** UKFA to communicate updates and provide new XSDs.
4.  **Long-term archival strategy for data on the ELSS device:** Responsibility of the vessel owner/Master; specification only requires retention until end of trip.
5.  **Certification process for PGP encryption implementation:** Validation Authority to test during approval.
6.  **Specific "Man-Machine Interface" design for sea conditions:** ELSS Suppliers to implement appropriately; noted as optional (SHOULD) guidance.
7.  **Formal process for de-listing an approved product:** UKFA to establish policy.
8.  **Handling of data for future bilateral agreements:** UKFA to update specification as needed.