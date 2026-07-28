# Software Requirements Specification (SRS)
## Platform-i MSN Messenger Xlet

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document provides a comprehensive specification of the functional and non-functional requirements for the Platform-i MSN Messenger Xlet. It is intended for use by the project stakeholders, including the Customer, the Development Team, and project managers, to ensure a common understanding of the system to be developed.

#### 1.2 Document Conventions
*   **Requirements:** Functional requirements are uniquely identified with the prefix `FR`. Non-functional requirements are prefixed with `NFR`.
*   **Keywords:** The terms "MUST," "SHALL," "REQUIRED," "SHOULD," "MAY," and "OPTIONAL" are to be interpreted as described in IETF RFC 2119.
*   **Formatting:** User interface elements are denoted in *italics*. System commands or protocol elements are in `monospace`.

#### 1.3 Project Scope
This project involves the development of an MHP (Multimedia Home Platform) xlet that implements core MSN Messenger functionality for a television environment. The primary goal is to demonstrate MHP and Platform-i capabilities by enabling instant messaging, presence sharing, and basic email integration via the .NET Messenger Service.

**In-Scope Features:**
*   User authentication and presence management via .NET Passport.
*   Management of a buddy list (view, add, remove contacts).
*   Sending and receiving instant text messages, including support for emoticons.
*   Initiating and participating in group conversations.
*   Display of buddy nicknames and real-time status (Online, Away, Busy, Offline, etc.).
*   A "TV Program Sharing" feature to view the currently watched program of online buddies.
*   Basic Hotmail integration providing new mail notifications and limited inbox viewing.

**Out-of-Scope Features:**
*   Peer-to-peer file transfer functionality.
*   Audio/Video communication (webcam or voice chat).
*   Account creation or management for .NET Passport.
*   Advanced gaming features beyond basic initiation.
*   Detailed graphical user interface (GUI) mockups and asset creation.

#### 1.4 References
*   **MSNP Protocol:** .NET Messenger Service Protocol (MSNP) Version 8 Documentation.
*   **MHP Specification:** ETSI TS 102 812, "Multimedia Home Platform (MHP) Specification."
*   **Platform-i Documentation:** Relevant Platform-i API and middleware documentation.

### 2. Overall Description

#### 2.1 Product Perspective
The MSN Messenger Xlet is a self-contained application (xlet) that runs on an MHP-compliant digital television receiver. It operates independently of broadcast streams but utilizes the receiver's return channel (e.g., broadband modem) to communicate with the external .NET Messenger Service.

**System Interfaces:**
*   **.NET Messenger Service:** The xlet MUST communicate with Microsoft's messenger servers using the MSNPv8 protocol over a TCP/IP connection.
*   **MHP Middleware:** The xlet SHALL utilize standard MHP APIs (JAVA, DVB-J) for graphics, user input, network access, and persistent storage.
*   **Platform-i APIs:** The xlet MAY use Platform-i specific extensions for enhanced features, such as accessing electronic program guide (EPG) data for the TV program sharing feature.

#### 2.2 User Classes and Characteristics
*   **End User (TV Viewer):** The primary user. Assumed to have basic familiarity with a TV remote control and existing MSN Messenger concepts. Input is primarily via remote control directional pad and buttons. Text entry is expected to be slow and cumbersome via an on-screen keyboard.
*   **Administrator/Customer:** The entity deploying the xlet. Requires configuration and potential branding options.
*   **Development Team:** Engineers who will implement, test, and maintain the xlet based on this specification.

#### 2.3 Operating Environment
*   **Hardware:** MHP-enabled digital TV receiver or set-top box with a return channel capability.
*   **Software:** MHP middleware (version TBD). Platform-i extensions (if applicable).
*   **Network:** Persistent internet connection via the receiver's return channel.
*   **Input Devices:** Standard IR remote control. Support for an optional wireless USB keyboard is an undecided issue.
*   **Output Device:** Standard definition or high definition television screen.

