# Software Requirements Specification (SRS)
## Stock Trading Matching Engine Subsystem

**Document Version:** 1.0
**Date:** [Current Date]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Stock Trading Matching Engine Subsystem. This document is intended for use by the project stakeholders, including software developers, testers, project managers, and system architects, to ensure a common understanding of the system to be developed.

#### 1.2 Scope
The system is a critical backend subsystem responsible for the automated matching of stock trade instructions (orders). Its core purpose is to match buy and sell instructions based on predefined price-time priority rules, manage the lifecycle of these instructions (including cancellation), and provide controlled interfaces for trade information. The system operates within a larger trading platform but functions as a discrete, high-performance engine.

**In-Scope:**
*   Real-time matching of buy/sell orders.
*   Order validation against price limits.
*   Order cancellation processing.
*   Provision of query interfaces for trade and order book data.
*   End-of-day cleanup procedures.
*   System performance and reliability under high load.

**Out-of-Scope:**
*   User interface for traders (front-end).
*   User authentication and authorization.
*   Payment settlement and clearing processes.
*   Risk management beyond basic price limits.
*   Market data feeds (consumes data via defined interfaces).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **Order/Instruction:** A request to buy or sell a specific quantity of a stock at a specified price or better.
*   **Matching Engine:** The core component that pairs buy and sell orders.
*   **Price-Time Priority:** The primary matching rule where the best price is prioritized first, and at equal prices, the earliest order is prioritized.
*   **Order Book:** The electronic list of buy and sell orders for a specific security, maintained by price and time.
*   **Limit Order:** An order to buy or sell at a specified price or better.
*   **Price Limit:** The maximum allowable price movement (rise/fall) for an order relative to a reference price (e.g., previous close).
*   **SLA:** Service Level Agreement.

#### 1.4 References
*   [PRD-001] Project Charter for Trading Platform
*   [DOC-010] System Architecture Overview

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific functional requirements. Section 4 outlines the non-functional requirements, including performance, safety, and constraints.

### 2. Overall Description

#### 2.1 Product Perspective
The Matching Engine is a server-side subsystem within a larger distributed trading platform. It interacts with:
*   **Order Gateway:** Receives new and cancel instructions.
*   **Market Data Engine:** Receives reference prices for validation.
*   **Trade Reporting Interface:** Publishes matched trade details.
*   **Query Service Interface:** Responds to requests for order book and trade data.
*   **Settlement System:** (Downstream) receives confirmed trades.

#### 2.2 Product Functions
The high-level functions of the system are:
1.  **Order Validation:** Validate incoming orders against business rules (e.g., price limits, format).
2.  **Order Management:** Insert, modify (via cancel/replace), and remove orders from the order book.
3.  **Order Matching:** Continuously attempt to match buy and sell orders based on price-time priority.
4.  **Trade Generation:** Create an immutable trade record when a match occurs.
5.  **Data Dissemination:** Provide real-time access to order book states and trade history via APIs.
6.  **System Maintenance:** Perform end-of-day clearing and recovery procedures.

#### 2.3 User Characteristics
The primary "users" are system components and operational personnel:
*   **External Systems (Automated Clients):** Submit orders at high frequency with low latency expectations.
*   **Compliance Officers:** Configure and monitor price limit parameters.
*   **System Administrators:** Monitor system health, perform start-of-day and end-of-day procedures.

#### 2.4 Constraints
1.  **Performance Constraint:** Must be designed to handle peak loads of **[TBD - e.g., 100,000+]** orders per second per instrument with sub-millisecond latency for matching.
2.  **Business Rule Constraint:** Must reject any buy (sell) order priced above (below) the defined static or dynamic price rise/fall limit.
3.  **Data Lifecycle Constraint:** All unfulfilled (resting) orders must be automatically removed from the system at the defined end of the trading day.
4.  **Technical Constraint:** Must prevent system crashes or significant performance degradation due to memory leaks, uncontrolled queue growth, or garbage collection overhead.

#### 2.5 Assumptions and Dependencies
*   Assumes incoming orders are pre-validated for basic format and compliance by the Order Gateway.
*   Depends on the Market Data Engine to provide accurate reference prices for limit validation.
*   Assumes a reliable messaging infrastructure (e.g., Kafka, Aeron) for inter-system communication.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Order Processing
*   **FR-OP-01: Order Reception**
    *   The system shall accept new order instructions via a defined API from the Order Gateway.
*   **FR-OP-02: Price Limit Validation**
    *   The system shall reject any new order where the limit price exceeds the configured price rise/fall limit relative to the last closing price or a dynamic reference price. A rejection message with reason code `PRICE_LIMIT_VIOLATION` shall be sent back.
