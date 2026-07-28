# Software Requirements Specification (SRS)
## For the Oregon University System Computer Science Recruitment Website

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Prepared for:** Oregon University System (OUS) Chancellor's Office  
**Prepared by:** [Your Name/Team Name]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Oregon University System (OUS) Computer Science (CS) Recruitment Website. The primary purpose of this document is to provide a detailed description of the system's features, constraints, and interfaces to serve as a reference for stakeholders, designers, developers, and testers throughout the project lifecycle.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Priority:** Requirements are prioritized as (H)igh, (M)edium, or (L)ow.
*   **Keywords:** `MUST`, `SHALL`, `WILL` indicate mandatory requirements. `SHOULD`, `COULD`, `MAY` indicate desirable but optional features.

#### 1.3 Project Scope
The scope of this project is to design, develop, and deploy a public-facing website with the singular goal of **attracting Oregon high school students to pursue computer science degrees at institutions within the Oregon University System.**

**In-Scope:**
*   Informational content about CS careers, OUS college programs, and professional resources.
*   Dynamic content featuring profiles of professionals in diverse CS fields.
*   A unified search functionality for internal and external CS-related information.
*   A responsive web design accessible on standard browsers and mobile devices.
*   Integration and compliance with the existing OUS web domain, servers, and branding guidelines.

**Out-of-Scope:**
*   Student application processing or university admissions systems.
*   User account creation, login, or personalized dashboards.
*   E-commerce or payment processing.
*   Real-time chat or complex interactive tools.
*   Development of a standalone mobile application.

#### 1.4 References
*   OUS Web Hosting and Domain Policy
*   OUS Branding and Style Guide
*   OUS IT Security Standards

### 2. Overall Description

#### 2.1 Product Perspective
This website is a new, independent subsystem that will reside within the broader OUS web ecosystem (`www.ous.edu` or a subdomain thereof). It will be a static/dynamic hybrid site, leveraging the OUS's existing server infrastructure and content management framework where possible. It must present a consistent user experience with other OUS digital properties while fulfilling its unique recruitment mission.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Primary: High School Students** | Ages 14-18; varying familiarity with CS; uses mobile devices heavily; seeks engaging, relatable content. | Easy-to-understand career info, relatable role models, clear paths to OUS programs, fast-loading media. |
| **Secondary: Educators/Parents** | Advisors to primary users; seeks credible, detailed information to provide guidance. | Comprehensive program details, data on career outcomes, trustworthy resources. |
| **Administrators (OUS Staff)** | Non-technical content managers; limited time for maintenance. | Simple, intuitive content update process without developer intervention. |

#### 2.3 Operating Environment
*   **Hosting:** OUS-approved servers and data centers.
*   **Domain:** Must be hosted under the official OUS domain (e.g., `cs.ous.edu`).
*   **Client-Side:** Must support current versions of Chrome, Firefox, Safari, and Edge on desktop, tablet, and mobile platforms.
*   **Network:** Must be designed for users with variable bandwidth, including areas with limited high-speed internet access.

#### 2.4 Design and Implementation Constraints
1.  **Hosting Constraint:** The entire application and its database MUST be deployed on OUS-managed infrastructure and comply with all OUS IT policies (`NFR-001`).
2.  **Bandwidth Constraint:** The design MUST optimize media (especially video) to be functional and informative for users with limited bandwidth. Video streaming should not be a barrier to accessing core content (`NFR-002`).
3.  **Resource Constraint:** Development MUST prioritize cost-effective solutions, utilize existing OUS-licensed tools/frameworks where possible, and favor simplicity and maintainability over complex custom features due to limited Chancellor's Office resources (`NFR-003`).

#### 2.5 Assumptions and Dependencies
*   **Assumption:** OUS marketing/communications staff will provide and maintain all textual and media content for careers, programs, and profiles.
*   **Assumption:** Necessary approvals for domain setup and server access will be provided by OUS IT in a timely manner.
*   **Dependency:** The project relies on the continued availability and stability of the chosen OUS hosting environment and any central authentication or CMS services.

### 3. System Features and Requirements

