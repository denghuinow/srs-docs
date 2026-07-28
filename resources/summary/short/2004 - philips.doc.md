# Short Summary: Platform-i MSN Messenger Xlet

## Background and Objectives
This document specifies the functional requirements for a Multimedia Home Platform (MHP) version of the MSN Messenger application, designed to demonstrate MHP and Platform-i capabilities. The primary objective is to enable instant text communication and presence sharing between users on a TV platform.

## In Scope
*   User presence management (login via .NET Passport, status updates, buddy list management).
*   Core messaging functions (sending/receiving text messages, emoticon support, group conversations).
*   Display of buddy nicknames and statuses.
*   TV program sharing feature to see what online buddies are watching.
*   Basic Hotmail integration for new mail notifications and inbox viewing.

## Out of Scope
*   File transfer capabilities between users.
*   Webcam or video chat support.
*   Creation of new .NET Passport accounts from the application.
*   Extensive game-playing features (implied as limited).
*   Detailed user interface design specifications.

## Stakeholders and Core Use Cases
**Stakeholders:**
*   **End User:** The TV viewer who uses the application to communicate with friends and family.
*   **Customer:** The entity commissioning the development of the MSN Messenger xlet.
*   **Development Team:** The engineers responsible for designing and building the application based on this specification.

**Core User Stories:**
1.  As an **End User**, I want to log in with my existing .NET Passport account so that I can access the messenger service.
2.  As an **End User**, I want to see the online status of my buddies so that I know who is available to chat.
3.  As an **End User**, I want to send and receive instant text messages with emoticons so that I can communicate in real-time.
4.  As an **End User**, I want to see which TV program my online buddy is watching so that we can share viewing experiences.
5.  As an **End User**, I want to be notified of new Hotmail messages so that I can check my inbox.
6.  As a **Development Team**, we need a clear specification of external protocols and interfaces so that we can design a compatible system.

## Success Metrics
*   Successful login and communication using the MSNPv8 protocol.
*   Accurate and real-time reflection of user and buddy presence status changes.
*   Reliable delivery and display of text messages between users.

## Major Constraints
*   The application must be developed as an MHP xlet for the TV platform.
*   It must interface using the standard .NET Messenger Service protocol (MSNPv8).
*   Input is primarily via remote control, with potential for a wireless keyboard.
*   Output is displayed solely on a TV screen.
*   The specification is dependent on the continued availability and compatibility of the MSN messenger service.

## Undecided Issues
*   Final user interface design and interaction details.
*   Specific implementation details for the "Play games" feature.
*   Potential use of a wireless keyboard as an input device.