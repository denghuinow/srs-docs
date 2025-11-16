# Enterprise E-mail Functional Requirements Specification

## 1. Enterprise E-mail Scope
Establishment of a statewide electronic mail system as an enterprise information technology service designed to meet the needs of all executive branch agencies and reduce current cost of operation and support. The system includes service delivery and support for a statewide e-mail, messaging, and calendaring service.

Key requirements for the proposed plan:
- Analysis of in-house and external sourcing options (internally hosted system, externally sourced system, combined option)
- Cost-benefit analysis estimating all major cost elements (nonrecurring and recurring costs) for each sourcing option
- Comparison of total cost of each enterprise e-mail sourcing option and existing e-mail services
- Estimated expenditures for each state agency associated with e-mail costs for 2009-2010 fiscal year
- Identification of existing e-mail infrastructure for reuse
- Analysis of each sourcing option's ability to meet federal and state requirements for confidentiality, privacy, and security
- Complete description of scope of functionality, operations, and required resources for each sourcing option
- Recommendations for standardizing format of state e-mail addresses
- Reliable schedule for decommission of all state agency e-mail systems and migration of all agencies to new system (beginning by July 1, 2010, completing by June 30, 2013)

## 2. Requirements Workgroup Methodology
Process for gathering and categorizing requirements as either "basic" or "extended":
- Review 2006 e-mail survey and additional historical documentation
- Create 2009 e-mail survey
- Send survey to agency e-mail (business) experts
- Compile survey results into formal requirements specification
- Obtain requirements approval from key stakeholders

Survey categories included:
- E-mail, Calendar, & Contacts (user interface and administrative requirements)
- Archiving, Retention, Search, Discovery requirements
- Disaster Recovery requirements
- Backup & Restore requirements
- Security, Anti-Virus, Filtering requirements
- Remote Access & Mobile Messaging requirements
- Additional E-mail requirements

Decision factors for basic vs. extended requirements:
- Percentage of agencies that currently provide the capability
- Number of total users currently supported
- Legal necessity of fulfilling the requirement

## 3. Requirements Workgroup Goals
- Manage Scope: Ensure requirements remain within preliminary scope statement
- Manage Time: Complete specification within 6 weeks (30 business days)
- Use 2006 Messaging Optimization Workgroup Survey as basis for 2009 survey
- Ensure completeness for RFI/RFP/ITN submission
- Include attachment with narrative and breakdown of existing agency resources
- Include attachment listing agencies' risks, issues, or constraints affecting transition

## 4. Requirements Workgroup Glossary
- Basic requirements: Functional requirements that should be met as part of the "basic" (minimal) solution-offering
- Extended requirements: Functional requirements that could be met as part of the "extended" solution offering
- E-mail, Calendar, Contacts: End-user services found in all e-mail platforms in use by the State
- Archiving, Retention, Discovery: Method of retaining e-mail messages to comply with legal requirements
  - Archiving: Systematic approach to saving and protecting e-mail messages
  - Retention: Period of time e-mail messages are retained to meet requirements
  - Discovery: Ability to search e-mail archives based on specific criteria for legal requests
  - Search: Ability to scan e-mails based on criteria such as sender, date, subject, content
- Disaster Recovery: Services that allow an agency to continue working during/after a disaster
- Backup & Restore: Making copies of data for recovery after data loss event
- Security, Anti-Virus, Filtering: Services that protect end-user from inappropriate/threatening messages
- Remote Access, Mobile Messaging: Method by which user can access e-mail by means other than at work site
- Additional E-mail Services: Features allowing users to communicate beyond sending e-mail

## 5. Basic Functional Requirements

### 5.1 E-mail, Calendar, Contacts
- Send, receive, and delete e-mail and attachments
- Reply to e-mail and attachments
- Forward e-mail and attachments
- Print e-mail messages
- Customize e-mail messages with word processor-like formatting features
- Establish rules (auto reply, out of office reply, temporary transfer, move files to inbox folders)
- Spell check
- Organize content into personal folders or similar storage mechanism
- Migrate existing public folders into statewide e-mail system
- Create and manage public folders for collection, organization, and sharing of information
- Create contact lists, including those imported from other sources
- Export contact lists
- Share contact lists/address book
- Create and share distribution lists (including query based distribution lists from LDAP-like directory services)
- Create calendars and customize calendar views
- Schedule resources such as conference rooms, teleconference rooms
- Create reminders and tasks
- Accommodate programmer testing of e-mail functionality embedded in software applications
- Share inbox, calendar, and files with users given permission
- Delegate permissions to another user
- Embed links to files and websites in e-mails
- Provision e-mail accounts (including integration with LDAP-like directory services)
- Search for e-mails based on age, size, sender, recipient, subject, keyword, attachment content
- Auto-enforce standard conventions for creating accounts and distribution lists
- Control message size limits for e-mail (inbound and outbound)
- Create generic email accounts/addresses accessed by multiple users
- Customize view in client application (adding fields, arranging fields, ordering emails by fields)

