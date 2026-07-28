# Software Requirements Specification (SRS)
## For Space Fractions Educational Game
**Version:** 1.0
**Date:** October 26, 2023
**Prepared for:** Ms. Andrea Brooks, Client
**Prepared by:** The Denominators Development Team
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the "Space Fractions" software system. It is intended to serve as a comprehensive guide for the development team, stakeholders, and testers, ensuring a common understanding of the project's scope, features, and constraints.

### 1.2 Scope
Space Fractions is a web-based, interactive educational game designed to improve fraction-solving skills for sixth-grade students. The system comprises:
*   A standalone Flash-based game with a branching storyline.
*   A "Math Umbrella" web portal linking to other related educational projects.
*   A secure administrative web interface for teachers to update game questions.

**In-Scope:**
*   Gameplay via mouse interaction in a web browser with Flash 5.
*   A set of multiple-choice fraction questions integrated into a narrative.
*   A password-protected HTML interface for content management.
*   A static HTML page for the Math Umbrella portal.
*   Hosting on a standard web server.

**Out of Scope (Non-Goals):**
*   Keyboard-based navigation or input.
*   Integration with other educational software platforms or gradebooks.
*   Support for specialized hardware.
*   Persistent user accounts or long-term student progress tracking beyond a single session.
*   Accessibility features for students with disabilities (acknowledged as a limitation).

### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS:** Software Requirements Specification.
*   **S2S:** Students to Software program.
*   **SWF:** Shockwave Flash, the file format for Flash movies.
*   **HTML:** HyperText Markup Language.
*   **HTTP:** Hypertext Transfer Protocol.
*   **Admin:** Game Administrator (e.g., Teacher).
*   **UI:** User Interface.

### 1.4 References
*   Project Charter and initial meeting notes with Ms. Andrea Brooks.
*   S2S Program Guidelines.

### 1.5 Overview
The remainder of this document describes the overall product perspective, features, and constraints. It details specific functional requirements, external interfaces, and non-functional attributes.

## 2. Overall Description

### 2.1 Product Perspective
Space Fractions is a new, self-contained component of the broader S2S educational ecosystem. It will be linked from the central "Math Umbrella" portal but will operate independently. The system interacts with users through a web browser and relies on a web server for file delivery and data persistence.

### 2.2 Product Functions
The major functions of the system are:
1.  **Interactive Game Play:** Deliver an engaging, story-driven sequence of fraction problems with immediate feedback.
2.  **Content Management:** Provide a secure interface for authorized administrators to modify the question bank.
3.  **Resource Navigation:** Serve as an entry point (via the Math Umbrella) to other S2S math projects.
4.  **Session Management:** Track a student's progress, score, and story path during a single gameplay session.

### 2.3 User Characteristics
| Stakeholder | Role | Characteristics & Expectations |
| :--- | :--- | :--- |
| **Sixth-Grade Student** | Primary User | Age 11-12. Comfortable with basic mouse use. Motivated by games, stories, and visual feedback. May have varying levels of fraction knowledge. |
| **Game Administrator (e.g., Teacher)** | Secondary User | Educator with basic computer literacy. Needs a simple, secure way to update educational content without technical expertise. |
| **Ms. Andrea Brooks (Client)** | Sponsor/Reviewer | Represents the educational need. Provides pedagogical input and final acceptance. |
| **Development Team** | Creator/ Maintainer | Software engineering students responsible for building, testing, and deploying the system. |
| **Dr. Vicki L. Almstrum** | Academic Oversight | Ensures project aligns with S2S program goals and academic standards. |
| **Mr. Keith Henning** | Technical Mentor | Provides technical guidance, architecture review, and risk assessment. |

### 2.4 Constraints
1.  **Technical:** Must run on standard school computers (circa 2001) with web browsers supporting Macromedia Flash Player 5 and JavaScript.
2.  **Network:** Must be usable over typical school internet connections (e.g., 56k modems).
3.  **Development:** Built by a student team within a single academic semester.
4.  **Input:** Navigation and interaction are limited to mouse clicks.

