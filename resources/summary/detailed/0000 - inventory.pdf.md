# Detailed Summary: Unified University Inventory System (UUIS)

## Background and Scope
The Unified University Inventory System (UUIS) is a web-based application designed to integrate inventory management across three university faculties (Arts & Science, Computer Science, Engineering). It provides centralized control over assets (rooms/spaces, software licenses, other assets), enables request workflows for borrowing/reserving, and supports hierarchical administrative permissions. The system must be accessible during working hours with secure external access. Non-goals include replacing existing faculty databases entirely (integration focus), mobile application development, and real-time inventory tracking sensors.

## Stakeholders Matrix and Use Cases
*   **University Administrator (Level 3):** Oversees all university inventory and approves inter-faculty/outside-university transfers.
*   **Faculty Administrator (Level 2):** Manages inventory within their faculty and approves inter-departmental transfers.
*   **Department Administrator (Level 1):** Controls department-level inventory and approves internal transfers.
*   **Inventory Administrator (Delegated):** Performs specific inventory tasks (add, modify, approve requests) as delegated by higher-level administrators.
*   **User (Level 0 - Students/Professors):** Creates requests to borrow assets or reserve spaces.
*   **IT/Security Administrator (Level 4):** Maintains system infrastructure, manages user permissions at the group level, and handles exception requests for new asset types or spaces.

**Main Scenarios:** User creates a borrow/reserve request; Department Administrator approves an intra-department request; Inventory Administrator adds new assets via bulk upload; Administrator generates an asset report by location.
**Exception Scenarios:** IT Administrator creates a new room/space based on an exception request; Request is rejected due to insufficient privileges or asset unavailability; Authentication fails due to incorrect credentials.

## Business Process
**Main Process: Asset Borrowing Request & Fulfillment**
1.  **Trigger:** User needs an asset. **Input:** User credentials, asset details.
2.  User authenticates into the system.
3.  User creates a request (basic or advanced form) specifying asset(s) and duration.
4.  System routes request to the appropriate approval queue based on asset location and transfer type (intra-department, inter-department, inter-faculty).
5.  Authorized Administrator (Dept, Faculty, or University level) reviews and approves/rejects the request.
6.  **Output:** Notification email sent to user; Request status updated.
7.  Upon approval, asset status is changed to "checked out" and inventory is updated.
8.  **Output:** User receives the asset; Inventory Administrator updates system upon return, marking asset as available or damaged.

**Key Branch A: Intra-Department Transfer**
1.  Department Administrator initiates transfer directly.
2.  System updates asset location in database.
3.  **Output:** Inventory record updated. (No approval request needed).

**Key Branch B: Exception Handling for New Asset Type**
1.  Administrator attempts to add an asset with a non-existent type.
2.  System triggers an exception request to the IT team.
3.  IT Administrator defines the new asset type and its properties.
4.  **Output:** New asset type available in the system; original administrator can retry the addition.

## Domain Model
Core entities and their key constraints:
*   **User:** userID (unique), name, role, departmentID (reference), facultyID (reference).
*   **Asset:** assetID (unique), serialNumber, type (required), status, currentLocationID (reference), ownerDepartmentID (reference).
*   **Request:** requestID (unique), requesterUserID (reference), assetID (reference), type (borrow/reserve), status, approvalLevelRequired.
*   **Location/Room:** locationID (unique), name, type, parentLocationID (reference for hierarchy), facultyID (reference).
*   **Permission:** permissionID (unique), code (e.g., `asset:edit`), description.
*   **UserPermission:** userID (reference, unique with permissionID), permissionID (reference) - Manages assignment of permissions to users.
*   **UniversityStructure:** nodeID (unique), name (e.g., "Faculty of Engineering"), type (University/Faculty/Department), parentNodeID (reference).
*   **AuditLog:** logID (unique), userID (reference), action, timestamp, details.

