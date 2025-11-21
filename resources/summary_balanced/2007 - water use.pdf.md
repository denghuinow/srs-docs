# Balanced Summary

## Goals and Scope
The Water Use Tracking (WUT) System is a GIS-based application designed to spatially and temporally track and analyze regulatory and water resource management data for the Southwest Florida Water Management District. It supports activities defined in the Southern Water Use Caution Area (SWUCA) Management Plan and validates SWUCA II Rules implementation. The system integrates permitting, geographic, and water resource data from existing District databases to enable comprehensive water use analysis and reporting.

## Roles and User Stories
- **WUP Evaluator**: I want to view permit locations and compliance data spatially so that I can assess new applications efficiently.
- **Technical Services Staff**: I want to aggregate permitted and actual pumpage by geographic area so that I can analyze long-term water use trends.
- **Records and Data Staff**: I want to access water use permit details and quality control tools so that I can maintain data accuracy.
- **External Customer**: I want to search and view interactive maps of water use permits so that I can access consistent public information.
- **WUT Administrator**: I want to maintain system parameters and news items so that I can support user communication and system configuration.

## Key Processes
1. **Trigger: User access request** – System authenticates user role and displays the WUT Home Page with role-specific features.
2. **Trigger: Nightly schedule** – System replicates and normalizes data from mainframe DB2 to Oracle database.
3. **Trigger: User query** – System searches water use permits based on spatial, temporal, or attribute criteria.
4. **Trigger: Map request** – System displays water use data with selectable GIS layers for spatial analysis.
5. **Trigger: Report selection** – System generates predefined reports with optional runtime criteria filtering.
6. **Trigger: Data maintenance need** – Administrator updates water use estimates or business rule parameters.
7. **Trigger: System startup** – System loads configuration and news items for user access.

## Domain Data Elements
- **Water Use Permit**: Permit Number, Permittee, Issue Date, Expiration Date, Permitted Quantity, Use Type
- **Well**: Universal ID, Aquifer, Total Depth, Casing Depth, Status
- **Pumpage Report**: Report ID, Reporting Date, Meter Reading, Calculated Quantity, Compliance Status
- **GIS Layer**: Layer ID, Description, Source, Update Frequency, Spatial Reference
- **Compliance Data**: Condition ID, Requirement, Submission Date, Verification Status, Notes
- **Water Resource**: Site ID, Measurement Type, Value, Collection Date, Location

## Non-Functional Requirements
- System must provide real-time data access with consistent query results
- Application must support role-based security and District programming standards
- All data transfers must occur during non-business hours to minimize network impact
- User interface must be intuitive with online help and training materials
- System must integrate with existing District hardware/software architecture
- Metadata must be FGDC compliant and readily accessible

## Milestones and External Dependencies
- Completion of HP-UX system upgrade in FY 2004
- Implementation of required data structure changes in mainframe systems
- Availability of current Regulatory, WMDB, and GIS databases in existing formats
- Coordination with adjacent water districts for GIS layer compatibility
- Adherence to SWUCA Rules implementation timeline

## Risks and Mitigation Strategies
- **Risk**: Required data not available in source systems – **Mitigation**: Implement temporary storage in WUT application
- **Risk**: Changes to current database structures – **Mitigation**: Establish communication protocols with system owners
- **Risk**: Hardware/software architecture modifications – **Mitigation**: Adhere to District technology standards
- **Risk**: Insufficient data quality – **Mitigation**: Implement data validation and correction workflows
- **Risk**: Scope creep from numerous stakeholder requirements – **Mitigation**: Prioritize features across multiple releases

## Undecided Issues
- Integration schedule with adjacent districts' GIS data
- Specific implementation timeline for mainframe data structure changes
- Final prioritization of requirements for subsequent releases
- Detailed security implementation approach
- Training delivery method and schedule
- Not mentioned