# Short Summary: Grid-BGC Application Version 1.0

## Background and Objectives
This project aims to develop a grid-based software infrastructure to support biogeochemical (BGC) modeling, utilizing the Daymet surface weather interpolation engine and the Biome-BGC model. The system will provide a graphical user interface and leverage grid technologies for secure, reliable access to remote computing resources.

## In Scope
*   A web portal for managing input data, running simulations (Daymet and Biome-BGC), visualizing results, and managing output data.
*   User account management integrated with NCAR Gatekeeper, including roles for Scientists and Portal Administrators.
*   Data organization through reusable "Objects" (e.g., Surface Observation, DEM) and simulation "Projects" that group objects.
*   Support for creating, sharing, and templating various data objects and running model simulations on specified computational resources.
*   Basic portal administration functions for user management, job monitoring, and system metrics.

## Out of Scope
*   Detailed implementation of visualization projects for Daymet and BiomeBGC output.
*   Implementation of a dedicated evaluation project for post-processing analysis.
*   Support for user roles and functionality for "Data Users" (lowest priority).
*   Implementation of resource quotas for users (lowest priority).
*   Native data format conversion for downloads; data is downloadable in system formats only.

## Stakeholders and Core Use Cases
*   **Scientists (Primary Users)**: Researchers who use the system to manage data, run simulations, and analyze results.
*   **Portal Administrator**: Responsible for managing user accounts, monitoring system operations, and handling administrative tasks.
*   **Data Users (Low Priority)**: Researchers who need to access and use simulation output data but do not run simulations themselves.

**User Stories:**
1.  As a Scientist, I want to create and configure a Daymet modeling project so that I can generate gridded surface weather datasets.
2.  As a Scientist, I want to initiate and monitor a Biome-BGC model run so that I can perform biogeochemical simulations.
3.  As a Scientist, I want to download the output data from my completed model runs so that I can perform further external analysis.
4.  As a Scientist, I want to share my data objects with specific colleagues so that we can collaborate on projects.
5.  As a Portal Administrator, I want to approve or reject new user account applications so that I can control system access.
6.  As a Portal Administrator, I want to view and manage currently running user jobs so that I can ensure system stability and assist users.

## Success Metrics
*   Successful execution and completion of Daymet and Biome-BGC modeling runs via the portal.
*   Effective data sharing and collaboration between scientists using the shared object system.
*   Reliable administrative control over user accounts and system resources as measured by portal metrics.

## Major Constraints
*   The system must use the Globus toolkit for grid communications.
*   All file-based storage must utilize the NCAR Mass Storage System (MSS).
*   The web portal must integrate into the existing NCAR Dataportal Web Server.
*   The system must comply with all NCAR security policies and constraints.
*   User authentication is dependent on the external NCAR Gatekeeper account system.

## Undecided Issues
*   The specific mechanism for user access to the NCAR Mass Storage System (MSS) – using user credentials or a proxy account.
*   The detailed workflow for handling "invalidated" objects and projects when dependencies change.
*   The full set of configurable system settings available to the Portal Administrator.
*   The specific file formats and archive structures required for various data uploads (e.g., for Surface Observation Objects).
*   The implementation details for data subsetting and extraction operations.