# Software Requirements Specification (SRS)
## Space Fractions: An Interactive Educational Game

**Document Version:** 1.0
**Date:** [Current Date]
**Prepared for:** Ms. Andrea Brooks, Pecan Springs Elementary School
**Prepared by:** The Denominators Development Team
**Project Sponsor:** S2S Program

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the "Space Fractions" web-based educational game. It is intended to serve as a comprehensive guide for the development team, stakeholders, and project oversight, ensuring a common understanding of the system's capabilities, constraints, and goals.

#### 1.2 Scope
Space Fractions is an interactive, story-driven game designed to improve fraction-solving skills for sixth-grade students. The project comprises three main components:
1.  A Flash-based game with a narrative structure that presents multiple-choice fraction questions.
2.  A secure, web-based administrative tool (Question Updater) for modifying game content.
3.  A static "Math Umbrella" web page that provides organized links to other related S2S math projects.

The software will be hosted on the S2S web infrastructure and accessed via standard web browsers with the Macromedia Flash 5 plugin. The scope explicitly excludes the development of other projects linked from the Math Umbrella page.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS:** Software Requirements Specification
*   **S2S:** [Assumed: "Students to Software" or relevant program name]
*   **UI:** User Interface
*   **Admin:** Administrator
*   **URL:** Uniform Resource Locator
*   **ID:** Identifier

#### 1.4 References
*   Project Charter: Balanced Summary - Space Fractions
*   Macromedia Flash 5 Developer Documentation

#### 1.5 Overview
The remainder of this document details the overall description of the product, specific system features, external interface requirements, and other non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
Space Fractions is a new, self-contained component intended for integration into the existing S2S educational web ecosystem. It will link to and from a central "Math Umbrella" page but will operate independently.

#### 2.2 Product Functions
The major functions of the system are:
1.  Deliver an engaging, story-based educational game for fraction practice.
2.  Manage user sessions, track scores, and control narrative branching.
3.  Provide immediate feedback and a performance summary to the student.
4.  Allow an authorized administrator to update the game's question bank via a web form.
5.  Serve as an access point (via the Math Umbrella) to other S2S math resources.

#### 2.3 User Characteristics
| User Class | Characteristics | Key Expectations |
| :--- | :--- | :--- |
| **Sixth-Grade Student** | Primary end-user. Age 11-12. Varied computer literacy and fraction comprehension. Motivated by fun, story, and competition. | Intuitive, mouse-only interaction. Clear instructions. Engaging visuals and narrative. Immediate feedback. |
| **Game Administrator (Teacher)** | Computer-literate adult. Subject matter expert (fractions). Needs to tailor content to class curriculum. | Secure, simple web interface for content management. Reliable data saving. |
| **Development Team** | Technical experts in Flash ActionScript and web development. | Clear, modular code structure for maintainability. Well-documented requirements. |

#### 2.4 Constraints
1.  **Technical:** Must be built for Macromedia Flash Player 5.
2.  **Interface:** All gameplay must be controllable via mouse only.
3.  **Performance:** Core game movie file must be optimized for web delivery (target 1-2MB).
4.  **Platform:** Must be hosted on the existing S2S web server infrastructure.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** End-users will have access to a computer with a web browser and the Flash 5 plugin installed.
*   **Assumption:** The S2S server will provide stable hosting and support server-side scripting for the Question Updater.
*   **Dependency:** Final hosting URL and directory structure will be provided by S2S web infrastructure team.
*   **Dependency:** The list of projects and URLs for the Math Umbrella page will be supplied by the project sponsor.

### 3. System Features

#### 3.1 Feature 1: Interactive Game Play
**3.1.1 Description and Priority**
This is the core feature of the system. It provides the storyline, presents fraction questions, accepts user answers, manages session state, and delivers feedback. Priority: High.

**3.1.2 Stimulus/Response Sequences**
1.  **Stimulus:** User navigates to the game URL.
    *   **Response:** Introductory movie plays. A "Skip" button is available.
2.  **Stimulus:** Movie ends or user clicks "Skip".
    *   **Response:** Main Menu is displayed with options: "Start Game", "Help", "Team Info", "Math Umbrella".
3.  **Stimulus:** User clicks "Start Game".
    *   **Response:** Game session is initialized. The first story segment and the first multiple-choice question are displayed.
4.  **Stimulus:** User clicks on a multiple-choice answer.
    *   **Response:** System provides immediate visual/audio feedback (correct/incorrect), updates the session score, and advances the narrative. If the question is a "Critical Point," the story branch is updated.
5.  **Stimulus:** The final question is answered.
    *   **Response:** Ending Scene is displayed, showing final score, a narrative conclusion based on performance, and options to "Quit" or "Play Again".

**3.1.3 Functional Requirements**
*   **FR1.1:** The system shall play an introductory movie upon initial load, with a visible and functional "Skip" button.
*   **FR1.2:** The system shall present a Main Menu with, at minimum, "Start Game", "Help", and "Math Umbrella" buttons.
*   **FR1.3:** The system shall present one multiple-choice fraction question at a time within the context of the storyline.
*   **FR1.4:** The system shall evaluate the user's selected answer immediately upon click and provide clear visual feedback.
*   **FR1.5:** The system shall increment the user's score for a correct answer. The scoring algorithm is TBD (see Undecided Issues).
*   **FR1.6:** The system shall track the user's path through "Critical Point" questions to determine the appropriate story branch and ending.
*   **FR1.7:** The system shall display a final score and a story conclusion tailored to the user's performance at the end of the game.

