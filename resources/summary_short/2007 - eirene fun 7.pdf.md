# Short Summary

- **Background and objectives**: The EIRENE Functional Requirements Specification defines a digital radio standard for European railways to ensure interoperability and manufacturing economies of scale, primarily for international high-speed lines and future replacement of national systems.
- **In scope**: Voice services (point-to-point, emergency, broadcast, group, multi-party); data services (text messaging, general data, fax, train control); call-related services (priority, closed user group, forwarding); railway-specific services (functional addressing, location-dependent addressing, shunting mode, emergency calls).
- **Out of scope**: Detailed specification of controller equipment interfaces; internationally standardized pre-defined messaging applications; alphanumeric numbering support for interoperability; public network pre-emption without special agreements; automatic network selection for international border crossing.
- **Roles and core use cases**:
  - As a **driver**, I want to initiate Railway emergency calls so that all trains and controllers in the area are alerted to danger.
  - As a **controller**, I want to establish group calls with drivers so that operational instructions can be broadcast efficiently.
  - As a **shunting team member**, I want to use shunting mode with link assurance so that safe pushing manoeuvres are assured during silent periods.
- **Success metrics**: Railway emergency call setup time <2s in 95% of cases; group call setup time <5s in 95% of cases; text message segment transfer time <30s in 95% of cases.
- **Major constraints**: Must support train speeds up to 500 km/h; mandatory compliance with CENELEC ERTMS driver-machine interface standards; functional numbers must be unique across all networks; all mobiles must operate in allocated 900 MHz railway bands; environmental specs must not prevent use of other EIRENE mobiles.
- **Undecided issues**: Specific languages for MMI implementation; duration of emergency call audible indication (trials needed); alternative link assurance indication methods; automatic network selection activation/deactivation by driver; directed network selection implementation.