### 2.5 Assumptions and Dependencies
*   The target school's computer lab has the Flash 5 plugin installed or can install it.
*   A web server with appropriate file write permissions will be available for hosting and for the admin updater functionality.
*   The list of projects for the Math Umbrella will be provided by the S2S program.

## 3. System Features and Requirements

### 3.1 Feature 1: Interactive Game Play
**Description:** The core Flash-based game presents a space-themed story interspersed with fraction questions.

**3.1.1 Functional Requirements:**
*   **FR1.1:** The system shall play an introductory animation upon initial load, which can be skipped by a user mouse click.
*   **FR1.2:** The system shall display a main menu with "Start Game," "Help," and "Team Link" options.
*   **FR1.3:** Upon starting the game, the system shall present a story segment followed by a multiple-choice fraction question.
*   **FR1.4:** The system shall prevent the user from proceeding to the next question until an answer option is selected.
*   **FR1.5:** Upon answer selection, the system shall immediately validate it against the correct answer.
    *   **FR1.5.1:** If correct, the system shall display positive feedback (visual/audio) and advance to the next story segment/question.
    *   **FR1.5.2:** If incorrect, the system shall display instructive feedback and re-present the same question for a second attempt. The score for that question shall be recorded as incomplete.
*   **FR1.6:** The system shall track and display a cumulative score based on correct first-attempt answers.
*   **FR1.7:** At predefined story points, the system shall branch the narrative based on the correctness of the answer to a specific "critical" question.
*   **FR1.8:** After the final question, the system shall display an ending scene that includes the final score, a story conclusion tailored to performance, and options to "Return to Menu" or "Exit."

### 3.2 Feature 2: Administrative Question Updater
**Description:** A password-protected web interface allows administrators to modify the game's question bank.

**3.2.1 Functional Requirements:**
*   **FR2.1:** The system shall present a login form requiring a password to access the updater interface.
*   **FR2.2:** The system shall authenticate the provided password against a stored hash before granting access.
*   **FR2.3:** Upon authentication, the system shall display a form with fields for: Question Text, Answer Option 1-4, and a selector for the Correct Answer.
*   **FR2.4:** The system shall load existing question data into the form for editing.
*   **FR2.5:** The system shall perform validation on form submission. Validation includes:
    *   **FR2.5.1:** Question Text field cannot be empty.
    *   **FR2.5.2:** All Answer Option fields cannot be empty.
    *   **FR2.5.3:** Exactly one Correct Answer must be selected.
*   **FR2.6:** If validation fails, the system shall display a clear error message and not save the data.
*   **FR2.7:** If validation passes, the system shall write the updated question set to a structured configuration file (e.g., XML, JSON, or custom text format) on the server.

### 3.3 Feature 3: Math Umbrella Portal
**Description:** A static HTML page that organizes and links to other S2S math projects.

**3.3.1 Functional Requirements:**
*   **FR3.1:** The system shall display a categorized list of links to other S2S educational projects (e.g., Fractions, Decimals).
*   **FR3.2:** Each link shall display the project title and category.
*   **FR3.3:** When a user clicks a project link, the system shall open the corresponding project URL in a new browser window or tab.

### 3.4 Feature 4: System Configuration and Data
**Description:** The game reads its core content from external configuration files.

**3.4.1 Functional Requirements:**
*   **FR4.1:** The Flash game shall load question data (text, options, correct answer) from an external configuration file provided by the web server.
*   **FR4.2:** The Flash game shall load story branch logic from a predefined internal or external script.
*   **FR4.3:** The Math Umbrella page shall load its list of links from a static HTML file or a simple data file.

## 4. External Interface Requirements

