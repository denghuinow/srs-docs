Of course. Below is a comprehensive Software Requirements Specification (SRS) document for the described project, following professional standards and structured with markdown formatting.

***

# Software Requirements Specification
## Moodle Enhancement for University of Puget Sound

**Version:** 1.0
**Date:** October 26, 2023
**Author:** [Your Name/Department]
**Status:** Draft

---

### Table of Contents
1. [Introduction](#1-introduction)
    1.1 [Purpose](#11-purpose)
    1.2 [Project Scope](#12-project-scope)
    1.3 [Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
    1.4 [References](#14-references)
    1.5 [Overview](#15-overview)
2. [Overall Description](#2-overall-description)
    2.1 [Product Perspective](#21-product-perspective)
    2.2 [Product Functions](#22-product-functions)
    2.3 [User Characteristics](#23-user-characteristics)
    2.4 [Constraints](#24-constraints)
    2.5 [Assumptions and Dependencies](#25-assumptions-and-dependencies)
3. [System Features](#3-system-features)
    3.1 [Per-Page Multiple File Upload Configuration](#31-per-page-multiple-file-upload-configuration)
    3.2 [Voice Clip Portfolio for Language Courses](#32-voice-clip-portfolio-for-language-courses)
    3.3 [Per-Page Web Feed Toggle](#33-per-page-web-feed-toggle)
    3.4 [Advanced Assignment Grading](#34-advanced-assignment-grading)
4. [Non-Functional Requirements](#4-non-functional-requirements)
    4.1 [Performance Requirements](#41-performance-requirements)
    4.2 [Availability Requirements](#42-availability-requirements)
    4.3 [Technical Constraints](#43-technical-constraints)

---

## 1. Introduction

### 1.1 Purpose
This document describes the functional and non-functional requirements for the enhancement of the University of Puget Sound's courseware system. The project aims to replace existing Blackboard functionality with a customized, Moodle-based solution. This SRS will serve as a agreement between the development team and the stakeholders and will be the basis for system design, implementation, and testing.

### 1.2 Project Scope
The scope of this project is to develop and integrate specific enhancements into a core Moodle installation. These enhancements are designed to meet the unique pedagogical needs of the University, focusing on file management, content presentation, language learning, and assignment grading. The project is explicitly *not* a from-scratch development but an augmentation of the existing Moodle platform.

### 1.3 Definitions, Acronyms, and Abbreviations
- **SRS**: Software Requirements Specification
- **MVP**: Minimum Viable Product
- **Moodle**: A open-source Learning Management System (LMS)
- **LMS**: Learning Management System
- **API**: Application Programming Interface
- **Actor**: A user interacting with the system (e.g., Student, Instructor, Administrator).
- **Course Administrator**: A user role with permissions to manage and grade assignments within a specific course (typically an Instructor or Teaching Assistant).

### 1.4 References
- Moodle Official Documentation: [https://docs.moodle.org/](https://docs.moodle.org/)
- Moodle Plugin Development Guide: [https://docs.moodle.org/dev/Guide](https://docs.moodle.org/dev/Guide)

### 1.5 Overview
The remainder of this document details the overall description of the system, specific features, and non-functional requirements.

## 2. Overall Description

### 2.1 Product Perspective
This product is a set of custom modules and plugins for a standard Moodle LMS installation. It will integrate seamlessly with the core Moodle system, leveraging its existing user authentication, course management, and role-based access control systems.

### 2.2 Product Functions
The high-level functions of the system enhancements are:
1. To provide granular control over file upload interfaces on course pages.
2. To offer a dedicated portfolio tool for organizing and reviewing audio submissions, specifically for language courses.
3. To allow fine-grained management of web feed (RSS) visibility.
4. To enhance the assignment grading interface with point ratio calculations and integrated feedback.

### 2.3 User Characteristics
- **Students**: Primary users who will upload files, create voice clips, and view grades.
- **Instructors/Course Administrators**: Users who configure page settings, manage student portfolios, and grade assignments.
- **System Administrators**: Technical staff responsible for installing, configuring, and maintaining the Moodle instance and its plugins.

### 2.4 Constraints
1. **Technical Constraint**: All enhancements must be developed using existing Moodle APIs and follow standard Moodle plugin architecture. Customizations must not modify the core Moodle code.
2. **Performance Constraint**: The system must support a minimum of 1000 concurrent users without significant performance degradation.
3. **Operational Constraint**: The system should maintain 99% uptime, available 24/7.

### 2.5 Assumptions and Dependencies
- **Assumption**: The University of Puget Sound has or will procure adequate server hardware and network infrastructure to host the Moodle instance.
- **Dependency**: The project is dependent on the stability and continued development of the upstream Moodle project.
- **Dependency**: Development assumes the use of a supported version of Moodle (e.g., 4.x).

## 3. System Features

### 3.1 Per-Page Multiple File Upload Configuration
**3.1.1 Description**
This feature allows a Course Administrator to enable or disable the ability for users to upload multiple files simultaneously on a per-page basis within a course.

**3.1.2 Functional Requirements**
- **FR-1.1**: The system shall provide a configuration setting within the page editing interface for "Multiple File Uploads."
- **FR-1.2**: The setting shall be a binary toggle (Enabled/Disabled).
- **FR-1.3**: When enabled, the file upload interface on that specific page shall present an option to select and upload multiple files at once.
- **FR-1.4**: When disabled, the file upload interface shall only allow for the selection of a single file.

### 3.2 Voice Clip Portfolio for Language Courses
**3.2.1 Description**
This feature provides a dedicated "Portfolio" area where students in language courses can upload, manage, and review their voice clip submissions. Course Administrators can view and access student portfolios.

**3.2.2 Functional Requirements**
- **FR-2.1**: The system shall provide a "Language Portfolio" block or activity that can be added to a course.
- **FR-2.2**: Students shall be able to upload audio files (voice clips) to their personal portfolio within the course.
- **FR-2.3**: Students shall be able to delete or re-record voice clips within their portfolio.
- **FR-2.4**: The portfolio shall display voice clips in a list or grid view, showing metadata such as date created and title.
- **FR-2.5**: A Course Administrator shall be able to view the portfolio of any student enrolled in their language course.

### 3.3 Per-Page Web Feed Toggle
**3.3.1 Description**
This feature allows a Course Administrator to control the visibility of web feeds (RSS) on a per-page basis.

**3.3.2 Functional Requirements**
- **FR-3.1**: The system shall provide a configuration setting within the page editing interface for "Display Web Feed."
- **FR-3.2**: The setting shall be a binary toggle (On/Off).
- **FR-3.3**: When toggled "On," any configured web feed for that page shall be visible to users with appropriate permissions.
- **FR-3.4**: When toggled "Off," the web feed shall be hidden from all users on that page.

### 3.4 Advanced Assignment Grading
**3.4.1 Description**
This feature enhances the standard Moodle assignment grading interface to allow Course Administrators to grade using point ratios and provide inline feedback.

**3.4.2 Functional Requirements**
- **FR-4.1**: In the grading interface, the system shall display the assignment's total possible points.
- **FR-4.2**: The Course Administrator shall be able to enter a grade as a ratio (e.g., `45/50`).
- **FR-4.3**: The system shall automatically calculate the corresponding percentage and absolute score based on the entered ratio.
- **FR-4.4**: The grading interface shall include a dedicated, persistent text field for entering qualitative feedback for the student.
- **FR-4.5**: The calculated grade and feedback shall be saved and made visible to the student upon submission.

## 4. Non-Functional Requirements

### 4.1 Performance Requirements
- **PER-1**: The system, with all enhancements, shall support a minimum of **1000 concurrent users** performing typical operations (browsing, uploading, grading).
- **PER-2**: Page load times for all enhanced features shall be under 3 seconds under normal load (500 concurrent users).

### 4.2 Availability Requirements
- **AVAIL-1**: The overall system shall be available 24 hours a day, 7 days a week.
- **AVAIL-2**: The system shall maintain a **99% uptime** excluding scheduled maintenance windows. Scheduled maintenance shall be communicated at least 48 hours in advance.

### 4.3 Technical Constraints
- **TECH-1**: All custom code for the enhancements described in Section 3 must be implemented as Moodle plugins (e.g., activity modules, blocks, local plugins) and utilize official, stable Moodle APIs.
- **TECH-2**: The plugins must be compatible with the University's specified version of Moodle and PHP.

---
***End of Document***