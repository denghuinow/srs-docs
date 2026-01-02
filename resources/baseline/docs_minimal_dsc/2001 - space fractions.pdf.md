# Software Requirements Specification (SRS)
## Fraction Quest: A Web-Based Fraction Learning Game

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Approved for Development

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for "Fraction Quest," a web-based educational game designed to improve fraction-solving skills for sixth-grade students. This document is intended for use by the project stakeholders, development team, quality assurance team, and project management.

#### 1.2 Scope
Fraction Quest is a standalone, story-driven, multiple-choice game focused on fraction problems aligned with sixth-grade mathematics standards. The system includes:
*   A student-facing game interface with an introductory movie, main menu, and sequential gameplay.
*   A web-based administrative interface for teachers to update game questions without developer intervention.
*   An "umbrella" menu system that provides links to other, related math learning games within the same educational suite.
*   Real-time score feedback for students.

**Out of Scope:**
*   User account creation or login for students.
*   Tracking of student progress across sessions.
*   The development of the other math games linked from the umbrella menu.
*   Support for mathematical topics outside the defined sixth-grade fraction curriculum.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS:** Software Requirements Specification
*   **UI:** User Interface
*   **Admin:** Administrator (the teacher in this context)
*   **MCQ:** Multiple Choice Question

#### 1.4 References
*   Common Core State Standards for Mathematics, Grade 6
*   Macromedia Flash 5 Player Documentation
*   Project Charter: Fraction Quest, Version 1.0

#### 1.5 Overview
The remainder of this document details the overall description of the product, its specific requirements, and appendices. Specific requirements are presented with sufficient detail to enable design and testing.

---

### 2. Overall Description

#### 2.1 Product Perspective
Fraction Quest is a new, self-contained web application. It will be one of several games accessible via a shared "umbrella" portal for math games. It must operate within the constraints of a standard web browser with specific plugin support.

#### 2.2 Product Functions
The major functions of the product are:
1.  Display an introductory animation/movie upon first load.
2.  Present a main menu allowing navigation to "Start Game," "Umbrella Menu," and potentially "Replay Intro."
3.  Deliver a sequence of fraction-based MCQs within an engaging storyline context.
4.  Evaluate student answers and provide immediate visual and numerical score feedback.
5.  Provide a centralized menu (Umbrella Menu) with clickable links to launch other, external math games.
6.  Provide a secure, separate administrative web interface for authorized teachers to add, modify, or remove game questions and multiple-choice answers.

#### 2.3 User Characteristics
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **Student (Primary)** | Sixth-grade student using the game for learning and practice. | Limited attention span for complex instructions. Comfortable with mouse interaction. Mathematical skill level is at ~6th grade. May have varying reading proficiency. |
| **Teacher/Admin (Secondary)** | Educator managing the game content. | Computer literate but not necessarily a technical expert. Understands pedagogical goals and fraction curriculum. Requires a simple, intuitive interface for content management. |

#### 2.4 Constraints
1.  **Technical:** The application must run within a standard web browser (e.g., Internet Explorer 5+, Netscape Navigator 6+) equipped with **Macromedia Flash Player 5** and **JavaScript** enabled.
2.  **Input Method:** All user interaction, including navigation and answering questions, must be accomplished **solely via mouse clicks**. Keyboard input is explicitly prohibited.
3.  **Deployment:** The game must be accessible over the public Internet or a school intranet via a standard URL.
4.  **Maintainability:** Game questions and answers must be modifiable through a web-based admin interface, requiring no changes to the Flash source code or recompilation of the core game.

#### 2.5 Assumptions and Dependencies
*   It is assumed that the target machines in schools have the required browser and plugin (Flash 5) installed.
*   The development of the "other math games" linked from the Umbrella Menu is a separate project, but their launch URLs will be provided.
*   The administrative interface will require teacher authentication (basic mechanism to be defined).

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

**3.1.1 User Interfaces**
*   **UI-01: Introductory Movie.** A non-interactive (or click-to-skip) Flash animation introducing the game's storyline and characters.
*   **UI-02: Main Menu.** A graphical screen with clearly labeled, clickable buttons for: "Start Game," "Umbrella Menu," and "Replay Intro."
*   **UI-03: Game Play Screen.**
    *   Displays the storyline context (text/graphics).
    *   Presents a single fraction question in clear text.
    *   Shows 3-4 multiple-choice answer options as clickable buttons or regions.
    *   Includes a visual score indicator (e.g., "Score: 75/100") updated after each question.
    *   Provides a "Next Question" button (clickable) to proceed.
