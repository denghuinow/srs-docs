# Detailed Summary: EVLA Correlator Backend System

## Background and Scope
The EVLA Correlator Backend System is a critical real-time astronomical data processing pipeline component for the Very Large Array Expansion Project. It receives raw lag data from the Correlator, performs assembly, Fourier transforms, and optional processing, then delivers formatted spectra to the End-to-End archive system. The system must operate on a distributed processor cluster with high-speed networks. Non-goals include direct user interfaces (all interaction is via Monitor & Control) and combining spectra from different sub-bands ("stitching").

## Stakeholders Matrix and Use Cases
*   **Array Operator**: Monitors system status and error messages via the Monitor & Control System to ensure continuous astronomical observations.
*   **Engineers and Technicians**: Perform corrective/preventive maintenance and remote diagnostics to ensure hardware and software reliability.
*   **Astronomer/Scientist**: Selects and provides parameters for optional data processing steps beyond the core Fourier transforms.
*   **Software Developer**: Develops, troubleshoots, and maintains system software, requiring remote access for support.
*   **Web User (Authorized)**: Has restricted access to typically off-limits parts of the system for specific oversight or support tasks.

**Main Scenarios**: 1) Real-time data reception and processing pipeline execution. 2) User requests optional time/frequency domain processing. 3) System detects and reports a hardware/software fault. 4) Administrator performs user access management.
**Exception Scenarios**: 1) Temporary loss of connection to the End-to-End archive. 2) Correlator input data stream is interrupted. 3) Critical auxiliary data from Monitor & Control becomes unavailable. 4) Computational error (e.g., NaN, overflow) is detected during processing.

## Business Process
**Main Process: Real-Time Data Processing Pipeline**
1.  **Trigger**: Correlator begins sending lag frame data packets.
2.  Receive and verify lag frames from the Correlator input network.
3.  Assemble lag frames into complete, ordered time series (lag sets).
4.  Perform data integrity checks and apply corrections (e.g., normalization, VanVleck).
5.  Execute core Fast Fourier Transform on the time series.
6.  Apply any user-selected frequency domain processes and integrate spectra over time.
7.  Format results with metadata into AIPS++ Measurement Set entities.
8.  **Output**: Transfer formatted data to the End-to-End archive and verify receipt.

**Key Branch A: System Monitoring & Recovery**
1.  **Trigger**: Periodic check or fault detection.
2.  Monitor health of processes, processors, and internal networks.
3.  Detect failure or out-of-spec condition (e.g., high error rate, component crash).
4.  Attempt automatic recovery (e.g., restart process, reboot processor, offload work).
5.  Report status/error to Monitor & Control System.

**Key Branch B: Operational Control & Mode Change**
1.  **Trigger**: Command from Monitor & Control or correlator mode change.
2.  Receive new processing parameters or control commands.
3.  Update internal parameter tables and processing pipeline configuration.
4.  Synchronize data flow with new operational conditions without data loss.

## Domain Model
*   **Lag Frame**: (Required fields: lag_values[up to 128], frame_sequence_id, baseline_id, auxiliary_parameters)
*   **Lag Set**: (Required fields: assembled_time_series[up to 262144 values], metadata_reference)
*   **Processing Pipeline**: (Fields: process_sequence, user_selected_parameters, operational_mode)
*   **Spectrum**: (Fields: frequency_domain_data, integration_count, metadata_reference)
*   **Output Data Set**: (Required fields: formatted_spectra, complete_metadata, AIPS++_MS_compatible)
*   **System Status**: (Fields: component_health, performance_metrics, error_counts)
*   **User Account**: (Required/Unique fields: username, encrypted_password; Fields: access_properties)
*   **Error/Warning Report**: (Required fields: report_id, error_code, source, timestamp, severity)

## Interfaces and Integrations
*   **Correlator System**: Inbound. **Theme**: High-speed raw data ingestion. **Input**: Lag frames via UDP/IP. **Output**: Receipt verification/error reports. **SLA**: Must sustain 1.6 GB/s initial input rate.
*   **Monitor & Control (M&C) System**: Bi-directional. **Theme**: Command, control, and auxiliary data. **Input**: Commands, observational parameters, auxiliary data (state counts, meta-data). **Output**: Status, error/warning reports, operational data. **SLA**: Must cache data if M&C is temporarily unavailable.
*   **End-to-End (e2e) Archive System**: Outbound. **Theme**: Formatted result delivery. **Input**: Formatted AIPS++ Measurement Sets. **Output**: Transfer confirmation. **SLA**: Must sustain 25 MB/s initial output rate and buffer data during e2e outages.
*   **Internal Management Network**: Internal. **Theme**: Inter-processor communication for workload distribution and health checks.

