**Purpose & Scope**
Flight software for the X-Ray Telescope Control Processor on the Swift observatory to collect and process science data from a CCD camera, manage instrument health, and interface with the spacecraft.

**Core Functions**
*   Process science data from the camera and relay it to the Spacecraft Control Unit.
*   Receive and execute spacecraft commands to establish instrument state and camera mode.
*   Control heaters for the telescope tube and thermal baffles.

**Key Constraints**
*   Real-time housekeeping packets transmitted to the spacecraft must not exceed 230 bytes.
*   The ground system cannot reassemble segmented packets or decompress packets.
*   The average science telemetry downlink rate is limited to 3.9 kbps.