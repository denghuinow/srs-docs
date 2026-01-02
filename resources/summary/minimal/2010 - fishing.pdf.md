**Purpose & Scope**: The system replaces paper logbooks to electronically record and report fishing activity for UK vessels over 15 meters in length, as required by EU regulations. It defines functional requirements for software to be used onboard.

**Core Functions**:
*   Capture and validate logbook, transhipment, and landing declaration data.
*   Output all data as XML validated against a defined schema.
*   Transmit data via encrypted email to the UK fisheries administration system.
*   Receive and match acknowledgements for sent reports.
*   Generate corrections and deletions for reports within the current fishing trip.

**Key Users**: Vessel owner, vessel master, and subsidiary crew members with individual credentials.

**Key Constraints**:
*   Data must be transmitted at specified times, including automatically at least daily by 24:00 UTC.
*   All transmissions must be encrypted using PGP.
*   The software is only for onboard use at sea, not for onshore agents.
*   Each software installation must have a unique identifier included in every transmission.