# Balanced Summary

## Goals and Scope
This document specifies enhancements to Moodle for the University of Puget Sound's courseware system. The scope includes developing core functionality currently unavailable in Moodle while maintaining compatibility with existing APIs. These enhancements aim to improve the learning experience and address shortcomings in the current Blackboard system.

## Roles and User Stories
- **Student**: I want to upload multiple assignment files so that I can submit complex projects efficiently
- **Student**: I want to record and organize voice clips so that I can track language learning progress
- **Professor**: I want to configure web feeds per page so that I can control notification delivery
- **Professor**: I want to grade assignments online so that I can provide timely feedback
- **System Administrator**: I want to manage system backups on a configurable schedule so that data is protected

## Key Processes
1. **Course Setup** (triggered by semester start): Course administrators create and configure course pages with appropriate features enabled
2. **Content Management** (triggered by ongoing instruction): Professors upload materials and configure notification settings
3. **Assignment Submission** (triggered by due dates): Students submit assignments and audio recordings through the system
4. **Grading** (triggered by submission): Professors review and grade submitted work with feedback
5. **Search Navigation** (triggered by user need): Users search course content to quickly locate materials
6. **Notification Delivery** (triggered by content updates): System sends email/SMS alerts for page changes
7. **System Maintenance** (triggered by schedule): Administrators perform backups and system updates

## Domain Data Elements
- **User**: (UserID) - Role, Email, Phone, Preferences, PortfolioSpace
- **Course**: (CourseID) - Name, Description, Administrator, StartDate, EndDate
- **Assignment**: (AssignmentID) - Title, DueDate, PointsPossible, MultipleFilesEnabled, FeedEnabled
- **Grade**: (GradeID) - Score, Feedback, Timestamp, AssignmentID, StudentID
- **AudioClip**: (ClipID) - Format, Duration, StoragePath, CreationDate, OwnerID
- **Page**: (PageID) - Type, Content, FeedSetting, NotificationSetting, CourseID

## Non-functional Requirements
- Support at least 1000 concurrent users during peak periods
- Maintain 99% uptime with 24/7 availability
- Provide simple, responsive interface across all functions
- Enable configurable backup schedules with 6-hour restoration capability
- Ensure system maintainability with minimal IT staff intervention
- Store audio in speech-optimized formats with MP3 conversion for download

## Milestones and External Dependencies
- Integration with existing Moodle APIs and architecture
- Compatibility with university authentication systems
- Support for RSS 2.0 web feed standards
- Implementation of SMS notification gateways
- Adoption decision timeline for Moodle platform

## Risks and Mitigation Strategies
- **API compatibility issues**: Maintain close alignment with Moodle development team
- **Performance under load**: Conduct stress testing with 1000+ concurrent users
- **Data migration complexity**: Develop phased migration plan from Blackboard
- **User adoption resistance**: Provide comprehensive training and documentation
- **Audio storage capacity**: Implement finite space allocation per user

## Undecided Issues
- Specific Moodle version for implementation
- Final backup frequency configuration
- SMS gateway provider selection
- Wiki and blog engine integration choices
- Audio format optimization parameters
- Final theme and interface customization details