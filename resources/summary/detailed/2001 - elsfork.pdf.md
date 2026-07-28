# Detailed Summary: Functional Requirements for a Communication System for Wind Turbine Applications

## Background and Scope
This document defines functional requirements for a standardized communication system between wind turbine control systems and remote SCADA systems, addressing the current lack of interoperability among proprietary solutions. The scope covers data transfer and handling for both single turbines and wind farms, including operational functions like supervision, control, and alarm management. Non-goals include specifying SCADA system characteristics, HMI details, control algorithms, voice/video communication, and local temporary data hook-ups.

## Stakeholders Matrix and Use Cases
- **Electrical System Operator (Transmission Network)**: Manages grid stability and power quality for large wind farms.
- **Electrical Network Operator (Distribution)**: Oversees network connection and compliance at the point of common coupling.
- **Wind Turbine Operator (O&M)**: Performs daily remote supervision, control, and maintenance of turbines.
- **Owner**: Monitors production and asset performance for financial and operational oversight.
- **External Parties (Vendors, Third Parties)**: Access data for support, analytics, or regulatory purposes.

**Main Scenarios**:
1. Periodic data collection for operational monitoring.
2. Event-driven alarm transmission for fault conditions.
3. Remote control commands (start/stop, setpoints).
4. Historical data retrieval for analysis.
5. System configuration and software updates.
6. Time synchronization across devices.
7. Security authentication and access control.
8. Redundant communication channel failover.

**Exception Scenarios**:
1. Communication failure with local buffering and recovery.
2. Unauthorized access attempts with authentication rejection.
3. High-priority command during network congestion.
4. Legacy system integration via gateways.

## Business Process
**Main Process: Remote Monitoring and Control**
1. **Trigger**: SCADA system initiates connection to wind turbine controller.
2. **Authentication**: Secure handshake and client/server verification.
3. **Data Subscription**: SCADA requests specific data types (e.g., analog, binary).
4. **Continuous Data Transfer**: Turbine sends periodic/event-driven data (e.g., measurements, alarms).
5. **Operator Review**: Data presented on HMI for monitoring.
6. **Command Issuance**: Operator sends control commands (e.g., start/stop, setpoints).
7. **Command Execution**: Turbine executes with handshake confirmation.
8. **Logging**: All transactions logged locally and remotely.

**Key Branch A: Alarm Handling**
1. **Trigger**: Turbine detects abnormal condition (e.g., overheating).
2. **Immediate Transmission**: Alarm sent spontaneously to SCADA.
3. **Operator Alert**: HMI highlights alarm for acknowledgment.
4. **Logging**: Alarm stored locally and in SCADA event log.

**Key Branch B: Historical Data Retrieval**
1. **Trigger**: SCADA requests historical data (e.g., fault records).
2. **Buffer Access**: Turbine retrieves data from local storage.
3. **Data Transmission**: Data sent on-demand without real-time sync.
4. **SCADA Storage**: Data archived in central database.

## Domain Model
- **Wind Turbine**: Entity representing a single turbine (required attributes: ID, location, status).
- **Wind Farm**: Aggregates multiple turbines (required attributes: name, total capacity, WFMC reference).
- **Data Point**: Base entity for all data types (required attributes: name, value, timestamp, quality; unique: name hierarchy).
- **Alarm**: Specialized data point for abnormal states (required attributes: severity, acknowledged flag; reference: Data Point).
- **Event**: Logged state change or action (required attributes: description, user; reference: Data Point).
- **Command**: Instruction sent to turbine (required attributes: type, parameter, confirmation status).
- **User**: Actor with access rights (required attributes: role, authentication credentials; unique: username).
- **Communication Channel**: Physical/logical connection (required attributes: type, status, redundancy flag).

## Interfaces and Integrations
1. **SCADA to Wind Turbine Controller**
   - Direction: Bidirectional
   - Interaction: Data polling and command transmission
   - Input: Control commands, data requests
   - Output: Operational data, alarms, confirmations
   - SLA: Time-critical functions ≤0.5s transfer time; availability >99%

