# Short Summary: Gemini 8-m Telescopes Control System Software Requirements

## Background and Objectives
This document defines the operational requirements for the Gemini Control System software, guiding the development of controls and data acquisition systems to ensure consistent operation within the Gemini 8-m Telescopes. It establishes general criteria and specific functional requirements for software and controls design, oriented toward developers rather than end-users.

## In Scope
- Control and data acquisition software for telescope and instruments.
- Support for multiple observing modes: interactive, queue-based, remote, and service observing.
- On-line databases, communication subsystems, and data specifications.
- User interfaces and operational procedures across different access levels.
- Integration with external software (e.g., star catalogs, data reduction tools).

## Out of Scope
- Commercial or public-domain software used for telescope control (only interface specifications are considered).
- Embedded software with no software interface to the Gemini system.
- Detailed hardware specifications (covered in separate documents).
- Full redundancy requirements (only cost-effective redundancy is considered).
- Automatic expert scheduling software (only decision-support tools are required).

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Astronomer:** End user who plans and requests observations, focusing on data acquisition.
- **Science Observer:** On-site person responsible for monitoring data acquisition and validating data integrity.
- **Telescope Operator:** On-site controller responsible for telescope and instrument integrity during observations.
- **Support Personnel:** Responsible for maintenance, installation, and configuration changes.
- **Developer:** Designs, tests, configures, and upgrades subsystems.
- **Administrator:** Manages high-level functional control, scheduling, and system modifications.

**Core Use Cases:**
1. As an Astronomer, I want to submit observing commands via a scheduler so that observations can be executed automatically with minimal interaction.
2. As a Telescope Operator, I want direct control of the telescope and instruments during observations so that I can ensure system safety and performance.
3. As a Science Observer, I want to monitor data acquisition and quality in real-time so that I can validate data integrity for the astronomer.
4. As a Developer, I want to test and upgrade subsystems in a simulated environment so that I can ensure functionality without disrupting ongoing observations.
5. As Support Personnel, I want full access to subsystems for maintenance and diagnostics so that I can perform repairs and updates efficiently.
6. As an Administrator, I want to inquire about system utilization and scheduling so that I can make informed decisions about observatory operations.

## Success Metrics
- System downtime due to failures limited to a maximum of 2% (goal of 1%), translating to no more than 15 minutes per night or one night per month.
- Recovery and/or reconfiguration from error conditions within 5 minutes to resume observing.
- Support for up to six active control nodes and two monitoring nodes simultaneously without performance degradation.

## Major Constraints
- Use of commercial packages, off-the-shelf software, and standards whenever feasible.
- All software must be developed using standard methodologies (e.g., Ward/Mellor) and version control (CVS).
- Software must be portable and hardware-independent, with no assumptions beyond defined interfaces.
- Remote operations must be supported, with functionality transparent across sites despite bandwidth limitations.
- Safety systems must include independent hardware interlocks and software limits to protect personnel and equipment.

## Undecided Issues
1. Definition of a standard for acquisition and storage of detector data.
2. Choice of link for data transfer between subsystems.
3. Desirable hardware specifications for development and target systems.
4. Standards for online software and development environment.
5. Supportability plan details, including maintenance levels and resource requirements.
6. Descriptions and access methods for star catalogs.