### 5.2 Archiving, Retention, Discovery
- Archive at the desktop
- Provide server based archiving solution
- Archive at various regularly defined intervals
- Search archive and forward, print and restore in bulk items from archive
- Filter archive by sender, recipient, date, subject, content, attachments, keyword
- Provide long term retention separate from active e-mail system
- Provide individual users ability to search their portion of archive repository
- Meet Federal regulations for retention (Sarbanes Oxley, GLB, HIPAA)
- Satisfy legal requests for e-mail discovery and provide printed or digital results
- Capture all sent and received e-mails into organization
- Select e-mail retention period (1 year, 3 year, or 5 year)
- Search e-mail "header" including Date, From, Subject, To, and CC
- Search "body" of e-mail including header and all text
- Perform "full text" search including header, body and attachments
- Support litigation requests by production of responsive e-mail to specified location
- Move older data to tiered storage while maintaining accessibility
- Import data from other sources (PST, NSF files) into archiving solution
- Put discovery search results on legal hold to suspend deletion
- Review and mark discovery search results
- Search using Boolean fields
- Archive based on policy (e-mail address, OU, group, organization)
- Delete or flag for deletion by system administrators e-mails that have met retention
- Flag individual e-mails to not be archived

### 5.3 Backup, Restore
- Recover at the file level
- Recover all messages
- Recover specific e-mail message
- Recover by mailbox
- Recover by time
- Maintain backup and restore event logs
- Restore previous backup without service interruption

### 5.4 Security, Anti-Virus, Filtering
- Provide pre-emptive e-mail virus protection (scanning prior to delivery at mail server)
- Provide pre-emptive e-mail content filtering
- Whitelist/blacklist senders by domain or IP address
- Block or allow e-mail based on multiple message attributes
- Integrate message hygiene (antispam/antivirus) with LDAP
- Provide message hygiene statistical reports
- Encrypt outbound e-mail
- Establish TLS encryption with other businesses or customers
- Protect reputation of outbound mail gateways
- Protect internal e-mail customer identity

### 5.5 Remote Access, Mobile Messaging
- Access e-mail by secure web or client (Calendar, Address book, send/receive)
- Access e-mail with Blackberry services using Blackberry device
- Access e-mail with non-Blackberry mobile data devices (iPhones, Treos)
- Support other mobile device protocols (ActiveSync)
- Create, Update and Delete Blackberry accounts
- Access mailbox and components via web browser over secure connection

### 5.6 Additional E-mail Services
- Send/receive e-mails within workflow applications
- Provide resource reservations integrated into e-mail
- Access SMTP bridgehead for agency applications
- Integrate agency applications into e-mail and mobile messaging environments

## 6. Extended Functional Requirements

### 6.1 Archiving, Retention, Discovery
- Manually archive to server from client
- Electronically redact information from archival storage
- Digitally certify search results
- Catalog responsive e-mail (by case) for electronic certification as complete production
- Demonstrate due diligence and maintain markings for privileged and non-responsive search results
- Provide full audit trail of discovery and review

### 6.2 Disaster Recovery
- Real-time replication to alternate site
- Near-time replication to alternate site
- Fail-over mail system and clients to alternate site

### 6.3 Security, Anti-Virus, Filtering
- Retrieve quarantined messages
- Add digital signatures to e-mail

### 6.4 Remote Access, Mobile Messaging
- Access e-mail archive
- Use wireless service with GIS

### 6.5 Additional E-mail Services
- Provide fax service integrated into e-mail
- Integrate telephone messaging (VOIP) into e-mail and vice/versa
- Provide List Server option for internal and external publishing of information
- Integrate directory services with other complimentary external systems for unified client experience
- Provide RSS Feeds

## 7. Functional Requirements Summary
Survey results showing percentage of agencies with capabilities:
- Email, Calendar, and Contacts: 97% "have and use"
- Archiving, Retention, Discovery: 66% "have and use", 23% "would like to have"
- Disaster Recovery: 59% "have and use", 34% "would like to have"
- Backup & Restore: 79% "have and use", 19% "would like to have"
- Security, Anti-Virus, Filtering: 67% "have and use", 24% "would like to have"
- Remote Access, Mobile Messaging: 71% "have and use", 11% "would like to have"
- Additional E-mail: 48% "have and use", 26% "would like to have"

Majority of requirements for each category made it into basic requirements recommendation. Extended services are especially likely for archiving, disaster recovery, security, and remote-mobile messaging categories.

Collaboration services (shared documents, workflows, instant messaging, discussion forums) remain out of scope. Technical and financial feasibility of each functional requirement will be evaluated by technical and financial workgroups before submitting proposed plan by December 31, 2009.
