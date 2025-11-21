# Short Summary

- **Background and objectives**: The USDA-ARS is developing STEWARDS, a centralized data system to provide standardized, well-documented access to water, soil, management, and economic data from multiple research watersheds, supporting the Conservation Effects Assessment Project (CEAP) and broader research needs.

- **In scope**:
  - Centralized database management system for storage and management of diverse watershed data.
  - Web-based client application for data access, search, visualization, and download.
  - Support for biophysical, land use, management, and economic data types.
  - Metadata creation, storage, and querying compliant with federal standards.
  - Annual data updates from watershed sites after local quality assurance.

- **Out of scope**:
  - Real-time public data access; updates occur annually or less frequently.
  - Primary responsibility for data collection and quality assurance remains with local watershed teams.
  - No expansion to additional watersheds beyond the initial twelve CEAP Benchmark Watersheds in version 1.0.
  - Direct integration with agricultural models (e.g., SWAT, AnnAGNPS) for model execution.
  - Real-time data streaming from watershed sites.

- **Roles and core use cases**:
  - As a Watershed uploader, I want to upload local data to STEWARDS so that it is available in a standardized format for broader use.
  - As an ARS user, I want to search, visualize, and download watershed data so that I can conduct research and analysis.
  - As a Public user, I want to access public data without authentication so that I can utilize available watershed information.

- **Success metrics**:
  - System availability of 99% during operational hours.
  - Response time for metadata queries within a few seconds.
  - Successful annual data updates from all participating watersheds.

- **Major constraints**:
  - Use of current corporate standard Microsoft SQL Server database engine.
  - Compliance with USDA web style, accessibility, and security policies.
  - Data uploading may occur as infrequently as once per year.
  - Portability limitations due to specific system dependencies.
  - Adherence to ARS OCIO-provided hardware and software resources.

- **Undecided issues**:
  - Funding continuity beyond FY07.
  - Help desk staffing and funding model.
  - Specific performance thresholds for large data retrievals.
  - Conversion timeline if federal metadata standards change.
  - Not mentioned.