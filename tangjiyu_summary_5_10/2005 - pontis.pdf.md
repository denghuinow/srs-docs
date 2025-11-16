# Pontis 5.0 Bridge Management System - Functional Requirements

## 1. Introduction
Pontis 5.0 is the next generation of the Pontis Bridge Management System (BMS), providing licensing agencies with an up-to-date tool for bridge management including data management, condition assessment, model development, needs analysis, reporting, and interaction with other agency systems. It will replace the existing Pontis 4.x product line with a next-generation software application utilizing state-of-the-art software development technology while preserving licensee investments in Pontis 4.x implementation.

The system will support import and export of data in XML based on the TransXML schema, improved modeling approaches through NCHRP 12-67 research results, enhanced user interfaces for bridge-level analysis and project planning, and support for multiple asset types. It will provide seamless support for potential changes in National Bridge Inventory (NBI) coding standards.

## 2. Project Drivers

### 2.1 Purpose of the Product
Key goals for Pontis 5.0 include:
- A readily-accessible, robust repository for bridge information (inventory, condition, needs, project plans, accomplishments)
- Technically correct capabilities for all bridge management tasks
- Technologically up-to-date development foundation using .NET, web services, SOAP, XML, Model-View-Controller architecture
- Streamlined, simpler application and deployment mechanisms
- Flexible, customizable application that users can extend for agency-specific tasks
- Preservation of significant agency investments in BMS and Pontis specifically

### 2.2 Stakeholders
Key stakeholders include:
- Pontis Users (power users, routine users, casual users)
- Pontis Task Force (product quality, technical correctness, oversight)
- Technical Advisory Group (TAG) (requirements development, architecture, implementation)
- BRIDGEWare Integration TAG (integration impacts assessment)
- AASHTO (product quality, project management, licensing)
- Contractors (software development)
- Agencies (procurement, operation)

### 2.3 Users of the Product
- Inspectors (bridge data collection, review, database quantification)
- Bridge project planners (development, review, approval, tracking of bridge work)
- Bridge management engineers (inspection program, program development, policies)
- Bridge design/rating engineers (engineering decisions, structure design information)
- Highway information analysts (data collection for bridge management)
- Highway program planners (integration of project plans, corridor management)
- Other Pontis users (executives, public relations, engineering firms, casual users)

### 2.4 Project Constraints
- Development using Microsoft technologies (.NET application with stand-alone, thin client, and server components)
- Thin client designed for latest Microsoft Internet Explorer
- Stand-alone application requires .NET Runtime Framework and Windows XP
- Server application requires .NET Framework and common language runtime
- Visual Studio .NET as primary development tool
- Maximize use of third-party code libraries to minimize development costs
- Thin-client available via internal network and Internet as appropriate
- Take full advantage of web display capabilities
- Database design consistent with Pontis 4.4 with changes reviewed by BRIDGEWare Database TAG
- Support existing RDBMS (Sybase, Oracle, Microsoft SQL Server)
- GIS-aware application operating within ESRI, Intergraph, Open GIS technologies
- Accommodate both disconnected and connected users

## 3. Use Cases

### 3.1 Browse Bridge & Project Data
- View bridge data with find, filter, and select capabilities including map-based queries
- View project data with find, filter, and select capabilities including map-based queries
- Select and view predefined reports
- Select and view Pontis information using maps

### 3.2 Bridge Inventory & Inspection
- Create/edit structures (new structure, copy existing, import from file)
- Create/edit inspections (new inspection, copy previous, import PDI file)
- Calculate dependent/derived inspection results (NBI condition ratings, structural rating, geometric rating, sufficiency rating, SD/FO status)
- Add/edit elements, notes, work recommendations
- Inspection scheduling and planning
- Multimedia file linking and management
- Inspection record locking once signed/sealed

### 3.3 Preservation Model Development
- Develop preservation policy (update deterioration probabilities, preservation action costs)
- Perform health index targeting (determine long-term cost of meeting average health index target)

