# Balanced Summary

## Goals and Scope
The ERTMS/ETCS Functional Requirements Specification defines operational requirements for the European Train Control System to enable safe train operation across European railways. It supports interoperability between different national systems and defines mandatory and optional functions for train control and supervision. The system must function at speeds up to 500 km/h and provide driver information for safe train operation.

## Roles and User Stories
- **Driver**: I want to receive clear speed and distance information so that I can operate the train safely without ETCS intervention
- **Driver**: I want to enter train data before movement so that ETCS can properly supervise the journey
- **Driver**: I want to acknowledge operational state transitions so that responsibility changes are confirmed
- **RBC Operator**: I want to command emergency stops to specific trains so that safety incidents can be prevented
- **Maintenance**: I want equipment self-tests to run automatically at startup so that system integrity is verified

## Key Processes
1. **System Startup** (trigger: equipment power-on) - Automatic self-test performs equipment verification
2. **Train Data Entry** (trigger: before movement) - Driver enters train characteristics for supervision
3. **Movement Authority** (trigger: track-to-train transmission) - System receives and validates movement permissions
4. **Speed Supervision** (trigger: continuous monitoring) - Calculates braking curves and monitors speed compliance
5. **Operational State Transition** (trigger: automatic or manual) - Manages transitions between supervision modes
6. **Emergency Intervention** (trigger: safety violation) - Applies brakes when safety limits are exceeded
7. **Data Recording** (trigger: continuous) - Logs all operational data for investigation and analysis

## Domain Data Elements
- **Train**: Train ID, Length, Maximum Speed, Axle Load, Air Tight Status
- **Movement Authority**: Authority ID, End Location, Time-outs, Speed Profiles
- **Infrastructure Data**: Track ID, Speed Restrictions, Gradient, Adhesion Conditions
- **Driver**: Driver ID, Language Preference, Authorization Level
- **Operational State**: State Type, Transition Conditions, Supervision Parameters
- **National Values**: Default Parameters, Area Definitions, Country-specific Rules

## Non-functional Requirements
- Must support maximum train speed of 500 km/h
- Must maintain safety during transitions between operational states
- Must provide automatic failure detection and appropriate reactions
- Must ensure compatibility with existing national train control systems
- Must record operational data with UTC timestamping
- Must provide clear driver indications and warnings

## Milestones and External Dependencies
- Compatibility with national systems listed in CCS TSI
- Implementation of harmonized default values across all equipment
- Support for multiple application levels (0-3 and STM)
- Transition capabilities between different RBC areas
- Compliance with mandatory requirements marked (M)

## Risks and Mitigation Strategies
- **Transmission failures**: Implement fallback procedures with national value-defined reactions
- **Equipment failures**: Automatic brake application and failure indication to driver
- **Driver non-acknowledgment**: Brake application after timeout for critical transitions
- **Data unavailability**: Use default values when national values are unavailable
- **Interoperability issues**: Strict adherence to mandatory requirements and compatibility rules

## Undecided Issues
- Specific environmental specifications (Not mentioned)
- Detailed training requirements (Not mentioned)
- Complete RAMS specifications (Not mentioned)
- Detailed DMI design specifications (Not mentioned)
- Specific implementation timelines (Not mentioned)
- Performance metrics beyond basic requirements (Not mentioned)