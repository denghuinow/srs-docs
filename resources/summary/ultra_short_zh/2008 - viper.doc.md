Purpose & Scope  
System solves Ejada’s internal supply chain management needs for customer/supplier coordination, procurement, and item tracking. Excludes external integration with ERP systems like SAP. Scope limited to Ejada’s operational workflow, not enterprise-wide deployment.  

Product Background  
Sits within Ejada’s internal .NET framework as a dedicated SCM module. Integrates with two existing Ejada modules but does not interact with external CRM or HR systems.  

Core Function Overview  
- Manage customer/supplier information (add, edit, delete)  
- Handle customer/supplier requests (create, view, edit, delete)  
- Track items and resources (locations, inventory)  
- Coordinate procurement and supply chain workflows  
- Maintain performance metrics (cost, quality, productivity)  

Key Users & Scenarios  
Primary users: Ejada coordinators (manage all entities), customers (submit requests), suppliers (respond to requests). Coordinators perform bulk operations; customers/suppliers handle request-specific actions.  

Major External Interfaces  
Web-based UI (no hardware dependencies). Communicates via TCP/IP over internet. Requires IE 6/7 or Firefox 2/3 browsers. Integrates with Ejada’s .NET framework modules.  

Critical Non-Functional Requirements  
- Must handle 100+ concurrent users with 90% transactions <1 second  
- 100% uptime availability  
- Role-based access (coordinator/customer/supplier only)  
- Daily automated data backup  

Constraints, Assumptions & Dependencies  
Must use .NET 3.5 (ASP.NET/C#), MS SQL DB. Requires Ejada’s framework and two integrated modules. Assumes server runs supported Microsoft OS with internet access.  

Priority & Acceptance  
Top priority: Request/Item/Supplier/Customer management (Release 1.0). Acceptance: All core CRUD functions meet performance thresholds (response times, concurrency). No external system integration required.