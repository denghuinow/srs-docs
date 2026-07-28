**Purpose & Scope**
The system is a web-based Supply Chain Management (SCM) application for Ejada company. It manages the flow of customer requests, items, and supplier interactions to deliver products and services. The system's scope is limited to Ejada's operations and does not include integration with external systems like CRM or HR, though such integration is noted as a future possibility.

**Product Background / Positioning**
This SCM system is a custom solution for Ejada, positioned as an alternative to large-scale systems from Oracle or SAP. It is part of Ejada's internal framework and will later be integrated with two other modules within that framework.

**Core Functional Overview**
*   Manage customer and supplier requests (add, view, edit, delete).
*   Manage item catalog (add, view, edit, delete).
*   Manage supplier information (add, view, edit, delete).
*   Manage customer information (add, view, edit, delete).
*   Manage resource/storage locations (add, view, edit, delete).
*   Allow suppliers to view supply requests and submit feedback.
*   Allow customers to create and manage their own requests.

**Key Users & Usage Scenarios**
*   **Coordinator:** An Ejada employee with full administrative control. They manage all customers, suppliers, items, locations, and requests. They act as the intermediary between customers and suppliers.
*   **Customer:** External users who log in to create new requests for products/services, view their request status, and edit their profile.
*   **Supplier:** External users who log in to view pending supply requests from the coordinator, see request details, and submit feedback on their ability to fulfill requests.

**Major External Interfaces**
*   **User Interface:** A web-based interface accessed via browser.
*   **Software Interfaces:** Must interface with Microsoft SQL Server database. Client browsers are specified as Internet Explorer (v6/7) and Mozilla Firefox (v2/3).
*   **Communication Interfaces:** Uses TCP/IP over the internet/network. Future communication with external systems (e.g., CRM) is anticipated but out of scope.

**Key Non-functional Requirements**
*   **Performance:** Must support at least 100 concurrent users. 90% of transactions must complete in less than 1 second.
*   **Availability:** Must be available 100% of the time.
*   **Reliability:** All data must be backed up automatically daily. The system must detect errors and roll back incomplete database transactions.
*   **Security:** Access is controlled via login with three distinct roles (coordinator, customer, supplier).
*   **Maintainability:** The system is designed in modules to facilitate error detection and updates.

**Constraints, Assumptions & Dependencies**
*   **Constraints:** Must be a web-based system built using ASP.NET and C# on the .NET Framework. Must use MS SQL Server as the DBMS. Must comply with Ejada's programming standards and framework.
*   **Assumptions:** The server runs a suitable Microsoft OS with an internet connection.
*   **Dependencies:** Success depends on the Ejada .Net framework and future integration with two other Ejada modules.

**Priorities & Acceptance Approach**
All specified functional requirements are required prior to the first delivery (Release 1.0). Performance, availability, and security requirements are critical acceptance criteria. The system will be developed following a Waterfall process model.