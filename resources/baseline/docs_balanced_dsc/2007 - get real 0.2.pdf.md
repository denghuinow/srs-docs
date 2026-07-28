# Software Requirements Specification (SRS)
## Get Real Website (Version 2.0)

**Document Version:** 1.0
**Date:** [Current Date]
**Project:** Get Real - Oregon University System Computer Science Portal
**Client:** OUS Chancellor's Office / Computer Science Task Force (ETIC Subcommittee)
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for Version 2.0 of the "Get Real" website. The primary purpose is to provide a comprehensive, teen-friendly portal designed to attract and encourage Oregon high school students to pursue computer science degrees within the Oregon University System (OUS). This document serves as a guide for the development team, stakeholders, and project managers throughout the design, implementation, and maintenance phases.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Priority:** Requirements are categorized as (H)igh, (M)edium, or (L)ow priority based on stakeholder input and project goals.
*   **Keywords:** `MUST`, `SHALL`, `SHOULD`, `MAY` are used as defined in IETF RFC 2119.

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Sponsors & Task Force:** Focus on Sections 1 (Introduction), 2 (Overall Description), and 5 (Non-Functional Requirements) for strategic alignment.
*   **Web Designers & Developers:** Focus on Sections 3 (System Features), 4 (Data Requirements), and 6 (Other Requirements) for implementation details.
*   **OUS Administrators & Content Managers:** Focus on Sections 2.3 (User Characteristics), 3 (System Features), and 7 (Appendix) for operational and maintenance understanding.

#### 1.4 Project Scope
The "Get Real" website is a static/dynamic hybrid informational portal. Its core scope is to provide engaging, accurate, and accessible information about computer science careers and educational pathways to Oregon high school students.

**In-Scope:**
*   Development and hosting of a public-facing website on the `ous.edu` domain.
*   Presentation of curated content including CS professional profiles, OUS program details, career information, and preparatory course guidance.
*   Implementation of basic interactive features: FAQ submission/viewing, internal search, and display of dynamic RSS feeds.
*   Adherence to OUS branding, security, and accessibility standards.
*   Integration of analytics for user engagement tracking.

**Out-of-Scope:**
*   User account creation, login, or personalized dashboards.
*   Complex transactional processes (e.g., application submission, event registration).
*   Real-time chat or forums.
*   Development of mobile applications (responsive web design is in-scope).

### 2. Overall Description

#### 2.1 Product Perspective
The "Get Real" website is a new, independent web product within the OUS digital ecosystem. It will link to and from relevant OUS institutional pages but will maintain a distinct visual identity tailored to a high school audience. It may consume external data via RSS feeds but will not serve as a primary system of record for OUS academic programs.

#### 2.2 Product Functions (Summary)
1.  Present chunked, visually engaging informational content about CS careers and education.
2.  Showcase profiles of CS professionals and recent graduates.
3.  Detail CS degree programs and highlights across OUS campuses.
4.  Provide recommended high school course pathways.
5.  Allow users to submit questions and browse an FAQ.
6.  Enable users to search internal content and access curated external resources.
7.  Display dynamically updated CS news via RSS feeds.
8.  Provide site administrators with basic engagement analytics.

#### 2.3 User Characteristics
| User Class | Key Characteristics | Technical Proficiency | Primary Goals |
| :--- | :--- | :--- | :--- |
| **HS Student (CS-Interested)** | Actively researching CS, seeks depth, motivated. | Medium-High (comfortable web browsing). | Find detailed career paths and specific university program data. |
| **HS Student (College-Bound)** | Exploring options, needs persuasion, short attention span. | Medium. | Quickly understand the value and appeal of a CS major. |
| **Web Developer** | Implements and maintains site code. | Very High. | Efficiently update site with clear conventions and version control. |
| **CS Task Force Member** | Provides strategic direction and content guidance. | Variable. | Ensure site meets strategic goals and incorporates user feedback. |
| **OUS Administrator** | Hosts site and provides institutional oversight. | Medium-High (system administration). | Ensure site performance, security, and institutional compliance. |
| **Profiled CS Professional** | Subject of profile content. | Variable. | Accurately represent their career path and experience. |

#### 2.4 Operating Environment
*   **Server:** Hosted on OUS (OSU) servers with sufficient bandwidth for web traffic and potential video content.
*   **Client:** Must be accessible via major web browsers in use at the time of deployment (specifically called out: Internet Explorer, Firefox, Netscape).
*   **Development:** Adobe Dreamweaver with check-in/check-out version control procedures. Style conventions defined via CSS.

