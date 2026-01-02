# Software Requirements Specification (SRS)
## MSN Messenger MHP Xlet for TV

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for an MHP (Multimedia Home Platform) Xlet application that provides core MSN Messenger functionality on a television platform. This document is intended for use by the project stakeholders, including developers, testers, project managers, and system architects.

#### 1.2 Scope
The system, herein referred to as the "Messenger TV Xlet," will allow users to log in with an existing .NET Passport account, manage contacts, view presence status, exchange instant text messages, and see what TV program a contact is currently watching. The application will be implemented as an MHP Xlet, adhering to the ETSI (European Telecommunications Standards Institute) MHP standard, and will communicate using the official .NET Messenger Service protocol (MSNPv8).

**In-Scope Features:**
*   User authentication via .NET Passport.
*   Contact list management and presence notification.
*   Sending and receiving of instant text messages.
*   Integration with TV broadcast information to share/view currently watched program.
*   User interface optimized for TV display and navigation via remote control.

**Out-of-Scope Features:**
*   File transfer of any kind (images, documents, etc.).
*   Webcam or video chat functionality.
*   Voice chat functionality.
*   Support for protocols other than MSNPv8.
*   Functionality on non-MHP compliant platforms.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **MHP (Multimedia Home Platform):** A standard middleware platform for digital television receivers.
*   **Xlet:** An application written for the MHP platform, analogous to an "applet" in Java.
*   **MSNP (Microsoft Notification Protocol):** The protocol used by the .NET Messenger Service.
*   **MSNPv8:** The specific version 8 of the MSNP protocol.
*   **.NET Passport:** Now known as Microsoft account, the authentication system for MSN Messenger.
*   **Presence:** The online/offline/away/busy status of a user.
*   **SRS:** Software Requirements Specification.

#### 1.4 References
*   ETSI TS 102 812: "Multimedia Home Platform (MHP) Specification."
*   Microsoft .NET Messenger Service Protocol Documentation (MSNP8).
*   RFC 2119: Key words for use in RFCs to Indicate Requirement Levels.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional and non-functional requirements.

---

### 2. Overall Description

#### 2.1 Product Perspective
The Messenger TV Xlet is a self-contained application residing on an MHP-compliant digital TV receiver or set-top box. It operates independently of other MHP applications but shares system resources (graphics, network). Its primary external interaction is with the Microsoft .NET Messenger Service servers via the internet.

**System Interfaces:**
*   **SI.1 - Messenger Service:** Communication via MSNPv8 over TCP/IP.
*   **SI.2 - TV Broadcast Data:** Reads current program information from the DVB (Digital Video Broadcasting) stream or MHP's "Service Information" API.
*   **SI.3 - User Input:** Receives commands from a standard TV infrared remote control.
*   **SI.4 - Graphics Output:** Renders interface to the TV screen using the MHP's Java-based graphics APIs.

#### 2.2 Product Functions (Summary)
1.  User authentication and session management.
2.  Retrieval, display, and local management of the user's contact list.
3.  Sending, receiving, and displaying instant messages in a chat interface.
4.  Updating and displaying the user's own presence status.
5.  Receiving and displaying the presence status of contacts.
6.  Determining and transmitting the currently watched TV channel/program.
7.  Receiving and displaying the currently watched TV program of contacts.

#### 2.3 User Characteristics
The sole user class is the **End-User** (TV viewer). Key characteristics:
*   **Technical Expertise:** Assumed to be low to moderate. Users are familiar with watching TV and basic concepts of instant messaging but not with technical configuration.
*   **Primary Interaction:** Standard TV remote control (d-pad, numeric keys, color keys, OK, BACK).
*   **Environment:** A living room setting, with a typical viewing distance of 2-3 meters from the screen.

#### 2.4 Constraints
1.  **C.1 - Protocol Constraint:** The system **MUST** use the .NET Messenger Service Protocol version 8 (MSNPv8) for all communication with the messaging network.
2.  **C.2 - Platform Constraint:** The application **MUST** be developed as an MHP 1.0.3 (or later) Xlet, using the prescribed Java-based APIs.
3.  **C.3 - Hardware Constraint:** The UI and input model **MUST** be designed for operation via a standard TV remote control, not a mouse and keyboard.
4.  **C.4 - Legal/Compliance Constraint:** The application must comply with the terms of service of the .NET Messenger Service.

#### 2.5 Assumptions and Dependencies
*   **AS.1:** The user has an existing, valid .NET Passport (Microsoft account) with MSN Messenger contacts.
*   **AS.2:** The MHP-enabled receiver has an active internet connection.
*   **AS.3:** The TV broadcast includes valid Electronic Program Guide (EPG) data for the "current program" feature.
*   **DE.1:** The continued availability and non-modification of the MSNPv8 protocol by Microsoft is a project dependency.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **UI.1 - Login Screen:** Provides fields for .NET Passport email address and password. Navigable by remote control d-pad.
*   **UI.2 - Main Contact List Screen:** Displays a vertical list of contacts with their display name, presence icon (online, away, busy, offline), and optionally their "now watching" status. The focus should be clearly indicated.
*   **UI.3 - Chat Window Screen:** Displays a history of messages in a scrollable view, with a clearly marked area for text entry. Remote control color keys (e.g., Red=Send, Green=Close, Yellow=Smilies).
*   **UI.4 - Status Menu:** A pop-up menu allowing the user to change their own presence status (Online, Away, Busy, Invisible, Appear Offline).

