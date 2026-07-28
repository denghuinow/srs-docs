# Software Requirements Specification (SRS)
## Get Real Website - Version 2

**Document Version:** 1.0
**Date:** [Date of Creation]
**Project:** Get Real Website Redesign
**Client:** Oregon University System (OUS) - Computer Science Task Force
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for Version 2 of the Get Real website (`getreal.ous.edu`). The primary purpose of this document is to provide a detailed description of the system to be developed, serving as a basis for agreement between stakeholders and as a guide for the design and development teams. This SRS will be used by web designers, project managers, and the Computer Science Task Force for implementation, verification, and project management.

#### 1.2 Scope
Version 2 of the Get Real website is a comprehensive redesign and enhancement of the existing site (created in 2006). The project's core objective is to create a more engaging, teen-friendly online resource that effectively encourages Oregon high school students to pursue computer science (CS) degrees and minors within the Oregon University System.

**In-Scope:**
*   Complete visual and structural redesign of all existing web pages.
*   Implementation of improved, intuitive site navigation.
*   Development of new functional sections: Integrated Search, "Ask a Grad or Prof" FAQ, RSS feed display, and High School Course Recommendations.
*   Enhancement of content presentation using shorter text chunks, bullet points, charts, and increased visual elements (photos, video profiles).
*   Cross-browser compatibility testing (IE, Firefox, Netscape).
*   Performance optimization to match OUS standards.

**Out-of-Scope (Non-Goals):**
*   Development of a comprehensive CS knowledge base or wiki.
*   Creation of extensive user documentation or tutorials.
*   Building a fully-featured community forum or social network.
*   These items are deferred for consideration in a potential Version 3.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **CS:** Computer Science
*   **OUS:** Oregon University System
*   **ETIC:** [Expand if known, e.g., Education and Technology Innovation Committee]
*   **SRS:** Software Requirements Specification
*   **UI:** User Interface
*   **RSS:** Really Simple Syndication
*   **FAQ:** Frequently Asked Questions
*   **SLA:** Service Level Agreement
*   **DSS:** [Expand if known, e.g., Data Subscription Service]

#### 1.4 References
*   Get Real Website Version 1 (Existing Site)
*   OUS Web Standards and Policies (`www.ous.edu`)
*   Project Charter and Initial Summary Document (Provided)

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its stakeholders, and operating environment. Section 3 details the specific functional and non-functional requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The Get Real V2 website is a standalone informational web application but exists within the OUS web ecosystem. It is dependent on the OUS web server for hosting and must comply with OUS design and security policies. It integrates externally with an RSS feed from the Chancellor's Office and may leverage an external search engine API (e.g., Google Custom Search) for extended search capabilities.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **High School Student (CS-Interested)** | Primary target. Actively seeking detailed info on CS university programs and careers. Requires concise, in-depth, comparable data. | Explore and compare OUS CS programs; understand career paths and requirements. |
| **High School Student (College-bound, Non-CS)** | Secondary target. Needs to be engaged and have CS presented as an attractive option. Low initial interest, short attention span. | Discover CS as a potential major through compelling, visual, and easy-to-digest content. |
| **Student Considering a CS Minor** | Niche target. Interested in combining CS with another field (medicine, law, business). | Understand the value and structure of a CS minor across OUS campuses. |
| **High School Counselor** | Indirect user. Advisor who may recommend the site. Needs accurate, trustworthy information to share. | Quickly find reliable resources to direct students to relevant CS information. |
| **Web Designer/Developer** | Primary system builder and maintainer. Technical skill varies. | Implement requirements accurately; maintain and update site content and functionality efficiently. |
| **OUS Campus Representative** | Content contributor (program info, FAQ answers). Subject matter expert. | Provide accurate program data; engage with student questions. |
| **Computer Science Task Force** | Product owner and stakeholder. Provides oversight and final requirements. | Ensure site meets strategic goals of increasing CS enrollment within OUS. |

#### 2.3 Operating Environment
*   **Server Environment:** Standard OUS web hosting infrastructure.
*   **Client Environment:** Must be fully functional and visually consistent on Internet Explorer, Firefox, and Netscape browsers common in 2006-era high school environments.
*   **Network Environment:** Accessible via standard internet connections; must perform adequately on typical school and home bandwidth.

