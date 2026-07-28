# Detailed Summary: Central Trading System (CTS)

## Background and Scope
The Central Trading System (CTS) is a core subsystem within the broader Stock Trading System (STS), responsible for executing stock trades. Its primary function is to receive, analyze, and match buy/sell instructions from clients according to specific trading rules (price-time priority). It interfaces with other subsystems to manage accounts, release information, and support system management. Non-goals include direct user interaction (handled by the Transaction User Interface) and long-term archival of trade data.

## Stakeholders Matrix and Use Cases
*   **Transaction User Interface:** Primary actor; submits buy, sell, cancel, and query instructions from end-users to the CTS.
*   **Security Account Management:** Secondary actor; receives and saves confirmed trade information from the CTS to update user accounts.
*   **Trading Information Release:** Secondary actor; queries the CTS for trading data to be statistically analyzed and published.
*   **Trading System Management:** Secondary actor; monitors and manages the CTS, potentially accessing its information and logs.
*   **System Maintainer:** Responsible for the operation, troubleshooting, and enhancement of the CTS, requiring Java and socket programming skills.

**Main Scenarios:**
1.  **Buy Stock:** CTS receives a buy instruction, saves it, matches it with a corresponding sell order, executes the trade, and updates the instruction status.
2.  **Sell Stock:** CTS receives a sell instruction, saves it, matches it with a corresponding buy order, executes the trade, and updates the instruction status.
3.  **Cancel Trading Instruction:** CTS receives a cancel instruction and attempts to remove the corresponding pending buy/sell order from its matching queue.
4.  **Save Trade Information:** After a successful trade, CTS sends the trade details to the Security Account Management subsystem for persistence.
5.  **Query Trade Information:** CTS processes queries from the Trading Information Release subsystem and returns structured trading data.

**Exception Scenarios:**
1.  **Instruction Matching Failure:** No corresponding buy/sell order is found for a new trading instruction.
2.  **Invalid Instruction:** An instruction violates rules such as price rising/falling limits.
3.  **Cancel Failure:** The instruction to be canceled has already been executed or does not exist.
4.  **System Suspension:** All trading operations are temporarily halted.

## Business Process
**Main Process: Instruction Processing & Matching**
1.  **Trigger:** Receive a new instruction (buy/sell/cancel/query) from the Transaction User Interface.
2.  **Instruction Pretreatment:** Validate the instruction format and business rules (e.g., price limits). Freeze the buyer's funds if applicable and log the incoming instruction.
3.  **Instruction Routing:** Route the validated instruction to the appropriate manager module (Trade, Cancel, or Query).
4.  **Trade Instruction Handling (Key Branch):** For buy/sell instructions, add to the order book and attempt to match based on price-time priority.
    *   **Match Found:** Execute trade, generate trade result, update order status to "filled" or "partially filled".
    *   **No Match:** Queue the instruction in the order book pending future matches.
5.  **Cancel Instruction Handling (Key Branch):** Locate the specified pending order in the order book.
    *   **Order Found & Cancelable:** Remove the order and update its status.
    *   **Order Not Found/Executed:** Reject the cancel request.
6.  **Result Generation:** Create a result message (trade confirmation, cancel acknowledgment, query response).
7.  **Output Dispatch:** Send results to relevant subsystems: trade confirmations to Security Account Management, market data to Trading Information Release, and status updates to the Transaction User Interface.
8.  **Logging:** Record the outcome of the instruction processing for audit and system management.

## Domain Model
Key entities managed by the CTS include:
*   **Instruction:** Core entity representing a user's intent. Fields: InstructionID (unique), UserID (required), StockID (required), Type (buy/sell/cancel/query, required), Quantity (required), Price (required for trades), Timestamp (required), Status (pending/matched/canceled/expired).
*   **Trade:** Represents a completed transaction. Fields: TradeID (unique), BuyInstructionID (reference), SellInstructionID (reference), StockID (required), Quantity (required), Price (required), ExecutionTimestamp (required).
*   **Order Book:** A logical collection of pending buy and sell instructions for a specific stock, used for matching.
*   **User Account (Reference):** Managed externally by Security Account Management; referenced by UserID for fund freezing and updates.
*   **Stock (Reference):** Managed externally; referenced by StockID, contains attributes like price limits.
*   **System Log:** Record of system activities and errors for auditing and maintenance.

