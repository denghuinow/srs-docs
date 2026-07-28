# Balanced Summary: Get Real Website (Version 0.2)

## Goals and Scope
The Get Real website aims to attract and encourage Oregon high school students to pursue computer science (CS) degrees within the Oregon University System. It provides a teen-friendly, easily navigable portal with career information, personal profiles, and educational pathways to increase CS graduates. The scope is limited to supporting high school students, with a focus on engaging both those already interested in CS and those who might be persuaded to consider it.

## Stakeholders and User Stories
*   **High School Students (Interested in CS):** Students seeking detailed information about CS careers and university programs.
*   **High School Students (General College-Bound):** Students who may be attracted to CS through engaging content and clear value propositions.
*   **Web Designers/Developers:** Team members responsible for implementing, updating, and maintaining the website.
*   **Computer Science Task Force (ETIC Subcommittee):** Contributors defining requirements and providing strategic direction for the site.
*   **OUS Chancellor's Office/Administrators:** Entity hosting the site and providing institutional resources and oversight.
*   **CS Professionals & Graduates (Profiled):** Individuals featured to provide real-world career insights and role models.

**User Stories:**
1.  As a high school student interested in CS, I want to see profiles of recent graduates so that I can understand real career paths.
2.  As a college-bound student, I want visually engaging, chunked information so that I can quickly grasp what CS offers.
3.  As a web designer, I want clear style conventions and check-in/out procedures so that I can collaborate effectively on site updates.
4.  As a member of the CS Task Force, I want student feedback incorporated so that the site remains relevant and appealing.
5.  As the OUS administrator, I want the site to be hosted on performant servers so that it retains users with short attention spans.
6.  As a student exploring majors, I want to see how a CS minor complements other fields so that I can understand its broader value.

## Key Processes
1.  **Site Navigation & Content Discovery:** (Trigger: User visits site) Users browse organized sections (e.g., Real People, Jobs & Money) to find relevant CS information.
2.  **Consuming Profile & Career Content:** (Trigger: User selects a profile or article) Users view text, images, and potentially video/audio content from CS professionals.
3.  **Exploring Educational Pathways:** (Trigger: User accesses college or high school course sections) Users review CS program offerings across OUS campuses and recommended preparatory curricula.
4.  **Searching for Information:** (Trigger: User initiates a search query) Users perform internal site searches or access curated external CS resources.
5.  **Accessing Dynamic Content:** (Trigger: User subscribes or visits relevant section) Users view updated content via RSS feeds from selected CS news sources.
6.  **Submitting & Viewing Q&A:** (Trigger: User submits a question) Users ask questions to grads/professors and view posted answers in an FAQ format.
7.  **Site Evaluation & Update:** (Trigger: Periodic review based on analytics) Administrators review site hits and user engagement metrics to guide future content and design changes.

## Domain Data Elements
*   **CS Professional Profile:** (Primary Key: Profile_ID) Fields: Name, Career Stage (Recent Grad/Experienced), Job Title, Biography, Media (photo/video).
*   **OUS Campus Program:** (Primary Key: Campus_ID) Fields: Campus Name, CS Degree Offerings, Unique Program Highlights, Contact Information.
*   **Article/External Resource:** (Primary Key: Resource_ID) Fields: Title, Source/URL, Summary, Relevant Tags (e.g., careers, women in CS).
*   **FAQ Item:** (Primary Key: Question_ID) Fields: Question Text, Answer Text, Category, Date Posted.
*   **High School Course Recommendation:** (Primary Key: Curriculum_ID) Fields: Source (e.g., ACM, UO), Course List, Description, Target Grade Level.
*   **Professional Organization:** (Primary Key: Org_ID) Fields: Organization Name (e.g., ACM, IEEE), Description, Student Chapter URL.

## Non-Functional Requirements
1.  **Performance:** The site must have rapid server response times to accommodate users with short attention spans.
2.  **Usability:** The design must be teen-friendly, using visuals, white space, and chunked information to avoid "walls of text."
3.  **Compatibility:** The site must function correctly on major web browsers (IE, Firefox, Netscape).
4.  **Maintainability:** Development must adhere to established CSS/style conventions and use version control (Dreamweaver check-in/out).
5.  **Evaluability:** The site must support tracking hits and user engagement time for content evaluation.
6.  **Security:** Copyright and security measures must align with the standards of the main OUS website.

## Milestones and External Dependencies
1.  **Milestone:** Completion of Version 2 prototype and design updates based on student feedback.
2.  **Dependency:** Availability of OUS (OSU) server resources and bandwidth, especially for hosting video content.
3.  **Dependency:** Limited availability of Chancellor's Office web design resources for ongoing updates.
4.  **Milestone:** Implementation and population of new sections (e.g., High School Courses, FAQ).
5.  **Future Milestone:** Planning for a potential Version 3 based on lessons learned from Version 2.

## Risks and Mitigation Strategies
1.  **Risk:** Site fails to engage the target teen audience due to poor design or slow performance.
    *   **Mitigation:** Prioritize usability feedback from students, implement a visually appealing design, and ensure hosting on a performant server.
2.  **Risk:** Resource constraints limit the ability to create or maintain new content (e.g., videos, RSS feed curation).
    *   **Mitigation:** Prioritize new features, seek additional resources, or scale back the scope of resource-intensive sections.
3.  **Risk:** Information becomes outdated (e.g., college program details, professional links).
    *   **Mitigation:** Establish clear ownership and a review schedule for updating key content sections.
4.  **Risk:** Difficulty in sourcing and creating compelling "Real People" profiles, especially with video.
    *   **Mitigation:** Start with text/image profiles, leverage existing resources (e.g., UW videos), and gradually build a library.
5.  **Risk:** Low site traffic or poor search engine visibility.
    *   **Mitigation:** Leverage the `ous.edu` domain for SEO, promote through school counselors, and ensure content is shareable.

## Undecided Issues
1.  The extent to which community and private Oregon colleges should be listed in the "Exploring College" section.
2.  The specific implementation and resource commitment for video "Real People" profiles.
3.  Final prioritization and implementation details for all proposed new pages/sections.
4.  The specific tools and integration method for the internal/external site search functionality.
5.  The exact process and responsibility for curating and maintaining the RSS feed content.
6.  Mechanisms for actively obtaining and incorporating ongoing feedback from high school students after launch.