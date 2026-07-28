**Purpose & Scope**: The system processes real-time astronomical data from the Correlator for the End-to-End archive, performing assembly, formatting, and basic processing.

**Core Functions**:
*   Receive real-time correlator lag data.
*   Assemble lag frames into time series and perform Fourier Transforms.
*   Deliver formatted spectral data to the End-to-End archive.

**Key Constraints**:
*   Must maintain real-time processing to prevent astronomical data loss.
*   Processing operations must be reversible; raw input data must be recoverable from the output.
*   Throughput is constrained by computational hardware limits and network performance.