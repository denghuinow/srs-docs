Purpose & Scope  
TACHOnet enables secure cross-border exchange of tachograph card and driving license information among EU Member States. It handles card status checks, status modifications, and assignment notifications but does not store card data or manage Member State systems. The system explicitly prevents reconstruction of a consolidated European database.

Product Background / Positioning  
TACHOnet is a central messaging hub for DG TREN (European Commission), built on the TESTA-II network to standardize communication between Member State Card Issuing Authorities (CIAs). It replaces direct bilateral communications, integrating with existing CIA systems via XML messaging without requiring changes to Member State infrastructure.

Core Functional Overview  
- Check driver’s issued cards (by driver details or card number)  
- Check tachograph card status (e.g., lost, stolen)  
- Declare card status modifications (e.g., lost, stolen, exchanged)  
- Send card/driving license assignments (for foreign licenses)  
- Generate Phonex search keys for driver names  
- Perform US/Ascii transliteration for non-Latin text  
- Generate and browse system usage statistics  
- Manage Member State configurations (add/edit/remove)

Key Users & Usage Scenarios  
Primary users: CIA clerks/enforcers (for card checks/modifications), CIA Administrators (for statistics access), and TCN Administrators (for system management). CIA clerks use the system via their Member State’s CIA application; TCN Administrators manage configuration and monitoring. Typical scenarios: road checks for card status, declaring lost cards, and adding new Member States.

Major External Interfaces  
- XML messaging interface with Member State CIAs (over TESTA-II network)  
- Secure web interface for statistics reporting (Windows authentication)  
- Administrative interfaces for system configuration (BizTalk tools)

Key Non-functional Requirements  
- Security: Non-repudiation and encryption mandatory for all transactions  
- Reliability: Few interruptions in first operational year  
- Availability: 24x7 operation with response time <1 minute for enforcement requests  
- Maintainability: System must be maintainable and extensible

Constraints, Assumptions & Dependencies  
- Constraints: System must prevent consolidated database reconstruction; Member States must use specified message formats  
- Assumptions: Single CIA point of contact per Member State; system uses TESTA-II network  
- Dependencies: Member States must implement required services; system relies on TESTA-II infrastructure

Priorities & Acceptance Approach  
Critical priorities: security, reliability, and core messaging functions. Acceptance requires validation of all functional requirements and non-functional metrics (response time, reliability) against specified criteria.