# The Energy Management System (THEMAS) - Software Requirements Specification

## System Overview
THEMAS is an energy management system designed to monitor and control heating and cooling systems in buildings. The system operates independently of other systems and consists of both hardware and software components. This specification focuses solely on the software requirements.

## Product Functions

### Temperature Monitoring
- Receive valid temperature and system parameters
- Determine temperature status based on predefined limits
- Activate heating/cooling mode when temperature changes are requested
- Validate temperature readings from thermostats
- Generate alarm data for invalid or out-of-range temperatures

### Utilization Determination
- Process heating/cooling requests and utilization parameters
- Determine status of all heating/cooling units
- Generate unit unavailable events when requests cannot be fulfilled
- Control heating/cooling signals to turn units on/off
- Manage concurrent operation limits for heating/cooling units

### System Initialization
- Load heating/cooling unit definitions from initialization file
- Load thermostat definitions with unique identifiers
- Load utilization parameters including maximum concurrent units
- Set trigger values for temperature thresholds
- Set overtemperature values for safety limits
- Establish valid temperature range for system operation
- Turn off all heating/cooling units during initialization

### System Reporting
- Store all system events in a database
- Generate operational history reports for past twelve months
- Create statistical summary reports for selected months
- Provide supervisor interface for report selection and generation

## Functional Requirements

### Initialization (SRS-001 to SRS-007)
- Load H/C unit definitions from initialization file
- Load thermostat definitions with unique identifiers for each zone
- Load utilization parameters including maximum concurrent running units
- Set trigger values for determining when to activate heating/cooling units
- Set overtemperature values with maximum deviation of 3 degrees Fahrenheit
- Establish valid temperature range for system response
- Initialize system by turning off all units and checking thermostat settings

### Temperature Validation (SRS-008)
- Validate temperature readings against defined valid range
- Process both current temperature values and temperature settings
- Identify and flag invalid temperature readings
- Output valid temperature status for further processing

### Temperature Monitoring (SRS-009 to SRS-010)
- Determine temperature status by comparing readings to overtemperature limits
- Generate temperature trigger exceeded conditions
- Determine heating/cooling mode based on temperature differentials
- Activate appropriate heating or cooling units when needed

### Utilization Management (SRS-011 to SRS-014)
- Maintain ON/OFF status of all heating and cooling units
- Limit number of simultaneously running units based on utilization parameters
- Queue requests when maximum units are already running (LIFO queue)
- Generate unit unavailable events for denied requests
- Generate heating/cooling signals to control unit operation
- Provide status feedback to requesting thermostats

### Event and Alarm Management (SRS-015 to SRS-016)
- Generate alarm data for invalid temperatures or exceeded limits
- Produce distinct audible alarms for different conditions:
  - Invalid temperature: Alternating 500 Hz and 700 Hz beeps (3/4 second duration)
  - Temperature limit exceeded: Alternating 1000 Hz and 1500 Hz beeps (1/2 second duration)
- Generate event data for all system occurrences
- Record events with timestamps in Microsoft Access database

### User Interface (SRS-017 to SRS-018)
- Provide supervisor mechanism to change thermostat settings
- Display available thermostats and current temperature settings
- Allow selection of valid temperature values for thermostats
- Generate two types of reports:
  1. Operational history for past twelve months
  2. Statistical summary for selected months including:
     - Percentage of time each unit was on per day
     - Ratio of granted to denied heating/cooling requests per thermostat

## Technical Requirements

### Hardware Assumptions
- Thermostats provide temperature values and settings with no real-time delay
- Heating/cooling units cannot return current on/off status to THEMAS
- Units can be turned on/off by supervisor commands
- All hardware interfaces operate through Windows NT operating system

### System Constraints
- Thermostats only provide temperature values and settings
- Heating/cooling units provide no feedback to THEMAS system
- Signals sent to units cannot be verified for successful execution
- System designed to run on Microsoft Windows NT operating system

### Data Management
- Initialization data stored in configuration files
- Event data stored in Microsoft Access database
- Report data generated as ASCII files with selectable locations
- Temperature data processed in real-time from thermostats

## User Characteristics
- Intended for building maintenance personnel responsible for HVAC systems
- Minimal user intervention required during normal operation
- Supervisor receives warnings about faulty temperatures
- System provides clear, non-confusing status information
- Report generation capability for efficient system management

## Quality Attributes
- Automated operation with minimal external intervention
- Real-time temperature monitoring and response
- Safety mechanisms through overtemperature limits
- Audible alarm system for critical conditions
- Statistical reporting for performance analysis
- Queue management for handling peak demand situations
