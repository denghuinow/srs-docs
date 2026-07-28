# Balanced Summary: Space Fractions

## Goals and Scope
Space Fractions is a web-based, interactive educational game designed to improve fraction-solving skills for sixth-grade students. The project includes a game with a storyline and a separate "Math Umbrella" web menu linking to other math-related S2S projects. The game provides feedback based on player scores and allows an administrator to update questions.

## Stakeholders and User Stories
*   **Ms. Andrea Brooks (Client/Teacher):** The client from Pecan Springs Elementary School who requested the software.
*   **Sixth-Grade Students (Primary Users):** The target users who will play the game to learn fractions.
*   **Game Administrator (e.g., Teacher Claire):** Responsible for updating the game's question content via a web interface.
*   **Development Team (The Denominators):** The team responsible for designing, building, and maintaining the software.
*   **Dr. Vicki L. Almstrum & Mentor (Project Oversight):** Provide academic and technical guidance for the project.

**User Stories:**
1.  As a sixth-grade student, I want an engaging storyline so that learning fractions is fun and not boring.
2.  As a competitive student, I want to see my score and ranking so that I can try to improve and excel.
3.  As a teacher, I want to be able to update the game's questions so that I can customize the content for my class.
4.  As a student, I want clear instructions and help so that I can understand how to play the game without frustration.
5.  As a user, I want to access the game from a standard web browser so that I don't need to install special software.
6.  As a teacher, I want students to receive feedback on their performance so that they can identify areas for improvement.

## Key Processes
1.  **Trigger:** User navigates to the game URL. The introductory movie plays to set up the storyline, but can be skipped.
2.  **Trigger:** Movie ends or is skipped. The user arrives at the Main Menu, where they can start the game, get help, or view team info.
3.  **Trigger:** User clicks "Start Game". The Game Sequence presents a series of multiple-choice fraction questions within a storyline.
4.  **Trigger:** User answers a question. The system provides immediate feedback (correct/incorrect) and may branch the story at critical points.
5.  **Trigger:** All questions are completed. The Ending Scene displays the user's final score, a story conclusion based on performance, and options to quit or replay.
6.  **Trigger:** Administrator logs into the Question Updater. A web form interface allows them to modify question data, which is saved to a server file.
7.  **Trigger:** User accesses the Math Umbrella. A separate web page provides organized links to other S2S math projects.

## Domain Data Elements
*   **Question:** (Question ID) - Question Text, Correct Answer, Incorrect Answer Options, Question Type (e.g., arithmetic, equivalence), Critical Point Flag.
*   **User Session:** (Session ID) - Current Score, Current Question Index, Story Branch Path.
*   **Game Configuration:** (Config ID) - Total Number of Questions, Score Calculation Rules, Storyline Definitions.
*   **Administrator:** (Admin ID) - Username, Password Hash.
*   **Math Umbrella Link:** (Link ID) - Project Title, URL, Topic Category (e.g., Fractions, Decimals).

## Non-Functional Requirements
1.  The game must run in a standard web browser with the Macromedia Flash 5 plug-in.
2.  All user input must be achievable via mouse clicks only; no keyboard input is required.
3.  The main game movie file size should be optimized, targeting 1-2MB for reasonable download times.
4.  The code must be maintainable, using modular structures like sub-scenes for easy future updates.
5.  The product must be reliable, ensured through extensive testing by the development team.
6.  The question update functionality must be secure, requiring administrator authentication.

## Milestones and External Dependencies
1.  Completion of the core Flash-based game sequence and user interface.
2.  Development and integration of the web-based Question Updater administrative tool.
3.  Creation of the standalone Math Umbrella web page linking to other projects.
4.  Dependency on the S2S website infrastructure for hosting the final product.
5.  Dependency on user machines having a compatible web browser with Flash support.

## Risks and Mitigation Strategies
1.  **Risk:** The Flash-based game may not perform consistently across different browsers or future Flash versions.
    *   **Mitigation:** Adhere strictly to Flash 5 specifications and conduct cross-browser testing.
2.  **Risk:** Students may find the game too difficult or not engaging, reducing its educational value.
    *   **Mitigation:** Involve the client (teacher) and sample users in early testing to gather feedback on difficulty and engagement.
3.  **Risk:** The question updater could be misused if credentials are compromised or the interface allows invalid data.
    *   **Mitigation:** Implement input validation on the web form and ensure secure password handling.
4.  **Risk:** Project scope may expand uncontrollably when integrating with the broader "Math Umbrella."
    *   **Mitigation:** Clearly define the deliverable as a standalone game with a simple menu link to the umbrella, not building the umbrella itself.
5.  **Risk:** File size of game assets (movies, graphics) could lead to long load times for users with slow internet.
    *   **Mitigation:** Optimize media assets and leverage Flash's streaming playback capability.

## Undecided Issues
1.  The exact number of questions and the specific "critical points" that affect the storyline.
2.  The detailed algorithm for calculating the final score and ranking.
3.  The specific security protocol for the administrator login (beyond a basic password).
4.  The full list and categorization of projects to be included in the Math Umbrella.
5.  The detailed format of the data file generated by the Question Updater for the game to read.
6.  The specific hosting details and URL structure on the final S2S server.