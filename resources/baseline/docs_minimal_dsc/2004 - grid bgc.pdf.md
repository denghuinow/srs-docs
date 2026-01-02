# Software Requirements Specification (SRS)
## For the NCAR Bio-Geochemical Modeling Grid Portal

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft  
**Authors:** System Architects, NCAR  
**Stakeholders:** Scientific User Community, NCAR IT, Portal Administrators

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for a grid-based software infrastructure designed to support bio-geochemical modeling. The system will provide a centralized web portal interface for scientists to manage data, execute simulations using the Daymet and Biome-BGC models, and visualize/download results. This document is intended for use by the project managers, developers, testers, and stakeholders involved in the system's design, implementation, and validation.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms "MUST," "MUST NOT," "SHALL," "SHALL NOT," "SHOULD," and "MAY" are used as defined in IETF RFC 2119.
*   **Formatting:** Code, file paths, and system commands are presented in `inline code` blocks.

#### 1.3 Project Scope
The *Bio-Geochemical Modeling Grid Portal* (BMGP) is a web-based application that abstracts the complexity of grid computing and high-performance storage for environmental scientists. It will allow authenticated users to prepare input data, submit jobs to execute the Daymet and Biome-BGC models on remote computational resources, manage the resulting data objects within a project context, and visualize or download output.

**In-Scope:**
*   A secure web portal for user interaction.
*   Integration with the Globus Toolkit for grid job submission and data transfer.
*   Management of user projects, input files, and output files stored on the NCAR Mass Storage System (MSS).
*   Execution workflows for the two specified models (Daymet, Biome-BGC).
*   Basic visualization of standard model output (e.g., time series, spatial plots).
*   User and project administration functions.

**Out-of-Scope:**
*   Development or modification of the core Daymet or Biome-BGC model codes.
*   Provisioning of computational resources (assumed to be available via the grid).
*   Advanced data analysis or machine learning capabilities.
*   Mobile application interface.

#### 1.4 References
*   Globus Toolkit Documentation
*   NCAR Security Policy Manual
*   NCAR Mass Storage System (MSS) User Guide
*   Daymet Model Documentation
*   Biome-BGC Model Documentation

### 2. Overall Description

#### 2.1 Product Perspective
The BMGP is a new, self-contained system that will integrate with existing NCAR cyberinfrastructure. It acts as a middleware layer between the scientist user and the underlying grid resources (computational clusters, the MSS).

**System Interfaces:**
*   **Globus Toolkit:** For GRAM job submission and GridFTP data transfers.
*   **NCAR MSS:** The primary repository for all persistent input and output data.
*   **NCAR Gatekeeper/LDAP:** For user authentication and authorization.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Requirements |
| :--- | :--- | :--- |
| **Scientist (Primary)** | Domain experts in ecology, biogeochemistry, climatology. Comfortable with model concepts but seeks to avoid command-line grid complexity. May have limited computational experience. | Intuitive project/data management, reliable job submission, clear status feedback, easy data retrieval and visualization. |
| **Portal Administrator** | NCAR IT staff or designated power users. Responsible for user management, system monitoring, and troubleshooting. | Tools for managing user accounts and projects, viewing system logs, managing job queues, and resolving issues. |

#### 2.3 Operating Environment
*   **Software:** The portal will be deployed on an NCAR-approved web server (e.g., Apache Tomcat). It will utilize the Globus Toolkit client libraries and MSS client libraries.
*   **Hardware:** Standard NCAR web server hardware. Underlying grid resources (computational clusters, MSS) are pre-existing.
*   **Network:** Operate within the NCAR secure network, accessible via HTTPS.

#### 2.4 Design and Implementation Constraints
1.  **`CON-001`:** The system MUST be built using the Globus Toolkit for all grid interactions (job management, data transfer).
2.  **`CON-002`:** The system MUST comply with all applicable NCAR security policies for web applications and data access.
3.  **`CON-003`:** All user project data, input files, and output files MUST be stored on the NCAR Mass Storage System (MSS). Local server disk space shall only be used for temporary caching.
4.  **`CON-004`:** Access to the portal MUST require a valid, active NCAR Gatekeeper (or equivalent centralized) account.

#### 2.5 Assumptions and Dependencies
*   Assumes the underlying Daymet and Biome-BGC executables are pre-installed and configured on target grid resources.
*   Assumes users have a basic understanding of the input parameters required for their chosen model.
*   Dependent on the continued availability and support of the Globus Toolkit and NCAR MSS.

### 3. System Features and Requirements

