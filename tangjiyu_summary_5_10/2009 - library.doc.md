# Software Requirements Specification for System Administration of an Integrated Library System

## 1. Introduction

### 1.1 Purpose and Perspective
This document describes functional and non-functional requirements for the System Administration Module of an Integrated Library System (ILS). The requirements were developed specifically for King County Library System but are suitable for many large, urban, multiple-branch, centralized library systems.

The System Administration Module will replace and enhance current capabilities of commercially available ILSes, adding new functionality.

### 1.2 Product Scope and Features
The System Administration Module facilitates management of every aspect of the Integrated Library System, supporting:
- Configuring ILS to enable features for management of Library branches, patrons, collections, and circulation transactions
- Monitoring, troubleshooting, and controlling server performance
- Monitoring, troubleshooting, and controlling database and application performance
- Monitoring, troubleshooting, and controlling services, ports, and APIs
- Managing user and group accounts and privileges
- Managing server and client software installation, upgrades, and updates
- Backing up databases, configuration files, log files, etc.

### 1.3 Intended Audience
This document is intended for library managers and staff who may contribute additional requirements or commentary, and for software project managers and developers who will implement the requirements.

### 1.4 Operating Environment
- Support for large, multiple-branch library system (50 locations, 20 million circulations, 500,000+ items per year)
- Operation on Linux or Solaris server
- Accessibility through web-browser or Windows-compatible client
- Browser support: Microsoft Internet Explorer (v.6.0+) and Mozilla Firefox (v.2.0+)
- Compatibility with screen-reading software, screen-magnification software, and other accessibility programs

### 1.5 Design and Implementation Constraints
- Use fully relational database back-end
- Produce standards-compliant HTML
- Provide development and training environment with ability to migrate configurations to production
- Control user rights and privileges through security groups and/or "roles"

### 1.6 User Documentation
- Complete data specifications for all record types maintained/accessed by the System Administration Module
- High-level description of major processes
- Online, hierarchical, cross-linked help system in HTML describing all system functions

### 1.7 Assumptions and Dependencies
- Part of an enterprise-level Library Automation System
- System Administration processes consolidated at central location
- Interface with vendor websites via APIs and standard-format data files (USMARC21, EDIFACT)
- Interaction with patron interface (OPAC)

## 2. System Requirements

### 2.1 Systems: General
- SQL-based database with ability to run queries against any table and access as ODBC source
- Real-time processing for up-to-date pull lists, live shelf reading and weeding
- Field and record sharing allowing simultaneous access/update by multiple staff/patrons
- Record lock management to identify where records are in use
- Individual and shared staff login accounts with role-based access control
- System documentation specific to library and software version
- Access to all configuration files and log files
- Root shell access

### 2.2 Systems: Consoles and Dashboards
- Custom dashboard creation displaying system performance, record creation/modification, circulation transactions
- Full SNMP support for monitoring system resources (disk space, CPU load, memory load, processes, interfaces, ports)
- Configurable alert thresholds with notifications via dashboards, email, text messages
- Record lock administration with threshold setting and unlocking capability
- System performance dashboard showing processes with ID, owner, IP, CPU/memory utilization
- Server management console with software/server shutdown/restart utilities
- Application dashboard displaying backup status, system reboots, software versions, transaction queues, log sizes, record counts
- Client management console showing workstations running client software
- Circulation dashboard with key performance indicators
- Single console for configuration file access with read/write permissions by user/group
- Log-file dashboard for locating/viewing logs
- Job scheduling console for reviewing/controlling scheduled tasks
- Email configuration access with quick menu of common settings
- SMTP support for email transport

### 2.3 Systems: Business Rules
- Business rule restrictions (e.g., prevent deleting checked-out items or bibliographic records with holds)
- Customizable 'Rules of Suppression' specifying record visibility for patrons/staff in interfaces
- Requesting rules determining patron hold eligibility based on patron type, account balance, item type/status, etc.
- Loan rules allowing/disallowing check-out, calculating loan periods, determining renewal limits
- Data validation specifying default values, validation rules, automatic formatting, and required status for fields

### 2.4 Systems: Data Recovery
- Live incremental and full backup capabilities with support for third-party backup software (EMC NetWorker)
- Data rollback functionality with revision control for undo operations
- Server clustering for failover capability

### 2.5 Systems: Security
- Patron data security in all system transfers
- Full visibility and control of user privileges for system administrative staff
- Secure protocol support including SFTP, SSL, and SSH

### 2.6 Systems: Maintenance
- MARC bibliographic and authority record import/export (single/batch, all/selected fields)
- Unlimited record sets with batch import/export, batch field updates, query limiting, deletion with review/undo
- Dedicated interface for staff account creation with configurable templates and granular privileges
- Dedicated interface for patron account creation with configurable templates, field validation, required fields, defaults
- Job scheduling for maintenance tasks, reports, data exports with sequential execution
- Keyboard macros and shortcuts (administrator/user-programmable, centrally managed)

### 2.7 Systems: Client Management
- Staff/group accounts independent from workstations
- Centrally managed client software installation/updates using standard/proprietary network tools
- Server-based client configuration files with export/import between clients

### 2.8 Systems: Queries and Reports
- Fully customizable report layout/appearance with multiple output formats (CSV, Excel, printable)
- User-friendly query interface for all record types with field selection, picklists, regular expressions, Boolean operators
- Report templates created by administrators for front-line staff use
- Fine-grained permissions for specific reports and ad hoc queries
- Record number reports for all record types (current, deleted, purged counts)
- Support for four printer types (receipt, standard, label, forms) with all Windows printers
- Multiple print output options (file, ftp, email, printer) with field selection/order control