### 4.1 User Interfaces
*   **Game UI:** Implemented in Macromedia Flash. Includes animated scenes, clickable buttons, text displays, and progress indicators. Input is exclusively via mouse click.
*   **Admin Updater UI:** Implemented in HTML with form elements. Includes text inputs, radio buttons, and a submit button.
*   **Math Umbrella UI:** Implemented in static HTML. Includes headings, categorized lists, and hyperlinks.

### 4.2 Hardware Interfaces
None. The system requires only standard PC hardware with a mouse and a network interface.

### 4.3 Software Interfaces
*   **Web Browser:** The client must use a web browser (e.g., Internet Explorer 5+, Netscape Navigator) with Macromedia Flash Player 5 plugin installed and JavaScript enabled.
*   **Web Server:** The system requires an HTTP web server (e.g., Apache, IIS) to host the SWF, HTML, and data files.

### 4.4 Communications Interfaces
Communication via standard HTTP/HTTPS protocols for serving files and submitting the admin form.

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
*   **PER-1:** The main game Flash file shall be optimized to a size of 1-2 MB.
*   **PER-2:** The introductory movie and main menu shall begin playback within 60 seconds over a 56k modem connection.
*   **PER-3:** The game shall use progressive streaming to begin gameplay before the entire file is downloaded.
*   **PER-4:** All user interface responses (e.g., button highlights, feedback displays) shall occur within 500ms of a mouse click under normal conditions.

### 5.2 Safety Requirements
Not applicable.

### 5.3 Security Requirements
*   **SEC-1:** Access to the Question Updater shall require password authentication.
*   **SEC-2:** The administrator password shall be stored in a hashed format on the server.
*   **SEC-3:** The game shall not collect, store, or transmit any personally identifiable information (PII) of students.
*   **SEC-4:** The admin update form shall validate data on the server-side to prevent corruption of the question file.

### 5.4 Software Quality Attributes
*   **Reliability:** The game shall be robust against crashes during normal operation. Target uptime for the web server during school hours is >95%.
*   **Maintainability:** The question data shall be separated from game logic to allow easy updates via the admin interface.
*   **Observability:** The Flash game shall log critical errors (e.g., missing asset files) to the browser console if possible. The admin updater shall provide clear success or failure messages upon form submission.

### 5.5 Compliance Requirements
*   **COM-1:** The software shall be compatible with standard web browsers and the Macromedia Flash 5 plugin as commonly configured in school environments circa 2001.

## 6. Other Requirements

### 6.1 Business Rules
*   A student is allowed a maximum of two attempts per question.
*   Only a correct answer on the first attempt contributes positively to the final score.
*   The narrative branches only at specific, predefined questions.

### 6.2 Acceptance Criteria
**Feature: Game Play**
*   **AC1:** Given a student is presented with a question, when they select the correct answer on the first try, then the game shall display positive feedback, increment the score, and advance the story.
*   **AC2:** Given a student selects an incorrect answer, when they are presented with the same question again, then their score shall not increment for that question, and they shall proceed after the second attempt (regardless of correctness).

**Feature: Content Update**
*   **AC3:** Given an admin is logged into the updater, when they submit a form with all fields valid and complete, then the system shall save the data and confirm the save successfully.
*   **AC4:** Given an admin submits a form without selecting a correct answer, when they click save, then the system shall display an error message and the question file shall remain unchanged.

### 6.3 Undecided Issues & TBDs
| Issue | Description | Responsible Party |
| :--- | :--- | :--- |
| **TBD-1** | Final number of questions and difficulty progression. | Dev Team + Ms. Brooks |
| **TBD-2** | Specific password storage and transmission security protocol. | Dev Team + Mr. Henning |
| **TBD-3** | Final list/categorization of projects for Math Umbrella. | Dev Team + S2S (Dr. Almstrum) |
| **TBD-4** | Detailed scoring algorithm and mapping to final feedback. | Development Team |
| **TBD-5** | Fallback procedure for missing Flash plugin. | Development Team |

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Client Representative | Ms. Andrea Brooks | | |
| Development Lead | [Name, The Denominators] | | |
| Mentor | Mr. Keith Henning | | |