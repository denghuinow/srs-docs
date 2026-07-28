# Software Requirements Specification (SRS)
## For the Get Real Website Project

**Document Version:** 1.0
**Date:** [Current Date]
**Project Sponsor:** Oregon University System (OUS) Chancellor's Office
**Prepared For:** Computer Science Task Force Subcommittee (ETIC)
**Prepared By:** [Your Organization/Team Name]

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the redesign and enhancement of the Get Real website. The purpose of this project is to create a more engaging, informative, and effective online platform to encourage Oregon high school students to pursue computer science degrees within the Oregon University System. This SRS serves as a contract between the development team, the ETIC subcommittee, and the OUS Chancellor's Office, and will be the basis for design, development, testing, and project evaluation.

#### 1.2 Document Conventions
This document follows standard IEEE SRS formatting conventions. Requirements are uniquely identified with labels (e.g., **FR-1** for Functional Requirement 1, **NFR-1** for Non-Functional Requirement 1). Markdown is used for structure, with headers, lists, and code blocks to enhance readability.

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Sponsors & ETIC Subcommittee:** Should review the entire document, focusing on Sections 1 (Introduction), 2 (Overall Description), and 5 (Success Metrics).
*   **Web Designers & Developers:** Should review the entire document, with particular attention to Sections 3 (System Features) and 4 (External Interface Requirements).
*   **Content Providers & Stakeholders (OUS Campuses):** Should review Sections 2.2 (Stakeholders) and 3 (System Features) to understand their contribution points.
*   **Testers & QA:** Should review Sections 3 and 4 to derive test cases and validation criteria.

#### 1.4 Project Scope
The scope of this project encompasses the comprehensive redesign of the existing Get Real website to improve user engagement and information delivery for Oregon high school students (grades 9-12). This includes visual redesign, information architecture restructuring, addition of new content sections, integration of multimedia, implementation of a search function, and the addition of site analytics. The project is explicitly bounded by the "In Scope" and "Out of Scope" items detailed in the project summary.

### 2. Overall Description

#### 2.1 Product Perspective
The Get Real website is a standalone informational website hosted within the OUS web ecosystem. It must adhere to OUS design conventions, branding guidelines, and security standards. It will consume and display content from internal sources (OUS campus CS program data) and external sources (RSS feeds from professional organizations, links to external career sites). It is not integrated with student information systems or other specialized OUS software.

#### 2.2 Stakeholders and User Characteristics
| Stakeholder Group | Primary Interest / Role |
| :--- | :--- |
| **Oregon High School Students (Primary User)** | Seeking engaging, credible information on CS careers, college programs, and preparation. Varied levels of technical interest and knowledge. |
| **Web Designers (Primary Maintainer)** | Develop, test, maintain, and update site content and functionality. Require manageable tools and analytics. |
| **ETIC Subcommittee (Primary Client)** | Define strategic direction, approve requirements, and evaluate project success. |
| **OUS Campuses (Content Provider)** | Provide accurate, compelling details about their CS degree programs, faculty, and unique offerings. |
| **High School Counselors (Secondary User)** | Refer students to the site as a reliable resource for CS career and college planning. |
| **OUS Chancellor's Office (Host/Sponsor)** | Provide hosting infrastructure, ensure institutional alignment, and allocate limited resources. |

#### 2.3 Operating Environment
*   **Software:** The website must be fully accessible and functionally tested on the following major web browsers: Internet Explorer, Firefox, and Netscape Navigator.
*   **Hardware:** Standard consumer-grade computers and devices used in high schools and homes.
*   **Network:** Must be optimized to perform adequately within typical school and residential bandwidth constraints, particularly for streaming video content.

#### 2.4 Design and Implementation Constraints
1.  **Resource Constraints:** Development and maintenance are subject to the limited availability of Chancellor’s Office web design staff hours.
2.  **Technical Constraints:** Video content must be optimized for streaming within identified bandwidth limitations.
3.  **Compliance Constraints:** The site must adhere to OUS site-wide design conventions, branding, and existing security standards.
4.  **Process Constraints:** Design and feature prioritization must be validated through feedback from two distinct student user groups (e.g., students interested in CS and those unsure).
5.  **Content Constraints:** The site depends on externally curated content (RSS feeds, professional org links), requiring defined processes for ongoing review and updates.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** OUS campuses will provide timely and accurate content for their respective program pages.
*   **Assumption:** High school students have access to a modern web browser and a basic broadband internet connection.
*   **Dependency:** Project timeline is dependent on timely feedback and content provision from the ETIC subcommittee and OUS campuses.
*   **Dependency:** The functionality of external RSS feeds and linked resources is outside the project's direct control.

### 3. System Features

#### 3.1 Feature 1: Redesigned Core Content Pages
**Description:** The existing core informational pages ("Exploring College," "Jobs & Money," "Real People") will be visually redesigned and restructured for improved teen appeal, readability, and navigation.
*   **FR-1.1:** The system shall present all core content pages with a modern, visually engaging design that appeals to a high school demographic.
*   **FR-1.2:** The "Real People" section shall be enhanced to include integrated multimedia profiles (see Feature 3).
*   **FR-1.3:** Navigation between these core pages and new site sections shall be consistent and intuitive.

