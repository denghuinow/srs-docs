# Short Summary: Central Trading System (CTS)

## Background and Objectives
The Central Trading System (CTS) is a core subsystem of the Stock Trading System (STS) responsible for processing, matching, and executing stock trading instructions. Its primary objective is to analyze incoming buy, sell, and cancel instructions, match them according to specific rules (price and time priority), and facilitate the completion of trades.

## In Scope
*   Processing and matching buy and sell stock instructions.
*   Handling instruction cancellation requests.
*   Validating instructions against trading rules (e.g., price limits).
*   Logging transaction information and system events.
*   Providing interfaces for querying trade data by other subsystems.

## Out of Scope
*   User authentication and login processes.
*   Direct management of user security or financing accounts.
*   The design of the end-user trading client interface.
*   Long-term archival of historical trade data.
*   Real-time public web display of trading information.

## Stakeholders and Core Use Cases
**Stakeholders:**
*   **Transaction User Interface (Subsystem):** Submits user trading instructions (buy, sell, cancel) to the CTS.
*   **Security Account Management (Subsystem):** Receives and saves confirmed trade information from the CTS for account settlement.
*   **Trading Information Release (Subsystem):** Queries the CTS for trade data to publish statistical market information.
*   **Trading System Management (Subsystem):** Monitors and manages the CTS operations.
*   **System Maintainers:** Personnel responsible for ensuring the CTS's operational stability, performing repairs, and implementing updates.

**Core User Stories:**
1.  As a **Transaction User Interface**, I want to submit a buy instruction so that a customer's order to purchase stock can be processed and matched.
2.  As a **Transaction User Interface**, I want to submit a sell instruction so that a customer's order to sell stock can be processed and matched.
3.  As a **Transaction User Interface**, I want to submit a cancel instruction so that a customer can retract a pending order.
4.  As a **Security Account Management** subsystem, I want to receive successful trade information so that I can update the involved user accounts accordingly.
5.  As a **Trading Information Release** subsystem, I want to query the latest trading results so that I can analyze and publish market data.
6.  As a **System Maintainer**, I want the system to log exceptions and key events so that I can diagnose and resolve issues during system failures.

## Success Metrics
*   High system availability and ability to handle frequent, heavy transaction loads without crashing.
*   Accurate and reliable matching of buy/sell instructions according to defined price-time priority rules.
*   Correct and timely propagation of trade results to all dependent subsystems (e.g., account management).

## Major Constraints
*   Must integrate and communicate seamlessly with five other specified STS subsystems.
*   Must be implemented in Java and support socket-based communication.
*   Must adhere to financial trading principles: price-first, then time-first matching logic.
*   Must validate instructions against daily price fluctuation limits (rising/falling limits).
*   Must automatically remove any unmatched instructions at the end of the trading day.

## Undecided Issues
*   Whether trade confirmation/failure messages should be returned to the user interface immediately or with a delay (e.g., next day).
*   The specific strategy and format for exception logging within the system.
*   The required frequency for the Trading Information Release subsystem to send data queries.
*   Detailed security protocols and measures for protecting instruction and trade data.
*   Whether to provide a status return message for cancel instruction requests.