##### 3.1.2 Hardware Interfaces
*   **HI.1:** The application shall receive input from the standard infrared TV remote control via the MHP platform's `javax.tv.service.selection.ServiceContext` and key event APIs.
*   **HI.2:** The application shall output video/graphics to the TV screen via the standard MHP `java.awt` and `javax.tv.graphics` APIs.

##### 3.1.3 Software Interfaces
*   **SI.1 - MSNPv8 Protocol Stack:** A custom Java implementation of the MSNPv8 client protocol shall handle connection, authentication, and messaging.
*   **SI.2 - MHP SI Access:** The `javax.tv.service` API package shall be used to read the current service (channel) and program information.
*   **SI.3 - Network:** Network connectivity via the MHP's `java.net` package.

##### 3.1.4 Communications Interfaces
*   **CI.1:** The system shall initiate and maintain a persistent TCP connection to the .NET Messenger Service dispatch server (typically on port 1863).
*   **CI.2:** All communication shall comply with the command/transaction structure defined by MSNPv8.

#### 3.2 Functional Requirements

##### 3.2.1 Authentication & Session Management
*   **FR.1:** The system shall allow the user to enter a .NET Passport email address and password.
*   **FR.2:** The system shall establish a connection to the Messenger Service and perform authentication using the provided credentials via the MSNPv8 `USR` command sequence.
*   **FR.3:** The system shall securely store login credentials (optional, user-configurable) in accordance with MHP's persistent storage API.
*   **FR.4:** The system shall gracefully handle authentication failures (wrong password, network error) and inform the user.

##### 3.2.2 Contact and Presence Management
*   **FR.5:** Upon successful login, the system shall retrieve the user's contact list (roster) from the server via the `LST` command.
*   **FR.6:** The system shall display the contact list, showing each contact's friendly name and a visual indicator of their presence status.
*   **FR.7:** The system shall dynamically update and display changes in contact presence status (e.g., from online to away) as notified by the server (`NLN`, `FLN` commands).
*   **FR.8:** The system shall allow the user to change their own presence status, which shall be transmitted to the server (`CHG` command).

##### 3.2.3 Messaging
*   **FR.9:** The user shall be able to select a contact from the list and initiate a chat session.
*   **FR.10:** The system shall provide a text entry field for composing messages, with support for remote-controlled on-screen keyboard input.
*   **FR.11:** Upon sending, the system shall transmit the text message to the selected contact via the `MSG` command.
*   **FR.12:** The system shall receive incoming messages from contacts and display them in the appropriate chat window, clearly identifying the sender.
*   **FR.13:** The chat history shall be scrollable and persist for the duration of the chat session.

##### 3.2.4 TV Program Integration
*   **FR.14:** The system shall periodically (e.g., every 5 minutes or on channel change) query the MHP platform for the currently tuned service (channel) and the current program information (title, episode, etc.) from the EPG.
*   **FR.15:** The system shall format this "Now Watching" data into a string (e.g., "Watching: News on Channel 1") and transmit it as a personal message (P4) or status via the `PRP` command.
*   **FR.16:** The system shall receive and parse the "Now Watching" status from contacts and display it adjacent to their name in the contact list.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **PR.1:** The application shall start and present the login screen within 5 seconds of being launched from the MHP portal.
*   **PR.2:** The time between user pressing "Send" and the message being displayed in the local chat history shall be less than 1 second under normal network conditions.
*   **PR.3:** Presence updates from the server shall be reflected in the UI within 3 seconds.

##### 3.3.2 Safety & Security Requirements
*   **SR.1:** User passwords shall never be displayed in clear text.
*   **SR.2:** Network communication should, to the extent supported by MSNPv8, be considered for obfuscation (though note MSNPv8 is largely plaintext).
*   **SR.3:** Persistent storage of credentials shall be optional and clearly indicated to the user.

##### 3.3.3 Software Quality Attributes
*   **QA.1 - Usability:** All functions must be achievable within 4 levels of menu navigation. Text must be legible from a 3-meter distance on a standard-definition (SD) TV.
*   **QA.2 - Reliability:** The Xlet shall not cause the MHP receiver to crash or become unresponsive. Network errors shall be caught and handled, allowing the user to return to the main menu.
*   **QA.3 - Portability:** The Xlet shall run on any MHP 1.0.3 compliant receiver without modification, aside from potential receiver-specific bugs.
*   **QA.4 - Maintainability:** The code shall be modular, separating protocol logic, UI, and TV integration into distinct packages.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Manager | | | |
| Lead Developer | | | |
| QA Lead | | | |