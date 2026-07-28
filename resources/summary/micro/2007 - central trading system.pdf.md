Purpose & Scope: The system is a subsystem for completing stock trades by matching buy and sell instructions according to specific rules.

Core Functions:
*   Match buy and sell instructions based on price and time priority.
*   Process and cancel trading instructions.
*   Provide interfaces for querying and releasing trade information.

Key Constraints:
*   Must handle high transaction frequency and prevent system crashes from overhead.
*   Must reject instructions that exceed defined price rise/fall limits.
*   Must remove unfulfilled instructions at the end of the trading day.