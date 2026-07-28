# Detailed Summary: Platform-i MSN Messenger Xlet

## Background and Scope
This document defines the functional requirements for a Multimedia Home Platform (MHP) version of the MSN Messenger application, designed to run on a TV set-top box environment (Platform-i). The core purpose is to enable instant text communication, presence management, and basic MSN service integration (like email notification) for end-users via their television. The scope is limited to the MHP xlet application; it explicitly **excludes** file transfer, webcam support, and the ability to create new .NET Passport accounts.

## Stakeholders Matrix and Use Cases
*   **End-User (TV Viewer):** The primary user who logs in, manages contacts, and sends/receives messages via the TV interface.
*   **Development Team (PDSL):** Responsible for designing, building, and testing the xlet based on this specification.
*   **Customer (Stakeholder):** The entity commissioning the project, who must review and agree on these requirements.

**Main & Exception Scenarios (≤8):**
1.  **Login:** User successfully logs in with an existing .NET Passport account.
2.  **Status Update:** User changes their own online status (e.g., Online, Busy, Away).
3.  **Contact Management:** User adds or removes a buddy from their contact list.
4.  **Send Message:** User composes and sends a text message, optionally with emoticons, to a single buddy.
5.  **Receive & Read Message:** User is notified of, views, and reads an incoming message.
6.  **View Contact Status:** User sees the updated online status and nickname of buddies in their list.
7.  **Group Chat:** User initiates or participates in a conversation with multiple buddies.
8.  **Exception - Login Failure:** User attempts to log in with invalid credentials or tries to create a new account (not allowed).

## Business Process
**Main Process: User Chat Session**
1.  **Trigger:** User launches the MSN Messenger xlet on the TV.
2.  **Input:** User enters .NET Passport credentials.
3.  **Process:** Application authenticates with the MSN service.
4.  **Process:** Application retrieves and displays the user's contact list with buddy statuses.
5.  **Process:** User selects a buddy and composes a message.
6.  **Process:** Application sends the message via the MSN protocol.
7.  **Process:** Application receives and displays an incoming message from the buddy.
8.  **Output:** A continuous chat history is displayed on the TV screen.

**Key Branch A: Manage Contact List (Trigger: User selects "Add Buddy")**
1.  User selects option to add a new buddy.
2.  User inputs the buddy's .NET Passport ID.
3.  Application sends an invitation via the MSN service.
4.  Buddy is added to the contact list upon acceptance.

**Key Branch B: Check Hotmail (Trigger: User selects "Check Mail")**
1.  User selects the Hotmail inbox option.
2.  Application requests inbox data from the MSN service.
3.  Application parses and displays email headers/subjects.
4.  User can select an email to view its full content.

## Domain Model
Core Entities (≤8):
1.  **User Account**
    *   Passport ID (Required, Unique)
    *   Nickname
    *   Current Status (e.g., Online, Away)
2.  **Buddy/Contact**
    *   Passport ID (Required, Unique, Reference to User Account)
    *   Assigned Nickname (User-defined)
    *   Blocked Flag (Boolean)
3.  **Contact List**
    *   Owner (Required, Reference to User Account)
    *   List of Buddies (Required, References to Buddy)
4.  **Message**
    *   Sender (Required, Reference to User Account)
    *   Recipient(s) (Required, List of References)
    *   Content (Required)
    *   Timestamp (Required)
    *   Contains Emoticon Flag
5.  **Chat Session**
    *   Participants (Required, List of References to User Account)
    *   Message History (List of References to Message)
6.  **Emoticon**
    *   Code (e.g., ":)", Required, Unique)
    *   Graphic Representation
7.  **TV Program Info** (Linked from external source)
    *   Channel
    *   Program Name

## Interfaces and Integrations
1.  **MSN Messenger Service**
    *   **Direction:** Outbound & Inbound
    *   **Interaction:** Core protocol for presence, messaging, and contact management.
    *   **Input Key Points:** Login credentials, message payloads, status change commands.
    *   **Output Key Points:** Buddy status updates, incoming messages, email notifications.
    *   **SLA Key Points:** Protocol compliance (MSNPv8), connection reliability for real-time updates.
