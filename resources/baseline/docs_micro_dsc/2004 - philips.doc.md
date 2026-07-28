# Software Requirements Specification (SRS)
## MSN Messenger for TV (MHP-Based Application)

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Approved for Development

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for an MSN Messenger client application designed to run on Multimedia Home Platform (MHP)-enabled television sets. The primary purpose of this application is to provide text-based instant messaging and presence features, adapted for a TV interface and remote control interaction.

#### 1.2 Document Conventions
*   **Shall / Must:** Indicates a mandatory requirement.
*   **Should:** Indicates a recommended, but not mandatory, requirement.
*   **May / Could:** Indicates an optional feature or capability.
*   `Monospaced Text`: Used for protocol commands, code snippets, and user input examples.
*   **Bold Text:** Used for key terms and interface elements.

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Managers:** For scope and milestone planning.
*   **Software Architects & Developers:** For system design and implementation.
*   **QA/Test Engineers:** For creating test plans and validation suites.
*   **UI/UX Designers:** For designing the television-optimized user interface.

#### 1.4 Project Scope
The "MSN Messenger for TV" application will allow users with an MHP-enabled television and a valid .NET Passport (now Microsoft account) to log in to the MSN Messenger service. Users will be able to view their contact list (buddy list), see the online presence status of their contacts, and exchange text messages including emoticons. The application will communicate exclusively using the MSNPv8 protocol with Microsoft's Messenger servers.

**Out-of-Scope:**
*   Creation of new .NET Passport/Microsoft accounts.
*   File transfer of any kind (images, documents, etc.).
*   Audio or video communication (webcams, voice chat).
*   Integration with non-MSN messaging services.
*   Message history storage on the TV or MHP receiver.

#### 1.5 References
*   *MSNP8 Protocol Documentation* (Microsoft, proprietary/internal reference).
*   *ETSI TS 102 812 V1.3.1* - Multimedia Home Platform (MHP) Specification.
*   *ETSI TR 101 202 V1.2.1* - Guidelines for the use of MHP.

### 2. Overall Description

#### 2.1 Product Perspective
This application is a self-contained MHP Xlet. It operates within the constraints of the MHP runtime environment (typically Java-based) and uses the MHP API for graphics, user input (via RC), and network connectivity. It acts as a client connecting to the external MSN Messenger service infrastructure.

#### 2.2 Product Functions (Summary)
1.  **Authentication:** Log in and log out using existing .NET Passport credentials.
2.  **Presence Management:** Display and update the user's own status (Online, Away, Busy, Invisible, etc.). Display the real-time status of buddies on the contact list.
3.  **Contact List Management:** Retrieve and display the user's server-stored contact list. Provide simple in-session list management (add/remove contacts requires specification confirmation, as it may involve out-of-band sync).
4.  **Text Messaging:** Send and receive plain text messages. Send and receive a defined subset of graphical emoticons (e.g., `:)`, `:(`, `:D`).
5.  **Session Management:** Handle connection, disconnection, and reconnection logic with the MSN servers gracefully.

#### 2.3 User Classes and Characteristics
*   **Primary User:** A home television viewer with an existing MSN Messenger/.NET Passport account, familiar with basic instant messaging concepts but using a TV remote control for input.
*   **Characteristic:** Input is primarily via an infrared remote control (d-pad, numeric keys, color keys, OK, BACK). Text input will be slow using an on-screen keyboard. Display is viewed from a distance (10ft/3m).

