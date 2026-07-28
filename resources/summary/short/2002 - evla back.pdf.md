# Short Summary: EVLA Correlator Backend System Requirements

## Background and Objectives
The EVLA Correlator Backend System is a critical real-time data processing pipeline component for the Expanded Very Large Array (EVLA), positioned between the Correlator and the End-to-End (e2e) archive system. Its primary objective is to receive, assemble, process, and format astronomical correlation data in real-time for scientific analysis and archiving.

## In Scope
*   Real-time reception and assembly of correlator lag data into time series.
*   Execution of core processing functions, including Fourier Transforms and user-selectable optional processes.
*   Formatting and delivery of processed spectral data to the End-to-End (e2e) archive system.
*   System monitoring, error handling, and automated recovery procedures.
*   Interaction with the external Monitor and Control (M&C) system for commands, status, and auxiliary data.

## Out of Scope
*   Direct user interfaces; all user interaction is mediated through the Monitor and Control system.
*   Combining ("stitching") spectra from different correlator sub-bands.
*   Long-term data archiving, which is the responsibility of the e2e system.
*   Generation of the raw correlator lag data or auxiliary observational data.
*   Final assembly of visibility data from different baselines.

## Stakeholders and Core Use Cases
*   **Array Operator**: Monitors system status and handles operational alerts via the M&C system.
*   **Engineer/Technician**: Performs maintenance, diagnostics, and repairs on backend hardware and software.
*   **Astronomer/Scientist**: Defines optional data processing parameters for scientific analysis via the M&C system.
*   **Software Developer**: Develops, tests, and debugs backend system software.
*   **System Administrator**: Manages user access, security, and overall system configuration.

**User Stories:**
1.  As an **Array Operator**, I want to receive clear error and status messages via the M&C system so that I can maintain continuous observatory operations.
2.  As an **Engineer**, I want remote diagnostic tools to inspect hardware and software components so that I can quickly troubleshoot and repair faults.
3.  As an **Astronomer**, I want to select and parameterize optional data processing steps (e.g., windowing for RFI mitigation) so that I can optimize the data for my scientific goals.
4.  As a **Software Developer**, I want remote access to system logs and debugging capabilities so that I can resolve software issues during non-working hours.
5.  As a **System Administrator**, I want to manage user privileges and access controls so that I can ensure system security and proper operational roles.

## Success Metrics
*   Sustained real-time processing of a minimum input data rate of 1.6 GB/s and output of 25 MB/s without data loss.
*   High system availability, capable of indefinite operation without complete service loss outside of total power failure.
*   Successful, verifiable delivery of all formatted data to the e2e archive system.

## Major Constraints
*   The system is mission-critical; any downtime results in the loss of incoming astronomical data.
*   Processing must be reversible, allowing recovery of raw input data from the final output.
*   Performance is limited by available hardware computational power, network bandwidth, and software efficiency.
*   The system must handle Correlator mode changes and temporary losses of external systems (e2e, M&C) in a loss-less manner.
*   All software and operating systems should adhere to industry standards, with a strong preference for open-source availability.

## Undecided Issues
*   The specific amount of excess memory/storage needed for buffering and outage recovery.
*   The exact duration the system can operate without critical auxiliary data from the M&C system.
*   The maximum acceptable delay when resuming operations from a standby/idle state.
*   The final details of the internal data structures and processing parameter tables.
*   The specific optional time and frequency domain processing algorithms to be implemented.