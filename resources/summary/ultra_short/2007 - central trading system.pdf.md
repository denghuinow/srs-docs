**Purpose & Scope**
The Central Trading System (CTS) is a subsystem that completes stock trades by matching buy and sell instructions according to specific rules. It processes instructions from clients and interfaces with other subsystems to save and release trading data. It does not handle user account management, client UI presentation, or final trade settlement.

**Product Background / Positioning**
The CTS is one of six core subsystems within the larger Stock Trading System (STS). It receives trading instructions from the Trade Client Serve subsystem and sends results to the Network Message Promulgating and Trading Information Release subsystems. The Trading System Management subsystem also interfaces with it for oversight.

**Core Functional Overview**
*   Receive and validate buy, sell, and cancel instructions.
*   Match buy and sell instructions for the same stock based on price-time priority rules.
*   Execute trades when a match is found.
*   Cancel pending trading instructions upon request.
*   Save successful trade information to the Security Account Management subsystem.
*   Provide trading data to the Trading Information Release subsystem for queries.
*   Enforce daily price rising/falling limits on instructions.
*   Remove outdated instructions that are not matched within the trading day.

**Key Users & Usage Scenarios**
Primary users are external subsystems: Trade Client Serve (submitting instructions), Security Account Management (recording trades), and Trading Information Release (querying data). A system maintainer/administrator role exists for troubleshooting and modifications. Typical scenarios include a client submitting a buy order, the system matching it with a sell order, recording the trade, and providing the result.

**Major External Interfaces**
The system interfaces with four external entities: Trade Client Serve (for instruction input and result output), Security Account Management (for saving trade data), Trading Information Release (for querying data), and Trading System Management (for administrative access). All communication occurs via defined programmatic interfaces.

**Key Non-functional Requirements**
The system must handle frequent instruction operations (fetch, deal, repeal) and be designed for heavy transaction loads. Maintainers must be able to diagnose and fix crashes, especially when system overhead exceeds capacity. The system must log instructions and trade results.

**Constraints, Assumptions & Dependencies**
The system is a subsystem dependent on the broader Stock Trading System architecture. It assumes correct input from the Trade Client Serve subsystem. A key constraint is that maintainers require specific skills in Java programming and socket communication for support.

**Priorities & Acceptance Approach**
Core functions (buy, sell, save trade info, query info) are essential for the first release. The cancel instruction function is a moderate priority for a second increment. Acceptance requires correct matching per defined principles, enforcement of trading limits, and proper interface communication with all connected subsystems.