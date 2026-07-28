# Software Requirements Specification (SRS)
## MSN Messenger MHP Application
**Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the **MSN Messenger MHP Application**. It is intended to serve as a complete description of the system for the development team, testers, project managers, and stakeholders. The primary purpose of this application is to provide instant messaging and social TV features on a television platform via the Multimedia Home Platform (MHP) standard.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms "MUST," "SHALL," "REQUIRED," "SHOULD," "MAY," and "OPTIONAL" are to be interpreted as described in IETF RFC 2119.
*   **User Interface:** Descriptions refer to navigation via a standard TV remote control (D-pad, OK, Back, Color keys).

#### 1.3 Project Scope
The system is an MHP (Multimedia Home Platform) application for TV, providing instant messaging via the MSN Messenger service. It allows users to see online contacts, chat, and see which TV programs contacts are watching.

**In-Scope:**
*   User authentication via .NET Passport.
*   Contact list management (view, add, delete, block).
*   Sending and receiving text-based instant messages with emoticons.
*   Display of user and contact online status.
*   Notification of new Hotmail email.
*   Display of the TV program a contact is currently watching.
*   Operation within the MHP and Platform-i runtime environment.

**Out-of-Scope:**
*   File transfer of any kind (images, documents, etc.).
*   Webcam or video chat functionality.
*   Voice communication.
*   Integration with non-MSN messaging services.
*   Advanced profile customization beyond nickname and status.

#### 1.4 References
*   **MHP Specification:** ETSI TS 102 812 (Multimedia Home Platform).
*   **MSNP Protocol:** Microsoft Notification Protocol, Version 8 (MSNPv8).
*   **Platform-i Documentation:** Relevant vendor-specific MHP implementation guides.

---

### 2. Overall Description

#### 2.1 Product Perspective
This is a standalone MHP application, an independent product designed to demonstrate the capabilities of the MHP and Platform-i environment. It is a TV-adapted version of the MSN Messenger client found on personal computers.

**System Interfaces:**
*   **.NET Messenger Service:** The application acts as a client, communicating via the MSNPv8 protocol over the internet.
*   **MHP Middleware:** The application relies on the host set-top box's MHP middleware for graphics rendering, network access, and input handling.
*   **Broadcast Stream (Optional):** May utilize the broadcast carousel for application updates or static data.

**User Interfaces:**
*   **Input:** Primary input via infrared remote control. A wireless keyboard (if supported by the MHP platform) may be used for enhanced text entry.
*   **Output:** Graphical user interface displayed on a standard definition or high definition television screen (resolution dependent on MHP platform).

#### 2.2 User Classes and Characteristics
*   **End-User / TV Viewer:** The sole user class. Users are assumed to have a basic understanding of instant messaging concepts and TV navigation. They possess a valid .NET Passport (MSN/Hotmail) account. Physical interaction is limited to a remote control.

#### 2.3 Operating Environment
*   **Hardware:** MHP-compliant digital television set-top box or integrated digital TV (iDTV).
*   **Software:** MHP middleware (specifically, the Platform-i implementation). A compatible Java runtime environment as mandated by MHP.
*   **Network:** Persistent broadband internet connection (via set-top box).
*   **External Services:** Access to the public .NET Messenger Service (MSNPv8 endpoints).

#### 2.4 Design and Implementation Constraints
1.  **MHP Compliance:** The application MUST be developed according to the ETSI MHP specification (TS 102 812) and any Platform-i extensions.
2.  **MSNPv8 Protocol:** The application SHALL use the MSNPv8 protocol for all communication with the messenger service. This is a critical dependency.
3.  **Resource Limitations:** Application memory, processing power, and graphics performance are constrained by the capabilities of the target set-top box.
4.  **Input Device:** The user interface MUST be fully navigable using only a standard D-pad remote control.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The target MHP platform provides stable and standards-compliant Java APIs for networking, graphics, and user input.
*   **Assumption:** The .NET Messenger Service (MSNPv8) remains available and its protocol specifications are accurate.
*   **Dependency:** Successful operation is entirely dependent on network connectivity and the availability of the external .NET Messenger Service.
*   **Dependency:** The application requires user acceptance of MSN service terms and conditions.