### 3.4 Program Simulation
- Configure simulation parameters (timeframe, thresholds, project types, needs, annual budget)
- Perform program simulation (run simulation for selected structures)
- Perform bridge analysis (view impact of work items on structure condition)

### 3.5 Project & Program Development
- Create/edit programs (manual entry, edit/delete existing)
- Create/edit projects (manual entry, edit/delete existing, assign work recommendations)
- Split/combine projects
- Batch update multiple projects

### 3.6 Data Management
- Perform data validation (single-field, cross-field, configurable input range checks)
- Exchange data (NBI, PDI, XML formats with TransXML schema)
- Perform data archiving (archive data for existing and removed structures)
- BRIDGEWare integration support (database integration, load rating data transfer)

### 3.7 System Administration
- Define and manage user roles (create/edit roles, assign permissions)
- Manage application users (add users, modify profiles, assign access filters)
- Perform user authentication (validate credentials, authorize access)
- Configure application functionalities (units of measure, DATADICT table, field security)
- Configure user-interface presentation (labels, internationalization)
- Administration functionalities (external service interface, override check-out status)

## 4. Functional Requirements

### 4.1 Browse Data
- View data in Physical Inventory tables through GUI
- Switch between predefined structure lists
- Select structures by ID, district, county, administrative area, ownership, custodianship, functional class, NHS status, inspector, bridge group, inspection due dates
- Find structures by ID, name, feature intersected, facility carried, route number, LRS Inventory Route, KM/mile posts
- Enter SQL WHERE clause for queries
- Select structures by typing structure ID directly
- Display data in appropriate unit of measurement
- Select bridges on map display for lists

### 4.2 Bridge Inventory & Inspection
- Create new structures with user-defined bridge key
- Create structures by copying existing structure data
- Create structures by importing from supported file types (PDI, NBI, XML)
- Edit and remove existing structures
- Mark bridges with status values (inactive/closed) with automatic filtering
- Support storage for bridges in design/preconstruction state
- Renumber bridge key identifier with global change
- Create/edit inspection data with short-form interface
- Copy notes from previous inspections
- Add/edit elements, NBI data, element inspection data
- Edit inspection and structure notes with plain text/XML storage
- Create/edit work recommendations with quantity estimation
- Inspection scheduling tool
- Compare two inspections in tiled presentation
- Configurable tracking mechanism for reviewed/approved screens

### 4.3 Preservation Model Development
- Create cost and deterioration elicitation records
- Update transition probabilities based on expert elicitations
- Update preservation action costs based on expert elicitations
- Update transition probabilities for do-nothing actions based on historical data
- Edit cost and deterioration models through GUI with immediate impact visualization
- Develop optimal preservation policy using transition probabilities and costs
- Recover model if elicitation process fails
- Restore previous action costs, transition probabilities, and preservation policy
- Support multiple cost and deterioration models
- Incorporate Health Index targets in preservation model
- Streamline model generation process

### 4.4 Program Simulation
- Specify simulation characteristics (timeframe, thresholds, project types, needs, annual budget)
- Update unit costs and policy standards governing improvement model
- Modify technical parameters governing simulation
- Select structural elements included in simulation
- Dynamically determine bridge subsets as scenario settings
- Run program simulation for selected structures
- Choose from work recommendations for bridge simulation
- Run bridge analysis for single structure
- Bridge Analysis Dashboard for work item selection and timing

### 4.5 Project & Program Development
- Create/edit programs manually
- Create/edit projects manually
- Assign work recommendations to projects
- Split projects into multiple projects
- Combine multiple projects into master project
- Edit characteristics of multiple projects simultaneously
- Track and link funding levels and project budgets
- Group work candidates by action types

### 4.6 Data Management
- Perform single-field and cross-field validation on NBI data
- Perform configurable input range checks using DATADICT table
- Perform data validation including cross-field validation upon saving
- Configure data validation rules
- Data review wizard for comparing incoming with existing data
- Guarantee atomic database transactions for data integrity
- Maximize multi-user concurrency and conflict resolution
- Exchange data in NBI, PDI, and XML formats
- Designate recipient for checked-out bridges
- Store export/import control information within database
- Archive data for existing and removed structures
- Provide reporting mechanism for viewing archived data
- Restore archived data
- Use timestamps to log when rows were last changed
- Continue existing application integration with BRIDGEWare products

