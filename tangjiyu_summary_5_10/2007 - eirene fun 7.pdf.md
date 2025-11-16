# EIRENE Functional Requirements Specification

## 1. Introduction

### 1.1 General
The EIRENE Functional Requirements Specification defines requirements for a digital radio standard for European railways, part of the Technical Specification for Interoperability. It specifies the functional requirements for the European Integrated Railway Radio Enhanced Network.

### 1.2 Scope
The specification encompasses ground-train voice and data communications, along with ground-based mobile communications needs of trackside workers, station and depot staff, and railway administrative personnel. It aims to provide interoperability for trains and staff crossing national borders and manufacturing economies of scale.

### 1.3 Applicability
The specification defines functional requirements to ensure core railway functionality is provided, distinguishing between requirements affecting railway network infrastructure and mobile equipment used in EIRENE-compliant networks.

### 1.4 System Overview
The system services include:
- Voice services: point-to-point, public emergency, broadcast, group, and multi-party voice calls
- Data services: text message bearer, general data applications, automatic fax, train control applications
- Call related services: closed user group, multi-level priority and pre-emption, advanced call handling
- Railway specific applications: functional addressing, location dependent addressing, shunting mode, multiple driver communications, railway operational emergency calls

## 2. Network Requirements

### 2.1 Voice Services
- Point-to-point voice calls allowing both parties to talk simultaneously
- Public emergency point-to-point voice calls
- Broadcast voice calls providing one-way communications from single user to multiple users in predefined area
- Group voice calls providing communications between users in predefined local area
- Multi-party voice communications between up to six different parties with simultaneous talking capability

### 2.2 Data Services
- Text messages (point-to-point and point-to-multipoint)
- General data applications (timetable information, maintenance, diagnostics, e-mail, remote database access)
- Automatic fax transmissions
- Train control applications supporting ERTMS/ETCS levels 2 and 3

### 2.3 Call Related Services
- Display of identity of called/calling user (telephone number and textual description)
- Priority and pre-emption mechanism with higher priority calls overriding lower priority ones
- Closed user group limiting network access to allowed EIRENE users
- Call forwarding (unconditional, busy, no reply, not reachable)
- Call hold and call waiting
- Call barring preventing users from making/receiving calls based on various criteria

### 2.4 Railway Specific Services
- Functional addressing including registration/deregistration
- Location dependent addressing
- Shunting mode
- Railway emergency calls

## 3. Network Configuration

### 3.1 Coverage and Performance
- Minimum 95% coverage over 95% of designated area for vehicle with external antenna
- Support for mobiles when stationary and traveling at speeds up to maximum allowable line speed or 500 km/h
- Seamless communication support for train speeds up to 500 km/h

### 3.2 Call Set-up Time Requirements
- Railway emergency calls: <2 seconds
- Group calls between drivers in same area: <5 seconds
- Operational mobile-to-fixed calls: <5 seconds
- Operational fixed-to-mobile calls: <7 seconds
- Operational mobile-to-mobile calls: <10 seconds
- Low priority calls: <10 seconds

### 3.3 Broadcast and Group Call Areas
- Group or broadcast call area determines which mobiles can participate
- Mobiles entering call area where railway emergency call is ongoing shall automatically join this call
- Cab Radios entering area where call to all drivers is ongoing shall automatically join unless involved in higher priority call

## 4. Mobile Equipment Core Specification

### 4.1 Services and Facilities
Three distinct mobile radio types:
1. Cab radio - for train driver and on-train systems
2. General purpose radio - for general railway personnel use
3. Operational radio - for railway personnel involved in train operations

All mobiles operate in 900 MHz frequency bands and function correctly when traveling at speeds from 0 km/h to 500 km/h.

## 5. Cab Radio

### 5.1 Functional Requirements
Driver call-related functions:
- Call controllers (primary, secondary, power supply)
- Call other drivers in area
- Send/receive Railway emergency calls
- Communicate with other drivers on same train
- Call train staff and other authorized users
- Receive incoming voice calls and terminate calls
- Receive text messages
- Enter/leave shunting mode and direct mode
- Monitor calls to other on-train users/devices

Other driver-related functions:
- Powering up/down radio with automatic self-testing
- Switch radio MMI on/off
- Select language and adjust loudspeaker volume
- Manual/directed/automatic network selection
- Register/deregister train number and stock number
- Store/retrieve numbers and invoke tests

### 5.2 Environmental and Physical Requirements
- Comply with section 4.3 requirements
- Operate on board rolling stock
- Sufficient battery capacity for typical railway use
- Continue operation for at least 1 hour in event of train power failure

### 5.3 Driver Man-Machine Interface
- Display, control panel, loudspeaker, handset with Push-To-Talk button
- Not obstruct driver's vision or hinder safe driving
- Controls suitable for use with gloves and in various lighting conditions
- Emergency call button red and protected against accidental use

## 6. General Purpose Radio

