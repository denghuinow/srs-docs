# Detailed Summary: Laboratory Information System (LIS) Rewrite

## Background and Scope
This project involves rewriting the core Laboratory Information System (LIS) to improve performance, ensure system integrity, and streamline workflows. The scope includes critical enhancements and defect fixes that burden users, along with architectural improvements to support business growth. Existing core functionalities will remain unchanged. Non-goals include implementing undocumented requirements and modifying functionalities outside the validated critical issues.

## Stakeholders Matrix and Use Cases
*   **CIO / Business & Technical Owner**: Final approver and overall business/technical owner of the project.
*   **IT Manager (QA/QC & Implementation)**: Oversees quality assurance, quality control, and implementation activities.
*   **Programmer Analyst / Project Manager**: Manages project development and provides subject matter expertise.
*   **Programmer Analyst / SME**: Provides subject matter expertise for system development.
*   **Sr. Business Systems Analyst**: Leads requirements analysis and validation.
*   **QA Analyst**: Executes testing procedures, including regression and user acceptance testing.
*   **Technical Writer**: Creates user documentation and online help system content.
*   **System Users (e.g., Admin)**: End-users who interact with the system to perform daily operations, such as user management.

**Main Use Case: Admin - Create/Add User**
1.  An admin navigates to the user management page and initiates adding a new user.
2.  The system validates the user does not already exist in the LIS and is active in Active Directory.
3.  The admin fills in required user information and associates at least one role, division, designator code, and lab location.
4.  The system saves the new user record with associated roles and permissions.
**Exception Scenario: Validation Failure**
1.  Admin attempts to save a user that already exists in the LIS.
2.  System displays an error message and prevents the save operation.
3.  Admin corrects the user information or cancels the operation.

## Business Process
**Main Process: User Account Creation**
*   **Trigger**: Admin requests to add a new user.
*   **Input**: New user details (User Name, Display Name), role assignments, division/lab associations.
*   **Output**: New user record saved in the database.
1.  Admin accesses the Admin module and selects "Add User".
2.  System displays the user creation form with required fields.
3.  Admin enters user information and assigns roles/divisions.
4.  System validates user against LIS database and Active Directory.
5.  Upon successful validation, system saves the new user record.
6.  System displays a confirmation message.
**Key Branch: Cancel Operation**
1.  Admin clicks "Cancel" during data entry.
2.  System clears entered data.
3.  System returns admin to the main Admin page.

## Domain Model
*   **User** (UserID: required/unique, UserName: required/unique, DisplayName: required, Status)
*   **Role** (RoleID: required/unique, RoleName: required, Permissions)
*   **Division** (DivisionID: required/unique, DivisionName: required)
*   **LabLocation** (LocationID: required/unique, LocationCode: required, Address)
*   **UserRole** (UserID: required/reference to User, RoleID: required/reference to Role)
*   **UserDivision** (UserID: required/reference to User, DivisionID: required/reference to Division)
*   **SystemLog** (LogID: required/unique, Timestamp: required, Severity, Message)
*   **HelpTopic** (TopicID: required/unique, Title: required, Content)

## Interfaces and Integrations
*   **Active Directory**: Direction: Outbound. Interaction: User status verification. Input: User credentials/identifier. Output: Active/Inactive status. SLA: Response time < 2 seconds for validation.
*   **SQL Server Database**: Direction: Bi-directional. Interaction: Primary data persistence for all entities. Input: CRUD operations. Output: Query results and persistence confirmation. SLA: 99.9% availability during business hours.
*   **Email System**: Direction: Outbound. Interaction: Send error notifications. Input: Error event details. Output: Notification email to Client Services distribution list. SLA: Email dispatched within 5 minutes of error.
*   **Online Help System**: Direction: Integrated. Interaction: Context-sensitive user assistance. Input: Help link selection. Output: Pop-up window with relevant help topic. SLA: Help page load < 3 seconds.

## Acceptance Criteria
**Capability: Create User from Template**
*   Given an admin user with appropriate privileges and a pre-defined user template,
*   When the admin selects to create a user from that template,
*   Then the new user record is populated with all role and setting defaults from the template.
**Capability: Mandatory Field Validation**
*   Given an admin is creating a new user and has not filled all required fields,
*   When the admin attempts to save the record,
*   Then the system displays an error message and prevents saving until all required fields are completed.

## Non-functional Metrics
*   **Performance**: Critical user-facing page response times under 3 seconds; batch process completion within defined time windows.
*   **Reliability**: System availability target of 99.5%; scheduled downtime limited to defined maintenance windows (e.g., Tuesdays 7 PM - 7 AM).
*   **Security & Compliance**: Maintain full HIPAA compliance for data security and confidentiality; all new code must adhere to defined security standards.
*   **Observability**: All errors, warnings, and informational messages must be logged to an external application server log file.

## Milestones and Release Strategy
1.  Requirements gathering and validation sign-off.
2.  Completion of Admin module development and internal testing.
3.  User Acceptance Testing (UAT) for the first release bundle.
4.  Technical owner sign-off for production deployment.
5.  First production release (focused on critical fixes and Admin module).
6.  Subsequent iterative releases for remaining modules/enhancements.

## Risk List and Mitigation Strategies
1.  **Scope Creep**: Mitigation: Strict adherence to validated requirements document; change requests require formal approval.
2.  **Integration Issues with Active Directory**: Mitigation: Early prototyping and testing of the authentication/validation interface.
3.  **Insufficient UAT Time**: Mitigation: Allocate dedicated UAT period in project schedule and involve business stakeholders early.
4.  **Performance Degradation**: Mitigation: Conduct performance benchmarking early and integrate performance testing into the QA cycle.
5.  **Non-compliance with HIPAA**: Mitigation: Include security and compliance checkpoints in the development and code review process.

## Undecided Issues and Responsible Parties
1.  Final list of all modules to be included in the rewrite (CIO / Project Manager).
2.  Detailed definition of "critical" severity level for defects and enhancements (Business Owner / Sr. Business Analyst).
3.  Specific performance benchmarks for each module (Technical Lead / QA Manager).
4.  Complete mapping of all existing interfaces to be retained or modified (Technical Lead / Development Team).