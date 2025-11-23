```markdown
# Software Requirements Specification
# Get Real Website Version 2.0

**Document Version:** 1.0  
**Date:** [Current Date]  
**Project:** Get Real Website Update  
**Client:** Oregon University System (OUS)  
**Status:** Draft

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [System Features](#3-system-features)
4. [External Interface Requirements](#4-external-interface-requirements)
5. [Non-Functional Requirements](#5-non-functional-requirements)
6. [Other Requirements](#6-other-requirements)

---

## 1 Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Get Real Website Version 2.0. The system aims to attract Oregon high school students (grades 9-12) to pursue computer science degrees at Oregon University System campuses.

### 1.2 Scope
The Get Real system shall provide career information, campus resources, and student-focused content specifically designed to encourage computer science enrollment among Oregon high school students.

**In-Scope:**
- Career information and professional profiles
- Campus resource directories
- Student-focused engaging content
- Internal search functionality
- Video content featuring CS professionals

**Out-of-Scope:**
- Non-educational content
- Direct admissions processing
- Support for students outside Oregon
- Integration with external admission systems
- User account management

### 1.3 Definitions, Acronyms, and Abbreviations
- **CS**: Computer Science
- **OUS**: Oregon University System
- **OSU**: Oregon State University
- **ACM**: Association for Computing Machinery
- **IEEE**: Institute of Electrical and Electronics Engineers

### 1.4 References
- OUS Web Design Standards
- Get Real Version 1.0 Documentation
- OUS Performance Standards

### 1.5 Overview
This document is organized into six main sections covering introduction, overall description, system features, external interfaces, non-functional requirements, and other project constraints.

## 2 Overall Description

### 2.1 Product Perspective
The Get Real website is an update to the existing Version 1 system, hosted as a subdomain of OUS (`getreal.ous.edu`). The system runs on OSU servers within the OUS domain to maximize search engine visibility and institutional alignment.

**System Architecture:**
```
[Web Browser] → [OUS Domain] → [OSU Servers] → [Get Real Application]
```

### 2.2 Product Functions
The core functionality includes:
1. Real People professional profiles with video content
2. Career and salary information section
3. Women in Computer Science spotlight features
4. High school course recommendations
5. Internal site search capability
6. Professional organizations directory

### 2.3 User Characteristics
**Primary Users:** Oregon high school students (grades 9-12)

**User Segments:**
1. **CS-Interested Students**: Seeking detailed career information and educational pathways
2. **College-Bound Undecided Students**: Requiring motivation and exposure to CS opportunities

**Key User Traits:**
- Limited attention span for text-heavy content
- Preference for visual and interactive media
- Need for concise, engaging information
- Varied levels of technical understanding

### 2.4 Constraints
- Limited Chancellor's Office development resources
- Bandwidth limitations for video streaming
- Must comply with OUS design and technical standards
- No external system dependencies or integrations

### 2.5 Assumptions and Dependencies
**Assumptions:**
- Target users have access to standard web browsers
- Video content will be optimized for available bandwidth
- OUS infrastructure can support anticipated traffic

**Dependencies:**
- OUS server availability and maintenance
- Compliance with OUS web standards
- Availability of content creation resources

## 3 System Features

### 3.1 Real People Profiles
#### 3.1.1 Description
Feature showcasing video stories from computer science professionals in diverse careers and backgrounds.

#### 3.1.2 Functional Requirements
- **FR-001**: System shall display video profiles of CS professionals
- **FR-002**: Videos shall include transcript or closed captioning options
- **FR-003**: Profile pages shall include professional background information
- **FR-004**: Content shall be categorized by career type and industry
- **FR-005**: Video player shall support standard playback controls

### 3.2 Jobs & Money Section
#### 3.2.1 Description
Comprehensive career information addressing salary expectations and career value propositions.

#### 3.2.2 Functional Requirements
- **FR-006**: System shall present salary range information for CS careers
- **FR-007**: Content shall explain career growth opportunities in CS
- **FR-008**: Information shall be presented in visually engaging formats (infographics, charts)
- **FR-009**: Career paths shall be organized by specialization and education level

### 3.3 Women in Computer Science
#### 3.3.1 Description
Specialized content highlighting women professionals and community involvement opportunities.

#### 3.3.2 Functional Requirements
- **FR-010**: System shall feature profiles of women in CS careers
- **FR-011**: Content shall highlight community and support networks
- **FR-012**: Information shall address common concerns and barriers
- **FR-013**: Shall showcase successful role models and mentors

### 3.4 High School Courses
#### 3.4.1 Description
Recommendations for high school curricula that prepare students for computer science degrees.

#### 3.4.2 Functional Requirements
- **FR-014**: System shall provide course recommendation lists
- **FR-015**: Recommendations shall be organized by grade level (9-12)
- **FR-016**: Shall include prerequisite and preparation guidance
- **FR-017**: Content shall link to OUS program requirements

### 3.5 Internal Search Functionality
#### 3.5.1 Description
Site-specific search capability for locating Get Real content efficiently.

#### 3.5.2 Functional Requirements
- **FR-018**: System shall provide search interface for site content
- **FR-019**: Search results shall be relevance-ranked
- **FR-020**: Search shall support keyword matching across all content types
- **FR-021**: Results shall be filterable by content category

### 3.6 Professional Organizations Directory
#### 3.6.1 Description
Directory of professional organizations and student groups relevant to computer science.

#### 3.6.2 Functional Requirements
- **FR-022**: System shall maintain directory of professional organizations
- **FR-023**: Directory entries shall include contact information and descriptions
- **FR-024**: Organizations shall be categorized (professional, student, special interest)
- **FR-025**: Shall include links to external organization websites

## 4 External Interface Requirements

### 4.1 User Interfaces
- **UI-001**: Website shall be compatible with Internet Explorer
- **UI-002**: Website shall be compatible with Firefox
- **UI-003**: Website shall be compatible with Netscape
- **UI-004**: Design shall follow OUS style conventions and branding
- **UI-005**: Interface shall be optimized for teenage user engagement

### 4.2 Hardware Interfaces
No specific hardware interface requirements beyond standard web server infrastructure.

### 4.3 Software Interfaces
- **SI-001**: Standard web protocols (HTTP/HTTPS)
- **SI-002**: Video streaming compatible with common web formats
- **SI-003**: No integration with external databases or systems

### 4.4 Communication Interfaces
- **CI-001**: Standard internet protocols (TCP/IP)
- **CI-002**: No specialized communication interfaces required

## 5 Non-Functional Requirements

### 5.1 Performance Requirements
- **PER-001**: System response time shall match OUS site performance standards
- **PER-002**: Page load times shall not exceed 3 seconds for standard content
- **PER-003**: Video streaming shall accommodate bandwidth constraints through optimization
- **PER-004**: System shall handle concurrent user load typical for OUS educational sites

### 5.2 Reliability
- **REL-001**: System availability shall match OUS web service standards (99% uptime)
- **REL-002**: Content updates shall not require significant downtime

### 5.3 Usability
- **USA-001**: Interface design shall be teen-friendly and engaging
- **USA-002**: Content shall avoid "walls of text" through visual presentation
- **USA-003**: Navigation shall be intuitive for high school student users
- **USA-004**: Site shall provide clear pathways to key motivational content

### 5.4 Supportability
- **SUP-001**: System shall track user engagement metrics (hits, time spent)
- **SUP-002**: Analytics shall support iterative design improvements
- **SUP-003**: Content management shall accommodate regular updates

### 5.5 Implementation Requirements
- **IMP-001**: Shall be hosted on OSU servers within OUS domain
- **IMP-002**: Shall maintain getreal.ous.edu subdomain
- **IMP-003**: Code and content shall comply with OUS security standards

## 6 Other Requirements

### 6.1 Development Constraints
- Limited Chancellor's Office resources for development and maintenance
- Bandwidth optimization required for video content
- Must utilize existing OUS technical infrastructure

### 6.2 Acceptance Criteria
**Primary Acceptance Metrics:**
- Demonstrated adherence to OUS design standards
- Measurable user engagement improvements over Version 1.0
- Successful tracking of key metrics (time-on-site, repeat visits)

**Success Indicators:**
- Increased student engagement with CS content
- Higher conversion rates to OUS CS program inquiries
- Positive feedback from target user testing

### 6.3 Priority Definitions
- **High Priority**: Teen-friendly design, core content features, engagement tracking
- **Medium Priority**: Advanced search features, detailed analytics
- **Low Priority**: Enhanced video features, additional content categories

### 6.4 Appendices
No appendices at this time.

---

## Document Approval

**Prepared By:** [Name/Title]  
**Reviewed By:** [Name/Title]  
**Approved By:** [Name/Title]  
**Date:** [Date]

**Revision History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial SRS Document |
```