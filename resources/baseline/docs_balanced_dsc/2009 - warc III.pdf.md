# Software Requirements Specification (SRS)
## WARC Tools Phase III
### Version 1.0

**Document Status:** Draft  
**Prepared For:** International Internet Preservation Consortium (IIPC)  
**Prepared By:** Hanzo Archives Limited  
**Date:** [Current Date]

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the WARC Tools Phase III project. The purpose is to provide a complete description of the system to be developed, serving as a basis for agreement between the stakeholders and the development team. This document is intended for project managers, developers, testers, and the sponsoring IIPC member institutions.

### 1.2 Scope
The WARC Tools Phase III project extends the existing open-source toolkit for manipulating Web ARChive (WARC) files. The primary deliverables are:

1.  A comprehensive **Migration Application** for converting legacy ARC files to the WARC format.
2.  A suite of **Utility Tools** for repackaging, reporting, and quality assurance of WARC collections.
3.  An **Enhanced WARC Browser** with improved access and search capabilities.

The project builds upon the foundational `libwarc` library and tools from prior phases. The scope excludes the development of core archival crawlers or long-term digital preservation systems, focusing instead on post-crawl processing and access tooling.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **ARC:** A legacy file format for storing web crawls.
*   **WARC (ISO 28500):** The standard file format for web archives, succeeding ARC.
*   **IIPC:** International Internet Preservation Consortium.
*   **BnF:** Bibliothèque nationale de France.
*   **BL:** The British Library.
*   **QA:** Quality Assurance.
*   **CLI:** Command-Line Interface.
*   **API:** Application Programming Interface.
*   **URI:** Uniform Resource Identifier.

### 1.4 References
*   ISO 28500:2017, *WARC file format*.
*   IIPC WARC Tools Phase II Documentation.
*   Project Charter: Balanced Summary for WARC Tools Phase III.

### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2** provides a general description of the product, its user classes, and operating environment.
*   **Section 3** lists specific functional requirements organized by system feature.
*   **Section 4** details non-functional requirements including performance, usability, and design constraints.
*   **Appendices** contain supplementary information.

## 2. Overall Description

### 2.1 Product Perspective
This project is a major enhancement to the existing WARC Tools ecosystem. It is a standalone suite of tools that can interoperate with existing web archiving workflows. The system will consume ARC/WARC files as input and produce WARC files, reports, and validation logs as output.

### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Web Archivist / Collection Manager** | Manages large-scale web archives. Technical but not necessarily a software developer. | Migrate collections, generate reports, ensure compliance and integrity. |
| **Crawl Engineer** | Highly technical, operates crawlers and processing pipelines. | Validate data integrity, repackage collections, perform QA comparisons. |
| **Researcher** | Uses archives for analysis. May have limited technical expertise in archive formats. | Easily browse, search, and extract specific subsets of archived content. |
| **System Administrator** | Deploys and maintains software in institutional environments. | Requires scriptable tools, clear logging, and manageable resource usage. |
| **IIPC & Institutional Stakeholders** | Sponsors and advisors. Define strategic requirements and provide test data. | Ensure tools meet community needs and support large-scale, real-world operations. |

### 2.3 Operating Environment
*   **Software:** Must run on standard Java Virtual Machine (JVM) environments (version 8 or later). Tools should be deployable on Linux-based servers. Web-based components (browser, configuration UI) should be accessible via modern web browsers.
*   **Hardware:** Must be capable of operating on systems processing multi-terabyte archive collections. No specific hardware architecture is mandated, but tools must be efficient in I/O-bound scenarios.
*   **External Systems:** May integrate with external tools for virus scanning (e.g., ClamAV) and format identification (e.g., JHOVE, DROID). Integration must be configurable and not create hard dependencies.

### 2.4 Design and Implementation Constraints
1.  **UNIX Philosophy:** Tools should follow the UNIX philosophy: do one thing well, work with text streams, and be composable.
2.  **Open Source:** All deliverables will be released under an open-source license.
3.  **Backward Compatibility:** New tools must not break existing `libwarc` API compatibility without deprecation cycles.
4.  **Technology Neutrality:** Avoid dependencies on specific partner infrastructures or complex frameworks (e.g., Hadoop) unless absolutely necessary for core requirements.

### 2.5 Assumptions and Dependencies
*   **Assumption:** Participating IIPC institutions (BnF, BL, etc.) will provide representative ARC files for testing and validation.
*   **Dependency:** Requirements and priorities may be refined based on ongoing collaboration with IIPC members.
*   **Assumption:** The underlying `libwarc` library is stable and provides the necessary low-level read/write capabilities.

## 3. System Features and Requirements

### 3.1 Migration Application
This feature encompasses the end-to-end workflow for converting collections from the legacy ARC format to the standard WARC format.

