# Detailed Summary

## Background and Scope
Grid-BGC is a grid-based software infrastructure supporting bio-geochemical modeling using Daymet surface weather interpolation and Biome-BGC models. The system provides a graphical interface for managing input data, running simulations, visualizing results, and managing output data through grid technologies. Non-goals include extensive data validation during merging operations and low-priority visualization features.

## Role Matrix and Use Cases
**Roles:**
- Scientist (Primary): Manages data, runs simulations, visualizes results
- Portal Administrator: Manages accounts, monitors system, controls jobs
- Data User (Low Priority): Accesses simulation output without running models

**Use Cases:**
- Daymet Modeling Run
- BiomeBGC Modeling Run  
- Data Visualization
- Data Analysis
- Data Download
- Data Publication
- Account Management
- System Administration

## Business Process
**Main Process - Model Execution:**
1. User logs in with Gatekeeper credentials
2. Creates/selects input objects (Projection, Site Data, Surface Observation)
3. Configures project parameters
4. Submits model run to compute resources
5. System monitors execution status
6. Output objects automatically created
7. User views/downloads results
8. User can share output data

**Key Branches:**
- **Account Creation:** Apply → Admin Approval → Account Activation
- **Data Management:** Create Object → Share/Lock → Reference in Projects

## Domain Model
**Entities:**
- User Account (username: required/unique, status: required, role: required)
- Project (name: required, type: required, state: required)
- Object (name: required, type: required, state: required)
- Template (name: required, type: required, submitter: required/reference)
- Model Run (id: required/unique, status: required, user: required/reference)
- Output Data (id: required/unique, project: required/reference)
- Compute Resource (name: required/unique, status: required)
- System Metrics (timestamp: required, metrics: required)

## Interfaces and Integrations
- **NCAR Gatekeeper:** Inbound, Authentication, Username/password, Authentication status, NCAR security policies
- **NCAR Mass Storage System:** Outbound, File storage, User data files, Storage confirmation, File availability SLA
- **Compute Cluster:** Outbound, Job execution, Model parameters, Job status, Execution time estimates
- **Web Portal:** Inbound/Outbound, User interaction, User inputs, System responses, Browser compatibility requirements

## Acceptance Criteria
**Model Execution:**
- Given a user with valid credentials and configured project, when submitting a model run, then the system should queue the job and provide execution estimates

**Data Sharing:**
- Given a user with shared objects, when another user references them, then the objects should become locked and dependencies maintained

**Account Management:**
- Given a new user application, when admin approves, then the account should become active with scientist role

## Non-functional Metrics
- **Performance:** Model execution within estimated timeframes, Portal response < 3 seconds
- **Reliability:** 99% system availability, Graceful failure handling for compute jobs
- **Security:** NCAR security policy compliance, Secure authentication channels
- **Compliance:** Data integrity preservation through locking mechanism
- **Observability:** Comprehensive portal metrics, System consistency checks

## Milestones and Release Strategy
1. Core authentication and user management
2. Basic object creation and management
3. Daymet model integration
4. BiomeBGC model integration  
5. Data sharing and collaboration features
6. Administrative and monitoring capabilities

## Risk List and Mitigation Strategies
- **Complex dependency management:** Implement robust locking/invalidation logic
- **Grid technology integration:** Use proven Globus toolkit components
- **Data integrity concerns:** Prevent changes to referenced objects
- **Performance scalability:** Monitor and optimize MSS interactions
- **User adoption:** Provide comprehensive online help system
- **Security compliance:** Strict adherence to NCAR security policies
- **Resource contention:** Admin job management capabilities
- **Data validation:** Clear documentation of validation limitations

## Undecided Issues and Responsible Parties
- Specific visualization implementation details (Development team)
- Resource quota implementation priority (Project management)
- Native model file formats for various objects (Scientific team)
- MSS credential management approach (System architecture)
- Browser compatibility beyond specified versions (Development team)
- Advanced analysis project requirements (Scientific team)
- Compute node configuration settings (System administration)
- Data publication integration details (Not mentioned)