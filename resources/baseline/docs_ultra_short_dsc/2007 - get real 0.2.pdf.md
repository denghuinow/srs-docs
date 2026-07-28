# Software Requirements Specification (SRS)
## For the Get Real Website (Version 2.0)

**Document Version:** 1.0
**Date:** [Current Date]
**Project:** Get Real Website v2.0
**Client/Sponsor:** Oregon University System (OUS)
**Prepared by:** [Your Name/Team]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for Version 2.0 of the Get Real website. The primary purpose of this document is to provide a detailed description of the system's capabilities, interfaces, and performance characteristics to serve as a basis for design, development, testing, and stakeholder agreement. The intended audience includes project managers, developers, designers, testers, and OUS stakeholders.

#### 1.2 Scope
The Get Real website is an informational portal designed to attract and encourage Oregon high school students (grades 9-12) to pursue computer science (CS) degrees within the Oregon University System. The system's core functionality includes providing comparative educational program data, career information, professional profiles, and curated resources.

**In-Scope:**
*   Dynamic presentation and comparison of CS programs across OUS institutions.
*   Management and display of career information, salary data, and job roles.
*   Content management for "Real People" profiles (professionals and graduates).
*   A dedicated "Women in CS" section with profiles and resources.
*   Site-wide and external content search functionality.
*   Integration and display of external RSS feeds related to computer science.
*   A managed FAQ section with contributions from graduates and professors.
*   A "teen-friendly" user interface emphasizing visual design and rapid navigation.
*   Hosting within the OUS domain (`getreal.ous.edu`) on existing OSU infrastructure.

**Out-of-Scope:**
*   University application or admission processes.
*   User account creation or personalization (beyond session-based navigation).
*   Direct communication channels between students and universities/professionals.
*   High-bandwidth content delivery (e.g., extensive video streaming).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **CS** | Computer Science |
| **OUS** | Oregon University System |
| **OSU** | Oregon State University |
| **RSS** | Really Simple Syndication (web feed format) |
| **CMS** | Content Management System |
| **UI** | User Interface |
| **UX** | User Experience |
| **FAQ** | Frequently Asked Questions |
| **SRS** | Software Requirements Specification |

#### 1.4 References
*   Get Real Website Version 1.0 Documentation
*   OUS Web Style Guide and CSS Conventions
*   Project Charter for Get Real v2.0

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, usability, and maintainability. Section 5 covers external interface requirements, and Section 6 lists other relevant requirements and constraints.

---

### 2. Overall Description

#### 2.1 Product Perspective
This system is an evolutionary upgrade (Version 2.0) of the existing Get Real website. It is a component within the larger OUS web ecosystem, residing on OSU servers under the `ous.edu` domain. The system is a standalone informational website but must integrate visually and technically with OUS standards.

#### 2.2 Product Functions
The high-level functions of the Get Real website are:
1.  **Program Information Delivery:** Present searchable, comparable listings of CS degree programs offered by OUS universities.
2.  **Career Information Hub:** Display information about CS career paths, including roles, descriptions, and salary data.
3.  **Profile Management:** Host and present profiles of CS professionals ("Real People") and recent graduates.
4.  **Targeted Resource Section:** Maintain a dedicated area with content aimed at encouraging women to pursue CS.
5.  **Content Discovery:** Provide a unified search function for site content and approved external resources.
6.  **Dynamic Content Integration:** Aggregate and display relevant CS news/articles via RSS feeds.
7.  **Question & Answer Portal:** Host an FAQ section with authoritative answers from the CS community.

#### 2.3 User Characteristics
| User Class | Characteristics | Expected Expertise |
| :--- | :--- | :--- |
| **Primary: High School Student (Interested)** | Oregon student in grades 9-12 with existing interest in CS. Seeks detailed program comparisons, career outlooks, and authentic stories. | Basic web browsing skills. Short attention span. Motivated to find specific information. |
| **Primary: High School Student (Undecided)** | College-bound Oregon student with no initial CS interest. Needs persuasive, engaging content to spark curiosity. | Basic web browsing skills. Very short attention span. Needs clear, compelling value propositions. |
| **Secondary: Student (Other Major)** | Student considering a CS minor. Needs concise information on minor requirements and benefits. | Basic web browsing skills. Goal-oriented. |
| **Content Administrator (OUS Staff)** | OUS or university staff responsible for updating program data, profiles, FAQs, and resources. | Proficient with web-based CMS. Subject matter knowledge. |

#### 2.4 Constraints
*   **Technical:** Limited server bandwidth precludes reliance on high-volume video streaming.
*   **Resource:** Development and maintenance resources from the Chancellor’s Office are limited.
*   **Infrastructure:** The site is dependent on OUS servers, domain hosting, and network policies.
*   **Compatibility:** Must support legacy browsers (Netscape) alongside modern ones (IE, Firefox).

#### 2.5 Assumptions and Dependencies
*   **Assumption:** OUS will provide accurate and timely data feeds for university program information.
*   **Assumption:** CS professionals and graduates will be available to contribute profile and FAQ content.
*   **Dependency:** The site's visibility is dependent on the `ous.edu` domain for search engine ranking.
*   **Dependency:** The design must inherit and comply with the existing OUS and Get Real v1.0 CSS/style standards.

---

### 3. Specific Requirements

#### 3.1 Functional Requirements
**FR1: Program Comparison Module**
*   **FR1.1:** The system shall display a list of all OUS universities offering CS degrees.
*   **FR1.2:** The system shall allow users to select and side-by-side compare up to three (3) CS programs based on criteria (e.g., degree type, location, estimated cost, core courses).
*   **FR1.3:** The system shall present program information in a concise, scannable format using icons, short lists, and key highlights.

