# Detailed Summary: WARC Tools Phase III

## Background and Scope
This project aims to extend the existing WARC Tools suite to facilitate large-scale migration from the ARC to the WARC file format and provide enhanced tools for managing web archive collections. The core objectives are to build a migration application, repackaging tool, reporting application, quality assurance tool, and an enhanced WARC browser, fostering adoption within the International Internet Preservation Consortium (IIPC) community. Non-goals include developing functionality to handle hardware failures and creating partner-specific integration technologies.

## Stakeholders Matrix and Use Cases
*   **Hanzo Archives Limited (Project Lead):** Responsible for project management, requirements gathering, development, and deployment of the WARC Tools Phase III suite.
*   **IIPC Member Institutions (e.g., BnF, BL, Netarchive.dk):** Act as collaborative partners contributing to requirements specification, providing test data, and conducting acceptance testing in real-world environments.
*   **Crawl Engineers / Web Archivists (End Users):** Utilize the command-line tools and applications to migrate, validate, repackage, and analyze large collections of web archive files.
*   **Researchers (End Users):** Leverage the reporting and comparison tools to analyze and explore web archive content for research purposes.

**Main Scenarios:**
1.  An archivist configures and initiates a large-scale, distributed migration of ARC files to WARC format using the migration application.
2.  A user validates a completed migration by comparing checksums between original ARC and new WARC files, optionally using sampling.
3.  An engineer creates a subset of a WARC collection by repackaging files based on URL, MIME-type, or date filters.
4.  A researcher generates and exports summary reports (e.g., by MIME-type, hostname) from a collection of WARC files.
5.  A quality assurance analyst compares two crawls of the same seed to identify deltas and changes for crawl validation.

**Exception Scenarios:**
1.  A migration job encounters a corrupt ARC record; the tool skips it based on configuration and logs the error.
2.  A validation check fails due to a checksum mismatch, flagging a potential migration error for operator review.
3.  A repackaging operation is configured with a pre-operation filter that prevents certain records from being processed.

## Business Process
**Main Process: ARC to WARC Migration & Validation**
1.  **Trigger:** Archivist decides to migrate a collection of ARC files.
2.  **Input:** Collection of ARC files, migration configuration file.
3.  **Configure Migration:** Use web UI or scripts to define migration strategy, metadata, and external tool integrations (e.g., virus scanning).
4.  **Execute Migration:** Run `arc_warc_migrate` tool, potentially distributed across multiple machines, converting ARC records to WARC format with added metadata.
5.  **Monitor Progress:** Use console application to monitor migration job progress, logs, and statistics.
6.  **Validate Output:** Run `arc_warc_verify` tool to compare checksums between original ARC and new WARC files.
7.  **Generate Reports:** Use reporting tools to create summaries of the newly created WARC collection.
8.  **Output:** Validated collection of WARC files, migration logs, and summary reports.

**Key Branch A: Repackaging for Data Transfer**
1.  **Trigger:** Need to extract a subset of records for testing or sharing.
2.  **Input:** Source WARC files, filter criteria (URL, date, MIME-type).
3.  **Filter & Extract:** Run `warc_repackage` tool to select records based on criteria.
4.  **Output:** New, smaller WARC files containing only the filtered records and context metadata.

**Key Branch B: Quality Assurance Crawl Comparison**
1.  **Trigger:** Need to assess consistency between repeated crawls.
2.  **Input:** WARC files from two or more crawls of the same seed.
3.  **Compare:** Run `warc_compare` tool to analyze differences based on defined criteria.
4.  **Output:** Delta report and graphs highlighting changes between crawl sets.

## Domain Model
*   **ARC File:** (Original file; fields: filename, size, record offsets)
*   **WARC File:** (Target file; fields: filename, size, WARC-Record-ID [unique])
*   **Migration Job:** (fields: job ID [unique], configuration reference, status, start/end time)
*   **WARC Record:** (fields: record type, target URI, payload digest, Content-Type, timestamp [required])
*   **Migration Configuration:** (fields: config ID, settings for metadata, error handling, external tools)
*   **Validation Result:** (fields: associated job ID, check status, details of mismatches)
*   **Report:** (fields: report type, source collection, generated date, output format)
*   **Filter Criteria:** (Used for repackaging/QA; fields: type [URL, MIME, etc.], pattern/value)

