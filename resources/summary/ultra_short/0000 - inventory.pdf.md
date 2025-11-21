**Purpose & Scope**  
The system integrates three faculty databases into a unified web interface for inventory management. It handles asset transfers, requests, and reporting within the university. Excludes external system integration and non-university access outside working hours.

**Product Background / Positioning**  
Serves as the central inventory platform for all university faculties, replacing fragmented faculty-level systems. Interfaces with existing faculty databases but requires no external system modifications.

**Core Functional Overview**  
- Asset transfer with multi-level approval (department, faculty, university)  
- Request management for borrowing assets or reserving spaces  
- Asset editing/modifying (excluding IDs) and bulk additions  
- Report generation (asset location, requests, user permissions)  
- Role-based permission delegation across administrative levels  

**Key Users & Usage Scenarios**  
Level 0 (students/professors): Create requests only.  
Levels 1-3 (department/faculty/university admins): Manage assets, locations, and approve requests.  
Level 4 (IT): Full system control, permission configuration, and database maintenance.  

**Major External Interfaces**  
Web-based user interface accessible via standard browsers. Integrates with existing faculty databases for data synchronization. No external API dependencies for core functions.

**Key Non-functional Requirements**  
- Usability: Maximum 4-hour learning time for new users.  
- Availability: 24/7 during university working hours; maintenance outside these hours.  
- Security: Role-based access control with username/password authentication.  
- Reliability: Queries terminate after 1 minute; automated backups.  

**Constraints, Assumptions & Dependencies**  
Requires university working hours for all user access. Assumes faculty databases support integration. Depends on IT team for server maintenance and permission configuration.  

**Priorities & Acceptance Approach**  
Critical: Asset transfer, request approval, and security.  
Acceptance: System must support all administrative levels’ permission workflows and generate required reports without errors.