# Short Summary

- **Background and objectives**: This document specifies the functional requirements for the UK Fishing Vessel’s Electronic Logbook (ELSS) to comply with EU regulations, replacing paper logbooks for vessels over 15 meters. It aims to standardize data capture, transmission, and validation for fishing activity reporting.

- **In scope**:
  - Data capture and XML output for fishing activities.
  - Transmission of logbook, transhipment, and landing declarations.
  - Support for data corrections, deletions, and acknowledgments.
  - Printing and secure electronic distribution of logbook data.
  - Compliance with UK-specific XML schemas and encryption requirements.

- **Out of scope**:
  - Onshore use by agents or representatives.
  - Non-email transmission methods without prior approval.
  - Software updates impacting core regulatory compliance.
  - Expansion of data structures beyond defined XML schemas.
  - Detailed implementation of non-UK third-country requirements.

- **Roles and core use cases**:
  - As a **vessel master**, I want to record and transmit fishing activity data so that I comply with EU and UK reporting regulations.
  - As a **product supplier**, I want to validate ELSS features against the specification so that my product can be approved for use.
  - As a **fisheries administrator**, I want to receive standardized electronic reports so that I can monitor and enforce fishing regulations.

- **Success metrics**:
  - Successful transmission and acknowledgment of all required report types.
  - Adherence to daily and event-driven reporting frequencies.
  - Accurate validation against UK XML/XSD before transmission.

- **Major constraints**:
  - Must use UTC for all dates and times.
  - Data must be encrypted using PGP for email transmission.
  - ELSS must only be used onboard and not onshore.
  - All corrections require retransmission of the full report.
  - Software updates must not affect approved functionality.

- **Undecided issues**:
  - Alternative transmission methods beyond email.
  - Integration specifics with non-UK third-country systems.
  - Not mentioned.
  - Not mentioned.
  - Not mentioned.