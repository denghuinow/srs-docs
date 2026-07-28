# Software Requirements Specification (SRS)
## WARC Tools Project - Phase III

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft for Review  
**Project:** WARC Tools - Phase III  
**Prepared for:** International Internet Preservation Consortium (IIPC) Member Institutions  
**Prepared by:** [Your Organization/Team Name]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the third phase of the WARC Tools project. The primary purpose of this phase is to facilitate the adoption of the WARC (Web ARChive) file format by providing a comprehensive suite of tools for migrating, validating, repackaging, reporting on, and comparing web archive files. This document is intended for use by the development team, project stakeholders, and testing personnel within the IIPC community.

#### 1.2 Scope
The system encompasses a suite of command-line and web-based tools built upon the existing `libwarc` library. The in-scope functionality includes:
*   Migration of ARC file collections to the WARC format.
*   Validation and quality assurance of migrated content.
*   Repackaging and filtering of WARC files.
*   Reporting and comparative analysis of WARC collections.
*   Enhanced browsing of WARC file contents.

**Out of Scope:**
*   Functionality for handling hardware failures.
*   Development of partner-specific integration technologies.
*   Core development of the `libwarc` library (assumed as a stable dependency).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ARC:** A legacy file format for storing web crawls.
*   **WARC:** Web ARChive file format, an ISO standard (ISO 28500) for storing web archival data.
*   **IIPC:** International Internet Preservation Consortium.
*   **CLI:** Command-Line Interface.
*   **GUI:** Graphical User Interface.
*   **MIME-type:** Multipurpose Internet Mail Extensions type, a standard identifier for file formats.
*   **PID:** Persistent Identifier.
*   **QA:** Quality Assurance.

#### 1.4 References
1.  ISO 28500:2017 - WARC file format specification.
2.  ARC File Format Specification (Internet Archive).
3.  Phase I & II SRS and Technical Documentation for `libwarc` and foundational tools.
4.  IIPC Member Institution Requirement Documents.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, scalability, and design constraints.

### 2. Overall Description

#### 2.1 Product Perspective
This project is the third phase of the WARC Tools ecosystem. It is a dependent system that builds upon the existing open-source `libwarc` library and command-line tools developed in Phases I and II. The tools act as middleware, processing archival data and potentially interfacing with external systems for services like virus scanning (e.g., ClamAV), file identification (e.g., DROID, Siegfried), and PID generation (e.g., Handle, DOI services).

#### 2.2 Product Functions
The core suite of tools will provide the following high-level functions:
1.  **ARC-to-WARC Migration:** Convert large collections of legacy ARC files into standardized WARC files.
2.  **Validation & QA:** Verify the integrity and correctness of migrated WARC files against original ARC sources.
3.  **Repackaging:** Create new, subsetted WARC files by filtering records based on user-defined criteria.
4.  **Reporting:** Generate statistical and descriptive summaries of WARC file collections.
5.  **Comparison:** Analyze and report differences between two WARC collections.
6.  **Enhanced Browsing:** Provide a web-based interface for exploring the contents of WARC files beyond basic replay.

#### 2.3 User Characteristics
| User Class | Description | Key Skills & Knowledge |
| :--- | :--- | :--- |
| **Crawl Engineer** | Technical staff responsible for operating web crawlers and managing archival data pipelines. | Advanced CLI proficiency, understanding of web crawling technologies, ARC/WARC formats, and filesystem management. |
| **Web Archivist** | Professional responsible for curating, managing, and providing access to web archives. | Strong understanding of archival principles, metadata, WARC format, and basic CLI skills. |
| **Researcher** | Academic or analyst studying archived web content. | Variable technical skill; may rely more on GUI tools and generated reports. |

*Note: The system does not define distinct internal roles or permission levels. Access control is assumed to be managed at the operating system or network level.*

