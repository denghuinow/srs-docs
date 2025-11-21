# Short Summary

- **Background and objectives**: The Swift X-Ray Telescope (XRT) Control Processor (XCP) Flight Software (FSW) is designed to control the XRT instrument on the Swift Gamma Ray Burst Explorer, enabling autonomous observation and data processing of gamma-ray bursts and afterglows. Its primary objectives include processing science data, managing instrument states, and ensuring reliable communication with the spacecraft.

- **In scope**:
  - Processing and relaying science data from the CCD camera to the spacecraft.
  - Receiving and executing spacecraft commands to control instrument states and modes.
  - Managing housekeeping telemetry and time synchronization with the spacecraft.
  - Controlling heaters, thermo-electric coolers, and telescope alignment monitors.
  - Supporting multiple observation sequences (automatic, preplanned, target of opportunity).

- **Out of scope**:
  - Ground system operations and simulators (e.g., ITOS upgrades for packet reassembly).
  - Decompression of packets by the ground system.
  - Reassembly of segmented packets by the spacecraft.
  - Real-time telemetry packets exceeding 230 bytes.
  - On-orbit software patching via dynamic loading (noted as TBD/TBR).

- **Roles and core use cases**:
  - As a **Science Operator**, I want to command observation modes so that the XRT can autonomously collect and process burst data.
  - As a **System Monitor**, I want to receive housekeeping telemetry so that instrument health and status can be tracked.
  - As a **Maintenance Engineer**, I want to upload software patches so that on-orbit issues can be resolved without full reloads.

- **Success metrics**:
  - Achieve an average science telemetry rate of ≤1 kbps over 24 hours.
  - Maintain synchronization with the spacecraft clock within specified tolerances.
  - Execute all telecommands and mode transitions without unrecoverable errors.

- **Major constraints**:
  - TDRSS downlink bandwidth limited to 1 kbps for spacecraft data.
  - Real-time housekeeping packets must not exceed 230 bytes.
  - Limited Malindi ground contacts (≈7 per day, 7–10 minutes each).
  - ITOS ground system cannot reassemble segmented packets or decompress data.
  - Memory and CPU throughput must support continuous 24-hour observation buffers.

- **Undecided issues**:
  - Final numerical values for science data acquisition modes (TBD).
  - Specific algorithms for bias and centroid calculations (TBD).
  - Verification methods for certain software requirements (TBD).
  - Ground system capabilities for packet reassembly and decompression (Not mentioned).
  - Some referenced document data and abbreviations are incomplete (TBR).