#### 3.2 Feature 2: New Informational Sections
**Description:** New dedicated sections will be added to provide comprehensive preparatory and career information.
*   **FR-2.1:** The system shall include a "High School Courses" page detailing recommended mathematics, science, and technology courses to prepare for a CS degree.
*   **FR-2.2:** The system shall include a "Professional Organizations" page listing relevant national and local CS organizations (e.g., ACM, IEEE-CS) with descriptions and links.
*   **FR-2.3:** Content shall explicitly address the value of a CS minor for students in other fields (e.g., pre-med, business, law).

#### 3.3 Feature 3: Multimedia Profiles
**Description:** Video and/or rich-media profiles of diverse CS professionals (including OUS graduates) will be incorporated to showcase real career paths.
*   **FR-3.1:** The system shall display video profiles within the "Real People" or a dedicated "Profiles" section.
*   **NFR-3.1:** Video files shall be optimized (e.g., format, compression, resolution) to stream reliably within the identified bandwidth constraints.
*   **FR-3.2:** Each profile shall include text-based key takeaways (job title, degree path, daily work description).

#### 3.4 Feature 4: Site Search Functionality
**Description:** A search tool will allow users to find content both within the Get Real site and across a curated set of external CS resources.
*   **FR-4.1:** The system shall provide a search interface on all major pages.
*   **FR-4.2:** The search function shall return relevant results from the internal Get Real website content.
*   **FR-4.3:** The search function shall provide the option to include results from a pre-defined, curated list of external career and education websites (e.g., ACM Career Resource Page, Bureau of Labor Statistics).

#### 3.5 Feature 5: Usage Tracking and Analytics
**Description:** Backend functionality will be implemented to collect data on site usage to inform future improvements.
*   **FR-5.1:** The system shall track and record key metrics including page hits, unique visits, session duration, and common navigation paths.
*   **FR-5.2:** The system shall provide an administrative dashboard (or integrate with existing OUS analytics) where web designers can view summarized usage reports.
*   **NFR-5.1:** Analytics collection must comply with OUS privacy policies and applicable regulations (e.g., not collecting personally identifiable information from minor students).

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The overall look and feel shall conform to OUS website design conventions while employing a "teen-friendly" aesthetic (e.g., dynamic, clean, using imagery of peers).
*   Navigation shall be simple, with a persistent global menu providing access to: Home, Exploring College, Jobs & Money, Real People/Profiles, High School Courses, Professional Organizations, and Search.

#### 4.2 Hardware Interfaces
None required. The system is a standard website.

#### 4.3 Software Interfaces
1.  **OUS Web Hosting Environment:** The site must be compatible with the OUS Chancellor's Office web servers and hosting stack.
2.  **RSS Feeds:** The system shall be capable of consuming and displaying content from selected RSS feeds (e.g., from computing professional organizations).
3.  **External Links:** The system will maintain a managed list of links to external career information sites.

#### 4.4 Communications Interfaces
Standard HTTP/HTTPS protocols for web delivery.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NFR-PERF-1:** All static pages shall load completely in under 3 seconds on a standard broadband connection.
*   **NFR-PERF-2:** The search function shall return results in under 2 seconds for internal searches.

#### 5.2 Safety and Security Requirements
*   **NFR-SEC-1:** The website shall inherit and adhere to the general security standards and protocols of the main OUS website.
*   **NFR-SEC-2:** No custom login or user data collection from students is required for this version, minimizing security surface area.

#### 5.3 Software Quality Attributes
*   **Usability:** The site shall achieve a positive usability rating from >80% of high school student participants in formal user testing.
*   **Reliability:** The site shall have 99.5% uptime, excluding scheduled maintenance.
*   **Maintainability:** The code and content structure shall allow a web designer to update standard page content within the OUS CMS without developer assistance.
*   **Portability:** The site shall render and function correctly on the specified browser list (IE, Firefox, Netscape).

### 6. Success Metrics & Evaluation
The success of the Get Real website project will be measured by the following key performance indicators (KPIs), to be evaluated 6 and 12 months post-launch:
1.  **Engagement:** A 25% increase in average time spent on site and a 40% increase in total page views compared to the pre-redesign baseline.
2.  **User Satisfaction:** Positive qualitative feedback from user testing sessions with the target demographic, specifically regarding visual appeal and ease of finding information.
3.  **Strategic Impact:** An upward trend in the number of Oregon resident freshmen enrolling in CS majors across OUS campuses, as measured by annual institutional data (recognizing this is a long-term, multi-factorial metric).

### Appendix A: Undecided / TBD Issues
The following items require resolution by the ETIC subcommittee and project sponsors:
1.  The final decision on the extent of listing community and private colleges in the "Exploring College" section.
2.  The specific technical and editorial implementation model for the "Ask a Grad or Prof – FAQ" feature.
3.  Prioritization of any new page ideas proposed after the signing of this SRS.
4.  Formal allocation of weekly web designer hours for the ongoing curation of RSS feeds and external links.
5.  Final, approved list of external career information websites to be included in the search function and links pages.

### Appendix B: Glossary
*   **CS:** Computer Science
*   **ETIC:** [Expansion if known, e.g., Engineering and Technology Industry Council] Computer Science Task Force Subcommittee.
*   **OUS:** Oregon University System
*   **RSS:** Really Simple Syndication – a web feed format for publishing frequently updated content.