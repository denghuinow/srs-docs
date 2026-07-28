**Purpose & Scope**: The Model Manager is a software tool for configuring, scheduling, running, monitoring, and stopping weather and climate model jobs across one or more clusters.

**Core Functions**:
*   Set up and submit new model jobs (e.g., Weather FDDA, ClimoFDDA).
*   Submit pre-configured 'by-hand' or custom jobs.
*   Monitor, stop, restart, and resume scheduled, running, and completed jobs.

**Key Constraints**:
*   Must manage jobs across one or more clusters, with centralized node allocation.
*   Must be accessible via both a web-based GUI and a command-line tool.
*   Must allow users to optionally specify a target cluster for job execution.