#### 2.5 Design and Implementation Constraints
1.  **Technical:** Must comply with OUS central web security and copyright policies.
2.  **Resource:** Development and maintenance are dependent on limited Chancellor's Office web design resources.
3.  **Content:** Video content is subject to server bandwidth constraints and production resource availability.
4.  **Procedural:** All updates must follow the established Dreamweaver check-in/out process to prevent conflicts.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** High school students will engage more with visual, chunked content than with long-form text.
*   **Assumption:** The `ous.edu` domain will provide inherent search engine visibility.
*   **Dependency:** Ongoing availability of OUS server resources and administrative support.
*   **Dependency:** The CS Task Force will provide and vet core content (profiles, program details).

### 3. System Features

#### 3.1 Feature: Content Presentation & Navigation
*   **Priority:** H
*   **Description:** The system shall present all content through a teen-friendly, easily navigable interface that avoids "walls of text."
*   **Requirements:**
    *   `FR-101`: The homepage shall provide clear, visual navigation to major site sections (e.g., Real People, Jobs & Money, Exploring College).
    *   `FR-102`: All informational pages shall present content in "chunked" segments with ample white space, images, and headings.
    *   `FR-103`: The site shall implement a consistent global navigation menu on all pages.

#### 3.2 Feature: CS Professional Profiles ("Real People")
*   **Priority:** H
*   **Description:** The system shall display profiles of CS professionals and recent graduates to provide realistic career role models.
*   **Requirements:**
    *   `FR-201`: The system shall display a gallery or list of profile entries, showing at minimum: Name, Job Title, and a Thumbnail image.
    *   `FR-202`: Selecting a profile shall display a dedicated page with the full profile data: Name, Career Stage, Job Title, Biography, and a primary Photo/Video.
    *   `FR-203`: Profiles shall be filterable or categorizable by "Career Stage" (e.g., Recent Grad, Experienced Professional).

#### 3.3 Feature: Educational Pathways
*   **Priority:** H
*   **Description:** The system shall provide information about OUS CS programs and recommended high school preparation.
*   **Requirements:**
    *   `FR-301`: A section "Exploring College" shall list all OUS campuses offering CS degrees, with the ability to view per-campus details: Campus Name, Degree Offerings, Unique Highlights, Contact Info.
    *   `FR-302`: A section "High School Courses" shall display recommended preparatory curricula, including source, course list, description, and target grade level.
    *   `FR-303`: Content shall include information on how a CS minor complements other fields of study.

#### 3.4 Feature: FAQ & Question Submission
*   **Priority:** M
*   **Description:** Users can view answered questions and submit new questions to be answered by grads/professors.
*   **Requirements:**
    *   `FR-401`: The system shall display a public FAQ page with questions and answers, categorized for browsing.
    *   `FR-402`: The system shall provide a form for users to submit a new question, capturing at minimum the question text and user's email address (for response).
    *   `FR-403`: Submitted questions shall be routed to a designated administrator for review and response. Posting an answer shall publish it to the public FAQ.

#### 3.5 Feature: Search and Resource Access
*   **Priority:** M
*   **Description:** Users can find information via internal search and access curated external links.
*   **Requirements:**
    *   `FR-501`: The site shall include a search function that queries internal page content (title and body text).
    *   `FR-502`: A "Resources" section shall list curated external articles and professional organizations (e.g., ACM, IEEE), displaying Title, Source/URL, Summary, and Tags.

#### 3.6 Feature: Dynamic Content (RSS Feed)
*   **Priority:** L
*   **Description:** The site can display periodically updated content from external CS news sources.
*   **Requirements:**
    *   `FR-601`: The system shall be capable of parsing and displaying headlines/summaries from at least one configured RSS feed on a designated page or sidebar.

#### 3.7 Feature: Site Analytics and Evaluation
*   **Priority:** M
*   **Description:** Administrators can assess site effectiveness through basic metrics.
*   **Requirements:**
    *   `FR-701`: The system shall integrate a mechanism (e.g., server logs, Google Analytics) to track page hits and user session engagement time.
    *   `FR-702`: Analytics data shall be accessible to site administrators in a report format.

### 4. Data Requirements

#### 4.1 Data Entities and Attributes
The following core data entities will be managed, likely through a combination of static HTML pages and a simple database or flat-file system for dynamic content.

