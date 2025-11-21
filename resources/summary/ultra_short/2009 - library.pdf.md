Purpose & Scope  
This system admin module manages the Integrated Library System (ILS) for large, multi-branch libraries, enabling configuration, monitoring, and maintenance of core ILS functions. It excludes patron-facing services (e.g., cataloging, circulation) and assumes existing ILS data structures.  

Product Background  
Part of an enterprise library automation system, it consolidates administration for King County Library System (50+ branches, 20M annual circulations) and interfaces with Acquisitions, Cataloging, and OPAC modules.  

Core Functional Overview  
- Configure ILS features for branches, patrons, collections, and circulation.  
- Monitor and troubleshoot server, database, and application performance.  
- Manage user accounts, privileges, and security groups.  
- Perform database backups, recovery, and data rollback.  
- Customize dashboards for system performance and circulation metrics.  
- Define business rules for records, holds, and loans.  

Key Users & Usage Scenarios  
System Administrators (full access) manage servers, data, and security. Library Managers (limited access) configure business rules and reports. Staff access basic dashboards for operational data under admin-defined permissions.  

Major External Interfaces  
Interfaces with OPAC, vendor APIs (USMARC21, EDIFACT), and client management systems. Supports web-browser (IE 6.0+, Firefox 2.0+) and Windows-compatible clients.  

Key Non-functional Requirements  
Support 50+ branches, 20M annual circulations, and 500K+ annual item acquisitions. Operate on Linux/Solaris. Provide screen-reader accessibility. Ensure real-time circulation data updates. Support SFTP/SSL/SSH for secure data transfers.  

Constraints, Assumptions & Dependencies  
Must use relational SQL database. Requires enterprise ILS data structures. Relies on Acquisitions/Cataloging modules. Depends on vendor APIs for external data exchange.  

Priorities & Acceptance Approach  
Priority 2: Report format customization. Priority 3: All other requirements. Acceptance requires meeting all scope, performance, and security constraints without exceeding defined scale limits.