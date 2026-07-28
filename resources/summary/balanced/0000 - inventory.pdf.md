# Balanced Summary: IUfA's Unified University Inventory System (UUIS)

## Goals and Scope
The Unified University Inventory System (UUIS) aims to integrate inventory databases from three university faculties into a single web-based interface, enabling secure access and management of university assets. The system will support operations such as asset transfers, requests, modifications, and reporting, available during working hours to authorized users.

## Stakeholders and User Stories
*   **University Administrators:** Manage the entire university inventory and approve inter-faculty transfers.
*   **Faculty Administrators:** Control inventory within their faculty and approve intra-faculty requests.
*   **Department Administrators:** Manage inventory within their department.
*   **Inventory Administrators:** Users delegated by administrators to perform specific inventory tasks.
*   **Users (Students/Professors):** Can request to borrow assets or reserve spaces.
*   **IT Administrators:** Maintain the system, manage permissions, and handle exception requests.

**User Stories:**
1.  As a **User**, I want to create a request to borrow an asset so that I can use it for my work or studies.
2.  As a **Department Administrator**, I want to approve or reject asset transfer requests within my department so that inventory is properly managed.
3.  As a **Faculty Administrator**, I want to generate an asset report by location so that I can audit inventory across departments.
4.  As an **Inventory Administrator**, I want to edit asset properties so that the inventory records remain accurate.
5.  As a **University Administrator**, I want to delegate permission to edit assets to another user so that tasks can be distributed.
6.  As an **IT Administrator**, I want to create a new space/location in the system so that the floor structure can be updated when needed.

## Key Processes
1.  **Authentication:** A user logs in with credentials to access the system (trigger: application start).
2.  **Asset Search:** An authorized user searches for assets using simple or advanced criteria (trigger: user initiates search).
3.  **Request Creation:** A user creates a request to borrow an asset or reserve a space (trigger: user needs an asset/space).
4.  **Request Approval:** An administrator reviews and approves or rejects pending requests within their authority (trigger: pending request exists).
5.  **Asset Modification:** An authorized administrator edits or updates asset properties (trigger: asset information changes).
6.  **Asset Return:** An inventory administrator updates the system when a borrowed asset is returned (trigger: asset is physically returned).
7.  **Report Generation:** An authorized user generates reports on assets, requests, or permissions (trigger: user needs a report).

## Domain Data Elements
*   **Asset:** (Asset_ID, Type, Serial_Number, Location, Status, Owner)
*   **User:** (User_ID, Name, Role, Department, Authentication_Credentials)
*   **Request:** (Request_ID, Requester_ID, Asset_ID(s), Type, Status, Creation_Date)
*   **Location/Space:** (Location_ID, Building, Room_Number, Faculty, Department)
*   **Permission:** (Permission_ID, User_ID, Action_Type, Scope)
*   **University Structure:** (Unit_ID, Name, Type, Parent_Unit_ID)

## Non-Functional Requirements
1.  **Usability:** The web interface must be learnable within 2-4 hours for users with basic internet and office experience.
2.  **Availability:** The system must be available during all working hours, with maintenance conducted outside this time.
3.  **Portability:** The web application must run on common browsers (IE, Firefox, Chrome, Opera, Safari).
4.  **Security:** All users must authenticate; permissions are role-based; database server access is restricted to the IT team.
5.  **Performance:** Database queries are terminated if they take longer than one minute.
6.  **Maintainability:** The system must be designed to facilitate future evolution and ease of maintenance.

## Milestones and External Dependencies
1.  Finalization and approval of the Software Requirements Specification.
2.  Completion of the system's core architecture and database integration design.
3.  Development and testing of key use cases (e.g., Authentication, Request Creation, Approval).
4.  User Acceptance Testing (UAT) with stakeholders from different administrative levels.
5.  System deployment and go-live, dependent on successful UAT and infrastructure readiness.

## Risks and Mitigation Strategies
1.  **Risk:** Complex permission delegation could lead to security gaps or confusion.
    *   **Mitigation:** Implement a clear, hierarchical permission model with audit trails and provide comprehensive administrator training.
2.  **Risk:** Integrating three separate faculty databases may encounter data inconsistency or migration issues.
    *   **Mitigation:** Conduct a thorough data audit and cleansing phase before integration, using staged migration.
3.  **Risk:** High volume of requests during peak periods could impact system performance.
    *   **Mitigation:** Design for scalability and implement query optimization and caching strategies.
4.  **Risk:** Users (e.g., working students) may find the system difficult to use, reducing adoption.
    *   **Mitigation:** Adhere strictly to usability requirements, conduct iterative UI/UX testing, and create clear user guides.
5.  **Risk:** The project timeline (3 months) is aggressive for the defined scope.
    *   **Mitigation:** Prioritize features for a phased release, focusing on core inventory and request management first.

## Undecided Issues
1.  The specific fields and data types for all asset properties, especially for the "other assets" category.
2.  The detailed workflow and approval chain for complex, multi-asset transfer requests.
3.  The exact format and delivery mechanism (e.g., email, on-screen) for user notifications.
4.  The backup strategy's frequency, retention policy, and recovery time objectives.
5.  The specific criteria and interface for the "advanced search" functionality.
6.  The process for handling and resolving exception requests for new asset types or locations.