**Purpose & Scope**  
The system replaces and enhances Evergreen ILS management capabilities for PINES, a statewide Georgia library network serving 275+ libraries. It enables analysis of collections, demographics, inventory, patron records, transactions, and financials. It excludes acquisitions, cataloging, and OPAC functionality.  

**Product Background / Positioning**  
PINES operates a centralized library consortium using Evergreen ILS. This management layer extends Evergreen’s core to support enterprise-level reporting and analytics across all 286 PINES locations. It integrates with existing Acquisitions and Cataloging modules.  

**Core Functional Overview**  
- Report templates with configurable permissions and field restrictions.  
- Query tool supporting Boolean operators, picklists, and field-level access control.  
- Demographic analysis of patron behavior and geographic/age-based statistics.  
- Inventory reports for material volume, shelf space allocation, and item status tracking.  
- Financial reporting for item valuation, fines, and audit-compliant transactions.  

**Key Users & Usage Scenarios**  
Global System Administrators manage system-wide reports and configurations. Library Managers generate branch-level analytics for collection planning. Staff run ad hoc reports for circulation or inventory tracking. Permissions restrict report creation, template modification, and data access by user role.  

**Major External Interfaces**  
Interfaces with OPAC for patron data, vendor APIs (USMARC21, EDIFACT) for external data, and Acquisitions/Cataloging modules for core library data. All interfaces use standardized data formats.  

**Key Non-functional Requirements**  
Reports must process during open hours without disrupting system operations. System must support Linux/Solaris servers, web browsers (IE 6.0+, Firefox 2.0+), and accessibility tools. Output formats include HTML, Excel, and CSV.  

**Constraints, Assumptions & Dependencies**  
Requires relational database backend and standards-compliant HTML. Depends on existing Evergreen ILS data structures and Acquisitions/Cataloging modules. Excludes OPAC module functionality.  

**Priorities & Acceptance Approach**  
All requirements are Priority 1. Acceptance requires validated report outputs matching predefined templates (e.g., demographic statistics, financial audits) and permission controls as specified in requirements.