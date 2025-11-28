# Software Requirements Specification (SRS)
## MSN Messenger for Platform-i

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft

---

## 1. Introduction

### 1.1 Purpose
This document describes the functional and non-functional requirements for the MSN Messenger application for Platform-i. The purpose of this application is to provide real-time text messaging capabilities via television sets while demonstrating the Multimedia Home Platform (MHP) capabilities of the Platform-i ecosystem.

### 1.2 Scope
The MSN Messenger for Platform-i is an independent MHP application that enables Platform-i users to:
- Manage their presence and buddy lists
- Engage in real-time text messaging
- View buddies' current TV programs
- Receive Hotmail notifications and display messages

**Out of Scope:**
- File transfers of any kind
- Webcam or video calling support
- Creation of new Passport accounts
- Integration with external systems beyond the specified protocols
- PC-based MSN Messenger features not explicitly listed

### 1.3 Definitions, Acronyms, and Abbreviations
- **MHP**: Multimedia Home Platform
- **MSNPv8**: .NET Messenger Protocol Version 8
- **IM**: Instant Messaging
- **TV**: Television
- **UI**: User Interface

### 1.4 References
- .NET Messenger Protocol (MSNPv8) Specification
- Platform-i Development Guidelines
- MHP Standards Documentation

### 1.5 Overview
This document is organized into sections covering overall description, specific requirements, and appendices. The requirements are structured to provide comprehensive guidance for developers, testers, and stakeholders.

## 2. Overall Description

### 2.1 Product Perspective
The MSN Messenger for Platform-i is a standalone MHP application operating within the TV environment. It functions independently without dependencies on other projects and is specifically designed to showcase Platform-i's multimedia capabilities.

**System Context Diagram:**
```
[TV Remote] → [Platform-i] → [MSN Messenger App] → [MSNPv8 Server]
                    ↓
               [TV Display]
```

### 2.2 Product Functions
The core functionality includes:
- Presence management and status updates
- Real-time text messaging with emoticon support
- Buddy list management operations
- Buddy status and nickname display
- TV program sharing capabilities
- Hotmail inbox integration

### 2.3 User Characteristics
**Single User Type:** End-users
- Interaction method: TV remote control
- Technical proficiency: Basic TV operation skills
- Permissions: Standard IM functions only
- No administrative privileges required

### 2.4 Constraints
- Must operate within MHP framework constraints
- Limited to MSNPv8 protocol compatibility
- TV remote control as primary input device
- TV screen resolution and display limitations
- No external system integration capabilities

### 2.5 Assumptions and Dependencies
**Assumptions:**
- Users have existing Passport accounts
- Platform-i hardware meets minimum requirements
- TV remote control is functional and compatible
- MSNPv8 protocol remains available and supported

**Dependencies:**
- Availability of MSNPv8 protocol (critical dependency)
- Platform-i MHP runtime environment
- TV display and remote control functionality

### 2.6 Apportioning of Requirements
Future enhancements may include:
- Additional protocol support if MSNPv8 becomes unavailable
- Enhanced multimedia features
- Extended messaging capabilities

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
**Input Interfaces:**
- TV remote control navigation
- On-screen keyboard input
- Button-based menu selection

**Output Interfaces:**
- TV screen display with MHP-compliant rendering
- Visual feedback for user actions
- Status indicators and notifications

**UI Characteristics:**
- Optimized for TV viewing distances
- Remote-control friendly navigation
- Clear, legible text and icons
- Consistent with Platform-i design guidelines

#### 3.1.2 Hardware Interfaces
- TV remote control input processing
- TV display output rendering
- Network connectivity for protocol communication

#### 3.1.3 Software Interfaces
**MSNPv8 Protocol Interface:**
```plaintext
Protocol: .NET Messenger Protocol Version 8
Function: Messaging, presence, and buddy list management
Authentication: Passport account credentials
Data Format: Protocol-defined message structures
```

**Platform-i MHP Interface:**
- MHP runtime environment integration
- TV display management
- Remote control event handling

#### 3.1.4 Communications Interfaces
- TCP/IP connectivity for MSNPv8 protocol
- Standard network port usage per protocol specification
- Error handling for network disruptions

### 3.2 Functional Requirements

#### 3.2.1 Presence Management

**REQ-PRESENCE-001: Status Updates**
```markdown
The system shall allow users to set their online status from predefined options:
- Available
- Busy
- Away
- Appear Offline
```

**REQ-PRESENCE-002: Buddy Visibility**
```markdown
The system shall display the online status of all buddies in the user's contact list.
```

**REQ-PRESENCE-003: Automatic Status Detection**
```markdown
The system shall automatically set status to "Away" after a period of inactivity.
```

#### 3.2.2 Real-time Text Messaging

**REQ-MESSAGING-001: Message Exchange**
```markdown
The system shall enable real-time text message exchange between logged-in users.
```