## Interfaces and Integrations
1.  **Transaction User Interface (Inbound):** Receives all client instructions. Input: Structured instruction message (UserID, StockID, Type, Quantity, Price). Output: Instruction acknowledgment and final status. SLA: Low latency for instruction acceptance.
2.  **Security Account Management (Outbound):** Sends confirmed trade details. Input: Trade execution message. Output: Acknowledgment of receipt. SLA: High reliability to ensure financial consistency.
3.  **Trading Information Release (Bidirectional):** Responds to data queries. Input: Query request (stock/user filters). Output: Structured dataset of trades/orders. SLA: Support for high-frequency query bursts.
4.  **Trading System Management (Bidirectional):** Provides system monitoring and control access. Input: Management commands, log queries. Output: System status, logs. SLA: Secure and authenticated access.

## Acceptance Criteria
*   **Capability: Execute a Buy Trade**
    *   Given a valid buy instruction is received and a matching sell order exists in the book, when the matching engine runs, then a trade is executed, the order statuses are updated, and a confirmation is sent to the Security Account Management.
    *   Given a buy instruction with a price above the daily rising limit, when the instruction is preprocessed, then it is rejected and an error is returned to the user interface.
*   **Capability: Cancel an Order**
    *   Given a cancel instruction for a pending buy order, when processed, then the order is removed from the order book and a cancel confirmation is sent.
    *   Given a cancel instruction for an already executed trade, when processed, then the cancel is rejected and an error message is returned.

## Non-Functional Metrics
*   **Performance:** Must process and match instructions with sub-second latency under peak load. System must handle a specified high volume of concurrent instructions.
*   **Reliability:** Achieve 99.9% uptime during trading hours. Ensure no data loss in trade execution through transactional integrity.
*   **Security:** All external interfaces must be authenticated. Sensitive financial data in transit must be encrypted.
*   **Compliance:** Trading matching logic must strictly adhere to price-time priority rules as per financial regulations.
*   **Observability:** All system states and instruction flows must be logged for audit trails. Key performance and error metrics must be exposed for monitoring.

## Milestones and Release Strategy
1.  Core Instruction Pretreatment and Validation.
2.  Basic Trade Matching Engine (Buy/Sell) with order book.
3.  Integration with Security Account Management for trade persistence.
4.  Cancel Instruction functionality.
5.  Query Interface for Trading Information Release.
6.  System Management and Monitoring Console.

## Risk List and Mitigation Strategies
1.  **Risk:** High transaction volume leading to system overload and crash.
    *   **Mitigation:** Implement robust queue management, horizontal scaling strategies, and rigorous load testing.
2.  **Risk:** Inconsistency between CTS trade state and external account balances.
    *   **Mitigation:** Design idempotent and reliable messaging patterns with the Security Account Management system; implement reconciliation processes.
3.  **Risk:** Incorrect trade matching logic leading to regulatory non-compliance.
    *   **Mitigation:** Formalize and document matching rules; implement extensive unit and integration tests for the matching engine.
4.  **Risk:** Complex failure recovery due to system crashes during trading.
    *   **Mitigation:** Design for stateless processing where possible, maintain persistent order book state, and create detailed recovery playbooks.
5.  **Risk:** Security vulnerabilities in external interfaces.
    *   **Mitigation:** Conduct security audits, implement API gateways with throttling and authentication.

## Undecided Issues and Responsible Parties
1.  **Real-time Feedback:** Should trade success/failure be returned to the user interface immediately or with a delay? (Product Owner)
2.  **Exception Handling:** Detailed specification for exception logging and alerting mechanisms. (System Architect)
3.  **Query Frequency:** Agreed-upon SLA and limits for query frequency from the Trading Information Release system. (Integration Team Lead)
4.  **Data Retention Policy:** Duration for maintaining pending orders and completed trade records within the CTS. (Compliance Officer)
5.  **Deployment Architecture:** Decision on on-premise vs. cloud deployment and associated infrastructure. (Infrastructure Team)