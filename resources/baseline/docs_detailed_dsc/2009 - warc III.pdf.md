# Software Requirements Specification (SRS)
## WARC Tools Phase III Suite

**Document Version:** 1.0
**Date:** [Date of Generation]
**Project Lead:** Hanzo Archives Limited
**Stakeholders:** International Internet Preservation Consortium (IIPC) Member Institutions

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the WARC Tools Phase III project. The purpose is to define the extensions to the existing WARC Tools suite to enable large-scale migration from the ARC to the WARC file format and to provide enhanced tools for managing web archive collections. This document serves as a reference for developers, testers, project managers, and stakeholders.

#### 1.2 Scope
The scope of this project includes the development of five core components:
1.  A migration application for converting ARC files to WARC format.
2.  A repackaging tool for creating subsets of WARC collections.
3.  A reporting application for generating collection summaries.
4.  A quality assurance tool for comparing crawls.
5.  An enhanced WARC browser with improved navigation and search.

**In-Scope:**
*   Development of command-line tools for archivists and engineers.
*   Integration with external services for virus scanning, file identification, and persistent ID generation.
*   Support for distributed, large-scale processing.
*   Creation of a web-based console for monitoring and reporting.
*   Compliance with the WARC standard (ISO 28500).

**Out-of-Scope (Non-Goals):**
*   Functionality to handle underlying hardware or network failures.
*   Development of partner-specific integration technologies or customizations.
*   Long-term maintenance and hosting of deployed instances at partner institutions.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ARC:** A legacy format for storing web crawl data.
*   **WARC (Web ARChive):** The ISO 28500 standard format for storing web archive collections, successor to ARC.
*   **IIPC:** International Internet Preservation Consortium.
*   **URI:** Uniform Resource Identifier.
*   **MIME-type:** Multipurpose Internet Mail Extensions type, a standard identifier for file formats.
*   **SLA:** Service Level Agreement.
*   **QA:** Quality Assurance.
*   **API:** Application Programming Interface.
*   **UUID:** Universally Unique Identifier.
*   **ARK:** Archival Resource Key.
*   **NOID:** Nice Opaque Identifier.

#### 1.4 References
*   ISO 28500:2017 - WARC (Web ARChive) file format.
*   Existing WARC Tools Suite Documentation.
*   IIPC Community Guidelines and Best Practices.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its stakeholders, and operating environment. Section 3 details the specific functional requirements for each component. Section 4 outlines non-functional requirements. Appendices may contain supplementary diagrams or data models.

### 2. Overall Description

#### 2.1 Product Perspective
The WARC Tools Phase III suite is an enhancement of the existing open-source WARC Tools ecosystem. It operates as a collection of standalone, interoperable command-line utilities and a supporting web application. It interacts with external systems for specialized services (virus scanning, format identification) and produces standards-compliant WARC files and reports for use by preservation systems and researchers.

#### 2.2 Stakeholders and User Classes
| Stakeholder / User Class | Role & Responsibilities |
| :--- | :--- |
| **Hanzo Archives Limited** | Project lead. Responsible for project management, requirements finalization, development, integration, and final deployment of the open-source suite. |
| **IIPC Member Institutions** (e.g., BnF, BL, Netarchive.dk) | Collaborative partners. Provide requirements, real-world test data, conduct acceptance testing, and offer feedback. |
| **Crawl Engineers / Web Archivists** (Primary End User) | Technical users who will execute command-line tools to migrate, validate, repackage, and perform QA on large-scale web archive collections. |
| **Researchers** (Secondary End User) | Use reporting, comparison, and enhanced browsing tools to analyze content within web archive collections for academic or investigative purposes. |

#### 2.3 Operating Environment
*   **Software:** Designed to run on standard Linux/Unix-based server environments. Tools are command-line based. The WARC Browser is a web application requiring a servlet container (e.g., Tomcat, Jetty).
*   **Hardware:** Must support processing of very large collections (terabytes to petabytes). Tools are designed to be I/O-bound and capable of distributed execution across multiple machines.
*   **External Dependencies:** Relies on integration with external services (ClamAV, DROID/JHOVE, Persistent ID minting service). These services are not provided by this project.