#### 3.1.1 Migration Configuration (FR-01)
**Description:** The system shall provide a mechanism to define and persist migration job configurations.
**Requirements:**
*   **FR-01.1:** Configuration shall be definable via a human-editable file (e.g., YAML, JSON, XML) and/or a web-based user interface.
*   **FR-01.2:** Configuration shall specify source ARC file locations, target WARC output directory, and metadata application rules.
*   **FR-01.3:** Configuration shall support the definition of default WARC metadata fields (e.g., `WARC-Concurrent-To`, `WARC-IP-Address`) to be populated during migration, as determined by IIPC input.
*   **FR-01.4:** Configuration shall allow for "dry-run" simulation to preview migration actions without writing files.

#### 3.1.2 ARC to WARC Conversion Tool (FR-02)
**Description:** The core tool shall read ARC files and write semantically equivalent WARC files.
**Requirements:**
*   **FR-02.1:** The tool shall process ARC records and convert them to appropriate WARC record types (`response`, `resource`, `request`, etc.).
*   **FR-02.2:** The tool shall preserve the original payload digest and generate new WARC-specific digests (e.g., `WARC-Block-Digest`, `WARC-Payload-Digest`).
*   **FR-02.3:** The tool shall handle large files and directories efficiently, supporting parallel processing of multiple input files.
*   **FR-02.4:** The tool shall generate a persistent, unique `WARC-Record-ID` for each output record.
*   **FR-02.5:** The tool shall provide detailed progress logging and a summary report upon completion.

#### 3.1.3 Migration Validation Tool (FR-03)
**Description:** A tool shall verify the integrity and completeness of a migration from ARC to WARC.
**Requirements:**
*   **FR-03.1:** The tool shall compare checksums (payload digests) of original ARC records and migrated WARC records to confirm content preservation.
*   **FR-03.2:** The tool shall verify that the count of records is consistent between source and target collections.
*   **FR-03.3:** The tool shall produce a validation report listing any discrepancies, errors, or warnings.
*   **FR-03.4:** The tool shall be executable independently of the migration tool for post-hoc verification.

### 3.2 WARC Utility Tools

#### 3.2.1 Repackaging Tool (FR-04)
**Description:** A tool to filter and extract subsets of records from one or more WARC files into new WARC files.
**Requirements:**
*   **FR-04.1:** The tool shall filter records based on configurable criteria including: URL/URI pattern (regex), MIME-type, date range, and WARC record type.
*   **FR-04.2:** The tool shall maintain all WARC header fields and payloads for selected records in the output files.
*   **FR-04.3:** The tool shall support both inclusion and exclusion filtering logic.

#### 3.2.2 Reporting Tool (FR-05)
**Description:** A tool to analyze WARC files and generate statistical and descriptive reports.
**Requirements:**
*   **FR-05.1:** The tool shall generate a summary report containing: total files, total records, total data volume, and date range.
*   **FR-05.2:** The tool shall generate a MIME-type distribution report.
*   **FR-05.3:** The tool shall generate a report listing hostnames and their respective frequencies and data volumes.
*   **FR-05.4:** The tool shall extract and present crawl log information (`metadata` records) in a readable format.
*   **FR-05.5:** Reports shall be output in both human-readable (plain text, Markdown) and machine-readable (CSV, JSON) formats.

#### 3.2.3 Quality Assurance (Crawl Comparison) Tool (FR-06)
**Description:** A tool to compare two sets of WARC files (e.g., from different crawls of the same seed) to identify changes.
**Requirements:**
*   **FR-06.1:** The tool shall identify URLs captured in both crawl sets, only in Crawl A, and only in Crawl B.
*   **FR-06.2:** For URLs present in both sets, the tool shall detect if the payload (content) has changed, using digest comparison.
*   **FR-06.3:** The tool shall generate a report highlighting significant deltas, such as new/changed/missing hosts or MIME-type distributions.
*   **FR-06.4:** The tool shall be configurable to ignore specific, inconsequential changes (e.g., differences in `Server` headers).

### 3.3 Enhanced WARC Browser (FR-07)
**Description:** Enhancements to the existing web-based WARC file browser to improve accessibility and usability.
**Requirements:**
*   **FR-07.1:** The browser shall implement server-side rewriting of embedded URIs within archived content (HTML, CSS) to allow proper rendering of intra-archive links.
*   **FR-07.2:** The browser shall support a "proxy mode" allowing it to act as a gateway to browse live web content alongside archived content.
*   **FR-07.3:** The browser shall integrate a full-text search capability across the content of loaded WARC files.
*   **FR-07.4:** The search interface shall allow filtering by date and URL domain.
*   **FR-07.5:** The browser shall provide a clear, navigable directory listing of WARC files and their contained records.

### 3.4 External Tool Integration
**Description:** The system shall provide hooks for integration with external validation and analysis tools.
**Requirements:**
*   **FR-08:** The migration and repackaging workflows shall have configurable points to call external virus scanning tools (e.g., ClamAV) on record payloads.
*   **FR-09:** The system shall have configurable points to call external format identification/validation tools (e.g., JHOVE) on record payloads and record the results in WARC metadata.

