# EIRENE System Requirements Specification

## 1. Introduction

### 1.1 General
This specification defines a digital radio standard for European railways, forming part of the technical interoperability specification. It encompasses ground-train voice and data communications, along with ground-based mobile communications needs of trackside workers, station and depot staff, and railway administrative and managerial personnel.

### 1.2 Scope
The EIRENE System Requirements Specification defines a radio system satisfying the mobile communications requirements of European railways. It ensures interoperability for trains and staff crossing national or other borders between systems, and intends to provide manufacturing economies of scale.

### 1.3 Applicability
The specification distinguishes between requirements affecting railway network infrastructure (onto which mobiles will roam) and requirements concerning mobiles which may be used in any EIRENE compliant network.

### 1.4 System Overview
The system is based on the ETSI GSM standard, supplemented by:
- GSM services: voice broadcast service, voice group call service, enhanced multi-level precedence and pre-emption, General Packet Radio Service (GPRS)
- Railway specific applications: functional and location dependent addressing, emergency calls, shunting mode, multiple driver communications, direct mode facility
- Railway specific features: link assurance signal, calling and connected line presentation of functional identities, cab radio interfaces, environmental specifications

### 1.5 Structure
Specification divided into sections covering:
- Introduction
- Network requirements
- Network configuration
- Mobile equipment core specification
- Cab radio
- General purpose radio
- Operational radio
- Controller equipment specifications
- Numbering plan
- Subscriber management
- Functional numbering and location dependent addressing
- Text messaging
- Railway emergency calls
- Shunting mode
- Direct mode
- References

## 2. Network Requirements

### 2.1 GSM Teleservices
Mandatory services:
- Telephony (speech transmission)
- Emergency calls
- Voice Group Call Service (VGCS)
- Voice Broadcast Service (VBS)
- Short message services (optional)

### 2.2 GSM Bearer Services
Mandatory services:
- Asynchronous 2.4 kbps (transparent and non-transparent)
- Asynchronous 4.8 kbps (transparent and non-transparent)
- Asynchronous 9.6 kbps (transparent and non-transparent)

### 2.3 GSM Supplementary Services
Mandatory services:
- Calling Line Identification Presentation (CLIP)
- Connected Line Identification Presentation (CoLP)
- Call Forwarding Unconditional (CFU)
- Call Forwarding on Mobile Subscriber Busy (CFB)
- Call waiting (CW)
- Call hold (HOLD)
- Multi Party Service (MPTY)
- Closed User Group (CUG)
- Barring of Incoming Calls when Roaming Outside the Home PLMN Country (BIC-Roam)
- BOIC except those to Home PLMN Country (BOIC-exHC)
- Unstructured Supplementary Service Data (USSD)
- Sub-addressing
- Enhanced Multi-Level Precedence and Pre-emption (eMLPP)
- User-to-User Signalling 1 (UUS1)

### 2.4 Railway Specific Services
Mandatory services:
- Functional addressing
- Location dependent addressing
- Shunting mode
- Multiple driver communications
- Emergency calls

## 3. Network Configuration

### 3.1 Coverage
Minimum values:
- 95% coverage probability at 38.5 dBmV/m (-98 dBm) for voice and non-safety critical data
- 95% coverage probability at 41.5 dBmV/m (-95 dBm) on lines with ETCS levels 2/3 for speeds ≤ 220km/h

### 3.2 Handover
Handover success rate should be at least 99.5% over train routes under design load conditions.

### 3.3 Call Setup Time
Call setup times shall be achieved with authentication and ciphering procedures enabled.

### 3.4 Frequency Band
Network shall operate in R-GSM band (876-915/921-960 MHz).

## 4. Mobile Equipment Core Specification

### 4.1 Radio Interface
All mobiles shall be capable of operation in R-GSM frequency bands (876-915/921-960 MHz).

### 4.2 Power Classes
- Cab radio: Power class 2 (8W)
- General purpose radio: Power class 4 (2W)
- Operational radio: Power class 4 (2W)

### 4.3 Services and Facilities
Support for all mandatory GSM teleservices, bearer services, and supplementary services as defined in section 2.

## 5. Cab Radio

### 5.1 System Components
Architecture comprises:
- GSM Mobile Termination (GSM-MT)
- Direct Mode Mobile Termination (DM-MT)
- EIRENE Cab radio applications
- Man Machine Interface (MMI)

### 5.2 Driver Call-Related Functions
Mandatory functions:
- Call controller with 'Railway operation' priority
- Call other drivers in area using group call with eMLPP priority level 2
- Send Railway emergency call
- Communicate with other drivers on same train using GSM Multi-Party service
- Call train staff using functional number
- Call other authorised users as standard GSM telephone
- Receive short (SMS) text messages
- Support shunting mode communications
- Support direct mode communications (optional)

### 5.3 MMI Functions
Mandatory functions:
- Switch radio on and off with automatic self-testing
- Adjust loudspeaker volume with 5 levels
- Register and deregister train number using USSD
- Register and deregister stock number

