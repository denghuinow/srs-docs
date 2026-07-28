**Purpose & Scope**
Pontis 5.0 is the next-generation Bridge Management System (BMS) for state highway agencies. It provides a central repository and analytical tools for managing bridge inventory, inspection data, preservation modeling, program simulation, and project planning. It is intended to replace the existing Pontis 4.x product line. The system does not include hosted application services, disaster recovery procedures, or support for non-Microsoft browsers as a guaranteed capability.

**Product Background / Positioning**
The system is the successor to the widely deployed Pontis 4.x BMS, owned by AASHTO. It must preserve agencies' existing investments in data, procedures, and training. It operates within the BRIDGEWare software suite and must integrate with other products like Virtis/Opis. Its development is influenced by ongoing national research projects (NCHRP 12-67, 20-64).

**Core Functional Overview**
1.  Browse, filter, and select bridge and project data, including via map-based queries.
2.  Create, edit, and manage bridge inventory records and inspection data.
3.  Develop and update preservation policy models (deterioration, costs) and perform Health Index targeting.
4.  Run network-level program simulations and individual bridge-level analyses.
5.  Create, edit, and manage programs and projects, assigning work items from various sources.
6.  Import and export data in standard formats (NBI, PDI, XML/TransXML).
7.  Perform system administration: user/role management, authentication, and application configuration.

**Key Users & Usage Scenarios**
*   **Inspectors:** Collect and enter field inspection data, often in disconnected environments.
*   **Bridge Management Engineers / Power Users:** Develop preservation models, run simulations, and perform advanced analysis.
*   **Project Planners:** Create and manage bridge projects and programs.
*   **Casual Users / Analysts:** Browse data, run predefined reports, and view maps.
*   **System Administrators:** Configure the application, manage users, and control security. Permissions and data access are role-based.

**Major External Interfaces**
*   **Database:** Supports Sybase Adaptive Server Anywhere, Oracle, and Microsoft SQL Server.
*   **GIS:** Must be GIS-aware and operate with standard systems (ESRI, Intergraph, Open GIS).
*   **BRIDGEWare:** Must integrate with other suite products (e.g., Virtis/Opis).
*   **Data Exchange:** Imports/exports via NBI, PDI, and XML (aligned with TransXML schema).
*   **Client:** Thin-client via Microsoft Internet Explorer; thick-client as a .NET Windows application.

**Key Non-functional Requirements**
*   **Performance:** Must support a database of 50,000 bridges. Login/logout within 2 seconds. Program simulation for 100 bridges in under 30 seconds.
*   **Reliability/Availability:** Target of 98% uptime during 18-hour daily, 353-day annual operating windows.
*   **Security:** Role-based application security. Must support single sign-on (e.g., Active Directory/LDAP) and database-level security.
*   **Maintainability:** Source code must be documented and deliverable. Must adhere to AASHTO development standards.
*   **Operational:** Server requires Windows Server 2003+, IIS, and .NET Framework. Thick-client requires Windows XP Professional+ and .NET Framework.

**Constraints, Assumptions & Dependencies**
*   **Technology Stack:** Must be developed using Microsoft .NET technologies (C#, ASP.NET, etc.).
*   **Database Design:** Changes must be reviewed/approved by the BRIDGEWare Database TAG.
*   **Compatibility:** Must maintain consistency with Pontis 4.x functionality and provide a migration path for existing databases.
*   **External Factors:** Must accommodate future changes to National Bridge Inventory (NBI) coding standards. Design informed by NCHRP Project 12-67 results.
*   **Deployment:** Assumes agency-managed server infrastructure; not a hosted solution.

**Priorities & Acceptance Approach**
The recommended implementation is a dedicated design followed by phased releases (Alternative 3). Priority is on delivering core functionality and a web inspection module first. Acceptance will be based on meeting the specified functional requirements, performance targets, and successful migration from Pontis 4.x. Formal Alpha and Beta releases will precede the final release.