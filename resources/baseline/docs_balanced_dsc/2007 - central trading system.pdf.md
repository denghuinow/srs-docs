# Software Requirements Specification (SRS)
## Central Trading System (CTS)
### Version 1.0

**Document Status:** Draft  
**Date:** [Current Date]  
**Prepared for:** Stock Trading System (STS) Project  
**Prepared by:** [Author/Team Name]

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Central Trading System (CTS), a core subsystem of the Stock Trading System (STS). It is intended for use by project stakeholders, developers, testers, and maintainers to guide the design, implementation, and verification of the system.

### 1.2 Scope
The CTS is responsible for the real-time processing, matching, and execution of stock trading instructions (buy, sell, cancel, query). Its scope includes:
*   Receiving and validating instructions from the Transaction User Interface.
*   Matching buy and sell orders based on price-time priority and other business rules.
*   Managing instruction lifecycle (including cancellation).
*   Generating and dispatching trade results to the Security Account Management subsystem.
*   Providing trading data to the Trading Information Release subsystem.
*   Maintaining a comprehensive audit log of all system activities.

**Out of Scope:**
*   User authentication and authorization (assumed to be handled upstream).
*   The graphical user interface for end-users (handled by Transaction User Interface).
*   Long-term archival of data beyond operational logs.
*   Market data feeds for stock price discovery (assumed to be provided).

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **CTS** | Central Trading System |
| **STS** | Stock Trading System |
| **Instruction** | A request to perform an action (Buy, Sell, Cancel, Query). |
| **Order** | A Buy or Sell instruction that is active in the matching engine. |
| **Trade** | A completed transaction resulting from a matched buy and sell order. |
| **Price-Time Priority** | A matching rule where the best price is matched first, and at the same price, the earliest order is matched first. |
| **SAML** | Security Account Management (subsystem) |
| **TIR** | Trading Information Release (subsystem) |

### 1.4 References
*   STS Project Charter
*   System Architecture Overview Document
*   Interface Control Documents (for SAML, TIR, Transaction UI)

### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Overall Description - Provides context, user characteristics, and constraints.
*   **Section 3:** Specific Requirements - Details functional, interface, data, and non-functional requirements.
*   **Appendices:** Include supplementary information.

## 2. Overall Description

### 2.1 Product Perspective
The CTS is a server-side subsystem within the larger STS ecosystem. It acts as the "matching engine," interfacing with several other subsystems as depicted in the context diagram below.

```
[Transaction User Interface] --> (Submit Instructions) --> [CTS]
                                                          |  ^
                                 (Query Data)             |  | (Return Results/Status)
                                                          v  |
[Trading Info Release] <--------------------------------> [CTS]
                                                          |
                                 (Push Trade Results)     |
                                                          v
[Security Account Management] <------------------------- [CTS]
                                                          |
                                 (Management & Oversight) |
                                                          v
[Trading System Management] <--------------------------> [CTS]
```

### 2.2 User Characteristics
| Actor | Description | Technical Skill |
| :--- | :--- | :--- |
| **Transaction User Interface** | An external subsystem representing the client-facing application. Submits instructions on behalf of end-users. | System-to-system integration. |
| **Security Account Management (SAML)** | An external subsystem responsible for user portfolios and balances. Consumes trade results. | System-to-system integration. |
| **Trading Information Release (TIR)** | An external subsystem that queries for aggregated trading data for publication. | System-to-system integration. |
| **Trading System Management** | An external subsystem for administrative oversight and control of the STS. | System administration. |
| **Maintainer** | Technical personnel responsible for deploying, monitoring, and updating the CTS. | Proficient in Java, socket programming, and system diagnostics. |

### 2.3 Design and Implementation Constraints
1.  **Technology Stack:** The core matching engine must be implemented in Java to align with team expertise and existing STS components.
2.  **Communication Protocol:** Inter-subsystem communication for instruction submission and result dispatch must use sockets for high-performance, low-latency data transfer.
3.  **Database:** Must integrate with the enterprise relational database management system (RDBMS) designated for the STS project.
4.  **Concurrency:** The system must be designed for high concurrency, handling multiple simultaneous instructions efficiently and safely.

