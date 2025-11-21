# Ultra Short Summary
A standard C/C++ modeling interface for connecting untimed software models to RTL hardware models on emulators, enabling high-performance co-emulation.

- MVP points: Provides multiple message channels between software models and hardware DUT; supports dual-ready handshake protocol for message ports; includes controlled clock generation and reset control; offers C++ and C APIs for software-side integration.
- Key constraints: Optimized for bridging untimed software with cycle-accurate hardware; not intended for event-based or sub-cycle accurate simulation; requires frequent service loop calls for message processing.
- Major risks/undecided issues: Not mentioned.