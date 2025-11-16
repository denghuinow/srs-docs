# Clarus Weather System Design - Detailed System Requirements Specification

## 1. Introduction

The Clarus Initiative is a U.S. Department of Transportation sponsored program to organize and enhance environmental and road condition observation capabilities for surface transportation. The system aims to collect, quality check, and make available surface transportation weather and road condition observations to improve safety and mobility on all roads.

## 2. System Overview

### 2.1 Purpose and Scope
Clarus represents a "network of networks" for surface transportation environmental data, interconnecting weather data collection networks similar to how the Internet connects computer networks. The system focuses on four primary motivations:
1. Enhance productivity of transportation agencies in maintaining safety and mobility
2. Extend existing weather data sources for general purpose forecasting
3. Support real-time operational responses to weather
4. Enhance atmospheric boundary layer predictions for more accurate forecasts

### 2.2 System Components
The Clarus system architecture consists of:
- **Collector Services (CS)**: Receive environmental data from various sources and convert to standard format
- **Quality Checking Services (QChS)**: Apply multiple algorithms to validate data quality
- **Qualified Environmental Data Cache (QEDC)**: Store quality-checked environmental data
- **Qualified Environmental Data Services (QEDS)**: Format and disseminate data to service providers
- **Environmental Metadata Cache (EMC)**: Store metadata about contributors and collectors
- **Environmental Metadata Services (EMS)**: Format and disseminate metadata
- **Configuration & Administration Service (CAS)**: Manage system configuration, quality rules, and data sharing restrictions
- **Watchdog (DOG)**: Monitor system state and restart unresponsive services
- **Schedule Service (SS)**: Prioritize data collection and dissemination requests

## 3. Functional Requirements

### 3.1 Data Collection
- Collect in-situ environmental observations from data collectors (F-201)
- Access remotely sensed environmental observations (F-205)
- Receive roadway weather measurements derived from VII data (F-211)
- Accept environmental data derived from images including CCTV and still images (F-214)
- Retrieve data directly from environmental sensor station collectors (F-221)
- Accept data from railway systems and in-situ ESS along tracks (F-241)
- Accept data from railroad, roadway, maintenance, construction, service patrol, transit, and emergency vehicles (F-245-F-275)
- Receive weather data from weather service providers (F-281)
- Process data as received (F-223)
- Collect pavement-related observations (F-231)

### 3.2 Quality Checking
- Implement quality checking processes as soon as data become available (F-101)
- Provide environmental data quality flags (F-111)
- Allow human quality checks of environmental data (F-141)
- Implement quality checking rules for each environmental parameter (F-155)
- Implement quality checking rules for specific environmental situations (F-161)
- Implement quality checking rules specific to observation locations (F-163)
- Base quality checking process on historical environmental data (F-171)
- Use multiple algorithms for quality checking process (F-175)
- Detect out of range values using sensor range and climate records (F-121)
- Not modify original observations (F-125)
- Record methods applied when deriving quality checking information (F-151)
- Base quality checking on values from multiple observations (F-165)
- Base quality checking on values distributed in time (F-166)
- Implement spatial tests using available data (F-162)

### 3.3 Data Dissemination
- Disseminate data in response to scheduled requests (D-051)
- Disseminate environmental data in response to polling (D-061)
- Disseminate data in response to change notification requests (D-071)
- Notify subscribers when datasets become available (D-081)
- Disseminate data using standard Internet protocols (D-091)
- Provide notification of data quality conditions to data contributors (F-115)
- Enable quality managers to review which quality checks passed or failed (F-140)
- Disseminate NWS watches, warnings, and advisories (F-219)
- Restrict environmental data publication based on source (F-811)
- Disseminate data based on spatial queries (F-505)

### 3.4 Metadata Management
- Acquire, process, and disseminate environmental metadata (H-120)
- Provide sensor equipment metadata in response to requests (F-401)
- Manage contributor and collector metadata (H-120B1-B2)
- Store collector metadata based on TMDD & MS/ETMCC standards (I-017E1)

