# Detailed Summary

## Background and Scope
The Agency for Enterprise Information Technology (AEIT) is establishing a statewide email system as mandated by Florida Statute 282.34 to serve all executive branch agencies. The project aims to reduce operational costs while providing comprehensive email, messaging, and calendaring services. Key deliverables include a proposed plan analyzing sourcing options, cost-benefit analysis, migration schedule, and standardization recommendations. Non-goals include collaboration services such as shared documents, instant messaging, and discussion forums, which remain out of scope.

## Role Matrix and Use Cases
- **End User**: Send/receive email, manage calendar/contacts, archive messages
- **Agency Admin**: Provision accounts, manage distribution lists, handle archiving/discovery
- **Data Center Admin**: Manage system security, backup/restore, message filtering
- **Legal/OIG User**: Review discovery results, place legal holds
- **Application Developer**: Test email functionality in applications
- **SSRC Admin**: Control message size limits, system-wide configurations

Main scenarios include email composition/sending, calendar management, and archiving; exception scenarios include disaster recovery failover and legal discovery processes.

## Business Process
**Main Email Process (8 steps)**:
1. User composes email with attachments
2. System applies security filtering and virus scanning
3. Message routed to recipient's mailbox
4. Recipient receives notification
5. Recipient opens and reads message
6. Recipient can reply, forward, or archive
7. System archives message per retention policies
8. User can search and retrieve archived messages

**Key Branch - Legal Discovery (4 steps)**:
Trigger: Legal request for records
1. Admin performs advanced search across archives
2. System produces responsive records
3. Legal team reviews and marks records
4. Results provided in required format

**Key Branch - Disaster Recovery (4 steps)**:
Trigger: System outage declaration
1. Failover to alternate site initiated
2. Services restored with minimal data loss
3. Users reconnect to system
4. Normal operations resume after primary restoration

## Domain Model
- **User Account** (email: unique/required, password: required, permissions: required)
- **Email Message** (message_id: unique/required, sender: required/reference, recipients: required, subject, body, attachments)
- **Calendar Event** (event_id: unique/required, organizer: required/reference, attendees, location, time)
- **Contact** (contact_id: unique/required, name: required, email: required, groups)
- **Distribution List** (list_id: unique/required, owner: required/reference, members: required)
- **Archive Record** (record_id: unique/required, message: required/reference, retention_period: required)
- **Security Policy** (policy_id: unique/required, rules: required, filters: required)
- **Backup Set** (backup_id: unique/required, timestamp: required, scope: required)

## Interfaces and Integrations
- **LDAP Directory**: Inbound, user provisioning and authentication, user attributes, authentication status, real-time sync
- **Mobile Devices**: Outbound, email/calendar sync, device credentials, email data, push notifications, 99.5% availability
- **Archiving System**: Bidirectional, record retention and retrieval, search criteria, archived records, legal hold compliance
- **Anti-Virus Service**: Inbound, message scanning, email content, clean/quarantined messages, <2 second processing
- **Backup System**: Outbound, data protection, backup jobs, backup verification, 4-hour RTO
- **Web Client**: Outbound, user interface, user actions, display data, sub-second response
- **SMTP Gateway**: Bidirectional, email routing, outgoing messages, delivery status, 99.9% uptime
- **Legal Hold System**: Inbound, discovery requests, search parameters, case results, audit trail maintenance

## Acceptance Criteria
**Email Composition**:
- Given a user is authenticated, when they compose and send an email, then the message is delivered to recipients and archived per policy

**Account Provisioning**:
- Given an agency admin has appropriate permissions, when they create a new user account, then the account is provisioned and integrated with directory services

**Legal Discovery**:
- Given a legal hold request is received, when an admin performs a discovery search, then all responsive records are identified and preserved

**Disaster Recovery**:
- Given a system failure occurs, when failover procedures are initiated, then services are restored within defined recovery objectives

## Non-functional Metrics
- **Performance**: System supports 50,000+ concurrent users with sub-second email delivery; archive searches complete within 30 seconds
- **Reliability**: 99.9% uptime for core services; backup completion within 4-hour window
- **Security**: Multi-layered virus protection with <0.1% false positives; encrypted data transmission
- **Compliance**: Meets Florida Public Records Law and federal regulations (HIPAA, Sarbanes-Oxley)
- **Observability**: Comprehensive audit trails for all administrative actions; real-time system monitoring

## Milestones and Release Strategy
1. Requirements specification approval (Oct 2009)
2. Sourcing option analysis completion (Nov 2009)
3. Proposed plan submission to government (Dec 31, 2009)
4. Vendor selection and contracting (Q1 2010)
5. Pilot agency migration (July 2010)
6. Full migration completion by all agencies (June 2013)

## Risk List and Mitigation Strategies
1. **Budget constraints**: Conduct thorough cost-benefit analysis and consider phased implementation
2. **Agency resistance**: Develop comprehensive change management and communication plan
3. **Technical compatibility**: Inventory existing systems and plan for integration challenges
4. **Data migration complexity**: Implement staged migration with rollback capabilities
5. **Security vulnerabilities**: Implement layered security and regular penetration testing
6. **Regulatory compliance**: Engage legal experts early and maintain audit trails
7. **Resource availability**: Secure executive sponsorship and dedicated project team
8. **Scope creep**: Maintain strict scope control through change management process

## Undecided Issues and Responsible Parties
1. Final sourcing model (in-house vs. external) - AEIT leadership
2. Specific cost allocation model across agencies - Financial workgroup
3. Detailed migration sequence for all agencies - Technical workgroup
4. Exact email address standardization format - Requirements team
5. Final archiving retention periods - Legal and compliance teams
6. Mobile device support specifics - Technical workgroup
7. Integration with existing agency applications - Application teams
8. Training and support model - Not mentioned