# Software Requirements Specification (SRS)
## WARC Format Adoption and Manipulation System (WFAMS)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the WARC Format Adoption and Manipulation System (WFAMS). The purpose of this document is to provide a detailed description of the system's capabilities, interfaces, and performance characteristics. It is intended for use by the project stakeholders, developers, testers, and project managers involved in the system's development and deployment.

#### 1.2 Scope
The WFAMS is a suite of tools designed to facilitate the adoption, validation, and manipulation of the WARC (Web ARChive) file format, an ISO standard (28500:2017) for web archives. The system's primary scope encompasses:

*   **Format Migration:** Converting legacy ARC (Archive) format collections to the WARC format.
*   **Data Integrity:** Validating the fidelity of migrated content against original ARC sources.
*   **Collection Management:** Repackaging existing WARC collections by filtering and extracting records based on user-defined criteria.
*   **Collection Analysis:** Generating comprehensive reports on the content and structure of WARC file collections.

The system is explicitly scoped to handle web archive data. It does not include general-purpose file conversion, long-term archival storage management, or web crawling functionalities.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ARC:** A legacy file format for storing web crawls and archives.
*   **WARC:** Web ARChive file format, an ISO standard that extends the ARC format.
*   **Record:** A discrete unit of data within an ARC or WARC file (e.g., a single HTTP response, a request, metadata).
*   **Collection:** A logical grouping of ARC or WARC files, often representing a complete crawl or archive project.
*   **Web Archivist:** A professional responsible for appraising, selecting, and preserving web content.
*   **Crawl Engineer:** A professional responsible for designing, configuring, and operating web crawlers.

#### 1.4 References
*   ISO 28500:2017, *Information and documentation — WARC file format*
*   *ARC File Format Specification* (Internet Archive)
*   *Web Archiving Lifecycle* (IIPC)

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details specific system requirements, including functional, external interface, and non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
The WFAMS is a standalone, command-line driven suite of tools. It operates on file-based inputs and outputs, interacting primarily with the host operating system's file system. It may read configuration files and write log files and report outputs.

#### 2.2 Product Functions
The core functions of the WFAMS are:
1.  **ARC-to-WARC Migration:** Convert one or more ARC files into WARC format, preserving all original record content and essential metadata.
2.  **Migration Validation:** Perform a byte-level or checksum-based comparison between original ARC records and their migrated WARC counterparts to ensure data integrity.
3.  **WARC Repackaging:** Create new WARC files from existing ones by selecting records that match user-specified filters (e.g., URL patterns, date ranges, MIME types).
4.  **WARC Reporting:** Analyze collections of WARC files to generate reports summarizing metrics such as total size, record counts, URL domains, date spans, and record types.

#### 2.3 User Characteristics
*   **Primary User (Web Archivist / Crawl Engineer):** Technically proficient, possesses deep understanding of web archive formats (ARC/WARC), file systems, and large-scale data processing concepts. Comfortable using command-line interfaces and scripting for batch operations.
*   **Secondary User (System Administrator):** Responsible for deploying and scheduling large-scale migration jobs. Requires understanding of system resource management and configuration.

#### 2.4 Constraints
1.  **Scalability Constraint:** The tools must be designed to process collections containing **millions of files** and terabytes/petabytes of data efficiently.
2.  **Dependency Constraint:** The implementation must **avoid unnecessary technology dependencies** (e.g., specific commercial databases, heavy-weight frameworks) to ensure portability, ease of deployment, and long-term maintainability.
3.  **Operational Constraint:** The migration tool must support **configuration-driven execution** to enable automated, large-scale operations without manual intervention per job.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Input ARC and WARC files conform to their respective format specifications.
*   **Assumption:** The host system provides sufficient storage (temporary and permanent) and memory to handle the intended collection sizes.
*   **Dependency:** Access to a stable file system (local, NAS, or cloud storage) for input and output.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 Migration Module**
*   **FR-MIG-01:** The system shall read a specified ARC file and convert each valid ARC record into a corresponding WARC record.
*   **FR-MIG-02:** The system shall preserve the payload (content block) of the original ARC record without alteration during migration.
*   **FR-MIG-03:** The system shall generate appropriate WARC header fields (e.g., `WARC-Type`, `WARC-Record-ID`, `WARC-Date`, `Content-Length`) for each migrated record.
*   **FR-MIG-04:** The system shall support batch processing of all ARC files within a specified directory tree.
*   **FR-MIG-05:** The system shall accept a configuration file that defines parameters for large-scale migration jobs (e.g., source/destination paths, file patterns, error handling rules, logging verbosity).

