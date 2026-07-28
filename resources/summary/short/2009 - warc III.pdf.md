# Short Summary: WARC Tools Phase III Functional Requirements Specification

## Background and Objectives
This document outlines the functional requirements for WARC Tools Phase III, a project aimed at extending the existing open-source toolset for managing web archive (WARC) files. The primary objective is to facilitate large-scale migration from the legacy ARC format to WARC, enhance tool capabilities for manipulation and analysis, and promote adoption within the web archiving community through collaboration with IIPC member institutions.

## In Scope
1.  Development of a Migration Application with configurable workflow, tools for ARC-to-WARC conversion, validation, and process monitoring.
2.  Creation of a Repackaging Tool to filter and extract records from WARC files into new collections.
3.  Implementation of a Reporting Application, including a summary tool and enhanced web browser integration for analyzing WARC content.
4.  Development of a Quality Assurance Tool for comparing WARC file sets from similar crawls.
5.  Enhancement of the existing WARC Browser with features like server-side rewriting, proxy mode, and integration of full-text search.

## Out of Scope
1.  Development of functionality for handling hardware failures within distributed processing.
2.  Implementation of partner-specific integration technologies.
3.  Expansion of the core `libwarc` library's fundamental architecture.
4.  Direct modification of external tools like JHOVE or DROID for file identification.
5.  Comprehensive, non-sampling-based validation for every record in extremely large collections by default.

## Stakeholders and Core Use Cases
*   **Hanzo Archives Limited (Project Lead):** Responsible for specification, development, project management, and deployment of the WARC Tools.
*   **International Internet Preservation Consortium (IIPC) Member Institutions (e.g., BnF, BL, Netarchive.dk):** Collaborate on requirements gathering, provide test data, and conduct acceptance testing in real-world settings.
*   **Crawl Engineers / Web Archivists:** Use the tools to manipulate, migrate, validate, and analyze web archive collections.
*   **Researchers:** Utilize the tools to explore, search, and repackage archived web content for study.

**User Stories:**
1.  As a **web archivist**, I want to **migrate a large collection of ARC files to the WARC format** so that **our archive complies with the modern standard and is preservable**.
2.  As a **crawl engineer**, I want to **validate that a migrated WARC collection's content matches the original ARC files** so that **I can ensure data integrity after conversion**.
3.  As a **researcher**, I want to **repackage a WARC collection by filtering records based on URL, date, or MIME-type** so that **I can create a focused dataset for analysis**.
4.  As an **archivist**, I want to **generate summary reports (e.g., by MIME-type, hostname) from a WARC collection** so that **I can understand its composition and scope**.
5.  As a **quality assurance analyst**, I want to **compare WARC files from two sequential crawls of the same seed** so that **I can identify significant changes and assess crawl consistency**.
6.  As an **end-user**, I want to **browse and perform full-text searches on a WARC collection via a web interface** so that **I can easily locate and access archived web content**.

## Success Metrics
1.  Successful deployment and use of the migration and validation tools by participating IIPC institutions on their test data.
2.  All developed tools meet the specified non-functional requirements for processing large-scale collections (e.g., handling multiple files, scalable performance).
3.  The enhanced toolset is released as stable, open-source software on the project's public code repository.

## Major Constraints
1.  Tools must avoid unnecessary technology dependencies and maintain compatibility with existing Java environments and web service APIs.
2.  Implementation must follow the UNIX philosophy of simple, scriptable command-line tools that operate with minimal memory usage.
3.  Project scope is fixed to the baseline; requirements from institutions that exceed it require additional funding or descoping.
4.  The migration workflow must support configurable integration with external tools and services (e.g., for virus scanning, format identification).
5.  Tools must provide logging facilities and the ability to operate on selected collection subsets (e.g., by name, random sample).

## Undecided Issues
1.  The specific form of contribution from the Swedish National Library (NL) is to be confirmed.
2.  The final list of default metadata to be included during migration requires input from IIPC members (NFR 13).
3.  The detailed non-functional requirements concerning the scale of migration need to be developed alongside functional specs.
4.  The exact mechanisms for the "dry-run migration" simulation are defined by configuration and may evolve.
5.  Specific external tools or services for generating preservation metadata will be identified during configuration strategy development.