### 2.4 Assumptions and Dependencies
*   **A1:** The Transaction User Interface will perform initial data validation and formatting before submitting instructions to the CTS.
*   **A2:** The SAML subsystem will provide a reliable and available interface for receiving trade confirmations.
*   **A3:** Stock reference data (valid Stock IDs, price limits) is accessible to the CTS.
*   **D1:** Successful integration is dependent on stable API definitions from the Transaction User Interface, SAML, and TIR subsystems.
*   **D2:** Project timelines are dependent on the readiness of the shared database infrastructure.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 Instruction Processing
*   **FR1.1: Instruction Reception**
    *   The system shall accept new trading instructions (Buy, Sell, Cancel, Query) via a defined socket interface from the Transaction User Interface.
*   **FR1.2: Instruction Validation**
    *   The system shall validate all incoming instructions for:
        *   Format correctness.
        *   Valid User ID and Stock ID.
        *   For Buy/Sell: Positive quantity and price within daily permissible limits.
        *   For Cancel: Valid reference to an existing, pending instruction.
*   **FR1.3: Fund/Stock Pre-processing**
    *   Upon validation of a **Buy** instruction, the system shall place a hold (freeze) on the user's cash balance equivalent to `Quantity * Price`.
    *   Upon validation of a **Sell** instruction, the system shall place a hold on the user's portfolio for the specified quantity of the stock.
*   **FR1.4: Instruction Logging**
    *   The system shall create a persistent log entry for every instruction received, capturing its full state and a timestamp.

#### 3.1.2 Trade Matching
*   **FR2.1: Order Book Management**
    *   The system shall maintain separate Buy and Sell order books for each stock.
*   **FR2.2: Matching Algorithm**
    *   The system shall match Buy and Sell orders for the same stock based on **Price-Time Priority**.
    *   **Price Priority:** A Sell order with a lower asking price will match before one with a higher price. A Buy order with a higher bid price will match before one with a lower price.
    *   **Time Priority:** Among orders at the same price, the order received earliest shall be matched first.
*   **FR2.3: Trade Execution**
    *   Upon a successful match, the system shall:
        1.  Generate a unique Trade ID.
        2.  Record the trade details (buyer, seller, stock, quantity, executed price).
        3.  Update the status of the matched instructions to "Filled" or "Partially Filled".
        4.  Release unfrozen funds/securities for the unfilled portion of a partially filled order.

#### 3.1.3 Instruction Management
*   **FR3.1: Cancel Instruction Processing**
    *   The system shall process a Cancel instruction by attempting to remove the referenced pending order from its order book.
    *   If the order is successfully canceled, the system shall release any associated frozen funds or securities and update the instruction status to "Canceled".
*   **FR3.2: Query Instruction Processing**
    *   The system shall process a Query instruction by retrieving the current status and details (fills, remaining quantity) of the referenced instruction and returning it to the requester.

#### 3.1.4 Data Distribution
*   **FR4.1: Trade Result Dispatch**
    *   Upon trade execution, the system shall immediately push trade confirmation messages (Trade ID, details) to the Security Account Management (SAML) subsystem.
*   **FR4.2: Trading Data Provision**
    *   The system shall provide an interface for the Trading Information Release (TIR) subsystem to query for trading data (e.g., trades executed within a time range, volume per stock).

### 3.2 Interface Requirements

#### 3.2.1 External Hardware Interfaces
*   None specified. Assumes standard server hardware.

#### 3.2.2 External Software Interfaces
*   **ESI-1: Transaction User Interface API**
    *   **Protocol:** TCP Sockets
    *   **Direction:** Inbound
    *   **Purpose:** Receive trading instructions.
    *   **Data Format:** Structured binary or JSON message (TBD).
*   **ESI-2: Security Account Management (SAML) API**
    *   **Protocol:** TCP Sockets or Message Queue (TBD)
    *   **Direction:** Outbound
    *   **Purpose:** Push trade confirmation data.
*   **ESI-3: Trading Information Release (TIR) API**
    *   **Protocol:** TCP Sockets
    *   **Direction:** Bi-directional (Query/Response)
    *   **Purpose:** Respond to data queries.
