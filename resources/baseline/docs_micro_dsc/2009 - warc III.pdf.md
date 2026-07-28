# Software Requirements Specification (SRS)
## WARC Tools Extension: Large-Scale Migration & Management Suite

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the requirements for extending the existing WARC Tools open-source software suite. The primary purpose is to enable large-scale, automated migration of legacy web archive collections from the ARC format to the ISO-standard WARC format, and to provide enhanced, scalable management tools for WARC-based archives. This SRS is intended for use by project managers, developers, testers, and stakeholders involved in the implementation and validation of the new capabilities.

#### 1.2 Scope
The scope of this project encompasses the design, development, and integration of new command-line tools and programmatic APIs within the WARC Tools framework. The extensions will provide:
1.  **Batch ARC-to-WARC Migration:** Configurable, validated conversion of ARC file collections.
2.  **Intelligent WARC Repackaging:** Filtering and subsetting of WARC files based on metadata criteria.
3.  **Analytical Reporting:** Generation of summary reports on WARC file contents.
4.  **Scalable Architecture:** Support for parallel and distributed processing of large collections.

**Out of Scope:**
*   Development of a graphical user interface (GUI).
*   Long-term archival storage solutions or digital preservation workflows.
*   Deep content analysis (e.g., NLP, image recognition) within records.
*   Modification of the core WARC file format specification.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface
*   **ARC:** A legacy file format for storing web crawls and archival data.
*   **HTTP:** Hypertext Transfer Protocol
*   **ISO:** International Organization for Standardization
*   **JVM:** Java Virtual Machine
*   **MIME-type:** Multipurpose Internet Mail Extensions type, a standard identifier for file formats.
*   **REST:** Representational State Transfer
*   **SRS:** Software Requirements Specification
*   **URI/URL:** Uniform Resource Identifier / Locator
*   **WARC:** Web ARChive file format, an ISO standard (ISO 28500) for storing web archival data.

#### 1.4 References
*   ISO 28500:2017 - WARC file format specification.
*   Internet Archive ARC File Format Specification.
*   Existing WARC Tools Suite Documentation & Source Code.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements, including performance, scalability, and design constraints.

### 2. Overall Description

#### 2.1 Product Perspective
This project is a major extension of the existing WARC Tools suite, a set of Java-based libraries and command-line utilities for handling WARC files. The new modules will integrate seamlessly with the existing architecture, adhering to its design patterns and conventions.

#### 2.2 Product Functions
The enhanced suite will provide three core functional groups:
1.  **Migration Tool (`arc2warc-batch`):** Orchestrates the conversion of directories containing ARC files to WARC format, with progress tracking, error handling, and configurable options.
2.  **Filter & Repackage Tool (`warc-filter`):** Creates new WARC files containing a subset of records from one or more input WARC files, selected via user-defined filters (URL pattern, date range, MIME-type, etc.).
3.  **Reporting Tool (`warc-summary`):** Analyzes one or more WARC files and produces structured reports (e.g., JSON, CSV) detailing counts, sizes, MIME-type distributions, date spans, and URL patterns.

#### 2.3 User Characteristics
Primary users are **digital archivists, digital librarians, and system administrators** responsible for managing web archive collections. They are technically proficient with command-line interfaces and have a strong understanding of web archiving concepts and file formats.

#### 2.4 Constraints
1.  **Technical Constraints:** The implementation must be primarily in Java and compatible with Java 8+ JVM environments.
2.  **Architectural Constraints:** Tools must be designed to process multiple files in parallel and must support scaling to very large collections through integration with distributed processing frameworks (e.g., Apache Spark, Hadoop MapReduce) via clean APIs.
3.  **Dependency Constraints:** Must avoid introducing unnecessary or heavy third-party dependencies. The core tools should remain lightweight and portable.
4.  **Integration Constraints:** Must avoid hard-coded, partner-specific integrations. Functionality should be generic and configurable.

#### 2.5 Assumptions and Dependencies
*   Assumes input ARC and WARC files are structurally valid and not corrupt.
*   Dependent on the continued maintenance of the core WARC Tools library.
*   Assumes target deployment environments have sufficient disk I/O and memory for processing large files.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Batch ARC to WARC Migration (FUN-MIG-001)
**Description:** The system shall provide a tool to migrate a collection of ARC files to WARC format in a batch operation.

**Requirements:**
*   **FUN-MIG-001.1:** The tool shall accept a directory path as input and recursively discover all files with the `.arc` or `.arc.gz` extension.
*   **FUN-MIG-001.2:** The tool shall convert each discovered ARC file to a corresponding WARC file (`.warc` or `.warc.gz`), preserving all original record content and metadata.
*   **FUN-MIG-001.3:** The tool shall support a configurable number of parallel conversion threads to optimize performance.
*   **FUN-MIG-001.4:** The tool shall generate a validation report post-migration, listing successful conversions, failures, and any integrity check errors.
*   **FUN-MIG-001.5:** The tool shall provide command-line options to specify output directory, compression preference, and batch size.

