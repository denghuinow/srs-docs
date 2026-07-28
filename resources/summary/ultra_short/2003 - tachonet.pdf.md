**Purpose & Scope**
The system, TACHOnet, is a network for exchanging information about driver tachograph smart cards between EU Member States' Card Issuing Authorities (CIAs). It enables CIAs to check card statuses, declare card modifications, and share card/license assignments. It does not manage individual CIA users, store a consolidated European database of card holders, or impose technology constraints on Member States' internal systems.

**Product Background / Positioning**
TACHOnet is a central messaging hub commissioned by DG TREN. It connects the disparate, sovereign systems of each Member State's CIA, acting as a Single Point of Contact (SPOC) for cross-border queries and notifications related to driver tachograph cards.

**Core Functional Overview**
1.  Check if a driver has been issued cards in other Member States.
2.  Check the current status (e.g., valid, lost, stolen) of a specific tachograph card.
3.  Declare a modification to a card's status (e.g., report it as lost or stolen).
4.  Notify a Member State when a driver's tachograph card is linked to a driving license they issued.
5.  Provide phonetic search key generation (Phonex) for name matching.
6.  Provide transliteration services (e.g., Greek to US/ASCII) for personal data.
7.  Generate and present usage statistics for administrators.
8.  Log all messages exchanged for tracking and non-repudiation.

**Key Users & Usage Scenarios**
*   **CIA Application:** An automated system representing a Member State. It sends and receives XML messages for administrative tasks (e.g., bulk card checks).
*   **CIA User (Clerk/Enforcer):** An individual in a Member State who may use web interfaces for services like Phonex generation or perform administrative tasks that trigger messages via the CIA Application.
*   **CIA Administrator:** A single user per Member State who can browse TACHOnet usage statistics reports via a secure web portal.
*   **TCN Administrator:** An administrator for the central TACHOnet system, responsible for monitoring, configuration, and managing Member State accounts.

**Major External Interfaces**
*   **CIA Applications:** Interface via secure XML messaging over the TESTA-II network.
*   **CIA Users & Administrators:** Interact via secure web interfaces for specific services and statistics.
*   **Member State Backend Systems:** Interface through a generic/proposed XML interface; their internal technology is not constrained.

**Key Non-functional Requirements**
*   **Performance:** The system must respond to user requests rapidly irrespective of background tasks. High availability (24x7) is required from Member State systems to ensure response times of less than 1 minute for enforcement authority requests.
*   **Security:** Must provide full security including non-repudiation and encryption. No member, including the administrator, can be technically able to reconstruct a consolidated European database from the exchanged messages.
*   **Reliability:** Must be a robust, dependable operational system tolerant to operator errors, with few or no interruptions.
*   **Supportability:** Must be maintainable, extensible, and able to migrate to upgraded hardware, new OS versions, or a different network (e.g., from TESTA-II).
*   **Compatibility:** Must establish and maintain dialog with Member State systems despite various technical environments and technologies.

**Constraints, Assumptions & Dependencies**
*   Must use the TESTA-II network facilities.
*   Must use predefined XML message formats and technical rules.
*   Each Member State designates a Single Point of Contact (SPOC) CIA.
*   Functionality should depend on pre-existing or commercially available software where possible.
*   Member States are responsible for managing their own internal CIA users and validating business rules like card status transitions.

**Priorities & Acceptance Approach**
Core messaging transactions (card checks, status declarations) are fundamental. Administrative and statistical functions are supporting. Acceptance will involve validating the secure, reliable exchange of XML messages between the central hub and Member State systems, meeting performance and security constraints, and ensuring no consolidated database can be created.