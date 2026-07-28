**Purpose & Scope**
The system is a set of enhancements to the Moodle courseware system to address the University of Puget Sound's instructional needs, replacing Blackboard. It focuses on adding core functionality currently missing. It does not constitute a completely new system and assumes development will use Moodle's existing APIs.

**Product Background / Positioning**
This is an enhancement project for Moodle, which is being evaluated as a replacement for the existing Blackboard courseware system. The goal is to refine Moodle to better support diverse teaching methods and improve the learning experience at the university.

**Core Functional Overview**
*   Configure and enable multiple file uploads on specific course pages.
*   Record, organize into a portfolio, and manage audio clips (e.g., for language assignments).
*   Provide web feeds (e.g., RSS) for course content, configurable per page.
*   Search for content within courses and across the system.
*   Grade assignments online and maintain a grade history.
*   Provide integrated wiki and blog engines for collaboration.
*   Send email and SMS notifications for changes to course pages.

**Key Users & Usage Scenarios**
*   **Students**: Consume content, submit assignments, participate in discussions and collaborations.
*   **Professors (Course Administrators)**: Create and manage course content, grade assignments, configure features like file uploads and notifications.
*   **System Administrators**: Maintain system configuration, perform backups, and handle updates.

**Major External Interfaces**
The system interfaces with users via a web browser. It must send notifications via external email and SMS gateways. It will integrate existing third-party wiki and blog software.

**Key Non-functional Requirements**
*   **Performance**: Support at least 1000 concurrent users.
*   **Reliability/Availability**: Target 99% uptime, acknowledging necessary maintenance windows.
*   **Reliability**: System data must be backed up on a configurable schedule, with the ability to restore from backup within six hours.
*   **Maintainability**: The system must be maintainable by a limited IT staff without substantial modification.

**Constraints, Assumptions & Dependencies**
*   Development is dependent on and constrained by the existing Moodle platform and its APIs.
*   It is assumed Moodle is a viable candidate to replace Blackboard, but the requirements define needed functionality for any potential system.

**Priorities & Acceptance Approach**
Priority 1 (Core) and Priority 2 requirements are mandatory for the initial release. Priority 3 requirements will be included as time and budget allow. Acceptance is based on delivering the specified functional capabilities and meeting the quantified non-functional targets (e.g., concurrent user support, backup restore time).