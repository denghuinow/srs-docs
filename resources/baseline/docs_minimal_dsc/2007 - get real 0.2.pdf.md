# Software Requirements Specification (SRS)
## For: Oregon University System Computer Science Recruitment Website

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Prepared for:** Oregon University System (OUS) Chancellor's Office  
**Prepared by:** [Your Name/Team Name]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Oregon University System (OUS) Computer Science Recruitment Website. The primary purpose of this document is to provide a detailed description of the system's features, constraints, and interfaces to serve as a reference for developers, testers, project managers, and stakeholders. This SRS will be the basis for design, implementation, and verification.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Priority:** Requirements are prioritized as (H)igh, (M)edium, or (L)ow.
*   **Keywords:** `MUST`, `SHALL`, `WILL` indicate mandatory requirements. `SHOULD`, `COULD`, `MAY` indicate desirable but not mandatory features.

#### 1.3 Project Scope
The system is a public-facing website designed to attract Oregon high school students (grades 9-12) to pursue computer science degrees at campuses within the Oregon University System. The website will serve as a centralized, engaging information hub, moving beyond static program listings to dynamically connect academic opportunities with real-world career outcomes. The scope includes front-end website development, content management capabilities, and integration with existing OUS infrastructure. It explicitly excludes backend student application systems, university admissions processes, and any form of user account creation or login for students.

#### 1.4 References
*   OUS IT Infrastructure and Hosting Policies
*   OUS Branding and Visual Identity Guidelines
*   Web Content Accessibility Guidelines (WCAG) 2.1 AA

### 2. Overall Description

#### 2.1 Product Perspective
This system is a new, independent web application that will reside within the `ous.edu` domain. It will be hosted on Oregon State University (OSU) servers and must interoperate with existing OUS web standards and templates. It is a self-contained system but may link to external OUS university program pages and third-party career data sources.

#### 2.2 Product Functions (Summary)
1.  Present structured, comparable information on CS undergraduate programs offered at all OUS campuses.
2.  Display career pathway information, including job titles, descriptions, and salary ranges for CS graduates.
3.  Host a gallery of multimedia profiles featuring diverse professionals working in computer science fields.
4.  Provide an intuitive, visually engaging, and age-appropriate navigation structure for high school students.
5.  Allow authorized OUS staff to update website content (programs, careers, profiles) via a secure interface.

#### 2.3 User Classes and Characteristics
*   **High School Students (Primary):** Oregon residents in grades 9-12. Varied levels of technical proficiency and prior interest in CS. Motivated by exploration, future opportunities, and relatable role models. Access the site primarily from school or personal computers.
*   **OUS Content Administrators (Secondary):** Staff from the Chancellor's office or member universities. Technically proficient enough to use a web-based CMS. Responsible for keeping program, career, and profile information accurate and current.
*   **General Public (Secondary):** Parents, teachers, guidance counselors. Seek information to support students.

#### 2.4 Operating Environment
*   **Hardware:** Virtual servers provided by OSU's central IT.
*   **Software:** Must be compatible with the standard OUS LAMP/LEMP (Linux, Apache/Nginx, MySQL, PHP) or equivalent stack.
*   **Browsers:** The public website **MUST** support:
    *   Internet Explorer 11+
    *   Firefox (latest stable version)
    *   Netscape Navigator (latest version compatible with modern web standards)
*   **Network:** Accessible via the public internet. Subject to OUS network bandwidth policies.

#### 2.5 Design and Implementation Constraints
1.  **Hosting Constraint:** The application MUST be deployed and operated within the OUS domain (`*.ous.edu`) on OSU-provided servers.
2.  **Resource Constraint:** Design and media (especially video) MUST be optimized to function within limited allocated server storage and network bandwidth.
3.  **Browser Constraint:** Full functionality and core content MUST be accessible on the browsers specified in Section 2.4.
4.  **Resource Constraint:** Development and maintenance are limited to the budget and personnel resources allocated by the Chancellor's Office.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** OUS member institutions will provide accurate and timely data about their CS programs.
*   **Assumption:** High school students have access to a reasonably modern computer and internet connection at school or home.
*   **Dependency:** Project timelines are dependent on OUS stakeholder availability for content creation and review.
*   **Dependency:** The site's career salary data may depend on third-party APIs or datasets which must remain publicly available.

### 3. System Features

#### 3.1 Feature 1: University Program Information
**Description:** This feature will present detailed, standardized information about Computer Science and related undergraduate degree programs at each OUS campus.

**Priority:** High

