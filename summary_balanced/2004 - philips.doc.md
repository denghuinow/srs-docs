# Balanced Summary

## Goals and Scope
The Platform-i MSN application is an MHP version of the popular PC instant messenger, designed to demonstrate MHP and Platform-i capabilities. It enables users to see online friends, chat with them, and view which TV programs they are watching, while excluding file transfer and webcam support. The document establishes common understanding between customer and development team for architectural design.

## Roles and User Stories
- **End User**: I want to log in with my Passport account so that I can access the messenger service.
- **End User**: I want to view and change my online status so that buddies know my availability.
- **End User**: I want to send and receive instant messages so that I can communicate with buddies.
- **End User**: I want to see buddies' TV programs so that I know what they are watching.
- **End User**: I want to add/remove buddies from my contact list so that I can manage my contacts.

## Key Processes
1. **Trigger: User action** - Log in using existing .NET Passport credentials.
2. **Trigger: User action** - Manage contact list by adding/removing buddies.
3. **Trigger: System event** - Display and update buddy presence status automatically.
4. **Trigger: User action** - Initiate chat sessions with individual or multiple buddies.
5. **Trigger: Incoming message** - Notify user and display received messages.
6. **Trigger: User action** - Change personal nickname and status settings.
7. **Trigger: System event** - Show TV program information for online buddies.

## Domain Data Elements
- **User Account**: Passport ID, Password, Nickname, Status, Contact List
- **Buddy**: Buddy ID, Nickname, Status, User-defined Nickname, Blocked Status
- **Message**: Message ID, Sender, Recipient, Content, Timestamp
- **Chat Session**: Session ID, Participants, Message History, Start Time
- **TV Program**: Program ID, Channel, Title, Current Viewers
- **Email**: Email ID, Sender, Subject, Content, Received Time

## Non-functional Requirements
- Must use MSNPv8 protocol for messenger service communication
- Interface via remote control and potentially wireless keyboard
- Display output on standard TV screen
- Support MHP (Multimedia Home Platform) environment
- Maintain real-time status updates for buddy presence
- Provide responsive messaging with emoticon support

## Milestones and External Dependencies
- Dependence on .NET Messenger Service protocol availability
- Integration with MHP platform specifications
- Compatibility with existing .NET Passport authentication system
- Adherence to TV display output requirements
- Dependency on Hotmail service for email notifications

## Risks and Mitigation Strategies
- **Risk**: MSN messenger service protocol changes
  **Mitigation**: Document states FRS must be adjusted if protocol becomes unavailable
- **Risk**: Limited input methods on TV platform
  **Mitigation**: Support both remote control and optional wireless keyboard
- **Risk**: Feature parity with PC version expectations
  **Mitigation**: Clearly document limitations (no file transfer/webcam)
- **Risk**: Real-time communication performance on TV platform
  **Mitigation**: Optimize for MHP environment constraints

## Undecided Issues
- Final user interface design specifications
- Wireless keyboard support implementation details
- Hotmail integration scope and limitations
- Game functionality implementation approach
- Specific performance benchmarks and metrics
- Detailed error handling and recovery procedures