##### 3.1.2 WARC Record Filtering and Repackaging (FUN-REP-001)
**Description:** The system shall provide a tool to create new WARC files containing a filtered subset of records from one or more source WARC files.

**Requirements:**
*   **FUN-REP-001.1:** The tool shall accept one or more input WARC files and a set of filter criteria.
*   **FUN-REP-001.2:** The tool shall filter records based on:
    *   **FUN-REP-001.2a:** URI/URL (e.g., prefix, regex pattern).
    *   **FUN-REP-001.2b:** MIME-type (e.g., `"image/jpeg"`, `"text/html"`).
    *   **FUN-REP-001.2c:** Record type (e.g., `response`, `request`, `metadata`).
    *   **FUN-REP-001.2d:** Date-Time range (based on WARC-Date header).
*   **FUN-REP-001.3:** The tool shall write all records matching the filter criteria to a new, valid WARC file.
*   **FUN-REP-001.4:** The tool shall preserve the original order of records from the source file(s) in the output file.
*   **FUN-REP-001.5:** The tool shall support combining filtered results from multiple input files into a single output file.

##### 3.1.3 WARC Content Summary and Reporting (FUN-REP-002)
**Description:** The system shall provide a tool to generate summary reports and statistics for one or more WARC files.

**Requirements:**
*   **FUN-REP-002.1:** The tool shall analyze specified WARC files and calculate the following metrics:
    *   Total number of records per type (response, request, etc.).
    *   Total uncompressed and compressed byte size.
    *   Distribution of MIME-types for response records.
    *   Time range (earliest and latest WARC-Date).
    *   List of unique hostnames or URL prefixes (configurable depth).
*   **FUN-REP-002.2:** The tool shall output the report in structured, machine-readable formats (JSON primary, CSV optional).
*   **FUN-REP-002.3:** The tool shall be capable of generating a consolidated report for a directory of WARC files.

##### 3.1.4 Programmatic API (FUN-API-001)
**Description:** The core functionality for migration, filtering, and reporting shall be exposed through a well-defined Java API to enable integration into larger workflows and distributed processing jobs.

**Requirements:**
*   **FUN-API-001.1:** A service layer shall be provided, encapsulating the business logic for migration, filtering, and reporting.
*   **FUN-API-001.2:** This service layer shall be callable via RESTful web services (e.g., using JAX-RS), allowing for remote execution and integration.
*   **FUN-API-001.3:** The API shall be designed to accept job definitions (source paths, filter parameters) and return job status and results asynchronously.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements
*   **PERF-001:** The batch migration tool shall be capable of processing ARC files at a rate no less than 50% of the maximum I/O throughput of the underlying storage system.
*   **PERF-002:** The filter tool shall stream records to avoid loading entire WARC files into memory, ensuring scalability to multi-gigabyte files.

##### 3.2.2 Scalability Requirements
*   **SCAL-001:** The architecture of all tools shall support parallel processing of multiple independent files. Command-line tools shall use a configurable thread pool.
*   **SCAL-002:** The design of the core processing logic (filtering, conversion) shall be separable from the job orchestration, enabling it to be packaged as a library for use in distributed frameworks like Apache Spark.

##### 3.2.3 Reliability & Availability
*   **RELY-001:** The batch migration tool shall be idempotent. Re-running on the same source directory shall skip successfully converted files (based on checksum or presence) unless forced.
*   **RELY-002:** Tools shall include comprehensive error logging and shall fail gracefully with informative messages for malformed input files.

##### 3.2.4 Design Constraints
*   **CONS-001:** Implementation shall be in Java, maintaining compatibility with the existing WARC Tools codebase.
*   **CONS-002:** New third-party dependencies must be justified and kept to a minimum. Preference is for lightweight, widely-adopted libraries.

##### 3.2.5 Compliance
*   **COMP-001:** Output WARC files must strictly comply with the ISO 28500:2017 WARC format specification.
*   **COMP-002:** RESTful APIs, if implemented, shall follow standard HTTP conventions and use standard media types (e.g., `application/json`).

### 4. Appendices

#### 4.1 Example Command-Line Usage
```bash
# 1. Batch Migration
java -jar warc-tools.jar arc2warc-batch --input /data/arc_collection/ --output /data/warc_collection/ --threads 8 --compress

# 2. Filtering
java -jar warc-tools.jar warc-filter --input "crawl_*.warc.gz" --output subset.warc.gz --mime-type "text/html" --url-prefix "https://example.com"

# 3. Reporting
java -jar warc-tools.jar warc-summary --input /data/collection/*.warc --format json --output report.json
```

#### 4.2 Preliminary Reporting Schema (JSON)
```json
{
  "analyzedFiles": ["file1.warc.gz", "file2.warc.gz"],
  "summary": {
    "totalRecords": 150432,
    "totalSizeBytes": 2547892134,
    "earliestDate": "2020-01-01T12:00:00Z",
    "latestDate": "2020-12-31T23:59:59Z"
  },
  "breakdown": {
    "byRecordType": {
      "response": 120345,
      "request": 30087
    },
    "byMimeType": {
      "text/html": 80321,
      "image/jpeg": 15234,
      "application/javascript": 9876
    }
  }
}
```