#### 3.1 Feature 1: Informational Content Delivery
**Description:** The website shall present structured, easy-to-navigate information about Computer Science careers, degree programs within OUS, and professional resources (e.g., internships, clubs).

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| `FR-101` | The system SHALL provide a dedicated "Careers in CS" section with pages detailing various CS fields, typical job roles, salary ranges, and growth outlook. | H |
| `FR-102` | The system SHALL provide a dedicated "OUS Programs" section with pages for each participating university, listing CS degree options, unique selling points, and contact links. | H |
| `FR-103` | The system SHALL provide a "Resources" section with links to external authoritative sites (e.g., ACM, Code.org), scholarship information, and internship opportunities. | M |
| `FR-104` | All informational pages SHALL support the inclusion of images, graphics, and text formatted according to OUS style guides. | M |

#### 3.2 Feature 2: Professional Profile Showcase
**Description:** The website shall feature dynamic profiles of real people working in diverse CS fields, with a focus on relatability to Oregon high school students.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| `FR-201` | The system SHALL provide a "Meet the Pros" or "Profiles" section displaying a gallery of individual professional profiles. | H |
| `FR-202` | Each profile SHALL include a photo, name, job title, employer, short biography, educational background (highlighting OUS if applicable), and a "Day in the Life" description. | H |
| `FR-203` | Each profile SHALL have the option to include a short, low-bandwidth-optimized video interview (max 2-3 minutes) or a text-based Q&A. | M |
| `FR-204` | Profiles SHALL be filterable or taggable by criteria such as "OUS Alumnus," "Career Field," or "Location in Oregon." | M |
| `NFR-201` | Profile videos MUST use efficient compression (e.g., H.264) and provide a fallback transcript or summary for users with slow connections (`NFR-002`). | H |

#### 3.3 Feature 3: Unified Search Functionality
**Description:** The website shall include a single search interface that allows users to find content both within the site and from a curated set of external CS resources.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| `FR-301` | The system SHALL provide a prominent search bar on all major pages. | H |
| `FR-302` | The search function SHALL return relevant results from internal pages (careers, programs, profiles, resources). | H |
| `FR-303` | The search function SHALL be configurable to include results from a pre-defined list of trusted external domains (e.g., `bls.gov/computer-and-information-technology`, `code.org`). | M |
| `FR-304` | Search results SHALL clearly distinguish between internal and external links. | M |

#### 3.4 Feature 4: Content Management
**Description:** Authorized OUS staff shall be able to update website content without requiring direct code changes.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| `FR-401` | The system SHALL provide a secure administrative interface for content editors to add, edit, and delete professional profiles. | H |
| `FR-402` | The system SHALL allow editors to update basic text and images on informational pages through a simple WYSIWYG or form-based interface. | M |
| `NFR-401` | The administrative interface MUST use existing OUS single sign-on (SSO) credentials for authentication, if available. | H |

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   `NFR-P01`: All static pages (text, images) shall load in under 3 seconds on a standard broadband connection.
*   `NFR-P02`: The site shall remain functional and navigable on connections as slow as 1.5 Mbps, with video content being optional or heavily optimized (`NFR-002`).

#### 4.2 Security Requirements
*   `NFR-S01`: The site shall comply with all OUS IT security policies for public-facing websites.
*   `NFR-S02`: Any administrative backend shall be protected against common web vulnerabilities (e.g., SQL injection, XSS).

#### 4.3 Maintainability & Support
*   `NFR-M01`: The system shall be built using well-documented, sustainable technologies approved by OUS IT to ensure long-term maintainability with limited resources (`NFR-003`).
*   `NFR-M02`: The codebase and content structure shall be clearly organized to allow for future handoff between developers.

#### 4.4 Usability Requirements
*   `NFR-U01`: The site shall achieve a WCAG 2.1 AA compliance level for accessibility.
*   `NFR-U02`: The navigation structure shall be intuitive, allowing a high school student to find key information (careers, programs) within 3 clicks from the homepage.

---
**APPROVAL**

| Name | Role | Signature | Date |
| :--- | :--- | :--- | :--- |
| *[OUS Project Sponsor]* | Project Sponsor | | |
| *[Lead Developer]* | Development Lead | | |
| *[System Architect]* | System Architect | | |