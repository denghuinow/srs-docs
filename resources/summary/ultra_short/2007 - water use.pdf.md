Purpose & Scope: The system is a GIS-based tool to track and analyze geographic and temporal trends in permitted and actual water use within the Southern Water Use Caution Area (SWUCA). It supports validation of SWUCA II Rules implementation and replaces current manual/semi-automated tracking methods. It does not handle manual data collection or provide new data collection capabilities.

Product Background / Positioning: The system integrates data from existing District databases (Regulatory Database, GIS, Water Management Database) to provide a unified water use tracking solution. It serves as the primary tool for SWUCA Management Plan implementation and aligns with the CWM Information Technology initiative.

Core Functional Overview: Track lapsed quantities and relocation of water use permits; view water use permits with spatial and temporal analysis; monitor net benefit changes from water use modifications; track minimum flows and levels impacts; view compliance information and water withdrawal credits; generate well packages for groundwater modeling; analyze water use trends by geographic area.

Key Users & Usage Scenarios: Water Use Permit Evaluators (review permits and impacts), Technical Services Staff (track long-term water use trends), Resource Conservation Staff (support groundwater modeling), Planning Department (analyze demographic impacts), Executive Staff (access standard reports), External Customers (view public water use data).

Major External Interfaces: Integrates with IBM DB2 (Regulatory Database), HP-UX ArcSDE/Oracle (GIS), and Water Management Database. Requires Web/ArcIMS servers for public access and maintains existing desktop workstation environment.

Key Non-functional Requirements: Must support daily data replication between DB2 and Oracle systems. Must provide consistent, reliable query results over time. Must allow customizable queries with reasonable web application refresh rates. Must be user-friendly with consistent decision-making support.

Constraints, Assumptions & Dependencies: Depends on current RDB, GIS, and WMDB systems remaining available during development. Assumes data collection changes will be made within existing systems. Must be developed within current District software development environment.

Priorities & Acceptance Approach: Initial release focuses on SWUCA implementation. Subsequent releases may include additional features. Acceptance based on completion of critical use cases and requirement traceability matrix coverage.