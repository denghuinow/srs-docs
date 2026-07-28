# Software Requirements Specification (SRS)
## Platform-i MSN Messenger Xlet

**Document Version:** 1.0
**Status:** Draft for Review
**Date:** [Date of Generation]
**Authors:** [SRS Generator]
**Stakeholders:** End-User (TV Viewer), Development Team (PDSL), Customer

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Multimedia Home Platform (MHP) version of the MSN Messenger application, referred to as the "Platform-i MSN Messenger Xlet." This document is intended for use by the development team (PDSL), project managers, testers, and the customer commissioning the project. It serves as the definitive source of requirements against which the system will be designed, built, and validated.

#### 1.2 Scope
The scope of this project is the development of an MHP xlet (application) that provides core MSN Messenger functionality on the Platform-i TV set-top box environment. The application will enable users to perform instant text messaging, manage online presence, and access basic MSN service integrations such as Hotmail notifications via their television.

**In-Scope Features:**
*   User authentication with existing .NET Passport accounts.
*   Management of contact lists (view, add, remove).
*   Real-time one-to-one and multi-user (group) text chat.
*   Support for emoticons within messages.
*   User status management (Online, Away, Busy, etc.).
*   Display of Hotmail email headers and content.
*   Display of current TV program information (linked from broadcast system).
*   Compliance with the MHP 1.0.x standard.

