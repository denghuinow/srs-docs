**Purpose & Scope**  
The system is the flight software for the X-Ray Telescope Control Processor on the Swift Gamma Ray Burst Explorer observatory. It controls the X-Ray Telescope instrument to collect and process science data from Gamma-Ray Burst afterglows and manage the instrument’s interfaces, thermal systems, and internal states.

**Core Functions**  
- Process science data from the CCD camera and format it into CCSDS packets for downlink.  
- Receive and execute commands from the spacecraft to configure observation modes and instrument states.  
- Transmit housekeeping telemetry (voltages, temperatures, status) to the spacecraft.  
- Control telescope tube heaters, baffle heaters, and the thermo-electric cooler to maintain thermal stability.  
- Synchronize the instrument’s clock with the spacecraft and read the Telescope Alignment Monitor.

**Key Users**  
- Spacecraft Control Unit (command source and data destination).  
- Ground operators (via telecommands and telemetry).

**Key Constraints**  
- The TDRSS downlink bandwidth allocated to the instrument is 1 kbps, limiting telemetry rates.  
- Real-time housekeeping packets must not exceed 230 bytes each.  
- The spacecraft does not reassemble segmented packets; the ground system (ITOS) cannot decompress packets.  
- Ground contacts are limited to about seven per day, each 7–10 minutes long.