# Balanced Summary

## Goals and Scope
The Clarus system aims to collect, quality control, and disseminate surface transportation weather and road condition observations across North America. It serves as a "network of networks" to enhance safety, mobility, and weather forecasting capabilities. The scope includes atmospheric, pavement, and hydrologic data from various transportation sources.

## Roles and User Stories
- **Data Collector**: As a data collector, I want to submit environmental observations so that they can be shared and quality-controlled
- **Service Provider**: As a service provider, I want to access quality-controlled environmental data so that I can create value-added weather products
- **System Administrator**: As a system administrator, I want to manage user privileges and security groups so that data access complies with sharing agreements
- **Maintenance Personnel**: As maintenance personnel, I want to obtain environmental conditions so that I can make informed road treatment decisions
- **Research Community**: As a researcher, I want to access historical environmental data so that I can study surface transportation weather patterns

## Key Processes
1. **Data Collection Trigger**: Environmental data becomes available from autonomous layer sources
2. **Data Acquisition**: System collects observations from approved sources within 5 minutes of availability
3. **Quality Control**: Automated quality checks applied within 10 seconds of data receipt
4. **Data Processing**: System processes data as received and organizes by location/type
5. **Quality Flagging**: Quality flags added based on completeness of metadata and validation rules
6. **Data Publication**: Quality-controlled data published within 20 minutes of receipt
7. **Data Dissemination**: System responds to user queries and subscriptions within one minute

## Domain Data Elements
- **Environmental Observation** (Observation ID): timestamp, location, data type, measured value, quality flag
- **Sensor Station** (Station ID): location coordinates, sensor configuration, station category, metadata
- **Quality Control Rule** (Rule ID): parameter type, validation criteria, regional applicability, algorithm
- **Data Provider** (Provider ID): contact information, network details, sharing restrictions
- **User Account** (User ID): access privileges, subscription preferences, organization
- **Weather Hazard** (Hazard ID): hazard type, location, timeframe, severity

## Non-functional Requirements
- Support 600 concurrent users and 6,000 registered users
- Respond to 95% of data requests 95% of the time
- Operate 24x7 with redundant hardware and communications
- Use industry-standard interfaces and Internet protocols
- Implement security measures against denial-of-service attacks
- Maintain data for at least seven days in dynamic library

## Milestones and External Dependencies
- Establish data sharing agreements with participating sources
- Define quality control rules and validation criteria
- Implement NTCIP ESS 1204 standard for data collection
- Develop standardized interface protocols
- Coordinate with NOAA and National Weather Service

## Risks and Mitigation Strategies
- **Data Quality Variability**: Implement multiple quality control algorithms and regional rules
- **System Scalability**: Use modular components and distributed architecture
- **Participation Uncertainty**: Develop attractive value proposition for data providers
- **Security Threats**: Follow government IT security requirements and implement attack mitigation
- **Technical Integration**: Support both standard and native interfaces for legacy systems

## Undecided Issues
- Long-term data archiving strategy
- Regional boundary definitions
- Specific quality control algorithms
- Data retention standards beyond 7 days
- Criticality classification for operational support
- Not mentioned