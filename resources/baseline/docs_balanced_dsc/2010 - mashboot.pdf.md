# Software Requirements Specification (SRS)
## Mashbot: Social Media Campaign Management Platform
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for Mashbot, a web-based service designed to streamline social media marketing campaign management for small-to-medium businesses (SMBs). It serves as a formal agreement between stakeholders and the development team, providing a foundation for system design, implementation, and testing.

#### 1.2 Document Conventions
*   **PK**: Denotes a Primary Key in data models.
*   **FK**: Denotes a Foreign Key in data models.
*   **User Roles**: Specific roles (`Contributor`, `Approver`, `Publisher`, `System Administrator`) are capitalized when referring to the defined system role.
*   Requirements are uniquely identified as `FR` (Functional) or `NFR` (Non-Functional) with sequential numbering.

#### 1.3 Project Scope
The scope of Mashbot's initial release (v1.0) is limited to:
*   Core user account and role-based access management.
*   Creation, editing, and lifecycle management of marketing campaigns.
*   A configurable, multi-step approval workflow for content.
*   Visual scheduling of approved content for automated publishing.
*   Integration with a defined set of external social media services (e.g., Facebook, Twitter) via a plugin architecture.
*   A dashboard for viewing aggregated campaign performance metrics.

**Out of Scope for v1.0:**
*   Advanced content types (audio/video) beyond text and images.
*   Detailed "Explore" view for social media trend analysis.
*   Customer service or direct mail functionalities.
*   Advanced data mining and brand strength analytics.

#### 1.4 References
*   Project Charter: "Balanced Summary: Mashbot"
*   IEEE Std 830-1998: Recommended Practice for Software Requirements Specifications

### 2. Overall Description

#### 2.1 Product Perspective
Mashbot is a standalone web application. It interacts with external systems as depicted in the context diagram below:

```mermaid
graph TD
    A[Mashbot Web Application] --> B[External Social Media APIs<br/>(Facebook, Twitter, etc.)];
    A --> C[External SMTP Service<br/>(Email Notifications)];
    A --> D[External Database<br/>(Persistent Storage)];
    E[User Browser] -- HTTPS --> A;
```

#### 2.2 Product Functions (Summary)
1.  **User Management:** Secure registration, authentication, and role assignment.
2.  **Campaign Management:** Create, view, and organize marketing campaigns.
3.  **Content Authoring:** Create and edit text and image content within campaigns.
4.  **Approval Workflow:** Submit content for review and approve/reject it based on user role.
5.  **Visual Scheduling:** Drag-and-drop approved content onto a calendar to set publish times.
6.  **Automated Publishing:** Execute scheduled publishing tasks to connected social networks.
7.  **Metrics Aggregation:** Collect and display key performance indicators from linked services.
8.  **System Administration:** Configure security, authentication, and system parameters.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **System Administrator** | Technical expertise, responsible for system health and security. | Maintain system availability, manage users, configure security settings. |
| **Contributor** | Marketing staff, content creators. Non-technical. | Efficiently create and prepare marketing content for review. |
| **Approver** | Marketing managers or team leads. | Ensure content quality and brand compliance before publication. |
| **Publisher** | Typically a senior marketing role or the Approver. | Schedule and manage the timing of campaign launches. |
| **Business Employee** | General SMB employee. May encompass Contributor, Approver, or Publisher roles. | Monitor campaign performance and manage the overall marketing calendar. |

#### 2.4 Operating Environment
*   **Server:** Standard LAMP/LEMP stack or equivalent. Must run on hardware/VM supporting 1GB RAM minimum.
*   **Client:** Modern web browser supporting HTTP/1.1 and HTML 4.0+ (e.g., Chrome, Firefox, Safari, Edge latest stable versions). Requires keyboard and pointing device.
*   **External Dependencies:**
    *   Social Media Platform APIs (OAuth 2.0, REST).
    *   SMTP Server for email notifications.
    *   Relational Database (e.g., PostgreSQL, MySQL).

#### 2.5 Design and Implementation Constraints
1.  **C1:** The system **must** implement a plugin-based architecture for social network integrations to ensure maintainability.
2.  **C2:** The client-side application **must not** exceed 256 MB of RAM usage during standard operation.
3.  **C3:** Data persistence **must** rely on an external, industry-standard RDBMS.

