# Software Requirements Specification (SRS)
## WARC Tools Phase III

**Document Version:** 1.0
**Date:** [Date of Generation]
**Project Lead:** Hanzo Archives Limited
**Stakeholders:** International Internet Preservation Consortium (IIPC) Member Institutions

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the WARC Tools Phase III project. The purpose is to define the capabilities, constraints, and interfaces for a suite of tools designed to manage, migrate, and analyze web archive collections in the WARC (Web ARChive) format. This document serves as a reference for developers, testers, project managers, and stakeholders.

#### 1.2 Scope
The project extends an existing open-source toolset to facilitate large-scale migration from the legacy ARC format to WARC and to enhance capabilities for manipulation, validation, and analysis of web archive data. The primary deliverables are five core applications:
1.  A configurable **Migration Application** for ARC-to-WARC conversion.
2.  A **Repackaging Tool** for filtering and extracting WARC records.
3.  A **Reporting Application** for collection analysis.
4.  A **Quality Assurance Tool** for comparing crawl sets.
5.  An enhanced **WARC Browser** with improved access and search.

**Out-of-Scope Items:**
*   Fault tolerance for hardware failures in distributed systems.
*   Custom integration technologies for specific partners.
*   Fundamental architectural changes to the core `libwarc` library.
*   Modification of third-party identification tools (e.g., JHOVE, DROID).
*   Mandatory record-by-record validation for all records in extremely large collections.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ARC:** A legacy format for storing web crawls.
*   **WARC (ISO 28500):** The standard format for storing web archives, an evolution of ARC.
*   **IIPC:** International Internet Preservation Consortium.
*   **SRS:** Software Requirements Specification.
*   **CLI:** Command Line Interface.
*   **MIME-type:** Multipurpose Internet Mail Extensions type, a standard identifier for file formats.

#### 1.4 References
*   ISO 28500:2017, *WARC (Web ARChive) file format*.
*   Project Charter: WARC Tools Phase III Functional Requirements Specification (Provided Input).
*   `libwarc` Library Documentation.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product and its operating environment. Section 3 details the specific functional requirements for each application. Section 4 outlines non-functional requirements. Appendices may include user interface sketches or data flow diagrams.

### 2. Overall Description

#### 2.1 Product Perspective
The WARC Tools Phase III suite is an enhancement of an existing ecosystem of open-source tools. It interfaces with:
*   **Input:** Legacy ARC files, existing WARC files, configuration files.
*   **Output:** New WARC files, reports (text/JSON/HTML), logs, repackaged WARC subsets.
*   **External Systems:** External validation services, virus scanners, format identification tools (e.g., DROID), and existing web service APIs. Integration is configurable and non-invasive.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Primary Goals |
| :--- | :--- | :--- |
| **Web Archivist / Crawl Engineer** | Technically proficient, manages large collections. | Migrate archives, ensure data integrity, validate processes. |
| **Researcher** | May have moderate technical skill, focused on content. | Explore archives, create focused datasets, analyze content. |
| **Quality Assurance Analyst** | Detail-oriented, understands crawl semantics. | Compare crawls, identify anomalies, ensure consistency. |
| **End-User** | Limited technical knowledge of WARC format. | Browse and search archived websites via a simple interface. |
| **System Administrator** | Deploys and maintains tools. | Configure workflows, monitor batch jobs, manage resources. |

#### 2.3 Operating Environment
*   **Software:** Java Runtime Environment (JRE) 8 or later. Tools will be primarily command-line based. The WARC Browser will require a servlet container (e.g., Tomcat, Jetty).
*   **Hardware:** Must operate on standard server and desktop hardware. Tools are designed to process multi-terabyte collections and should be optimized for sequential I/O and memory efficiency.
*   **Network:** Some tools (Browser proxy mode, external service integration) require network access.

#### 2.4 Design and Implementation Constraints
1.  **UNIX Philosophy:** Tools shall be developed as simple, composable, scriptable command-line utilities with a focus on doing one thing well.
2.  **Technology Stack:** Must avoid unnecessary dependencies. Core tools will be Java-based for portability and compatibility with existing `libwarc` and institutional environments.
3.  **Scalability:** Must handle large numbers of files and records without requiring all data to be loaded into memory.
4.  **Configurability:** The migration workflow must be highly configurable via external files to support integration with various institutional pipelines.
5.  **Logging:** All tools must provide configurable logging (e.g., INFO, WARN, ERROR levels) to standard output/error and/or log files.

#### 2.5 Assumptions and Dependencies
*   Input ARC and WARC files are structurally valid according to their respective specifications.
*   Participating IIPC institutions will provide representative test data for development and acceptance testing.
*   The core `libwarc` library provides stable, low-level read/write capabilities.

### 3. System Features and Requirements

#### 3.1 Migration Application
**Objective:** Provide a configurable, monitored workflow to convert ARC collections to WARC format while ensuring data integrity.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-M-01** | The application shall accept as input a list of ARC files and/or directories containing ARC files. | High |
| **FR-M-02** | It shall convert each valid ARC record to a corresponding WARC record, preserving all original payload data. | High |
| **FR-M-03** | The conversion process shall generate and insert appropriate WARC header fields (e.g., `WARC-Type`, `WARC-Record-ID`, `WARC-Date`). | High |
| **FR-M-04** | It shall support a configurable "dry-run" mode that simulates the migration (parsing input, logging actions) without writing output files. | Medium |
| **FR-M-05** | The workflow shall be configurable to execute external tools/services at defined stages (e.g., virus scanning pre-conversion, format identification post-conversion). | High |
| **FR-M-06** | It shall allow for the addition of configurable, institution-specific preservation metadata to WARC records during conversion. | Medium |
| **FR-M-07** | The application shall produce a detailed log file, including counts of records processed, errors encountered, and any validation failures. | High |
| **FR-M-08** | It shall support processing a random sample or a named subset of the input collection for testing and validation purposes. | Medium |

