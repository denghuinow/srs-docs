# Software Requirements Specification (SRS)
## For the Central Trading System (CTS)
**Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### **1. Introduction**

#### **1.1 Purpose**
This document defines the functional and non-functional requirements for the Central Trading System (CTS), a core subsystem of the Stock Trading System (STS). It is intended for use by the project stakeholders, development team, testers, and system architects to guide the design, implementation, and verification of the CTS.

#### **1.2 Document Conventions**
*   Requirements are uniquely identified using the format `CTS-FR-XXX` for functional requirements and `CTS-NFR-XXX` for non-functional requirements.
*   Keywords such as **MUST**, **SHALL**, **SHOULD**, **MAY**, **MUST NOT**, **SHALL NOT** are used as defined in IETF RFC 2119.
*   All monetary values and quantities are represented as integers or decimals with appropriate precision.

#### **1.3 Project Scope**
The CTS is responsible for the real-time processing, validation, matching, and execution of stock trading instructions. It acts as the central engine, receiving orders from the user interface, matching buy and sell orders based on price-time priority, and disseminating trade results to other subsystems for account settlement and information publishing.

**In-Scope Elements:**
*   Processing of buy, sell, and cancel instructions.
*   Validation of instructions against business and regulatory rules.
*   Order matching based on price-time priority.
*   Generation and logging of trade confirmations.
*   Provision of query interfaces for trade data.
*   System event and error logging.

**Out-of-Scope Elements:**
*   User authentication, authorization, and session management.
*   Management of user cash or securities holdings (performed by the Security Account Management subsystem).
*   The graphical user interface presented to the end-user.
*   Long-term data warehousing and archival.
*   Public-facing market data feeds or websites.

#### **1.4 References**
*   STS System Architecture Overview
*   IETF RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels
*   Financial Trading Principles & Price Limit Regulations

---

### **2. Overall Description**

#### **2.1 Product Perspective**
The CTS is a server-side component within the larger STS ecosystem. It interfaces with several other subsystems via defined APIs (socket-based). The diagram below illustrates its context:

```
[Transaction User Interface] --> (Submit Order/Cancel) --> [CENTRAL TRADING SYSTEM] --> (Trade Confirmations) --> [Security Account Management]
                                                                      |
                                                                      |--> (Trade Data Queries/Results) --> [Trading Information Release]
                                                                      |
                                                                      |--> (Monitoring/Management) <--> [Trading System Management]
```
*   **Transaction User Interface:** Primary source of trading instructions.
*   **Security Account Management:** Primary consumer of executed trade data for settlement.
*   **Trading Information Release:** Consumer of trade data for analytics and reporting.
*   **Trading System Management:** Provides operational control and monitoring.

#### **2.2 Product Functions**
The core functions of the CTS are:
1.  **Instruction Ingestion:** Accept incoming buy, sell, and cancel instructions.
2.  **Instruction Validation:** Validate instructions for format, price limits, and basic integrity.
3.  **Order Book Management:** Maintain pending buy and sell orders for each stock symbol.
4.  **Order Matching:** Apply price-time priority logic to match compatible buy and sell orders, generating trades.
5.  **Trade Execution & Notification:** Formally execute matched trades and notify relevant subsystems.
6.  **Cancellation Processing:** Locate and remove pending orders based on cancel requests.
7.  **Data Provision:** Serve historical and real-time trade data via queries.
8.  **System Maintenance:** Log operations, handle exceptions, and support end-of-day processing.

#### **2.3 User Classes and Characteristics**
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **Transaction UI (System)** | Subsystem submitting user orders. | High-frequency, machine-driven, requires low-latency acknowledgment. |
| **Security Account Mgmt (System)** | Subsystem consuming trade confirmations. | Requires guaranteed, in-order delivery of trade data for accurate settlement. |
| **Trading Info Release (System)** | Subsystem querying for market data. | Periodic or on-demand queries, requires aggregated and filtered data. |
| **System Maintainer (Human)** | IT personnel managing the CTS. | Technical expertise, requires detailed logs and operational controls. |

#### **2.4 Operating Environment**
*   **Software:** Java Runtime Environment (JRE) 11 or later. Host operating system (Linux/Windows Server).
*   **Hardware:** Enterprise-grade server with sufficient CPU, memory, and network I/O to handle projected peak load.
*   **Network:** Reliable TCP/IP network supporting socket communication between STS subsystems.

