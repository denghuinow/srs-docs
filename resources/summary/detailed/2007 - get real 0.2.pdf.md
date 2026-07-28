# Detailed Summary: Get Real Website (Version 2)

## Background and Scope
This document specifies requirements for Version 2 of the Get Real website, an update to the existing site created in 2006. The primary goal is to attract and encourage Oregon high school students to pursue computer science (CS) degrees within the Oregon University System (OUS). The scope includes redesigning the site to be more teen-friendly with improved navigation, visual appeal, and updated content, while maintaining its core informational purpose. Non-goals include developing a comprehensive knowledge base or extensive user documentation, which are deferred to a potential future Version 3.

## Stakeholders Matrix and Use Cases
*   **Web Designers:** Primary readers and implementers responsible for contributing to and testing the Get Real website.
*   **Computer Science Task Force (ETIC subcommittee):** Contributors to this SRS document, providing requirements and oversight.
*   **Oregon High School Students (Interested in CS):** Target users seeking concise, in-depth information about CS careers and university programs.
*   **Oregon High School Students (College-bound, not CS-focused):** Target users who might be attracted to a CS career through engaging site content and presentation.
*   **Students Considering a CS Minor:** A potential user group interested in diverse fields (e.g., medicine, law) where a CS minor adds value.
*   **OUS Campuses:** Provide CS program information and may supply content (e.g., FAQ answers, recommended curricula).
*   **High School Counselors:** Indirect users; the site serves as a resource they may recommend to students.

**Main Scenarios:**
1.  A student interested in CS navigates to explore university offerings and career information.
2.  A college-bound student with no CS focus visits the site and is engaged by visual content, leading to exploration of CS paths.
3.  A user searches internally for specific information or externally for broader CS resources.
4.  A user views "Real People" profiles (including video) to understand diverse CS career applications.
5.  A user accesses RSS feeds for current CS news and articles.
6.  A user submits or views questions and answers in the "Ask a Grad or Prof" FAQ section.

**Exception Scenarios:**
1.  A user encounters slow page load times, potentially leading to site abandonment.
2.  A user searches for information not covered by the site's content or external search scope.

## Business Process
**Main Process: Student Information Discovery & Engagement**
1.  **Trigger:** Student navigates to `getreal.ous.edu`.
2.  **Input:** Student intent (general browsing or specific query).
3.  **Step 1:** Student lands on redesigned homepage with improved visuals, white space, and clear navigation.
4.  **Step 2:** Student browses core sections (e.g., Exploring College, Jobs & Money, Real People) with content presented in shorter chunks, bullets, and charts.
5.  **Step 3:** Student may use the internal/external search function to find specific information.
6.  **Step 4:** Student may engage with interactive elements (e.g., video profiles, RSS feeds, FAQ).
7.  **Step 5:** Student is presented with a "call to action" (e.g., plan for CS preparation, contact resources).
8.  **Output:** Informed student with increased interest in pursuing CS or a CS minor.

**Key Branch A: Content Contribution (FAQ)**
1.  **Trigger:** User submits a question via the "Ask a Grad or Prof" interface.
2.  **Step 1:** Question is routed to designated OUS grad or professor.
3.  **Step 2:** Answer is provided and reviewed.
4.  **Step 3:** Q&A pair is posted to the public FAQ section.
5.  **Output:** Updated FAQ knowledge base.

**Key Branch B: Content Maintenance (RSS)**
1.  **Trigger:** Scheduled update cycle (e.g., weekly).
2.  **Step 1:** Web designer edits URLs to the Chancellor's Office DSS feed.
3.  **Step 2:** RSS feed content is updated on the Get Real site.
4.  **Output:** Fresh CS news available to subscribers.

## Domain Model
*   **Web Page:** (Title, Content, Navigation Path, Last Updated Date)
*   **University Program:** (OUS Campus Name [required], CS Degree Offerings, Contact Information)
*   **Real Person Profile:** (Name [required], Career Stage [Recent Grad/Experienced], Biography, Photo/Video Asset, Career Field)
*   **Career Resource:** (Title [required], Type [Article/Program Link], Description, External URL)
*   **FAQ Item:** (Question [required], Answer [required], Date Posted, Status [Published/Pending])
*   **RSS Feed Item:** (Title [required], Source, Summary, Link [required], Publication Date)
*   **Search Query:** (Query Terms, Scope [Internal/External], Results List)
*   **High School Course Recommendation:** (Subject Area, Recommended Course Name, Source [e.g., ACM, UO])

