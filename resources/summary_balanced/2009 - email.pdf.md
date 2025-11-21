# Balanced Summary

## Goals and Scope
This project aims to establish a statewide enterprise email system for all executive branch agencies to reduce operational costs while meeting messaging, calendaring, and contact management needs. The scope includes developing a proposed plan analyzing sourcing options, cost-benefit analysis, and migration strategy by December 31, 2009. The system must support basic email functionality while addressing security, archiving, and compliance requirements.

## Roles and User Stories
- **End User**: I want to send/receive emails and manage calendars so that I can communicate effectively and organize my work
- **Agency Administrator**: I want to provision email accounts and manage distribution lists so that I can support my organization's messaging needs
- **Data Center Administrator**: I want to implement security filtering and backup systems so that I can maintain system integrity and availability
- **Legal/Compliance Officer**: I want to search archived emails and place legal holds so that I can fulfill discovery requests and compliance requirements
- **Mobile User**: I want to access email from mobile devices so that I can work remotely

## Key Processes
1. **Requirements Gathering** (triggered by project initiation) - Survey agencies to identify functional needs through structured questionnaires
2. **Solution Analysis** (triggered by requirements compilation) - Evaluate in-house vs external sourcing options with cost-benefit analysis
3. **System Design** (triggered by requirements approval) - Design system architecture meeting basic functional requirements
4. **Migration Planning** (triggered by system design) - Develop agency migration schedule from July 2010 to June 2013
5. **Implementation** (triggered by plan approval) - Deploy statewide email system according to approved design
6. **Agency Transition** (triggered by implementation) - Migrate agencies from existing systems to new enterprise system
7. **Decommissioning** (triggered by successful migration) - Retire legacy agency email systems

## Domain Data Elements
- **User Account** (Primary Key: User ID) - Email address, Display name, Department, Security permissions, Mailbox quota
- **Email Message** (Primary Key: Message ID) - Sender, Recipients, Subject, Body content, Timestamp
- **Distribution List** (Primary Key: List ID) - List name, Members, Owner, Visibility scope, Creation date
- **Calendar Event** (Primary Key: Event ID) - Organizer, Attendees, Start time, End time, Location
- **Archive Record** (Primary Key: Archive ID) - Source message, Retention period, Storage location, Compliance flags
- **Security Policy** (Primary Key: Policy ID) - Filter rules, Whitelist/blacklist, Encryption requirements, Audit settings

## Non-functional Requirements
- System must meet federal and state confidentiality, privacy, and security requirements
- Service must maintain high availability with disaster recovery capabilities
- Solution must demonstrate cost reduction compared to existing agency systems
- System must support standardized email address formats across all agencies
- Migration must complete by June 30, 2013 without service disruption
- Archiving must comply with legal retention requirements and discovery processes

## Milestones and External Dependencies
- Submit proposed plan to Governor and Legislature by December 31, 2009
- Complete agency migration by June 30, 2013
- Depend on existing email infrastructure assessment for reuse opportunities
- Require agency inventory and financial data from subsequent surveys
- Dependent on technical and financial feasibility analysis of requirements

## Risks and Mitigation Strategies
- **Technical feasibility risks** - Mitigate through thorough technical analysis of all functional requirements
- **Agency migration resistance** - Mitigate through phased migration schedule and comprehensive communication
- **Cost reduction uncertainty** - Mitigate through detailed cost-benefit analysis comparing all sourcing options
- **Compliance requirements** - Mitigate by incorporating legal and regulatory requirements into archiving design
- **System integration challenges** - Mitigate by identifying application dependencies during requirements phase

## Undecided Issues
- Final sourcing model (in-house vs external vs hybrid)
- Specific cost allocation model for agencies
- Detailed technical architecture specifications
- Exact migration sequence for all agencies
- Not mentioned
- Not mentioned