## 4. Non-Functional Requirements

### 4.1 Performance Requirements
*   **NFR-01 (Scalability):** The migration and repackaging tools shall be capable of processing collections containing **billions of records** and spanning **petabytes of data**. They shall support processing multiple files in parallel.
*   **NFR-02 (Efficiency):** Tools shall be designed for I/O-bound performance, minimizing memory footprint and enabling streaming processing where possible to handle very large files.
*   **NFR-03 (Responsiveness):** The web-based WARC browser shall load record listings and render rewritten pages with a latency of less than 2 seconds for typical operations.

### 4.2 Usability & Operational Requirements
*   **NFR-04 (CLI):** All core tools (migration, validation, repackaging, reporting, QA) shall provide a comprehensive, well-documented command-line interface.
*   **NFR-05 (Scriptability):** CLI tools shall use standard input/output streams and exit codes to enable easy scripting and integration into larger pipelines.
*   **NFR-06 (Logging):** All tools shall produce detailed, configurable logs (INFO, WARN, ERROR levels) to standard error or log files to facilitate debugging and auditing.
*   **NFR-07 (Web UI):** The migration configuration module and WARC browser shall have intuitive, accessible web interfaces designed for their respective user classes.

### 4.3 Design Constraints
*   **NFR-08 (Configurability):** Filter criteria (FR-04), report formats (FR-05), and comparison parameters (FR-06) shall be highly configurable without code modification.
*   **NFR-09 (Technology Independence):** The system shall avoid hard dependencies on specific commercial platforms, libraries, or partner-specific APIs. Dependencies must be justified by core requirements.
*   **NFR-10 (Verifiability):** The migration process shall be inherently verifiable. All tools that modify data shall provide a companion validation mechanism or log sufficient detail to enable external verification.

### 4.4 Portability & Integration
*   **NFR-11:** The software shall run on any standard JVM (version 8+) and be tested on major Linux distributions (Ubuntu LTS, CentOS/RHEL).
*   **NFR-12:** The tools shall be packageable as standalone JAR files and, where beneficial, as system packages (e.g., `.deb`, `.rpm`).

### 4.5 Undefined Requirements (To Be Resolved)
*   **NFR-13:** The default set of metadata fields to be populated during ARC-to-WARC migration is pending final specification from IIPC member consultation.
*   **NFR-14:** Quantitative targets for "large-scale" processing (e.g., records/second, TB/day) will be defined during the requirements gathering milestone with IIPC institutions.
*   **NFR-15:** The specific implementation strategy for distributed processing (e.g., messaging protocol, job queue design) is TBD based on technical prototyping.

## Appendix A: Data Definitions

| Entity | Primary Key | Key Fields / Attributes |
| :--- | :--- | :--- |
| **ARC File** | Filename | File path, size, collection context, internal record structure. |
| **WARC File** | Filename | File path, size, `WARC-Filename` header, internal WARC records. |
| **Migration Job** | Job ID | Configuration ID, source list, target directory, status (`PENDING`, `RUNNING`, `COMPLETE`, `FAILED`), timestamps, log file reference. |
| **WARC Record** | WARC-Record-ID | `WARC-Type`, `Target-URI`, `WARC-Date`, `Content-Type`, `WARC-Block-Digest`, `WARC-Payload-Digest`, payload. |
| **Report** | Report ID / Type | Source file list, generation timestamp, report format, filter parameters used, output location. |
| **Collection** | Logical | Set of WARC/ARC files, associated metadata (institution, crawl seed, time interval, curator). |

## Appendix B: Risk Log

| Risk ID | Description | Probability | Impact | Mitigation Strategy | Owner |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | Scope creep due to additional feature requests from IIPC members. | Medium | High | Maintain a strict requirement baseline. New requests must go through a formal change process, requiring descoping of existing features or additional funding. | Project Lead |
| R-02 | Distributed processing architecture becomes overly complex. | Medium | Medium | Favor simple, proven messaging (e.g., file-based queues, RabbitMQ) over complex frameworks (e.g., Hadoop). Prototype early. | Lead Developer |
| R-03 | Performance bottlenecks with extremely large (>1B record) migrations. | High | High | Adhere to streaming, low-memory design patterns. Conduct performance testing with real data as early as possible. | Lead Developer |
| R-04 | Delayed feedback or test data from partner institutions. | Medium | Medium | Proactive, scheduled communication. Define clear deadlines for feedback. Have fallback test plans using publicly available ARC data. | Project Manager |
| R-05 | Integration failures with external tools (ClamAV, JHOVE). | Low | Medium | Design integration as optional, plugin-based modules. Confirm versions and APIs during the design phase. | Developer |

---
*This document is subject to change upon resolution of Undecided Issues and further input from IIPC stakeholders.*