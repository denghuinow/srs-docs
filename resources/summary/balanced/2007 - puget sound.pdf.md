# Balanced Summary: Moodle Puget Sound Enhancements

## Goals and Scope
This project aims to enhance the Moodle courseware system to better meet the educational needs of the University of Puget Sound, addressing core functional gaps identified in the existing Blackboard system. The scope includes implementing new features like audio recording and search, while redesigning the user interface for improved data flow and consistency with university practices. These enhancements are contingent on adopting Moodle and utilizing its existing APIs.

## Stakeholders and User Stories
*   **Students:** Primary consumers who access course materials, submit assignments, and participate in discussions.
*   **Professors:** Primary content administrators who upload materials, create collaborative spaces, and grade assignments.
*   **System Administrators:** Responsible for maintaining system configuration, updates, and overall platform health.

**User Stories:**
1.  As a professor, I want to enable multiple file uploads on specific assignment pages so that students can submit multi-part projects easily.
2.  As a foreign language student, I want to record and organize voice clips into a personal portfolio so that my oral progress can be tracked over time.
3.  As a student, I want to search for course pages and materials from any location within the system so that I can navigate and find information quickly.
4.  As a professor, I want to post grades and feedback for assignments online so that students receive timely evaluation.
5.  As a student, I want to subscribe to email or SMS notifications for new announcements so that I stay informed about course updates.
6.  As a system administrator, I want a centralized, simple interface to configure system settings and themes so that maintenance is efficient.

## Key Processes
1.  **Course Page Configuration:** Triggered by a professor creating or editing a course page, this process allows enabling/disabling features like multiple file uploads and web feeds.
2.  **Audio Clip Management:** Triggered by a student initiating a recording, this process captures, stores in a speech-optimized format, and archives voice clips into a personal portfolio.
3.  **System-Wide Search:** Triggered by a user entering a query, this process searches course content and returns categorized, relevant results.
4.  **Assignment Grading:** Triggered by a professor reviewing a submission, this process allows posting a grade with feedback and maintains a change history.
5.  **Notification Subscription:** Triggered by a page update (e.g., new announcement), this process sends alerts via the user's preferred channel (SMS/email).
6.  **System Backup:** Triggered on a configurable schedule, this process performs data backups to ensure protection and enable restoration within six hours.

## Domain Data Elements
*   **User:** (User ID) - Role, Name, Contact Information, Notification Preferences.
*   **Course:** (Course ID) - Title, Administrator(s), Enrollment List, Settings.
*   **Page/Resource:** (Page ID) - Title, Content Type (e.g., Assignment, Wiki), Parent Course, Configuration (uploads, feeds).
*   **Assignment:** (Assignment ID) - Due Date, Submission Status, Attached Files, Associated Grade.
*   **Gradebook Entry:** (Entry ID) - Score, Points Possible, Feedback, Timestamp, Grader.
*   **Audio Portfolio Entry:** (Clip ID) - Owner, Recording Date, Associated Course/Assignment, Audio File, Format.

## Non-functional Requirements
1.  **Usability:** The system must provide a simple, responsive, and configurable administrative interface to reduce page clutter.
2.  **Reliability:** The system must be available 99% of the time and support scheduled maintenance windows.
3.  **Performance:** The system must support at least 1000 concurrent users, particularly during peak academic periods.
4.  **Supportability:** The system must be maintainable with minimal modification to reduce IT staff effort.
5.  **Data Integrity:** System and course data must be backed up on a nightly basis with configurable schedules.
6.  **Documentation:** Comprehensive, searchable online help must be available for both end-users and system administrators.

## Milestones and External Dependencies
1.  Final decision by the University of Puget Sound to adopt Moodle as its primary courseware system.
2.  Completion of stakeholder interviews and final prioritization of enhancement requirements.
3.  Successful integration of chosen third-party wiki and blog engines (for social networking features).
4.  Establishment of a reliable SMS gateway service for notification delivery.
5.  Development and testing of the audio recording and portfolio management module.

## Risks and Mitigation Strategies
1.  **Risk:** University decides not to adopt Moodle, rendering enhancements moot.
    *   **Mitigation:** Frame requirements generically to apply to any courseware system and seek early commitment.
2.  **Risk:** Performance degradation under load of 1000+ concurrent users.
    *   **Mitigation:** Conduct rigorous load testing during development and optimize database queries and caching.
3.  **Risk:** Complexity of audio feature integration and storage management.
    *   **Mitigation:** Prototype the audio portfolio component early and define clear storage quotas and formats.
4.  **Risk:** User resistance to new interface and workflow changes.
    *   **Mitigation:** Involve stakeholder groups in UI/UX design reviews and provide clear documentation and training.
5.  **Risk:** Over-reliance on external services (e.g., for SMS notifications).
    *   **Mitigation:** Design notifications with fallback mechanisms (e.g., email-only) and choose reliable service providers.

## Undecided Issues
1.  The specific version of Moodle that will serve as the base for development.
2.  The precise allocation method and storage quotas for student audio portfolios.
3.  The selection of the specific third-party wiki and blog engines to be integrated.
4.  The detailed configuration options for the system-wide backup schedule and procedures.
5.  The extent of web search engine integration (e.g., Google) within the course search page.
6.  The final prioritization and inclusion of some Priority 3 features within the project timeline.