#### **2.5 Design and Implementation Constraints**
1.  **CTS-FR-001:** The system **SHALL** be implemented in Java.
2.  **CTS-FR-002:** All inter-subsystem communication **MUST** be conducted via TCP sockets using predefined message protocols.
3.  **CTS-FR-003:** The matching engine **MUST** implement price-time priority (best price first; at same price, earliest order first).
4.  **CTS-FR-004:** The system **MUST** validate all order prices against the daily price fluctuation limit (e.g., ±10% from previous day's closing price).
5.  **CTS-FR-005:** All unmatched orders **MUST** be automatically purged at the official end of the trading day.

#### **2.6 Assumptions and Dependencies**
*   It is assumed that upstream subsystems (Transaction UI) will perform initial data sanity checks before sending instructions.
*   The CTS depends on the Trading System Management subsystem to provide a definitive signal for the start and end of the trading day.
*   Network connectivity between subsystems is assumed to be stable and secure within the STS deployment environment.

---

### **3. System Features and Requirements**

#### **3.1 Feature: Instruction Processing & Validation**
**Description:** The system shall accept and validate trading instructions.

**Requirements:**
*   **CTS-FR-010:** The system **SHALL** accept `BUY` and `SELL` instructions containing at minimum: Unique Instruction ID, Timestamp, Stock Symbol, Order Type (Market/Limit), Quantity, Price (for Limit orders), and User/Account Reference.
*   **CTS-FR-011:** The system **SHALL** accept `CANCEL` instructions containing the Unique Instruction ID of the order to be canceled.
*   **CTS-FR-012:** The system **SHALL** validate the price of a Limit order against the daily price fluctuation limit for the specified stock. Orders violating the limit **SHALL** be rejected.
*   **CTS-FR-013:** The system **SHALL** validate that the Instruction ID is unique and not previously processed. Duplicate IDs **SHALL** be rejected.
*   **CTS-FR-014:** The system **SHALL** send an immediate acknowledgment (ACK) or error message back to the Transaction UI subsystem upon receipt and validation of any instruction.

#### **3.2 Feature: Order Matching & Trade Execution**
**Description:** The system shall match valid buy and sell orders and generate trades.

**Requirements:**
*   **CTS-FR-020:** The system **SHALL** maintain separate order books for each stock symbol, segregating buy orders and sell orders.
*   **CTS-FR-021:** Buy orders **SHALL** be ranked in the order book first by highest price (descending), then by earliest timestamp.
*   **CTS-FR-022:** Sell orders **SHALL** be ranked in the order book first by lowest price (ascending), then by earliest timestamp.
*   **CTS-FR-023:** A trade **SHALL** be executed when a buy order price is greater than or equal to a sell order price.
*   **CTS-FR-024:** The execution price **SHALL** be the price of the order that was first entered into the book (price-time priority).
*   **CTS-FR-025:** Upon matching, the system **SHALL** generate a trade confirmation containing: Trade ID, Execution Timestamp, Stock Symbol, Execution Price, Execution Quantity, and the IDs of the matched buy and sell instructions.
*   **CTS-FR-026:** The system **SHALL** immediately transmit the trade confirmation to the Security Account Management subsystem.

#### **3.3 Feature: Cancel Request Processing**
**Description:** The system shall process requests to cancel pending orders.

**Requirements:**
*   **CTS-FR-030:** Upon receiving a valid `CANCEL` instruction, the system **SHALL** locate the corresponding pending order in the relevant order book.
*   **CTS-FR-031:** If the order is found and is still pending (not partially or fully executed), it **SHALL** be removed from the order book.
*   **CTS-FR-032:** The system **SHALL** send a confirmation message (success/failure) back to the Transaction UI subsystem indicating the result of the cancellation request.

#### **3.4 Feature: Trade Data Query Interface**
**Description:** The system shall provide an interface for querying trade information.

**Requirements:**
*   **CTS-FR-040:** The system **SHALL** provide a socket-based query interface for the Trading Information Release subsystem.
*   **CTS-FR-041:** The system **SHALL** support queries for trades within a specified time range.
*   **CTS-FR-042:** The system **SHALL** support queries for trades of a specific stock symbol.
*   **CTS-FR-043:** Query results **SHALL** be returned in a structured, machine-readable format (e.g., JSON, XML).

#### **3.5 Feature: System Logging & Management**
**Description:** The system shall log its activities and support operational management.

**Requirements:**
*   **CTS-FR-050:** The system **SHALL** log all system events (startup, shutdown, end-of-day processing) to a persistent log file.
*   **CTS-FR-051:** The system **SHALL** log all errors and exceptions (e.g., validation failures, communication errors) with sufficient detail for diagnosis (timestamp, error code, description, relevant instruction ID).
*   **CTS-FR-052:** The system **SHALL** expose a basic management interface (e.g., via a specific port or command) to accept a "Market Close" signal from the Trading System Management subsystem, triggering the purge of all unmatched orders.

---

### **4. External Interface Requirements**

#### **4.1 User Interfaces**
Not applicable. The end-user interface is out of scope. System-to-system interfaces are defined below.

#### **4.2 Hardware Interfaces**
None specified beyond standard server hardware.

#### **4.3 Software Interfaces**
*   **Interface with Transaction UI:** Bidirectional socket connection. Defined message protocol for `BUY`, `SELL`, `CANCEL`, `ACK`, `ERROR`, and `CANCEL_RESPONSE` messages.
*   **Interface with Security Account Management:** Unidirectional (CTS -> SAM) socket connection. Protocol for `TRADE_CONFIRMATION` messages.
*   **Interface with Trading Information Release:** Bidirectional socket connection. Protocol for `QUERY` and `QUERY_RESULT` messages.
*   **Interface with Trading System Management:** Bidirectional socket connection. Protocol for `HEARTBEAT`, `MARKET_OPEN`, `MARKET_CLOSE`, and `STATUS` messages.

#### **4.4 Communications Interfaces**
All external communications **SHALL** use TCP/IP sockets to ensure reliable, ordered, and error-checked delivery of data streams.

---

### **5. Non-Functional Requirements**

#### **5.1 Performance Requirements**
*   **CTS-NFR-001:** The system **SHALL** process 99% of incoming instructions (validation and book entry) within 100 milliseconds under normal load.
*   **CTS-NFR-002:** The system **SHALL** generate and dispatch a trade confirmation within 50 milliseconds of a match occurring.
*   **CTS-NFR-003:** The system **MUST** be capable of sustaining a peak load of 1,000 instructions per second.

#### **5.2 Safety Requirements**
*   **CTS-NFR-010:** No trade **SHALL** be executed at a price outside the daily permissible price limit.
*   **CTS-NFR-011:** The system **MUST** guarantee that no instruction is executed more than once (idempotency for duplicate submissions).

#### **5.3 Security Requirements**
*   **CTS-NFR-020:** All inter-subsystem socket connections **SHOULD** be established within a trusted, isolated network segment.
*   **CTS-NFR-021:** The system **SHALL** validate the source of incoming messages to a configurable level (e.g., IP whitelist). *(Note: Detailed security protocols are an Undecided Issue)*.

#### **5.4 Software Quality Attributes**
*   **Availability (CTS-NFR-030):** The system **SHALL** achieve 99.9% operational availability during scheduled trading hours.
*   **Reliability (CTS-NFR-031):** The system **SHALL** have a Mean Time Between Failures (MTBF) of not less than 720 hours.
*   **Maintainability (CTS-NFR-032):** Log files **SHALL** be structured and parsable to facilitate automated monitoring and troubleshooting.

---

### **6. Appendices**

#### **6.1 Undecided Issues & TBD**
1.  **Trade Confirmation to UI:** Decision pending on whether trade success/failure is communicated to the user interface in real-time or via end-of-day batch.
2.  **Logging Strategy:** The specific log format (e.g., JSON, Syslog), rotation policy, and retention period need to be defined.
3.  **Query Frequency:** The agreed-upon query interval or trigger for the Trading Information Release subsystem must be established to size the query interface appropriately.
4.  **Security Protocols:** The need for encryption (TLS), authentication (certificates), or message signing must be formally assessed and specified.
5.  **Cancel Request Status:** Requirement `CTS-FR-032` provides a status return. This decision is recorded as finalized.

#### **6.2 Glossary**
| Term | Definition |
| :--- | :--- |
| **Instruction** | A request to perform an action (Buy, Sell, Cancel). |
| **Order** | A validated Buy or Sell instruction residing in the order book. |
| **Order Book** | The electronic list of pending buy and sell orders for a security. |
| **Price-Time Priority** | A matching rule where the best price executes first; identical prices are executed in chronological order. |
| **Trade** | The completed transaction resulting from a matched buy and sell order. |
| **STS** | Stock Trading System, the overarching system. |