*   **ESI-4: Database Interface**
    *   **Protocol:** JDBC
    *   **Purpose:** Persistent storage of Instructions, Trades, and Logs.

#### 3.2.3 Communication Protocols
*   Inter-subsystem communication shall primarily use TCP for reliable, ordered data delivery.

### 3.3 Data Requirements

#### 3.3.1 Logical Data Model
Key entities and their attributes:
*   **Instruction**
    *   `instruction_id` (PK), `user_id`, `stock_id`, `type` (ENUM: BUY, SELL, CANCEL, QUERY), `quantity`, `price`, `timestamp`, `status` (ENUM: PENDING, PARTIAL_FILL, FILLED, CANCELED, REJECTED), `original_instruction_id` (for Cancel/Query).
*   **Trade**
    *   `trade_id` (PK), `buy_instruction_id` (FK), `sell_instruction_id` (FK), `stock_id`, `quantity`, `executed_price`, `timestamp`.
*   **Log Entry**
    *   `log_id` (PK), `timestamp`, `instruction_id` (FK, nullable), `action` (e.g., "RECEIVED", "VALIDATED", "MATCHED", "CANCELED"), `result`, `error_code`.

#### 3.3.2 Data Persistence
*   All Instructions, Trades, and Log Entries must be persisted to a relational database before a transaction is considered complete.
*   In-memory order books shall be the source of truth for matching performance but must be recoverable from persistent logs.

### 3.4 Non-Functional Requirements

#### 3.4.1 Performance
*   **PER-1:** The 95th percentile of instruction processing latency (from receipt to result dispatch) shall be less than **10 milliseconds** under normal load.
*   **PER-2:** The system shall be capable of sustaining a peak load of **5,000 instructions per second**.

#### 3.4.2 Reliability & Availability
*   **REL-1:** The system shall achieve 99.9% operational availability during market hours.
*   **REL-2:** In the event of a process crash, the system shall be able to recover its last state (order books) from persistent logs with no data loss for acknowledged instructions.

#### 3.4.3 Maintainability
*   **MAIN-1:** The codebase shall be modular, with clear separation between matching logic, communication handlers, and data access layers.
*   **MAIN-2:** System configuration (e.g., ports, timeouts, limits) shall be externalized in property files.

#### 3.4.4 Accuracy
*   **ACC-1:** Trade matching shall be 100% accurate according to the price-time priority rule. This shall be verified by automated unit and integration tests.

#### 3.4.5 Auditability
*   **AUD-1:** Every state change for an instruction (creation, validation, match, cancel) must be recorded in an immutable log with a timestamp and initiating actor/process.

### 3.5 Security Requirements
*   **SEC-1:** All socket communications with external subsystems shall be over secure channels (e.g., within a protected VPN, or using TLS).
*   **SEC-2:** The system shall validate that the sender of a Cancel or Query instruction is authorized to act on the referenced instruction (e.g., same User ID).
*   **SEC-3:** System logs shall not contain sensitive user information (e.g., full account numbers) in plaintext.

---

## Appendix A: Open Issues / TBD
The following items require stakeholder resolution:
1.  **Trade Confirmation Batching:** Should confirmations be sent to the UI immediately per trade or batched?
2.  **Failure Communication:** Specification for how failed instructions (e.g., validation errors, unfilled orders) are communicated back to the end-user.
3.  **Exception Log Detail:** Required fields for the exception/error log (e.g., stack trace, severity level, component).
4.  **Security Deep Dive:** Specific encryption standards, certificate management, and intrusion detection requirements.
5.  **Cancel Status Return:** Should the success/failure status of a cancel request be synchronously returned to the Transaction UI?
6.  **TIR Polling Frequency:** Agreed-upon schedule or event-driven triggers for TIR data queries.

## Appendix B: Glossary of Business Rules
*   **Price-Time Priority:** Defined in FR2.2.
*   **Daily Price Limit:** A stock's price cannot rise or fall beyond a set percentage from its previous day's closing price within a single trading session. Instructions violating this limit must be rejected.
*   **Partial Fill:** An order may be filled in multiple transactions until its total quantity is met. The order remains active with a reduced remaining quantity.