```plaintext
Entity: CS_Professional_Profile
PK: Profile_ID (Integer)
Attributes:
- Name (String)
- Career_Stage (Enum: 'Recent Grad', 'Experienced')
- Job_Title (String)
- Biography (Text)
- Photo_URL (String)
- Video_URL (String, Optional)

Entity: OUS_Campus_Program
PK: Campus_ID (String, e.g., "OSU")
Attributes:
- Campus_Name (String)
- Degree_Offerings (Text)
- Program_Highlights (Text)
- Contact_Info (Text)

Entity: FAQ_Item
PK: Question_ID (Integer)
Attributes:
- Question_Text (Text)
- Answer_Text (Text)
- Category (String)
- Date_Posted (Date)
- Submitted_By_Email (String, Optional)

Entity: External_Resource
PK: Resource_ID (Integer)
Attributes:
- Title (String)
- Source_URL (String)
- Summary (Text)
- Tags (String)
- Type (Enum: 'Article', 'Organization')
```

#### 4.2 Data Volumes and Storage
*   Initial profiles: 10-20
*   OUS Campuses: ~7
*   FAQ items: Expected to grow slowly over time.
*   Storage for images and potential video files will be required on the OUS server.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-001`: (H) Page load times (server response + render) must be under 3 seconds for 95% of page views to accommodate users with short attention spans.

#### 5.2 Usability Requirements
*   `NFR-002`: (H) The interface must be designed for a high school (teen) audience, prioritizing visual appeal, intuitive icons, and scannable content chunks over dense text.
*   `NFR-003`: (M) The site must maintain a consistent look and feel across all pages via a shared CSS stylesheet.

#### 5.3 Compatibility Requirements
*   `NFR-004`: (M) The website must render and function correctly on the latest stable versions of major browsers as of launch, with special consideration for Internet Explorer, Firefox, and Netscape as per stakeholder input.

#### 5.4 Maintainability Requirements
*   `NFR-005`: (H) All HTML and CSS code must adhere to documented style conventions. All file updates must be managed using the Dreamweaver check-in/check-out system.

#### 5.5 Evaluability Requirements
*   `NFR-006`: (M) The site must support the collection of analytics data (hits, engagement time) as specified in `FR-701` and `FR-702`.

#### 5.6 Security and Compliance Requirements
*   `NFR-007`: (H) The site must comply with all OUS-wide security policies, copyright laws, and privacy standards (especially for submitted FAQ questions containing email addresses).

### 6. Other Requirements

#### 6.1 Development Standards
*   Use of semantic HTML where possible.
*   CSS for all presentation logic.
*   JavaScript to be used sparingly and degradably for enhancement.

#### 6.2 Business Rules
*   All profile content must be approved by the profiled individual and the CS Task Force.
*   All external resource links must be reviewed periodically for relevance and accuracy.
*   FAQ answers must be provided or vetted by a qualified CS professional or educator.

### 7. Appendix A: User Stories Mapped to Requirements
| User Story | Mapped Functional Requirements |
| :--- | :--- |
| *As a high school student interested in CS, I want to see profiles...* | FR-201, FR-202, FR-203 |
| *As a college-bound student, I want visually engaging, chunked information...* | FR-102, NFR-002 |
| *As a web designer, I want clear style conventions...* | NFR-005 |
| *As a member of the CS Task Force, I want student feedback incorporated...* | FR-701, FR-702 (informs updates) |
| *As the OUS administrator, I want the site hosted on performant servers...* | NFR-001, NFR-007 |
| *As a student exploring majors, I want to see how a CS minor complements...* | FR-303 |

### 8. Appendix B: Open Issues and TBDs
The following issues require stakeholder resolution prior to or during development:
1.  **College Listing Scope:** Final decision on including community/private Oregon colleges alongside OUS schools.
2.  **Video Profile Implementation:** Resource commitment and technical approach for hosting and displaying video profiles.
3.  **Search Tool Selection:** Specific software or service to be used for the internal site search (`FR-501`).
4.  **RSS Feed Curation:** Defined process and responsible party for selecting and maintaining RSS feed sources.
5.  **Ongoing Feedback Mechanism:** Concrete method for collecting and integrating post-launch student feedback (e.g., embedded survey, focus groups).
6.  **Content Update Schedule:** Formal review and update calendar for dynamic content (Programs, Resources, Profiles).