2.  **MHP Platform (Platform-i)**
    *   **Direction:** Inbound
    *   **Interaction:** Provides runtime environment, remote control/keyboard input, and screen output.
    *   **Input Key Points:** User input events (key presses).
    *   **Output Key Points:** Graphical user interface rendering to TV screen.
    *   **SLA Key Points:** Adherence to MHP specification for xlet lifecycle and UI rendering.
3.  **TV Broadcast System** (Implied for D1.1)
    *   **Direction:** Inbound
    *   **Interaction:** Query for current program information.
    *   **Input Key Points:** Request for current channel/program data.
    *   **Output Key Points:** Program name and channel identifier.
    *   **SLA Key Points:** Availability of program information feed.

## Acceptance Criteria
*   **Capability: User Login**
    *   Given a user has a valid .NET Passport account, when they enter their credentials in the xlet, then they are successfully logged in and their contact list is displayed.
    *   Given a user attempts to log in without an account, when they try to proceed, then they are shown an error message and cannot access the service.
*   **Capability: Instant Messaging**
    *   Given a user is logged in and has an online buddy, when they send a text message, then the message is delivered and appears in the buddy's chat session.
    *   Given a user is in a chat session, when they receive a new message, then a notification appears and the message is added to the session history.
*   **Capability: Presence Management**
    *   Given a user is online, when they change their status to "Busy", then all their buddies see the updated status in their contact lists.

## Non-functional Metrics
*   **Performance:** Message delivery latency should be within [TBD] seconds under normal network conditions. UI response to remote control input should be perceptibly instantaneous.
*   **Reliability:** The xlet should maintain a stable connection to the MSN service, automatically reconnecting after transient network failures.
*   **Security:** User credentials must be handled securely (e.g., not stored in plaintext). Communication should use the secure aspects of the MSNPv8 protocol.
*   **Compliance:** The application must fully comply with the MHP 1.0.x standard for execution on the Platform-i.
*   **Observability:** The xlet should log critical events (login success/failure, connection loss) to a platform-accessible log for debugging.

## Milestones and Release Strategy
1.  Requirements Specification Sign-off.
2.  Completion of Architectural Design.
3.  Core Protocol Integration (Login, Presence, 1-on-1 Messaging).
4.  UI Implementation and Integration.
5.  Internal Alpha Testing (Feature Complete).
6.  Customer Acceptance Testing and Final Release.

## Risk List and Mitigation Strategies
1.  **Risk:** MSNPv8 protocol may change or be deprecated.
    *   **Mitigation:** Isolate protocol handling in a dedicated module for easier updates. Monitor official MSN developer channels.
2.  **Risk:** Performance issues on constrained set-top box hardware.
    *   **Mitigation:** Early prototyping of core network and UI components. Optimize graphic assets and message processing.
3.  **Risk:** Inability to use the official MSN Messenger service protocol.
    *   **Mitigation:** This is a fundamental constraint noted in the document; the entire FRS would need revision to target an alternative service.
4.  **Risk:** Complex user input (text entry) with a remote control.
    *   **Mitigation:** Design an intuitive on-screen keyboard and consider support for optional wireless keyboard.
5.  **Risk:** Network latency causing poor real-time chat experience.
    *   **Mitigation:** Implement optimistic UI updates and clear "sending..."/connection status indicators.

## Undecided Issues and Responsible Parties
1.  **Final Visual Design & UI Layout:** Awaiting customer/design team input. (Responsible: Customer/Design Lead)
2.  **Specific Set of Supported Emoticons:** Which graphics/codes will be implemented? (Responsible: Development Team)
3.  **Details of "Play Games" (D4.1) Feature:** Scope and game list undefined. (Responsible: Customer/Product Manager)
4.  **Exact Mechanism for Retrieving "TV Program" Info (D1.1):** Interface with broadcast system needs specification. (Responsible: System Architect)
5.  **Wireless Keyboard Support Confirmation:** Is it a requirement or a "maybe"? (Responsible: Customer)
6.  **Hotmail Email Display Depth (D3.2):** How many emails, which fields are shown? (Responsible: Development Team)
7.  **Precise Non-functional Targets:** Specific numbers for latency, reconnect time, etc. (Responsible: Customer/Architect)
8.  **Handling of Offline Messages:** Is any form of storage or notification supported? (Responsible: Customer/Product Manager)