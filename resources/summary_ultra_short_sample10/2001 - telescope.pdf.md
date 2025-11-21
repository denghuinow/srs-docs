# Ultra Short Summary

The X-Ray Telescope Control Processor flight software autonomously controls the Swift XRT instrument to collect and process GRB science data, manage thermal systems, and interface with the spacecraft.

**MVP Points**
- Process science data from the CCD camera and transmit it to the spacecraft as CCSDS packets.
- Receive and execute spacecraft commands to configure instrument states and camera modes.
- Control heaters and the thermo-electric cooler to maintain instrument thermal stability.
- Synchronize the local clock with the spacecraft time and transmit housekeeping telemetry.

**Key Constraints**
- The TDRSS downlink bandwidth limits housekeeping telemetry to 1 kbps.
- Real-time housekeeping packets must not exceed 230 bytes.
- The ground system cannot reassemble segmented packets or decompress data.

**Major Risks**
- Some science data acquisition modes and algorithm parameters are TBD.
- Not mentioned.