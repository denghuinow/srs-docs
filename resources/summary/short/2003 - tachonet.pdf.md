# Short Summary: TACHOnet Software Requirements Specification

## Background and objectives
TACHOnet is a network system for European Member States' Card Issuing Authorities (CIAs) to exchange information about driver smart cards and tachograph cards. The system enables secure communication between CIAs for administrative tasks like checking card statuses and generating statistics while preventing reconstruction of a consolidated European database.

## In scope
- Administrative tasks: checking driver's issued cards, verifying tachograph card status, declaring card status modifications
- Statistics generation and browsing for system usage monitoring
- Member State management and system configuration
- Secure XML message exchange between CIAs via TACHOnet
- Phonetic search key computation and transliteration services

## Out of scope
- Management of individual CIA users (clerks or enforcers) within Member States
- Validation of card status transition logic (handled by Member States)
- Research and development of new algorithms
- Reconstruction of consolidated European databases
- Direct management of Member States' internal organizational structures

## Stakeholders and core use cases
**Stakeholders:**
- CIA Application: Acts as single interface for Member State to exchange XML messages with TACHOnet
- CIA Administrator: Single user per Member State administering CIA application and accessing statistics
- CIA User: Clerks or enforcers performing administrative tasks via CIA application
- TCN Administrator: Administers entire TACHOnet services including configuration and monitoring

**User stories:**
1. As a CIA clerk, I want to check a driver's issued cards so that I can verify card validity during administrative processing
2. As an enforcer, I want to check tachograph card status so that I can validate cards during road checks
3. As a CIA administrator, I want to browse usage statistics so that I can monitor system performance and identify issues
4. As a CIA application, I want to declare card status modifications so that other Member States are informed about lost/stolen cards
5. As a TCN administrator, I want to monitor the system so that I can maintain high availability and performance
6. As a CIA user, I want to get phonetic search keys so that I can store standardized search terms for driver names

## Success metrics
- System availability 24x7 with response times under 1 minute for enforcement requests
- High reliability with few interruptions in first operational year
- Successful prevention of consolidated European database reconstruction

## Major constraints
- Must use TESTA-II network facilities for communication
- Must guarantee non-repudiation and data privacy for all transactions
- Must support various technical environments across Member States
- Must comply with existing XML messaging standards and protocols
- Must maintain operational capability for many years without major redesign

## Undecided issues
- Duration for keeping message tracking data in the database
- Specific BizTalk monitoring rules configuration for MOM integration
- Firewall configuration between TACHOnet servers and central monitoring console
- Whether TACHOnet servers will be directly monitored from central MOM console
- Implementation details for additional transliteration standards beyond Greek/Latin