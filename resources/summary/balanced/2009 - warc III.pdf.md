# Balanced Summary: WARC Tools Phase III

## Goals and Scope
The WARC Tools Phase III project aims to extend the existing open-source toolkit for manipulating web archive (WARC) files, building upon the foundational libwarc library and tools developed in prior phases. Its primary scope is to develop a comprehensive migration application for converting legacy ARC files to WARC format, alongside new tools for repackaging, reporting, quality assurance, and enhanced browsing of WARC collections. The project emphasizes community collaboration with IIPC member institutions for requirements gathering and real-world testing.

## Stakeholders and User Stories
**Stakeholders:**
*   **Hanzo Archives Limited:** Project lead responsible for specification, development, and delivery.
*   **International Internet Preservation Consortium (IIPC):** Consortium sponsoring and overseeing the project.
*   **IIPC Member Institutions (e.g., BnF, BL, Netarchive.dk):** Contributing institutions providing requirements, test data, and deployment environments.
*   **Crawl Engineers / Web Archivists:** End-users who will operate the tools to manage and migrate web archive collections.
*   **Researchers:** End-users who will utilize the tools to explore and analyze archived web content.

**User Stories:**
1.  As a **web archivist**, I want to **migrate large collections of ARC files to the WARC format** so that **our archive complies with the modern standard and is interoperable**.
2.  As a **crawl engineer**, I want to **validate that a migration from ARC to WARC preserved all content correctly** so that **I can ensure data integrity**.
3.  As a **researcher**, I want to **extract a subset of records from a WARC collection based on URL or date** so that **I can analyze a specific segment of the archive**.
4.  As a **collection manager**, I want to **generate summary reports on the content and structure of WARC files** so that **I can understand and document my holdings**.
5.  As a **quality assurance analyst**, I want to **compare the results of two crawls of the same seed** so that **I can identify significant changes or anomalies**.
6.  As an **end-user**, I want to **browse and search the contents of WARC files through a web interface** so that **I can easily access archived web materials**.

## Key Processes
1.  **Migration Configuration:** A user configures the migration workflow via a web UI or file, defining parameters and metadata. *(Trigger: Start of a migration project)*.
2.  **ARC to WARC Conversion:** The migration tool processes a set of ARC files, converting records to WARC format according to the configuration. *(Trigger: Execution of the migration job)*.
3.  **Migration Validation:** The validation tool compares checksums and metadata between original ARC and newly created WARC files to verify correctness. *(Trigger: Post-migration verification)*.
4.  **WARC Repackaging:** A tool filters and extracts specific records from WARC files based on criteria (URL, MIME-type, date) into new WARC files. *(Trigger: User request to subset or reorganize a collection)*.
5.  **Collection Reporting:** The summary tool analyzes WARC files to generate reports on content statistics, mimetypes, hostnames, and crawl logs. *(Trigger: User request for collection analysis)*.
6.  **Crawl Comparison:** The QA tool compares two sets of WARC files from similar crawls to identify deltas and changes for quality assurance. *(Trigger: Need to analyze differences between crawl iterations)*.
7.  **Enhanced Browsing & Search:** The WARC browser is enhanced with server-side rewriting, proxy mode, and integrated full-text search capabilities. *(Trigger: User access to the web-based browser interface)*.

## Domain Data Elements
*   **ARC File:** (Primary Key: Filename). Key Fields: Record payload, URL, timestamp, MIME-type, original header metadata.
*   **WARC File:** (Primary Key: Filename). Key Fields: WARC-Record-ID, Target-URI, WARC-Date, Content-Type, WARC-Type.
*   **Migration Job:** (Primary Key: Job ID). Key Fields: Configuration reference, source ARC file list, target directory, status, start/end time.
*   **WARC Record:** (Primary Key: WARC-Record-ID). Key Fields: Payload, checksum, record type, concurrent To, concurrent From.
*   **Report:** (Primary Key: Report ID / Type). Key Fields: Source WARC files, generation date, report format (e.g., summary, mimetype), filter criteria.
*   **Collection:** (Logical Entity). Key Fields: Set of WARC/ARC files, institution, crawl seed, time interval.

## Non-Functional Requirements
1.  **Scalability:** Tools must process large collections, support multiple files simultaneously, and allow for distributed processing.
2.  **Performance:** Implementation must prioritize performance for I/O-bound operations on large datasets.
3.  **Usability & Integration:** Tools must provide command-line interfaces, scriptable wrappers, logging, and comply with Java/web service environments.
4.  **Configurability:** Migration workflow and tool operations (like repackaging filters) must be highly configurable.
5.  **Technology Independence:** Avoid unnecessary technology dependencies and partner-specific integrations.
6.  **Verifiability:** Migration process must include validation mechanisms and support "dry-run" simulations.

## Milestones and External Dependencies
1.  Completion of collaborative requirements gathering with IIPC institutions.
2.  Delivery of the core Migration Application (including configuration, tool, validation, and console).
3.  Delivery of the Repackaging, Reporting, and Quality Assurance tools.
4.  Delivery of the Enhanced WARC Browser with search integration.
5.  Successful deployment and acceptance testing within participating IIPC institutions.
6.  *(External Dependency)*: Availability of test ARC data from institutions like BnF and BL.

## Risks and Mitigation Strategies
1.  **Risk:** Scope creep from additional institutional requirements. **Mitigation:** Flag out-of-scope requests; require descoping or additional funding.
2.  **Risk:** Complexity in distributed processing for large-scale migration. **Mitigation:** Use simple messaging infrastructure and avoid complex APIs like Hadoop where possible.
3.  **Risk:** Performance bottlenecks when processing billions of records. **Mitigation:** Design tools for minimal memory usage and atomic operations, following UNIX philosophy.
4.  **Risk:** Insufficient or delayed feedback from participating institutions. **Mitigation:** Proactive project management and clear communication channels.
5.  **Risk:** Integration challenges with external tools (e.g., ClamAV, JHOVE). **Mitigation:** Design flexible APIs and confirm tool compatibility early.

## Undecided Issues
1.  The specific form of contribution from the Swedish National Library.
2.  Final, detailed non-functional requirements concerning the scale of migration operations.
3.  Default metadata to be included during migration, pending input from IIPC members (NFR 13).
4.  The precise implementation strategy for the distributed processing/messaging infrastructure.
5.  Selection and integration details for external tools for format identification (FR 9) and virus scanning (FR 8).
6.  The exact mechanisms and rules for server-side rewriting in the enhanced WARC browser (FR 33).