**Purpose & Scope**: The system is the real-time astronomical data processing pipeline between the Correlator and the End-to-End archive, performing basic data assembly, formatting, and processing.

**Core Functions**:
*   Receive real-time data from the Correlator.
*   Assemble time-series from correlator lag output.
*   Perform Fourier Transforms on the assembled time series.
*   Deliver formatted results to the End-to-End System.

**Key Users**: Array Operator, Engineers and Technicians, Astronomer/Scientist, Software Developer.

**Key Constraints**:
*   The system is critical; if unavailable, incoming astronomical data is lost.
*   Throughput is constrained by computational hardware limits and network performance.
*   All processing operations must be reversible.