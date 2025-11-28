Of course. Below is a comprehensive Software Requirements Specification (SRS) document for the Virtual-ED project, structured according to professional IEEE-style standards and formatted in Markdown.

***

# Software Requirements Specification (SRS) for Virtual-ED

**Version:** 1.0  
**Date:** October 26, 2023  
**Project:** Virtual-ED - Secure Distance Learning Platform  
**Client:** New Jersey Institute of Technology (NJIT)  
**Status:** Draft

---

## Table of Contents

1. [Introduction](#1-introduction)
    1.1 [Purpose](#11-purpose)
    1.2 [Project Scope](#12-project-scope)
    1.3 [Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
    1.4 [References](#14-references)
    1.5 [Overview](#15-overview)
2. [Overall Description](#2-overall-description)
    2.1 [Product Perspective](#21-product-perspective)
    2.2 [Product Functions](#22-product-functions)
    2.3 [User Classes and Characteristics](#23-user-classes-and-characteristics)
    2.4 [Operating Environment](#24-operating-environment)
    2.5 [Design and Implementation Constraints](#25-design-and-implementation-constraints)
    2.6 [Assumptions and Dependencies](#26-assumptions-and-dependencies)
3. [System Features](#3-system-features)
    3.1 [Real-Time Communication Suite](#31-real-time-communication-suite)
    3.2 [Lecture Streaming & Podcasting](#32-lecture-streaming--podcasting)
    3.3 [User Profile Management](#33-user-profile-management)
    3.4 [Virtual-Space File Management](#34-virtual-space-file-management)
    3.5 [Online Examination System](#35-online-examination-system)
    3.6 [Collaborative Whiteboard](#36-collaborative-whiteboard)
4. [External Interface Requirements](#4-external-interface-requirements)
    4.1 [User Interfaces](#41-user-interfaces)
    4.2 [Hardware Interfaces](#42-hardware-interfaces)
    4.3 [Software Interfaces](#43-software-interfaces)
    4.4 [Communications Interfaces](#44-communications-interfaces)
5. [Non-Functional Requirements](#5-non-functional-requirements)
    5.1 [Performance Requirements](#51-performance-requirements)
    5.2 [Safety Requirements](#52-safety-requirements)
    5.3 [Security Requirements](#53-security-requirements)
    5.4 [Software Quality Attributes](#54-software-quality-attributes)
    5.5 [Business Rules](#55-business-rules)

---

## 1 Introduction

### 1.1 Purpose
This document provides a detailed description of the Software Requirements Specification (SRS) for the Virtual-ED platform. It is intended for NJIT stakeholders, project managers, software developers, testers, and end-users (faculty, students, and administrators). This SRS will serve as the foundation for the design, development, testing, and acceptance of the final product.

### 1.2 Project Scope
Virtual-ED is a secure, web-based distance learning platform designed to facilitate real-time communication and collaboration between NJIT students and faculty. The system will provide core functionalities including audio/video streaming, instant messaging, file sharing, customizable user profiles, and a secure online exam system.

**Out-of-Scope:**
*   Replacement of existing institutional email systems.
*   Handling or distribution of non-educational content.
*   Support for non-English documentation.
*   Replacement of existing Learning Management Systems (LMS) like Moodle or Blackboard; Virtual-ED is a supplementary tool.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **Virtual-ED:** The name of the distance learning platform.
*   **NJIT:** New Jersey Institute of Technology.
*   **LMS:** Learning Management System (e.g., Moodle, Blackboard).
*   **FTP:** File Transfer Protocol.
*   **Mbps:** Megabits per second.
*   **UI:** User Interface.
*   **SRS:** Software Requirements Specification.

### 1.4 References
*   NJIT IT Infrastructure Documentation
*   IEEE Std 830-1998 - IEEE Recommended Practice for Software Requirements Specifications

### 1.5 Overview
The remainder of this document describes the overall project requirements in detail. Section 2 provides a general description of the product. Section 3 details the specific system features. Section 4 outlines the external interface requirements. Section 5 specifies the non-functional requirements.

## 2 Overall Description

### 2.1 Product Perspective
Virtual-ED is a self-contained web application that integrates with NJIT's existing infrastructure. It acts as a dedicated real-time collaboration environment, supplementing the asynchronous capabilities of the existing LMS. The system relies on the legacy NJIT user database for authentication and user management.

### 2.2 Product Functions
The core functions of Virtual-ED are:
1.  Real-time, text-based instant messaging (one-to-one and group).
2.  Live and on-demand audio/video streaming for lectures and meetings.
3.  Management of customizable user profiles.
4.  A file management system ("Virtual-Space") for uploading, sharing, and organizing files.
5.  A secure online exam system with timed submissions.
6.  Lecture podcasting (downloadable recordings).
7.  A collaborative whiteboard for real-time document sharing and editing.

### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Administrator** | IT staff with full system privileges. | User management, class setup, system-wide configuration, and maintenance. |
| **Faculty** | Instructors and professors with course-level privileges. | Create/manage classes, host lectures, administer exams, manage course-specific files. |
| **Student** | Enrolled learners with limited privileges. | Attend lectures, participate in chats, submit assignments/exams, view and edit limited profile information. |

### 2.4 Operating Environment
*   **Software:** The application shall be accessible via web browsers (Internet Explorer, Firefox, Safari). It interfaces with Microsoft Office for exam document handling and Real Player for podcast playback.
*   **Hardware:** The system will be hosted on NJIT servers. End-users require a computer with a webcam, microphone, and broadband internet connection.

### 2.5 Design and Implementation Constraints
1.  **User Limit:** The system shall support a maximum of 250 concurrent users, as constrained by the legacy NJIT user database.
2.  **Browser Compatibility:** The user interface shall be designed and tested exclusively for Internet Explorer, Firefox, and Safari.
3.  **Authentication:** User authentication must integrate with the existing NJIT user database.

### 2.6 Assumptions and Dependencies
*   **Assumptions:**
    *   End-users have access to broadband internet meeting the minimum performance requirements.
    *   End-users have a functional webcam and microphone.
*   **Dependencies:**
    *   The project is dependent on the availability and stability of the existing NJIT user database, which may require maintenance or modification.

## 3 System Features

### 3.1 Real-Time Communication Suite
**Description:** This feature provides text-based, real-time communication between users in both one-to-one and group contexts.
**Requirements:**
*   **FR-1.1:** The system shall allow any two users to initiate a private text chat.
*   **FR-1.2:** Faculty and Administrators shall be able to create and moderate group chat channels for their respective classes or system-wide announcements.
*   **FR-1.3:** Chat messages shall be delivered and displayed to recipients in near real-time (< 2 seconds).

### 3.2 Lecture Streaming & Podcasting
**Description:** This feature enables faculty to broadcast live audio/video lectures and to provide on-demand recordings (podcasts).
**Requirements:**
*   **FR-2.1:** The system shall allow faculty to initiate a live audio/video stream to enrolled students.
*   **FR-2.2:** The system shall encode and save live streams for on-demand viewing.
*   **FR-2.3:** The system shall provide downloadable audio/video podcast files in a format compatible with Real Player.

### 3.3 User Profile Management
**Description:** This feature allows users to create and customize their personal profiles.
**Requirements:**
*   **FR-3.1:** All users shall be able to view their own profile and the profiles of others within their classes.
*   **FR-3.2:** All users shall be able to edit basic contact information.
*   **FR-3.3:** Students shall have limited customization options (e.g., background, fonts).
*   **FR-3.4:** Faculty and Administrators shall have advanced customization options, including the ability to upload a video introduction.

### 3.4 Virtual-Space File Management
**Description:** This feature provides a quota-managed storage space for users to upload, organize, and share files.
**Requirements:**
*   **FR-4.1:** The system shall allow users to upload files to their personal Virtual-Space via a web interface or integrated FTP.
*   **FR-4.2:** Faculty shall be able to share files with an entire class or with individual students.
*   **FR-4.3:** The system shall enforce storage quotas per user and per class as defined by the Administrator.
*   **FR-4.4:** All uploaded files shall be scanned by an antivirus service before being made available for download.

### 3.5 Online Examination System
**Description:** This feature provides a secure environment for faculty to administer timed exams, which students complete and submit electronically.
**Requirements:**
*   **FR-5.1:** Faculty shall be able to create an exam, set a time limit, and make it available to a class.
*   **FR-5.2:** The system shall automatically start a timer upon a student opening the exam and enforce submission when the time expires.
*   **FR-5.3:** Exam answers shall be submitted via file upload, with support for Microsoft Office formats.
*   **FR-5.4:** The system shall prevent exam submission after the designated deadline.

### 3.6 Collaborative Whiteboard
**Description:** This feature provides a shared digital whiteboard for real-time collaborative editing of documents during lectures or meetings.
**Requirements:**
*   **FR-6.1:** Faculty shall be able to initiate a shared whiteboard session during a live lecture.
*   **FR-6.2:** All participants in a session shall be able to view changes to the whiteboard in real-time.
*   **FR-6.3:** The system shall allow the faculty member to control editing permissions (e.g., view-only or collaborative editing for students).

## 4 External Interface Requirements

### 4.1 User Interfaces
The system shall present a web-based user interface that is consistent and intuitive. The UI shall be fully functional and tested on the following browsers:
*   Internet Explorer (Version X and above)
*   Firefox (Version Y and above)
*   Safari (Version Z and above)

### 4.2 Hardware Interfaces
The system requires no specific hardware interfaces beyond standard web servers and network infrastructure on the host side.

### 4.3 Software Interfaces
*   **NJIT User Database:** For user authentication and role-based access control.
*   **FTP Server:** For backend file storage and management of the Virtual-Space.
*   **Microsoft Office Suite:** For rendering and processing exam documents.
*   **Real Player:** For playback of downloadable podcast files.

### 4.4 Communications Interfaces
The system shall use standard HTTP/HTTPS protocols for web communication and FTP/SFTP for secure file transfers.

## 5 Non-Functional Requirements

### 5.1 Performance Requirements
*   **Streaming:** The system shall deliver audio/video streams effectively to users with a minimum download speed of 1.5 Mbps.
*   **Concurrency:** The system shall be designed to handle up to 250 concurrent users as per the hard constraint.
*   **Messaging:** Instant messages shall be delivered with a latency of less than 2 seconds.

### 5.2 Safety Requirements
Not applicable for this software system.

### 5.3 Security Requirements
*   **Authentication:** All users must authenticate using their NJIT credentials.
*   **Password Policy:** Passwords must be 8-12 characters long, containing only letters and numbers. Passwords must be changed every 3 months.
*   **Data Integrity:** All file transfers must be scanned by an antivirus service.
*   **Content Responsibility:** Users are responsible for the content they upload and share. The system provides the mechanism but does not police content.

### 5.4 Software Quality Attributes
*   **Availability:** The system shall maintain 99% uptime, excluding scheduled maintenance.
*   **Maintainability:** Scheduled maintenance shall be permitted with a 24-hour notice provided to all users.
*   **Reliability:** The system will make a best-effort attempt to preserve data, but data loss is possible during unexpected system outages. Users are advised to maintain backups of critical files.

### 5.5 Business Rules
*   **User Permissions:**
    *   Students cannot create classes or administer exams.
    *   Faculty can only manage resources for classes they are assigned to.
    *   Only Administrators can create new users or assign system-wide roles.
*   **Feature Priority:** For development and testing purposes, features are prioritized as follows:
    *   **High:** Real-time messaging, online exams, lecture podcasting.
    *   **Medium:** File management, user profiles, collaborative whiteboard.