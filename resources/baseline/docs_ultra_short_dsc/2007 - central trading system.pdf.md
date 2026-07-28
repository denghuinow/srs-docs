# Software Requirements Specification (SRS)
## Central Trading System (CTS)
### Version 1.0

**Prepared by:** [Author Name/Team]
**Date:** [Date]
**For:** Stock Trading System (STS) Project

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Central Trading System (CTS), a core subsystem of the Stock Trading System (STS). It is intended for use by the project stakeholders, including system architects, developers, testers, and maintainers, to ensure a common understanding of the system's capabilities and constraints.

### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Priority:** `[Essential]`, `[Moderate]`, `[Future]` as defined in Section 8.
*   **Keywords:** `MUST`, `SHALL`, `SHOULD`, `WILL`, `MAY` are used as defined in IETF RFC 2119.

### 1.3 Project Scope
The CTS is the subsystem responsible for the core matching and execution of stock trades. It receives, validates, and matches buy and sell instructions according to defined business rules, executes trades, and interfaces with other subsystems to persist and disseminate trading data.

**In-Scope:**
*   Receipt and validation of trading instructions (buy, sell, cancel).
*   Matching of buy and sell instructions based on price-time priority.
*   Execution of matched trades.
*   Management of pending instructions (cancellation, daily expiry).
*   Enforcement of daily price fluctuation limits.
*   Persistence of trade data to the Security Account Management subsystem.
*   Provision of trading data to the Trading Information Release subsystem.
*   Logging of all instruction and trade activity.
*   Administrative interfaces for system oversight.

**Out-of-Scope:**
*   User account management or authentication.
*   Client-facing user interface (UI) presentation.
*   Final financial settlement of trades.
*   Network message promulgation to end-clients.
*   Management of the broader STS ecosystem.

### 1.4 References
*   STS High-Level Architecture Document
*   Trade Client Serve Subsystem Interface Specification
*   Security Account Management Subsystem Interface Specification

## 2. Overall Description

### 2.1 Product Perspective
The CTS is one of six interdependent subsystems within the Stock Trading System (STS). It acts as the central matching engine. Its position and interfaces are depicted below:

```
[Trade Client Serve] --> (Instructions & Cancels) --> [CENTRAL TRADING SYSTEM] --> (Trade Results) --> [Network Message Promulgating]
         |                                                              |
         |                                                              |--> (Trade Data) --> [Trading Information Release]
         |                                                              |
         |                                                              |--> (Persisted Trade Data) --> [Security Account Management]
         |                                                              |
         |<------------------------ (Administrative Cmds/Queries) ------|--> [Trading System Management]
```

### 2.2 User Classes and Characteristics
*   **External Subsystems (Primary "Users"):**
    *   **Trade Client Serve (TCS):** Submits all trading instructions (buy, sell, cancel) and receives execution results. High-frequency, programmatic interaction.
    *   **Security Account Management (SAM):** Receives and records immutable data for completed trades. Interaction occurs upon each successful trade execution.
    *   **Trading Information Release (TIR):** Queries the CTS for trading data (e.g., order book status, recent trades). Read-only, potentially high-volume queries.
    *   **Trading System Management (TSM):** Provides administrative oversight, including system health checks, manual overrides (in emergencies), and configuration updates. Low-frequency, privileged access.
*   **System Maintainer/Administrator:** A human role responsible for monitoring logs, diagnosing system crashes, performing deployments, and applying fixes. Requires expertise in Java and socket-based communication.

### 2.3 Operating Environment
*   **Software:** JVM-based environment (e.g., Java 11+). Expected to run within a Linux server environment.
*   **Hardware:** Must be deployable on scalable server infrastructure to support heavy transaction loads.
*   **Integration:** All external interactions are via defined programmatic interfaces (e.g., REST APIs, gRPC, or dedicated TCP sockets).

### 2.4 Design and Implementation Constraints
1.  The system SHALL be implemented in Java.
2.  Communication with the Trade Client Serve subsystem SHALL utilize socket-based protocols.
3.  The system architecture MUST be a subsystem within the broader, predefined STS architecture and cannot operate as a standalone product.
4.  Maintainers assigned to the system MUST possess specific skills in Java and socket communication.

### 2.5 Assumptions and Dependencies
*   **Assumption:** The Trade Client Serve subsystem will provide correctly formatted and semantically valid instructions.
*   **Assumption:** The Security Account Management and Trading Information Release subsystems will be available and responsive according to their service-level agreements (SLAs).
*   **Dependency:** The CTS is wholly dependent on the existence and correct operation of the interfacing STS subsystems (TCS, SAM, TIR, TSM).
*   **Dependency:** The definition of "daily price rising/falling limits" and "price-time priority rules" will be provided by a separate business rules document.

## 3. System Features and Requirements

### 3.1 Instruction Processing
#### 3.1.1 Receive and Validate Instructions
*   **FR-001:** [Essential] The system SHALL accept new trading instructions (buy or sell) from the Trade Client Serve subsystem via its defined programmatic interface.
*   **FR-002:** [Essential] The system SHALL validate all incoming instructions for basic integrity (e.g., required fields present, stock symbol valid, quantity > 0, price > 0).
*   **FR-003:** [Essential] The system SHALL enforce daily price rising/falling limits on all buy and sell instructions, rejecting any instruction that violates these limits.
*   **FR-004:** [Essential] Upon successful validation, the instruction SHALL be placed in the appropriate pending order book (buy or sell) for the specified stock.

#### 3.1.2 Cancel Instruction
*   **FR-005:** [Moderate] The system SHALL accept cancel instructions from the Trade Client Serve subsystem to repeal a pending buy or sell instruction.
*   **FR-006:** [Moderate] The system SHALL validate that the instruction to be canceled exists, is pending, and belongs to the originating client.
*   **FR-007:** [Moderate] Upon successful validation, the system SHALL remove the pending instruction from its order book.

