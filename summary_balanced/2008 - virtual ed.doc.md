# Balanced Summary

## Goals and Scope
Virtual-ED is a distance learning system designed for NJIT to create a classroom-like online environment. It aims to enhance communication between professors and students through features like audio/video streaming, file sharing, and online testing. The system will provide a secure application platform that supports real-time collaboration and learning material delivery.

## Roles and User Stories
- **System Administrator**: I want to manage system enrollment and virtual classes so that the platform remains organized and functional
- **Professor**: I want to conduct video lectures and online exams so that I can effectively teach remote students
- **Student**: I want to access lecture podcasts and collaborate on documents so that I can learn flexibly and work with classmates
- **Student**: I want to customize my profile interface so that I can personalize my learning environment
- **Professor**: I want to share applications and whiteboards so that I can demonstrate concepts visually during lectures

## Key Processes
1. User logs into Virtual-ED system (trigger: user authentication)
2. User selects desired feature from main menu (trigger: successful login)
3. User accesses file management tools for document sharing (trigger: file sharing selection)
4. User initiates real-time communication via instant messaging or video conferencing (trigger: communication request)
5. Professor creates and administers online exams (trigger: assessment need)
6. System manages file storage and user quotas (trigger: file upload/download)
7. User customizes interface preferences (trigger: profile settings update)

## Domain Data Elements
- **User Profile** (PK: UserID) - ContactInfo, Preferences, AccessLevel, CustomizationSettings
- **Course** (PK: CourseID) - CourseName, Instructor, EnrollmentList, Materials
- **File Storage** (PK: FileID) - FileName, Owner, StoragePath, AccessPermissions
- **Communication Session** (PK: SessionID) - Participants, SessionType, StartTime, Duration
- **Assessment** (PK: ExamID) - Questions, TimeLimit, SubmissionStatus, Grades
- **Lecture Content** (PK: ContentID) - MediaType, RecordingDate, AccessRights, Format

## Non-functional Requirements
- System must support 250 concurrent users
- 99% uptime availability requirement
- Compatible with IE, Firefox, and Safari browsers
- Minimum broadband connection required for video features
- Password policy enforcement (8-12 characters, quarterly changes)
- Data backup responsibility assigned to users

## Milestones and External Dependencies
- Integration with existing NJIT user database system
- Scheduled maintenance during low usage periods
- Staff training and acceptance of new system
- Hardware/software upgrades funding approval
- Browser compatibility validation

## Risks and Mitigation Strategies
- Current database may only support limited concurrent users (mitigation: phased rollout and monitoring)
- System downtime during development (mitigation: schedule deployments during low usage)
- User resistance to new system (mitigation: comprehensive training and support)
- Bandwidth limitations affecting video quality (mitigation: minimum requirements specification)
- Security breaches (mitigation: strict password policies and user education)

## Undecided Issues
- Language support for system documentation
- Specific media player requirements beyond Real Player
- Detailed quota management procedures
- Mobile device compatibility
- Integration depth with other campus systems
- Long-term storage policies for user data