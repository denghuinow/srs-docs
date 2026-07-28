# Software Requirements Specification (SRS)
## For
### Space Fractions: An Interactive Educational Game
**Version:** 1.0  
**Date:** October 26, 2023  
**Prepared for:** Ms. Andrea Brooks, Pecan Springs Elementary  
**Prepared by:** The Denominators Development Team  
**Project Sponsor:** S2S (Student to Student) Project, The University of Texas at Austin

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the "Space Fractions" software system. It is intended to serve as a comprehensive guide for the development team, stakeholders, and project sponsors, ensuring a common understanding of the project's scope, features, and constraints.

### 1.2 Document Conventions
- Requirements are categorized as Functional (FR) or Non-Functional (NFR).
- Priority is indicated as: **High (H)**, **Medium (M)**, **Low (L)**.
- All user interface interactions are assumed to be via mouse click unless otherwise specified.
- Markdown formatting is used for structure and clarity.

### 1.3 Project Scope
Space Fractions is a web-based, interactive educational game designed to improve fraction-solving skills for sixth-grade students through an engaging, adaptive storyline. The system includes a core game and a separate administrative tool for content management. It is part of a larger "Math Umbrella" suite of educational games.

**In-Scope Components:**
1.  Client-side Flash-based game application.
2.  Introductory storyline movie.
3.  Main menu with navigation.
4.  Interactive game sequence with adaptive branching.
5.  Scoring and conclusion scene.
6.  Web-based administrative tool for question management.

**Out-of-Scope Items:**
1.  Keyboard-based input mechanisms.
2.  Local file storage or persistent user profiles on the client machine.
3.  Dependencies on software other than a standard web browser with Flash 5 and JavaScript.
4.  Any new hardware requirements for the end-user.
5.  Multi-user or collaborative gameplay within a single instance.

### 1.4 References
- Project Charter: "Space Fractions - Short Summary"
- Stakeholder Interviews
- Macromedia Flash 5 ActionScript Reference Guide

## 2. Overall Description

### 2.1 Product Perspective
Space Fractions is a self-contained, client-side web application. It will be hosted on a standard web server and accessed via a URL. It connects to a server-side component only for the administrative question updater functionality. The game is intended to be one title under a future "Math Umbrella" portal.

### 2.2 Product Functions (High-Level Features)
1.  **Story Presentation:** Deliver an introductory animated movie to set context.
2.  **Gameplay:** Present multiple-choice fraction questions within an interactive, branching narrative.
3.  **Adaptive Feedback:** Provide immediate correctness feedback and adapt the storyline based on user performance at defined "critical points."
4.  **Scoring & Assessment:** Calculate, display, and track a user's score throughout and at the end of the session.
5.  **Content Management:** Provide a secure, web-based interface for authorized administrators to update the game's question bank.
6.  **Help System:** Offer easily accessible instructions and game rules.

### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Sixth-Grade Student (Primary)** | Age 11-12; varying comfort with computers and math; motivated by graphics, story, and game mechanics. | Learn/practice fractions in a fun, engaging way; receive positive reinforcement; understand progress. |
| **Competitive Student (Bobby)** | Subset of primary user; highly motivated by scores, speed, and visible achievement. | Answer quickly, achieve a high score, and "win" the game. |
| **Technologically-Nervous Student (Alice)** | Subset of primary user; may be hesitant with new software. | Access clear help, navigate the game confidently without fear of making mistakes. |
| **Game Administrator (e.g., Teacher Claire)** | Educator with basic web literacy; no assumed programming knowledge. | Easily customize learning content (questions/answers) to match curriculum needs. |
| **Development Team (The Denominators)** | Computer science students; responsible for build and maintenance. | Create maintainable, well-documented code that meets all requirements. |

### 2.4 Operating Environment
- **Client-Side (Game):** Any internet-connected computer with a web browser capable of running **Macromedia Flash Player 5** and **JavaScript**.
- **Client-Side (Admin Tool):** Any modern web browser with forms support.
- **Server-Side (Admin Tool):** Standard HTTP server (e.g., Apache) with server-side scripting (e.g., PHP, Perl) to process form submissions and update a flat file or simple database.
- **Network:** Standard modem connection (56kbps). Total Flash movie size must be optimized for this constraint.