#### 2.4 Design and Implementation Constraints
1.  **Compliance:** All WARC file output must strictly comply with ISO 28500.
2.  **Performance:** Must use memory-efficient, stream-oriented processing to handle billions of records.
3.  **Integration:** External tool integrations must be configurable and not create hard dependencies.
4.  **Open Source:** The final product will be released as open-source software.

#### 2.5 User Documentation
Comprehensive documentation shall be provided, including:
*   Man pages for all command-line tools.
*   A user guide covering installation, configuration, and typical workflows.
*   API documentation for integration points.
*   Example configuration files and scripts.

### 3. System Features and Requirements

#### 3.1 Feature: ARC to WARC Migration
**3.1.1 Description**
A tool (`arc_warc_migrate`) to convert collections of legacy ARC files into the standard WARC format, with configurable metadata enhancement and integration with external services.

**3.1.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **MIG-001** | The tool shall accept as input a directory (or list) of ARC files and a configuration file. | High |
| **MIG-002** | The tool shall parse ARC files using a reliable external ARC reader library (e.g., Heritrix arcreader). | High |
| **MIG-003** | For each valid ARC record, the tool shall create a corresponding WARC record with all original payload content. | High |
| **MIG-004** | The tool shall generate and assign a unique, persistent WARC-Record-ID to each new WARC record, configurable to use a service (ARK, NOID) or local UUID. | High |
| **MIG-005** | The tool shall allow configuration to add user-specified metadata fields (WARC headers) during migration (e.g., operator, software). | Medium |
| **MIG-006** | The tool shall support a pre-migration "virus scan" step via integration with an external scanner (e.g., ClamAV). Records flagged as malware shall be skipped or logged according to configuration. | High |
| **MIG-007** | The tool shall support a "file identification" step via integration with an external tool (e.g., DROID, JHOVE) to populate format metadata. | Medium |
| **MIG-008** | The tool shall be capable of distributed execution, allowing a migration job to be split across multiple nodes. | High |
| **MIG-009** | The tool shall create checkpoints to allow for restarting a migration job from the last committed state in case of intentional stoppage. | Medium |
| **MIG-010** | The tool shall log detailed progress, statistics (records processed, errors), and any failures to a configurable destination. | High |

#### 3.2 Feature: Migration Validation
**3.2.1 Description**
A tool (`arc_warc_verify`) to validate the fidelity of a migration by comparing the original ARC and resultant WARC collections.

**3.2.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **VAL-001** | The tool shall accept a list of source ARC files and their corresponding migrated WARC files. | High |
| **VAL-002** | The tool shall perform a checksum comparison (e.g., SHA-1) of the payload content for each ARC record and its corresponding WARC record. | High |
| **VAL-003** | The tool shall support a sampling mode where only a configurable percentage of records are validated, to speed up verification on very large collections. | Medium |
| **VAL-004** | The tool shall produce a validation report indicating success, or detailing any mismatches (checksum, missing records). | High |
| **VAL-005** | The tool shall be usable independently of the migration tool to validate third-party migrations. | Low |

#### 3.3 Feature: WARC Repackaging
**3.3.1 Description**
A tool (`warc_repackage`) to create new, smaller WARC files by filtering records from a source collection based on specified criteria.

**3.3.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **REP-001** | The tool shall accept as input a set of source WARC files and filter criteria. | High |
| **REP-002** | The tool shall filter records based on URL patterns (regex or glob). | High |
| **REP-003** | The tool shall filter records based on MIME-type. | High |
| **REP-004** | The tool shall filter records based on date ranges (WARC-Date). | High |
| **REP-005** | The tool shall include necessary contextual records (e.g., the corresponding `warcinfo` record) in the output package. | Medium |
| **REP-006** | The tool shall output new, valid WARC files containing only the filtered records and their context. | High |
| **REP-007** | The tool shall support "pre-operation" filters to exclude records from processing (e.g., skip very large binary files). | Low |

#### 3.4 Feature: Reporting and Analysis
**3.4.1 Description**
A tool (`warc_summary`) and web interface to generate summary reports and statistics from a collection of WARC files.

**3.4.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **REP-101** | The command-line tool shall generate a report of MIME-type distribution for a given WARC collection. | High |
| **REP-102** | The command-line tool shall generate a report of hostname/domain distribution. | High |
| **REP-103** | The command-line tool shall output reports in human-readable (text) and machine-readable (CSV, JSON) formats. | Medium |
| **REP-104** | The WARC Browser web UI shall provide a dashboard displaying high-level summary statistics (file count, total size, date range) for a loaded collection. | High |
| **REP-105** | The WARC Browser shall allow users to generate and export the reports defined in REP-101 and REP-102 via the UI. | Medium |

