# Moodle Software Requirements Specification for Puget Sound Enhancements

## 1. Introduction

### 1.1 Purpose
This document captures the description and requirements of a new courseware system for the University of Puget Sound's educational needs. It describes functional requirements with background discussions and nonfunctional requirements necessary to provide a complete and comprehensive description of the software requirements.

### 1.2 Scope
This document deals with immediate requirements for developing core functionality currently unavailable in Moodle. The University's enhancements to Moodle will embody several small redesigns for consistency with other university practices and redesign the user interface to reflect a more natural flow of data. The enhancements will utilize existing APIs made available by Moodle.

### 1.3 Definitions, Acronyms and Abbreviations
- Actor: Synonymous with user, describes users performing actions in use cases
- Course Administrator: Actor acting as professor or system administrator with ability to manage courses and course pages
- Courseware System: Software to facilitate electronic classroom management, electronic grading, assignment submission, discussion, and other learning tools
- System: Existing courseware system, new courseware system, or modifications being made to Moodle

### 1.4 References
- Moodle Requirements Brainstorming.pdf: Results of stakeholder interviews forming foundation for this document

### 1.5 Overview
This is a working document subject to change, initially incomplete and requiring continuing refinement. Requirements may be modified and additional requirements added as development progresses. This document forms the basis for continuing discussions with stakeholders and sponsors to enhance and further describe requirements for future enhancements to Moodle.

## 2. Overall Description

### 2.1 Assumptions
The University of Puget Sound is investigating Moodle as an option to replace Blackboard. This document determines what any courseware system would need to qualify as a viable solution for the University and applies this to Moodle to determine whether features lacking in Moodle but important to stakeholders can be implemented.

### 2.2 Product Characteristics
Moodle is a courseware system that manages courses, assignments, wiki pages, forums, etc. The goal is to refine parts of Moodle to provide functionality that improves the overall learning experience of students and helps professors present material in new ways. The University believes Blackboard is not providing the functionality students and faculty need to encourage learning.

### 2.3 User Characteristics

#### 2.3.1 Students
Students are primary consumers of the courseware system, accessing information posted by professors, uploading assignments and project files, and discussing concepts.

#### 2.3.2 Professors
Professors are primary content administrators, uploading files, links, and multimedia, grading assignments, and creating new places for students to discuss and collaborate.

#### 2.3.3 System Administrators
System administrators maintain the courseware system, contributing minimally to courses but spending more time modifying system configuration and making updates.

### 2.4 Stakeholder Needs
Stakeholders (professors and students) were interviewed to determine what is lacking in the existing courseware solution. Requirements are based on feedback summarized in Moodle Requirements Brainstorming.pdf.

## 3. Specific Requirements

### 3.1 Multiple File Transfer (Priority 2)
The system must capture and manage files where appropriate. Actors in the role of course administrator should be able to optionally upload multiple files where useful, such as on a devoted project page.

#### 3.1.1 The system must allow for multiple file upload to be configured on a per-page basis
Actors in the capacity of course administrator or professor should be able to enable multiple file uploads on a page of their choosing. For collaborative projects, it becomes important for actors to upload more than one file to a given page, especially for assignments with multiple parts.

### 3.2 Audio Recording (Priority 2)
The system must capture and organize voice clips that can be used where appropriate. The current courseware system's shortcoming is that the foreign language department cannot capture and track voice clips recorded by students for oral homework.

#### 3.2.1 The system must allow actors to organize their voice clips into a portfolio
Equal and finite drive space needs to be allotted to each actor in the role of professor or administrator to store voice clips recorded and submitted by students. Actors should be able to partition this space for students, either by previewing clips before archiving or automatically archiving clips. Maintaining an archive makes it possible to compare clips to determine improvement in language skills over multiple courses.

#### 3.2.2 The system must allow actors to download their voice clips in a flexible format
Voice clips should be optionally downloadable in MPEG Audio (mp3) format since it is widely supported across different web browsers and operating systems.

#### 3.2.3 The system must store audio clips in a format conducive to speech
Voice clips should be stored in a format optimized for speech. Recordings should only be converted to MPEG Audio (mp3) format when being downloaded; a separate viewer should be provided for listening to clips in Moodle.

#### 3.2.4 The system must allow actors to delete recorded clips
Actors should be able to examine their portfolio to select and delete clips if they choose, allowing them to manage archived voice clips and create a cohesive portfolio for professors to judge improvement over time.

### 3.3 Web Feeds (Priority 1)
The system must display web feeds (such as RSS 2.0 feeds) for all pages where elements such as forum posts, assignment postings, announcements, wiki alterations and other blocks of information are added. Actors in the role of course administrators should determine which components have feeds and to whom these feeds should pertain.

#### 3.3.1 The system must allow web feeds to be turned on or off on a per-page basis
Actors in the course administrator role may not feel the need to provide web feeds for every page in their course. During page creation and editing, that actor should be able to toggle web feed availability.

