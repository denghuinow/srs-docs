**Purpose & Scope**
The system is the EVLA Correlator Backend, a real-time astronomical data processing pipeline. It receives raw correlation data from the Correlator, performs assembly, Fourier transforms, and optional processing, then delivers formatted spectral data to the End-to-End archive system. It does not combine data from different sub-bands or directly provide user interfaces.

**Product Background / Positioning**
It is a critical component positioned between the Correlator hardware and the End-to-End (archive) system within the EVLA telescope array. All user interaction and system control occurs indirectly through a separate Monitor and Control (M&C) system.

**Core Functional Overview**
*   Receive real-time lag frame data streams from the Correlator.
*   Assemble lag frames into complete time series (lag sets).
*   Perform Fast Fourier Transforms on the time series.
*   Apply user-selectable time or frequency domain processing operations.
*   Integrate (sum) spectral results over a configurable time period.
*   Format final spectra and metadata for the End-to-End archive.
*   Monitor system health, performance, and errors.
*   Manage internal workload distribution and recovery from failures.

**Key Users & Usage Scenarios**
*   **Array Operators:** Monitor status and error messages relayed via the M&C system.
*   **Astronomers/Scientists:** Select and parameterize optional data processing steps.
*   **Engineers & Technicians:** Perform maintenance, diagnostics, and repairs using remote access tools.
*   **Software Developers:** Develop, test, and troubleshoot the system software.
*   **Administrators:** Have unrestricted access to all system aspects for configuration and user management.

**Major External Interfaces**
*   **Correlator Interface:** Very high-speed network input for raw lag frame data.
*   **Monitor & Control (M&C) Interface:** For receiving auxiliary data, commands, and sending status/error reports.
*   **End-to-End (e2e) Interface:** Very high-speed network output for formatted archive data.

**Key Non-functional Requirements**
*   **Performance:** Must accept a minimum aggregate input data rate of 1.6 GB/s and deliver a minimum output rate of 25 MB/s simultaneously.
*   **Reliability/Availability:** Must continue loss-less operation during temporary loss of the e2e system or M&C system (for a cached period). Must self-detect and auto-correct hardware/software failures.
*   **Data Integrity:** Must maintain data fidelity and dynamic range. All processing must be reversible to recover raw input data.
*   **Scalability:** Architecture must be scalable to ultimately handle up to 2 GB/s per Correlator output channel.
*   **Security:** All access requires unique user authentication. An administrator controls all user privileges.

**Constraints, Assumptions & Dependencies**
*   **Constraint:** System throughput is limited by available hardware computational performance and network capabilities.
*   **Assumption:** The Correlator delivers properly formatted network packets, and the e2e system can accept the Backend's output data rate.
*   **Dependency:** Relies on the external M&C system for auxiliary data and operational commands.

**Priorities & Acceptance Approach**
Critical requirements center on real-time data ingestion, processing integrity, and reliable delivery to the archive. Acceptance will involve verifying sustained input/output performance metrics, correct data processing reversibility, and fault tolerance during simulated failures of external systems.