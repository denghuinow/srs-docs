Purpose & Scope  
System enables EU Member States to securely manage driver tachograph card status (e.g., lost, stolen) across national authorities without consolidating data. Excludes card issuance, driver licensing, and physical card manufacturing.  

Product Background/Positioning  
Operates as a centralized messaging layer within the European transport infrastructure, connecting national Card Issuing Authorities (CIAs) via the TESTA-II network to support enforcement and administrative workflows under EU regulations.  

Core Functionality  
- Check driver card status via surname/DOB or card number.  
- Check tachograph card status using card number and issuing state.  
- Declare card status changes (e.g., lost, stolen, exchanged).  
- Send card/driving license assignments between states.  
- Generate phonex search keys for name matching.  

Key Users & Scenarios  
- **Enforcement Authorities**: Perform real-time card checks during road stops.  
- **CIA Administrators**: Manage system configuration, statistics, and user access.  
- *Permissions*: Enforcement users access only card checks; administrators configure system and view usage stats.  

Key External Interfaces  
TESTA-II network for all message exchanges; no direct client-facing APIs.  

Critical Non-Functional Requirements  
24/7 system availability with enforcement request response time <1 minute.  

Constraints, Assumptions & Dependencies  
- **Hard constraint**: No consolidated European database may be reconstructed from messages.  
- **Dependency**: Must operate exclusively over TESTA-II network.  
- **Assumption**: Each Member State manages its own CIA application (no central user database).  

Priority & Acceptance  
Mandatory for EU compliance; acceptance requires verified <1-minute response time for enforcement requests and zero data consolidation capability.