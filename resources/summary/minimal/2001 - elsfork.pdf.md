**Purpose & Scope**: Defines requirements for a standardized communication system to transfer data between wind turbine controllers and remote SCADA systems, enabling vendor-independent monitoring and control for single turbines and wind farms.

**Core Functions**:
*   Remote supervision of turbine status and measurements.
*   Remote control commands (start/stop, set points).
*   Alarm and event management.
*   Retrieval of historical data, logs, and configuration.
*   System management (time synchronization, network management, security).

**Key Users**: Wind turbine operator/owner, electrical network operator, and external parties (e.g., vendors).

**Key Constraints**:
*   Must not be used for safety-critical functions (failsafe turbine operation is self-contained).
*   Must be based on open, widely accepted standards and interfaces.
*   Must withstand wide temperature, moisture, salinity, and vibration ranges.
*   Time-critical function response must be within 0.5 seconds.
*   Must allow interfacing with existing, proprietary systems via gateways.