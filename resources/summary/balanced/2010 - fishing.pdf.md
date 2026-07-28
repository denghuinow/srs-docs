# Balanced Summary: UK Fishing Vessel’s Electronic Logbook Functional Requirements Specification

## Goals and Scope
This document specifies the functional requirements for an Electronic Logbook Software System (ELSS) used on UK fishing vessels exceeding 15 meters in length, as mandated by EU regulations. Its purpose is to define the system's capabilities for recording, transmitting, and managing fishing activity data to ensure compliance with reporting obligations to UK fisheries administrations. The scope includes data capture, transmission protocols, validation, and the approval process for ELSS products.

## Stakeholders and User Stories
*   **Vessel Master:** Responsible for overseeing fishing operations and ensuring accurate, timely logbook entries and transmissions.
*   **Vessel Owner:** Accountable for providing and maintaining the approved ELSS on their vessel(s).
*   **ELSS Supplier/Developer:** Develops, maintains, and submits software products for approval against the specification.
*   **UK Fisheries Administrations (UKFAs):** Define the regulatory requirements, operate the receiving ERS, and manage the product approval program.
*   **Validation Authority:** Independently tests and validates ELSS products for conformance.
*   **Fisheries Monitoring Centre (FMC):** Monitors vessel activity and receives transmitted logbook data.

**User Stories:**
1.  As a **Vessel Master**, I want to enter fishing activity data into the ELSS so that I can comply with daily reporting regulations.
2.  As a **Vessel Owner**, I want to install an approved ELSS on my vessel so that it is legally permitted to operate.
3.  As an **ELSS Supplier**, I want a clear specification and approval process so that I can develop compliant software for the market.
4.  As the **UK Fisheries Administrations**, we want standardized, validated XML data from vessels so that we can effectively monitor fishing activity and enforce regulations.
5.  As the **Validation Authority**, I need a detailed product profile from suppliers so that I can efficiently test for conformance.
6.  As a **Vessel Master**, I want to receive acknowledgements for my transmissions so that I can confirm successful data delivery.

## Key Processes
1.  **Data Capture:** The Master or crew enters logbook data via ELSS screens, triggered by fishing events (e.g., departure, haul, discard).
2.  **Data Validation:** The ELSS validates entered data against the UK XML schema before allowing transmission.
3.  **Report Generation:** The system formats the data into a specific XML report type (e.g., DEP, FAR, LAN).
4.  **Data Transmission:** The ELSS encrypts and transmits the XML file via email to the UK ERS, triggered automatically (e.g., daily, post-fishing) or manually by the Master.
5.  **Acknowledgment Handling:** The system receives and matches return (RET) messages from the ERS to confirm successful receipt or indicate errors.
6.  **Correction/Deletion:** The Master can generate correction (COR) or deletion (DEL) messages for reports from the current fishing trip, triggering re-transmission of the full report.
7.  **Printing:** The ELSS can generate hard copies of logbook data via an onboard printer, triggered by user request or for specific regulatory needs.

## Domain Data Elements
*   **Fishing Trip (LOG):** Primary Key: GBRLOGNO. Key Fields: Vessel RSS Number, Master Name, Trip Start Date, Sequence Number.
*   **Report Message (ERS):** Primary Key: GBRRN. Key Fields: Message Date/Time, Operation Type (DAT/DEL/COR), Vessel Identifier.
*   **Fishing Activity (FAR):** Primary Key: Part of ERS message. Key Fields: Activity Date/Time, Catch Details (linked SPE), Gear Details (linked GEA), Position.
*   **Species Catch (SPE):** Primary Key: Part of parent report. Key Fields: Species Code (FAO), Weight, Number of Fish, Relevant Area.
*   **Gear Deployment (GEA):** Primary Key: Part of parent report. Key Fields: Gear Type, Mesh Size, Deployment Date/Time, Fishing Depth.
*   **Landing Declaration (LAN):** Primary Key: Part of ERS message. Key Fields: Landing Date/Time, Port Code, Landed Catch Details (linked SPE/PRO).

## Non-Functional Requirements
1.  The ELSS must use English (UK) localization and UTC for all dates and times.
2.  The system must retain all logbook reports and corrections at least until the end of the fishing trip.
3.  Data transmissions must be encrypted using PGP when sent as email attachments.
4.  The software must provide user access controls, requiring unique usernames and authentication.
5.  The ELSS must be designed for use at sea on a moving platform and is not for onshore use by agents.
6.  Software updates must not impact compliance; significant changes require product re-approval.

## Milestones and External Dependencies
1.  **1 January 2010:** Initial mandate for vessels >24m to use electronic logbooks.
2.  **1 July 2011 (or 1 Jan 2011 for 3rd country waters):** Mandate extends to vessels >15m.
3.  Dependence on EU Council Regulation (EC) No. 1966/2006 and Commission Regulation (EC) No. 1077/2008.
4.  Dependence on the UK Fisheries Administrations providing and maintaining the ERS receiving system and test environment.
5.  Supplier dependence on the Validation Authority for product testing and approval.

## Risks and Mitigation Strategies
1.  **Risk:** Poor or unreliable vessel communications may delay or prevent transmission.
    *   **Mitigation:** ELSS must track unacknowledged messages and alert the Master; data is retained onboard for later transmission.
2.  **Risk:** Incorrect data entry by crew leads to non-compliant reports.
    *   **Mitigation:** ELSS includes validation against the XML schema and provides clear user interfaces.
3.  **Risk:** ELSS software updates inadvertently break compliance features.
    *   **Mitigation:** Suppliers must submit significant updates for re-approval before deployment.
4.  **Risk:** System failure or damage at sea.
    *   **Mitigation:** Requirement for hard-copy printing capability as a backup.
5.  **Risk:** Complexity of reporting rules for different fishing zones (e.g., Norwegian waters).
    *   **Mitigation:** Specification includes conditional (CIF) requirements, and ELSS should guide users based on activity location.

## Undecided Issues
1.  Final acceptance criteria and testing protocols for alternative transmission methods (other than email).
2.  Specific mechanisms for agents/representatives to submit data onshore via the ERS website or offline methods.
3.  Detailed interface specifications for populating ELSS data automatically from other onboard systems (e.g., GPS, scales).
4.  Resolution of all conditional (CIF) requirements based on final bilateral agreements with third countries.
5.  The process and timeline for updating the UK XML/XSD schemas and managing version compatibility with deployed ELSS products.
6.  Specific security protocols and key management details for the PGP encryption requirement.