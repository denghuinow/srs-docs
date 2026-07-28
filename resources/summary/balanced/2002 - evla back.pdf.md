# Balanced Summary: EVLA Correlator Backend System

## Goals and Scope
The EVLA Correlator Backend System is the primary real-time astronomical data processing pipeline component, positioned between the Correlator and End-to-End (e2e) systems. Its core responsibility is to receive correlator data, assemble time-series, perform Fourier Transforms and optional processing, and deliver formatted results for archiving. The scope is strictly limited to defining the Backend System's requirements, excluding external system functionalities.

## Stakeholders and User Stories
*   **Array Operator**: Monitors system status and error messages via the Monitor and Control (M&C) System to ensure operational continuity.
*   **Engineers and Technicians**: Perform corrective/preventive maintenance and remote diagnostics to ensure hardware and software reliability.
*   **Astronomer/Scientist**: Provides parameters for optional data processing steps to extract scientific value from the observational data.
*   **Software Developer**: Develops, tests, and troubleshoots system software, requiring remote access for support.
*   **Web User**: A restricted set of authorized individuals granted limited access to typically restricted system parts.
*   **Administrator**: An individual with unrestricted system access for full control and user management.

**User Stories:**
1.  As an **Array Operator**, I want to receive consolidated status and error reports via the M&C System so that I can monitor the health of the data processing pipeline.
2.  As an **Engineer**, I want remote diagnostic tools to inspect individual hardware devices so that I can perform rapid fault diagnosis and repair.
3.  As an **Astronomer**, I want to select and parameterize optional time/frequency domain processing steps so that I can apply specific corrections or analyses to the data.
4.  As a **Software Developer**, I want remote access to the system for troubleshooting so that I can resolve issues outside of normal working hours.
5.  As the **System Administrator**, I want to manage user access privileges so that I can control who can interact with different subsystems.
6.  As a **Technician**, I want the system to use hot-swappable hardware components so that I can perform maintenance without a full system shutdown.

## Key Processes
1.  **Data Receive (Trigger: Incoming network packets)**: Receive lag frame data packets from the Correlator via a high-speed network interface.
2.  **Time Series Assembly**: Assemble received lag frames into complete, correctly ordered time-series (lag sets) for processing.
3.  **Core Processing**: Apply mandatory processing steps including normalization, time-stamp adjustment, and a power-of-two complex Fast Fourier Transform.
4.  **Optional Processing**: Apply user-selected, chainable time or frequency domain processes (e.g., windowing for RFI mitigation) upon request.
5.  **Integration & Formatting**: Integrate (sum) spectral results over a specified time duration and format them with metadata into output datasets (e.g., AIPS++ Measurement Sets).
6.  **Data Output (Trigger: Formatted data ready)**: Send formatted output data to the e2e archive system and verify successful delivery.
7.  **System Monitoring & Recovery**: Continuously monitor I/O rates, computation, processes, and hardware; attempt automatic recovery from failures.

## Domain Data Elements
*   **Lag Frame** (Primary Key: Frame ID): Contains correlation lag values, baseline ID, timestamps, auxiliary parameters for assembly.
*   **Lag Set/Time Series** (Primary Key: Set ID): Assembled from Lag Frames, contains ordered lag values, baseline ID, integrated time span.
*   **Processed Spectrum** (Primary Key: Spectrum ID): Output of Fourier Transform, contains spectral data, baseline ID, frequency channels, metadata.
*   **Output Dataset** (Primary Key: Dataset ID): Formatted for e2e, contains spectra, integrated time, all meta/auxiliary data, processing history.
*   **Processing Parameters** (Primary Key: Process ID): Defines processing steps, sequence order, adjustable parameters, user selections.
*   **System Status/Error Report** (Primary Key: Report ID & Timestamp): Contains error/warning codes, source component, statistics, system state flags.

## Non-Functional Requirements
1.  **Performance**: Must accept a minimum 1.6 GB/s input stream and deliver a 25 MB/s output stream in real-time without data loss.
2.  **Reliability/Availability**: Must self-monitor and auto-correct hardware/software failures; continue loss-less operation during temporary e2e or M&C outages.
3.  **Data Integrity**: Must maintain input data fidelity and dynamic range; all processing must be reversible to recover raw input from output.
4.  **Scalability**: Hardware and software must be expandable to ultimately handle up to 2 GB/s per correlator output channel transparently.
5.  **Security**: Requires robust user authentication (e.g., username/password), encrypted logins, and administrator-controlled access privileges.
6.  **Maintainability**: Must support partial shutdowns for upgrades; use modular, hot-swappable hardware and well-documented, readable software.

## Milestones and External Dependencies
1.  **Correlator Interface**: Dependency on the Correlator delivering properly formatted lag frame packets over the network.
2.  **Auxiliary Data Feed**: Dependency on the Monitor & Control System providing all necessary meta-data and processing parameters in a timely manner.
3.  **e2e System Readiness**: Dependency on the End-to-End archive being capable of accepting the Backend's output data rate and format.
4.  **Hardware Procurement**: Milestone for acquiring the distributed cluster of processors and high-speed networking hardware.
5.  **Initial Deployment**: Milestone for system commissioning with baseline 1.6 GB/s input processing capability.

## Risks and Mitigation Strategies
1.  **Risk**: Hardware/software failures causing critical data loss in the real-time pipeline.
    *   **Mitigation**: Implement robust self-monitoring, automatic failover to standby processors, and data buffering for outage recovery.
2.  **Risk**: Computational or I/O bottlenecks preventing real-time processing as data rates scale.
    *   **Mitigation**: Design for hardware scalability and software efficiency; use performance profiling to identify and optimize bottlenecks.
3.  **Risk**: Loss of critical auxiliary data from the M&C system halting processing.
    *   **Mitigation**: Implement data caching to continue operations for a predetermined time until critical data is received.
4.  **Risk**: Complex system making diagnosis and repair difficult, increasing downtime.
    *   **Mitigation**: Provide comprehensive remote diagnostic tools for engineers and ensure software processes are independently debuggable and restartable.
5.  **Risk**: Security breaches from unauthorized access to the critical data path.
    *   **Mitigation**: Enforce strict user authentication, encrypted communications, and principle of least privilege access controls.

## Undecided Issues
1.  Specific amount of excess memory/disk storage required for buffering and outage recovery.
2.  Exact time duration the system can operate losslessly without the e2e system being available.
3.  The precise amount of correlator data to cache upon loss of critical data from the M&C system.
4.  The detailed specifications for "minimal delay" when resuming operations from standby idle mode.
5.  The final selection of specific optional time and frequency domain processing algorithms to be implemented.
6.  The exact mechanisms and protocols for the "hot-swappable" replacement of hardware components during operation.