### 5.4 Environmental and Physical
Requirements:
- Operating temperature range: -20°C to +70°C
- Compliance with prEN 50125 for shock and vibration
- Emergency power supply for 6 hours in case of main power failure
- Protection against electrical hazards as defined in EN 50153
- EMC compliance with ENV 50121 parts 1, 2, 3-2 and 4

## 6. General Purpose Radio

### 6.1 System Components
Standard data interface for computer connection. Operates as standard GSM terminal.

### 6.2 Functions
Mandatory functions:
- Switch radio on with automatic self-testing
- Register and deregister functional number using USSD
- Receive all calls using MSISDN or group call number

### 6.3 Environmental and Physical
Requirements:
- Compliance with core climatic conditions in section 4
- Rechargeable batteries for minimum 8 hours operation
- Suitable for use with car adapter kit

## 7. Operational Radio

### 7.1 System Components
Standard data interface for computer connection. Operates as standard GSM terminal.

### 7.2 Functions
Mandatory functions:
- Switch radio on with automatic self-testing
- Register and deregister functional number using USSD
- Call controller with 'Railway operation' priority
- Send/receive Railway emergency call
- Support shunting mode communications (optional)
- Support direct mode communications (optional)

### 7.3 Environmental and Physical
Requirements:
- Compliance with section 4 standards
- IP 54 protection minimum
- Rechargeable batteries for minimum 8 hours operation
- Suitable for use with car adapter kit

## 8. Controller Equipment Specifications

### 8.1 Termination of VGCS/VBS Calls
Entitled controller may terminate VGCS/VBS call using DTMF sequence "***".

### 8.2 Muting and Unmuting for VGCS Calls
Muting and unmuting in line with GSM specifications using DTMF sequences.

## 9. Numbering Plan

### 9.1 General
International standardisation required for interworking between networks. Numbers will not exceed 15 digits and consist of digits 1-9 and 0.

### 9.2 Types of Numbers
Within GSM-R network, user shall be able to dial:
- National EIRENE Number (NEN)
- International EIRENE Number (IEN)
- MSISDN numbers
- Short Dialling Code (SDC)
- Breakout Codes for external network access

### 9.3 National EIRENE Number Structure
Consists of three parts:
1. Call Type (CT) prefix
2. User Identifier Number (UIN)
3. Function Code (FC)

### 9.4 International EIRENE Number Structure
Consists of:
- International Code (IC)
- National EIRENE Number (NEN)

## 10. Subscriber Management

### 10.1 Allocation of Priorities
Mandatory allocation of UIC priority levels to eMLPP priority codes:
- Priority 0: Railway emergency with pre-emption
- Priority 1: Public emergency and group calls between drivers
- Priority 2: Railway operation
- Priority 3: Railway information and all other calls
- Priority 4: Control-command information

### 10.2 Network Selection
SIM cards shall contain list of authorised networks displayed in priority order:
- Home EIRENE network
- Foreign EIRENE networks
- Non-EIRENE networks

## 11. Functional Numbering and Location Dependent Addressing

### 11.1 Functional Numbering
Provides mechanism for addressing mobile terminal by function number rather than permanent subscriber number.

### 11.2 Functional Number Management
USSD messages and protocols as specified in GSM Follow-me service for:
- Train number
- Engine number
- Coach number
- Shunting team number
- Maintenance team number

### 11.3 Presentation of Functional Identities
Calling party functional number passed to receiving mobile using User-to-User Signalling (UUS1) during call setup.

### 11.4 Location Dependent Addressing
Minimum requirement: call routing using short codes in conjunction with cell dependent routing.

## 12. Text Messaging

### 12.1 System Requirements
Where text messaging implemented, Short Message Service (SMS) shall be used.

## 13. Railway Emergency Calls

### 13.1 Provision
Railway emergency calls defined as calls of 'Railway emergency' priority routed to pre-defined user or group due to railway operational emergency.

### 13.2 Initiation
Railway emergency call initiated using appropriate function code for required type.

### 13.3 Receipt
Mobiles shall store list of emergency Group IDs in SIM appropriate to function.

### 13.4 Confirmation
Confirmation of Railway emergency calls implemented using User-to-User Signalling (UUS1).

## 14. Shunting Mode

### 14.1 System Requirements
Purpose: effective communication for personnel involved in shunting operation.

### 14.2 Enter Shunting Mode
Operational radio determines if shunting group ID already activated on SIM.

### 14.3 Leave Shunting Mode
Two possibilities for shunting leader:
- Release group call: all members leave and deregister
- Maintain group call: leader leaves momentarily but members remain active

## 15. Direct Mode

### 15.1 Introduction
Operational requirements:
1. Short range fall-back communications between train drivers and trackside personnel in event of GSM service failure
2. Short range communications for railway personnel in remote areas without GSM facilities

### 15.2 System Requirements
Implementation optional but where implemented:
- Frequency modulated equipment conforming to ETS 300 086
- Maximum transmit power of 1 Watt
- Sensitivity at least -107dBm
- Operation in specified channels (876.0125 MHz to 876.0625 MHz)
- Simplex mode operation
- Voice transmission only when PTT button pressed
- Continuous Tone Coded Squelch Systems (CTCSS) at 203.5 Hz
- Common access channel (channel 1) at 876.0125 MHz
