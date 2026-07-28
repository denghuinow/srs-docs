# Software Requirements Specification (SRS)
## Platform-i MSN Messenger Xlet for MHP

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the "Platform-i MSN" project. The goal is to develop a Multimedia Home Platform (MHP) xlet that provides a TV-adapted version of the MSN Messenger service, enabling instant messaging, presence management, and TV-viewing integration for users in a living room environment.

#### 1.2 Scope
The scope of this project includes the development of an MHP-compliant xlet application that allows users to:
*   Log in to the MSN Messenger service using a .NET Passport account.
*   Manage a contact list (add, remove, block buddies).
*   Send and receive instant text messages with emoticons.
*   View the online presence and status of contacts in real-time.
*   See which TV program a buddy is currently watching.
*   Receive notifications for new Hotmail emails.

**Out of Scope:**
*   File transfer capabilities.
*   Webcam or video chat functionality.
*   Full-featured email client (beyond notification).
*   Features inherent to the PC version of MSN Messenger not explicitly listed above.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **MHP:** Multimedia Home Platform. A standard for interactive digital television.
*   **Xlet:** A Java-based application designed to run on an MHP-compliant receiver.
*   **MSNP:** Microsoft Notification Protocol. The protocol used by MSN Messenger.
*   **MSNPv8:** Version 8 of the MSNP protocol.
*   **.NET Passport:** Microsoft's single sign-on web service (now part of Microsoft Account).

#### 1.4 References
*   MHP Specification (ETSI TS 102 818, ETSI TS 102 819)
*   MSNPv8 Protocol Documentation (External, Microsoft)
*   Project Charter: Platform-i MSN Demonstration Project

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and constraints. Section 3 details the specific functional and non-functional requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The Platform-i MSN xlet is a self-contained component that will be deployed on MHP-enabled set-top boxes or integrated digital televisions. It operates as a middleware application, communicating with the external .NET Messenger Service via the internet and rendering its interface within the TV's broadcast video environment.

#### 2.2 Product Functions (High-Level)
1.  User authentication via .NET Passport.
2.  Management and display of user presence status.
3.  Management of a contact list (buddy list).
4.  Conducting one-to-one instant messaging sessions.
5.  Querying and displaying a buddy's currently watched TV program.
6.  Providing visual and/or auditory notifications for new Hotmail emails.

#### 2.3 User Characteristics
| Stakeholder | Role | Characteristics |
| :--- | :--- | :--- |
| **End-User** | Primary user of the xlet. | A TV viewer with a basic understanding of instant messaging. Comfortable using a TV remote control. May have limited text input speed. |
| **Customer** | Commissioner of the project. | Interested in demonstrating MHP platform capabilities and potential interactive TV applications. Technical understanding of MHP constraints. |
| **Development Team** | Builder of the xlet. | Experienced in Java, MHP development, network programming (MSNP), and UI design for TV displays. |

#### 2.4 Constraints
1.  **Technical:** Must comply with MHP standards (Java DVB API, lifecycle, resource limits).
2.  **Protocol:** Must communicate using the MSNPv8 protocol.
3.  **Hardware:** Must function with standard TV remote control input; optional support for wireless keyboard.
4.  **Performance:** Must operate within the memory and processing limitations of typical MHP receivers.
5.  **UI:** Interface must be legible and navigable on a standard-definition TV screen from a typical viewing distance.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The target MHP receiver has an active internet connection.
*   **Assumption:** The user possesses a valid .NET Passport account.
*   **Dependency:** The continued availability and stability of the .NET Messenger Service and the MSNPv8 protocol.
*   **Dependency:** Availability of suitable MHP development and testing tools.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Authentication & Session Management
*   **FR-1: Login**
    *   **Description:** The system shall allow the user to enter .NET Passport credentials (email and password).
    *   **Input:** Alphanumeric input via remote/onscreen keyboard.
    *   **Processing:** Credentials shall be transmitted securely to the .NET Messenger service via MSNPv8 for authentication.
    *   **Output:** Upon success, the main application interface (contact list) shall be displayed. Upon failure, an appropriate error message shall be shown.

*   **FR-2: Logout**
    *   **Description:** The user shall be able to log out of the messenger service, terminating the session.
    *   **Processing:** The xlet shall send a logout command (MSNPv8 `OUT`) and close the network connection.

##### 3.1.2 Contact List & Presence Management
*   **FR-3: Display Contact List**
    *   **Description:** The system shall display the user's buddy list retrieved from the messenger service.
    *   **Data:** For each buddy, display: nickname (or user-assigned nickname), current presence status (Online, Away, Busy, Offline, etc.).
    *   **Update:** The display shall update in real-time upon receiving status change notifications from the server.

*   **FR-4: Manage Contacts**
    *   **FR-4.1:** The user shall be able to add a new buddy by providing a .NET Passport address.
    *   **FR-4.2:** The user shall be able to remove a buddy from the contact list.
    *   **FR-4.3:** The user shall be able to block a buddy, preventing communication.

*   **FR-5: Set Personal Status**
    *   **Description:** The user shall be able to set their own presence status (e.g., Online, Away, Busy).

##### 3.1.3 Messaging
*   **FR-6: Initiate Chat**
    *   **Description:** The user shall be able to select an online buddy from the contact list to start a chat session.

