# Balanced Summary

**Goals and Scope**
The EVLA Correlator Backend System is a critical real-time astronomical data processing pipeline component. It receives correlator lag data, performs assembly, Fourier transforms, and optional processing, then delivers formatted spectra to the End-to-End archive system. The system operates on a distributed processor cluster with high-speed network interfaces.

**Roles and User Stories**
- *Array Operator*: I want automated status/error reporting through Monitor & Control so that array operations can be monitored continuously
- *Astronomer/Scientist*: I want to select additional data processing parameters so that scientific analysis requirements are met
- *Engineer/Technician*: I want remote diagnostic tools so that system faults can be rapidly identified and repaired
- *Software Developer*: I want remote system access so that troubleshooting can occur during non-working hours
- *Administrator*: I want user privilege management so that system security can be maintained

**Key Processes**
1. *Trigger: Correlator data arrival* → Receive lag frames from correlator via high-speed network
2. Verify data receipt completeness and check for errors
3. Assemble lag frames into properly ordered time series
4. Apply Fourier transforms and user-selected processing operations
5. Format results with metadata for End-to-End system compatibility
6. *Trigger: Processing completion* → Transfer formatted spectra to archive system
7. Monitor system components and perform automatic error recovery

**Domain Data Elements**
- *Lag Frame* (Frame ID, lag values, timestamp, baseline ID, metadata)
- *Time Series* (Series ID, assembled lag values, validity flags, processing state)
- *Spectrum* (Spectrum ID, frequency data, integration count, metadata, quality flags)
- *Processing Parameters* (Parameter ID, process type, values, sequence position)
- *Error Report* (Error ID, source, timestamp, statistics, message)
- *User Account* (User ID, privileges, access level, authentication)

**Non-functional Requirements**
- Real-time processing with 1.6 GB/sec input and 25 MB/sec output capacity
- Hardware/software reliability for continuous operation between maintenance windows
- Modular scalability to handle future 2 GB/sec per channel data rates
- Secure user authentication and privilege-based access control
- Reversible data processing maintaining original data recoverability
- Industry-standard software components with source code availability

**Milestones and External Dependencies**
- Initial deployment meeting specified throughput requirements
- Integration with Correlator Monitor and Control System
- Compatibility with AIPS++ Measurement Set format for archive
- Hardware cluster configuration and network infrastructure
- EVLA observational mode parameter synchronization

**Risks and Mitigation Strategies**
- *Hardware failure*: Implement redundant components and automatic failover
- *Data overflow*: Provide memory/disk buffering with overflow detection
- *Network disruption*: Cache data during outages and verify delivery
- *Processing delays*: Monitor performance and redistribute workload
- *Software errors*: Include debugging capabilities and graceful error handling

**Undecided Issues**
- Specific amounts for memory requirements and excess storage
- Duration thresholds for temporary e2e system outages
- Quantification of cached data during M&C system unavailability
- Exact delay specifications for standby mode resumption
- Complete list of user-selectable time/frequency domain processes
- Not mentioned: Final hardware vendor selections and specific network protocols