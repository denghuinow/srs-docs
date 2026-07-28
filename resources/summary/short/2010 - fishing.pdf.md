# Short Summary: UK Fishing Vessel’s Electronic Logbook Functional Requirements Specification

## Background and Objectives
This document specifies the functional requirements for an Electronic Logbook Software System (ELSS) for UK fishing vessels exceeding 15 meters, mandated by EU regulations to replace paper logbooks. Its purpose is to define the system for recording and transmitting fishing activity data to UK fisheries administrations via the Electronic Recording and Reporting System (ERS).

## In Scope
*   Mandatory data capture and XML output for fishing activities, including logbook entries, transhipments, and landing declarations.
*   Support for required report types (e.g., Departure, Fishing Activity, Landing) and data operations (Data, Correction, Deletion).
*   Onboard data entry screens, printing capabilities, and secure data transmission via encrypted email.
*   Compliance with specific UK XML schemas and data definitions for validation.
*   User access controls requiring unique logins and electronic signatures for data entry.

## Out of Scope
*   Onshore use of the ELSS by agents or representatives; they must use separate ERS web interfaces.
*   Software updates that alter core compliance without re-approval.
*   Expansion on detailed internal data structures or software implementation processes.
*   Non-UK localization or time zones; all interfaces must use English (UK) and UTC.
*   Transmission methods other than email, unless proposed and approved as an alternative.

## Stakeholders and Core Use Cases
*   **UK Fisheries Administrations:** Regulatory body defining requirements and operating the ERS for compliance monitoring.
*   **ELSS Supplier/Developer:** Company creating and submitting software for approval against the specification.
*   **Vessel Owner:** Responsible for procuring and installing approved ELSS on their vessel.
*   **Vessel Master:** Ultimate user responsible for ensuring accurate data entry, signing reports, and managing transmissions.
*   **Onboard Crew (Authorized Users):** Personnel granted access by the Master to enter logbook data.

**User Stories:**
1.  As a **Vessel Master**, I want to **enter daily catch data and fishing activities** so that **I comply with EU and UK reporting regulations**.
2.  As a **Vessel Master**, I want to **transmit logbook reports automatically or on-demand** so that **the UK Fisheries Administrations receive timely and mandatory data**.
3.  As a **Vessel Master**, I want to **receive and view acknowledgements for my transmissions** so that **I can confirm successful delivery and identify any errors**.
4.  As a **Vessel Master**, I want to **correct or delete previously sent reports for the current trip** so that **I can fix errors in my submitted data**.
5.  As an **ELSS Supplier**, I want to **complete a Product Profile questionnaire** so that **my software can be validated and approved for use on UK vessels**.
6.  As a **Vessel Owner**, I want to **set up unique user accounts for the Master and crew** so that **data entry is accountable and access is controlled**.

## Success Metrics
*   Successful validation and listing of the ELSS product on the UK Fisheries Administrations' Approved Product Register.
*   Accurate generation and transmission of all mandatory XML reports according to the defined schemas and schedules.
*   Reliable receipt and matching of system acknowledgements for all data transmissions.

## Major Constraints
*   Must comply with Council Regulation (EC) No. 1966/2006 and Commission Regulation (EC) No. 1077/2008.
*   Data must be transmitted in specific UK XML format, encrypted with PGP, and sent via email as the primary method.
*   Reports must be transmitted at least daily by 24:00 UTC and immediately after key events (e.g., departing port, completing fishing).
*   Software can only be used at sea on board vessels, not onshore.
*   All dates, times, and user interfaces must use UTC and English (UK) localization.

## Undecided Issues
*   Final acceptance and support for alternative data transmission methods beyond email.
*   Specific implementation details for interfacing with other onboard systems (e.g., GPS, weighing systems) are optional and supplier-defined.
*   The exact process and criteria for software re-approval after updates are not detailed.
*   Some data fields are conditional (CIF) based on fishing location (e.g., Norwegian waters) or gear type, leaving specific implementation to context.
*   The commercial description for the public Approved Product Register is optional for the supplier to provide.