#### 2.6 Assumptions and Dependencies
*   **A1:** Users have valid accounts on the external social networks they wish to connect.
*   **A2:** The external social network APIs are available and provide the necessary publishing and metrics endpoints.
*   **D1:** Successful development of the core, open-source facade API for social networks.
*   **D2:** Availability and stability of the chosen external SMTP service and database software.

### 3. System Features and Requirements

#### 3.1 Feature: User Account Management
**Description:** This feature handles the creation, authentication, and management of user accounts and their roles within the system.

**3.1.1 Functional Requirements:**
*   **FR-1:** The system shall allow a new user to register an account by providing a unique username, email address, name, and password.
*   **FR-2:** The system shall authenticate users via a configurable authentication module (e.g., local database, LDAP).
*   **FR-3:** The system shall assign one or more roles (`Contributor`, `Approver`, `Publisher`, `Administrator`) to a user account.
*   **FR-4:** A System Administrator shall be able to view, enable, disable, and delete user accounts.
*   **FR-5:** The system shall enforce a configurable session timeout period after which an inactive user is automatically logged out.

#### 3.2 Feature: Campaign and Content Lifecycle
**Description:** This feature enables the creation, editing, submission, approval, and scheduling of campaign content.

**3.2.1 Functional Requirements:**
*   **FR-6:** A user shall be able to create a new Campaign, defining its name and selecting target social media services.
*   **FR-7:** A user with the `Contributor` role shall be able to create, edit, and delete content items (text, image) within a Campaign.
*   **FR-8:** A `Contributor` shall be able to submit a content item for approval, changing its status to `Pending Review`.
*   **FR-9:** A user with the `Approver` role shall be presented with a list of content items in `Pending Review` status.
*   **FR-10:** An `Approver` shall be able to approve or reject a submitted content item, with an optional comment. Approval changes status to `Approved`. Rejection changes status to `Draft`.
*   **FR-11:** A user with the `Publisher` role shall be presented with a visual calendar interface.
*   **FR-12:** A `Publisher` shall be able to drag-and-drop an `Approved` content item onto the calendar to set its scheduled date and time for publishing.

#### 3.3 Feature: Automated Publishing
**Description:** This feature executes the publishing of scheduled content to external social networks.

**3.3.1 Functional Requirements:**
*   **FR-13:** The system shall include a background service (e.g., cron job, queue worker) that checks for scheduled content items whose publish time has been reached.
*   **FR-14:** For each item due for publishing, the system shall use the appropriate service plugin to transmit the content (text and image) to the designated social network API.
*   **FR-15:** Upon successful publishing, the system shall update the content item's status to `Published` and log the event.
*   **FR-16:** Upon publishing failure, the system shall update the content item's status to `Failed`, log the error, and notify the campaign owner via email.

#### 3.4 Feature: Dashboard and Metrics
**Description:** This feature provides users with an overview of campaign performance.

**3.4.1 Functional Requirements:**
*   **FR-17:** The system shall provide a main Dashboard view upon user login.
*   **FR-18:** The Dashboard shall display aggregated, high-level metrics (e.g., total engagements, clicks, impressions) for the user's active campaigns.
*   **FR-19:** The system shall periodically fetch metric data from connected social network APIs via service plugins.
*   **FR-20:** Users shall be able to view a detailed metrics history for a specific campaign.

#### 3.5 Feature: System Administration
**Description:** This feature allows administrative control over system configuration.

**3.5.1 Functional Requirements:**
*   **FR-21:** A `System Administrator` shall be able to configure the system's authentication method from a predefined set of modules.
*   **FR-22:** A `System Administrator` shall be able to configure the global session timeout duration.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **UI-1:** Responsive web interface compatible with browsers supporting HTML 4.0+.
*   **UI-2:** Primary views shall include: Login, Dashboard, Campaign Manager (Create/Edit), Approval Queue, Scheduling Calendar, and System Admin panel.
*   **UI-3:** The scheduling interface shall implement a drag-and-drop interaction model for placing content on a calendar.

#### 4.2 Hardware Interfaces
None specified. The system is a standard web application.