## Interfaces and Integrations
*   **External ARC Reader (e.g., Heritrix arcreader):** Direction: Inbound; Interaction: Used by validation tool; Input: ARC file; Output: ARC record data; SLA: Must correctly parse ARC format.
*   **External File Identification Service (e.g., DROID, JHOVE):** Direction: Outbound; Interaction: Called during migration for format ID; Input: File payload; Output: Format identification metadata; SLA: Configurable timeout.
*   **External Virus Scanner (e.g., ClamAV):** Direction: Outbound; Interaction: Pre-migration scanning step; Input: File payload; Output: Clean/Malware flag; SLA: Critical for safety.
*   **Persistent ID Service (e.g., NOID, ARK):** Direction: Outbound; Interaction: Generate unique WARC-Record-IDs; Input: Record metadata; Output: Persistent identifier; SLA: Must be unique and opaque.
*   **WARC Browser Web UI:** Direction: Inbound/Outbound; Interaction: User interface for reports and browsing; Input: User requests; Output: HTML reports, file manifests; SLA: Responsive for summary display.
*   **Search Tools Module:** Direction: Integration; Interaction: Provides full-text search to WARC Browser; Input: WARC files; Output: Search index and query results; SLA: Indexing performance on large collections.

## Acceptance Criteria
**For Migration:**
*   Given a valid configuration file and a set of ARC files, when the `arc_warc_migrate` command is executed, then it should produce corresponding WARC files containing all records with user-specified metadata.
*   Given a completed migration, when the `arc_warc_verify` tool runs with checksum comparison, then it should report 100% match for all sampled records.

**For Repackaging:**
*   Given a set of WARC files and a URL filter pattern, when the `warc_repackage` command is run, then the output should only contain WARC records whose URLs match the filter.

**For Reporting:**
*   Given a directory of WARC files, when the `warc_summary` tool is executed with the mimetype report option, then it should output a breakdown of content types present in the collection.

## Non-Functional Metrics
*   **Performance:** Tools must process large collections with minimal memory usage (I/O bound). Support distributed processing across multiple machines.
*   **Reliability:** Migration process must include checkpoints for atomic transactions where possible. Tools must provide comprehensive logging.
*   **Security:** Integration with virus scanning tools (e.g., ClamAV) for pre-conversion file checking.
*   **Compliance:** Tools and outputs must comply with the WARC standard (ISO 28500). Implementation should avoid unnecessary technology dependencies.
*   **Observability:** Tools shall provide logging facilities to track command progression, duration, and output levels.

## Milestones and Release Strategy
1.  Finalize requirements specification with IIPC community feedback.
2.  Complete development of core migration application (tool, validation, console).
3.  Complete development of repackaging and reporting tools.
4.  Complete development of quality assurance tools (comparator) and WARC browser enhancements.
5.  Conduct internal testing and integration.
6.  Deploy release candidate to participating IIPC institutions for acceptance testing and final release as open-source software.

## Risk List and Mitigation Strategies
1.  **Risk:** Scope creep from diverse IIPC institution requirements. **Mitigation:** Flag out-of-scope requirements; institutions can descope or provide additional funding.
2.  **Risk:** Performance issues with extremely large-scale migrations (billions of URLs). **Mitigation:** Leverage distributed processing design and atomic, low-memory operations from libwarc.
3.  **Risk:** Complexity in integrating multiple external tools/services. **Mitigation:** Use a flexible, configuration-driven API to isolate dependencies.
4.  **Risk:** Insufficient testing in real-world environments. **Mitigation:** Engage IIPC institutions early for testing with their own data.
5.  **Risk:** Challenges in achieving accurate validation, especially for sampled checks. **Mitigation:** Implement multiple validation methods (checksum, metadata, round-trip).
6.  **Risk:** Dependency on external open-source projects (e.g., Search Tools). **Mitigation:** Plan for concurrent updates and close coordination with those projects.
7.  **Risk:** Ensuring usability for the target audience of crawl engineers and archivists. **Mitigation:** Provide shell script wrappers and comprehensive documentation.
8.  **Risk:** Project delays due to collaborative, distributed nature. **Mitigation:** Proactive project management and clear communication channels with all partners.

## Undecided Issues and Responsible Parties
1.  **Default metadata to include during migration.** (Responsible: IIPC members to provide requirements to Hanzo)
2.  **Specific external tools to be integrated for file format identification.** (Responsible: Hanzo, with IIPC input)
3.  **Final choice of persistent identifier service (NOID, ARK, UUID).** (Responsible: Hanzo, based on community practice)
4.  **Detailed sampling strategy for validation of very large collections.** (Responsible: Hanzo, to be refined during testing)
5.  **Specific graph types and visualizations for the QA comparator tool.** (Responsible: Hanzo, with IIPC user feedback)
6.  **Extent of server-side rewriting rules for the enhanced WARC browser.** (Responsible: Hanzo)
7.  **Form of contribution from the Swedish National Library.** (Responsible: Swedish NL to confirm)
8.  **Prioritization of post-migration reporting database features.** (Responsible: Hanzo, based on effort and value)