---

### 3. System Features

#### 3.1 Feature: User Authentication and Session Management
**Description:** The system shall allow users to log in and out of the MSN Messenger service and manage their connection state.

**Requirements:**
*   `FR-010` The system SHALL present a login screen for entering .NET Passport credentials (email and password).
*   `FR-011` The system SHALL securely transmit credentials to the .NET Messenger Service via the MSNPv8 protocol for authentication.
*   `FR-012` The system SHALL provide visual feedback during the login process (e.g., "Connecting...", "Signing in...").
*   `FR-013` The system SHALL handle login failures (invalid credentials, network error) and display an appropriate error message to the user.
*   `FR-014` The system SHALL provide a "Sign Out" or "Exit" function to properly terminate the session with the messenger service.
*   `FR-015` The system SHALL attempt to reconnect automatically if the session is dropped unexpectedly, subject to user-configurable settings.

#### 3.2 Feature: Contact List Management
**Description:** The system shall display the user's contact list and allow management of contacts.

**Requirements:**
*   `FR-020` The system SHALL display the user's contact list, grouping contacts by status (Online, Away, Busy, Offline, etc.).
*   `FR-021` For each contact, the system SHALL display their nickname (or email if nickname unavailable) and current online status icon.
*   `FR-022` The system SHALL allow the user to add a new contact by entering a valid .NET Passport email address.
*   `FR-023` The system SHALL allow the user to delete an existing contact from the list.
*   `FR-024` The system SHALL allow the user to block a contact, preventing them from sending messages or seeing the user's status.
*   `FR-025` The system SHALL reflect real-time updates to contact statuses (online/offline, nickname changes) as pushed by the messenger service.

#### 3.3 Feature: Instant Messaging
**Description:** The system shall enable the sending and receiving of real-time text messages.

**Requirements:**
*   `FR-030` The user SHALL be able to initiate a chat session by selecting an online contact from the list.
*   `FR-031` The system SHALL open a dedicated chat window displaying the message history with that contact.
*   `FR-032` The user SHALL be able to compose and send a text message within the chat window.
*   `FR-033` The system SHALL display incoming messages from the contact in the chat window in near real-time.
*   `FR-034` The system SHALL support a set of common emoticons (e.g., `:)`, `:(` ). These MAY be displayed as graphical icons or as text characters.
*   `FR-035` The system SHALL provide a visual and/or audible notification for new incoming messages, even if the chat window is not in focus.

#### 3.4 Feature: User Status
**Description:** The system shall allow the user to view and set their own availability status.

**Requirements:**
*   `FR-040` The system SHALL display the user's current status (e.g., Online, Away, Busy, Invisible) prominently within the application.
*   `FR-041` The user SHALL be able to change their current status from a predefined list (Online, Away, Busy, Appear Offline).
*   `FR-042` The system SHALL broadcast the status change to the messenger service immediately upon user selection.

#### 3.5 Feature: Email Notification
**Description:** The system shall notify the user of new, unread email in their associated Hotmail inbox.

**Requirements:**
*   `FR-050` The system SHALL display a clear, non-intrusive indicator (e.g., an envelope icon with a count) when the messenger service notifies of new Hotmail messages.
*   `FR-051` The notification SHALL be visible on the main contact list screen.
*   `FR-052` Selecting the notification MAY display a text message such as "You have [N] new email(s)." The application itself SHALL NOT provide full email client functionality.

#### 3.6 Feature: Social TV / "What's On"
**Description:** The system shall display information about the TV program a contact is currently watching.

**Requirements:**
*   `FR-060` For online contacts who are broadcasting "What I'm Watching" data, the system SHALL display this information next to their name in the contact list (e.g., "John - [Movie: Star Wars]").
*   `FR-061` The specific format and source of this program data are dependent on the MSNPv8 protocol and the contact's own client (e.g., a PC). The MHP client SHALL only display the information as provided by the service.

