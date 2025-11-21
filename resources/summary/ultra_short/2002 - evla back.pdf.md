**Purpose & Scope**  
The system processes real-time astronomical data streams between the EVLA Correlator and End-to-End (e2e) Systems. It assembles lag frames into time-series, performs Fourier Transforms, and formats output for e2e. It does not handle spectrum stitching across sub-bands or provide direct user interfaces.  

**Product Background / Positioning**  
Critical to EVLA’s real-time data pipeline; failure causes irreversible data loss. Integrates with Correlator (input), M&C System (control/auxiliary data), and e2e (output). Replaces legacy VLA processing infrastructure.  

**Core Functional Overview**  
- Assemble lag frames into complete time-series (lag sets ≤262,144 values).  
- Perform Fourier Transforms on time-series.  
- Apply user-selectable time/frequency domain processing.  
- Format output as AIPS++ Measurement Sets for e2e.  
- Monitor internal system health (processors, networks, compute).  
- Recover from failures without data loss (raw data always recoverable).  

**Key Users & Usage Scenarios**  
- **Array Operators**: Receive status/errors via M&C; no direct access.  
- **Scientists**: Specify optional processing parameters (e.g., RFI mitigation).  
- **Engineers**: Diagnose hardware/software faults remotely; perform maintenance.  
- **Developers**: Debug software remotely; require full system access.  
- **Web Users**: Limited restricted access (e.g., monitoring).  

**Major External Interfaces**  
- **Correlator**: Input via UDP/IP packets (lag frames); no ordering guarantee.  
- **M&C System**: Control commands, auxiliary data, status reports, error handling.  
- **e2e System**: Output of formatted spectra (AIPS++); no data reassembly.  

**Key Non-functional Requirements**  
- **Performance**: Input ≥1.6 Gbytes/sec; output ≥25 MB/sec.  
- **Reliability**: 99.9% availability; recover from Correlator/e2e loss without data loss.  
- **Security**: Role-based access (admin: full control; others: restricted); encrypted logins.  
- **Reversibility**: All processing must be reversible (raw data recoverable).  

**Constraints, Assumptions & Dependencies**  
- **Constraints**: Hardware limits throughput; networks must support real-time rates.  
- **Assumptions**: Lag sets are power-of-two; auxiliary data arrives via M&C.  
- **Dependencies**: e2e must accept output rates; Correlator delivers lag frames.  

**Priorities & Acceptance Approach**  
Critical priority due to data loss risk. Acceptance requires:  
- Verified throughput (input ≥1.6 Gbytes/sec, output ≥25 MB/sec).  
- Zero data loss during Correlator/e2e outages.  
- Full reversibility of all processing steps.