**Out-of-Scope Features:**
*   File transfer capabilities.
*   Webcam or voice chat support.
*   Creation of new .NET Passport accounts.
*   Advanced email management (replying, deleting, complex sorting).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **MHP:** Multimedia Home Platform. A standard for interactive digital television.
*   **Xlet:** A Java-based application designed to run within an MHP-compliant environment.
*   **Platform-i:** The target TV set-top box environment for this xlet.
*   **MSN Messenger:** The instant messaging service operated by Microsoft.
*   **MSNPv8:** The MSN Messenger Protocol version 8, used for client-server communication.
*   **.NET Passport:** The Microsoft single sign-on service used for authentication (now known as Microsoft Account).
*   **SLA:** Service Level Agreement.
*   **UI:** User Interface.
*   **PDSL:** [Presumably the Development Team's name].

#### 1.4 References
*   MHP 1.0.x Specification
*   MSNPv8 Protocol Documentation
*   Platform-i Set-Top Box Technical Manual

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details specific functional requirements. Section 4 outlines external interface requirements. Section 5 specifies non-functional requirements. Subsequent sections cover other supporting information.

### 2. Overall Description

#### 2.1 Product Perspective
The MSN Messenger Xlet is a self-contained application that operates within the Platform-i MHP environment. It acts as a client to the external MSN Messenger service and optionally interfaces with the TV broadcast system for program information. The relationship is shown below:

```
[TV Broadcast System] --> [Platform-i MHP / Set-Top Box] <--> [MSN Messenger Service]
                                ^
                                |
                        (MSN Messenger Xlet)
```

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **End-User (TV Viewer)** | Primary user. Interacts via TV remote control (potentially a wireless keyboard). Assumed to have an existing .NET Passport account. May have varying technical proficiency. | Log in securely, communicate with contacts via text, manage contact list, check email notifications, all via the TV interface. |
| **Development Team (PDSL)** | Technical staff responsible for implementation, testing, and maintenance. | Clear, unambiguous requirements to build and validate the system. |
| **Customer (Stakeholder)** | Entity commissioning the project. Provides business requirements and final acceptance. | A delivered product that meets agreed-upon functional and quality standards. |

#### 2.3 Operating Environment
*   **Hardware:** Platform-i compliant digital TV set-top box.
*   **Software:** MHP 1.0.x middleware.
*   **Network:** Persistent internet connection (via set-top box).
*   **External Services:** MSN Messenger Service (MSNPv8), TV Broadcast Data Service.

#### 2.4 Design and Implementation Constraints
1.  The application **must** be implemented as an MHP 1.0.x compliant xlet.
2.  The UI **must** be navigable using a standard TV remote control (d-pad, select, number keys).
3.  Communication **must** use the MSNPv8 protocol.
4.  The application **must not** store user credentials in plaintext.
5.  New .NET Passport account creation is explicitly prohibited.

#### 2.5 Assumptions and Dependencies
*   The MSN Messenger service (MSNPv8) will remain available and stable.
*   The Platform-i environment provides reliable MHP APIs for UI rendering and input.
*   Users possess a valid .NET Passport account prior to using the xlet.
*   A TV broadcast data feed is available for the program information feature (D1.1).

### 3. System Features and Requirements

#### 3.1 Feature: User Authentication and Session Management
**Description:** The system shall allow a user to log in and log out using an existing .NET Passport account.

**Requirements:**
*   **FR1.1:** The xlet shall present a login screen upon launch, with fields for .NET Passport ID (email) and password.
*   **FR1.2:** The xlet shall authenticate the user's credentials against the MSN Messenger service using the MSNPv8 protocol.
*   **FR1.3:** Upon successful authentication, the xlet shall retrieve and display the user's contact list.
*   **FR1.4:** If authentication fails (invalid credentials, network error), the xlet shall display a user-friendly error message and return to the login screen.
*   **FR1.5:** The xlet shall provide a "Log Out" option from the main menu, which terminates the session with the MSN service.

#### 3.2 Feature: Contact List Management
**Description:** The system shall allow the user to view, add, and remove contacts (buddies).

**Requirements:**
*   **FR2.1:** The xlet shall display the user's contact list, showing each buddy's nickname, Passport ID, and current online status (e.g., Online, Away, Busy, Offline).
*   **FR2.2:** The user shall be able to select an "Add Buddy" option.
*   **FR2.3:** When adding a buddy, the user shall input the buddy's .NET Passport ID. The xlet shall send an invitation via the MSN service.
*   **FR2.4:** The xlet shall update the contact list to reflect the new buddy once the invitation is accepted by the recipient.
*   **FR2.5:** The user shall be able to remove a buddy from their contact list. The xlet shall send the appropriate removal command via the MSN service.

#### 3.3 Feature: Instant Messaging
**Description:** The system shall enable the user to send and receive real-time text messages.

**Requirements:**
*   **FR3.1:** From the contact list, the user shall be able to select an online buddy to initiate a one-to-one chat session.
*   **FR3.2:** The chat session screen shall display a scrollable history of messages in the conversation, including sender, timestamp, and message content.
*   **FR3.3:** The user shall be able to compose a text message using an on-screen keyboard (or wireless keyboard if supported).
*   **FR3.4:** The xlet shall support the insertion of emoticons into the message text from a predefined set. Emoticons shall be displayed as graphical icons in the chat history.
*   **FR3.5:** Upon sending, the xlet shall transmit the message to the recipient via the MSNPv8 protocol.
*   **FR3.6:** When a new message is received, the xlet shall provide a visual and/or audible notification and update the relevant chat session history.
*   **FR3.7:** The user shall be able to initiate a group chat session by selecting multiple buddies. All participants shall receive all messages within that session.

#### 3.4 Feature: Presence Management
**Description:** The system shall allow the user to set and update their own online status and shall display the status of contacts.

**Requirements:**
*   **FR4.1:** The user shall be able to select their current status from a predefined list (e.g., Online, Busy, Away, Appear Offline).
*   **FR4.2:** The xlet shall immediately transmit status changes to the MSN service, propagating the update to all contacts.
*   **FR4.3:** The xlet shall dynamically update the displayed status icon/text for all buddies in the contact list as notifications are received from the MSN service.

#### 3.5 Feature: Hotmail Integration
**Description:** The system shall provide basic access to the user's linked Hotmail inbox.

**Requirements:**
*   **FR5.1:** The user shall be able to select a "Check Mail" or "Hotmail" option from the main menu.
*   **FR5.2:** The xlet shall query the MSN service for the user's email inbox headers (e.g., sender, subject, date).
*   **FR5.3:** The xlet shall display a list of email headers.
*   **FR5.4:** The user shall be able to select an email from the list to view its full body content.

#### 3.6 Feature: TV Program Information Display (D1.1)
**Description:** The system shall display information about the currently viewed TV program.

**Requirements:**
*   **FR6.1:** The xlet shall include an area on the screen (e.g., a footer, sidebar) to display TV program information.
*   **FR6.2:** The xlet shall query the TV broadcast system (via a platform API) to obtain the current channel and program name.
*   **FR6.3:** The displayed information shall update when the user changes the channel on the set-top box.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The UI shall be designed for Standard Definition (SD) TV resolution (e.g., 720x576i/p).
*   All navigation shall be possible using a standard TV remote control (Directional Pad, OK/Select, Back, Color Keys, Numeric Keys).
*   Text input shall be facilitated via an on-screen keyboard.
*   The visual design and final layout are pending customer/design team input (See Undecided Issues).

#### 4.2 Hardware Interfaces
*   **Input:** Standard IR TV Remote Control. Optional support for USB wireless keyboard is under consideration.
*   **Output:** Video signal to television via SCART, HDMI, or composite.

#### 4.3 Software Interfaces
| Interface | Direction | Purpose | Protocol/Standard |
| :--- | :--- | :--- | :--- |
| **MSN Messenger Service** | Outbound/Inbound | Core messaging, presence, contact management. | MSNPv8 over TCP/IP. Must handle authentication, messaging commands (MSG), presence notifications (NLN, FLN), and contact list sync. |
| **MHP Platform APIs** | Inbound | Application lifecycle, UI rendering (Havi), user input. | MHP 1.0.x Java APIs (org.dvb.*, javax.tv.*). |
| **TV Broadcast System** | Inbound | Retrieval of current program information. | Platform-specific API or DSM-CC Object Carousel data. Mechanism TBD. |

#### 4.4 Communications Interfaces
The xlet requires a reliable TCP/IP network connection provided by the Platform-i set-top box to communicate with the MSN Messenger servers on the standard MSN ports.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   The UI shall respond to user remote control input with a latency of less than 200ms.
*   Under normal network conditions, the latency between sending a message and its delivery to the MSN service shall be less than 2 seconds.
*   The contact list shall load within 5 seconds of successful login.

#### 5.2 Safety Requirements
*   Not applicable for this software type.

#### 5.3 Security Requirements
*   User passwords shall not be stored persistently on the set-top box in plaintext.
*   The xlet shall utilize the secure authentication methods defined within the MSNPv8 protocol.
*   Session data in memory shall be cleared upon logout or application termination.

#### 5.4 Software Quality Attributes
*   **Reliability:** The xlet shall implement automatic reconnection logic to recover from transient network disconnections with the MSN service without user intervention.
*   **Availability:** The xlet shall be available for use whenever the set-top box is powered on and has network connectivity, barring MSN service outages.
*   **Maintainability:** The code shall be modular, with protocol handling isolated to facilitate updates if the MSNPv8 protocol changes.
*   **Portability:** The xlet shall only depend on standard MHP 1.0.x APIs to remain portable across compliant platforms.
*   **Observability:** The xlet shall log key events (e.g., `INFO: Login successful for userX`, `ERROR: Connection lost`, `WARN: Reconnection attempt #Y`) to a system log accessible for debugging purposes.

### 6. Other Requirements

#### 6.1 Acceptance Criteria
The following Gherkin-style scenarios define minimum acceptance criteria:

**Feature: User Login**
```
Scenario: Successful Login with Valid Credentials
    Given the user has a valid .NET Passport account
    When the user enters the correct ID and password in the xlet
    Then the user is authenticated
    And the main application screen showing their contact list is displayed

Scenario: Failed Login with Invalid Credentials
    Given the user is at the login screen
    When the user enters an incorrect ID or password
    Then an appropriate error message is shown
    And the user is not granted access to the application
```

**Feature: Instant Messaging**
```
Scenario: Send and Receive a Message
    Given User A is logged in and has online Buddy B
    When User A sends a text message "Hello" to Buddy B
    Then the message "Hello" appears in Buddy B's chat session with User A
    And when Buddy B replies "Hi there"
    Then the message "Hi there" appears in User A's chat session with Buddy B
```

**Feature: Presence Management**
```
Scenario: Update User Status
    Given User A is online and visible to Buddy B
    When User A changes their status to "Busy"
    Then Buddy B's contact list is updated to show User A's status as "Busy"
```

#### 6.2 Undecided Issues (Open Questions)
| # | Issue | Impact | Responsible Party |
| :--- | :--- | :--- | :--- |
| 1 | Final Visual Design & UI Layout | High - Blocks UI Development | Customer / Design Lead |
| 2 | Specific Set of Supported Emoticons (Graphics & Codes) | Medium - Affects Implementation | Development Team |
| 3 | Details of "Play Games" (D4.1) Feature Scope | Medium - Additional Scope | Customer / Product Manager |
| 4 | Exact Mechanism for Retrieving "TV Program" Info | Medium - Affects D1.1 Implementation | System Architect |
| 5 | Wireless Keyboard Support Confirmation | Low - Input Method Enhancement | Customer |
| 6 | Hotmail Email Display Depth (Number of emails, fields shown) | Low - UI/Data Detail | Development Team |
| 7 | Precise Non-functional Targets (e.g., exact latency numbers) | Medium - Quality Metrics | Customer / Architect |
| 8 | Handling of Offline Messages (Storage/Notification) | Medium - Feature Completeness | Customer / Product Manager |

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner / Customer | | | |
| Project Manager | | | |
| Lead Architect | | | |