### 4.7 System Administration
- Create/edit application roles and assign users
- Manage application roles through user interface
- Assign application permissions to user roles
- Add/remove users and modify account profiles
- Create bridge-level access filters
- Validate user name and password during login
- Authorize access based on user privileges
- Track login and logout activity
- Support concurrent sessions for users
- Support Windows Authentication mechanism
- Integrate authentication with BRIDGEWare
- Operate with single-sign-on authentication
- Configure system units of measure (English/metric)
- Store INI file configuration in database or registry
- Edit DATADICT table through GUI
- Add/configure pre-populated new structure templates
- Configure field-level security and mandatory fields
- Configure dropdown list values
- Create agency-specific elements and definitions
- Add custom structure and project lists
- Configure default scenario parameters
- Adhere to .NET logging and exception handling standards
- Support internationalization using Windows/.NET standards

## 5. Non-Functional Requirements

### 5.1 Look and Feel
- Conform to W3C design guidelines and industry practices
- Clearly identify product name, licensee, user, and developer
- Professional and conservative appearance
- Consistent with other AASHTOWare/BRIDGEWare applications

### 5.2 Usability
- Straightforward and intuitive design familiar to existing users
- Effective navigation, visual referencing, and task sequencing
- Online help throughout UI
- Consistent look and feel in web and standalone environments
- Users comfortable after two days training, data viewers after two hours
- System administrators comfortable after one day administration training
- Support existing custom forms and reports

### 5.3 Performance
- Repository capacity: 50,000 bridges, 30 inspections per bridge, 50,000 projects
- Simultaneous read-write users: 25 (web), 10 (standalone)
- Simultaneous view-only users: 150
- Login/Logout: <2 seconds
- Desktop redisplay: 5-10 seconds
- Create new bridge record: <3 seconds
- Export 50 bridges: <30 seconds
- Import 50 bridges: <30 seconds
- Retrieve/display single bridge detail: <2 seconds
- Validate 50 bridges for NBI edit check: <10 seconds
- Generate formatted report: 10-20 seconds
- Available 18 hours/day, 353 days/year with 98% uptime

### 5.4 Operational
- Server runs Windows Server 2003 or successor with ASP.NET
- Database co-located or accessible via standard protocols
- Support Internet Explorer primarily
- Standalone capabilities require latest .NET Framework
- Sybase Adaptive Server Anywhere release 9 or above for offline work

### 5.5 Installation and Deployment
- Installer program for user computers
- Remove via Windows Add/Remove Programs
- Upgrade scripts for database versions
- Coexist with earlier Pontis versions

### 5.6 Maintainability and Portability
- Comply with AASHTO application development standards
- Use latest Microsoft tools and databases
- Provide all source code to AASHTO with clear documentation
- Support automatic testing with driver modules
- Provide online and printed documentation
- Support through telephone, email, and online issues tracking

### 5.7 Security
- Mix of database and application security
- Single sign-on approach with declarative security management
- Database security through specific username/password combinations
- Application level security consistent with Pontis 4.x procedures
- Limited configurability for normal users

### 5.8 Cultural and Political
- Design for agency/international localization
- Support native language for UI elements, reports, messages

### 5.9 Legal
- Export NBI data in specified format
- Support future NBI coding guide changes

## 6. Implementation Plan
Three alternatives considered:
1. Dedicated Design and Release (complete product delivered at single point)
2. Phased Design and Release (components delivered serially with web inspection focus)
3. Dedicated Design and Phased Release (dedicated design followed by phased development)

Recommended approach: Alternative 3 (dedicated design and phased release) aligning with revenue cycles, allowing formal design review, and making key components available relatively quickly.

## 7. Risk Analysis
Major risks include requirement creep, technology obsolescence, development cost/schedule overruns, resource risks, NBI changes, agency custom forms migration, Pontis 4.x maintenance costs, and user satisfaction.
