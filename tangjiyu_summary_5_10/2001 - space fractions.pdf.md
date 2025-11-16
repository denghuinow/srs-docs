# Space Fractions - Software Requirements Specification

## 1. Introduction
### 1.1 Purpose of this Document
This is the Software Requirements Specification (SRS) for the "Space Fractions" project. The purpose of the document is to describe the purpose and functionality of the software product requested by Ms. Andrea Brooks of Pecan Springs Elementary School. The SRS will include the details of the project's requirements, interface, design issues, and components.

### 1.2 Scope of the Development Project
The Space Fractions project is a learning tool created to help improve fraction-solving skills for sixth-grade students. The product will be a web-based, interactive game. At the end of the game, students will be given feedback based on their game scores. We are also providing an umbrella for the past games created. The umbrella will be a web-based menu system allowing the user to choose between the games.

### 1.3 Definitions, Acronyms, and Abbreviations
- HTML: Hypertext Markup Language - the formatting language used to describe web pages
- Macromedia Flash: An application for creating dynamic graphics and sound for display over the World Wide Web
- SRS: Software Requirements Specification
- Umbrella: A software product that consists of several independent programs unified under a single interface
- Web-based: Able to be run over the web, without any permanent files on the user's computer

## 2. General Description
### 2.1 User Personas and Characteristics
The target clients are sixth-grade students and their teacher:
- Alice: A sixth-grade female student learning fractions who does not like to use computers
- Bobby: A sixth-grade male student learning fractions who is very competitive
- Claire: A sixth-grade teacher with computer skills

### 2.2 Product Perspective
- Requires a web browser capable of running Flash movies
- Not dependent on any other software and is not a component of another program
- Does not require any new hardware

### 2.3 Overview of Functional Requirements
The umbrella will be a singular component, providing links to projects relating to fractions, decimals, and percents in a format accessible over the World Wide Web.

The "Space Fractions" game will have the following functional components:
1. An introductory movie to set up the storyline
2. A main menu, including a brief help section
3. A series of fraction questions (testing arithmetic, equivalence, graphical interpretation, and improper versus proper fraction skills) that sequentially form a storyline related to the introduction
4. An ending scene where the user's score is calculated and ranked, with an option to quit the game or try again

In addition, a component accessible over the World Wide Web will allow the series of fraction questions to be updated by an administrator of the game.

### 2.4 Overview of Data Requirements
The administrator may design a custom game with custom fraction questions. This information must be saved in a file on the web server where the game is hosted and will be easily edited through simplified administrative screens. The user's score must be kept as local data within the game so that the results may be given at the end of the game. Input will consist entirely of mouse clicks for the user to choose answer options and to set preferences. Output will be sounds and animations through Flash movies to acknowledge success or failure in answering the fraction questions.

### 2.5 General Constraints, Assumptions, Dependencies, and Guidelines
This program will run on any Internet-accessible computer with a web browser that supports JavaScript and Macromedia Flash 5.

### 2.6 User View of Product Use
Upon starting the program, the user is taken through a brief introductory movie to provide background story and information that will help them complete the fraction questions. There is an option to skip the introduction.

At the main title screen, the user will be able to view a general help screen to reveal basic instructions on game play. Also, a short summary of our team and a link to our website will be provided.

Next, the user progresses through a series of questions in the form of cartoon images that comprise the main story. These questions will test the user's knowledge of basic fraction operations and will be presented as a multiple-choice questionnaire.

After the last question, the main character's adventure will come to an end. The last scene will be determined by the user's response on certain critical questions that impact the story's plot, and an option to try again will be presented. In addition, the player's exact score will be given with a customized message.

As the game administrator, Claire can use the question updater to change any of the questions in the game. She navigates to the updater page, which asks for a password. Upon correct submission of her password, she uses an intuitive web forms interface to update the game to her desiring.

## 3. Specific Requirements
### 3.1 External Interface Requirements
The interface for this program will be relatively simple. As the target users are in the sixth grade, this product will be as graphically oriented and appealing as possible. No portion of the interface will require the keyboard; all input will be accomplished via mouse clicks.

This product requires a web browser capable of running the Flash plug-in. Otherwise, this product has no software interaction.

### 3.2 Detailed Description of Functional Requirements
#### 3.2.2 Introductory Movie
Purpose: A short movie to set up the storyline of the game and provide information to help the user complete the fraction questions.
Processing: Upon entrance to the movie component, the introductory movie will begin playing. If a mouse click is received, this component will terminate the movie and forward the user to the main menu component. Otherwise, the movie will continue to its completion and the user will be moved to the main menu.

#### 3.2.3 Main Menu
Purpose: A menu that displays a brief section offering help on playing the game, and provides a link to the main game component and the Denominators' web page.
Processing: This component will wait until the user selects a button. At that time, the user will be forwarded to the game sequence component or the Denominators' web page, depending on the button selected.

#### 3.2.4 Game Sequence
Purpose: A series of multiple-choice fraction questions, which sequentially form a storyline related to the introduction.
Processing: This component will display a question, and then wait until the user chooses an answer.
- If the user selects the correct answer, a message to this effect will be displayed and the component will move to the next question.
- If the incorrect answer is selected, this component will inform the user of this and give them another chance to answer the question. However, their score will not count this question as being answered correctly.
- At certain "critical points," this component will choose different directions in the plot based on whether the question at the critical point was answered correctly.
- After the user has proceeded through a set number of questions, they will be directed to the ending scene component.

#### 3.2.5 Ending Scene
Purpose: A screen offering a conclusion to the game's plot based on performance at certain critical points in the game sequence, where the user's score is displayed and the user is given a chance to exit or return to the main menu.
Processing: This component will wait until the user selects either to return to the main menu or to exit the game. After receiving the user's input, the component will act accordingly.

#### 3.2.6 Question Updater
Purpose: A web-accessible tool to allow questions in the game sequence to be updated by a game administrator.
Processing: The component will wait for the user to click a submission button for each question. After the button is clicked, the component will check that the inputted data is complete and makes sense in the context of the updated question.

#### 3.2.7 Math Umbrella
Purpose: This component will provide links to mature S2S projects dealing with mathematics for sixth graders, organized by topic.

### 3.3 Performance Requirements
Only one person can use a single instance of the product. However, the product will reside on the Internet so more than one user can access the product and download its content for use on their computer. The product will consist of Flash movies linked together to form a web-based game: there will be a small introductory movie (~200KB), a main menu movie (~100KB), and a main game movie (1-2MB). Due to the relatively small size of the introductory and main menu movies, they can be downloaded in approximately one minute with a modem connection. Because Flash movies do not have to be fully downloaded to play, the main game can be played within a few minutes with a regular modem connection to the Internet.

### 3.4 Quality Attributes
- The product will be as secure as the web browser that will run the product
- The product will be available over the Internet via the S2S website
- Reliability will be ensured by extensive testing by the team members and mentors
- Maintainability is a primary goal for this project

### 3.5 Other Requirements
There are no additional requirements at this time.