*   **FR-OP-03: Order Book Entry**
    *   Upon successful validation, the system shall insert the order into the appropriate price level in the central limit order book, maintaining time priority within the same price level.

##### 3.1.2 Order Matching
*   **FR-MT-01: Price-Time Priority Matching**
    *   The system shall match incoming sell (buy) orders against the best-priced existing buy (sell) orders first.
    *   At the same price level, the system shall match against the oldest resting order first (FIFO).
*   **FR-MT-02: Trade Execution**
    *   Upon a successful match, the system shall generate a unique, immutable trade record containing Trade ID, Symbol, Price, Quantity, Buy Order ID, Sell Order ID, and Timestamp.
    *   The system shall update the quantities of the matched orders, removing them from the book if fully filled.
*   **FR-MT-03: Partial Fills**
    *   The system shall support partial fills. An order shall remain in the book with its remaining quantity if only partially matched.

##### 3.1.3 Order Management
*   **FR-OM-01: Order Cancellation**
    *   The system shall accept order cancellation requests via a defined API.
    *   If the order is still resting in the book, it shall be removed immediately, and a cancellation confirmation shall be sent.
*   **FR-OM-02: End-of-Day Clear-Out**
    *   At a pre-configured time marking the end of the trading day, the system shall automatically cancel and remove all unfulfilled orders from all order books. A summary report of cleared orders shall be generated.

##### 3.1.4 Information Services
*   **FR-IS-01: Trade Publication**
    *   The system shall publish a real-time stream of all executed trade records to the Trade Reporting Interface.
*   **FR-IS-02: Order Book Query**
    *   The system shall provide a query interface (e.g., REST/gRPC) to return the current state of the order book for a specified symbol, including top N price levels for bids and asks.
*   **FR-IS-03: Order Status Query**
    *   The system shall provide a query interface to return the current status (e.g., resting, partially filled, filled, cancelled) and fill history of a specific order by its unique ID.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements
*   **PER-01: Latency**
    *   The 99th percentile latency for processing an order (from receipt to matching/trade publication or book entry) shall be less than **1 millisecond** under normal load.
*   **PER-02: Throughput**
    *   The system shall sustain a steady-state throughput of **50,000 orders per second** and handle burst rates of **100,000 orders per second** for periods of up to 5 minutes.
*   **PER-03: Concurrent Connections**
    *   The system shall support connections from up to **50** concurrent external system clients.

##### 3.2.2 Reliability & Availability
*   **REL-01: Availability**
    *   The system shall have an availability SLA of **99.95%** during trading hours.
*   **REL-02: Fault Tolerance**
    *   The system shall be designed to prevent a single order or a burst of malformed data from causing a crash or significant performance impact to other orders.

##### 3.2.3 Safety & Security
*   **SEC-01: Data Integrity**
    *   No trade shall be lost once generated. The system must guarantee at-least-once delivery of trade records to the reporting interface.
*   **SEC-02: Input Validation**
    *   All input from interfaces must be sanitized and validated to prevent injection attacks or malformed data from disrupting core logic.

##### 3.2.4 Design Constraints
*   **CON-01: Overhead Management**
    *   The system shall be implemented in a memory-safe language (e.g., Java, C#, Go, Rust) or with rigorous manual memory management (C++) to prevent memory leaks.
    *   Data structures (e.g., order books) shall be optimized for lock-free or minimal-lock concurrency to reduce overhead.

### 4. Appendices

#### Appendix A: Data Formats (Examples)
```json
// New Order Instruction
{
  "messageType": "NEW_ORDER",
  "orderId": "ORD-20231027-00001",
  "symbol": "AAPL",
  "side": "BUY",
  "orderType": "LIMIT",
  "price": 175.50,
  "quantity": 100,
  "timestamp": "2023-10-27T09:30:00.123Z"
}

// Trade Report
{
  "tradeId": "TRD-20231027-0054321",
  "symbol": "AAPL",
  "price": 175.50,
  "quantity": 100,
  "buyOrderId": "ORD-20231027-00001",
  "sellOrderId": "ORD-20231027-00002",
  "executionTime": "2023-10-27T09:30:00.456Z"
}
```

#### Appendix B: Price Limit Calculation
The price limit (`L`) shall be configurable per symbol. For a given reference price (`R`), typically the previous day's close:
*   Valid Buy Order Price Range: `<= R * (1 + L)`
*   Valid Sell Order Price Range: `>= R * (1 - L)`
Where `L` is the decimal equivalent of the percentage limit (e.g., 0.10 for 10%).