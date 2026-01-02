**Purpose & Scope**: The Central Trading System completes stock trading by analyzing, matching, and processing trading instructions received from a client subsystem. It is a subsystem within a larger Stock Trading System, interfacing with modules for client services, account management, information release, and system management.

**Core Functions**:
*   Match buy and sell instructions based on price and time priority rules.
*   Process instruction cancellation requests.
*   Save successful trade information to an account management subsystem.
*   Respond to queries for trade information from an information release subsystem.

**Key Users**: Transaction users (via a client interface) and system maintainers.

**Key Constraints**:
*   Must handle a high frequency of instruction operations.
*   Must enforce daily expiration for unfilled instructions.
*   Must reject instructions that violate predefined price rising/falling limits.