### 2.5 Design and Implementation Constraints
1.  **Technology Stack:** Must be developed primarily using Macromedia Flash 5 for the game interface and logic.
2.  **Input Method:** All user interaction must be achievable via mouse clicks only.
3.  **Performance:** Asset sizes (SWF, images) must be minimized to ensure acceptable load times over a 56kbps modem connection.
4.  **Maintainability:** Code must be modular, well-commented, and structured to allow future students to easily understand and modify it.
5.  **User Interface:** Must be highly graphical, intuitive, and visually appealing to sixth-grade students.

### 2.6 Assumptions and Dependencies
- The end-user's school or home computer has the Flash 5 plugin installed and enabled.
- The administrator has a basic understanding of fractions to create valid questions and answers.
- The "Math Umbrella" framework, when developed, will provide a standardized navigation method to launch this game.

## 3. System Features

### 3.1 Feature 1: Game Launch and Introduction
**Priority:** H
**Description:** Upon loading the application, the user is presented with an introductory animated movie.

**Functional Requirements:**
- **FR1.1:** The application shall automatically play a non-interactive introductory movie upon initial load. *(Priority: H)*
- **FR1.2:** The movie shall establish the game's storyline, characters, and primary objective. *(Priority: H)*
- **FR1.3:** A visible "Skip Intro" button shall be present, allowing the user to proceed directly to the main menu. *(Priority: M)*

### 3.2 Feature 2: Main Menu Navigation
**Priority:** H
**Description:** A central hub providing access to all game functions.

**Functional Requirements:**
- **FR2.1:** The main menu shall contain a minimum of three clickable buttons: "Start Game," "Help," and "The Team." *(Priority: H)*
- **FR2.2:** Selecting "Start Game" shall initiate the core game sequence (Feature 3). *(Priority: H)*
- **FR2.3:** Selecting "Help" shall display a screen with clear, concise instructions on how to play the game. *(Priority: H)*
- **FR2.4:** Selecting "The Team" shall display information about the development team (The Denominators). *(Priority: L)*
- **FR2.5:** A method to return to the main menu from the Help or Team screens shall be provided. *(Priority: M)*

### 3.3 Feature 3: Adaptive Gameplay Sequence
**Priority:** H
**Description:** The core interactive experience where users answer fraction questions that influence a branching storyline.

**Functional Requirements:**
- **FR3.1:** The game shall present fraction problems in a multiple-choice format (e.g., one question with 3-4 possible answers). *(Priority: H)*
- **FR3.2:** All answer choices shall be selectable via a mouse click. *(Priority: H)*
- **FR3.3:** Upon selecting an answer, the system shall provide immediate visual/audio feedback indicating "Correct" or "Incorrect." *(Priority: H)*
- **FR3.4:** The user's score shall be incremented for each correct answer and displayed persistently during gameplay. *(Priority: H)*
- **FR3.5:** The narrative shall branch at pre-defined "critical points" based on whether the user answered the preceding question correctly or incorrectly. *(Priority: H)*
- **FR3.6:** The difficulty and sequence of questions may be adapted based on user performance (exact logic TBD - see Undecided Issues). *(Priority: M)*

### 3.4 Feature 4: Game Conclusion and Scoring
**Priority:** H
**Description:** The final scene that concludes the story and summarizes the user's performance.

**Functional Requirements:**
- **FR4.1:** Upon completion of the question sequence, the game shall display a concluding narrative scene that resolves the storyline. *(Priority: H)*
- **FR4.2:** The final screen shall prominently display the user's total score (e.g., "You scored 8 out of 10!"). *(Priority: H)*
- **FR4.3:** The final message shall be customized based on the score achieved (e.g., "Galactic Hero!", "Good Job!", "Try Again!"). Exact criteria TBD. *(Priority: M)*
- **FR4.4:** An option to "Play Again" (returning to the main menu) shall be provided. *(Priority: M)*

### 3.5 Feature 5: Administrative Question Updater
**Priority:** H
**Description:** A web-based tool for authorized administrators to modify the game's question bank.

