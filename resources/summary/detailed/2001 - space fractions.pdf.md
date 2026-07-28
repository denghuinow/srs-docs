# Detailed Summary: Space Fractions

## Background and Scope
Space Fractions is a web-based, interactive educational game designed to improve fraction-solving skills for sixth-grade students. The project includes a standalone game with a storyline and a "Math Umbrella" web menu linking to other math-related S2S projects. The game provides feedback based on player scores and allows teachers to update questions via an administrative interface. Non-goals include supporting keyboard input, requiring specialized hardware, or integrating with other educational software platforms.

## Stakeholders Matrix and Use Cases
*   **Ms. Andrea Brooks (Client/Teacher):** Represents the school's needs, provides initial requirements, and will use the system to administer and update game content.
*   **Sixth-Grade Student (Primary User):** Uses the game to learn and practice fraction skills through an interactive, story-driven experience.
*   **Game Administrator (e.g., Teacher Claire):** Manages game content by updating questions and answers via a secure web interface.
*   **Development Team (The Denominators):** Designs, develops, tests, and maintains the software.
*   **Dr. Vicki L. Almstrum (Professor):** Provides academic oversight and connects the project to the broader S2S program.
*   **Mr. Keith Henning (Team Mentor):** Offers technical guidance and review throughout the development process.

**Main Scenarios:**
1.  Student launches the game, watches/skips the intro movie, and navigates the main menu to start playing.
2.  Student progresses through a series of multiple-choice fraction questions, receiving immediate feedback; correct answers advance the plot, while incorrect ones offer a retry.
3.  Game concludes by displaying the student's score and a story ending based on performance, then offers options to quit or replay.
4.  Administrator logs into the question updater, modifies question data via web forms, and saves changes to the server.

**Exception Scenarios:**
1.  Student attempts to proceed with an incomplete answer (system enforces selection).
2.  Administrator enters invalid data (e.g., incomplete question) in the updater (system validates input and requests correction).
3.  User's browser lacks the required Flash plugin (game cannot start, may need fallback message).
4.  Network issues interrupt game loading (movie playback may stall or fail).

## Business Process
**Main Process: Student Game Play**
1.  **Trigger:** Student accesses the game URL via a web browser.
2.  **Input:** Student loads the page; optional mouse click to skip intro.
3.  **Step 1:** Introductory movie plays (or is skipped).
4.  **Step 2:** Main menu displays with options (Start Game, Help, Team Link).
5.  **Step 3:** Student clicks "Start Game."
6.  **Step 4:** Game Sequence begins: displays a story-based fraction question.
7.  **Step 5:** Student selects a multiple-choice answer.
8.  **Step 6:** System validates answer: if correct, shows success and loads next question; if incorrect, shows feedback and allows retry (score impacted).
9.  **Step 7:** Repeats Steps 4-6 for a set number of questions; at critical points, story branches based on correctness.
10. **Step 8:** Final question completed; system transitions to Ending Scene.
11. **Step 9:** Ending Scene displays final score, story conclusion, and options (Return to Menu/Exit).
12. **Output:** Student learning experience, final score, and optional replay path.

**Key Branch A: Administrator Updates Questions**
1.  **Trigger:** Administrator navigates to the Question Updater URL.
2.  **Input:** Administrator enters password.
3.  **Step 1:** System authenticates password.
4.  **Step 2:** Administrator accesses web form, edits question text, answers, and correct option.
5.  **Step 3:** Administrator submits changes.
6.  **Step 4:** System validates data and writes updates to a configuration file on the server.
7.  **Output:** Updated question set for the game.

**Key Branch B: Accessing the Math Umbrella**
1.  **Trigger:** User accesses the Umbrella menu URL.
2.  **Input:** User mouse click on a project link.
3.  **Step 1:** System displays categorized links to other S2S math projects.
4.  **Step 2:** User selects a link.
5.  **Step 3:** System opens the selected project in a new browser window.
6.  **Output:** User accesses a separate, related educational resource.

## Domain Model
*   **Game Session:** `sessionId` (unique), `currentScore`, `currentQuestionIndex`, `storyBranchPath`.
*   **Question:** `questionId` (unique), `questionText` (required), `questionType` (e.g., arithmetic, equivalence), `associatedStorySegment`.
*   **Answer Option:** `optionId` (unique), `questionId` (reference), `optionText` (required), `isCorrect` (boolean, required).
*   **Student Profile:** `studentIdentifier` (local/session), `scoresHistory` (list of past game scores).
*   **Administrator:** `adminId` (unique), `passwordHash` (required).
*   **Game Configuration:** `configVersion`, `questionsFile` (reference to data file), `umbrellaLinksFile`.
*   **Story Branch:** `branchId` (unique), `triggerQuestionId` (reference), `condition` (correct/incorrect), `nextSegmentId`.
*   **Umbrella Project:** `projectId` (unique), `projectTitle` (required), `projectURL` (required), `topicCategory` (e.g., fractions, decimals).

## Interfaces and Integrations
*   **User Web Browser (Primary Interface):**
    *   **Direction:** System to User.
    *   **Interaction:** Displays Flash movies (intro, menu, game, ending) and HTML pages (umbrella, updater).
    *   **Input Key Points:** Mouse clicks only for navigation and answer selection.
    *   **Output Key Points:** Animations, sound feedback, score display, story graphics.
    *   **SLA Key Points:** Intro/menu movies load in <1 min on modem; main game starts playback before full download.