### 6.1 Functional Requirements
Call related functions:
- Call authorized users including controllers
- Send/receive Railway emergency calls
- Receive incoming calls and group/broadcast calls
- Terminate calls

Other functions:
- Switch radio on/off
- Select language and mobile radio network
- Adjust loudspeaker volume
- Register/deregister functional numbers
- Store/retrieve numbers and computer interface

### 6.2 Environmental and Physical Requirements
- Based on Commercial-Off-The-Shelf mobile design
- Small, compact and easy to carry
- Weight not exceeding 250g
- Rechargeable batteries providing minimum 8 hours operation

## 7. Operational Radio

### 7.1 Functional Requirements
Call related functions:
- Call authorized users and controllers
- Send/receive Railway emergency calls
- Receive incoming calls and group/broadcast calls
- Terminate calls
- Shunting mode communications and direct mode

Other functions:
- Switch radio on/off
- Select language and mobile radio network
- Adjust loudspeaker volume
- Register/deregister functional numbers
- Store/retrieve numbers and computer interface

### 7.2 Environmental and Physical Requirements
- Rugged design suitable for railway environment
- Withstand extreme environmental conditions
- Controls suitable for use with gloves
- Weight not exceeding 800g
- Rechargeable batteries providing minimum 8 hours operation

## 8. Controller Equipment Specifications

### 8.1 Primary Controller's MMI
- Queue all incoming calls with functional identity and priority display
- Allow controller to select queued calls
- Establish Railway emergency, public emergency, or railway operation priority calls
- Establish/close/enter/leave group calls
- Send/receive text messages

### 8.2 Other Controllers' MMIs
- Similar functionality to primary controllers with different control areas

## 9. Numbering Plan

### 9.1 Requirements
- Enable users to originate and receive calls by functional number
- Each mobile identified by unique telephone number
- Every on-train function identified by unique standard number
- Group call service areas freely configurable

### 9.2 Standardized Numbers
- Route call to most appropriate ERTMS/ETCS RBC
- Railway emergency call
- Route call to primary/secondary/power supply controllers
- Public emergency call

## 10. Subscriber Management

### 10.1 Allocation of Priorities
Five priority levels:
1. Railway emergency
2. Control-command (safety)
3. Public emergency and group calls between drivers in same area
4. Railway operation
5. Railway information

### 10.2 Call Restriction and Group Membership
- Various types of call restriction for additional security
- Mobile may be member of multiple groups with activation/deactivation capability
- Cab radios members of standard groups: Railway emergency call, 'all train drivers', shunting team, trackside worker

### 10.3 Network Selection and Access Matrix
- Authorised networks listed in order: home EIRENE, foreign EIRENE, public networks
- Access matrix defining which subscribers can contact which other subscribers

## 11. Functional Numbering and Location Dependent Addressing

### 11.1 Functional Addressing
- Address users by numbers corresponding to functional roles rather than terminal equipment
- Assign up to minimum 3 functional numbers to EIRENE user at any time
- Only one EIRENE user assigned to given functional number at any time
- Functional number remains valid as user roams between networks

### 11.2 Location Dependent Addressing
- Route calls based upon user's location
- Functions include Primary controller, Secondary controller, Power supply controller, Train management centre
- Location information derived from network itself or external systems

## 12. Text Messaging

### 12.1 Service Definition
- Transfer text messages between ground and mobile(s)
- Mandatory for Cab radio, optional for ground
- Maximum length of message segment: 96 characters
- Transfer time for each segment less than 30 seconds for 95% of messages

## 13. Railway Emergency Calls

### 13.1 Types and Management
Two types:
- Train emergency call sent to all drivers and controllers in predefined area
- Shunting emergency call sent to all users involved in shunting operations

Three distinct phases:
1. Stage 1: Warning with audible indication for 5 seconds
2. Stage 2: Information allowing originator to give emergency details
3. Stage 3: Terminate call by originator, controller, or network

### 13.2 Confirmation
- Automatic confirmation generated without user input
- Confirmation message contains timing and identification information
- Received at central location with 99% probability within 5 minutes of call termination

## 14. Shunting Mode

### 14.1 Functional Requirements
- Shunting call as group call with 'Railway operation' priority
- Link assurance signal providing end-to-end confirmation of voice communication link
- Shunting communication protected from unintentional/unauthorized access
- Only one member can transmit link assurance signal at any time

### 14.2 Group Membership
- Shunting group consists of shunting leader, shunting driver, up to three shunting team members
- Controller can be permanently/temporarily associated with shunting group
- Only shunting leader can communicate with external users

## 15. Direct Mode

### 15.1 Functional Requirements
Optional facility providing short range fall-back communications:
- Range up to at least 2000m in open terrain
- Voice only capability supporting link assurance signal
- Open channel mode with all users receiving transmissions when in range
- Minimum one channel available for direct mode
- Simple controls: direct mode on/off switch, Push-To-Talk, channel selection, volume control
- Battery life minimum 8 hours
