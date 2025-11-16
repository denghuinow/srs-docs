# UK Fishing Vessel's Electronic Logbook Functional Requirements Specification

## 1. Introduction

### 1.1 Purpose
This document specifies the Functional Requirements Specification for UK Fishing vessel's Electronic Logbook and enables suppliers to identify parts of the specification supported by their product for validation within the Electronic Logbook Software System (ELSS) Approval Programme.

### 1.2 Scope
Provides the UK Fishing Vessel's Electronic Logbook Functional Requirements Specification for the ELSS Approval Programme, implementing Council Regulation (EC) No. 1966/2006 for EC fishing vessels exceeding 15 metres in overall length.

## 2. Functional Requirements Specification

### 2.1 General Requirements
- ELSS must capture all data necessary for recording fishing activities
- ELSS must output data as XML file for transmission to UK fisheries administrations' ERS system
- ELSS data must be validated against UK XML/XSD before transmission
- ELSS data must be transmitted at required times
- Each ELSS data transmission will be acknowledged by return message from UK fisheries administrations' ERS system

### 2.2 Data Operations
Four main Data Operations:
- Data operation (DAT) - capture and deliver formatted ELSS data for transmission
- Delete operation (DEL) - capture and deliver formatted deletion request for previously sent data
- Correction operation (COR) - capture and deliver formatted correction request for previously sent data
- Receipt of acknowledgment operation - match acknowledgment with original message

### 2.3 Report Types
ELSS Report Types to be transmitted:
- Departure (DEP)
- Fishing Activity (FAR)
- Relocation of Catch (RLC)
- Transhipment (TRA)
- Entry into Zone (COE)
- Exit from Zone (COX)
- Control Point Area (GBRCON)
- Discard (DIS)
- Prior Notification of Arrival to Port (PNO)
- End of Fishing (EOF)
- Return to Port (RTP)
- Landing Declaration (LAN)

### 2.4 Data Definitions
- Data definitions for each report type required for transmission
- Data definitions provide for capture of items required for 3rd country requirements
- ELSS may provide means for recording additional data without interfering with required functions

### 2.5 Capture Functions
- ELSS must provide data capture screens for logbook, transhipment and landing declaration data
- ELSS must use English (UK) localizations
- All dates and times must be UTC
- Electronic Logbook data may be populated from other onboard systems (GPS, weighing systems, databases)

### 2.6 Printing Features
- ELSS must provide ability to print ELSS logbook data using onboard printer
- ELSS may generate formatted electronic print file for on-shore distribution
- Electronic print files must be protected from modification once generated
- ELSS may provide features for other print requirements (3rd country waters, transport documents, regulatory returns)

### 2.7 Data Transmission
- ELSS must provide Electronic Logbook data for transmission to UK fisheries administrations' ERS system
- ELSS should transmit data via email as XML document attachment
- Subject header must consist of 'ERS - ' prefixed to GBRRN attribute
- XML document filename should be based on GBRRN attribute
- All XML documents must be encrypted using PGP
- Alternative communication methods may be proposed and considered

### 2.8 Frequency of Transmission
Two categories of transmission:
- Automatically by ELSS (subject to override by vessel master):
  - At least daily by 24:00 even with no catch data
  - Immediately after last fishing operation
  - Immediately on departing port
  - Immediately after transhipment
  - Immediately on completion of Landing declaration
- Generation and transmission under Master's control:
  - Before entering port
  - At time of inspection at sea
  - At request of UK fisheries administrations

### 2.9 Data Corrections
- ELSS must provide facilities to capture and deliver corrections to previously transmitted data
- Entire report must be transmitted for corrections, not piecemeal items
- Corrections must be easily identifiable within ELSS user interface
- Only permitted for reports sent during current trip up to End of Fishing report

### 2.10 Data Deletions
- ELSS must provide facilities to transmit deletions to previously transmitted data
- Only permitted for reports sent during current trip up to End of Fishing report
- Deletions must be easily identifiable within ELSS user interface

### 2.11 Acknowledgement
- ELSS must receive acknowledgment (RET) messages from UK fisheries administrations' ERS system
- ELSS must match each acknowledgment with appropriate transmitted data operation
- ELSS must confirm successful acknowledgment or display error messages

### 2.12 Test Transmissions
- Test address and logon details provided for testing
- Test facility must be used to establish communications between vessel and ERS system
- ERS system acknowledges test messages but does not store transmitted data

### 2.13 Specific High Level Requirements
- ELSS must retain all logbook reports and corrections until end of trip
- Software updates must not impact requirements compliance
- ELSS security and access controls:
  - One username/password for owner of each vessel
  - Owner can set up subsidiary users with own credentials
  - Username recorded in each report and transmission
  - Person entering data must "sign" acknowledging responsibilities
  - Each ELSS instance must have unique identifier in transmissions
- ELSS must only be supplied for use at sea and loaded onto onboard system
- Not provided for onshore use by agents or representatives
