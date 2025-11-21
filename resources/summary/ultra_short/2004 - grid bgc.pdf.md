Purpose & Scope  
The system enables scientists to run bio-geochemical modeling via Daymet weather interpolation and BiomeBGC simulations. It manages input data, project workflows, and output results through a web portal. Excludes direct data publication, visualization, and analysis tools (marked low priority).  

Product Background / Positioning  
Built on NCAR’s grid infrastructure to integrate with existing NCAR Mass Storage System (MSS) and Gatekeeper authentication. Serves as the primary platform for scientific modeling workflows within NCAR’s research ecosystem.  

Core Functional Overview  
- Daymet and BiomeBGC modeling runs with input data management  
- Project-based organization linking inputs to simulation outputs  
- Data download of model results in native formats  
- User account management via NCAR Gatekeeper integration  
- Portal administration for system monitoring and resource control  

Key Users & Usage Scenarios  
Primary: Scientists (run models, manage projects). Secondary: Portal Administrators (manage users, system resources). Data Users (lowest priority; only download pre-generated outputs).  

Major External Interfaces  
Web portal accessible via IE 6.0 and Netscape 7.1. Integrates with NCAR Mass Storage System (MSS) for data storage. Requires browser cookies.  

Key Non-functional Requirements  
- Must use Globus toolkit for grid communications  
- Must comply with NCAR Security policies  
- Must store all files via NCAR Mass Storage System  
- Browser compatibility: IE 6.0, Netscape 7.1  

Constraints, Assumptions & Dependencies  
Mandatory Globus toolkit usage. NCAR Security policies govern all implementations. NCAR Mass Storage System (MSS) required for all file storage.  

Priorities & Acceptance Approach  
Scientists’ modeling needs are highest priority. Portal administrators’ system management is mid-priority. Data Users’ access is lowest priority. Acceptance requires functional modeling runs, data download, and account management per specified constraints.