#### 3.2 Feature 2: Question Management (Administrator)
**3.2.1 Description and Priority**
This feature provides a secure web interface for an administrator to modify the question bank used by the Flash game. Priority: High.

**3.2.2 Stimulus/Response Sequences**
1.  **Stimulus:** Administrator navigates to the Question Updater URL.
    *   **Response:** System presents a login form.
2.  **Stimulus:** Administrator enters valid credentials and submits the form.
    *   **Response:** System authenticates the user and presents a form populated with current question data (e.g., in a table or series of fields).
3.  **Stimulus:** Administrator modifies data (text, answers, flags) and clicks "Save".
    *   **Response:** System validates all input, writes the updated question data to a specified file on the server (format TBD), and confirms the save operation.

**3.2.3 Functional Requirements**
*   **FR2.1:** The system shall require username and password authentication to access the Question Updater interface.
*   **FR2.2:** The system shall display the existing set of questions, answers, and critical point flags in an editable format.
*   **FR2.3:** The system shall validate all administrator input (e.g., prevent empty question fields, ensure one correct answer is designated).
*   **FR2.4:** The system shall serialize the updated question data and save it to a server-side file in a format readable by the Flash game.

#### 3.3 Feature 3: Math Umbrella Portal
**3.3.1 Description and Priority**
This is a static web page that acts as a central menu linking to various S2S math projects, including Space Fractions. Priority: Medium.

**3.3.2 Functional Requirements**
*   **FR3.1:** The Math Umbrella page shall be accessible from the game's Main Menu.
*   **FR3.2:** The page shall display a categorized list (e.g., Fractions, Decimals) of S2S math project links (Title, URL).
*   **FR3.3:** The Space Fractions game shall be listed as one of the links on this page.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Game UI:** Implemented in Macromedia Flash 5. Must be entirely navigable via mouse clicks. Shall include: splash screen, main menu, story scenes, question/answer panels, feedback indicators, and score display.
*   **Admin UI:** Implemented as a standard HTML web form with server-side processing (e.g., PHP, Perl). Shall include: login screen, data entry/editing form, and save confirmation.

#### 4.2 Hardware Interfaces
None. The software is web-based and requires only standard client hardware (computer, mouse, monitor) and server hosting.

#### 4.3 Software Interfaces
*   **Flash Player:** The game component requires the Macromedia Flash Player 5 browser plugin.
*   **Web Server:** The Question Updater and Math Umbrella page require an S2S-supported web server (e.g., Apache) with server-side scripting capabilities.
*   **Data File:** The Flash game must read question data from a structured text file (e.g., XML, CSV) generated by the Question Updater.

#### 4.4 Communications Interfaces
Standard HTTP/HTTPS protocols for web access. No special communication interfaces are required.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NF1:** The main game Flash movie (.swf file) shall be optimized for web delivery with a target file size of 1-2MB.
*   **NF2:** The game shall load and begin the introductory movie within 30 seconds on a 56k modem connection.

#### 5.2 Safety Requirements
Not applicable.

#### 5.3 Security Requirements
*   **NF3:** Access to the Question Updater web form shall be protected by username and password authentication. Passwords shall be stored as hashed values.
*   **NF4:** The Question Updater shall implement input validation to prevent corruption of the question data file.

#### 5.4 Software Quality Attributes
*   **Usability:** The game shall be usable by a sixth-grade student with minimal instruction. All actions shall be accomplished with mouse clicks only.
*   **Maintainability:** The Flash code shall be structured modularly using sub-scenes and reusable components to facilitate future updates.
*   **Reliability:** The system shall undergo extensive unit, integration, and user-acceptance testing to minimize bugs and ensure stable operation.
*   **Portability:** The game shall be designed to run consistently across major web browsers (Internet Explorer, Netscape Navigator) that support Flash Player 5.

### 6. Other Requirements

#### 6.1 Appendices
*   **Appendix A: Data Definitions**
    *   **Question:** `{Question_ID, Question_Text, Correct_Answer, Distractor_1, Distractor_2, Distractor_3, Question_Type, Is_Critical_Point}`
    *   **User Session (Volatile):** `{Session_ID, Current_Score, Current_Question_Index, Branch_Path_Array}`
    *   **Administrator:** `{Admin_ID, Username, Password_Hash}`

#### 6.2 Index
[To be populated in final document.]

---

### **Undecided Issues & TBD (To Be Determined)**
The following items require resolution by the client and development team:
1.  The final number of questions and the identification of specific "Critical Point" questions.
2.  The detailed algorithm for calculating the user's score and any ranking system.
3.  The specific security protocol for the administrator login (e.g., HTTPS, password complexity rules).
4.  The finalized list and categorization of projects for the Math Umbrella page.
5.  The exact file format (XML, CSV, custom delimited) for the question data exchanged between the Question Updater and the Flash game.
6.  The definitive hosting path and URL on the S2S production server.