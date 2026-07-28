**Balanced Summary**

**Goals and scope**  
The Platform-i MSN project aims to develop an MHP (Multimedia Home Platform) xlet version of the MSN Messenger application for TV, enabling instant text communication, presence management, and integration with TV viewing. It will allow users to see online buddies, chat, and view buddies’ current TV programs, but excludes PC features like file transfer and webcam support.

**Stakeholders and user stories**  
*Stakeholders:*  
- **End-user:** TV viewer who uses the MSN Messenger xlet to communicate and see friends’ TV programs.  
- **Customer:** Entity commissioning the MSN Messenger xlet for demonstration of MHP capabilities.  
- **Development team:** Engineers responsible for designing and implementing the xlet based on this specification.  

*User stories:*  
1. As an end-user, I want to log in with my existing .NET Passport account so that I can access the messenger service.  
2. As an end-user, I want to see the online status of my buddies so that I know who is available to chat.  
3. As an end-user, I want to send and receive instant messages with emoticons so that I can communicate expressively.  
4. As an end-user, I want to add or remove buddies from my contact list so that I can manage my contacts.  
5. As an end-user, I want to see which TV program a buddy is watching so that we can share viewing experiences.  
6. As an end-user, I want to be notified of new Hotmail emails so that I can check my inbox.

**Key processes**  
1. **Login:** Triggered by user launching the xlet; authenticates via .NET Passport.  
2. **Presence management:** Triggered by user action; updates and displays user/buddy statuses.  
3. **Contact list management:** Triggered by user action; adds, removes, or blocks buddies.  
4. **Messaging:** Triggered by user initiating a chat; enables sending/receiving messages with emoticons.  
5. **Session history display:** Triggered during chat; shows message history for the current session.  
6. **TV program query:** Triggered by user request; retrieves and displays a buddy’s current TV channel/program.  
7. **Email notification:** Triggered by external event; alerts user to new Hotmail messages.

**Domain data elements**  
- **User Account:** Primary key: Passport ID; fields: nickname, status, buddy list, blocked list.  
- **Buddy:** Primary key: Passport ID; fields: nickname, status, user-assigned nickname, TV program.  
- **Message:** Primary key: message ID; fields: sender ID, receiver ID, content, timestamp, emoticons.  
- **Chat Session:** Primary key: session ID; fields: participant IDs, message history, start time.  
- **Email:** Primary key: email ID; fields: sender, subject, body, timestamp, read status.  
- **TV Program:** Primary key: program ID; fields: channel, title, broadcast time.

**Non-functional requirements**  
1. Must use the MSNPv8 protocol for communication with the .NET messenger service.  
2. Input via remote control and optional wireless keyboard; output displayed on TV screen.  
3. Real-time update of buddy status and nickname changes.  
4. Exclude file transfer and webcam functionality as in the PC version.  
5. Adhere to MHP platform constraints and standards.  
6. Ensure clear and intuitive user interface for TV interaction.

**Milestones and external dependencies**  
1. Finalize requirements specification approval.  
2. Dependency on .NET messenger service protocol (MSNPv8) availability and stability.  
3. Dependency on MHP platform compatibility and tools.  
4. Completion of xlet development and integration testing.  
5. Customer acceptance and demonstration.

**Risks and mitigation strategies**  
1. **Risk:** Changes to MSNPv8 protocol may break functionality. *Mitigation:* Monitor protocol updates and plan for adaptive integration.  
2. **Risk:** Inability to use MSN messenger service protocol. *Mitigation:* Adjust requirements to reflect alternative service if needed.  
3. **Risk:** Performance issues on TV hardware. *Mitigation:* Optimize xlet for MHP constraints and conduct performance testing.  
4. **Risk:** User interface not intuitive for TV remote control. *Mitigation:* Conduct usability testing with end-users.  
5. **Risk:** Delays due to external dependencies (e.g., MHP tools). *Mitigation:* Maintain close coordination with platform providers.

**Undecided issues**  
1. Final user interface design and layout details.  
2. Specific set of emoticons to be supported.  
3. Exact implementation of TV program retrieval mechanism.  
4. Handling of group conversation scalability.  
5. Integration details for Hotmail inbox display.  
6. Game functionality scope and implementation.