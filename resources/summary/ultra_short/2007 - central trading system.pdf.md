**Purpose & Scope**  
The Central Trading System (CTS) is a subsystem within the Stock Trading System, handling stock instruction matching and processing. It processes buy, sell, and cancel orders, validates instructions, and interfaces with other subsystems. It does not manage user accounts, handle fund transfers directly, or provide end-user UIs.  

**Product Background / Positioning**  
CTS operates as a core component within the Stock Trading System, interacting with six subsystems including Trade Client Serve, Security Account Management, and Trading Information Release. It processes instructions from Trade Client Serve and sends results to Information Release and Trading Management modules.  

**Core Functional Overview**  
- Match buy/sell instructions using price and time priority.  
- Cancel valid trading instructions.  
- Save successful trade records to Security Account Management.  
- Query trade data for statistical analysis and release.  
- Reject instructions violating price limits.  
- Remove outdated instructions after one day.  

**Key Users & Usage Scenarios**  
End-users (via Trade Client Serve) submit buy/sell/cancel orders. System maintainers (Java/socket experts) manage crashes and updates. Primary scenarios include matching orders during trading hours, canceling pending orders, and retrieving trade history for reporting.  

**Major External Interfaces**  
Interfaces with Trade Client Serve (for instruction input), Security Account Management (for trade data storage), and Trading Information Release (for query responses). All via defined system interfaces; no protocol or UI details specified.  

**Key Non-functional Requirements**  
Must process frequent instructions without crash during peak load. Outdated instructions automatically removed within 24 hours. System maintainers must recover from crashes when overhead exceeds capacity.  

**Constraints, Assumptions & Dependencies**  
CTS is strictly a subsystem of the Stock Trading System; no standalone operation. Requires integration with Trade Client Serve and Trading Management subsystems. No external dependencies beyond the Stock Trading System ecosystem.  

**Priorities & Acceptance Approach**  
Essential functions (matching, canceling, saving, querying, limit checks) must be implemented in first increment. Acceptance based on successful instruction matching per price/time priority, correct data persistence, and timely removal of outdated instructions.