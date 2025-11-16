# Detailed Summary

## Background and Scope
TACHOnet is a secure network system for EU Member States to exchange tachograph card information between Card Issuing Authorities (CIAs). The system enables checking driver card status, declaring card modifications, and managing card/driving license assignments while preventing reconstruction of a consolidated European database. Non-goals include managing individual CIA users and developing new cryptographic algorithms.

## Role Matrix and Use Cases
**Roles (4):**
- CIA Application: Automated system exchanging XML messages
- CIA User: Clerk/enforcer accessing web services
- CIA Administrator: Manages CIA application and views statistics
- TCN Administrator: Manages TACHOnet configuration and monitoring

**Main Scenarios (6):**
- Check driver's issued cards
- Check tachograph card status  
- Declaration of card status modification
- Send card/driving license assignment
- Generate and browse statistics
- Monitor system and manage Member States

## Business Process
**Main Process - Message Handling (6 steps):**
1. Receive and decrypt XML request
2. Validate syntax and assign TCN reference ID
3. Route to appropriate Member State(s)
4. Wait for responses with timeout handling
5. Consolidate responses
6. Encrypt and send consolidated response

**Key Branches:**
- **Timeout Handling**: Log timeout status after retries
- **Error Handling**: Validate syntax, return negative receipts for invalid messages

## Domain Model
**Entities (6):**
- Transaction (TCNRefId: required/unique, StatusCode, Timestamp)
- MemberState (CountryCode: required/unique, ContactInfo)
- CIA (Certificate: required, OrganizationDetails)
- Card (CardNumber: required, IssuingMS, Status)
- Driver (Surname, FirstNames, BirthDate, SearchKeys)
- StatisticsReport (Period, Metrics, CIAFilter)

## Interfaces and Integrations
**TESTA-II Network**
- Direction: Bidirectional
- Theme: Secure message transport
- Input: Encrypted XML messages
- Output: Encrypted XML responses  
- SLA: 24x7 availability, <1 min response for enforcement

**Web Services**
- Direction: Inbound
- Theme: Phonex and transliteration services
- Input: Driver name data
- Output: Search keys and transliterated values
- SLA: Synchronous response

## Acceptance Criteria
**Card Status Check**
- Given valid card number and issuing MS
- When status check request sent
- Then receive current card status within timeout

**Statistics Generation**  
- Given expired transactions in tracking DB
- When nightly job executes
- Then reports generated with status distribution

## Non-functional Metrics
- **Performance**: <1 min response for enforcement requests, 24x7 availability
- **Reliability**: MTBF >1 year, clean recovery from disasters
- **Security**: Non-repudiation, data privacy, restricted administrative access
- **Compliance**: TESTA-II network standards, XML messaging specifications

## Milestones and Release Strategy
1. Core messaging infrastructure
2. Member State onboarding
3. Statistics and reporting
4. Monitoring and operations
5. Future driving license network support
6. Additional transliteration standards

## Risk List and Mitigation
- **Network failures**: Automatic retry mechanism (3 attempts)
- **Member State unavailability**: Timeout handling and status reporting
- **Data encoding issues**: Phonex algorithm and transliteration services
- **Performance degradation**: Clustering and database optimization

## Undecided Issues and Responsible Parties
- Message retention period in tracking database (TCN Administrator)
- MOM monitoring configuration details (EC DI's Data Center)
- Additional transliteration standards support (Not mentioned)
- Future network migration strategy (Not mentioned)