2. **Wind Farm Main Controller (WFMC) to Individual Turbines**
   - Direction: Bidirectional
   - Interaction: Internal farm coordination
   - Input: Turbine data, local setpoints
   - Output: Coordinated commands, aggregated data
   - SLA: Periodic data ≤1s update; redundant paths

3. **Legacy System Gateway**
   - Direction: Bidirectional
   - Interaction: Protocol translation
   - Input: Proprietary protocol data
   - Output: Standardized protocol data
   - SLA: Transparent translation; minimal latency

4. **External Party Access**
   - Direction: Outbound
   - Interaction: Data feeds for vendors/third parties
   - Input: Authorization credentials
   - Output: Subset of operational/historical data
   - SLA: Secure encrypted channels; access logging

## Acceptance Criteria
**Capability 1: Real-time Data Monitoring**
- Given the SCADA system is connected, when requesting analog measurements, then values with timestamps and quality indicators are received within 1 second.
- Given an alarm condition occurs, when the turbine detects it, then an alarm is spontaneously transmitted to SCADA within 0.5 seconds.

**Capability 2: Remote Control**
- Given an authorized operator, when issuing a start command, then the turbine executes it and returns a confirmation handshake.
- Given a setpoint command, when sent to the turbine, then the value is updated and acknowledged.

**Capability 3: Historical Data Access**
- Given a request for fault records, when initiated by SCADA, then buffered data is transmitted on-demand without disrupting real-time operations.
- Given a counter reset command, when executed, then the reset time is stored and subsequent counts accumulate correctly.

## Non-functional Metrics
- **Performance**: Time-critical data transfer ≤0.5s; system management functions ≤2s response.
- **Reliability**: 99% availability; redundant communication channels; local data buffering for recovery.
- **Security**: Authentication for all access; data integrity via error checking; optional encryption for confidentiality.
- **Compliance**: Adherence to IEC standards (e.g., 60870, 61850); open protocol support.
- **Observability**: All data time-stamped with ≤10ms accuracy; system self-checking and fault logging.

## Milestones and Release Strategy
1. Finalize functional requirement specification.
2. Select and validate candidate communication protocols.
3. Develop prototype implementation for testing.
4. Conduct field tests in Swedish and Danish wind turbines.
5. Submit specification to IEC TC88 for standardization.
6. Roll out to pilot wind farms with gradual expansion.

## Risk List and Mitigation Strategies
1. **Proprietary Protocol Resistance**: Engage vendors early; demonstrate cost benefits of standardization.
2. **Legacy System Integration**: Develop robust gateways; phase migration plans.
3. **Network Reliability**: Design redundant channels; implement local data buffering.
4. **Security Breaches**: Implement strong authentication and encryption; regular audits.
5. **Performance Bottlenecks**: Prioritize time-critical messages; adequate bandwidth provisioning.
6. **Environmental Harshness**: Specify ruggedized equipment; environmental testing.
7. **Lack of Vendor Support**: Foster multi-vendor consortium; open-source reference implementations.
8. **Standardization Delays**: Parallel field testing; interim industry agreements.

## Undecided Issues and Responsible Parties
1. **Specific Protocol Recommendation**: Awaiting test results (Working Group).
2. **Encryption Implementation Details**: To be defined based on security audits (Security Team).
3. **HMI Standardization**: Out of scope but needs coordination (SCADA Vendors).
4. **Condition Monitoring Data Formats**: Further specification needed (Condition Monitoring Consortium).
5. **Third-Party Access Pricing Models**: Business decision (Wind Farm Owners).
6. **Legacy System Upgrade Timelines**: Site-dependent planning (Asset Managers).
7. **Redundancy Level Requirements**: To be detailed per site criticality (Design Engineers).
8. **Long-term Data Archiving Strategy**: Integration with enterprise systems (IT Department).