### 3.5 System Administration
- Configure schedules for executing quality checking services (F-101B1)
- Configure quality checking rules for environmental parameters (F-155B1)
- Enable administrators to manage quality checking rules (F-155B2)
- Configure quality checking rules for specific situations (F-161B1)
- Configure quality checking rules for observation locations (F-163B1)
- Configure historical environmental data for quality checking (F-171B1)
- Configure multiple algorithms for quality checking (F-175B1)
- Allow new observation types as they become available (F-213)
- Enable administrators to manage security groups (F-806)
- Record data sharing restrictions (F-811B1)
- Record system operation statistics (F-901)
- Log data transactions (F-905)
- Manage environmental data collection schedules (H-120B4)
- Manage quality checking schedules (H-120B3)
- Manage data sharing rules based on contributor agreements (I-032B1)

## 4. Data Standards and Interfaces

### 4.1 Data Standards
- Baseline data types defined by NTCIP ESS 1204 standard (H-011)
- Data definitions consistent with ITE TM 1.03 standard (H-012)
- Accept only observations with location, timestamp, and source metadata (H-151)
- Accept only observations of identified measurement types and units (H-155)
- Use Coordinated Universal Time (UTC) for all timestamps (D-126)
- Use latitude, longitude, and elevation coordinates to specify location (D-121)

### 4.2 Communication Standards
- Accept data through Clarus standard interface (I-011)
- Communicate with environmental sensor stations through NTCIP ESS 1204 (I-012)
- Communicate with RWIS databases through native interfaces (I-013)
- Transfer data efficiently using concurrent methods (I-016)
- Employ industry standards to minimize implementation impact (I-017)
- Extract data from XML, comma separated values, CMML, and netCDF messages (I-017D1-D6)

## 5. Performance Requirements

### 5.1 Capacity and Performance
- Support 470 million current observations (P-013)
- Respond to requests for information within one minute (P-025)
- Complete automated quality checking within ten seconds (P-023)
- Publish new data within twenty minutes of receipt (P-024)
- Handle three hundred simultaneous requests for environmental data (P-031)
- Support six thousand registered users (P-042)
- Support six hundred concurrent users (P-041)
- Publish data at three times the volume rate of collection (P-011)

### 5.2 Availability and Reliability
- Maintain continuous 24x7 operations (X-205)
- Provide uninterruptible power environment (X-207)
- Provide redundant communication (X-209)
- Mitigate communication denial-of-service attacks (Q-011)
- Respond to 95% of requests 95% of the time (Q-013)
- Automatically recover from unexpected shutdown (Q-012)
- Use redundant hardware (D-041)

## 6. Organizational Requirements

### 6.1 Program Management
- Establish data sharing agreements with all participating sources (X-201)
- Maintain continuous operations (X-205)
- Provide setup support (X-215)
- Provide customer service (X-221)
- Provide trained support staff (X-225)
- Define quality checking rules (X-232)
- Define data retention standards (X-233)
- Provide documentation of Clarus standards (X-235)
- Maintain comprehensive test environment (X-305)
- Test software and hardware changes before deployment (X-311, X-315)
- Operate according to IT Security Plan (X-601)
- Operate according to Government IT security requirements (X-605, X-611, X-615)

### 6.2 User Support
- Allow service providers to select specific desired datasets (I-021)
- Respond to queries for environmental data from available data (I-022)
- Enable environmental data queries by timestamp, location, quality, and source (I-025-I-028)
- Allow users to create data subscription requests (I-033)
- Alert users to system modifications (X-801)
- Enable weather service providers to use data for localized special weather products (X-805)
- Enable public agency personnel to obtain environmental conditions (X-811)
- Enable rail, traffic, transit, freight, and emergency personnel to obtain environmental conditions (X-815-X-827)

### 6.3 Data Management
- Maintain information about data providers (X-905)
- Maintain metadata about each data provider's network (X-910)
- Maintain information about data provider redistribution restrictions (X-915)
- Maintain information about service providers (X-921)
- Maintain information about service provider communications (X-925)
- Maintain information about service provider access to data (X-931)
- Allow potential data providers to request permission to submit information (X-935)
- Accept data only from sources with established data sharing agreements (X-101)
- Acquire, process, and disseminate data from across North America (H-301)
