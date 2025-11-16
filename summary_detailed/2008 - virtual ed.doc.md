# Detailed Summary

## Background and Scope
Virtual-ED is a distance learning platform being developed for NJIT to enhance online education through real-time collaboration tools. The system aims to create a classroom-like environment with features including audio/video streaming, instant messaging, file management, and online testing capabilities. Non-goals include supporting non-standard browsers beyond IE, Firefox, and Safari, and accommodating outdated database systems with limited concurrent user capacity.

## Role Matrix and Use Cases
**Roles:** System Administrator (full system control), Administrative End User (class management), Limited End User (profile management only)

**Use Cases:**
- User logs in and accesses dashboard
- Student joins video conference for lecture
- Professor hosts real-time exam session
- User customizes profile and interface preferences
- File upload/download with quota management
- Multi-user document collaboration
- Instant messaging with file transfer
- System administrator manages user enrollment

## Business Process
**Main Process - Course Participation:**
1. User authenticates with credentials
2. System displays personalized dashboard
3. User selects class/course
4. User accesses learning materials
5. User participates in real-time sessions
6. User submits assignments/tests
7. System records activity and updates grades
8. User logs out

**Key Branch - Technical Issues:**
1. User reports connectivity problem
2. System provides troubleshooting guide
3. If unresolved, escalates to help desk
4. Administrator resolves and notifies user

## Domain Model
**Entities:**
- User (username: required/unique, password: required, role: required)
- Course (courseID: required/unique, title: required, professor: reference)
- File (fileID: required/unique, name: required, size: required, owner: reference)
- Message (messageID: required/unique, content: required, timestamp: required)
- Exam (examID: required/unique, duration: required, questions: required)
- Profile (userID: required/unique, preferences: required, contact_info: required)
- Session (sessionID: required/unique, participants: required, type: required)
- Grade (gradeID: required/unique, score: required, student: reference)

## Interfaces and Integrations
- **NJIT User Database** (Inbound): Authentication sync, User data validation, SLA: 99% uptime
- **FTP Server** (Outbound): File transfer operations, Quota management, Input: File metadata, Output: Transfer status
- **Streaming Service** (Outbound): Audio/video delivery, Live and on-demand content, SLA: <2s latency
- **Email System** (Outbound): Notifications and alerts, System updates, Input: Message content, Output: Delivery confirmation

## Acceptance Criteria
**Video Conferencing:**
- Given user has webcam/microphone enabled, when joining video conference, then audio/video streams connect within 5 seconds

**File Management:**
- Given user has available storage quota, when uploading assignment file, then system confirms successful upload and updates available space

**Online Testing:**
- Given exam time limit is set, when student submits after deadline, then system rejects submission and notifies professor

## Non-functional Metrics
**Performance:** Video streaming latency <2s, File upload <30s for 100MB
**Reliability:** 99% system uptime, Automatic backup every 24 hours
**Security:** Password complexity enforcement, Data encryption in transit
**Compliance:** FERPA compliance for educational records, Accessibility standards (Section 508)
**Observability:** Real-time user activity monitoring, System performance dashboards

## Milestones and Release Strategy
1. Core authentication and user management (Release 1)
2. Basic messaging and file sharing (Release 1)
3. Video/audio streaming capabilities (Release 1)
4. Online testing framework (Release 2)
5. Advanced collaboration tools (Release 2)
6. Full system integration and optimization (Final Release)

## Risk List and Mitigation Strategies
1. **Limited database capacity** - Implement user session management and scaling plan
2. **Browser compatibility issues** - Standardize on supported browsers with fallback options
3. **Network bandwidth constraints** - Implement adaptive streaming and compression
4. **User adoption resistance** - Provide comprehensive training and support materials
5. **Security vulnerabilities** - Regular penetration testing and security audits
6. **System downtime during rollout** - Schedule deployments during low-usage periods
7. **Data loss during migration** - Implement phased migration with rollback capability
8. **Performance degradation** - Continuous monitoring and performance optimization

## Undecided Issues and Responsible Parties
1. Final storage capacity allocation - System Architects
2. Specific video codec standards - Technical Team
3. Backup frequency and retention policy - Infrastructure Team
4. Integration with existing campus systems - Integration Team
5. Mobile device support timeline - Product Management
6. Third-party tool licensing - Procurement Team
7. Data export formats - Technical Team
8. Long-term archive strategy - Not mentioned