*   **UI-04: Umbrella Menu Screen.** A simple, graphical menu displaying icons or buttons for other math games. Each item is a clickable link that opens the respective game (likely in a new window or the same window).
*   **UI-05: Admin Interface.** A separate, password-protected web page (HTML/JavaScript). Contains forms to:
    *   List existing questions.
    *   Add a new question (with fields for question text, correct answer, 3-4 distractors).
    *   Edit an existing question.
    *   Delete a question.

**3.1.2 Hardware Interfaces**
None. The application runs entirely within the client browser.

**3.1.3 Software Interfaces**
*   **Browser:** Must interface with the host web browser's Flash 5 plugin and JavaScript engine.
*   **Data Storage:** The admin interface will require a backend mechanism (e.g., a simple database or flat-file system) to store and retrieve questions. The Flash game must be able to load the current question set from this storage (e.g., via an XML file or similar method generated by the admin system).

**3.1.4 Communications Interfaces**
The application must communicate over HTTP/HTTPS to load the game assets (SWF, graphics) and the dynamic question data file.

#### 3.2 Functional Requirements

**3.2.1 Student Game Functions**

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-1** | The system shall display an introductory movie upon the initial loading of the application. | High |
| **FR-2** | The system shall present a Main Menu with clickable options to "Start Game," "Access Umbrella Menu," and "Replay Intro." | High |
| **FR-3** | Upon selecting "Start Game," the system shall load and present the first fraction question within the defined storyline. | High |
| **FR-4** | The system shall present each question as text alongside 3-4 selectable, multiple-choice answers. Only mouse clicks shall be used for selection. | High |
| **FR-5** | Upon a student clicking an answer choice, the system shall immediately evaluate its correctness. | High |
| **FR-6** | The system shall update and display the student's cumulative numerical score after each answered question. | High |
| **FR-7** | After answering, the system shall display a "Next Question" button. Clicking it shall load and present the subsequent question in the sequence. | High |
| **FR-8** | Upon completion of the final question, the system shall display a final score screen and a button to return to the Main Menu. | Medium |
| **FR-9** | From the Main Menu, selecting "Umbrella Menu" shall display a screen with links to other, external math learning games. | High |
| **FR-10** | Clicking a game link in the Umbrella Menu shall open the target game application (navigation method to be specified). | High |

**3.2.2 Administrative Functions**

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-11** | The system shall provide a separate, web-based administrative login page accessible via a specific URL. | High |
| **FR-12** | The admin interface shall allow an authenticated user to view a list of all current fraction questions and their answer sets. | High |
| **FR-13** | The admin interface shall provide a form to add a new question, including fields for: Question Text, Correct Answer, and at least three Distractor Answers. | High |
| **FR-14** | The admin interface shall allow an authenticated user to edit the text and answer choices of any existing question. | High |
| **FR-15** | The admin interface shall allow an authenticated user to delete an existing question from the game. | Medium |
| **FR-16** | Any changes made via the admin interface shall be reflected in the student game the next time a game session is started or the question data is reloaded. | High |

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   The introductory movie and main menu should load within 5 seconds over a standard school Internet connection (e.g., 10 Mbps).
*   Transition between questions after clicking "Next" should feel instantaneous to the user (< 1 second).

**3.3.2 Safety & Security Requirements**
*   The administrative interface **must not** be linked from or accessible within the student game interface.
*   The admin interface shall require username/password authentication (basic security).

**3.3.3 Software Quality Attributes**
*   **Usability:** The student interface must be intuitive for a 6th grader. All interactive elements must be clearly identifiable and provide visual feedback on hover/click.
*   **Reliability:** The game must not crash or become unresponsive due to malformed question data. It should default to a safe state.
*   **Maintainability:** The separation of game logic (Flash) and question data (external file) is critical. Adding new questions must not require Flash recompilation.

---

### 4. Appendices

#### Appendix A: Question Data Format (Example)
The following is a proposed XML schema for the external question file:
```xml
<questions>
  <question id="1">
    <storyline>Captain Math is dividing treasure. He has 3/4 of a gold bar and needs to give 1/3 to his first mate. How much does he give?</storyline>
    <text>What is 1/3 of 3/4?</text>
    <answers>
      <answer correct="true">1/4</answer>
      <answer correct="false">3/7</answer>
      <answer correct="false">2/3</answer>
      <answer correct="false">1/2</answer>
    </answers>
  </question>
  <!-- More questions -->
</questions>
```

#### Appendix B: Wireframe Sketches
*(Link or placeholder for basic wireframes of Main Menu, Game Screen, and Admin List/Edit screens.)*

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance Lead | | | |