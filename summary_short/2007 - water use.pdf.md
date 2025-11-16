# Short Summary

- **Background and objectives**: The Water Use Tracking (WUT) System is a GIS-based application designed to spatially and temporally track and analyze regulatory and resource management data for the Southwest Florida Water Management District. It supports the Southern Water Use Caution Area (SWUCA) Management Plan and validates SWUCA II Rules implementation.

- **In scope**:
  - Track permitted and actual water use trends geographically and over time.
  - Support analysis of water use permits, compliance, and net benefit calculations.
  - Provide mapping, reporting, and querying capabilities for District staff and external users.
  - Integrate data from Regulatory, Water Management, and GIS databases.
  - Enable tracking of lapsed quantities, water withdrawal credits, and MFL impacts.

- **Out of scope**:
  - Changes to source DB2 mainframe systems and data structures.
  - Real-time data updates; relies on nightly replication.
  - Collection of new external data not already in District databases.
  - Development of new hardware or network infrastructure.
  - Water quality trend calculation and certain advanced estimation tools.

- **Roles and core use cases**:
  - As a **WUT Administrator**, I want to maintain system parameters and news so that users have accurate, up-to-date information.
  - As a **General WUT User**, I want to view maps and run reports so that I can analyze water use trends and permit data.
  - As a **Water Use Estimator**, I want to import and maintain water use estimates so that unmetered permits can be included in analyses.

- **Success metrics**:
  - Improved consistency and reliability of water use data and reporting.
  - Reduced staff time for manual tracking and analysis of water use trends.
  - Enhanced ability to validate and assess SWUCA Rule compliance and impacts.

- **Major constraints**:
  - Must use existing District hardware, software, and database architecture.
  - Dependent on nightly data replication from DB2 to Oracle.
  - Adherence to District development standards and change management processes.
  - Must support role-based security and web-based deployment.
  - Data accuracy and availability depend on source system updates and quality.

- **Undecided issues**:
  - Integration with adjacent water district GIS data layers.
  - Handling of real-time data requirements for certain use cases.
  - Specific implementation of certain Net Benefit and MFL mitigation tracking.
  - Metadata management and FGDC compliance details.
  - Not mentioned: Final user training rollout strategy and long-term system scalability plans.