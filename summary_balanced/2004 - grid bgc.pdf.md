# Balanced Summary

## Goals and Scope
This project develops a grid-based software infrastructure to support bio-geo-chemical modeling using the Daymet surface weather interpolation engine and Biome-BGC model. The system provides a graphical user interface for managing input data, running simulations, visualizing results, and managing output data through web portal components integrated into the NCAR Dataportal Web Server.

## Roles and User Stories
- **Scientist**: I want to run Daymet modeling simulations so that I can generate gridded surface weather datasets from observation data
- **Scientist**: I want to run BiomeBGC modeling runs so that I can perform bio-geo-chemical modeling activities
- **Scientist**: I want to visualize output datasets so that I can analyze simulation results
- **Scientist**: I want to download output data so that I can perform further analysis externally
- **Portal Administrator**: I want to manage user accounts and system operations so that I can maintain day-to-day portal functionality
- **Data User**: I want to access simulation output data so that I can use it for research without running simulations

## Key Processes
1. **Trigger: User login** - User authenticates through NCAR Gatekeeper system to access the portal
2. **Trigger: Project creation** - User creates new modeling projects by selecting and configuring input objects
3. **Trigger: Model submission** - User selects computational resources and initiates model runs
4. **Trigger: Job monitoring** - System tracks and displays run status on tile-by-tile basis
5. **Trigger: Output generation** - System automatically creates output objects for completed simulations
6. **Trigger: Data access** - Users can download output data in native system formats
7. **Trigger: Administrative action** - Portal admin manages accounts, resources, and system consistency

## Domain Data Elements
- **User Account** (Primary Key: User ID) - Status, Role, Gatekeeper username, Creation date
- **Project** (Primary Key: Project ID) - Type, State, Referenced objects, Creation date
- **Object** (Primary Key: Object ID) - Type, Data format, Sharing status, Metadata
- **Model Run** (Primary Key: Run ID) - Status, Computational resource, Execution parameters
- **Output Data** (Primary Key: Output ID) - Tile information, Data files, Download status
- **Template** (Primary Key: Template ID) - Object type, Submission privileges, Access control

## Non-functional Requirements
- Must use Globus toolkit for grid technologies
- Must comply with NCAR security policies and constraints
- Must integrate with NCAR Mass Storage System for file storage
- Must support specified web browsers (IE 6.0, Netscape 7.1, Safari 1.2.1)
- Requires users to enable cookies for system functionality
- Must provide secure data channels for authentication

## Milestones and External Dependencies
- Integration with NCAR Dataportal Web Server
- Deployment on Hemisphere Linux cluster at CU
- Dependence on NCAR Gatekeeper account system
- Use of NCAR Mass Storage System for file storage
- Compliance with NCAR security policies

## Risks and Mitigation Strategies
- **Risk**: Data integrity issues from object dependencies
  - **Mitigation**: Implement locked/invalidated state management for objects and projects
- **Risk**: User account management complexity
  - **Mitigation**: Provide administrative functions for account approval, locking, and deletion
- **Risk**: Computational resource management
  - **Mitigation**: Implement job monitoring and termination capabilities for administrators
- **Risk**: Template submission control
  - **Mitigation**: Restrict template submission to privileged users only
- **Risk**: File system inconsistencies
  - **Mitigation**: Provide system consistency check tools for administrators

## Undecided Issues
- Resource quota implementation (lowest priority)
- Specific visualization capabilities for various object types
- Native model formats for DEM and analysis mask objects
- Site-specific PFT list implementation details
- General configuration settings for admin control
- MSS credential handling approach