**FR2: Career Information Module**
*   **FR2.1:** The system shall present a catalog of common CS job roles (e.g., Software Developer, Data Scientist, Security Analyst).
*   **FR2.2:** For each job role, the system shall display a description, typical career path, and relevant salary range data.
*   **FR2.3:** Career content shall be highly visual and link to related "Real People" profiles.

**FR3: Real People Profiles**
*   **FR3.1:** The system shall host a searchable gallery of profiles featuring CS professionals and recent OUS graduates.
*   **FR3.2:** Each profile shall include a photo, brief biography, educational path, current role, and "a day in the life" snapshot.
*   **FR3.3:** The system shall include a filter to view profiles by attributes (e.g., university attended, job role, gender for the Women in CS section).

**FR4: Women in Computer Science Section**
*   **FR4.1:** The system shall maintain a dedicated, prominently linked section for women in CS.
*   **FR4.2:** This section shall aggregate profiles of female professionals/graduates, resources (scholarships, organizations), and articles addressing gender-specific perspectives in CS.

**FR5: Search Functionality**
*   **FR5.1:** The system shall provide a single search input field on all major pages.
*   **FR5.2:** The search shall return relevant results from internal site pages (programs, careers, profiles, FAQs).
*   **FR5.3:** The search shall also return curated, vetted links to relevant external educational resources (e.g., Code.org, ACM).

**FR6: RSS Feed Integration**
*   **FR6.1:** The system shall consume and parse at least one (1) configured RSS feed from a reputable CS news source.
*   **FR6.2:** The system shall display the feed's most recent headlines (with publication date) and links in a designated sidebar or section.

**FR7: FAQ Management**
*   **FR7.1:** The system shall display a categorized list of frequently asked questions about studying and working in CS.
*   **FR7.2:** Each FAQ answer shall be attributed to a CS graduate or professor (by name and affiliation).
*   **FR7.3:** The FAQ shall have a simple, text-based search within its own content.

#### 3.2 External Interface Requirements
**3.2.1 User Interfaces**
*   The UI shall follow OUS brand guidelines and the visual style (layouts, color palettes, typography) established in Get Real v1.0.
*   All pages shall use responsive CSS techniques to ensure readability across screen sizes.
*   Navigation shall be consistent, simple, and require minimal clicks to reach key content.

**3.2.2 Hardware Interfaces**
*   The system shall operate on standard OUS-provided web servers (OSU infrastructure). No direct hardware interfaces are required.

**3.2.3 Software Interfaces**
*   **Browser Compatibility:** The website shall be fully functional and visually consistent on Internet Explorer 7+, Firefox 3+, and Netscape 8+.
*   **OUS Domain:** The site shall be hosted at `getreal.ous.edu` and link seamlessly to/from the main OUS website.
*   **RSS Feeds:** The system shall interface with external RSS 2.0 or Atom feeds over HTTP.

**3.2.4 Communications Interfaces**
*   Standard HTTP/HTTPS protocols shall be used for all client-server communication.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   **Page Load Time:** Average server response time for any page request shall be less than or equal to the response time of the main OUS homepage under similar load conditions.
*   **Concurrent Users:** The system shall support up to 150 concurrent user sessions without significant degradation in performance.

**3.3.2 Usability Requirements**
*   **Audience Appropriateness:** The design shall be "teen-friendly," avoiding dense "walls of text." Content shall use visuals, icons, bullet points, and short paragraphs.
*   **Learnability:** A new high school user shall be able to locate program comparison tools or career information within 3 clicks from the homepage.
*   **Navigation:** The information architecture shall be adaptable based on periodic analysis of site analytics (hits, time-on-page, click paths).

**3.3.3 Maintainability Requirements**
*   **Code Standards:** All HTML/CSS/JavaScript shall adhere to the conventions and structures defined in the Get Real v1.0 codebase and OUS web standards.
*   **Content Updates:** The backend shall utilize a CMS that allows authorized OUS staff to update all textual and image content (profiles, FAQs, career data) without developer intervention.
*   **Modularity:** The site layout shall be templated to allow global style changes (e.g., color scheme, header/footer) from a single CSS file.

**3.3.4 Security Requirements**
*   The public-facing site shall require no authentication for read access.
*   The administrative CMS interface shall be secured via OUS-standard authentication mechanisms.

---

### 4. Acceptance Criteria & Success Metrics

#### 4.1 Acceptance Approach
Formal acceptance of the system by the OUS Chancellor’s Office requires:
1.  Successful deployment and stable operation on the designated OUS/OSU production server.
2.  A visual design review confirming consistency with OUS and Get Real v1.0 style conventions.
3.  Verification that all functional requirements (Section 3.1) operate as specified.

#### 4.2 Success Evaluation
The long-term success of the project will be evaluated based on operational metrics, including:
*   **Increased Engagement:** Month-over-month growth in total site hits and unique visitors from Oregon IP ranges.
*   **User Retention:** Increase in average time spent on site per session, indicating engaging content.
*   **Navigation Effectiveness:** Analysis of heatmaps and click-tracking data to optimize page layouts and information flow.

---

### 5. Appendix

#### 5.1 Open Issues
*   Specific source(s) for salary data feed to be determined.
*   Final list of initial "Real People" profiles to be provided by OUS.

#### 5.2 Notes
This SRS is based on the provided project summary. Detailed wireframes, a sitemap, and a visual style guide should be created as subsequent deliverables to refine UI/UX requirements.