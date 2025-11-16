# Detailed Summary

## Background and Scope
The EVLA Correlator Backend System is a critical real-time astronomical data processing component positioned between the Correlator and End-to-End systems. Its primary functions include receiving correlator lag data, assembling time series, performing Fourier Transforms, applying user-selected processing, and delivering formatted spectra to the archive system. Non-goals include combining spectra from different sub-bands ("stitching") and direct user interface development.

## Role Matrix and Use Cases
- **Array Operator**: Receives status/error messages via Monitor & Control system
- **Engineers/Technicians**: Perform maintenance and diagnostics using remote tools
- **Astronomer/Scientist**: Selects additional data processing parameters
- **Software Developer**: Troubleshoots and maintains system remotely
- **Administrator**: Has unrestricted system access and user management privileges
- **Web User**: Limited authorized access to restricted areas

## Business Process
**Main Process (Real-time Data Pipeline):**
1. Receive lag frames from Correlator via high-speed network
2. Verify data receipt and check for errors
3. Assemble lag frames into complete time series
4. Apply normalization and corrections (VanVleck, timestamp adjustment)
5. Perform Fourier Transform and optional processing
6. Integrate spectra based on observational parameters
7. Format output with metadata for e2e system
8. Transfer and verify delivery to archive

**Key Branches:**
- **Error Handling**: Detect corruption → flag data → apply zero values → continue processing
- **System Recovery**: Monitor components → detect failure → attempt auto-correction → report status

## Domain Model
- **Lag Frame** (frame_id, lag_values[128], metadata, required)
- **Lag Set** (set_id, assembled_lags[262144], baseline_id, required)
- **Time Series** (series_id, normalized_data, timestamp, required)
- **Spectrum** (spectrum_id, frequency_data, integration_count, required)
- **Processing Parameters** (param_id, process_sequence, user_selections, required)
- **Error Report** (error_id, error_number, source, timestamp, required)
- **Metadata** (meta_id, coordinates, processes_applied, invalid_flags, required)
- **User Account** (user_id, username, access_level, password(encrypted), required/unique)

## Interfaces and Integrations
- **Correlator System** (Inbound): Lag frames via UDP/IP • Input: Lag values, auxiliary data • Output: Receipt verification • SLA: 1.6 GB/s initial throughput
- **Monitor & Control System** (Bidirectional): Commands and status • Input: Observational mode, processing parameters • Output: Error reports, operational status • SLA: Real-time synchronization
- **End-to-End System** (Outbound): Formatted spectra • Input: Processed data with metadata • Output: AIPS++ Measurement Sets • SLA: 25 MB/s initial throughput
- **Internal Network** (Bidirectional): Inter-processor communication • Input/Output: Data redistribution, workload management • SLA: Maintain real-time processing

## Acceptance Criteria
- **Data Processing**: Given valid lag frames, When assembled and transformed, Then produce correct spectra with preserved dynamic range
- **Error Handling**: Given corrupted input data, When detected during processing, Then flag affected segments and continue operation
- **System Recovery**: Given processor failure, When detected by monitoring, Then redistribute workload and report failure
- **Output Delivery**: Given formatted spectra, When sent to e2e system, Then verify successful transfer and handle temporary outages

## Non-functional Metrics
- **Performance**: Minimum 1.6 GB/s input and 25 MB/s output throughput; Real-time processing with no data loss
- **Reliability**: Continuous operation between maintenance windows; Automatic failure detection and recovery
- **Security**: User authentication with encrypted passwords; Role-based access control
- **Compliance**: Reversible processing operations; Industry standard software practices
- **Observability**: Comprehensive monitoring of I/O rates, computation errors, and component status

## Milestones and Release Strategy
1. Hardware cluster configuration and network setup
2. Core data processing pipeline implementation
3. Integration with Correlator and M&C systems
4. End-to-end testing with simulated data
5. Security and access control implementation
6. Production deployment with incremental capability increases

## Risk List and Mitigation Strategies
- **Hardware Limitations**: Constrain throughput → Use scalable cluster architecture with expansion capability
- **Network Performance**: Critical for real-time operation → Implement high-speed dedicated networks with redundancy
- **Software Efficiency**: Impact on processing speed → Optimize code and use industry-standard compilers
- **Data Loss**: During system failures → Implement buffering and recovery mechanisms
- **Component Failure**: Single points of failure → Use redundant components and load distribution
- **Security Breaches**: Unauthorized access → Implement robust authentication and logging
- **Maintenance Downtime**: Service interruption → Design for partial system operation during maintenance
- **Scalability Limits**: Future expansion needs → Use modular design with transparent hardware upgrades

## Undecided Issues and Responsible Parties
- Memory requirements and access speeds (System Architects)
- Buffer sizes for bursting and outage recovery (Performance Team)
- Duration of e2e outage tolerance (Operations Team)
- Amount of correlator data to cache during M&C outages (System Designers)
- Specific time domain and frequency domain processes (Science Team)
- Diagnostic package requirements for third-party software (Development Team)
- Maximum lag set size beyond 262,144 (Not mentioned)
- Specific operating system selection (Not mentioned)