**REQ-MESSAGING-002: Emoticon Support**
```markdown
The system shall display standard emoticons within message conversations.
```

**REQ-MESSAGING-003: Session History**
```markdown
The system shall maintain and display conversation history for active messaging sessions.
```

**REQ-MESSAGING-004: Message Notification**
```markdown
The system shall provide visual notification for incoming messages.
```

#### 3.2.3 Buddy List Operations

**REQ-BUDDY-001: Add Buddy**
```markdown
The system shall allow users to add new buddies to their contact list using Passport addresses.
```

**REQ-BUDDY-002: Delete Buddy**
```markdown
The system shall allow users to remove buddies from their contact list.
```

**REQ-BUDDY-003: Block Buddy**
```markdown
The system shall allow users to block specific buddies from contacting them.
```

**REQ-BUDDY-004: Buddy Information Display**
```markdown
The system shall display buddy nicknames and current status.
```

#### 3.2.4 TV Program Sharing

**REQ-TVSHARE-001: Current Channel Display**
```markdown
The system shall display the current TV channel being watched by buddies.
```

**REQ-TVSHARE-002: Program Information**
```markdown
The system shall show basic program information for buddies' current channels.
```

#### 3.2.5 Hotmail Integration

**REQ-HOTMAIL-001: Inbox Notification**
```markdown
The system shall display notifications for new Hotmail messages.
```

**REQ-HOTMAIL-002: Message Display**
```markdown
The system shall allow users to view basic Hotmail message information.
```

### 3.3 Performance Requirements

**REQ-PERF-001: Response Time**
```markdown
The system shall respond to user inputs within 2 seconds under normal conditions.
```

**REQ-PERF-002: Message Delivery**
```markdown
The system shall deliver messages within 5 seconds of sending.
```

**REQ-PERF-003: Status Updates**
```markdown
The system shall update buddy status within 10 seconds of change.
```

**REQ-PERF-004: Concurrent Operations**
```markdown
The system shall support multiple simultaneous messaging sessions without degradation.
```

### 3.4 Design Constraints

**REQ-DESIGN-001: MHP Compliance**
```markdown
The application shall fully comply with MHP standards and Platform-i specifications.
```

**REQ-DESIGN-002: Resource Usage**
```markdown
The application shall operate within Platform-i memory and processing constraints.
```

**REQ-DESIGN-003: Remote Control Navigation**
```markdown
All functions shall be accessible using standard TV remote control inputs.
```

### 3.5 Software System Attributes

#### 3.5.1 Reliability
**REQ-RELIABILITY-001: Session Stability**
```markdown
The system shall maintain stable connections for continuous messaging sessions.
```

**REQ-RELIABILITY-002: Error Recovery**
```markdown
The system shall recover gracefully from network interruptions.
```

#### 3.5.2 Availability
**REQ-AVAILABILITY-001: Operational Uptime**
```markdown
The system shall be available whenever Platform-i is operational and connected.
```

#### 3.5.3 Security
**REQ-SECURITY-001: Authentication**
```markdown
The system shall authenticate users using existing Passport credentials.
```

**REQ-SECURITY-002: Data Privacy**
```markdown
The system shall not store sensitive user data locally.
```

#### 3.5.4 Maintainability
**REQ-MAINTAIN-001: Code Standards**
```markdown
The system shall adhere to Platform-i development standards for future maintenance.
```

### 3.6 Other Requirements

**REQ-OTHER-001: Protocol Adaptability**
```markdown
The system design shall accommodate changes if MSNPv8 protocol becomes unavailable.
```

## 4. Supporting Information

### 4.1 Appendix A: Protocol Details
MSNPv8 protocol implementation details and message formats.

### 4.2 Appendix B: Platform-i Specifications
Technical specifications of the target Platform-i environment.

### 4.3 Appendix C: Use Case Scenarios
Detailed use cases for typical user interactions.

#### Use Case 1: Initiate Chat Session
**Actor:** User  
**Preconditions:** User is logged in and online  
**Basic Flow:**
1. User selects buddy from contact list
2. System opens messaging interface
3. User composes message using on-screen keyboard
4. System sends message via MSNPv8
5. System displays conversation with sent and received messages

#### Use Case 2: Check Buddy TV Programs
**Actor:** User  
**Preconditions:** User is logged in  
**Basic Flow:**
1. User navigates to buddy list
2. System displays current channel information for each online buddy
3. User selects buddy to view detailed program information

#### Use Case 3: View Hotmail Notifications
**Actor:** User  
**Preconditions:** User has linked Hotmail account  
**Basic Flow:**
1. System displays notification indicator for new emails
2. User selects Hotmail notification area
3. System displays basic message information
4. User can view limited message details

---

**Document Approval:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Manager | | | |
| Development Lead | | | |
| Quality Assurance | | | |