#### 4.3 Software Interfaces
*   **SI-1:** **Social Network APIs:** The system shall interact with external REST APIs (e.g., Facebook Graph API, Twitter API v2) using OAuth 2.0 for authentication. Communication will be via HTTPS.
*   **SI-2:** **Database:** The system shall connect to a relational database (e.g., MySQL 5.7+, PostgreSQL 12+) using standard drivers.
*   **SI-3:** **SMTP Server:** The system shall send email notifications via an external SMTP server using TLS.

#### 4.4 Communications Interfaces
*   **CI-1:** All client-server communication shall use HTTPS (TLS 1.2+).
*   **CI-2:** The system shall send email notifications for user account actions (welcome, password reset) and system events (publishing failures).

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NFR-1 (Performance):** The server-side application shall operate within a 1 GB RAM constraint under normal load.
*   **NFR-2 (Performance):** The web client shall operate within a 256 MB RAM constraint in a modern browser.
*   **NFR-3 (Performance):** Page load times for the Dashboard and Campaign Manager views shall be under 3 seconds on a standard broadband connection.

#### 5.2 Safety Requirements
Not applicable.

#### 5.3 Security Requirements
*   **NFR-4 (Security):** All data transmitted between the client and server **must** be encrypted using TLS.
*   **NFR-5 (Security):** User passwords **must** be hashed using a strong, adaptive algorithm (e.g., bcrypt, Argon2) before storage.
*   **NFR-6 (Security):** External service credentials (OAuth tokens) **must** be stored encrypted within the database.
*   **NFR-7 (Security):** The system shall implement role-based access control (RBAC) to enforce permissions for Contributors, Approvers, Publishers, and Administrators.

#### 5.4 Software Quality Attributes
*   **NFR-8 (Reliability):** System backups shall be performed without causing a service outage. Any user-visible performance degradation during a full backup shall not exceed 10 minutes.
*   **NFR-9 (Usability):** The interface shall be navigable using a standard keyboard and pointing device. Critical actions (like approval or publishing) shall require confirmation.
*   **NFR-10 (Maintainability):** The system shall be designed with a plugin architecture for social network integrations, allowing new services to be added or updated without modifying the core application code.
*   **NFR-11 (Configurability):** The authentication method and session timeout period shall be configurable by the System Administrator through a web-based interface without requiring code deployment.

### 6. Data Model
The core domain entities and their relationships are defined below. This is a conceptual model.

**Entity Relationship Diagram (Textual Representation):**

*   **User** (UserID PK, Username, PasswordHash, Name, Email, Roles)
    *   A User **owns** one or many Campaigns.
    *   A User **has** one or many ExternalServiceAccounts.
*   **Campaign** (CampaignID PK, Name, OwnerUserID FK, Status)
    *   A Campaign **contains** one or many ContentItems.
    *   A Campaign **has** one associated Schedule (aggregate of scheduled items).
*   **ContentItem** (ContentID PK, CampaignID FK, Type, Body, ApprovalStatus, ScheduledDateTime)
    *   A ContentItem **belongs to** one Campaign.
*   **ExternalServiceAccount** (ServiceAccountID PK, UserID FK, ServiceName, EncryptedCredentials)
    *   An ExternalServiceAccount **belongs to** one User.
*   **Metric** (MetricID PK, CampaignID FK, Type, Value, Timestamp)
    *   A Metric **is associated with** one Campaign.

### 7. Appendices

#### 7.1 Glossary
*   **Campaign:** A container for a coordinated set of marketing content aimed at a specific goal.
*   **Content Item:** A single piece of publishable content (e.g., a post with text and an image).
*   **Service Plugin:** A modular software component that handles all communication logic for a specific external social network (e.g., Facebook Plugin).

#### 7.2 Analysis Models
*Use Case Diagrams, Activity Diagrams for the approval workflow, and State Machine Diagrams for the Content Item lifecycle can be developed from this SRS.*

#### 7.3 Issues List (Undecided/Deferred)
1.  Implementation details for audio/video content types.
2.  Detailed UI/UX specification for the "Explore" trend-monitoring view.
3.  Policy for user account deactivation vs. permanent deletion.
4.  Standardized set of metrics to be provided by all service plugins.
5.  Heuristics for advanced data mining and brand strength analysis.
6.  Roadmap for Phase 2 features (customer service integration, direct mail).