**Functional Requirements:**
- **FR5.1:** The tool shall be accessed via a separate URL from the main game. *(Priority: H)*
- **FR5.2:** Access shall be controlled by a username and password. *(Security mechanism TBD). *(Priority: H)*
- **FR5.3:** Upon authentication, the administrator shall be presented with a web form. *(Priority: H)*
- **FR5.4:** The form shall allow the administrator to: *(Priority: H)*
    - a. Select an existing question to edit.
    - b. Enter new question text.
    - c. Enter multiple answer choices (with one marked as correct).
    - d. Specify a difficulty level (e.g., Easy, Medium, Hard).
    - e. Specify an associated storyline branch or "critical point" identifier.
- **FR5.5:** The form shall include "Submit" and "Cancel" actions. *(Priority: H)*
- **FR5.6:** Upon submission, the tool shall validate the input (e.g., a correct answer is specified) and update the central question data file on the server. *(Priority: H)*
- **FR5.7:** The tool shall provide confirmation of a successful update or an error message. *(Priority: M)*

## 4. External Interface Requirements

### 4.1 User Interfaces
- The game shall have a consistent, space-themed graphical style.
- All buttons shall be large enough to be easily clicked by a child and provide visual feedback on hover/click.
- Text shall use clear, age-appropriate language and a readable font size.
- The administrative tool shall be a standard, clean web form with clear labels and instructions.

### 4.2 Hardware Interfaces
None required beyond standard PC/Mac input (mouse) and output (monitor, speakers) devices.

### 4.3 Software Interfaces
- **Flash Player:** The game client shall require Macromedia Flash Player 5 plugin.
- **Web Browser:** The game and admin tool shall function within Internet Explorer 5+, Netscape Navigator 4.7+, or equivalent contemporary browsers (circa 2001).
- **Server Script:** The admin tool backend shall interface with a server-side script (e.g., Perl/PHP) to read/write the question data file.

### 4.4 Communications Interfaces
- The game will be delivered via HTTP.
- The admin tool will use HTTP POST to send form data to the server.

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
- **NFR1:** The initial game load (including introductory movie) shall not exceed **1.5 MB** total to facilitate modem downloads. *(Priority: H)*
- **NFR2:** Feedback for a user's answer selection shall be displayed within **0.5 seconds**. *(Priority: H)*
- **NFR3:** Scene transitions within the game shall be seamless with a maximum delay of **2 seconds**. *(Priority: M)*

### 5.2 Safety Requirements
None identified.

### 5.3 Security Requirements
- **NFR4:** The administrative question updater shall require authentication. *(Priority: H)*
- **NFR5:** The password shall not be stored or transmitted in plain text. (Specific mechanism TBD). *(Priority: M)*
- **NFR6:** The game client shall not read from or write to the user's local file system. *(Priority: H)*

### 5.4 Software Quality Attributes
- **Maintainability:** The Flash ActionScript code shall be organized into logical functions and frames, with comments explaining complex logic. *(Priority: H)*
- **Usability:** A first-time user (Alice persona) shall be able to start the game and answer a question without assistance, using only the on-screen help if needed. *(Priority: H)*
- **Reliability:** The application shall not crash or become unresponsive under normal use conditions. *(Priority: H)*
- **Portability:** The game shall function identically on both Windows and Macintosh systems with the required browser/plugin configuration. *(Priority: M)*

## 6. Other Requirements

### 6.1 Success Metrics
1.  **Deployment Success:** The game is hosted and fully functional on the target web server, accessible from any connected computer with Flash 5.
2.  **Educational Efficacy:** A pre- and post-test assessment shows a measurable improvement in fraction-solving skills for a pilot group of sixth-grade students.
3.  **Administrator Usability:** The designated teacher (Claire) can successfully add, edit, or delete five questions using the updater tool without developer assistance.

### 6.2 Undecided Issues / Open Items
1.  The specific algorithm for the adaptive storyline: the definition of "critical points" and the exact narrative branches.
2.  The total number of questions per game session and the ratio of Easy/Medium/Hard questions.
3.  The final integration design and visual layout of the "Math Umbrella" menu system.
4.  The technical implementation for administrator password security (e.g., HTTP Basic Auth, hashed passwords in a file).
5.  The score ranges and corresponding textual feedback messages for the ending scene (e.g., 90-100% = "Galactic Hero!").

---
*This document approves the requirements for the Space Fractions project.*

**Signature:** _________________________
**Ms. Andrea Brooks, Client**
**Date:** _________________________

**Signature:** _________________________
**The Denominators, Team Lead**
**Date:** _________________________