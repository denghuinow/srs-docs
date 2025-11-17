# Ultra Short Summary
Libra is an economy-driven cluster scheduler that provides Quality of Service computational economy for batch jobs on Linux clusters by prioritizing user utility over system performance.

- MVP points (4 items)
  - Schedule sequential and embarrassingly parallel batch jobs on a homogenous Linux cluster.
  - Allocate CPU time based on user-submitted budget and deadline constraints.
  - Integrate as an add-on module to the Sun Grid Engine cluster management system.
  - Use a bid-based proportional resource-sharing model with stride scheduling.

- Key constraints (3 items)
  - Must run on a limited test cluster of four Pentium-III workstations with 128MB RAM.
  - All coding must be done in standard C.
  - Must function as a sub-component of Sun Grid Engine without modifying the Linux kernel.

- Major risks/undecided issues (2 items)
  - The exact pricing and costing policy for charging users will be specified in a later version.
  - Not mentioned.