## Acceptance Criteria
**Capability: Real-time Processing Pipeline**
*   Given the Correlator is streaming data and the Backend is operational, when a complete lag set is assembled, then the system shall produce a valid Fourier-transformed spectrum delivered to the e2e.
*   Given a user has selected an optional frequency domain process, when the core Fourier transform completes, then the selected process shall be applied before integration and formatting.

**Capability: Fault Tolerance and Recovery**
*   Given a processor in the cluster fails, when the failure is detected by the monitoring system, then the workload shall be redistributed and the failure reported to M&C without stopping the data pipeline.
*   Given the connection to the e2e archive is temporarily lost, when data is ready for output, then it shall be buffered in memory/disk and delivered once the connection is restored.

**Capability: Secure Access Control**
*   Given an unauthorized user attempts to access the system, when they fail authentication, then access is denied and the attempt is logged.
*   Given an administrator, when they modify a user's access properties, then the changes are applied immediately to that user's next session.

## Non-Functional Metrics
*   **Performance**: Sustain initial aggregate input data rate of 1.6 GB/s; Sustain initial output data rate of 25 MB/s.
*   **Reliability**: Perform without total system restart between maintenance windows; Continue loss-less operation during temporary e2e outage (duration TBD).
*   **Security**: All access requires unique, authenticated login (e.g., username/password); Administrator has full privilege control and audit logging.
*   **Compliance**: Processing must be reversible (raw data recoverable from output); Software shall follow industry standards.
*   **Observability**: Provide error/warning reports with source and timestamp; Monitor and report on I/O and compute performance against tolerances.

## Milestones and Release Strategy
1.  Finalize and baseline Software Requirements Specification (this document).
2.  Complete high-level architectural and detailed design phases.
3.  Develop and unit test core processing pipeline components (data assembly, FFT).
4.  Integrate subsystems and begin end-to-end testing with simulated data.
5.  Conduct on-site integration testing with Correlator and e2e systems.
6.  Deploy initial operational capability meeting baseline performance specs.

## Risk List and Mitigation Strategies
1.  **Risk**: Hardware performance insufficient for target data rates. **Mitigation**: Design for modular scalability; use benchmarking to validate capacity early.
2.  **Risk**: Network latency or failure disrupts real-time flow. **Mitigation**: Implement robust buffering, redundant paths, and continuous network monitoring.
3.  **Risk**: Software bugs cause data corruption or pipeline halt. **Mitigation**: Employ rigorous testing, including fault injection; design processes to be restartable.
4.  **Risk**: Inability to handle correlator mode changes seamlessly. **Mitigation**: Design dynamic parameter loading and pipeline reconfiguration mechanisms.
5.  **Risk**: Extended outage of M&C system halts processing. **Mitigation**: Cache critical auxiliary data and implement a fallback operational mode.
6.  **Risk**: Security breach compromises system or data. **Mitigation**: Enforce strict authentication, authorization, and encryption; conduct security audits.
7.  **Risk**: Poor maintainability of complex distributed software. **Mitigation**: Adopt coding standards, comprehensive documentation, and modular design.
8.  **Risk**: Integration failures with external systems (Correlator, e2e). **Mitigation**: Establish clear interface contracts and conduct early joint testing.

## Undecided Issues and Responsible Parties
1.  **Precise memory requirements and access speeds** for processing without delay. (Responsible: System Architects/Designers)
2.  **Amount of excess storage (memory/disk)** needed for bursting and outage recovery. (Responsible: Performance Engineering Team)
3.  **Duration** the system can buffer data during a loss of the e2e connection. (Responsible: Project Lead & Operations)
4.  **Amount of correlator data to cache** when critical auxiliary data from M&C is unavailable. (Responsible: Software Designers)
5.  **Specific time delay** tolerated when resuming from standby idle mode. (Responsible: Systems Engineering)
6.  **Definition of "minimal confusion" coding practices** and choice of the one or two programming languages. (Responsible: Development Lead)
7.  **Detailed diagnostic package requirements** for third-party software tools without source code. (Responsible: Integration & Test Team)
8.  **Final list and specifications of user-selectable time and frequency domain processes**. (Responsible: Project Scientists & Developers)