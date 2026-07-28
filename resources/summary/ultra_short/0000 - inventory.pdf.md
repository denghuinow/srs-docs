**Purpose & Scope**
The system is a Unified University Inventory System (UUIS) to integrate three separate faculty inventory databases into a single web-accessible system. It manages inventory assets (spaces, software licenses, other assets) and processes requests for borrowing/reserving them. It does not handle financial transactions, payroll, or student academic records.

**Product Background / Positioning**
The system replaces or integrates three existing, separate faculty inventory databases. It operates within the defined university organizational hierarchy (University > Faculty > Department). It is a new central system intended for use by all university members.

**Core Functional Overview**
*   Manage inventory assets (add, edit, modify, return).
*   Create and submit requests to borrow assets or reserve spaces.
*   Approve or reject pending requests based on organizational authority.
*   Search the inventory (simple and advanced).
*   Generate standard reports (assets by location, requests, user permissions).
*   Authenticate users via username and password.
*   Delegate permissions from administrators to other users.

**Key Users & Usage Scenarios**
*   **Students/Professors (Level 0):** Can create basic requests to borrow assets.
*   **Department/Faculty/University Administrators (Levels 1-3):** Can manage assets within their scope and approve requests. Can delegate permissions.
*   **Inventory Administrators:** Users delegated specific permissions by administrators.
*   **IT Administrators (Level 4):** Have full system control, can create new permission groups, and manage system infrastructure.
*   Typical scenario: A professor requests a projector; the request is approved by their department administrator and executed by an inventory user.

**Major External Interfaces**
*   **User Interface:** A web interface accessible via standard browsers (IE, Firefox, Chrome, Opera, Safari).
*   **External Systems:** Interfaces with three existing faculty inventory databases for data integration.
*   **Email System:** Sends notifications to users when requests are processed.

**Key Non-functional Requirements**
*   **Availability:** The system must be available during all university working hours. Maintenance must occur outside working hours.
*   **Security:** All access requires username/password authentication. Permissions are enforced by user role. Database servers are only accessible locally by the IT team.
*   **Performance:** Database queries must be terminated if they take longer than 1 minute.
*   **Portability:** The application must be installable on both Microsoft and Unix platforms.
*   **Maintainability:** The system must be designed to facilitate future evolution and maintenance.

**Constraints, Assumptions & Dependencies**
*   The system must conform to the defined university organizational hierarchy.
*   It depends on the successful integration of three existing, separate faculty databases.
*   User authentication relies on an existing university credential system (implied).
*   The system assumes administrative users understand their permission boundaries when delegating tasks.

**Priorities & Acceptance Approach**
Core functionality (asset management, request workflow, authentication, and role-based access control) is highest priority. Acceptance will be based on correct enforcement of the permission model across organizational levels, successful processing of the defined request types, and system availability during working hours.