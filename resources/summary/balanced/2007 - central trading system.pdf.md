# Balanced Summary: Central Trading System (CTS)

## Goals and Scope
The Central Trading System (CTS) is a subsystem within the Stock Trading System (STS) responsible for processing, matching, and executing stock trading instructions (buy, sell, cancel, query). Its primary goal is to analyze incoming instructions, match buy and sell orders based on specific rules (price/time priority), and interface with other subsystems to manage accounts and release trading information.

## Stakeholders and User Stories
*   **Transaction User Interface:** Subsystem that submits user trading instructions (buy, sell, cancel, query) to the CTS.
*   **Security Account Management:** Subsystem that receives and saves successful trade information from the CTS to update user accounts.
*   **Trading Information Release:** Subsystem that queries the CTS for trading data to be statistically analyzed and published.
*   **Trading System Management:** Subsystem responsible for overall system oversight and management, interacting with the CTS.
*   **Maintainers:** Technical personnel responsible for system upkeep, requiring Java and socket programming knowledge to handle crashes and new requirements.

**User Stories:**
1.  As a **Transaction User Interface**, I want to **submit a buy instruction** so that **a customer's stock purchase request can be processed**.
2.  As a **Transaction User Interface**, I want to **submit a sell instruction** so that **a customer's stock sale request can be processed**.
3.  As a **Transaction User Interface**, I want to **submit a cancel instruction** so that **a pending trading instruction can be revoked**.
4.  As a **Security Account Management** system, I want to **receive successful trade information** so that **user account records can be updated**.
5.  As a **Trading Information Release** system, I want to **query trading data** so that **it can be analyzed and published on a website**.
6.  As a **System Maintainer**, I want the **system to handle high transaction loads** so that **it remains stable and does not crash under heavy traffic**.

## Key Processes
1.  **Instruction Reception:** The process is triggered when the Transaction User Interface submits a new instruction (buy, sell, cancel, query).
2.  **Instruction Pretreatment:** The incoming instruction is validated, user funds are frozen, and a log entry is created.
3.  **Instruction Management:** Valid instructions are routed to specific handlers based on their type (trade, cancel, query).
4.  **Trade Matching:** For buy/sell instructions, the system attempts to match orders based on price-time priority and other rules.
5.  **Result Processing:** After matching (or a cancel/query action), the instruction status is modified and results are prepared.
6.  **Data Dispatch:** Trading results are sent to the Security Account Management and Trading Information Release subsystems.
7.  **Logging:** A log of all instructions and their outcomes is maintained throughout the process.

## Domain Data Elements
*   **Instruction:** (Instruction ID) - User ID, Stock ID, Type (Buy/Sell/Cancel/Query), Quantity, Price, Timestamp, Status.
*   **Trade:** (Trade ID) - Buyer User ID, Seller User ID, Stock ID, Quantity, Executed Price, Timestamp.
*   **User Account:** (User ID) - Account Balance, Frozen Funds, Portfolio Holdings.
*   **Stock:** (Stock ID) - Stock Name, Current Price, Daily Price Limits (Rise/Fall).
*   **Log Entry:** (Log ID) - Timestamp, Instruction ID, Action, Result, Error Code (if any).

## Non-Functional Requirements
1.  **Performance:** The system must handle frequent, high-volume instruction processing with low latency.
2.  **Reliability:** Strategies must be in place to prevent and recover from system crashes due to overhead.
3.  **Maintainability:** The system should be modifiable by maintainers familiar with Java and socket programming.
4.  **Accuracy:** Trade matching must strictly follow defined business rules like price-time priority.
5.  **Auditability:** Comprehensive logging of all instructions and system actions is required.

## Milestones and External Dependencies
1.  **First Increment Delivery:** Implementation of core buy, sell, and query functions, and saving trade information.
2.  **Second Increment Delivery:** Implementation of the cancel instruction functionality.
3.  **Integration with Transaction User Interface:** Dependency on the stable API of the client-serving subsystem.
4.  **Integration with Security Account Management:** Dependency on the account subsystem's interface to receive trade data.
5.  **Database System Readiness:** Dependency on the underlying database for storing instructions, logs, and account data.

## Risks and Mitigation Strategies
1.  **Risk:** System crash under high transaction load.
    *   **Mitigation:** Implement robust load-handling strategies and failover mechanisms.
2.  **Risk:** Incorrect trade matching due to logic errors.
    *   **Mitigation:** Rigorous testing of matching algorithms against all defined business rules.
3.  **Risk:** Integration failures with other subsystems (e.g., Account Management).
    *   **Mitigation:** Establish clear, stable interface contracts and conduct early integration testing.
4.  **Risk:** Data inconsistency or loss during processing.
    *   **Mitigation:** Implement transaction management and reliable logging for recovery.
5.  **Risk:** Security vulnerabilities in instruction processing or interfaces.
    *   **Mitigation:** Incorporate security reviews and testing, addressing issues noted in open issues.

## Undecided Issues
1.  Should trade confirmation be returned to the user interface immediately or batched?
2.  How should trade failures be communicated back to the user (e.g., next day)?
3.  Is a detailed exception log required, and what should it contain?
4.  What specific security measures need to be implemented?
5.  Should the status of a cancel transaction be returned to the user?
6.  How frequently should the Trading Information Release system query for data?