## Interfaces and Integrations
*   **Web Browser (Frontend):** Direction: User → System. Interaction: All user interactions via web forms. Input: Clicks, form data. Output: HTML pages, reports, notifications. SLA: Support IE, Firefox, Chrome, Safari.
*   **Authentication System:** Direction: Bidirectional. Interaction: Validate user credentials. Input: Username/password. Output: Authentication token/status. SLA: Response time < 2 seconds.
*   **Legacy Faculty Databases (3):** Direction: System → Databases. Interaction: Periodic sync or real-time query for inventory data integration. Input: Query commands. Output: Asset records. SLA: Sync within 1 hour during off-peak; query timeout < 1 minute.
*   **Email Server (SMTP):** Direction: System → Server. Interaction: Send notifications for request approval/rejection and system alerts. Input: Recipient, subject, body. Output: Email sent. SLA: Delivery within 5 minutes.

## Acceptance Criteria
*   **Capability: Request Creation**
    *   Given a Level 0 User is authenticated, when they submit a basic borrow request for an available asset, then the request is created with a "Pending" status.
    *   Given a Department Administrator is authenticated, when they attempt to approve an inter-faculty transfer request, then the system displays an "Insufficient Privilege" error.
*   **Capability: Asset Management**
    *   Given an Inventory Administrator with `asset:edit` permission is viewing an asset, when they modify the asset's status to "Damaged" and save, then the inventory record is updated and the change is logged.
    *   Given a Faculty Administrator, when they use the bulk upload feature to add 50 new software licenses, then all licenses are added and owned by the respective departments under that faculty.

## Non-Functional Metrics
*   **Performance:** Web page load times < 3 seconds; Report generation for up to 10,000 assets < 30 seconds.
*   **Reliability:** System available 99% during defined working hours; Automated nightly backups with 7-day retention.
*   **Security:** All users authenticated via username/password; Database queries terminated if execution exceeds 1 minute.
*   **Compliance:** Audit logs retained for all inventory modifications and permission changes.
*   **Observability:** System logs all authentication attempts (success/failure) and request state transitions.

## Milestones and Release Strategy
1.  Project Kick-off & Environment Setup.
2.  Core Domain Model & Database Schema Finalized.
3.  Authentication, Basic User & Admin CRUD Operations Completed.
4.  Request Workflow (Create, Route, Approve/Reject) Implemented.
5.  Integration with at least one legacy faculty database.
6.  Pilot Release to one department for UAT, followed by phased rollout to all faculties.

## Risk List and Mitigation Strategies
1.  **Risk:** Legacy database integration is more complex than anticipated. **Mitigation:** Start integration prototyping early; plan for a phased integration approach.
2.  **Risk:** Ambiguous permission delegation logic leads to security gaps. **Mitigation:** Implement strict rule: "A user cannot delegate a permission they do not possess themselves."
3.  **Risk:** High volume of requests overwhelms manual approval process. **Mitigation:** Design clear, filterable approval queues; monitor load during pilot.
4.  **Risk:** Users find the system difficult to learn (>4 hours). **Mitigation:** Involve end-users (students, admins) in UI/UX design reviews and create quick-start guides.
5.  **Risk:** Inconsistent asset data from legacy systems. **Mitigation:** Implement data validation and cleansing routines during the integration phase.
6.  **Risk:** IT team capacity constraints delay handling of exception requests. **Mitigation:** Define clear SLAs for exception handling and provide administrators with templates for exception requests.

## Undecided Issues and Responsible Parties
1.  **Frequency and mechanism of sync with legacy databases** (real-time API vs. nightly batch). *Responsible: Technical Lead & Faculty IT Contacts.*
2.  **Specific format and validation rules for the bulk entry file** (CSV, XML). *Responsible: Business Analyst & Lead Developer.*
3.  **Detailed email notification templates for request approval/rejection.** *Responsible: UI/UX Designer & Product Owner.*
4.  **Formal definition of "working hours" for availability SLA.** *Responsible: Product Owner & University Administration.*
5.  **Priority order for integrating the three legacy faculty databases.** *Responsible: Project Sponsor & Technical Lead.*
6.  **Process for decommissioning or archiving old assets.** *Responsible: Business Analyst & Inventory Administrators.*