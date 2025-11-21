# Detailed Summary

## Background and Scope
The UK Fishing Vessel's Electronic Logbook system enables UK fishing vessels exceeding 15 meters to electronically record and report fishing activities in compliance with EU regulations. The system replaces paper logbooks and facilitates data transmission to UK fisheries authorities. Non-goals include onshore use by agents/representatives and support for non-UK localization requirements.

## Role Matrix and Use Cases
- **Vessel Master**: Primary user responsible for data entry, transmission, and legal signing of reports
- **Vessel Owner**: Sets up user accounts and manages system access
- **Fisheries Monitoring Centre**: Receives and processes transmitted data
- **ELSS Supplier**: Provides and maintains approved software
- **Validation Authority**: Conducts product approval testing
- **Inspector**: Requests reports during at-sea inspections

Main scenarios include departure reporting, daily fishing activity reporting, and landing declarations. Exception scenarios cover transmission failures and correction of previously submitted data.

## Business Process
**Main Process:**
1. Vessel departs port (trigger: departure)
2. Master records fishing activities daily (input: catch/gear data)
3. System validates data against XML schema
4. Master transmits reports via email (output: encrypted XML)
5. System receives acknowledgment from FMC
6. Vessel completes fishing operations
7. Master submits prior notification of return
8. Vessel lands catch and submits landing declaration

**Key Branches:**
- **Correction Process**: Master identifies error → creates correction message → transmits entire corrected report → receives acknowledgment
- **Inspection Process**: Inspector requests report → Master generates FAR with inspection marker → Immediate transmission → Verification

## Domain Model
- **Vessel** (RSS Number: required/unique, CFR Number, Name, Radio Call Sign)
- **Master** (Name: required, Address: required)
- **Fishing Trip** (Logbook Number: required/unique, Sequence Number: required)
- **Report** (Type: required, Date/Time: required, Position data)
- **Catch** (Species: required, Weight: required, Presentation)
- **Gear** (Type: required, Mesh Size, Deployment data)
- **Transmission** (Operation Number: required/unique, Status, Acknowledgment)
- **User Account** (Username: required/unique, Password: required, Role)

## Interfaces and Integrations
- **UK Fisheries ERS** (Direction: Outbound) - Email transmission of XML reports - Input: Validated XML data - Output: Acknowledgment messages - SLA: Daily transmission required
- **Onboard GPS** (Direction: Inbound) - Position data auto-population - Input: Latitude/Longitude coordinates - Output: Position in reports - SLA: Real-time when available
- **Onboard Printer** (Direction: Outbound) - Hard copy generation - Input: Report data - Output: Printed logsheets - SLA: On-demand printing
- **Onboard Weighing Systems** (Direction: Inbound) - Catch weight data - Input: Weight measurements - Output: Species weight data - SLA: Optional integration

## Acceptance Criteria
- **Given** a vessel has completed fishing operations, **when** the master submits an EOF report, **then** the system must transmit immediately and receive acknowledgment
- **Given** a transmission failure occurs, **when** no acknowledgment is received within preset time, **then** the system must alert the master and allow retransmission
- **Given** catch data requires correction, **when** the master submits a COR message, **then** the system must transmit the complete corrected report

## Non-functional Metrics
- **Performance**: Daily transmission completion within 24-hour windows; Position data capture within 1-minute accuracy
- **Reliability**: 99% successful transmission rate; Data retention throughout fishing trip duration
- **Security**: PGP encryption for all transmissions; Unique user authentication per report
- **Compliance**: Adherence to EU regulations 1966/2006 and 1077/2008; UTC time standard usage
- **Observability**: Transmission status tracking; Acknowledgment matching and error reporting

## Milestones and Release Strategy
1. Product validation and approval completion
2. Vessel installation and commissioning
3. Crew training and system familiarization
4. Initial transmission testing with FMC
5. Operational deployment and monitoring
6. Periodic software updates and re-approval

## Risk List and Mitigation Strategies
- **Communication failures**: Implement retry mechanisms and alternative transmission methods
- **Data entry errors**: Provide validation against XML schema before transmission
- **Software updates affecting compliance**: Require re-approval before deployment
- **User authentication issues**: Maintain unique identifiers and password protection
- **Third-country fishing requirements**: Support additional data capture for specific regions
- **Hardware failures onboard**: Ensure data retention and recovery capabilities
- **Regulatory changes**: Maintain flexibility in data schema and reporting requirements
- **Transmission security breaches**: Maintain PGP encryption and secure key management

## Undecided Issues and Responsible Parties
- Alternative transmission methods beyond email (UK Fisheries Administrations)
- Integration standards with additional onboard systems (ELSS Suppliers)
- Extended support for future regulatory changes (Joint: UK Fisheries & Suppliers)
- Third-country requirement harmonization (International bodies)
- Long-term data retention policies (UK Fisheries Administrations)
- Mobile/offline operation capabilities (ELSS Suppliers)
- Real-time monitoring interface requirements (Not mentioned)
- Disaster recovery procedures for vessel systems (Not mentioned)