# Balanced Summary

## Goals and Scope
STEWARDS is a centralized data system designed to organize, document, and provide one-point access to water, soil, management, and economic data from USDA-ARS research watersheds. It supports the Conservation Effects Assessment Project (CEAP) by enabling multi-site analyses and assessment of conservation practices. The system stores diverse data types including biophysical measurements, land use information, and modeling results, with annual updates from watershed sites after local quality assurance.

## Roles and User Stories
- **System Operator**: I want to maintain executable code so that the system remains functional and up-to-date.
- **Data Operations Manager**: I want to archive and maintain data so that data integrity and availability are ensured.
- **Watershed Uploader**: I want to upload local data to allocated space so that it becomes accessible through the central system.
- **ARS User**: I want to search and download watershed data so that I can use it for research purposes.
- **Public User**: I want to access public data without authentication so that I can review approved datasets for general use.

## Key Processes
1. **Trigger: Annual schedule** – Watershed staff perform local quality assurance on collected data.
2. Data is reformatted to match STEWARDS schema using translation filters.
3. Reformatted data and metadata are uploaded to the central database.
4. **Trigger: User request** – Users browse or query data via web interface.
5. System retrieves and displays data in tabular, chart, or spatial formats.
6. Users select data for visualization or download in standardized formats.
7. **Trigger: Download request** – Data is packaged and delivered via direct download or FTP.

## Domain Data Elements
- **Watershed**: WatershedID, Name, Location, Area, LandUse
- **Site**: SiteID, WatershedID, Description, Coordinates, Elevation
- **Climate_Data**: DataID, SiteID, Date, MinTemperature, MaxTemperature, Precipitation
- **Water_Quality**: SampleID, SiteID, DateTime, Parameter, Value, Unit
- **Metadata**: MetadataID, DatasetID, Standard, Abstract, Contact
- **Spatial_Layer**: LayerID, WatershedID, Type, Format, Extent

## Non-functional Requirements
- System must support common web browsers (IE, Netscape, Firefox).
- Response time for metadata queries should be a few seconds.
- Data and application backups must be performed week-nightly.
- System availability must be 99% during intended operational periods.
- Must comply with USDA web style and accessibility policies.
- Must use corporate standard Microsoft SQL Server database.

## Milestones and External Dependencies
- Initial population of database with historical watershed data.
- Development of data translation filters for each watershed.
- Annual data updates from watershed sites.
- Availability of operational platform at ARS OCIO.
- Continued funding from NRCS through FY07.

## Risks and Mitigation Strategies
- **Risk**: Watershed sites lack resources for data preparation.  
  **Mitigation**: Identify minimal CEAP data requirements and provide additional support.
- **Risk**: Funding shortfalls from NRCS.  
  **Mitigation**: Use base funds with adjusted timelines.
- **Risk**: Database design requires modification after deployment.  
  **Mitigation**: Design with flexibility for future changes.
- **Risk**: Portability issues when moving between operating systems.  
  **Mitigation**: Implement server-side applications where possible.
- **Risk**: Data loss during transmission.  
  **Mitigation**: Monitor failures and repeat upload process.

## Undecided Issues
- Specific hardware storage capacity requirements.
- Load balancing implementation details (fail-over vs session-managed).
- Selection of metadata input tool.
- Timeline for public data release.
- Help desk staffing and funding allocation.
- Conversion timeline if ISO 19115 metadata standard is adopted.