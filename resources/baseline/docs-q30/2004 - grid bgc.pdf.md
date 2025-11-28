Here is a comprehensive Software Requirements Specification (SRS) document based on the provided information, structured according to professional standards and formatted in Markdown.

# Software Requirements Specification
## Bio-Geochemical Modeling Web Portal

**Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft

---

## 1. Introduction

### 1.1 Purpose
This document provides a detailed description of the Software Requirements Specification (SRS) for the Bio-Geochemical Modeling Web Portal. It specifies the purpose, scope, functional and non-functional requirements, interfaces, and constraints of the system. This SRS is intended for use by the project stakeholders, including developers, testers, project managers, and end-users, to ensure a common understanding of the system to be developed.

### 1.2 Project Scope
The Bio-Geochemical Modeling Web Portal is a web-based system designed to enable scientists to execute bio-geochemical modeling workflows. The core functionality includes running Daymet weather interpolation and BiomeBGC simulations, managing associated input data, organizing work into projects, and handling output results.

**Out-of-Scope (Low Priority):**
*   Direct data publication services.
*   Integrated data visualization tools.
*   Advanced data analysis tools.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **BiomeBGC:** A model used for simulating biogeochemical and hydrologic processes.
*   **Daymet:** A model providing gridded estimates of daily weather parameters.
*   **MSS:** NCAR's Mass Storage System.
*   **NCAR:** National Center for Atmospheric Research.
*   **SRS:** Software Requirements Specification.

### 1.4 References
*   NCAR Security Policy Document
*   Globus Toolkit Documentation
*   NCAR MSS Interface Specifications

## 2. Overall Description

### 2.1 Product Perspective
This system is a new component built upon the existing NCAR grid infrastructure. It is positioned as the primary platform for scientific modeling workflows within NCAR's research ecosystem. The system will integrate seamlessly with two key legacy systems:
*   **NCAR Mass Storage System (MSS):** For all persistent data storage.
*   **NCAR Gatekeeper:** For user authentication and account management.

### 2.2 User Classes and Characteristics
| User Class | Priority | Description & Key Characteristics |
| :--- | :--- | :--- |
| **Scientist** | High (Primary) | Researchers who configure, execute, and manage modeling runs. They create projects, manage input data, and initiate simulations. |
| **Portal Administrator** | Medium (Secondary) | Technical staff responsible for system health, user management, and resource allocation and monitoring. |
| **Data User** | Low | Individuals who only require access to download pre-generated model outputs and results. |

### 2.3 Operating Environment
*   **Server-Side:** NCAR's grid infrastructure. The application logic will be deployed within this environment.
*   **Client-Side:** A standard web browser. Specifically:
    *   Internet Explorer 6.0
    *   Netscape Navigator 7.1
*   **Dependencies:** The system is dependent on the continuous operation and availability of the NCAR MSS and Gatekeeper authentication service.

### 2.4 Design and Implementation Constraints
1.  **Grid Communication:** The system **must** use the Globus toolkit for all grid-based communications.
2.  **Security:** All implementation **must** comply with NCAR Security policies.
3.  **Storage:** All system and user files **must** be stored via the NCAR Mass Storage System (MSS). Local disk storage for persistent data is prohibited.
4.  **Authentication:** User account management **must** be integrated with the NCAR Gatekeeper system.

### 2.5 Assumptions and Dependencies
*   It is assumed that users have valid NCAR Gatekeeper credentials.
*   The system is dependent on the stability and performance of the underlying NCAR grid infrastructure and MSS.
*   Browser cookies are enabled on the client side.

## 3. System Features

This section details the specific functional requirements of the system.

### 3.1 Feature 1: User Authentication and Session Management

**3.1.1 Description**
This feature allows users to securely log in and out of the web portal using their existing NCAR credentials.

**3.1.2 Requirements**
*   **FR-1.1:** The system shall authenticate users against the NCAR Gatekeeper service.
*   **FR-1.2:** The system shall create and manage a user session upon successful authentication using browser cookies.
*   **FR-1.3:** The system shall terminate the user session upon logout.

### 3.2 Feature 2: Project-Based Workflow Management

**3.2.1 Description**
This feature allows Scientists to organize their modeling work into discrete projects. A project logically links all input data, configuration parameters, and output results for one or more simulation runs.

**3.2.2 Requirements**
*   **FR-2.1:** The system shall allow an authenticated Scientist to create, view, update, and delete projects.
*   **FR-2.2:** Each project shall be associated with a unique owner (the creating Scientist).
*   **FR-2.3:** The system shall store all project metadata and file paths in the MSS.

### 3.3 Feature 3: Input Data Management

**3.3.1 Description**
This feature allows Scientists to upload, store, and select input data required for Daymet and BiomeBGC simulations within the context of a project.