**3.1.2 Validation Module**
*   **FR-VAL-01:** The system shall compare a migrated WARC file against its source ARC file.
*   **FR-VAL-02:** The system shall verify that the sequence and content of records are identical, focusing on the record payload.
*   **FR-VAL-03:** The system shall produce a validation report indicating success or detailing mismatches (e.g., record count difference, checksum failure).
*   **FR-VAL-04:** The system shall perform validation in a single pass to minimize I/O for large files.

**3.1.3 Repackaging Module**
*   **FR-REP-01:** The system shall read one or more WARC files and filter records based on user-provided criteria.
*   **FR-REP-02:** Filtering criteria shall include:
    *   URL (exact match, regex pattern, domain suffix).
    *   Record timestamp (date ranges).
    *   WARC record type (e.g., `response`, `request`, `metadata`).
    *   MIME type of the payload.
*   **FR-REP-03:** The system shall write matching records to a new, valid WARC file.
*   **FR-REP-04:** The system shall maintain all original WARC headers for the selected records.

**3.1.4 Reporting Module**
*   **FR-REP-01:** The system shall analyze a collection of WARC files and generate a summary report.
*   **FR-REP-02:** The report shall include, at a minimum:
    *   Total size of the collection (bytes, GB).
    *   Total number of WARC files.
    *   Total number of records, broken down by WARC type.
    *   Time span covered (earliest and latest WARC-Date).
    *   List of top N hostnames/domains and their record counts.
*   **FR-REP-03:** The system shall output the report in both human-readable (e.g., plain text, Markdown) and machine-parsable (e.g., JSON, CSV) formats.

#### 3.2 External Interface Requirements

**3.2.1 User Interfaces**
*   **CLI Interface:** The primary interface shall be a command-line interface (CLI). Each core function shall be a distinct command (e.g., `wfam migrate`, `wfam validate`, `wfam filter`, `wfam report`) with appropriate options and arguments.

**3.2.2 Hardware Interfaces**
*   The system shall operate on standard 64-bit server hardware.
*   It shall require read/write access to standard file systems.

**3.2.3 Software Interfaces**
*   **Operating System:** The system shall be compatible with major Linux distributions (e.g., RHEL/CentOS, Ubuntu). Portability to other POSIX-like environments (e.g., macOS) is desirable.
*   **Libraries:** Dependencies shall be minimized. Essential dependencies may include a standard library for compression (zlib) and, if necessary, a lightweight library for parsing WARC/ARC formats.

**3.2.4 Communications Interfaces**
*   Not applicable for initial version. All I/O is file-based.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   **PERF-01:** The migration and validation tools shall process data in a **streaming manner** to handle files larger than available RAM.
*   **PERF-02:** The system shall be capable of processing **at least 100 GB of WARC/ARC data per hour** on reference hardware (specified in Design Document).
*   **PERF-03:** Memory footprint during operation shall remain relatively constant and **sub-linear to input file size**.

**3.3.2 Scalability Requirements**
*   **SCAL-01:** The system's architecture shall allow parallel processing of independent files within a collection to leverage multi-core systems.
*   **SCAL-02:** The tools shall be able to process a collection defined by a list of millions of file paths.

**3.3.3 Reliability & Availability**
*   **RELY-01:** The system shall include comprehensive error handling for malformed input files, skipping or logging errors as per configuration without causing a total job failure.
*   **RELY-02:** For migration jobs, the system shall support resumable operations or be idempotent to allow safe restart from failure points.

**3.3.4 Portability & Maintainability**
*   **PORT-01:** The system shall be developed in a portable language (e.g., Java, Python, Go, C++) and avoid platform-specific code.
*   **MAIN-01:** The codebase shall be modular, with clear separation between core format logic, I/O handling, and business logic for each tool.

**3.3.5 Security Requirements**
*   **SEC-01:** The system shall not introduce security vulnerabilities (e.g., buffer overflows, path traversal via input parameters).
*   **SEC-02:** The system shall respect the file permissions of the operating system.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| Quality Assurance | | | |