**Requirements:**
*   `FR-101`: The system SHALL display a dedicated page or section for each OUS campus offering a CS-related degree. (H)
*   `FR-102`: For each program, the system SHALL display a standardized set of data points: program name, degree type (BS, BA), brief description, key coursework, and a direct link to the official university program page. (H)
*   `FR-103`: The system SHALL provide a comparison view (e.g., a table) allowing users to view key data points for multiple selected programs side-by-side. (M)
*   `FR-104`: The system SHALL include a filter/search function allowing users to find programs by criteria such as campus location, degree type, or specific focus areas (e.g., AI, Cybersecurity). (M)

#### 3.2 Feature 2: Career & Salary Information
**Description:** This feature will provide information about potential career paths, roles, and earning potential for graduates with CS degrees.

**Priority:** High

**Requirements:**
*   `FR-201`: The system SHALL display a list of common career roles for CS graduates (e.g., Software Developer, Data Scientist, UX Designer). (H)
*   `FR-202`: For each career role, the system SHALL display a description, typical required skills, and a salary range (e.g., Oregon median entry-level and experienced salaries). (H)
*   `FR-203`: The system SHALL source and clearly cite salary data from a reputable, publicly-available source (e.g., Bureau of Labor Statistics). (H)
*   `FR-204`: Career pages SHALL link to relevant "Profile" features (see FR-301) where applicable. (M)

#### 3.3 Feature 3: Professional Profiles
**Description:** This feature will showcase video and/or written profiles of real people from diverse backgrounds working in computer science fields.

**Priority:** High

**Requirements:**
*   `FR-301`: The system SHALL host a gallery of individual professional profiles. (H)
*   `FR-302`: Each profile SHALL include the individual's name, job title, employer, photo, a brief biography, and their educational path (including OUS campus if applicable). (H)
*   `FR-303`: Each profile SHOULD include a short, streamable video interview (≤ 2 minutes). (M)
*   `NFR-304`: Video content MUST be highly compressed and use a streaming-friendly format (e.g., H.264/MP4) to respect bandwidth constraints. (H)
*   `FR-305`: Profiles SHALL be taggable (e.g., by career role, OUS alma mater, background) and filterable via the user interface. (M)

#### 3.4 Feature 4: Content Management System (CMS)
**Description:** A secure back-end interface for authorized OUS administrators to manage website content without direct code deployment.

**Priority:** Medium

**Requirements:**
*   `FR-401`: The system SHALL provide a secure admin login portal separate from the public site. (H)
*   `FR-402`: Authorized administrators SHALL be able to Create, Read, Update, and Delete (CRUD) entries for University Programs, Career Information, and Professional Profiles through a web-based interface. (H)
*   `FR-403`: The CMS interface for adding a Professional Profile SHALL support uploading images and video files, which are automatically processed/optimized. (M)
*   `NFR-404`: Admin access SHALL be restricted by IP address or OUS VPN and require strong password authentication. (H)

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The public site shall have a modern, visually engaging design appropriate for a high school audience.
*   Navigation shall be simple, consistent, and use non-technical language.
*   All text shall comply with a minimum readability standard for a 9th-grade level.
*   The administrative CMS shall have a clean, form-based UI typical of modern content management systems (e.g., WordPress, Drupal admin panels).

#### 4.2 Hardware Interfaces
None specified beyond standard server hardware.

#### 4.3 Software Interfaces
*   **OUS Identity Management:** The admin CMS may interface with OUS LDAP or Single Sign-On (SSO) for authentication, if available.
*   **External Data:** The career/salary module may pull data via a secure API from a trusted public data source.

#### 4.4 Communications Interfaces
*   The system shall communicate over HTTP/HTTPS.
*   All public pages shall be served over HTTPS.
*   The system shall send transactional emails (e.g., password reset for admins) via the OSU mail server.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-501`: Public web pages shall have an average load time of less than 3 seconds on a standard broadband connection. (H)
*   `NFR-502`: The CMS shall allow an administrator to update a profile or program entry and see the change reflected on the public site within 60 seconds. (M)

#### 5.2 Safety Requirements
Not applicable.

#### 5.3 Security Requirements
*   `NFR-503`: The application shall be developed following OWASP Top 10 security guidelines to prevent common vulnerabilities (e.g., SQL injection, XSS). (H)
*   `NFR-504`: All administrator sessions shall timeout after 15 minutes of inactivity. (M)
*   `NFR-505`: The public site shall not collect any personally identifiable information (PII) from student visitors. (H)

#### 5.4 Software Quality Attributes
*   **Availability:** The public website shall have 99.5% uptime during standard school hours (7:00 AM - 5:00 PM PST).
*   **Maintainability:** The codebase shall be well-documented to allow future OUS developers to make updates.
*   **Accessibility:** The website shall conform to WCAG 2.1 AA standards to ensure accessibility for users with disabilities. (H)
*   **Usability:** The primary navigation and call-to-action buttons shall be intuitively located and tested with a group of target high school users prior to launch.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor, OUS | | | |
| Lead Developer | | | |
| SRS Author | | | |