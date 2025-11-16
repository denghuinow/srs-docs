# WARC Tools Phase III Functional Requirements Specification

## Introduction

### Background
The WARC Tools project facilitates adoption of the WARC file format for storing web archives by providing an open source software library, command line tools, web server plug-ins, and technical documentation for manipulation and management of WARC files.

### WARC Tools Phase I and II
Delivered a core software library called "libwarc" and a set of end user command line tools, extensions to existing tools, and simple web applications for accessing WARC content. All libraries have APIs and dynamic language bindings, making them scriptable and programmable.

### WARC Tools Phase III
Builds upon original libwarc, extending the collection of WARC Tools and implementing a full migration application. Includes community participation in specification of tools and applications from International Internet Preservation Consortium (IIPC) member institutions.

### Outline Approach
WARC Tools Phase III will specify, build, test and deploy:
1. Migration Application
2. Repackaging Tool
3. Reporting Application
4. Quality Assurance Tool
5. Enhanced WARC Browser

Additional tasks include collaborative requirements gathering, libwarc maintenance, project management, and deployment within participating institutions.

## Specification

### Default Behaviours
NFR 1: Tools shall process multiple WARC files simultaneously with options for explicit naming, wildcard matching, size limitation, and item count grouping.

NFR 2: Tools shall scale to process large collections using distributed processing and data transport.

NFR 3: Tools shall offer best possible performance for processing large collections (I/O bound).

NFR 4: Tools shall run on multiple machines without hardware failure handling functionality.

NFR 5: Implementation shall avoid unnecessary technology dependencies and partner-specific integration technologies.

NFR 6: Tools shall be compliant with Java development environments using web services and RESTful APIs.

NFR 7: Tools shall provide logging facilities for command progression tracking.

NFR 8: Tools shall provide enhanced usability with easy-to-adapt shell script wrappers.

NFR 9: Tools shall operate in modes restricting effects to selected collection subsets.

### Migration Application
Provides workflow to support and manage arc → warc migration process with verification functionality to check and validate by content and metadata.

NFR 10: Workflow system shall have configurable management strategy for migration from ARCs to WARCs.

NFR 11: Migration workflow system will be driven by command line tools and scripts.

NFR 11.1: Migration configurations can be built with a Web User Interface.

NFR 11.2: Active migrations can be monitored, paused, and restarted with a Web User Interface console.

NFR 12: Pre and post conversion actions will be provided at record, WARC, and job levels.

NFR 13: IIPC members should provide default METADATA they want included for migration.

NFR 14: Deduplication may be run before migration inside a batch process.

#### Migration Tool
Command: `arc_warc_migrate <ARC_FILES> <CONFIG> [options]`

FR 1: Migration workflow shall provide a clear Application Programming Interface (API) to handle the migration process and default configuration.

FR 2: Migration API will require inclusion of only one header file.

FR 3: Configuration must be provided explicitly; errors should be generated in the absence of a configuration.

FR 4: User shall provide metadata related to conversion stored in converted files (institution, context, crawler, collection name, etc.).

FR 5: Automatically generated migration metadata can be stored in converted files (OS/Kernel type, original ARC name, ARC size, ARC digests, conversion timestamp, ARC record offset, etc.).

FR 6: Migration workflow shall call external tools and services (database queries, shell commands, web services).

FR 7: Migration process shall use persistent, opaque, unique, and global identifiers for records access (Noid, ARK, UUID).

FR 8: Default external tool (e.g., ClamAV) will scan files before conversion (pre-conversion step).

FR 9: API should be flexible enough to allow external tools such as JHOVE, DROID for file format identification.

FR 10: ARC to WARC migration should run on multiple machines that are easy to deploy using simple messaging infrastructure.

FR 11: Logging during migration may be turned on/off at any time.

FR 12: Software checkpoints may be added during processing for managing atomic transactions.

FR 13: "Dry-run migration" shall be possible to generate reports without writing real WARC data.

FR 14: Duplicate detection shall find and report WARC records with same checksums using centralized database.

#### Validation Tool
Command: `arc_warc_verify <ARCFILE> <WARCFILE> <USER_DEFINED_ARC_READER> [options]`

FR 15: Validation uses METADATA in newly generated WARC files to match records with corresponding ARC files.

FR 15.1: Core validation shall use payload checksum comparisons.

FR 16: Sampling will be provided where applicable to quickly validate conversions.

FR 17: Validation shall use Heritrix's arcreader to double check original ARC record was correctly converted to WARC.

FR 18: Round trip validation shall be possible by migrating newly created WARC file back to ARC and comparing checksums.

### Repackaging Tool
Command: `warc_repackage -i <WARC_FILE> <WARC_PATTERN> [options]`

FR 19: Repackage WARC files by filtering records based on URL (regular expressions).

FR 20: Repackage WARC files by filtering records based on MIME-Types.

FR 21: Repackage WARC files by filtering records based on size.

FR 22: Repackage WARC files by filtering records based on timestamp (dates interval).

FR 23: Repackage WARC files by filtering on any field in the WARC specification.

FR 24: Repackaging allows pre and post record, file and job operations.

FR 24.1: Pre operation can prevent a file or record being processed by returning value.

FR 25: Each repackaged WARC file shall include user-defined METADATA record describing extraction context.

### Reporting Application

#### WARC Summary Tool
Command: `warc_summary WARC_FILES [options]`

FR 26: Migration framework shall provide tools to build reports from WARC files.

FR 27: Export summaries in various formats (XML, CSV).

NFR 16: Repackaging filters can be used by the summary module.

#### WARC Browser Integration
FR 28: Enhance WARC browser to display aggregated WARCs summaries in its UI.

FR 29: Enhance WARC browser to display a manifest of WARC files and their locations.

### Quality Assurance Tool

#### WARC Comparator
Command: `warc_compare <CRAWL_1_WARC_FILES> ... <CRAWL_N_WARC_FILES> [options]`

FR 30: Provide 'diff' tool to compare WARC sets based on defined criteria (timestamp, hostname, etc.).

FR 31: Provide tool to draw difference graphs between WARC collections.

FR 32: Provide way to view crawls deltas for quality assurance.

### Enhanced WARC Browser
FR 33: Implement WARC browser server side rewriting.

FR 34: Integrate a proxy mode inside the WARC browser.

FR 35: Integrate full-text search (search-tools project) module with WARC browser to provide users with WARC indexing/searching capabilities.