**3.3.2 Requirements**
*   **FR-3.1:** The system shall allow a Scientist to upload input data files for a specific project.
*   **FR-3.2:** All uploaded input files shall be transferred and stored directly in the NCAR MSS.
*   **FR-3.3:** The system shall provide a mechanism for the Scientist to select from available input data when configuring a model run.

### 3.4 Feature 4: Model Execution (Daymet & BiomeBGC)

**3.4.1 Description**
This is the core feature that enables Scientists to configure and initiate bio-geochemical modeling runs.

**3.4.2 Requirements**
*   **FR-4.1:** The system shall provide a web interface for configuring a Daymet weather interpolation run.
*   **FR-4.2:** The system shall provide a web interface for configuring a BiomeBGC simulation run.
*   **FR-4.3:** Upon initiation, the system shall use the Globus toolkit to submit the modeling job to the NCAR grid infrastructure.
*   **FR-4.4:** The system shall associate each model run with a specific project.

### 3.5 Feature 5: Output Data and Result Download

**3.5.1 Description**
This feature allows users to access and download the results of completed modeling runs.

**3.5.2 Requirements**
*   **FR-5.1:** The system shall store all model outputs in the NCAR MSS upon run completion.
*   **FR-5.2:** The system shall present a list of available output files for a completed model run to the project owner (Scientist).
*   **FR-5.3:** The system shall allow Data Users with appropriate access (e.g., via a shared link or project permission) to download pre-generated output files.
*   **FR-5.4:** All downloads shall provide the data in its native, model-generated format.

### 3.6 Feature 6: Portal Administration

**3.6.1 Description**
This feature provides Portal Administrators with the tools to monitor and control the system.

**3.6.2 Requirements**
*   **FR-6.1:** The system shall provide an administrative interface accessible only to users with the "Portal Administrator" role.
*   **FR-6.2:** The interface shall allow administrators to view a list of all system users.
*   **FR-6.3:** The interface shall allow administrators to monitor system resource usage (e.g., active jobs, MSS storage metrics).
*   **FR-6.4:** The interface shall provide controls to manage (e.g., pause, cancel) grid jobs for system maintenance.

## 4. External Interface Requirements

### 4.1 User Interfaces
*   The primary user interface shall be a web portal.
*   The portal must be functional and render correctly in the following browsers:
    *   Internet Explorer 6.0
    *   Netscape Navigator 7.1

### 4.2 Hardware Interfaces
*   The system interfaces with the NCAR grid infrastructure hardware for computational processing.
*   The system interfaces with the NCAR Mass Storage System (MSS) hardware for all data storage.

### 4.3 Software Interfaces
*   **NCAR Gatekeeper:** For user authentication (SOAP or other protocol as defined by NCAR).
*   **NCAR Mass Storage System (MSS):** For all file storage operations (using the HPSS or other MSS-specific API).
*   **Globus Toolkit:** For submitting and managing jobs on the grid (using GRAM protocol).

### 4.4 Communications Interfaces
*   All client-server communication will occur over HTTP/HTTPS as per NCAR security policy.
*   Server-to-grid and server-to-MSS communication will use protocols mandated by the respective systems (e.g., GridFTP, GRAM).

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
*   The web portal interface should respond to user actions (e.g., page loads, form submissions) within 3 seconds under normal load.
*   File transfer performance to and from the MSS is dependent on the MSS and network infrastructure and is not a direct requirement of this application.

### 5.2 Security Requirements
*   **SEC-1:** The system must fully comply with all NCAR Security policies.
*   **SEC-2:** All user access must be controlled via NCAR Gatekeeper authentication.
*   **SEC-3:** Users shall only be able to access projects and data they own or have been explicitly granted access to.
*   **SEC-4:** All administrative functions must be protected by role-based access control.

### 5.3 Technical Requirements
*   **TECH-1:** The system must be implemented using the Globus toolkit for all grid communications.
*   **TECH-2:** The system must use the NCAR Mass Storage System (MSS) as the sole repository for all persistent data.
*   **TECH-3:** The client-facing web portal must be compatible with Internet Explorer 6.0 and Netscape 7.1.

## 6. Acceptance Criteria

The system will be considered acceptable upon successful demonstration of the following, in order of priority:

1.  **High Priority (Scientist Needs):**
    *   A Scientist can log in via Gatekeeper, create a project, upload input data to MSS, configure and run a Daymet/BiomeBGC simulation via the Globus toolkit, and download the resulting outputs from MSS.
2.  **Medium Priority (Administrator Needs):**
    *   A Portal Administrator can log in, view system users, and monitor/control active grid jobs.
3.  **Low Priority (Data User Needs):**
    *   A Data User can download a pre-generated output file from a completed model run (with appropriate permissions).

All demonstrations must adhere to the specified constraints, including the use of the Globus toolkit, NCAR MSS for storage, and compliance with NCAR security policies.