#### 2.4 Design and Implementation Constraints
1.  **MHP Compliance:** The application SHALL be developed as a standard MHP xlet.
2.  **Protocol Dependency:** The core messaging logic SHALL be built to interface with the .NET Messenger Service using the MSNPv8 protocol.
3.  **Input Constraint:** The primary input method SHALL be a TV remote control. All navigation and interaction MUST be achievable without a keyboard.
4.  **Display Constraint:** All visual output SHALL be rendered for display on a standard television screen, considering safe zones and legibility from a typical viewing distance.
5.  **External Service Dependency:** The application's functionality is contingent upon the availability and compatibility of the external MSN Messenger service.

#### 2.5 Assumptions and Dependencies
*   It is assumed the end user possesses a valid .NET Passport (MSN) account.
*   The MHP receiver has an active internet connection.
*   The MSNPv8 protocol remains stable and accessible for the duration of the project and product lifecycle.
*   Platform-i provides necessary APIs for EPG data access for the TV sharing feature.

### 3. System Features and Requirements

#### 3.1 User Authentication and Presence Management
**Description:** This feature allows the user to log in to the messenger service and manage their online presence.

**FR-01: User Login**
*   The system SHALL provide a login screen for entering .NET Passport credentials (email and password).
*   The system SHALL securely transmit credentials to the .NET Messenger Service using the MSNPv8 protocol for authentication.
*   The system SHALL provide clear feedback for login success or failure (e.g., "Invalid password," "Network error").

**FR-02: Status Management**
*   The logged-in user SHALL be able to set their personal status from a predefined list (e.g., Online, Away, Busy, Appear Offline).
*   The system SHALL automatically set the status to "Away" after a period of inactivity (configurable, default 10 minutes).
*   The system SHALL update the user's status on the messenger service in real-time.

**FR-03: Buddy List Management**
*   The system SHALL download and display the user's buddy list from the messenger service upon successful login.
*   The system SHALL display each buddy's nickname and current status icon.
*   The system SHALL provide a means to add a new contact (by email address) and remove an existing contact.

#### 3.2 Core Messaging
**Description:** This feature enables real-time text-based communication between users.

**FR-04: Send Instant Message**
*   The user SHALL be able to select an online buddy and initiate a new conversation.
*   The system SHALL provide a text entry interface (e.g., on-screen keyboard).
*   The user SHALL be able to insert common emoticons (e.g., `:)`, `:(`) into the message.
*   Upon sending, the message SHALL be transmitted to the recipient via the MSNPv8 protocol.

**FR-05: Receive Instant Message**
*   The system SHALL display an incoming message notification (visual and/or auditory).
*   The system SHALL open a conversation window displaying the message history with the sending buddy.
*   New messages SHALL be appended to the conversation window in real-time.

**FR-06: Group Conversations**
*   The user SHALL be able to invite multiple online buddies into a single group conversation.
*   Messages sent in a group conversation SHALL be delivered to all participants.
*   The system SHALL clearly label the group conversation and list participants.

#### 3.3 TV Program Sharing
**Description:** This feature allows users to see what television program their online buddies are currently watching.

**FR-07: Program Status Transmission**
*   The system SHALL, when the user is logged in and watching live TV, determine the current channel/program using the Platform-i EPG API.
*   The system SHALL transmit this program information as a custom status message via the MSNPv8 protocol.

**FR-08: Program Status Display**
*   The system SHALL display the received program information (e.g., program title, channel name) next to the relevant buddy's name in the buddy list or conversation window.
*   This display SHALL be updated when the buddy changes the channel.

#### 3.4 Basic Hotmail Integration
**Description:** This feature provides notifications and limited access to the user's associated Hotmail inbox.

**FR-09: New Mail Notification**
*   The system SHALL periodically query the Hotmail service (via MSNP or associated method) for new, unread email counts.
*   If new mail is detected, the system SHALL display a non-intrusive notification icon (e.g., envelope icon) on the main application screen.