#### 3.5 Feature: Quality Assurance (Crawl Comparison)
**3.5.1 Description**
A tool (`warc_compare`) to analyze differences between two or more crawls (WARC collections) of the same seed set for QA purposes.

**3.5.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **QA-001** | The tool shall accept two sets of WARC files as input (Crawl A and Crawl B). | High |
| **QA-002** | The tool shall identify records that are unique to Crawl A, unique to Crawl B, and common to both. | High |
| **QA-003** | The tool shall compare common records and detect changes in HTTP status codes, payload digests, and content length. | High |
| **QA-004** | The tool shall generate a delta report summarizing the additions, deletions, and changes. | High |
| **QA-005** | The tool shall produce visualizations (e.g., graphs of change over time by domain) as configurable output. | Medium |

#### 3.6 Feature: Enhanced WARC Browser
**3.6.1 Description**
Enhancements to the existing WARC Browser web application for improved navigation, search, and display.

**3.6.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **WB-001** | The browser shall integrate the Search Tools module to provide full-text search across the payload content of a WARC collection. | High |
| **WB-002** | The browser shall implement server-side rewriting rules to improve the rendering of archived web pages by fixing common broken links. | Medium |
| **WB-003** | The browser shall provide a navigable file manifest view, listing all WARC files and their contained records with key metadata (URI, date, type). | High |
| **WB-004** | The browser UI shall be responsive and functional for summary-level interaction. (Detailed replay performance is out of scope). | Medium |

### 4. Non-Functional Requirements

#### 4.1 Performance
1.  The migration and processing tools shall be primarily I/O-bound and designed to minimize memory footprint, allowing processing of collections significantly larger than available RAM.
2.  The tools shall support scalable, distributed architectures to parallelize work across multiple machines for very large jobs.
3.  The WARC Browser web interface shall load summary dashboards and manifests responsively (target: < 3 seconds for collections of up to 1 million records).

#### 4.2 Reliability & Availability
1.  The migration process shall implement atomic write operations or checkpoints to prevent corruption of output WARC files in case of process interruption.
2.  All tools shall provide comprehensive logging (INFO, WARN, ERROR levels) to facilitate debugging and audit trails.

#### 4.3 Security
1.  The migration tool **must** integrate with a virus scanning interface (e.g., ClamAV) to check payloads before they are written to new WARC files. This is a critical safety requirement.
2.  Configuration files for external services (e.g., PID service credentials) shall be protected by standard filesystem permissions.

#### 4.4 Compliance
1.  All WARC files generated by the tools must be valid according to the ISO 28500 standard.
2.  The software shall be developed with minimal external technology dependencies to ensure long-term maintainability.

#### 4.5 Observability
1.  All command-line tools shall provide standard console output for progress and a `--verbose` flag for detailed logging.
2.  Tools shall log duration and outcome (success/failure) upon completion.

### 5. Interface Requirements

#### 5.1 External Service Interfaces
| Service | Direction | Purpose | Key Contract |
| :--- | :--- | :--- | :--- |
| **ARC Reader Lib** | Inbound | Parse ARC files. | Must correctly handle the ARC format specification. Input: ARC file path. Output: Stream of ARC records. |
| **Virus Scanner (e.g., ClamAV)** | Outbound | Scan payloads pre-migration. | Configurable TCP socket or command-line call. Input: Payload byte stream. Output: `CLEAN` or `FOUND`. Timeout must be configurable. |
| **File ID Service (e.g., DROID)** | Outbound | Identify file formats. | Configurable command-line call or API. Input: Payload file. Output: Format PUID/MIME-type. |
| **Persistent ID Service (e.g., NOID)** | Outbound | Mint unique record IDs. | Configurable HTTP API or command-line call. Input: Seed metadata. Output: Opaque unique identifier (ARK, NOID). Must guarantee uniqueness. |

#### 5.2 Software Interfaces
*   **Search Tools Module:** The WARC Browser will integrate with this existing module via its defined Java API to provide full-text search capabilities.
*   **libwarc:** Core tools will utilize the project's existing `libwarc` library for low-level, memory-efficient WARC file reading and writing.