#### 3.2 Repackaging Tool
**Objective:** Enable the creation of new, focused WARC collections from existing ones based on user-defined criteria.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-R-01** | The tool shall accept one or more source WARC files as input. | High |
| **FR-R-02** | It shall filter records based on one or more criteria: URL (regex/pattern), date range, and MIME-type. | High |
| **FR-R-03** | It shall output a new, valid WARC file containing only the records matching the filter criteria. | High |
| **FR-R-04** | The tool shall preserve the original order of records within the new WARC file unless a specific sorting option is selected (e.g., by URL, by date). | Low |
| **FR-R-05** | It shall provide an option to extract records to a flat file directory structure (e.g., for analysis outside the WARC container). | Medium |

#### 3.3 Reporting Application
**Objective:** Generate statistical and analytical summaries of WARC collection content.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-REP-01** | A summary tool shall generate a report from a WARC file or directory. | High |
| **FR-REP-02** | The report shall include, at a minimum: total size, record count, breakdown by WARC record type (response, request, metadata, etc.), and breakdown by top-level MIME-type. | High |
| **FR-REP-03** | The report shall include a list of top hostnames/domains by record count and total bytes. | Medium |
| **FR-REP-04** | The tool shall output reports in human-readable text format and machine-parsable format (e.g., JSON). | Medium |
| **FR-REP-05** | The enhanced WARC Browser shall integrate and visually present this summary data for a loaded collection. | Medium |

#### 3.4 Quality Assurance (QA) Tool
**Objective:** Compare two sets of WARC files from similar crawls to identify significant differences.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-QA-01** | The tool shall accept two sets of WARC files (Set A and Set B) as input. | High |
| **FR-QA-02** | It shall compare the two sets based on a defined key (e.g., URL + capture date). | High |
| **FR-QA-03** | It shall identify and report: records unique to Set A, records unique to Set B, and records present in both. | High |
| **FR-QA-04** | For records present in both sets, it shall optionally perform a checksum comparison of the HTTP response payload to identify changed content. | Medium |
| **FR-QA-05** | The output shall be a clear, structured report (text/JSON) suitable for automated alerting or manual review. | Medium |

#### 3.5 Enhanced WARC Browser
**Objective:** Provide an accessible web interface for browsing and searching WARC collections.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-B-01** | The browser shall allow users to navigate a list of archived URLs within a loaded WARC collection. | High |
| **FR-B-02** | It shall render archived web pages, applying **server-side rewriting** to convert absolute links and embedded resource references to point back to the browser's replay system. | High |
| **FR-B-03** | It shall offer a **proxy mode**, allowing it to act as a proxy for a live browser, serving archived content when available and falling back to the live web for gaps. | Medium |
| **FR-B-04** | It shall integrate a **full-text search** engine (e.g., Apache Lucene) to index and search the textual content of archived HTML pages and other text-based records. | High |
| **FR-B-05** | Search results shall link directly to the archived page replay. | High |
| **FR-B-06** | The browser interface shall be intuitive and require no knowledge of the WARC file structure from the end-user. | Medium |

### 4. Non-Functional Requirements

#### 4.1 Performance
*   **NFR-P-01:** The migration and repackaging tools shall be capable of processing data at a rate limited primarily by sequential I/O speed of the underlying storage system.
*   **NFR-P-02:** Command-line tools shall have minimal memory overhead, processing records in a streaming fashion where possible.
*   **NFR-P-03:** The WARC Browser shall load and render a typical archived HTML page in under 3 seconds for collections indexed locally.

#### 4.2 Scalability
*   **NFR-S-01:** Tools shall be able to process collections consisting of millions of records and terabytes of data.
*   **NFR-S-02:** The migration workflow shall be parallelizable at the file level (e.g., using GNU Parallel or similar).

#### 4.3 Reliability & Availability
*   **NFR-RA-01:** Tools shall be robust against malformed (but not malicious) input records, logging errors and skipping or quarantining the problematic record while continuing processing.
*   **NFR-RA-02:** The WARC Browser service shall be stable under typical institutional user loads.

#### 4.4 Usability
*   **NFR-U-01:** All command-line tools shall provide a `--help` option explaining arguments and usage.
*   **NFR-U-02:** The WARC Browser shall have a clean, simple user interface modeled on standard web search and browsing paradigms.

#### 4.5 Maintainability & Support
*   **NFR-MS-01:** The codebase shall be open-source (Apache 2.0 or similar) and publicly accessible.
*   **NFR-MS-02:** Code shall be well-documented and include unit tests for core functionality.

#### 4.6 Configuration & Integration
*   **NFR-CI-01:** The migration application's workflow shall be defined in an external configuration file (e.g., YAML, XML), not hard-coded.
*   **NFR-CI-02:** Tools shall use standard output/error streams and exit codes to facilitate scripting and integration into larger pipelines.

---
**Appendix A: Open / Undecided Issues**
1.  Contribution specifics from the Swedish National Library (NL).
2.  Final, detailed list of default preservation metadata for migration (linked to FR-M-06).
3.  Quantitative benchmarks for "large-scale" migration performance (linked to NFR-P-01, NFR-S-01).
4.  Detailed design of the "dry-run" simulation mechanism (linked to FR-M-04).
5.  Selection of specific external preservation metadata services/tools for reference configuration (linked to FR-M-05).