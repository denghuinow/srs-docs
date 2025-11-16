# Balanced Summary

**Goals and scope**  
This project aims to rewrite the core Laboratory Information System (LIS) to improve performance, automate decisions, and streamline workflows. The scope is limited to critical enhancements and defects that burden users, plus architectural improvements for efficient growth. Existing core functionalities will remain unchanged.

**Roles and user stories**  
- *Admin*: I want to create/add new users and assign roles so that system access is properly managed.  
- *Admin*: I want to use user templates for creating accounts so that role settings are inherited consistently.  
- *User*: I want to access context-sensitive online help so that I can resolve issues without external support.  
- *Developer*: I want to follow defined coding standards so that the system remains maintainable.  
- *QA Analyst*: I want to perform regression testing on scheduled builds so that system reliability is ensured.

**Key processes**  
1. (Trigger: User action) The system displays operational pages when users select hyperlinks from the main menu.  
2. (Trigger: Admin action) Admin creates a new user manually or from a template, associating roles and divisions.  
3. (Trigger: Save action) System validates user existence in Active Directory and saves user data with roles.  
4. (Trigger: Weekly schedule) Development team performs weekly integrations and deploys updates to staging.  
5. (Trigger: Build deployment) QA team conducts regression testing before production release.  
6. (Trigger: Error occurrence) System logs errors to external files and notifies Client Services via email.  
7. (Trigger: User request) Help system displays contextual assistance in pop-up windows with navigation features.

**Domain data elements**  
- *User*: UserID (PK), UserName, DisplayName, Status, Roles, Divisions  
- *Role*: RoleID (PK), RoleName, Permissions, Description  
- *Division*: DivisionID (PK), DivisionName, Code, LabLocation  
- *UserTemplate*: TemplateID (PK), TemplateName, DefaultRoles, Settings  
- *ErrorLog*: LogID (PK), Timestamp, ErrorMessage, UserID, Severity  
- *HelpTopic*: TopicID (PK), Title, Content, Category, Keywords

**Non-functional requirements**  
- System must maintain HIPAA compliance in all functionality  
- Production updates scheduled only on Tuesdays between 7pm-7am  
- Use .NET 3.5 platform with SQL Server 2008 database  
- Implement consistent coding and maintainability standards  
- Provide online help system with search and navigation capabilities  
- Log errors to external files and email notifications for critical errors

**Milestones and external dependencies**  
- Requirements validation sessions completion  
- Weekly integration builds to staging environment  
- User Acceptance Testing (UAT) before production deployment  
- Technical owner signoff for production releases  
- Active Directory integration for user validation

**Risks and mitigation strategies**  
- Scope creep: Strict adherence to documented requirements only  
- Integration issues: Weekly builds and regression testing  
- Compliance violations: Maintain HIPAA capabilities in all new functionality  
- User adoption: Early UI mockup demonstrations to stakeholders  
- Maintenance complexity: Consistent coding standards and external logging

**Undecided issues**  
- Specific module development priorities and sequence  
- Detailed UI design specifications  
- Comprehensive error message catalog  
- Performance benchmarks and targets  
- Backup and disaster recovery procedures  
- Training requirements and rollout strategy