### 6. Acceptance Criteria
The following high-level acceptance scenarios must be successfully demonstrated:

1.  **Migration Success:** Given a valid configuration file and a set of 1000 ARC files, when `arc_warc_migrate` is executed, it produces a corresponding set of WARC files containing all convertible records, with user-specified metadata and WARC-Record-IDs present.
2.  **Validation Accuracy:** Given the output from scenario 1, when `arc_warc_verify` is run with full checksum comparison, it reports a 100% match with zero errors.
3.  **Repackaging Filtering:** Given a set of WARC files and a URL filter for `*.example.com`, when `warc_repackage` is executed, the output WARC files contain only records whose target URI matches the pattern.
4.  **Report Generation:** Given a directory of WARC files, when `warc_summary --type=mimetype` is executed, it outputs a correct count of `text/html`, `image/jpeg`, etc., records in CSV format.
5.  **QA Comparison:** Given WARC files from two crawls of the same seed, when `warc_compare` is run, it produces a coherent delta report listing added, removed, and changed URLs.

### Appendix A: Domain Model (UML Class Overview)
```
+----------------+       +-------------------+       +---------------------+
|   ARC File     |       |  Migration Job    |       | WARC File           |
|----------------|       |-------------------|       |---------------------|
| - filename     |       | - jobId (UUID)    |1     1| - filename          |
| - size         |       | - configRef       |<>----<>| - size              |
| - records[]    |       | - status          |       | - records[]         |
+----------------+       | - startTime       |       | - warcInfoId        |
          ^              | - endTime         |       +---------------------+
          |              +-------------------+                   ^
          |                          |                           |
          | uses                     | generates                |
          |                          |                          |
+----------------+       +-------------------+       +---------------------+
| External ARC   |       | Migration Config  |       | WARC Record         |
| Reader         |       |-------------------|       |---------------------|
+----------------+       | - configId        |       | - recordId (Persist)|
                         | - metadataRules   |       | - type              |
                         | - errorHandling   |       | - targetURI         |
                         | - externalToolCfg |       | - payloadDigest     |
                         +-------------------+       | - contentType       |
                                   |                 | - date              |
                                   | configures      +---------------------+
                                   |                                    ^
+-------------------------------+  |                                    |
|      Validation Result        |  |                 +---------------------+
|-------------------------------|  |                 |   Filter Criteria   |
| - jobId                       |  |                 |---------------------|
| - status (PASS/FAIL)          |  |                 | - type (URL,MIME,Date)|
| - mismatchDetails[]           |  |                 | - pattern/value     |
+-------------------------------+  |                 +---------------------+
            ^                      |                           |
            | produced by          |                           | used by
            |                      |                           |
+-------------------------------+  |                 +---------------------+
|           Report              |  |                 |   QA Delta Report   |
|-------------------------------|  |                 +---------------------+
| - type (MIME, Host, etc.)     |  |
| - sourceCollection            |  |
| - generatedDate               |  |
| - outputFormat (CSV, JSON)    |  |
+-------------------------------+
```

### Appendix B: Open Issues and Decisions
The following items are pending resolution. The responsible party must decide before or during implementation.

| Issue | Description | Responsible Party |
| :--- | :--- | :--- |
| **ISSUE-01** | Final specification of default metadata headers to add during migration. | IIPC Members -> Hanzo |
| **ISSUE-02** | Selection of specific external file identification tool(s) for integration. | Hanzo (with IIPC input) |
| **ISSUE-03** | Final decision on persistent identifier service/format (NOID, ARK, UUID). | Hanzo (based on community practice) |
| **ISSUE-04** | Detailed sampling algorithm and confidence metrics for large-scale validation. | Hanzo (refined during testing) |
| **ISSUE-05** | Specific graph types (e.g., bar, timeline) for the QA comparator visualization output. | Hanzo (with IIPC user feedback) |
| **ISSUE-06** | Scope and complexity of server-side rewriting rules in the WARC Browser. | Hanzo |
| **ISSUE-07** | Nature and timeline of contribution from the Swedish National Library. | Swedish National Library |
| **ISSUE-08** | Priority and scope of building a post-migration reporting database. | Hanzo (based on effort/value) |

---
*Document End*