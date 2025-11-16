# Balanced Summary

## Goals and Scope
Space Fractions is a web-based, interactive game designed to improve fraction-solving skills for sixth-grade students. The product includes an introductory movie, a main menu, a series of fraction questions forming a storyline, and an ending scene with score feedback. An umbrella component provides links to related mathematics games organized by topic.

## Roles and User Stories
- **Student**: As a student, I want to answer fraction questions through an engaging storyline so that I can learn fractions in a fun way
- **Teacher**: As a teacher, I want to update game questions through a web interface so that I can customize the learning content
- **Administrator**: As an administrator, I want to access the question updater with password protection so that I can maintain game content securely

## Key Processes
1. **Trigger: Program start** → Introductory movie plays to set up storyline
2. **Trigger: Movie completion/skip** → Main menu displays with game options and help
3. **Trigger: Game start selection** → Series of fraction questions presented with multiple-choice answers
4. **Trigger: Answer submission** → System validates responses and provides immediate feedback
5. **Trigger: Critical question responses** → Storyline branches based on answer correctness
6. **Trigger: Question completion** → Ending scene displays score and plot conclusion
7. **Trigger: Admin access** → Question updater allows content modification through web forms

## Domain Data Elements
- **Question**: QuestionID, QuestionText, AnswerOptions, CorrectAnswer, DifficultyLevel
- **User Session**: SessionID, CurrentScore, CurrentQuestion, ProgressStatus, StartTime
- **Game Configuration**: ConfigID, CriticalQuestions, StorylineBranches, MaxQuestions
- **Administrator**: AdminID, Username, Password, AccessLevel, LastLogin

## Non-functional Requirements
- Compatible with web browsers supporting Flash 5 and JavaScript
- Download times under one minute for introductory components via modem
- Maintainable through modular Flash sub-scenes and separable code
- Accessible over Internet via S2S website
- Secure through web browser security mechanisms
- Reliable through extensive testing by team members

## Milestones and External Dependencies
- Completion of Flash movie development
- Integration with S2S website infrastructure
- Testing with sixth-grade student volunteers
- Dependency on Macromedia Flash compatibility
- Availability of web server hosting

## Risks and Mitigation Strategies
- **Browser compatibility issues**: Test across multiple browser configurations
- **Student engagement challenges**: Incorporate competitive elements and adaptive storytelling
- **Content maintenance complexity**: Provide intuitive administrative interface
- **Performance with modem connections**: Optimize file sizes and streaming capabilities
- **Security of administrative access**: Implement password protection for question updates

## Undecided Issues
- Specific fraction concepts to be covered in detail
- Exact number of questions in the game sequence
- Scoring algorithm and ranking methodology
- Detailed storyline plot points and characters
- Help section content and depth
- Integration approach with other S2S mathematics projects