---

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **4.1.1 Graphical User Interface (GUI):** The GUI shall be designed for TV viewing distances (10-foot UI). Text size, contrast, and button targets shall comply with MHP accessibility guidelines. A consistent color scheme and layout shall be used across all screens (Login, Contact List, Chat Window).
*   **4.1.2 Navigation Model:** Hierarchical navigation using UP/DOWN/LEFT/RIGHT keys for focus movement. The OK/SELECT key shall activate the focused item. A dedicated BACK/EXIT key shall return to the previous screen or context menu.

#### 4.2 Hardware Interfaces
*   **4.2.1 Input:** The application shall receive input events (key presses) from the MHP middleware, abstracted from the specific remote control hardware.
*   **4.2.2 Network:** The application shall utilize the TCP/IP networking stack provided by the MHP platform's network interface (Ethernet or WiFi).

#### 4.3 Software Interfaces
*   **4.3.1 .NET Messenger Service (MSNPv8):**
    *   **Communication Protocol:** MSNPv8 over TCP, typically on port 1863.
    *   **Data Format:** Text-based command/response protocol as defined by MSNPv8.
    *   **Responsibilities:** Authentication, presence notification, contact list synchronization, message relay.
*   **4.3.2 MHP API:** The application shall use the standard `org.davic.*`, `org.dvb.*`, and `java.awt.*` packages as per MHP specification for graphics, event handling, and network I/O.

#### 4.4 Communications Interfaces
The application requires full bidirectional TCP socket communication over the internet to the MSN messenger servers. The MHP platform is responsible for establishing the underlying network connection.

---

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-001` **Login Time:** The application shall present the main contact list screen within 15 seconds of the user initiating a login under normal network conditions.
*   `NFR-002` **Message Delivery:** The time between a user pressing "send" and the message appearing in the remote contact's client (as measured by a round-trip echo) shall be less than 5 seconds under normal conditions.
*   `NFR-003` **Status Updates:** Changes in contact online status shall be reflected in the local UI within 10 seconds of the event occurring on the server.

#### 5.2 Safety Requirements
Not applicable.

#### 5.3 Security Requirements
*   `NFR-010` **Credential Storage:** User passwords shall not be stored persistently on the set-top box in plain text. If caching is implemented, it must use platform-secure storage mechanisms.
*   `NFR-011` **Network Communication:** Sensitive data (login credentials) shall be transmitted over the network. The MSNPv8 protocol itself handles encryption; the application must not degrade this.

#### 5.4 Software Quality Attributes
*   `NFR-020` **Reliability:** The application shall not cause the host MHP platform to crash or become unresponsive. It should handle network timeouts and service errors gracefully.
*   `NFR-021` **Usability:** A first-time user shall be able to successfully log in and send a message within 3 minutes of launching the application, using only the remote control.
*   `NFR-022` **Maintainability:** The code shall be well-documented, with a clear separation between the UI logic, MSNP protocol handling, and MHP system interfaces.

---

### 6. Other Requirements

#### 6.1 Apportioning of Requirements
Future versions may consider:
*   Support for display pictures (avatars).
*   Chat history logging.
*   Customizable notification sounds.
*   Support for MSNP protocol versions later than v8.

---

### Appendix A: Glossary

| Term | Definition |
| :--- | :--- |
| **MHP** | Multimedia Home Platform. A standard for interactive digital television. |
| **MSNP** | Microsoft Notification Protocol. The protocol used by MSN Messenger. |
| **.NET Passport** | Microsoft's single sign-on service, now known as Microsoft Account. |
| **Platform-i** | A specific vendor's implementation of the MHP standard. |
| **Set-Top Box (STB)** | The hardware device that decodes the TV signal and runs the MHP application. |
| **Emoticon** | A representation of a facial expression using characters (e.g., `:)`) or a small graphic. |

---

### Appendix B: Analysis Models
*(Optional - To be added later. Could include UI wireframes, state transition diagrams for the MSNP session, or a high-level component diagram.)*

---

**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Manager | | | |
| Lead Developer | | | |
| QA Lead | | | |