*   **FR-7: Send Message**
    *   **Description:** Within an active chat session, the user shall be able to compose and send a text message.
    *   **Input:** Text entry via remote control keypad or optional wireless keyboard.
    *   **Processing:** The message shall be formatted according to MSNPv8 and sent to the recipient.

*   **FR-8: Receive & Display Message**
    *   **Description:** The system shall display incoming messages in the relevant chat session window in near real-time.
    *   **Display:** Messages shall be displayed with sender identification, timestamp, and content.

*   **FR-9: Support Emoticons**
    *   **Description:** The system shall support a defined set of emoticons (e.g., `:)`, `:(` ).
    *   **Processing:** Textual emoticon codes shall be parsed and displayed as corresponding graphical icons (or remain as text if graphics are undecided).
    *   **Undecided:** The specific set of graphical emoticons is TBD (See Section 4.1).

*   **FR-10: Display Session History**
    *   **Description:** During a chat session, the system shall display the history of messages exchanged within that session.

##### 3.1.4 TV Integration
*   **FR-11: Query Buddy's TV Program**
    *   **Description:** The user shall be able to select a buddy and request information about the TV program they are currently watching.
    *   **Processing:** The xlet shall retrieve this information. *[Mechanism TBD - See Section 4.3]*.
    *   **Output:** The program information (channel, title, broadcast time) shall be displayed in a pop-up or dedicated area of the UI.

##### 3.1.5 Email Notification
*   **FR-12: Notify of New Email**
    *   **Description:** The system shall notify the user upon receipt of a new Hotmail email.
    *   **Trigger:** Notification from the .NET Messenger service.
    *   **Output:** A non-intrusive on-screen notification (e.g., ticker, icon) shall be displayed. *[Inbox display integration TBD - See Section 4.5]*.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements
*   **NFR-1:** Buddy list and status updates shall be reflected on the UI within 3 seconds of the server notification.
*   **NFR-2:** Sent messages shall be delivered and displayed on the recipient's side within 5 seconds under normal network conditions.
*   **NFR-3:** The xlet shall start up and present the login screen within 5 seconds of launch.

##### 3.2.2 Technical Requirements
*   **NFR-4:** The application **shall** communicate exclusively using the **MSNPv8** protocol with the .NET Messenger service.
*   **NFR-5:** The application **shall** be developed as a compliant MHP xlet (Java, DVB API).
*   **NFR-6:** The application **shall** accept primary input from a standard DVB remote control. Support for an optional wireless keyboard is **recommended**.
*   **NFR-7:** The application **shall not** implement file transfer or webcam/video call functionality.

##### 3.2.3 Usability Requirements
*   **NFR-8:** All text and interactive elements shall be clearly readable on a standard TV screen from a distance of 2.5 meters.
*   **NFR-9:** Navigation using only directional keys and "OK"/"Back" buttons on a remote shall be intuitive and consistent.
*   **NFR-10:** The user interface shall follow established MHP UI guidelines for consistency.

##### 3.2.4 Reliability & Availability
*   **NFR-11:** The xlet shall handle loss of network connection gracefully, informing the user and attempting reconnection where appropriate.
*   **NFR-12:** The xlet shall not cause the host MHP receiver to crash or become unstable.

### 4. Undecided Issues & Open Questions
The following items require resolution during the design phase and may impact subsequent development:

1.  **UI Design & Layout:** The final visual design, screen layouts, color schemes, and font specifications are pending.
2.  **Emoticon Set:** The specific list of emoticons to be supported graphically (vs. as plain text) needs to be defined.
3.  **TV Program Retrieval:** The exact technical mechanism for determining a buddy's watched TV program (e.g., via a separate service, buddy-provided data, MHP broadcast integration) is to be determined.
4.  **Group Conversation Scalability:** The approach for handling potential group chats (if allowed by MSNPv8) within the TV UI constraints needs analysis.
5.  **Hotmail Inbox Integration:** The depth of email integration (notification only vs. basic inbox listing) requires clarification with the customer.
6.  **Game Functionality:** The scope, if any, of MSN game functionality to be included is undefined.

### 5. Appendices

#### 5.1 Data Model (Entity Relationship Overview)
Based on the provided domain data elements:
```plaintext
User Account (Passport ID)
    |
    |--- owns ---> Buddy List [Buddy]
    |--- owns ---> Blocked List [Buddy]
    |--- participates in ---> Chat Session
    |
Buddy (Passport ID) --- currently watching ---> TV Program (optional)
    |
Message --- part of ---> Chat Session
```
*(Note: Email entity is primarily for notification purposes and may not require full local storage.)*

#### 5.2 Risk Register Summary
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| MSNPv8 protocol changes | Medium | High | Monitor protocol updates; design for modular protocol handling. |
| MSN service unavailable | Low | Critical | Define fallback requirements; communicate dependency to customer. |
| TV hardware performance | Medium | High | Early prototyping on target hardware; aggressive optimization. |
| Non-intuitive TV UI | High | Medium | Conduct iterative usability testing with representative users. |
| MHP toolchain delays | Medium | Medium | Proactive coordination with tool providers; identify alternatives. |

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Architect | | | |
| QA Manager | | | |