## Interfaces and Integrations
*   **Web Browsers (User Interface):** Direction: Bidirectional. Interaction: Site rendering and user interaction. Input: User clicks, form entries, searches. Output: HTML/CSS/JS pages, dynamic content. SLA: Must support and be tested on IE, Firefox, Netscape.
*   **OUS Web Server (Hosting):** Direction: Inbound/Outbound. Interaction: Site hosting and delivery. Input: HTTP requests. Output: Web pages, assets. SLA: Must provide response times comparable to `www.ous.edu` to accommodate short teen attention spans.
*   **Search Engine (External - e.g., Google):** Direction: Outbound. Interaction: External site search. Input: Query terms. Output: Search results from indexed external CS sites. SLA: Dependent on external provider.
*   **RSS Feed Aggregator:** Direction: Inbound. Interaction: Pull content from Chancellor's Office feed. Input: RSS/XML feed URL. Output: Parsed article headlines and links for display. SLA: Requires manual editing hours per week from web design resource.

## Acceptance Criteria
*   **Capability: Engaging Teen-Friendly Design**
    *   Given a student lands on the homepage, When they view the layout, Then text is presented in short paragraphs with ample white space, bullets, and visual elements (photos, charts).
    *   Given a student not initially interested in CS, When they browse the "Real People" section, Then they see video profiles and career stories that are visually compelling and easy to digest.
*   **Capability: Comprehensive Information Access**
    *   Given a student wants to compare CS programs, When they use the "Exploring College" section, Then they find a clear listing of offerings from all seven OUS campuses.
    *   Given a user has a specific question, When they use the site search function, Then relevant results from both internal pages and approved external sources are returned.
*   **Capability: Dynamic Content**
    *   Given the site is live, When new content is added to the designated RSS feed source, Then the "RSS feeds" section updates to reflect the new items (following manual curation).
    *   Given a user submits a valid question via the FAQ interface, When an answer is approved, Then the Q&A pair becomes visible in the public FAQ listing.

## Non-functional Metrics
*   **Performance:** Page load times must be fast, benchmarked against the main OUS site (`www.ous.edu`). The site must handle typical high school user traffic without degradation.
*   **Reliability/Availability:** The site should have uptime consistent with the OUS web hosting standards.
*   **Security:** Adhere to OUS website copyright and security policies.
*   **Compliance:** Web design conventions (CSS, styles) must be consistent with established Get Real Version 1 and OUS site standards.
*   **Observability:** The site must support tracking and evaluation of hits and time spent by users to inform future content and design changes.

## Milestones and Release Strategy
1.  Finalize prioritization and prototyping of new page/section ideas.
2.  Complete graphic design and layout overhaul for all existing pages.
3.  Develop and integrate new functional pages (Search, FAQ, RSS, High School Courses, etc.).
4.  Conduct cross-browser testing (IE, Firefox, Netscape).
5.  Perform user acceptance testing with target student groups.
6.  Deploy Version 2 to the live `getreal.ous.edu` site.

## Risk List and Mitigation Strategies
1.  **Risk:** Limited availability of Chancellor's Office web design resources. **Mitigation:** Prioritize features clearly; consider phased implementation of lower-priority new sections.
2.  **Risk:** Site fails to engage the non-CS-interested student demographic. **Mitigation:** Incorporate direct student feedback early in the redesign process via prototypes.
3.  **Risk:** Bandwidth constraints for hosting video profiles. **Mitigation:** Optimize video formats and sizes; consider hosted streaming solutions.
4.  **Risk:** Content becomes stale (e.g., FAQ unanswered, RSS not updated). **Mitigation:** Define clear ownership and a maintenance schedule for dynamic content sections pre-launch.
5.  **Risk:** Inconsistent information from OUS campuses (e.g., HS course recommendations). **Mitigation:** Designate a campus liaison to collate and verify information for the site.
6.  **Risk:** Search functionality provides poor or irrelevant results. **Mitigation:** Implement and test search with a defined scope and curated external sources.
7.  **Risk:** Site navigation remains confusing despite redesign. **Mitigation:** Conduct usability tests on navigation structure before final development.
8.  **Risk:** Version 2 changes break compatibility with existing bookmarks or links. **Mitigation:** Implement appropriate URL redirects from old page paths to new ones.

## Undecided Issues and Responsible Parties
1.  **Issue:** Final extent of listing community and private colleges in Oregon within the "Exploring College" section. **Responsible:** Computer Science Task Force / OUS Liaison.
2.  **Issue:** Specific source and maintenance process for "High School Courses" recommendations. **Responsible:** UO (leading) & Computer Science Task Force.
3.  **Issue:** Selection criteria and sourcing for "Professional Organizations" links. **Responsible:** Computer Science Task Force.
4.  **Issue:** Moderation process and responsible parties for the "Ask a Grad or Prof" FAQ. **Responsible:** Computer Science Task Force & OUS Campuses.
5.  **Issue:** Specific weekly hours allocation for RSS feed maintenance. **Responsible:** Chancellor's Office Resource Manager.
6.  **Issue:** Final prioritization of the list of proposed new pages/sections. **Responsible:** Computer Science Task Force.
7.  **Issue:** Need for additional input from high school counselors on related sites and resources. **Responsible:** Computer Science Task Force.
8.  **Issue:** Decision on implementing a BLOG vs. a static FAQ for "Ask a Grad or Prof." **Responsible:** Computer Science Task Force & Web Designers.