*   **Web Server (Hosting):**
    *   **Direction:** System to/from Browser.
    *   **Interaction:** Serves static Flash (SWF) files, HTML pages, and the dynamic question data file.
    *   **Input Key Points:** HTTP requests for game assets.
    *   **Output Key Points:** Delivers game files and updated question configuration file.
    *   **SLA Key Points:** High availability during school hours; support for concurrent user sessions.
*   **Question Updater (Admin Interface):**
    *   **Direction:** Administrator to System.
    *   **Interaction:** Password-protected HTML form for data entry.
    *   **Input Key Points:** New question text, answer options, correct answer identifier.
    *   **Output Key Points:** Writes a structured text file to the server filesystem.
    *   **SLA Key Points:** Form validation prevents corrupt data; changes reflect in the game after server file update.

## Acceptance Criteria
**Capability: Play Game Sequence**
*   Given a student has started the game and is presented with a fraction question, when they select the correct answer, then the game displays positive feedback and advances to the next story segment.
*   Given a student has answered a question incorrectly, when they are presented with the same question again, then their score for that question is marked as incomplete, and they proceed after the second attempt.

**Capability: Update Game Content**
*   Given an administrator is authenticated in the Question Updater, when they submit a complete and valid set of new question data, then the system saves the data to the server and the new questions appear in the next game session.
*   Given an administrator submits a question with a missing correct answer flag, when they click save, then the system displays an error and does not update the question file.

## Non-Functional Metrics
*   **Performance:** Main game Flash movie (1-2MB) should begin playback within a few minutes on a standard 56k modem connection. The interface must respond to mouse clicks with visual feedback within 500ms.
*   **Reliability:** The game shall be extensively tested to ensure no crashes during normal gameplay. The web server hosting the game shall aim for >95% uptime during school operating hours.
*   **Security:** The Question Updater shall be protected by password authentication. The game itself shall not collect or transmit personal student data.
*   **Compliance:** The product must run on standard web browsers (circa 2001) with the Macromedia Flash 5 plugin and JavaScript enabled.
*   **Observability:** The game shall log critical errors (e.g., missing asset files) to the browser console if possible. Administrator actions in the updater should be confirmable via success/failure messages.

## Milestones and Release Strategy
1.  **Milestone 1:** Core Flash game engine complete (intro, menu, basic question loop).
2.  **Milestone 2:** Complete set of fraction questions integrated with branching storyline.
3.  **Milestone 3:** Question Updater web interface developed and tested.
4.  **Milestone 4:** Math Umbrella landing page with categorized links completed.
5.  **Milestone 5:** Internal alpha testing with team and mentor.
6.  **Milestone 6:** Beta release to client (Ms. Brooks) for feedback, followed by final deployment to S2S web server.

## Risk List and Mitigation Strategies
1.  **Risk:** Flash plugin not installed or supported on target school computers.
    *   **Mitigation:** Clearly state system requirements upfront; provide instructions for downloading the plugin.
2.  **Risk:** Game file size too large for slow school internet connections.
    *   **Mitigation:** Optimize Flash assets (graphics, sound); design game to stream and play progressively.
3.  **Risk:** Branching storyline logic becomes too complex to manage.
    *   **Mitigation:** Use a simple, predefined story graph; limit the number of major branching points.
4.  **Risk:** Question Updater allows creation of invalid question data (e.g., no correct answer).
    *   **Mitigation:** Implement robust server-side and client-side form validation.
5.  **Risk:** Lack of student engagement with the educational content.
    *   **Mitigation:** Involve the client teacher in reviewing storyline and question design for age-appropriateness.
6.  **Risk:** Difficulty integrating with existing S2S umbrella structure.
    *   **Mitigation:** Early coordination with S2S administrators to understand linking and hosting protocols.
7.  **Risk:** Team inexperience with Flash development leads to schedule delays.
    *   **Mitigation:** Allocate time for learning; use simple Flash features; seek mentor guidance.
8.  **Risk:** The game is not accessible to students with disabilities.
    *   **Mitigation:** Acknowledge as a known limitation of the Flash-based approach given project constraints.

## Undecided Issues and Responsible Parties
1.  **Issue:** Exact number of questions and difficulty progression in the game sequence.
    *   **Responsible:** Development Team in consultation with Ms. Brooks (Client).
2.  **Issue:** Specific security protocol for the administrator password (storage, transmission).
    *   **Responsible:** Development Team with review from Mr. Henning (Mentor).
3.  **Issue:** Final list and categorization of projects to be included in the Math Umbrella.
    *   **Responsible:** Development Team in coordination with S2S program (Dr. Almstrum).
4.  **Issue:** Detailed scoring algorithm and how it maps to final feedback messages.
    *   **Responsible:** Development Team.
5.  **Issue:** Handling of browser compatibility issues beyond Flash 5 support.
    *   **Responsible:** Development Team.
6.  **Issue:** Long-term maintenance plan after the semester ends.
    *   **Responsible:** S2S Program Administrators.