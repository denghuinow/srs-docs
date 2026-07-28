# Balanced Summary: TACHOnet Software Requirements Specification

## Goals and Scope
The TACHOnet system is a European network for exchanging information about driver tachograph cards between Member States' Card Issuing Authorities (CIAs). It enables secure, automated checking of card statuses, declarations of card modifications, and statistical reporting while preventing reconstruction of a consolidated European database. The system must operate 24/7 with high reliability and security across diverse technical environments.

## Stakeholders and User Stories
**Stakeholders:**
- **CIA Application:** Automated system representing a Member State's Card Issuing Authority, exchanges XML messages with TACHOnet.
- **CIA Administrator:** Single user per Member State who administers the CIA application and accesses TACHOnet statistics.
- **TCN Administrator:** Administers the entire TACHOnet system configuration, performance, and monitoring.
- **CIA User:** Clerks or enforcers within Member States who perform administrative tasks via CIA applications.

**User Stories:**
1. As a CIA Application, I want to check driver(s)' issued cards so that I can verify card delivery to similar persons.
2. As a CIA Application, I want to check tachograph card status so that I can validate cards before administrative actions.
3. As a CIA Application, I want to declare card status modifications so that I can report lost, stolen, or confiscated cards.
4. As a CIA Application, I want to send card/driving license assignments so that I can notify issuing states about new card associations.
5. As a CIA Administrator, I want to browse usage statistics so that I can monitor system performance and identify issues.
6. As a TCN Administrator, I want to monitor the system so that I can maintain high availability and performance.

## Key Processes
1. **Receive Request:** TACHOnet receives and decrypts XML requests from CIA applications (trigger: message arrival).
2. **Validate and Log:** System validates syntax, assigns tracking ID, and logs the original message.
3. **Route Requests:** Based on issuing Member State codes, TACHOnet builds and forwards requests to appropriate CIAs.
4. **Collect Responses:** System receives, validates, and stores responses from Member State CIAs.
5. **Handle Timeouts:** System manages response timeouts and late responses according to defined rules.
6. **Build Consolidated Response:** TACHOnet aggregates all responses into a single reply.
7. **Send Response:** System encrypts and sends the consolidated response to the original requester.

## Domain Data Elements
**Transaction:**
- Primary Key: TCNRefId
- Fields: RequestType, SenderCIA, Timestamp, Status, ResponseData

**Card:**
- Primary Key: CardNumber + IssuingMemberStateCode
- Fields: CardStatus, DriverName, IssueDate, ExpiryDate, SearchKeys

**Member State:**
- Primary Key: CountryCode
- Fields: CIAApplicationURL, ContactInfo, DigitalCertificate, Configuration

**Statistics Report:**
- Primary Key: ReportID + Period
- Fields: ReportType, GeneratedDate, DataRange, Metrics

**User Account:**
- Primary Key: Username
- Fields: Role, MemberState, PasswordHash, AccessRights

**Message Log:**
- Primary Key: MessageID
- Fields: OriginalMessage, Direction, Timestamp, EncryptionStatus

## Non-functional Requirements
1. **Performance:** System must respond to user requests within 1 minute despite background tasks.
2. **Reliability:** Must function with minimal interruptions, designed for many years of operational lifetime.
3. **Security:** Must provide non-repudiation, data privacy, and encryption compatible with required security levels.
4. **Usability:** Interface must guide users, be easy to learn, and allow easy error correction.
5. **Supportability:** System must be maintainable, extensible, and able to migrate to new hardware/software.
6. **Availability:** 24x7 operation required with high availability from both TACHOnet and Member State systems.

## Milestones and External Dependencies
1. Integration with TESTA-II network for communication infrastructure.
2. Dependence on Member States implementing compatible CIA applications with required XML interfaces.
3. Use of Microsoft Operations Manager (MOM) for system monitoring.
4. Reliance on SQL Reporting Services for statistics generation and reporting.
5. Compliance with XML messaging standards defined in TCN XML Messaging Reference Guide.

## Risks and Mitigation Strategies
1. **Network Failures:** Automatic retry mechanisms (3 attempts) with timeout handling and error logging.
2. **Invalid Messages:** Syntax validation with negative receipts returned to senders and administrator alerts.
3. **Member State Non-compliance:** Clear interface specifications and testing procedures before integration.
4. **Performance Degradation:** Monitoring system with alerts and scalable architecture design.
5. **Security Breaches:** Strong encryption, non-repudiation mechanisms, and restricted administrative access.

## Undecided Issues
1. Duration for keeping message logs in the tracking database before archiving.
2. Specific BizTalk monitoring rules to configure in Microsoft Operations Manager.
3. Firewall configuration requirements between TACHOnet servers and central MOM console.
4. Handling of multiple hierarchical contact points per country if organizational structures change.
5. Support for additional character set transliterations beyond Greek and Latin.
6. Procedures for removing Member States from the TACHOnet configuration.