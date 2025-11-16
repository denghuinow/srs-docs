# Balanced Summary

## Goals and Scope
This document specifies the functional requirements for the UK Fishing Vessel's Electronic Logbook system to comply with EU fishing regulations. It enables electronic recording and reporting of fishing activities for vessels exceeding 15 meters in length, replacing paper logbooks. The specification supports the ELSS Approval Programme to validate vendor products against mandatory requirements.

## Roles and User Stories
- **Vessel Master**: I want to record fishing activities electronically so that I comply with regulatory reporting requirements.
- **Vessel Owner**: I want to manage user access to the ELSS so that I can control who submits reports from my vessel.
- **Fisheries Administrator**: I want to receive standardized XML data so that I can monitor fishing activities effectively.
- **ELSS Supplier**: I want clear specification guidelines so that I can develop compliant software products.
- **System Validator**: I want test transmission capabilities so that I can verify system functionality before approval.

## Key Processes
1. **Trigger: Vessel departure** → Record and transmit departure declaration (DEP)
2. **Trigger: Daily fishing activity** → Submit fishing activity report (FAR) by midnight UTC
3. **Trigger: Fishing operation completion** → Record gear deployment and retrieval data
4. **Trigger: Catch events** → Document species and quantities caught
5. **Trigger: Zone entry/exit** → Submit crossing notifications (COE/COX)
6. **Trigger: Return to port** → Transmit prior notification (PNO) and landing declaration (LAN)
7. **Trigger: Data correction needed** → Submit complete corrected report (COR)

## Domain Data Elements
- **Vessel**: Primary Key: RSS Number; Fields: CFR Number, Name, Master, Flag State, Radio Call Sign
- **Fishing Trip**: Primary Key: Logbook Number; Fields: Departure Date, Return Date, Sequence Number, Master Name
- **Fishing Activity**: Primary Key: Activity Record ID; Fields: Date, Time, Location, Gear Type, Species Caught
- **Catch**: Primary Key: Species Record ID; Fields: Species Code, Weight, Quantity, Presentation State
- **Gear**: Primary Key: Gear Record ID; Fields: Gear Type, Mesh Size, Deployment Time, Retrieval Time
- **Transmission**: Primary Key: Message Number; Fields: Transmission Date, Time, Operation Type, Acknowledgment Status

## Non-functional Requirements
- Data must be transmitted via encrypted PGP email attachments
- System must retain all logbook reports until end of fishing trip
- User interface must support English (UK) localization
- All dates and times must use UTC timezone
- System must provide onboard printing capabilities
- Software updates must not impact regulatory compliance

## Milestones and External Dependencies
- Initial implementation for vessels >24 meters by January 2010
- Full implementation for vessels >15 meters by July 2011
- Dependence on EU Council Regulation (EC) No. 1966/2006
- Dependence on Commission Regulation (EC) No. 1077/2008
- Requirement for third-country fishing regulations (Norway, NAFO)

## Risks and Mitigation Strategies
- **Communication failures**: System must track unacknowledged transmissions and alert master
- **Data entry errors**: Provide clear validation against XML schemas before transmission
- **System updates**: Require re-approval if updates impact compliance functionality
- **User access control**: Implement unique user IDs and authentication mechanisms
- **Offline operation**: Retain data locally until transmission is possible

## Undecided Issues
- Alternative transmission methods beyond email
- Integration with specific onboard weighing systems
- Support for additional third-country requirements beyond Norway
- Hardware compatibility specifications
- Detailed user interface design standards
- Not mentioned