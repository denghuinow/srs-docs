# Detailed Summary

## Background and Scope
The Water Use Tracking (WUT) System is a GIS-based application designed to spatially and temporally track and analyze regulatory and water resource management data for the Southwest Florida Water Management District. It primarily supports the Southern Water Use Caution Area (SWUCA) Management Plan implementation and SWUCA II Rules validation. The system integrates water use permits, geographic data, and water resource information to enable trend analysis and compliance monitoring across the district. Non-goals include hardware/software architecture changes and modifications to existing mainframe database systems.

## Role Matrix and Use Cases
- **General WUT User**: Views reports, maps, and permit data
- **WUT Administrator**: Maintains system parameters and news
- **Water Use Estimator**: Manages water use estimation data
- **WUP Evaluator**: Analyzes permit applications and compliance
- **Technical Staff**: Performs spatial analysis and modeling
- **External Customers**: Accesses public-facing maps and reports

Key use cases include View Water Use Permit, View Map, Generate Well Package, View Compliance Information, and Maintain Water Use Estimates.

## Business Process
**Main Process: Water Use Analysis (8 steps)**
1. User accesses WUT system via web browser
2. System authenticates and determines user role
3. User selects analysis type (map, report, or permit search)
4. System presents relevant interface options
5. User defines spatial/temporal criteria
6. System queries integrated databases
7. Results displayed in chosen format
8. User can drill down for detailed information

**Key Branch: Permit Evaluation (4 steps)**
- Trigger: New permit application submission
- Evaluator searches existing permits in area
- System displays spatial relationships and MFL impacts
- Evaluator generates compliance report

**Key Branch: Data Maintenance (3 steps)**
- Administrator updates business rule parameters
- System validates changes
- New parameters available for next calculation cycle

## Domain Model
- **WaterUsePermit** (permitNumber: required/unique, issueDate, expirationDate, status)
- **WithdrawalPoint** (universalID: required/unique, location, aquifer)
- **Permittee** (ownerName: required, contactInfo)
- **WaterUse** (quantity: required, useType, timePeriod)
- **ComplianceData** (pumpageReports, meterReadings, cropReports)
- **LandUse** (landUseType, acreage, soilType)
- **MFLWaterbody** (waterbodyID: required/unique, minimumLevel)
- **NetBenefit** (benefitType, quantity, sourcePermit, targetPermit)

## Interfaces and Integrations
- **Regulatory Database (RDB)**: Direction: Inbound, Theme: Water use permits, Input: Daily replication, Output: Normalized permit data, SLA: Daily updates
- **Water Management Database (WMDB)**: Direction: Inbound, Theme: Water resource data, Input: Water levels/flows, Output: Historical trends, SLA: Daily synchronization
- **GIS/ArcSDE**: Direction: Bi-directional, Theme: Spatial data, Input: Location coordinates, Output: Map layers, SLA: Real-time access
- **External Web Services**: Direction: Outbound, Theme: Public data access, Input: Query parameters, Output: Interactive maps, SLA: Business hours availability

## Acceptance Criteria
**Water Use Tracking**
- Given a user selects a geographic area and time period, when they request water use trends, then the system displays permitted vs actual pumpage comparisons

**Permit Compliance Monitoring**
- Given an evaluator searches for permits near an MFL waterbody, when they view compliance data, then the system highlights permits exceeding allocated quantities

**Spatial Analysis**
- Given a user loads multiple GIS layers, when they perform spatial queries, then the system aggregates data by selected geographic boundaries

## Non-functional Metrics
- **Performance**: Sub-5-second response for standard queries; support 50 concurrent users
- **Reliability**: 99% uptime during business hours; automated daily data replication
- **Security**: Role-based access control; integration with district authentication
- **Compliance**: FGDC-compliant metadata; audit trail for permit decisions
- **Observability**: Comprehensive logging; system usage metrics tracking

## Milestones and Release Strategy
1. Core database replication and normalization
2. Basic reporting and map viewing capabilities
3. Water use permit search and detail views
4. Compliance tracking features
5. Net benefit calculation modules
6. Public-facing web components

## Risk List and Mitigation Strategies
- **Data Quality Issues**: Implement data validation routines and error reporting
- **System Performance**: Conduct load testing and optimize database queries
- **Scope Creep**: Maintain requirement traceability and change control process
- **Integration Complexity**: Establish clear interface specifications and testing protocols
- **User Adoption**: Provide comprehensive training and user support
- **Regulatory Changes**: Design flexible business rule parameters
- **Data Volume**: Implement data archiving and purging strategies
- **Security Compliance**: Regular security audits and access reviews

## Undecided Issues and Responsible Parties
- **Adjacent District Data Integration**: Technical Team - Not mentioned
- **Real-time Data Updates**: Architecture Team - Not mentioned
- **Mobile Access Requirements**: Stakeholder Committee - Not mentioned
- **Advanced Analytics Features**: Product Manager - Not mentioned
- **Long-term Data Archiving Strategy**: Infrastructure Team - Not mentioned
- **External API Development**: Technical Team - Not mentioned
- **Disaster Recovery Procedures**: Operations Team - Not mentioned
- **User License Management**: Administration Team - Not mentioned