# Short Summary

- **Background and objectives**: The EVLA Correlator Backend System is a real-time astronomical data processing pipeline that receives, processes, and formats correlator data for the End-to-End System, ensuring real-time inspection and data integrity.

- **In scope**:
  - Receive real-time data from the Correlator.
  - Assemble lag sets and perform Fourier Transforms.
  - Apply user-selected time and frequency domain processing.
  - Deliver formatted spectra and metadata to the End-to-End System.
  - Monitor system health and perform error recovery.

- **Out of scope**:
  - Combining spectra from different sub-bands ("stitching").
  - Direct user interface screens (all interaction via Monitor and Control System).
  - Long-term data archiving (handled by End-to-End System).
  - Hardware design of external systems (Correlator, networks).
  - Non-real-time data processing beyond test modes.

- **Roles and core use cases**:
  - As an Array Operator, I want status and error messages via M&C so that I can monitor system operations.
  - As an Astronomer/Scientist, I want to select additional data processing parameters so that I can customize data analysis.
  - As a Software Developer, I want remote access for troubleshooting so that I can maintain system functionality.

- **Success metrics**:
  - Process input data streams at ≥1.6 Gbytes/sec and output at ≥25 MBytes/sec.
  - Maintain real-time operations without data loss during correlator mode changes.
  - Achieve high reliability with automatic error correction and recovery.

- **Major constraints**:
  - Critical dependency on hardware and network performance for real-time processing.
  - All processing must be reversible to recover original raw data.
  - System must handle temporary outages of external systems (e2e, M&C) without data loss.
  - Scalability to support future data rate increases up to 2 Gbytes/sec per channel.
  - Security restrictions limiting access to authorized personnel only.

- **Undecided issues**:
  - Specific memory and storage capacity requirements (TBD).
  - Duration of tolerable e2e system outage (TBD).
  - Amount of critical auxiliary data to cache during M&C loss (TBD).
  - Exact standby mode resumption delay (TBD).
  - Not mentioned: Final selection of optional time/frequency domain processes.