# Pontis 5.0 Bridge Management System – Short Summary

## Background and Objectives
Pontis 5.0 is the next-generation Bridge Management System (BMS) designed to replace the existing Pontis 4.x product line. Its primary objectives are to provide a technologically up-to-date, robust, and accessible tool for bridge data management, condition assessment, needs analysis, and program development while preserving existing agency investments.

## In Scope
*   Development of a Microsoft .NET application with both web-based (thin-client) and standalone (thick-client) components.
*   Core BMS functionalities: bridge inventory & inspection, preservation model development, program simulation, and project & program development.
*   Data exchange capabilities supporting NBI, PDI, and future TransXML schemas.
*   Integration with other BRIDGEWare products (e.g., Virtis/Opis) and GIS systems.
*   Enhanced system administration for user management, security, and application configuration.

## Out of Scope
*   Hosting the application as a service (designed for agency deployment).
*   Support for non-Microsoft browsers or non-.NET development frameworks.
*   Development of a new, unrelated database architecture (builds upon BRIDGEWare/Pontis 4.x design).
*   Full ADA/Section 508 compliance (status to be determined by AASHTO).
*   Mission-critical, uninterrupted operation design with built-in disaster recovery.

## Stakeholders and Core Use Cases
**Stakeholders:**
*   **Pontis Users:** Day-to-day users who initiate and review requirements.
*   **Pontis Task Force:** Oversees product quality, technical correctness, and project decisions.
*   **Technical Advisory Group (TAG):** Develops requirements, architecture, and implementation plans.
*   **BRIDGEWare Integration TAG:** Coordinates database design and integration impacts.
*   **AASHTO:** Owns the product, manages the project, and handles licensing.
*   **Contractor:** Responsible for software design and development.

**Core User Stories:**
1.  As an **Inspector**, I want to **create and edit bridge inspection data** so that **field-collected condition information is accurately recorded in the system**.
2.  As a **Bridge Management Engineer**, I want to **run program simulations** so that **I can forecast network-level preservation needs and budget requirements**.
3.  As a **Bridge Project Planner**, I want to **create and edit projects by assigning work recommendations** so that **I can develop and track capital improvement programs**.
4.  As a **System Administrator**, I want to **define user roles and manage application access** so that **system security and data integrity are maintained**.
5.  As a **Data Analyst**, I want to **browse, filter, and generate reports on bridge and project data** so that **I can monitor performance and support decision-making**.
6.  As a **Model Developer**, I want to **update preservation policy costs and deterioration probabilities** so that **the system's optimization models reflect current agency practices and data**.

## Success Metrics
*   Successful migration of existing Pontis 4.x databases and user-developed custom forms/reports to the new platform.
*   Achievement of target performance benchmarks (e.g., user login <2 seconds, displaying 250 bridges in 5-10 seconds).
*   High user satisfaction post-training, with routine users comfortable after two days and casual data viewers comfortable after two hours.

## Major Constraints
*   Must be developed using Microsoft technologies (.NET Framework, IIS, SQL Server/Oracle/Sybase databases).
*   The database design must be consistent with and approved by the BRIDGEWare Database TAG.
*   Must maintain functional consistency with Pontis 4.x to preserve agency investments, with deviations explicitly justified.
*   Must support both connected (office) and disconnected (field) operational environments.
*   Must accommodate potential future changes to Federal National Bridge Inventory (NBI) coding standards.

## Undecided Issues
*   The specific approach and level of compliance with ADA/Section 508 requirements.
*   Final selection of third-party .NET reporting tools to replace PowerBuilder/InfoMaker.
*   Implementation details for a single-sign-on (SSO) authentication mechanism across BRIDGEWare products.
*   The extent of support for handheld or tablet computers in field inspection.
*   Resolution of specific "may" requirements listed in the "Waiting Room" (Section 7.4), such as electronic signatures and advanced wizards.