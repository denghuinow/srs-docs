# Short Summary

- **Background and objectives**: This specification defines the System Administration Module for an Integrated Library System, aiming to replace and enhance current ILS capabilities for large, multi-branch library systems like King County Library System.
- **In scope**: System monitoring and performance dashboards; user and group account management; configuration and log file access; business rules for loans, holds, and data validation; backup, recovery, and job scheduling.
- **Out of scope**: Detailed data structures and user interface design; OPAC and web services modules; expanding on general ILS functionality; specific process workflows; non-administrative patron features.
- **Roles and core use cases**:
  - As a **System Administrator**, I want to monitor server and application performance so that I can ensure system reliability and troubleshoot issues.
  - As a **Staff member**, I want to run custom reports and queries so that I can analyze library operations and patron activity.
  - As a **Manager**, I want to configure business rules and staff permissions so that I can enforce library policies and control data access.
- **Success metrics**: Real-time processing of transactions and data; support for 50 locations and 20 million circulations; accessibility via web browsers and assistive technologies.
- **Major constraints**: Must use a relational SQL database; must run on Linux or Solaris servers; must produce standards-compliant HTML; must integrate with existing ILS modules; must support SNMP and secure protocols.
- **Undecided issues**: Specific user interface layouts; detailed data migration procedures; integration timelines with other modules; training environment setup details; vendor API compatibility details.