#### 2.4 Operating Environment
*   **Software:** Must run on standard Linux distributions commonly used in heritage institutions (e.g., Ubuntu LTS, RHEL/CentOS). Compatibility with the existing `libwarc` library is mandatory.
*   **Hardware:** Must be deployable on institutional servers and scale to cluster/distributed environments for processing large collections.
*   **Network:** Tools may require network access to integrate with external identification and PID services.

#### 2.5 Design and Implementation Constraints
1.  **Technology Stack:** Must extend the existing `libwarc` (C/C++) codebase. New components should avoid introducing unnecessary technology dependencies.
2.  **IIPC Collaboration:** Requirements are derived from and validated by specified IIPC member institutions.
3.  **Fixed Scope:** The requirements outlined herein define a fixed scope. New institutional requirements requiring significant effort must be formally de-scoped or pursued under separate funding.
4.  **Metadata:** Default metadata requirements for migration will be supplied by IIPC members.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** The underlying `libwarc` library from Phases I/II is stable, performant, and provides the necessary low-level APIs.
*   **Assumption:** IIPC institutions will provide representative ARC collections and real-world environments for testing.
*   **Dependency:** Successful integration may depend on the availability and API stability of external services (virus scanning, format identification).

### 3. Specific Requirements

#### 3.1 External Interface Requirements
##### 3.1.1 User Interfaces
*   **Primary CLI:** All core tools (migrate, validate, repackage, report, compare) shall offer a comprehensive command-line interface with consistent argument patterns, help text, and exit codes.
*   **Migration Web UI:** A web-based interface shall be provided to configure migration jobs (source/target paths, metadata templates, filters) and monitor their progress.
*   **Monitoring Console:** A web-based dashboard shall display system status, active job queues, and historical logs for processing tasks.
*   **Enhanced Browser:** A web application shall allow users to upload or point to a WARC file, list its records, and inspect record headers and content.

##### 3.1.2 Hardware Interfaces
None specified beyond standard server hardware.

##### 3.1.3 Software Interfaces
*   **`libwarc` Library:** The tools shall link against and use the APIs provided by the existing `libwarc` library.
*   **External Service APIs:** The system shall be capable of interfacing with:
    *   Virus scanning daemons/APIs.
    *   File format identification tools (CLI or API).
    *   Persistent Identifier minting services.

##### 3.1.4 Communications Interfaces
Communication will occur via standard system calls (for CLI), HTTP/HTTPS (for web UIs and external service integration), and potentially network sockets for distributed processing nodes.

#### 3.2 Functional Requirements
##### 3.2.1 Migration Tool (`warc-migrate`)
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-MIG-01** | The tool shall accept a list of input ARC files, specified by direct path, wildcard pattern, or from a manifest file. | High |
| **FR-MIG-02** | The tool shall convert each valid ARC record into a corresponding compliant WARC record. | High |
| **FR-MIG-03** | The tool shall apply default IIPC-provided metadata profiles during migration, with options for customization. | High |
| **FR-MIG-04** | The tool shall support an optional pre-migration batch deduplication process to identify and handle duplicate records. | Medium |
| **FR-MIG-05** | The tool shall generate output WARC files based on configurable criteria (e.g., max file size, max records per file). | High |
| **FR-MIG-06** | The tool shall create a detailed manifest/log linking source ARC files and records to output WARC files and records. | High |
| **FR-MIG-07** | The tool shall be capable of processing millions of ARC files by supporting distributed, parallel execution across a cluster. | High |

##### 3.2.2 Validation & QA Tool (`warc-validate`)
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-VAL-01** | The tool shall validate the syntactic correctness of WARC files (structure, headers). | High |
| **FR-VAL-02** | The tool shall compare a migrated WARC file against its original ARC source to verify content fidelity (byte-for-byte payload match). | High |
| **FR-VAL-03** | The tool shall produce a validation report indicating success/failure and detailing any discrepancies found. | High |