### 3.4 Search (Priority 2)
The system must use search functionality as a way to navigate Moodle pages instead of using hierarchical links. Moodle can be difficult to navigate and requires too many clicks to be efficiently used.

#### 3.4.1 An actor must be able to search through pages in a course
Actors should be able to search for pages at the course level. The search feature should be present in two ways:
1. Search box and "Search" button on the top or bottom of every page
2. Dedicated page for searching the course management system with filtering options and search by specific sections

#### 3.4.2 The system must display a search box on every page after an actor has logged in
Actors should be able to search from any page. If outside a particular course, each course should be searched with results grouped by course. If inside a course, that course should be searched with an option to search all courses.

### 3.5 Gradebook (Priority 1)
The system must allow actors in the capacity of course administrator to post grades associated with assignments for students. Professors may want to optionally grade assignments online since they are submitted electronically.

#### 3.5.1 A course administrator must be able to grade an assignment
Course administrators should be able to post grades for an assignment based on the ratio of points earned to points possible, attach feedback in text or attachment form, and have timestamps attached to the last modification time.

#### 3.5.2 The system should display grade information to the appropriate actor
The system should display grade information such as grade for each assignment, averages, and overall grade to the actor to whom the grades belong. No other actor should view another's grades except course administrators for the course.

#### 3.5.3 The system should maintain a grade history
The system should maintain a history of grades for a particular assignment if the course administrator changes them, allowing actors to review grade information if scores change and wish to dispute it.

### 3.6 Social Networking Applications (Priority 3)
The social, collaborative components of Moodle are not very robust. Better, freely-available solutions should be integrated into Moodle to provide the best functionality possible for all actors without using 3rd party services.

#### 3.6.1 The system must provide a wiki where actors can collaboratively create networks of documents
A freely available wiki should provide a simple markup language for styling input and linking to other pages. Having the wiki inside Moodle reduces confusion and allows for integration of notifications and logins.

#### 3.6.2 The system must provide a blog engine
A freely available blog engine should provide all modern blog functionality such as tagging, drafting, and comments. These blogs should share authentication and notification with Moodle.

### 3.7 Notifications (Priority 3)
Currently, there is no system that allows actors to receive SMS or email notifications of changes to Moodle pages.

#### 3.7.1 The system must provide both e-mail and SMS notifications for pages
When a page is created, the actor in the role of course administrator should be able to toggle whether notifications are turned on. By default, they should be turned on for announcements. If notifications are turned off, students should be able to subscribe to notifications. Students should select in their preferences whether notifications are sent to mobile telephone (via SMS) or e-mail account and manage notification subscriptions.

## 4. General System Functional Requirements

### 4.1 Usability
#### 4.1.1 As far as possible, the system should provide a simple, responsive interface
The system should be configurable from a single source at a central administrative position and provide a central, easy-to-use interface that reduces page clutter. The system should meet this requirement with a single administrative interface rather than individual links for editing each page, allowing administrators to easily change themes and other settings affecting page layout across the entire courseware system.

### 4.2 Reliability
#### 4.2.1 The system must be backed up on a configurable schedule
Back-up requirements will be determined based on individual components. The system should be backed up nightly with options for weekly, off-site backup when necessary. The system must have the ability and capacity to restore back-up data within six hours so it is never offline for an inordinate period.

#### 4.2.2 The system should be available 24 hours a day, 7 days a week
This provides a general sense of system availability. The system should not exclude maintenance windows or scheduled downtime. 99% up-time should be considered sufficient to meet this requirement.

### 4.3 Performance
#### 4.3.1 The system should support at least 1000 concurrent users
This provides a general sense of reliability when the system is under load. It is important that a substantial number of actors access the system simultaneously since a courseware system is important to courses that employ it. The system must handle at least 1,000 concurrent users, especially during midterm and finals weeks.

### 4.4 Supportability
#### 4.4.1 The system must be maintainable without substantial modification
Due to limited staff in the Office of Information Services, the system must be mostly self-sustaining to reduce FTE hours spent maintaining the system and simplify maintenance tasks.

### 4.5 Design Constraints

### 4.6 On-line User Documentation and Help System Requirements
#### 4.6.1 Relevant, online documentation for users should be available on each page
Users must have easy access to help while interacting with the system. Adequate user documentation should minimize Help Desk calls about system problems. Modifications should be reported via the main page to inform actors of unexpected changes. Electronic documentation should be supplemented with phone and on-site support.

#### 4.6.2 System administrators must have access to comprehensive, searchable documentation
A comprehensive database of maintenance tasks and help files should be compiled to make the courseware system easier to maintain from an IT staff point-of-view. Search results should be displayed based on relevance, covering all procedures necessary for regular maintenance, common errors, and advanced troubleshooting.

### 4.7 Interfaces
#### 4.7.1 User Interfaces
#### 4.7.2 Hardware Interfaces
#### 4.7.3 Software Interfaces
#### 4.7.4 Communications Interfaces

### 4.8 Licensing Requirements

### 4.9 Applicable Standards

### 5. Supporting Information