#### 2.4 Design and Implementation Constraints
1.  **Visual Design:** Must adhere to OUS website branding and style conventions, while evolving from the existing Get Real V1 design.
2.  **Technology:** Solution must be compatible with existing OUS server technology stack and maintenance workflows.
3.  **Content Management:** Dynamic content features (FAQ, RSS) must be maintainable with limited dedicated web designer hours.
4.  **Legal:** Must comply with OUS copyright, privacy, and security policies.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** OUS web hosting will provide performance and uptime comparable to `www.ous.edu`.
*   **Assumption:** The Chancellor's Office DSS RSS feed will remain available and consistently formatted.
*   **Assumption:** OUS campuses will provide timely and accurate CS program information and FAQ responses.
*   **Dependency:** Project timeline is dependent on the availability of Chancellor's Office web design resources.
*   **Dependency:** Successful engagement relies on the procurement of compelling "Real People" video and profile content.

### 3. System Features and Requirements

#### 3.1 Feature: Teen-Friendly Design & Navigation
**Description:** The entire site shall undergo a visual and structural redesign to appeal to a high school audience, emphasizing clarity, engagement, and ease of use.

**3.1.1 Requirements:**
*   **REQ-DESIGN-001:** The homepage shall utilize ample white space, short paragraphs, bulleted lists, and integrated visual elements (relevant photos, info-graphics, charts).
*   **REQ-DESIGN-002:** A clear, consistent, and intuitive global navigation menu shall be present on all pages.
*   **REQ-DESIGN-003:** Text content across all informational pages (e.g., Jobs & Money, Exploring College) shall be presented in "chunked" formats, prioritizing scannability.
*   **REQ-DESIGN-004:** The "Real People" section shall present profiles using a visually dominant layout (e.g., large photos, video thumbnails) with concise, personal biography summaries.

#### 3.2 Feature: Comprehensive CS Information Portal
**Description:** The site shall serve as a central, reliable source for information on OUS CS programs, careers, and preparation.

**3.2.1 Requirements:**
*   **REQ-INFO-001:** An "Exploring College" section shall provide a clear, structured listing of Computer Science degree and minor offerings for all seven OUS campuses, including contact information.
*   **REQ-INFO-002:** A "High School Courses" page shall display recommended preparatory courses, citing sources (e.g., ACM, UO).
*   **REQ-INFO-003:** A "Jobs & Money" section shall present career outlook and salary information using charts and digestible data points.
*   **REQ-INFO-004:** A "Professional Organizations" page shall provide curated links to relevant external CS organizations.

#### 3.3 Feature: Integrated Search Functionality
**Description:** Users shall be able to search for information both within the Get Real site and across a curated set of external CS resources.

**3.3.1 Requirements:**
*   **REQ-SEARCH-001:** A search bar shall be prominently accessible on all pages.
*   **REQ-SEARCH-002:** The search function shall allow users to select scope: "This Site" or "CS Web" (external).
*   **REQ-SEARCH-003:** Internal search shall return relevant results from the Get Real website's content.
*   **REQ-SEARCH-004:** External search shall return results from a pre-defined, curated list of authoritative CS websites (implementation may use a custom search engine).

#### 3.4 Feature: Dynamic & Interactive Content
**Description:** The site shall include features that provide fresh content and user interaction to encourage repeat visits and deeper engagement.

**3.4.1 Feature: "Ask a Grad or Prof" FAQ**
*   **REQ-FAQ-001:** Users shall be able to submit a question via a web form.
*   **REQ-FAQ-002:** Submitted questions shall be routed to a designated OUS graduate or professor for answering.
*   **REQ-FAQ-003:** An administrative interface shall allow for reviewing and approving Q&A pairs.
*   **REQ-FAQ-004:** Approved Q&A pairs shall be displayed in a public, searchable FAQ listing, ordered by date posted.

**3.4.2 Feature: RSS News Feed**
*   **REQ-RSS-001:** The site shall include a section (e.g., "CS News") that displays headlines and summaries from a specified Chancellor's Office DSS RSS feed.
*   **REQ-RSS-002:** A web designer shall be able to update the RSS feed source URL via a maintained configuration.
*   **REQ-RSS-003:** Feed items shall display title, source, summary, and publication date, and link to the full external article.

**3.4.3 Feature: Real People Video Profiles**
*   **REQ-VIDEO-001:** The "Real People" profile pages shall support embedded video content.
*   **REQ-VIDEO-002:** Video players shall launch in-page or via a lightweight modal window.
*   **REQ-VIDEO-003:** Video assets must be optimized for web delivery to ensure reasonable load times on standard high school connections.