#### 2.4 Operating Environment
*   **Hardware:** MHP-compliant Digital TV, Set-Top Box, or Integrated Receiver Decoder (IRD).
*   **Software:** MHP Runtime Environment (MHP 1.0.3 or later recommended). No other specific software dependencies.
*   **Network:** Persistent broadband internet connection (via the MHP device's return channel).
*   **External Systems:** Microsoft MSN Messenger servers (compatible with MSNPv8 protocol).

#### 2.5 Design and Implementation Constraints
1.  **Protocol Constraint:** The application **shall** communicate using the **MSNPv8** protocol. No other protocol versions (e.g., MSNP9, MSNP15) are to be implemented.
2.  **Account Constraint:** The application **shall not** provide functionality to create a new .NET Passport/Microsoft account. It is for use with pre-existing accounts only.
3.  **Feature Constraint:** The application **shall not** implement file transfer (sending or receiving) or webcam/video call functionality.
4.  **Platform Constraint:** The application **must** be developed as a compliant MHP Xlet, adhering to the relevant ETSI standards.

#### 2.6 User Documentation
User help shall be integrated into the application as a series of accessible help screens, navigable by the user. A quick-reference guide may be provided in the electronic program guide (EPG) description.

#### 2.7 Assumptions and Dependencies
*   **Assumption:** The MHP device has a functional network connection and the necessary permissions to open sockets on standard ports (e.g., 1863).
*   **Assumption:** The user possesses a valid .NET Passport/Microsoft account with an existing contact list.
*   **Dependency:** Continued operation of Microsoft's MSNPv8-compatible Messenger servers. Changes to the server-side protocol may break the application.

### 3. System Features

#### 3.1 Feature 1: User Authentication and Session Management

##### 3.1.1 Description and Priority
This feature handles the secure login and logout process, establishing and terminating the connection to the MSN Messenger service. **Priority: High**

##### 3.1.2 Stimulus/Response Sequences
*   **Stimulus:** User launches the MHP Xlet.
*   **Response:** Application displays a login screen with fields for Passport email and password.
*   **Stimulus:** User enters credentials and selects "Log In".
*   **Response:** Application initiates an MSNPv8 connection sequence (`VER`, `CVR`, `USR`, `CHL` if needed, `SSO`/`LSG`). On success, transitions to the main contact list view. On failure, displays an appropriate error message.

##### 3.1.3 Functional Requirements
*   **FR1.1:** The application shall provide a secure input screen for .NET Passport email address and password.
*   **FR1.2:** The application shall establish a TCP connection to the MSN Messenger dispatch server and perform the MSNPv8 handshake.
*   **FR1.3:** The application shall authenticate the user using the provided credentials via the MSNPv8 `USR` command and any required challenge-response (`CHL`).
*   **FR1.4:** The application shall gracefully handle authentication failures (wrong password, network error) and inform the user.
*   **FR1.5:** The application shall provide a clear "Log Out" option that sends the proper `OUT` command and terminates the connection.

#### 3.2 Feature 2: Presence and Contact List Management

##### 3.2.1 Description and Priority
This feature manages the retrieval, display, and updating of presence status for the user and their contacts (buddies). **Priority: High**

##### 3.2.2 Stimulus/Response Sequences
*   **Stimulus:** Successful user login.
*   **Response:** Application retrieves the contact list via `LST`/`LSG` commands and the initial presence of each buddy via `PNG`/`FLN`/`NLN`. Displays the list graphically.
*   **Stimulus:** User selects "Change My Status" from a menu.
*   **Response:** Application presents a list of available statuses (Online, Away, Busy, Invisible). Upon selection, sends the appropriate `CHG` command.
*   **Stimulus:** A buddy changes their status.
*   **Response:** Application receives `NLN`, `FLN`, etc., and updates the buddy's icon/name in the on-screen list in real-time.

##### 3.2.3 Functional Requirements
*   **FR2.1:** The application shall retrieve and display the user's contact list (buddy list) from the server.
*   **FR2.2:** The application shall display a visual indicator (icon/color) next to each buddy representing their current presence status (e.g., green for Online, yellow for Away, red for Busy, gray for Offline).
*   **FR2.3:** The application shall allow the user to change their own presence status.
*   **FR2.4:** The application shall dynamically update the on-screen contact list when a buddy's presence status changes.
*   **FR2.5:** The application shall display the "friendly name" of the buddy if available, otherwise the email address.

#### 3.3 Feature 3: Text-Based Instant Messaging

##### 3.3.1 Description and Priority
This feature enables the composition, sending, and receiving of text messages, including the rendering of common emoticons as graphical icons. **Priority: High**

##### 3.3.2 Stimulus/Response Sequences
*   **Stimulus:** User selects a buddy from the contact list and chooses "Send Message".
*   **Response:** Application opens a new message window (chat session) with a history pane, a message composition area, and an on-screen keyboard.
*   **Stimulus:** User composes a message (e.g., "Hello! :)") and selects "Send".
*   **Response:** Application sends the message via the `MSG` command. The text `":)"` is replaced with a graphical smiley icon in both the sent and received history panes.
*   **Stimulus:** A message is received from a buddy.
*   **Response:** Application alerts the user (e.g., sound, flashing icon), opens or highlights the relevant chat window, and displays the incoming message with parsed emoticons.

##### 3.3.3 Functional Requirements
*   **FR3.1:** The application shall allow the user to initiate a text chat session with any online buddy.
*   **FR3.2:** The application shall provide an on-screen keyboard (or equivalent text input method) suitable for TV remote control input.
*   **FR3.3:** The application shall send and receive plain text messages using the MSNPv8 `MSG` command format.
*   **FR3.4:** The application shall recognize a standard set of text-based emoticon codes (e.g., `:)`, `:(`, `:P`, `:D`) and render them as corresponding graphical icons within the chat history display.
*   **FR3.5:** The application shall support multiple concurrent chat sessions, allowing the user to switch between them.
*   **FR3.6:** The application shall clearly distinguish between messages sent by the user and messages received from the buddy (e.g., alignment, color, or label).

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Login Screen:** Simple form with two text fields and login/logout buttons.
*   **Main Contact List:** Vertical or grid-based list showing buddy names, status icons, and a "Me" section showing user's own status.
*   **Chat Window:** Divided into a (non-editable) message history area and a (editable) message composition area. Includes an emoticon palette for quick insertion.
*   **On-Screen Keyboard (OSK):** A grid of characters navigable by D-pad, with "Shift" and "Space" keys.
*   **Menus:** Contextual menus activated by a dedicated "Menu" or "Options" remote key.

#### 4.2 Hardware Interfaces
*   **Input:** Standard MHP-compliant Infrared Remote Control.
*   **Output:** Television screen (SD or HD resolution, 4:3 or 16:9 aspect ratio). The application must be responsive and legible in both.

#### 4.3 Software Interfaces
*   **MSN Messenger Servers:** Communication via TCP sockets using the text-based MSNPv8 command set on the standard messaging port.
*   **MHP APIs:** Use of `javax.tv.xlet.*`, `org.davic.net.*`, `org.dvb.ui.*`, `java.awt.*` (subset) for application lifecycle, networking, and GUI.

#### 4.4 Communications Interfaces
*   **Protocol:** MSNPv8 over TCP/IP.
*   **Ports:** Initial connection to dispatch server (likely port 1863). Subsequent switching to notification and switchboard servers as directed by the protocol.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   The application shall establish a connection and display the contact list within 15 seconds of successful login initiation under normal network conditions.
*   Presence updates and incoming messages shall be displayed on the screen within 3 seconds of their receipt by the Xlet.
*   The GUI shall remain responsive to remote control input at all times (no "freezing").

#### 5.2 Safety Requirements
*   Passwords shall not be stored persistently on the MHP device.
*   The application shall not crash in a way that requires a reboot of the MHP device. It must be terminable via the MHP application manager.

#### 5.3 Security Requirements
*   All network communication involving passwords shall follow the secure authentication mechanisms defined in MSNPv8 (e.g., challenge `CHL`).
*   The application shall not log or store chat messages or contact lists in persistent storage on the TV/STB after logout.

#### 5.4 Software Quality Attributes
*   **Reliability:** The application shall handle network disconnections gracefully, attempting reconnection where appropriate and informing the user.
*   **Usability:** The interface must be navigable using only a standard 5-key D-pad (Up, Down, Left, Right, OK), BACK, and numeric keys. Text size must be appropriate for viewing on a standard-definition TV from 3 meters.
*   **Maintainability:** The code shall be modular, with clear separation between the MSNPv8 protocol engine, the MHP GUI layer, and the application logic.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| QA Manager | | | |