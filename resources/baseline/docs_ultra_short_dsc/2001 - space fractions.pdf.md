# Software Requirements Specification (SRS)
## Fraction Quest: An Interactive Story-Based Math Game

**Document Version:** 1.0  
**Date:** [Current Date]  
**Prepared for:** Elementary School Teacher & S2S Project  
**Prepared by:** [Your Name/Organization]

---

### 1. Introduction

#### 1.1 Purpose
This document describes the functional and non-functional requirements for "Fraction Quest," a web-based, interactive game designed to improve fraction-solving skills for sixth-grade students. This SRS is intended for use by the project stakeholders, developers, testers, and project managers to guide the design, implementation, and verification of the system.

#### 1.2 Scope
The product is a standalone, storyline-based quiz game focused on fraction problems. Its core features include an introductory movie, an adaptive question sequence, a scoring system, and an administrative interface for question management. The system also includes an "umbrella" menu linking to other Student-to-Student (S2S) math projects.

**In-Scope:**
*   A Flash-based interactive game playable within a standard web browser.
*   A graphical, mouse-driven user interface.
*   A storyline that adapts based on user answers.
*   A web-based administrative tool for updating the question bank.
*   Integration with the S2S website via an umbrella menu.

**Out-of-Scope:**
*   Teaching new mathematical concepts or providing instructional content.
*   Accepting keyboard or text input from the student user.
*   Functioning outside of a web browser environment.
*   Operating without the Macromedia Flash 5 plug-in.
*   User account creation or management for students.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **S2S:** Student to Student, the series of educational projects this product belongs to.
*   **Flash:** Macromedia Flash 5, the multimedia software platform required to run the game.
*   **UI:** User Interface.
*   **Admin:** Administrator (the teacher role).

#### 1.4 References
*   Project Charter and initial request from the elementary school teacher.
*   S2S Website Technical Guidelines.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general product description. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements, including performance, security, and constraints.

### 2. Overall Description

#### 2.1 Product Perspective
This product is a new, independent component of the S2S project series. It is not dependent on any other software system but will be hosted on the existing S2S website infrastructure. It interacts with a web server solely for file retrieval (the game SWF, question data files) and for the administrative update functionality.

#### 2.2 Product Functions
The high-level functions of the product are:
1.  Deliver an engaging introductory animation to establish a narrative context.
2.  Present a main menu for starting the game, accessing help, and navigating.
3.  Administer a sequence of multiple-choice fraction questions, where the story progression adapts based on user choices and correctness.
4.  Calculate and display a final score at the conclusion of the game, along with a story ending tailored to the user's performance.
5.  Provide a secure, web-based interface for an administrator to modify the bank of questions and answers.
6.  Offer a centralized menu ("umbrella menu") to access other S2S math games.

#### 2.3 User Characteristics
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **Student (Primary)** | Sixth-grade students using the game to practice fractions. | Basic computer and Internet literacy. Familiar with mouse operations. Subject knowledge aligns with 6th-grade fraction curriculum. No keyboard input required. |
| **Teacher/Admin** | The classroom teacher who manages the game content. | Computer literate. Has authority to update educational content. Requires secure access to the administrative tool. |

#### 2.4 Constraints
*   **Technical:** Must execute within a web browser with the Macromedia Flash 5 plug-in installed.
*   **Input:** The student interface is constrained to mouse-only input.
*   **Size:** The core game Flash movie file must be 1-2 MB or less to facilitate reasonable download times.
*   **Platform:** Must be compatible with any major web browser (Internet Explorer, Netscape Navigator) that supports Flash 5 and JavaScript.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** End-users (students and teacher) possess basic computer navigation skills.
*   **Assumption:** The hosting S2S web server is operational and configured correctly.
*   **Critical Dependency:** The end-user's computing environment must have the Macromedia Flash 5 plug-in installed and enabled.
*   **Dependency:** The product's network security is reliant on the security features of the host web browser and server.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

**3.1.1 User Interfaces**
*   **UI-01:** All student-facing screens shall be graphical, animated, and navigable exclusively via mouse clicks.
*   **UI-02:** The introductory movie shall play automatically upon game load or via a menu option.
*   **UI-03:** The main menu shall provide clearly labeled buttons for: "Start Game," "Help," "Replay Intro," and "Umbrella Menu."
*   **UI-04:** Question screens shall display a fraction problem, 3-4 multiple-choice answer options as clickable buttons, and a visual element tied to the storyline.
*   **UI-05:** The ending scene shall prominently display the final score (e.g., "You scored 8/10") and a paragraph of story conclusion text.
*   **UI-06:** The administrative interface shall be a separate, password-protected web page with form fields for entering new questions, multiple-choice answers, correct answer index, and associated storyline path data.

