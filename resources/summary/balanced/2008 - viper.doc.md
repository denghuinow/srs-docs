# Balanced Summary: Supply Chain Management (SCM) System

## Goals and Scope
The SCM system aims to streamline Ejada company's supply chain operations, including customer service, procurement, product development, and manufacturing flow management. Its scope is limited to Ejada's internal processes, providing a web-based platform for coordinators, customers, and suppliers to manage requests, items, and resources efficiently.

## Stakeholders and User Stories
*   **Coordinator**: Manages customers, suppliers, requests, and items within the supply chain.
*   **Customer**: Submits and tracks requests for products or services.
*   **Supplier**: Receives requests and provides feedback on supply capability.

**User Stories:**
1.  As a **Coordinator**, I want to add a new request to a supplier so that I can procure needed items.
2.  As a **Coordinator**, I want to view all customer details so that I can manage client relationships.
3.  As a **Customer**, I want to submit a new request so that I can receive products or services from Ejada.
4.  As a **Customer**, I want to edit my profile information so that my contact details are always current.
5.  As a **Supplier**, I want to view pending supply requests so that I can plan my deliveries.
6.  As a **Supplier**, I want to send feedback on a request so that the coordinator knows what I can supply and when.

## Key Processes
1.  **Trigger: User login.** The user authenticates via a web login page, selecting their domain (coordinator, customer, or supplier).
2.  The user navigates to their domain-specific dashboard (e.g., request management, profile editing).
3.  The user performs a core action, such as creating a new request or viewing a list of items.
4.  For creation/update actions, the user fills in a form (e.g., request details, customer information).
5.  The system validates the input and processes the transaction (e.g., saves to database, sends notification).
6.  The system provides confirmation or an error message to the user.
7.  The user logs out, ending the session.

## Domain Data Elements
*   **Customer** (PK: CustomerID): Name, Address, ContactPerson, Email.
*   **Supplier** (PK: SupplierID): Name, Address, ContactPerson, Email.
*   **Request** (PK: RequestID): Description, Status, CustomerID (FK), SupplierID (FK).
*   **Item** (PK: ItemID): Name, Description, Category.
*   **ResourceLocation** (PK: LocationID): Name, Address, Type.
*   **Coordinator** (PK: CoordinatorID): Username, Password, Domain.

## Non-functional Requirements
1.  The system must support at least 100 concurrent users.
2.  90% of transactions must complete in less than 1 second.
3.  The system must be available 100% of the time, with clear user feedback during errors.
4.  Data must be backed up automatically daily.
5.  The system must be developed using ASP.NET, C#, and MS SQL Server.
6.  The system must be compatible with Internet Explorer and Mozilla Firefox browsers.

## Milestones and External Dependencies
1.  Finalize and release SRS Version 2.0.
2.  Complete development for Release 1.0, including all core use cases.
3.  Dependency on Ejada's .NET framework for system integration.
4.  Dependency on future integration with other Ejada modules (CRM, HR).
5.  Server must run a suitable Microsoft OS with IIS and .NET Framework.

## Risks and Mitigation Strategies
1.  **Risk:** Coordinator cannot manage requests due to system error.
    *   **Mitigation:** Implement robust error handling and database transaction rollback to a previous stable state.
2.  **Risk:** Integration issues with Ejada's framework.
    *   **Mitigation:** Adhere strictly to Ejada's programming standards and conduct early integration testing.
3.  **Risk:** Supplier feedback delays the supply chain.
    *   **Mitigation:** Implement notification systems and allow alternative communication (e.g., phone) as a fallback.
4.  **Risk:** System performance degrades with increased user load.
    *   **Mitigation:** Design for scalability and perform load testing against the 100-concurrent-user target.
5.  **Risk:** Data loss due to system failure.
    *   **Mitigation:** Enforce daily automated backups and provide manual backup functionality for administrators.

## Undecided Issues
1.  Specific communication channels for notifications (e.g., email, in-system alerts).
2.  Refinement criteria for viewing filtered lists (e.g., requests by date, items by category).
3.  Whether to disable editing of customer requests once acknowledged by the coordinator.
4.  The exact process for notifying customers/suppliers upon profile edits or deletions.
5.  Handling scenarios where there are no suppliers available for a request.
6.  Detailed quality assurance procedures beyond basic error detection.