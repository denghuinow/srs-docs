**Purpose & Scope**: The system automates the configuration, scheduling, running, monitoring, and stopping/restarting of computational weather and climate model jobs. It is a stand-alone tool that can also integrate with a larger system.

**Core Functions**:
*   Configure and submit new model or post-processing jobs.
*   Submit pre-existing custom ("by-hand") jobs.
*   Retrieve, modify, and re-submit previously saved job configurations.
*   Monitor and manage (stop, restart, delete) scheduled, running, and past jobs.

**Key Users**: Scientists and engineers familiar with model setup for operations or research; users less familiar with model setup who run standard jobs or monitor status.

**Key Constraints**: The system must manage jobs across one or more compute clusters, including automated node allocation. It must accept jobs defined outside its own configuration module, requiring users to provide mandatory job information.