##### 3.2.3 Repackaging Tool (`warc-filter`)
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-REP-01** | The tool shall create a new WARC file containing a subset of records from one or more input WARC files. | High |
| **FR-REP-02** | The tool shall filter records based on criteria including: URL (regex patterns), MIME-type, date-time range, and record type (response, request, metadata, etc.). | High |
| **FR-REP-03** | The tool shall preserve all original WARC headers and payloads for selected records in the output file. | High |

##### 3.2.4 Reporting Tool (`warc-report`)
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-REP-01** | The tool shall analyze one or more WARC files and generate a summary report. | High |
| **FR-REP-02** | The report shall include statistics such as: total records per type, MIME-type distribution, top-level domain breakdown, date range, and total compressed/uncompressed size. | High |
| **FR-REP-03** | The tool shall output reports in human-readable (e.g., plain text, HTML) and machine-readable (e.g., JSON, XML) formats. | Medium |

##### 3.2.5 Comparison Tool (`warc-diff`)
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-CMP-01** | The tool shall compare the record inventories of two WARC file collections. | High |
| **FR-CMP-02** | The tool shall identify records unique to each collection and records common to both. | High |
| **FR-CMP-03** | The tool shall report differences at the collection level (e.g., counts, sizes) and provide optional detailed manifests of unique/common records. | Medium |

##### 3.2.6 Enhanced WARC Browser (`warc-browser`)
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-BRW-01** | The web application shall allow a user to select a WARC file from the local server filesystem. | High |
| **FR-BRW-02** | The application shall parse and display a paginated list of all records within the file, showing key headers (WARC-Type, URI, Date). | High |
| **FR-BRW-03** | The user shall be able to select any record to view its full WARC headers and a rendered or hex view of its HTTP payload. | High |
| **FR-BRW-04** | The browser shall provide basic navigation between linked records (e.g., from a response to its corresponding request). | Medium |

#### 3.3 Non-Functional Requirements
##### 3.3.1 Performance Requirements
| ID | Requirement |
| :--- | :--- |
| **NFR-PER-01** | The migration tool must be capable of processing multiple files simultaneously. The degree of parallelism must be configurable. |
| **NFR-PER-02** | All tools must support input selection via wildcard patterns, file size thresholds, and record count limits to facilitate batch operations. |
| **NFR-PER-03** | The migration application must be designed to handle collections comprising millions of ARC files without degradation due to memory constraints. |

##### 3.3.2 Scalability Requirements
| ID | Requirement |
| :--- | :--- |
| **NFR-SCA-01** | The architecture of core processing tools (especially migration and validation) must support distributed processing across a cluster of machines to scale with collection size. |

##### 3.3.3 Reliability & Logging
| ID | Requirement |
| :--- | :--- |
| **NFR-REL-01** | All tools must provide configurable logging facilities (e.g., syslog, file-based) with adjustable log levels (ERROR, WARN, INFO, DEBUG). |
| **NFR-REL-02** | Logs must capture sufficient detail to audit tool execution, diagnose failures, and verify processing outcomes. |

##### 3.3.4 Design Requirements
| ID | Requirement |
| :--- | :--- |
| **NFR-DES-01** | Implementation must avoid introducing unnecessary technology, library, or framework dependencies beyond the core `libwarc` dependency and essential external service clients. |
| **NFR-DES-02** | CLI tools must follow consistent naming conventions, argument structures, and help text formats. |

### 4. Acceptance Approach
The final toolset will be considered accepted upon successful completion of the following:
1.  **Functional Verification:** All requirements marked "High" priority pass unit and integration tests.
2.  **Deployment Testing:** The complete suite is deployed and operated in the real-world archival environments of at least three participating IIPC member institutions.
3.  **Real-World Validation:** Institutions confirm that the tools perform their intended tasks (migration, validation, repackaging, etc.) effectively on their own archival collections.
4.  **Performance Benchmarking:** The migration tool demonstrates the ability to process a representative large-scale collection (as defined by the IIPC) within an acceptable timeframe, utilizing its distributed capabilities if configured.

---
*This document is considered a living artifact and may be updated following formal change control procedures in collaboration with IIPC stakeholders.*