#### 3.5 Non-Functional Requirements

**3.5.1 Performance:**
*   **REQ-PERF-001:** Average page load times shall be comparable to, and not statistically slower than, the main `www.ous.edu` website.
*   **REQ-PERF-002:** The site shall handle concurrent user traffic typical of a statewide educational resource without significant performance degradation.

**3.5.2 Reliability & Availability:**
*   **REQ-RELY-001:** The website shall maintain uptime consistent with standard OUS web hosting service level agreements.

**3.5.3 Security & Compliance:**
*   **REQ-SEC-001:** The site shall fully adhere to OUS website security, privacy, and copyright policies.
*   **REQ-SEC-002:** All administrative interfaces (for FAQ moderation, RSS config) shall require appropriate OUS authentication.

**3.5.4 Maintainability & Compatibility:**
*   **REQ-MAINT-001:** CSS and styling shall be consistent with both the updated Get Real brand and overarching OUS web standards.
*   **REQ-MAINT-002:** The site shall render and function correctly on Internet Explorer, Firefox, and Netscape browsers.
*   **REQ-MAINT-003:** The site shall implement 301 redirects from all legacy Get Real V1 page URLs to their new V2 locations to preserve bookmark and link integrity.

**3.5.5 Observability:**
*   **REQ-OBS-001:** The site shall integrate with standard OUS web analytics (or an agreed-upon alternative) to track page hits, user flow, and time-on-page metrics.

### 4. Acceptance Criteria
(Summarized in Gherkin-style format for key capabilities)

**Engaging Teen-Friendly Design:**
*   **Scenario:** Viewing Redesigned Homepage
    *   Given a student has navigated to `getreal.ous.edu`
    *   When the homepage loads
    *   Then the layout presents text in short paragraphs with ample white space
    *   And key information is highlighted using bullet points and visual elements (photos, charts)

**Comprehensive Information Access:**
*   **Scenario:** Comparing University Programs
    *   Given a student wants to compare CS programs
    *   When they navigate to the "Exploring College" section
    *   Then they are presented with a clear, structured list of offerings
    *   And this list includes degree information from all seven OUS campuses

**Dynamic Content Management:**
*   **Scenario:** FAQ Publication
    *   Given a user has submitted a valid question via the "Ask a Grad or Prof" form
    *   And an administrator has reviewed and approved a corresponding answer
    *   When the FAQ listing page is viewed
    *   Then the new Q&A pair is visible in the public list

### 5. Appendices

#### 5.1 Domain Model Entities & Attributes
*   **Web Page:** `{Title: string, Content: html, NavigationPath: string, LastUpdated: date}`
*   **University Program:** `{CampusName: string (req), DegreeOfferings: text, ContactInfo: text}`
*   **Real Person Profile:** `{Name: string (req), CareerStage: enum, Biography: text, MediaAsset: url, CareerField: string}`
*   **FAQ Item:** `{Question: text (req), Answer: text (req), DatePosted: date, Status: enum}`
*   **RSS Feed Item:** `{Title: string (req), Source: string, Summary: text, Link: url (req), PubDate: date}`

#### 5.2 Interface Specifications
*   **User Interface:** HTML/CSS/JS delivered via HTTP/HTTPS. Must comply with browser compatibility matrix.
*   **RSS Integration:** Inbound consumption of XML feed from a configurable URL. Parser must handle standard RSS 2.0 format.
*   **Search Integration:** Outbound API calls to external search service (e.g., Google Custom Search JSON API) with predefined site restrictions.

#### 5.3 Open Issues & Decisions Pending
| Issue ID | Description | Responsible Party |
| :--- | :--- | :--- |
| OI-01 | Final extent of listing non-OUS colleges (community/private). | CS Task Force / OUS Liaison |
| OI-02 | Source and maintenance process for "High School Courses" data. | UO (Lead) & CS Task Force |
| OI-03 | Moderation workflow and ownership for the "Ask a Grad or Prof" FAQ. | CS Task Force & OUS Campuses |
| OI-04 | Final decision on FAQ implementation (static vs. BLOG platform). | CS Task Force & Web Designers |

---
*This document is considered the authoritative source of requirements for the Get Real Website Version 2 project. Any changes must be reviewed and approved by the Computer Science Task Force.*