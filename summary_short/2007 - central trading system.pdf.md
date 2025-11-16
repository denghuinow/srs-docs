# Short Summary

- **Background and objectives**: The Central Trading System (CTS) is a subsystem of the Stock Trading System designed to process stock trading instructions, match buy/sell orders based on specific rules, and interface with other modules for message exchange and data storage.

- **In scope**:
  - Processing buy, sell, and cancel stock trading instructions.
  - Matching instructions using price-first and time-first principles.
  - Logging and storing trade information.
  - Providing query interfaces for trade data.
  - Handling instruction validity checks and fund freezing.

- **Out of scope**:
  - User interface design and implementation.
  - Security account management operations.
  - Network message promulgation logic.
  - Trading system management functions.
  - Real-time trade information display to end users.

- **Roles and core use cases**:
  - As a Transaction User Interface, I want to submit buy/sell instructions so that trades can be executed.
  - As a Security Account Management system, I want to receive trade results so that accounts can be updated.
  - As a Trading Information Release system, I want to query trade data so that it can be published.

- **Success metrics**:
  - System processes frequent buy/sell instructions without crashes.
  - Trades are matched correctly under price and time rules.
  - Interfaces reliably communicate with other subsystems.

- **Major constraints**:
  - Must handle high instruction frequency and system overhead.
  - Requires Java and socket programming expertise for maintenance.
  - Must comply with daily instruction expiration rules.
  - Must enforce rising/falling price limits.
  - Must integrate with existing STS subsystems.

- **Undecided issues**:
  - Whether to return trade results immediately or the next day.
  - Whether to implement exception logging.
  - Frequency of queries from the release system.
  - Need for warning mechanisms on query failure.
  - Security implementation details.