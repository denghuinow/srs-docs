# Detailed Summary

## Background and Scope
THEMAS is an independent energy management system designed to monitor and control heating/cooling units across a 3-floor office building with 4 quadrants per floor. The system maintains temperature within defined ranges while limiting concurrent unit operation through utilization management. Non-goals include detailed hardware interface specifications and real-time unit status feedback mechanisms.

## Role Matrix and Use Cases
- **System Supervisor**: Monitors alarms, generates reports, modifies thermostat settings
- **Thermostat**: Provides temperature readings and settings (main scenario: continuous data transmission)
- **H/C Unit**: Receives control signals (exception: unit failure handling)
- **Initialization File**: Provides system parameters
- **Event Database**: Stores operational history
- **Report Generator**: Creates statistical summaries

## Business Process
**Main Process (Temperature Control Loop)**
1. System initialization loads operational parameters
2. Validate temperature readings against defined ranges
3. Compare current temperature to trigger values
4. Generate H/C requests when thresholds exceeded
5. Check utilization limits against active units
6. Send approved control signals to H/C units
7. Log system events and alarm conditions
8. Generate operational reports on demand

**Key Branch: Unit Unavailable**
- Request exceeds maximum concurrent units
- Add to LIFO queue
- Generate denied request event
- Process queued requests when capacity available

**Key Branch: Alarm Condition**
- Detect invalid temperature or limit exceeded
- Activate audible alarm pattern
- Require manual supervisor reset
- Log alarm event

## Domain Model
- **Thermostat** (thermostatID: string required/unique, currentTemp: integer, tempSetting: integer)
- **H/C Unit** (unitID: string required/unique, status: string, type: string)
- **Operational Parameters** (triggerDelta: integer required, overtempDelta: integer required)
- **Temperature Range** (minTemp: integer required, maxTemp: integer required)
- **Utilization Parameters** (maxConcurrent: integer required)
- **System Event** (eventID: string required/unique, timestamp: datetime, description: string)
- **Alarm Event** (alarmType: string required, resetRequired: boolean)
- **Report Data** (reportType: string, timePeriod: string)

## Interfaces and Integrations
- **Thermostat Interface** (inbound: temperature data, thermostat settings; outbound: unit status; SLA: real-time data transmission)
- **H/C Unit Control** (outbound: on/off signals; input: approved requests; output: unit activation; SLA: immediate execution)
- **Initialization File** (inbound: system parameters; input: configuration data; output: operational parameters)
- **Event Database** (outbound: event storage; input: system/alarm events; output: historical data; SLA: persistent storage)
- **Supervisor Interface** (bidirectional: alarm display, report generation, setting modification)
- **Audible Alarm System** (outbound: alarm patterns; input: alarm conditions; output: audible alerts)

## Acceptance Criteria
- Given valid initialization data when system starts then all H/C units initialize to off state and operational parameters load correctly
- Given temperature exceeds trigger values when utilization limit not reached then appropriate H/C unit activates and event logs
- Given supervisor requests monthly report when event data exists then system generates statistical summary with unit utilization percentages
- Given invalid temperature reading when validation fails then system activates alarm and requires manual reset

## Non-functional Metrics
- **Performance**: Process temperature updates within 1 second; Generate reports within 30 seconds
- **Reliability**: 99.5% system uptime; Temperature validation accuracy >99%
- **Security**: Supervisor authentication required for configuration changes
- **Compliance**: ANSI/IEEE STD 830-1984 compliance; Windows NT compatibility
- **Observability**: Comprehensive event logging; Real-time system status monitoring

## Milestones and Release Strategy
1. Core temperature monitoring and validation
2. H/C unit control and utilization management
3. Alarm system and event logging
4. Supervisor interface and reporting
5. System integration and validation
6. Production deployment

## Risk List and Mitigation Strategies
- **Hardware interface undefined**: Develop abstraction layer for future hardware integration
- **No unit status feedback**: Implement software-based unit status tracking
- **Concurrent unit limits**: Implement LIFO queuing with request validation
- **Temperature sensor failure**: Multiple validation checks with alarm escalation
- **Database corruption**: Regular backups with integrity verification
- **System initialization failure**: Fallback to default parameters with supervisor notification
- **Report generation delays**: Implement incremental data processing
- **Alarm system dependency**: Secondary visual alert system as backup

## Undecided Issues and Responsible Parties
- **H/C unit control signal specification**: Hardware team (Not mentioned)
- **Thermostat communication protocol**: Interface team (Not mentioned)
- **Database scalability requirements**: Architecture team (Not mentioned)
- **Multi-site deployment strategy**: Deployment team (Not mentioned)
- **Backup power requirements**: Infrastructure team (Not mentioned)
- **Long-term data retention policy**: Compliance team (Not mentioned)
- **Disaster recovery procedures**: Operations team (Not mentioned)
- **Future expansion capabilities**: Product team (Not mentioned)