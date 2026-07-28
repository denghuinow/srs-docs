# Short Summary: Water Use Tracking Project

## Background and Objectives
The Water Use Tracking (WUT) System is a GIS-based application developed by the Southwest Florida Water Management District to spatially and temporally track and analyze regulatory and resource management data. Its primary objective is to support the Southern Water Use Caution Area (SWUCA) Management Plan and validate SWUCA II Rules by providing automated tools for monitoring water use trends and compliance.

## In Scope
- Tracking geographic and temporal trends in permitted and actual water use within the SWUCA.
- Providing tools to aggregate water use data over defined geographic areas (e.g., counties, watersheds).
- Supporting water use permit evaluation and compliance monitoring.
- Integrating data from Regulatory, Water Management, and GIS databases.
- Enabling spatial analysis and reporting for internal staff and external customers.

## Out of Scope
- Major changes to existing mainframe databases (DB2) and applications.
- Development of new hardware or software infrastructure beyond the District's current environment.
- Comprehensive water quality data collection and loading into the Water Management Database.
- Real-time data updates; the system relies on replicated data.
- Full implementation of all identified requirements in the initial release (some deferred).

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Executive Sponsors (e.g., Bruce Wirth):** Provide executive-level oversight and requirements.
- **Science Business Experts (e.g., Albert Bond):** Estimate water usage and support modeling activities.
- **Regulatory Business Experts (e.g., Christine Jackson):** Provide permitting expertise and ensure rule compliance.
- **Technical Experts (e.g., Steven Dicks):** Offer GIS, database, and programming support.
- **Other Impacted Parties (e.g., Kurt Fritsch):** Provide cross-departmental perspective and ensure scope adherence.
- **External Customers (e.g., local governments):** Access standardized reports and interactive maps.

**Core User Stories:**
1. As a Water Use Permit Evaluator, I want to view spatial impacts of new applications so that I can assess competition for water resources.
2. As a Technical Services Staff member, I want to aggregate permitted pumpage over specific geographic areas so that I can analyze long-term trends.
3. As a Records and Data Staff member, I want tools for quality control of Water Use Permit data so that I can ensure data accuracy.
4. As a Resource Conservation Department member, I want to access water use data for groundwater model calibration so that I can support resource management.
5. As an Executive Staff member, I want to generate standard reports for the Governing Board so that I can support decision-making.
6. As an External Customer, I want to interact with web-accessible maps and documents so that I can query areas of interest independently.

## Success Metrics
- Successful integration of data from Regulatory, Water Management, and GIS databases.
- Delivery of a system that supports all SWUCA Management Plan tracking and analysis requirements.
- User acceptance across all stakeholder groups, including internal staff and external customers.

## Major Constraints
- Dependence on existing DB2, Oracle, and ArcSDE databases without structural changes.
- Requirement to operate within the District's current hardware and software architecture.
- Need for nightly data replication from mainframe systems to the Oracle reporting database.
- Adherence to statutory time frames for permit evaluation processes.
- Compliance with District programming standards and change management procedures.

## Undecided Issues
- Prioritization of requirements for subsequent system releases.
- Specific protocols for updating different data types and ensuring data consistency.
- Detailed implementation of certain Net Benefit calculations and tracking mechanisms.
- Final determination of user access levels and security roles for all system features.
- Resolution of data availability issues for certain requirements (e.g., relocated quantities).