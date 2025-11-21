Purpose & Scope: The XRT Control Processor (XCP) flight software manages the Swift X-Ray Telescope (XRT), a sensitive CCD imaging spectrometer that refines BAT position data to 2.5" within 5 seconds of target acquisition. The system processes science data from the camera, transmits telemetry to the spacecraft, and controls critical subsystems including heaters and the Telescope Alignment Monitor. It does not handle spacecraft attitude control or scientific data analysis.

Product Background / Positioning: The XRT is a key instrument on the Swift Gamma Ray Burst Explorer mission, one of three semi-autonomous instruments (alongside BAT and UVOT) for multi-wavelength transient astronomy. It reuses components from previous projects (CUBIC, IMAGE, JET-X, XMM) and interfaces with the spacecraft via MIL-STD-1553B to enable rapid GRB afterglow observations.

Core Functional Overview: 
- Process science data from camera and relay to spacecraft as CCSDS packets
- Receive commands from spacecraft to establish instrument state
- Transmit housekeeping telemetry within 230-byte constraints
- Synchronize local clock with spacecraft using 1PPS
- Control telescope tube and baffle heaters via closed-loop control
- Read and process Telescope Alignment Monitor data
- Support three observation sequences (Automatic, Preplanned, Target of Opportunity)
- Operate in multiple science modes including Image, Photo-Diode, Windowed Timing, and Photon Counting

Key Users & Usage Scenarios: Ground-based mission operators at the Science Mission Operations Center (SMOC) command the system via telecommands. The spacecraft autonomously executes observations when BAT detects GRBs, with ground operators adjusting parameters for specific observation types and science modes.

Major External Interfaces: MIL-STD-1553B bus for spacecraft communication, RS-422 for Telescope Alignment Monitor, analog I/O for housekeeping telemetry, and engineering Ethernet for development. All interfaces must comply with spacecraft constraints including 230-byte packet limits.

Key Non-functional Requirements: Must operate within strict real-time constraints for GRB response (position refinement within 5 seconds), maintain reliability with no single point of failure, support error detection/correction for memory, and operate within TDRSS downlink bandwidth limit of 1 kbps for telemetry.

Constraints, Assumptions & Dependencies: Malindi ground contacts limited to ~7 per day (7-10 minutes each), spacecraft does not reassemble segmented packets, ITOS ground system cannot decompress packets, and spacecraft HK packets must be ≤230 bytes. The system must operate with limited power from spacecraft 28VDC buses (OPB and SPB).

Priorities & Acceptance Approach: Mission success (GRB detection and afterglow study) is highest priority. Acceptance requires successful GRB position refinement within 5 seconds, telemetry within 1 kbps bandwidth limit, and system operation across all science modes with required error handling. Primary verification occurs through ground testing and on-orbit observation of known GRB events.