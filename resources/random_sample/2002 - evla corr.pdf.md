# Ultra Short Summary
- The EVLA Correlator Monitor & Control System provides the physical link between the WIDAR Correlator hardware and the EVLA monitor & control system for configuration, operation, and servicing.

- MVP points
  - Receive configuration information from the EVLA M&C system and translate it into a physical correlator hardware configuration.
  - Process and transfer dynamic control data and monitor data.
  - Monitor correlator and subsystem health and take autonomous corrective action for hardware and computing system faults.
  - Perform limited real-time data processing and probing such as collecting and displaying auto correlation products.

- Key constraints
  - The system is a critical component in the astronomical data path, and unavailability results in data loss.
  - The system must be modularized for fault detection and repair.
  - The system must provide full access with high data integration for a logical and coherent user interface.

- Major risks/undecided issues
  - Actions taken by external systems upon hard failures of the CPCC are TBD.
  - Not mentioned.