**FR-10: Inbox Viewing**
*   The user SHALL be able to select a "Check Hotmail" option.
*   The system SHALL display a list of recent email headers (sender, subject, date).
*   The user SHALL be able to select an email header to view the basic body text of the email (plain text rendering).

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The UI SHALL be designed for 625-line (PAL) or 525-line (NTSC) television display, adhering to MHP safe area guidelines.
*   All interactive elements MUST be navigable using a remote control's directional pad and "OK/Select" button.
*   Standard navigation patterns (Up/Down to move focus, Left/Right for tabs, OK to select) SHALL be used consistently.
*   Text size and contrast SHALL be sufficient for readability from a typical viewing distance (3 meters).

#### 4.2 Hardware Interfaces
*   **Input:** The xlet SHALL receive input events from the MHP middleware, abstracted from the specific remote control key codes.
*   **Network:** The xlet SHALL utilize the MHP network API (`org.davic.net`) to establish and maintain TCP/IP sockets for MSNPv8 communication.

#### 4.3 Software Interfaces
*   **MSNPv8 Protocol:** The xlet SHALL implement the client side of the MSNPv8 command set, including but not limited to: `VER`, `CVR`, `USR`, `CHG`, `LSG`, `ADD`, `REM`, `XFR`, `MSG`, `OUT`.
*   **MHP APIs:** The xlet SHALL use `javax.tv` and `org.dvb` packages for application lifecycle, GUI (`HScene`, `HComponent`), and persistence.
*   **Platform-i EPG API:** For feature FR-07, the xlet SHALL call the Platform-i specific API (e.g., `getCurrentProgramInfo()`) to retrieve the currently viewed program's metadata.

#### 4.4 Communications Interfaces
*   The xlet SHALL communicate with the following MSN Messenger servers via TCP on port 1863:
    *   Dispatch Server (DS) for initial connection and redirection.
    *   Notification Server (NS) for presence and buddy list updates.
    *   Switchboard Server (SB) for individual and group chat sessions.
*   All communication SHALL be compliant with the MSNPv8 protocol specification.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NFR-01:** The application SHALL launch and present the login screen within 5 seconds of being selected from the TV service menu.
*   **NFR-02:** After credential submission, authentication and initial buddy list download SHALL complete within 15 seconds under normal network conditions.
*   **NFR-03:** Sent messages SHALL be delivered and displayed on the recipient's interface with a latency of less than 5 seconds in 95% of cases.
*   **NFR-04:** Presence status updates (user's own and buddies') SHALL be reflected in the UI within 10 seconds of the change occurring.

#### 5.2 Safety and Security Requirements
*   **NFR-05:** User passwords SHALL NOT be stored in plain text on the receiver. They may be cached in a secure manner (e.g., using MHP's `PersistentStorage`) only if explicitly enabled by the user.
*   **NFR-06:** Network communication SHOULD be encrypted if supported by the MSNPv8 protocol and the underlying MHP stack.
*   **NFR-07:** The application SHALL not leak personal data (buddy list, conversation logs) to other applications on the receiver.

#### 5.3 Software Quality Attributes
*   **Reliability:** The xlet SHALL handle network disconnections gracefully, attempting reconnection and restoring state where possible without crashing.
*   **Usability:** The interface SHALL be intuitive for a user familiar with MSN Messenger. The focus navigation SHALL be predictable and loop logically.
*   **Maintainability:** The code SHALL be modular, separating protocol logic, UI rendering, and business logic.

---

### Appendix A: Undecided Issues / Open Questions
1.  The final visual design, color scheme, and specific screen layouts require separate UI/UX specification.
2.  The extent of the "Play games" feature is undefined. Clarification is needed: Is this limited to sending game invitations, or does it include embedded simple games?
3.  Whether to officially support and optimize the interface for a wireless keyboard needs to be resolved, as it significantly impacts text entry design.

### Appendix B: Glossary
*   **EPG:** Electronic Program Guide.
*   **MHP:** Multimedia Home Platform.
*   **MSNP:** .NET Messenger Service Protocol.
*   **Xlet:** A Java-based application designed to run on an MHP platform.
*   **.NET Passport:** Microsoft's single sign-in web service (now part of Microsoft Account).