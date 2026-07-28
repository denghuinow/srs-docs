**Purpose & Scope**
The system is a rewrite of the core Laboratory Information System (LIS) to improve performance, ensure reliability, and meet regulatory standards. The scope is limited to implementing critical enhancements and defects, and validated functional requirements gathered in specific sessions. It does not include changes to existing core functionalities unless they are modified to implement a new requirement.

**Product Background / Positioning**
This is a re-write and enhancement of an existing Laboratory Information System (LIS) for the company. The system is a core business application that must integrate with the company's Active Directory for user authentication and relies on a single SQL Server 2008 database.

**Core Functional Overview**
*   Administer user accounts, including creating new users and associating them with roles and divisions.
*   Integrate user authentication with the company's Active Directory.
*   Provide context-sensitive online help accessible from every screen.
*   Log system errors, warnings, and informational messages to an external file.
*   Send email notifications for specific system errors.
*   Maintain existing HIPAA compliance in all functionality.

**Key Users & Usage Scenarios**
Primary users are laboratory system users and administrators. Administrators have privileges to create and manage user accounts, associating them with specific roles, divisions, and locations. A typical scenario involves an administrator adding a new lab user, with the system validating the user against Active Directory and the existing user database.

**Major External Interfaces**
The system interfaces with the company's Active Directory for user status verification. It uses a single SQL Server 2008 database. It must send notification emails to a specified distribution list.

**Key Non-functional Requirements**
*   The system must log all errors, warnings, and informational messages to an external log file.
*   Production updates can only be scheduled for specific weekly maintenance windows (e.g., Tuesdays 7pm-7am).
*   All new and modified functionality must comply with HIPAA standards.
*   The development must use the .NET 3.5 platform and established open-source frameworks where appropriate.

**Constraints, Assumptions & Dependencies**
*   Development is constrained to the .NET 3.5 platform and a single SQL Server 2008 database.
*   The system depends on the company's Active Directory.
*   A formal Technical Owner sign-off is required for any production deployment.
*   The project assumes development will proceed module-by-module based on validated requirements.

**Priorities & Acceptance Approach**
Priority is given to critical defects and enhancements that cause user burden or facilitate efficient system growth. Acceptance requires formal User Acceptance Testing (UAT) prior to production deployment, regression testing of all builds, and final sign-off by the Technical Owner.