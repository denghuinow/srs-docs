# 2005 - clarus h.md

## System Overview
The Clarus system is an initiative sponsored by the Federal Highway Administration (FHWA) to enhance environmental and road condition observation capabilities.^[1]^ It collects, quality controls, and disseminates surface transportation weather and road condition observations to improve safety and mobility.^[2]^

## Key Requirements

### Functional Requirements
- **Data Collection**: Access in-situ and remotely sensed environmental observations from various data collectors.^[3]^
- **Quality Control**: Implement continuous quality control processes and provide data quality flags.
- **Data Dissemination**: Disseminate data based on spatial queries and ensure minimal dissemination time.^[4]^
- **Data Management**: Maintain a dynamic library of data for at least seven days.^[5]^

### Performance Requirements
- **Data Volume**: Publish environmental data at three times the collection volume rate.^[6]^
- **Timeliness**: Collect data from sources within 5 minutes of availability and complete quality control checks within 10 seconds.^[7]^
- **User Capacity**: Support 600 concurrent users and handle 300 simultaneous data requests.^[8]^

### Organizational Requirements
- **Data Sharing Agreements**: Establish agreements with all participating data sources.^[9]^
- **Security**: Comply with Government IT security requirements, including uninterruptible power and redundant communication.
- **Operations**: Maintain 24x7 operations and provide network management tools.^[10]^

### Data Requirements
- **Baseline Data Types**: Defined by NTCIP ESS 1204 standard.^[11]^
- **Metadata**: Include location, timeframe, and source metadata for all observations.^[12]^
- **Data Types**: Acquire, process, and disseminate atmospheric, surface, and hydrologic data.^[13]^

### Interface Requirements
- **Standard Interface**: Accept data through a Clarus standard interface.^[14]^
- **Communication Protocols**: Use NTCIP ESS 1204 and other industry-standard protocols for data collection and dissemination.^[15]^
- **User Interface**: Provide a user interface for system administration and manage user privileges according to data sharing agreements.^[16]^