**3.1.2 Hardware Interfaces**
*   None. The game runs within the browser, which manages all hardware interaction.

**3.1.3 Software Interfaces**
*   **SI-01:** The client-side game shall require the **Macromedia Flash 5 plug-in**.
*   **SI-02:** The game shall be embedded in an HTML page that may use **JavaScript** for basic page functionality (e.g., embedding the Flash object).
*   **SI-03:** The administrative tool shall interact with the web server (via HTTP POST/GET) to upload and save the updated question data file (e.g., XML or structured text).

**3.1.4 Communications Interfaces**
*   **CI-01:** The game shall communicate via standard HTTP/HTTPS protocols to load the initial game asset and the external question data file.

#### 3.2 Functional Requirements

**3.2.1 Game Flow & Student Experience**
*   **FR-01:** The system shall play an introductory animation upon user initiation.
*   **FR-02:** The system shall present a main menu from which the user can start the game, view help, or exit to the umbrella menu.
*   **FR-03:** Upon starting the game, the system shall load the first question based on the predefined storyline.
*   **FR-04:** The system shall present one fraction question at a time, formatted as a multiple-choice problem.
*   **FR-05:** The system shall accept only mouse clicks on provided answer choices as input.
*   **FR-06:** Upon selection of an answer, the system shall immediately check it against the correct answer.
*   **FR-07:** The system shall adapt the subsequent storyline path and question selection based on the correctness of the answer (adaptive storyline).
*   **FR-08:** The system shall track the number of correctly answered questions throughout the session.
*   **FR-09:** After the final question, the system shall display an ending scene which includes:
    *   **FR-09.1:** The total score (e.g., "X out of Y correct").
    *   **FR-09.2:** A unique narrative conclusion paragraph based on the user's score/performance tier.
*   **FR-10:** From the ending scene, the user shall be able to return to the main menu.

**3.2.2 Administrative Functions**
*   **FR-11:** The system shall provide a separate administrative login page accessible via a known URL.
*   **FR-12:** The administrative interface shall require a valid username and password for access.
*   **FR-13:** Once authenticated, the administrator shall be able to view the current list of questions, answers, and storyline mappings.
*   **FR-14:** The administrator shall be able to add a new question, including its text, answer choices, correct answer index, and storyline logic tags.
*   **FR-15:** The administrator shall be able to edit or delete any existing question.
*   **FR-16:** Upon saving changes, the system shall update a persistent data file on the web server that is loaded by the Flash game.

**3.2.3 Umbrella Menu**
*   **FR-17:** The system shall provide an "Umbrella Menu" option from the main menu.
*   **FR-18:** Selecting the Umbrella Menu shall navigate the user (open a new page or frame) to a central S2S hub page listing links to other related math games.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   **PER-01:** The main downloadable game asset (the .swf file) shall be **1-2 MB or less** in size.
*   **PER-02:** The game shall load and display the first interactive screen within 10 seconds on a standard 56k modem connection.
*   **PER-03:** User feedback (e.g., response to an answer click) shall be visually apparent within 0.5 seconds.

**3.3.2 Safety & Security Requirements**
*   **SEC-01:** The student-facing game shall not collect, transmit, or store any personal user data.
*   **SEC-02:** Administrative access shall be protected by a password. Password management (change, recovery) is out of scope and relies on web server security.
*   **SEC-03:** The game's security is contingent upon the security model of the web browser and the Flash Player plug-in.

**3.3.3 Software Quality Attributes**
*   **MAIN-01:** **Maintainability:** The question bank shall be stored in an external, modifiable file (not hard-coded in the Flash movie) to allow updates without recompiling the core game.
*   **USAB-01:** **Usability:** The game shall be intuitive for a sixth-grade student to navigate without written instructions. Visual and audio feedback shall be used to indicate correct/incorrect answers.
*   **PORT-01:** **Portability:** The game shall function identically on any major web browser (IE 5+, Netscape 6+) that meets the Flash 5 plug-in requirement.

### 4. Appendices

#### 4.1 Acceptance Criteria Summary
Acceptance of the final product will be based on successful demonstration of the following core scenarios:
1.  A student can launch the game, watch the intro, navigate the menu, complete a series of adaptive questions, and receive a correct final score and story conclusion.
2.  An administrator can log in via the web tool, successfully add a new fraction question, save it, and then have that new question appear in a subsequent student game session.
3.  The game functions correctly on two different browser environments with Flash 5 installed.
4.  The core game file size is within the 1-2 MB limit.

#### 4.2 Open Issues
*   The specific format of the external question data file (XML, CSV, etc.) is to be determined during design.
*   The mechanism for the "adaptive storyline" (e.g., branching logic table) requires detailed design.

---
*This document has been prepared to accurately reflect the requirements for the Fraction Quest project as of the date above.*