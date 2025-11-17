# Balanced Summary

**Goals and Scope**  
Pontis 5.0 is the next-generation Bridge Management System designed to replace Pontis 4.x, providing a robust repository for bridge data, condition assessment, and program simulation. It aims to modernize the technology foundation while preserving existing agency investments and supporting integration with other systems via TransXML. The system will offer both web-based and standalone client applications to accommodate varied user environments.

**Roles and User Stories**  
- *Inspector*: I want to enter and edit inspection data so that bridge conditions are accurately recorded and maintained.  
- *Bridge Management Engineer*: I want to develop preservation policies so that optimal maintenance strategies can be implemented.  
- *Project Planner*: I want to create and manage bridge projects so that work recommendations are effectively planned and funded.  
- *System Administrator*: I want to configure user roles and permissions so that system access is securely managed.  
- *Data Analyst*: I want to run program simulations so that long-term network trends and budget needs can be analyzed.

**Key Processes**  
1. *Trigger: User login* – Authenticate user and load applicable data based on role permissions.  
2. *Trigger: New inspection scheduled* – Create or copy inspection records and collect field data.  
3. *Trigger: Data entry/update* – Validate inventory and inspection data against rules.  
4. *Trigger: Model update request* – Calculate deterioration probabilities and preservation action costs.  
5. *Trigger: Simulation initiation* – Run program or bridge-level analysis using configured parameters.  
6. *Trigger: Project creation* – Assign work items to projects and allocate funding.  
7. *Trigger: Data export request* – Generate reports or export data in NBI, PDI, or XML formats.

**Domain Data Elements**  
- *Bridge*: Key: Structure ID; Fields: Location, Design Type, Inspection History, Element Data, Status  
- *Inspection*: Key: Inspection ID; Fields: Date, Inspector, Condition Ratings, Work Recommendations, Notes  
- *Project*: Key: Project ID; Fields: Program, Budget, Work Items, Status, Funding Source  
- *Preservation Policy*: Key: Policy ID; Fields: Action Costs, Deterioration Probabilities, Health Index Targets  
- *User*: Key: User ID; Fields: Role, Permissions, Contact Info, Authentication Data  
- *Simulation Scenario*: Key: Scenario ID; Fields: Timeframe, Budget, Parameters, Results

**Non-Functional Requirements**  
- Support for 50,000 bridges and 500 users with 98% uptime.  
- Web and standalone clients using .NET Framework and compatible RDBMS (e.g., SQL Server, Oracle).  
- User interface must be intuitive, with core proficiency achievable within two days of training.  
- Data export/import in NBI, PDI, and TransXML formats.  
- Adherence to AASHTO development standards and integration with BRIDGEWare products.  
- Configurable security roles and field-level data access controls.

**Milestones and External Dependencies**  
- Finalize Pontis 5.0 design document by June 2006.  
- Deliver web inspection module by June 2007.  
- Complete integration with TransXML schemas (dependent on NCHRP Project 20-64).  
- Coordinate database changes with BRIDGEWare Technical Advisory Group.  
- Align development with NCHRP 12-67 research on multi-objective optimization.

**Risks and Mitigation Strategies**  
- *Scope creep*: Manage through approved requirements document and change control.  
- *Technology obsolescence*: Use phased development to incorporate emerging .NET updates.  
- *Budget/schedule overruns*: Apply COSMIC-FFP estimation and modular delivery.  
- *User dissatisfaction*: Engage users via prototypes and early module releases.  
- *NBI coding changes*: Design flexible data structures to accommodate future standards.

**Undecided Issues**  
- ADA compliance implementation approach.  
- Support for handheld/tablet devices in field inspections.  
- Migration path for custom PowerBuilder forms and reports.  
- Third-party GIS integration specifics.  
- Electronic signature standards for inspection records.  
- Hosting strategy for web application components.