Purpose & Scope  
This system enables migration of web archive collections from ARC to WARC format, with validation and repackaging capabilities. It excludes handling hardware failures and does not provide custom integration technologies.  

Product Background / Positioning  
Builds on prior WARC Tools phases (libwarc, command-line tools) and integrates with IIPC member institutions’ workflows. Serves as the foundation for community-driven web archive management, extending existing open-source tools.  

Core Functional Overview  
1. Migration Application: Configurable workflow for ARC-to-WARC conversion with metadata handling.  
2. Validation Tool: Content and metadata verification against source ARC files.  
3. Repackaging Tool: Filter WARC records by URL, MIME-type, size, or timestamp.  
4. Reporting Application: Generate summaries (mimetypes, status codes, hostnames) from WARC collections.  
5. Quality Assurance Tool: Compare WARC sets to identify crawl deltas and changes.  

Key Users & Usage Scenarios  
Primary users are web archivists from IIPC institutions (BL, BnF, Netarchive.dk). BL and BnF contribute to requirements and testing; others provide test data. Scenarios include large-scale migration, validation, and reporting on archived collections.  

Major External Interfaces  
Web UI for migration configuration (NFR 11.1), command-line interfaces for all tools, and integration with Search Tools for full-text indexing.  

Key Non-functional Requirements  
- Scale to process millions of ARC files via distributed processing (NFR 2).  
- Optimize I/O-bound performance for large collections (NFR 3).  
- Comply with Java environments using RESTful APIs (NFR 6).  
- Deduplicate records pre-migration using checksums (NFR 14).  
- Exclude hardware failure handling (NFR 4).  

Constraints, Assumptions & Dependencies  
Institutional test data (ARC/WARC) required from IIPC members. Migration metadata defaults must be provided by IIPC (NFR 13). No scope for partner-specific integrations (NFR 5).  

Priorities & Acceptance Approach  
Core priority: Migration workflow and validation. Acceptance driven by IIPC institution testing in real-world environments, with requirements validated against their data.