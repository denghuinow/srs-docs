**Purpose & Scope**
The system, STEWARDS, is a centralized data portal to provide one-point access to standardized, well-documented water, soil, management, and economic data from multiple ARS research watersheds. It supports the CEAP watershed assessment studies and broader research. The system does not provide real-time data access; data is updated annually after local quality assurance. It does not replace local data management responsibilities at individual watersheds.

**Product Background / Positioning**
STEWARDS is a new system designed to consolidate and provide access to historically independent data from long-term USDA-ARS hydrologic research watersheds. It serves as the central repository for the CEAP project, linking data from up to 15 watersheds. It will utilize data from other agencies like NRCS and ERS and is intended to support agricultural models like SWAT and AnnAGNPS.

**Core Functional Overview**
1.  Store and manage diverse data types (biophysical, spatial, time-series, land use, economic).
2.  Allow users to browse, query, and download data and metadata by watershed, site, or topic.
3.  Provide tools to visualize time-series and spatial data in a geographic context.
4.  Support the upload of data from watershed sites using standardized formats and filters.
5.  Maintain a searchable metadata database compliant with federal standards (FGDC).
6.  Generate tabular reports and allow data export in standard formats (e.g., CSV, shapefiles).
7.  Provide user documentation, tutorials, and help desk support.

**Key Users & Usage Scenarios**
*   **System Operators & Data Managers (OCIO Staff):** Full system access for maintenance and archiving.
*   **Watershed Uploaders:** Local staff who write data for their specific watershed annually.
*   **ARS Researchers:** Authenticated users with access to all data, including sensitive agency data.
*   **Non-ARS Researchers:** Authenticated users with access to public data only.
*   **Public Users:** Unauthenticated access to publicly released data.
Typical scenarios include a researcher searching for and downloading specific water quality time-series data, or a watershed technician performing the annual data upload.

**Major External Interfaces**
*   **User Interface:** A web-based interface compatible with standard browsers (IE, Netscape, Firefox).
*   **Software Interfaces:** Uses standard ARS OCIO software resources (e.g., MS SQL Server, IIS, Apache).
*   **Hardware/Communications Interfaces:** Relies on ARS OCIO infrastructure at the Beltsville center, including network servers and T1 connections.

**Key Non-functional Requirements**
*   **Performance:** Query response times for metadata should be a few seconds. Retrieval of large datasets may take minutes to hours.
*   **Security:** Must implement authentication, confidentiality controls per user class, and data integrity validation. Follows ARS OCIO practices and policies.
*   **Availability:** The system must be available 24/7 with 99% uptime.
*   **Data Integrity:** Extensive QA/QC is required locally and during upload. Data is protected from unauthorized modification.
*   **Maintainability:** The database structure must allow for modification without a large overhaul.

**Constraints, Assumptions & Dependencies**
*   **Constraints:** Must use the corporate standard Microsoft SQL Server. Must comply with USDA accessibility, web design, and security policies. Client-side code must be platform-independent where possible.
*   **Assumptions:** Each watershed location will provide resources for data preparation and upload. The ARS OCIO operational platform in Beltsville will be available.
*   **Dependencies:** Partial funding is anticipated from NRCS through FY07. Continued operation depends on future funding from ARS base or discretionary funds.

**Priorities & Acceptance Approach**
The database management system is of the highest priority as the core component. Acceptance will be based on the system meeting the specified functional requirements for data storage, access, visualization, and download. User testing will validate that the interface is clear, complete, and consistent. System availability and performance metrics (e.g., query response times, 99% uptime) are key acceptance criteria.