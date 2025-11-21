# Detailed Summary

## Background and Scope
This document specifies enhancements to Moodle for the University of Puget Sound to replace their existing Blackboard system. The scope includes developing core functionality currently unavailable in Moodle, with redesigns for consistency with university practices and improved user interface flow. Non-goals include complete Moodle replacement and fundamental architectural changes beyond the specified enhancements.

## Role Matrix and Use Cases
**Roles:** Student (primary content consumer), Professor (content administrator), System Administrator (system maintenance)

**Main Scenarios:**
- Student submits multiple assignment files
- Professor grades assignments with feedback
- Student records and organizes audio clips for language courses
- User searches course content efficiently
- System sends notifications for course updates

**Exception Scenarios:**
- Audio clip deletion from portfolio
- Grade dispute resolution using history
- Notification subscription management

## Business Process
**Main Process - Assignment Submission & Grading (8 steps):**
1. Student accesses assignment page
2. System checks upload configuration
3. Student selects multiple files
4. System validates file types/sizes
5. Student submits files
6. Professor reviews submission
7. Professor assigns grade with feedback
8. System updates gradebook and notifies student

**Key Branch - Audio Portfolio Management (4 steps):**
*Trigger:* Student initiates audio recording
1. Student records voice clip
2. System stores in speech-optimized format
3. Student previews and chooses archive option
4. System organizes into portfolio with metadata

## Domain Model
**Entities (8):**
- User (id: required/unique, role: required, email: required/unique)
- Course (id: required/unique, title: required, administrator: reference)
- Page (id: required/unique, type: required, feed_enabled: required)
- Assignment (id: required/unique, due_date: required, multiple_upload: required)
- AudioClip (id: required/unique, format: required, portfolio_id: reference)
- Grade (id: required/unique, score: required, assignment_id: reference, student_id: reference)
- Notification (id: required/unique, type: required, user_preference: required)
- SearchIndex (id: required/unique, content: required, page_id: reference)

## Interfaces and Integrations
**Web Interface** (Direction: User→System) - Theme: Unified administrative interface; Input: Course configuration; Output: Consistent page layouts; SLA: Responsive under 1000 concurrent users

**Email/SMS Gateway** (Direction: System→External) - Theme: Notification delivery; Input: Page updates; Output: Mobile/email alerts; SLA: Configurable delivery timing

**Audio Processing** (Direction: System→Internal) - Theme: Speech optimization; Input: Raw audio; Output: Compressed formats; SLA: Real-time conversion

**Backup System** (Direction: System→Internal) - Theme: Data protection; Input: Course data; Output: Nightly backups; SLA: 6-hour restoration

## Acceptance Criteria
**Multiple File Upload:** Given an assignment page with multiple upload enabled, when a student selects multiple files, then all files should be accepted and stored with the submission.

**Audio Portfolio:** Given a student with audio recording access, when they record and preview a clip, then they should be able to choose archive option and access it later.

**Course Search:** Given a logged-in user, when they enter search terms, then relevant course pages should be displayed categorized by content type.

**Grade Management:** Given a professor viewing an assignment, when they enter a grade with feedback, then the gradebook should update and maintain change history.

## Non-functional Metrics
**Performance:** Support 1000 concurrent users; Responsive interface under normal load

**Reliability:** 99% uptime expectation; Configurable backup schedule with 6-hour restoration

**Security:** Role-based access control; Student grade privacy protection

**Compliance:** Adherence to university data policies; RSS 2.0 feed standards

**Observability:** Comprehensive administrator documentation; Searchable maintenance database

## Milestones and Release Strategy
1. Core Moodle assessment and API familiarization
2. Priority 1 & 2 requirements implementation
3. User interface consistency improvements
4. Audio recording portfolio development
5. Notification system integration
6. Production deployment with selected Priority 3 features

## Risk List and Mitigation Strategies
**Moodle API Limitations** - Mitigation: Early prototyping and contingency planning
**Audio Format Compatibility** - Mitigation: Standardized codec selection and testing
**Performance Under Load** - Mitigation: Load testing during development
**User Adoption Resistance** - Mitigation: Gradual rollout with training
**Integration Complexity** - Mitigation: Modular development approach
**Data Migration Issues** - Mitigation: Comprehensive migration testing
**Notification System Reliability** - Mitigation: Redundant delivery mechanisms
**Maintenance Resource Constraints** - Mitigation: Self-service administrative tools

## Undecided Issues and Responsible Parties
**Final Moodle Version Selection** - Responsible: University IT Department
**Audio Storage Format Optimization** - Responsible: Development Team
**Notification Preference Defaults** - Responsible: University Administration
**Backup Frequency Configuration** - Responsible: System Administrators
**Third-party Wiki/Blog Integration** - Responsible: Development Team
**Search Engine External Integration** - Responsible: Not mentioned
**Mobile Interface Requirements** - Responsible: Not mentioned
**Long-term Audio Portfolio Retention** - Responsible: University Administration