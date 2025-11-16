# 2004 - philips.md

## System Overview
The Platform-i MSN application is an MHP (Multimedia Home Platform) version of the popular PC-based MSN Messenger, designed to demonstrate the capabilities of MHP and Platform-i.^[1]^ It enables users to see online friends, chat with them, and view the TV programs they are watching.^[2]^

## Key Requirements

### Functional Requirements
- **User Login**: Use an existing .^[3]^NET Passport account to log in to the messenger.^[4]^
- **Status Management**: Change and maintain user status visible to buddies.^[5]^
- **Buddy List**: Display the presence status of buddies and update in real-time.^[6]^
- **Messaging**: Send and receive instant messages, including emoticons.^[7]^
- **Group Chat**: Support chat sessions with multiple buddies.^[8]^
- **TV Program Info**: Request and display the TV program currently watched by buddies.^[9]^

### External Interface Requirements
- **Input Devices**: Remote control and possibly a wireless keyboard.^[10]^
- **Output Devices**: TV screen.^[11]^
- **Communication Protocol**: Use the .^[12]^NET messenger service protocol (MSNPv8).^[13]^

### Non-Functional Requirements
- **Performance**: Ensure clear and concise user interface with minimal latency.^[14]^
- **Usability**: Design for intuitive use by end-users.^[15]^
- **Security**: Utilize .^[16]^NET Passport for secure login.^[17]^

### Constraints and Assumptions
- **Protocol Availability**: Assumes the availability of the MSN messenger service protocol (MSNPv8).^[18]^
- **No File Transfer**: The xlet does not support file transfer or webcam functionality.
- **End-User Only**: The system is designed solely for end-users.^[19]^