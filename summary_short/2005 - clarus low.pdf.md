# Short Summary

- **Background and objectives**: The Clarus Initiative, sponsored by the U.S. DOT, aims to collect, quality-check, and disseminate surface transportation weather and road condition observations to enhance safety, mobility, and forecasting accuracy across North America.

- **In scope**:
  - Collecting atmospheric, pavement, and hydrologic environmental data.
  - Implementing automated and manual quality checking processes.
  - Disseminating qualified environmental data and metadata to service providers.
  - Supporting data from various sources, including ESS, vehicles, and railways.
  - Managing data sharing agreements and access restrictions.

- **Out of scope**:
  - Archiving large volumes of environmental data long-term.
  - Developing value-added decision support tools (part of Clarus Initiative, not system).
  - Replacing existing critical operational systems.
  - Defining regional boundaries for data consumers.
  - Accepting data without location, timestamp, or source metadata.

- **Roles and core use cases**:
  - As a **data contributor**, I want to submit environmental data so that it can be quality-checked and shared under agreed terms.
  - As a **service provider**, I want to access qualified environmental data so that I can create value-added weather products.
  - As a **system administrator**, I want to configure quality rules and manage access so that the system operates securely and efficiently.

- **Success metrics**:
  - Respond to environmental data requests within one minute.
  - Complete automated quality checks within ten seconds of data receipt.
  - Publish new data within twenty minutes of receipt.

- **Major constraints**:
  - System must use open, standards-based interfaces (e.g., NTCIP 1204).
  - Data must include location, timestamp, and source metadata.
  - System must support 600 concurrent users and 6,000 registered users.
  - All timestamps must use Coordinated Universal Time (UTC).
  - System must operate 24x7 with redundant communications and power.

- **Undecided issues**:
  - Long-term data archiving strategy.
  - Specific regional boundaries for data queries.
  - Integration with external archiving systems.
  - Handling of data from sources without standard metadata.
  - Not mentioned: Future expansion to non-North American data sources.