**Purpose & Scope**
The system is an MHP (Multimedia Home Platform) application for TV, providing instant messaging via the MSN Messenger service. It allows users to see online contacts, chat, and see which TV programs contacts are watching. It explicitly does not support file transfers or webcam functionality.

**Product Background / Positioning**
This is an MHP version of the MSN Messenger PC application, intended to demonstrate the capabilities of the MHP and Platform-i environment. It is an independent application, not part of a larger system or product line.

**Core Functional Overview**
*   Log in using an existing .NET Passport account.
*   View and change own online status.
*   View the online status and nicknames of contacts.
*   Add, delete, and block contacts.
*   Send and receive instant text messages, including emoticons.
*   See a notification of new Hotmail email.
*   See which TV program an online contact is watching.

**Key Users & Usage Scenarios**
The only identified users are end-users (TV viewers). They use the application for social communication, checking email notifications, and seeing what friends are watching on TV.

**Major External Interfaces**
The primary interface is communication with the external .NET Messenger Service using the MSNPv8 protocol. User input is via remote control (and potentially a wireless keyboard). Output is displayed on a TV screen.

**Key Non-functional Requirements**
*(No explicit, measurable non-functional requirements are stated in the provided text.)*

**Constraints, Assumptions & Dependencies**
A critical dependency is the use of the .NET Messenger Service protocol (MSNPv8). The requirements specification must be adjusted if this protocol cannot be used.

**Priorities & Acceptance Approach**
*(No explicit prioritization or acceptance criteria are provided in the text.)*