#### 3.1 User Authentication and Authorization
*   **`FR-010`:** The system SHALL present a login page requiring NCAR Gatekeeper credentials.
*   **`FR-011`:** Upon successful authentication, the system SHALL create a user session and present a personalized dashboard.
*   **`FR-012`:** The system SHALL allow authorized Administrators to enable/disable user accounts and assign user roles (Scientist, Admin).

#### 3.2 Project and Data Management
*   **`FR-020`:** A user SHALL be able to create, view, rename, and delete projects. A project is a container for related model runs and data.
*   **`FR-021`:** Within a project, a user SHALL be able to upload input files (via browser or GridFTP reference) to the MSS.
*   **`FR-022`:** The system SHALL maintain a catalog of data objects (input/config files, output files) associated with each project, displaying metadata (name, size, type, creation date).
*   **`FR-023`:** A user SHALL be able to organize data objects within a project using a folder-like structure (virtual organization mapped to MSS paths).

#### 3.3 Model Execution (Daymet & Biome-BGC)
*   **`FR-030`:** The system SHALL provide distinct, guided interfaces for configuring a Daymet run and a Biome-BGC run.
*   **`FR-031`:** Each interface SHALL allow the user to select input files from their project space on the MSS and set model-specific parameters via a web form.
*   **`FR-032`:** Upon submission, the system SHALL use the Globus GRAM service to submit the job to a pre-configured grid resource.
*   **`FR-033`:** The system SHALL store the job submission parameters and a unique job identifier persistently.
*   **`FR-034`:** The system SHALL provide a "Job Status" page that polls the grid resource (via Globus) and displays the current state (Pending, Running, Completed, Failed) of each submitted job.
*   **`FR-035`:** Upon job completion, the system SHALL automatically stage standard output files from the compute resource to the user's designated location within their project space on the MSS.

#### 3.4 Output Visualization and Download
*   **`FR-040`:** For completed jobs, the system SHALL list output files in the project data catalog with visual indicators (e.g., icons for NetCDF, text files).
*   **`FR-041`:** The system SHALL provide a "Download" action for any file, initiating a secure transfer from the MSS to the user's local machine.
*   **`FR-042`:** For common, standardized output formats (e.g., time series NetCDF), the system SHALL provide basic visualization capabilities (e.g., generate summary plots via a backend service) directly within the web portal.

#### 3.5 Administrative Functions
*   **`FR-050`:** Administrators SHALL have a dedicated interface to view all system users and projects.
*   **`FR-051`:** Administrators SHALL be able to view a log of all job submissions and system events.
*   **`FR-052`:** Administrators SHALL be able to terminate or requeue stalled grid jobs on behalf of users.

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **`NFR-101`:** The portal dashboard SHALL load within 3 seconds for 95% of user requests under typical load (≤ 50 concurrent users).
*   **`NFR-102`:** Job status updates (polling) SHALL occur with a maximum latency of 30 seconds from the actual state change on the grid.

#### 4.2 Security Requirements
*   **`NFR-201`:** All communication between the user's browser and the portal SHALL be encrypted using TLS 1.2 or higher.
*   **`NFR-202`:** User credentials SHALL never be stored in plaintext. Authentication SHALL be performed against the central NCAR Gatekeeper.
*   **`NFR-203`:** The system SHALL enforce strict access controls, ensuring a user can only view and manipulate their own projects and data, unless explicitly granted shared access.
*   **`NFR-204`:** All file paths and job identifiers stored by the system SHALL be validated to prevent path traversal attacks.

#### 4.3 Reliability and Availability
*   **`NFR-301`:** The web portal application SHALL have an uptime availability of 99.5% during core business hours (8 AM - 6 PM MT).
*   **`NFR-302`:** Job submission metadata (parameters, status) SHALL be persisted such that no more than 1% of job records are lost in the event of an application server restart.

#### 4.4 Usability
*   **`NFR-401`:** The user interface for configuring a model run SHALL be usable by a scientist familiar with the model with less than 30 minutes of training.
*   **`NFR-402`:** The system SHALL provide clear, non-technical error messages for common failures (e.g., "Invalid input file format," "Grid resource unavailable").

### 5. Appendices

#### 5.1 Data Definitions
*   **Project:** A user-defined collection of model runs and associated data files. Stored as metadata in the portal database with pointers to MSS storage locations.
*   **Job:** A single instance of a model execution. Contains configuration, status, and pointers to input/output data objects.

#### 5.2 Acronyms and Abbreviations
*   **BGC:** Bio-GeoChemical
*   **GRAM:** Globus Resource Allocation Manager
*   **MSS:** Mass Storage System
*   **NCAR:** National Center for Atmospheric Research
*   **SRS:** Software Requirements Specification

---
*Document End*