### 3.2 Trade Matching and Execution
#### 3.2.1 Matching Algorithm
*   **FR-008:** [Essential] The system SHALL continuously attempt to match pending buy and sell instructions for the same stock.
*   **FR-009:** [Essential] Matching SHALL follow **price-time priority**:
    *   **Price Priority:** For a given stock, the highest buy price is matched with the lowest sell price.
    *   **Time Priority:** When prices are equal, the instruction received first (earliest timestamp) has priority.
*   **FR-010:** [Essential] A trade SHALL be executed immediately when a match is found. The trade price SHALL be the price of the earlier order (the one already in the book).

#### 3.2.2 Trade Finalization
*   **FR-011:** [Essential] Upon trade execution, the system SHALL generate an immutable trade record containing: Trade ID, Stock Symbol, Execution Price, Quantity, Buyer ID, Seller ID, and Timestamp.
*   **FR-012:** [Essential] The system SHALL transmit the complete trade record to the Security Account Management subsystem via its defined interface for permanent recording.
*   **FR-013:** [Essential] The system SHALL notify the Trade Client Serve subsystem of the execution result for both the buyer and seller.

### 3.3 Data Management and Provision
#### 3.3.1 Order Book Management
*   **FR-014:** [Essential] The system SHALL maintain pending buy and sell order books per stock symbol.
*   **FR-015:** [Essential] The system SHALL automatically remove any pending instruction that has not been matched or canceled by the end of the trading day.

#### 3.3.2 Data Query Interface
*   **FR-016:** [Essential] The system SHALL provide a programmatic interface for the Trading Information Release subsystem to query trading data.
*   **FR-017:** [Essential] Queryable data SHALL include, at a minimum: the current state of the order book (aggregated price levels) for a given stock and a list of recently executed trades.

### 3.4 Administrative Functions
#### 3.4.1 System Oversight
*   **FR-018:** [Essential] The system SHALL provide a secure interface for the Trading System Management subsystem to perform health checks and retrieve key performance metrics (e.g., instruction volume, match rate).
*   **FR-019:** [Essential] The system SHALL log all significant events, including: receipt of instructions, validation failures, trade executions, cancellations, and system errors.

## 4. External Interface Requirements

### 4.1 Software Interfaces
*   **Interface with Trade Client Serve (TCS):** Bidirectional socket-based interface. Protocol definition required (e.g., message framing, serialization format - JSON/Protobuf).
*   **Interface with Security Account Management (SAM):** Likely synchronous REST API or RPC call to `POST /api/trades`.
*   **Interface with Trading Information Release (TIR):** Likely REST API for queries (e.g., `GET /api/orderbook/{symbol}`, `GET /api/trades/recent`).
*   **Interface with Trading System Management (TSM):** Secure REST API or dedicated admin port for monitoring and control commands.

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
*   **NFR-001:** The system MUST be designed to handle **heavy transaction loads**, typical of a stock exchange matching engine.
*   **NFR-002:** The core matching cycle (fetch from order book, match, execute) for a single trade MUST have a 99th percentile latency of < 10 milliseconds under expected peak load.
*   **NFR-003:** The system MUST support the frequent processing of instruction operations (fetch/validate, deal/match, repeal/cancel) concurrently.

### 5.2 Reliability & Maintainability
*   **NFR-004:** The system MUST log sufficient detail (instruction ID, timestamp, state changes) to allow maintainers to diagnose the cause of any system crash.
*   **NFR-005:** The system architecture MUST allow for the diagnosis and remediation of issues arising when system overhead (e.g., memory, CPU) exceeds capacity.
*   **NFR-006:** Logs of all instructions and trade results MUST be persisted to durable storage and retained for a minimum of 90 days for auditing and troubleshooting.

### 5.3 Availability
*   **NFR-007:** The system SHALL target 99.9% availability during scheduled trading hours.

## 6. Other Requirements

### 6.1 Data Retention
*   Completed trade records are persisted externally to the SAM subsystem. Internal CTS logs and transient order book data are subject to separate retention policies defined in operational runbooks.

## 7. Appendices

### 7.1 Glossary
*   **Instruction:** A client request to buy or sell a quantity of a specific stock at a specified price.
*   **Order Book:** A real-time, dynamic list of pending buy and sell instructions for a security, organized by price and time.
*   **Price-Time Priority:** The primary rule for matching orders, where the best price is matched first, and orders at the same price are matched in the sequence they were received.
*   **STS:** Stock Trading System, the overarching platform.
*   **CTS:** Central Trading System, the subsystem described in this document.

## 8. Prioritization and Release Planning

### 8.1 Requirement Priorities
*   **Essential (Release 1.0):** FR-001, FR-002, FR-003, FR-004, FR-008, FR-009, FR-010, FR-011, FR-012, FR-013, FR-014, FR-015, FR-016, FR-017, FR-018, FR-019, NFR-001, NFR-002, NFR-003, NFR-004, NFR-006, NFR-007.
*   **Moderate (Release 2.0 Increment):** FR-005, FR-006, FR-007.
*   **Future/To Be Defined:** Additional administrative features, enhanced monitoring, more complex order types.

### 8.2 Acceptance Approach
Acceptance of the CTS for Release 1.0 requires verification of the following:
1.  Correct implementation of the price-time priority matching algorithm.
2.  Consistent enforcement of daily price rising/falling limits.
3.  Successful end-to-end integration and data flow with all four connected subsystems (TCS, SAM, TIR, TSM).
4.  Performance metrics meeting the defined non-functional requirements under simulated load.
5.  Comprehensive logging is in place as specified.