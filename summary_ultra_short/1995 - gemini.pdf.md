# Ultra Short Summary
- The Gemini Control System software is designed to guide the development of controls and data acquisition systems for the Gemini 8-m Telescopes, ensuring efficient and consistent operation across the observatory.

**MVP Points**
- The system must support interactive observing through an automatic sequencer, allowing users to interact with the scheduler rather than control programs directly.
- Remote operations must be fully supported, enabling all observing facilities to function both on-site and off-site without conceptual differences.
- Queue-based observing is the primary mode, requiring fully automated observing programs with minimal human interaction during execution.
- The system must provide a virtual telescope simulator for science planning and testing, allowing observation programs to be validated for completeness and functionality.

**Key Constraints**
- All software must use commercial packages, off-the-shelf public domain software, and standards whenever feasible to reduce life-cycle costs.
- Software must be developed using standard methodologies and development environments, with all components easily integrated into the system.
- Hardware must be scalable and capable of running the Gemini software environment, with identical network access and data format compatibility across systems.

**Major Risks/Undecided Issues**
- The definition of a standard for acquisition and storage of detector data remains unresolved.
- The supportability plan for the control system is not yet defined.