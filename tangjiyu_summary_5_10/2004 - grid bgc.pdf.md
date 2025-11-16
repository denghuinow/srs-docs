# Grid-BGC Application Version 1.0 Software Requirements Specification

## 1. Introduction

### 1.1 Purpose
This project is to develop a grid-based software infrastructure to support bio-geo-chemical modeling. The application will use the Daymet surface weather interpolation engine for generating gridded surface weather datasets from observation data records. The Biome-BGC model will be used to perform BGC modeling activities.

The system shall provide a graphical user interface to all functions of the system. Grid technologies shall be utilized to provide secure and reliable communications to remote computing resources.

### 1.2 Project Scope and Project Features
The system will organize data in two types of logical grouping elements:
1. Objects - elements that group related data elements in the system and serve as the mechanism for data sharing and reuse.
2. Projects - elements that group specific objects together to perform a unit of work.

### 1.3 References
Reference the proposal document.

## 2. Overall Description

### 2.1 Product Perspective
This project is to develop a grid-based software infrastructure to support bio-geo-chemical modeling. The application will use the Daymet surface weather interpolation engine for generating gridded surface weather datasets from observation data records. The Biome-BGC model will be used to perform BGC modeling activities.

The system shall provide a graphical user interface to all functions of the system. Grid technologies shall be utilized to provide secure and reliable communications to remote computing resources.

### 2.2 User Classes and Characteristics

#### 2.2.1 Scientists (Favored)
Scientific users are the favored and primary user class for the system. Scientific users will use the system to manage input data, run simulations, visualize results, and manage output data.

#### 2.2.2 Portal Administrator
The portal administrator will be in charge of managing the day to day operations of the system. This user will be responsible for managing user accounts, managing user runs if needed, and general portal settings and monitoring.

#### 2.2.3 Data Users (Lowest Priority)
Data users are researchers who need to use simulation output but who do not have the ability to initiate simulations.

### 2.3 Typical Usage Scenarios
- Daymet Modeling Run
- BiomeBGC Modeling Run
- Visualization
- Analysis
- Data download
- Data Publication

### 2.4 Operating Environment

#### 2.4.1 Web Portal
The web portal components shall integrate into the Dataportal Web Server at NCAR.

#### 2.4.2 Compute Nodes
The compute node software shall be developed and deployed for the Hemisphere Linux cluster at CU.

#### 2.4.3 Client User Interface
The system shall provide a web based (portal) user interface for all aspects of the system.

### 2.5 Design and Implementation Constraints

#### 2.5.1 The system shall use the Globus toolkit.

#### 2.5.2 NCAR Security policies and constraints.

### 2.6 User Documentation

#### 2.6.1 Online Help Manual
Full online manual with major sections listed in TOC.

#### 2.6.2 Context sensitive online help manual
Each page will have a context sensitive link to the help system. Each context sensitive help page will be displayed in a pop-up window. The link will display the topic relevant for the page. The TOC will not be displayed in the context sensitive view.

### 2.7 Assumptions and Dependencies

#### 2.7.1 The system will use the NCAR Mass Storage System for all file based storage.

## 3. System Features

### 3.1 User Accounts
Access to the functional areas of the system will be controlled by user accounts.

#### 3.1.1 Gatekeeper Accounts
1. All GridBGC users shall be required to have valid NCAR Gatekeeper accounts to use the system.
2. Not all Gatekeeper account holders will have access to the GridBGC system. Users must be approved by the GridBGC administrator(s) for access.

#### 3.1.2 User Account Information
1. The system shall retrieve all user information from the Gatekeeper account system.

User accounts will have the following status states:
- Pending Confirmation
- Pending Approval
- Active
- Locked
- Deleted (Place holder for deleted accounts but needed to maintain internal data structures)

#### 3.1.3 User Roles
The system shall support the following user roles:
1. User – General end user of the system
2. Administrator – Has additional permissions to administer the operation of the system.

#### 3.1.4 Account Creation
End users can apply for an account directly through the web portal.
1. Users must enter all required fields
2. The user must enter their NCAR Gatekeeper username.

#### 3.1.5 User Functionality

##### Apply for an account
End users can apply for an account directly through the web portal.

##### View account details
The user can view their current account details. Password will not be displayed.

##### Delete account
1. The system shall provide a means to request that the user account be deleted from the system.
2. The system shall notify the portal admin(s) about the delete requests.

##### Login to system
1. The system shall require the user to enter their username and password to login to the system.
2. The user shall be prompted at the beginning of the session for their credentials, once logged in they will not be prompted for additional or different credentials.
3. All login actions shall be protected by using secure data channels.
4. The system shall lock the account after 3 login attempts. This will require portal admin action to unlock the account.
5. Admin users will be authenticated against the portal database.
6. Users will be authenticated against the NCAR Gatekeeper system.

#### 3.1.6 Administrative Functions

##### Approve Accounts
1. Portal Admin(s) will receive e-mail notification when new accounts are ready for review.
2. Display a list of all accounts pending review.
3. Approve specific account.
4. Reject specific account.

##### Assign Template Submission Privileges
The system shall allow portal administrators the ability to control template submissions rights.

##### List Accounts
The portal admin shall have the ability to list the user accounts in the system:
1. List all user accounts
2. List accounts pending approval
3. List all account deletion requests
4. List all locked accounts

##### Delete Accounts
1. Delete a specific user account. This operation will not be reversible.
2. Data removal:
   - Templates: All user submitted templates will NOT be deleted from disk.
   - Shared Objects: All shared object that have NOT been referenced by dependant projects will be deleted.
   - All other objects/projects: Will be deleted completely from the system.

##### Lock/Unlock accounts
1. The admin can lock accounts:
   - The user will be notified via e-mail
   - Further logins will not be permitted until unlocked
   - Currently executing jobs will continue to run until the job ends or terminated by the portal admin
2. The admin can unlock accounts:
   - Once unlocked the user can login to the system and resume use

##### Job Management
1. The portal admin will have a display of all running jobs sorted by user
2. The status of each job and tile will be visible to the portal admin
3. The portal admin shall have the ability to terminate any user's running jobs.

##### Assign User Roles
1. The system shall assign all user accounts to the scientist role by default.
2. The system shall allow the portal admin to change a user's role in the system.

##### Resource Quotas (Lowest Priority)
Review the need to implement resource quotas if time permits at the end of the project.

### 3.2 Data Organization
The system will organize the system in to types of logical grouping elements:
1. Objects
2. Projects

#### 3.2.1 Objects
Objects will be elements the group related data elements in the system. Objects will be the mechanism by which data is shared and reused throughout the system.

#### 3.2.2 Projects
Projects will be elements that group specific objects together to perform a unit of work.

#### 3.2.3 Data Element Relationships

#### 3.2.4 Data Integrity
1. The system shall prevent the user from changing object/project values once that project has been used in a model run. This is to preserve the input values that produced a certain set of output values.
2. Each object/project will have states which control when the user can change product values.
3. The system shall support the following states:
   - Unlocked – The user can make changes as desired.
   - Locked – The user can not make any changes
   - Invalidated – A dependency has been modified in someway and object/project may no longer have valid inputs or outputs.

### 3.3 Objects
Objects will manage datasets and references to other logically related datasets.

#### 3.3.1 The system shall support 3 types of objects

##### List Objects
1. List objects will contain arbitrary points of data
2. The system will NOT enforce any spatial constraints on list datasets

##### Grid Objects
1. Grid objects will contain rectangular grid datasets.

##### Parameterization Objects
1. Parameterization projects will contain model specific parameter data

#### 3.3.2 Sharing
1. Users can select to share specific objects with other users.
2. Users can specify which users to share the object with:
   - All users
   - Select specific users within the system
3. When a shared project is referenced in the system the underlying datasets will NOT be copied.
4. Once a shared project has been referenced elsewhere in the system it will be in a locked state.

#### 3.3.3 Merging Objects
Users can create new dataset project by merging existing objects:
1. Project must be of the same type, list or grid
2. Merging operation will always be used to create new datasets from two existing datasets.
3. Merge sources can be:
   - Current users existing projects
   - Other users projects that have been shared
4. No data validation will be done at this stage:
   - Will not check for duplicate data
   - Will not check for spatial relationships of data.
   - Will not check for missing values
5. Full copies of the source datasets will be made during the creation of the merged dataset.
6. The system shall display dataset metadata to allow users to screen data prior to merging operations.

### 3.4 Projects
Project will have two main functions within the system; contain references to supporting datasets and serve as the simulation run control element.

#### 3.4.1 Project Type
1. The user shall specify the type of project during initial setup; either List or Grid
2. The system shall only allow the user to reference datasets of the same type as specified in the project

#### 3.4.2 Collaboration
1. Projects cannot be shared or be templates.

#### 3.4.3 New Project Creation
1. The user can create new projects:
   - List data projects
   - Grid projects

#### 3.4.4 Referenced Objects
1. The system shall allow the user to only select referenced objects that are of the appropriate type
   - List and Grid types matching shall be enforced.

### 3.5 Template Objects
System templates will provide a means of sharing expert knowledge within the portal.

#### 3.5.1 Object Types
Not all Object types shall support templates, see specific object details for more details.

#### 3.5.3 Access Control
Any user of the system shall be able to use a template.

#### 3.5.4 Submission
Only users with template submission privileges can submit new templates.

#### 3.5.5 Editing
Once a template has been submitted it can no longer be edited.

#### 3.5.6 Deletion
The system shall allow the following users to delete templates from the system:
1. Portal Admin(s)
2. The user who originally created the template

#### 3.5.7 Display
1. The system shall provide portal admin(s) with a list of all system templates by project type.
2. The system shall provide users with a list of their templates in the system.

#### 3.5.8 Template Use
1. Any time a template is used the user shall get their own full private copy of the data
2. The user must supply a new project name when using a template before saving the project.
3. If the template references a non-shared data resource the user must choose a new dataset before saving the project.

### 3.6 Projection Object
This object defines the projection parameters for a dataset.

#### 3.6.1 Collaboration
Projection Objects can be templates.

#### 3.6.2 Support Projection Types
The system shall support the following projection types:
1. Geographic
2. UTM
3. Albers Conical Equal Area
4. Lambert Conformal Conic
5. Lambert Azimuthal Equal Area
6. Interrupted Goode Homolosine
7. Interrupted Mollweide

#### 3.6.3 Creation
1. New Blank
2. Copied from system template.

#### 3.6.4 Read
1. View List of projection projects
2. View Projection Details

#### 3.6.5 Update
1. The project must be in an unlocked state
2. The user can change the parameter values
3. The user can NOT change the projection type

#### 3.6.6 Delete
1. If the project is in an unlocked state:
   - The project and all related data can be deleted.
2. If the project is in a locked state:
   - The user shall be prompted to delete all projects that reference this project following the candidate project deletion rules.

#### 3.6.7 Data Downloads
This information will not be downloadable by the user.

### 3.7 Grid Registration Object

#### 3.7.1 Collaboration
Projection Objects can be templates.

#### 3.7.2 Creation
1. New Blank
2. Copied from system template

#### 3.7.3 Read
1. View List of Grid Registration objects
2. View Grid Registration Details

#### 3.7.4 Update
1. The project must be in an unlocked state
2. The user can change the parameter values

#### 3.7.5 Delete
1. If the object is in an unlocked state:
   - The project and all related data can be deleted.
2. If the object is in a locked state:
   - The user shall be prompted to delete all projects that reference this object following the candidate object deletion rules.

#### 3.7.6 Data Downloads
This information will not be downloadable by the user.

### 3.8 Surface Observation Object
This dataset contains observed surface weather data. This is one the primary input data sets in the Daymet model.

#### 3.8.1 Referenced Objects
None

#### 3.8.2 Collaboration
Projection Objects can be shared.

#### 3.8.3 Supported Object Types
List

#### 3.8.4 Creation
1. New Blank Object:
   - User must upload data files to the system
   - Reference required NetCDF file convention
   - Specify required archive structure
2. Merge existing objects:
   - The user can combine 2 discrete objects into 1 new singular object
   - The system shall not perform any checking or conversion
3. Subset existing object:
   - The user can create a new object from a subset of a single existing object.
   - How is the subset performed specified?

#### 3.8.5 Read
1. The system shall display a list of all the objects the user currently has in the system
2. The system shall display the object details:
   - Display all metadata associated for the object
   - The system shall display all the stations for object
   - The system shall display all the data values for each station

#### 3.8.6 Update
1. Address the invalidation logic for locked state....
2. Delete the project and start over.

#### 3.8.7 Delete
1. The system shall allow the user to delete an unlocked project.
2. Address the invalidation logic for locked state....
3. The system shall allow the user to delete a locked project under the following conditions:
   - The user has selected to delete all associated projects that reference the project.
4. The system shall delete all associated input and model output data for this project during deletion.

#### 3.8.8 Visualization (Low Priority)
TBD - Later

### 3.9 Site Data Object

#### 3.9.1 Referenced Datasets
None

#### 3.9.2 Collaboration
Site Data Objects can be shared.

#### 3.9.3 Supported Object Types
1. List
2. Grid

#### 3.9.4 Creation
1. New Blank Object:
   - User can upload files to the system
   - List File Formats
   - Specify required archive structure
2. Merge existing objects
3. Subset of existing object:
   - Data extraction process:
     - The user can enter a series of data points
     - The user can select a source object
     - The system shall extract the specified points from the dataset and store them in a new dataset in the system.

#### 3.9.5 Read
1. The system shall display a list of all the objects the user currently has in the system
2. The system shall display the object details:
   - Display all metadata associated for the object

#### 3.9.6 Update
1. Grid Type:
   - Delete and start over.
2. List Type:
   - The system shall provide user interface to manage the observation points
   - The system shall allow a user to add new data points
   - The system shall allow a user to edit existing data points
   - The system shall allow a user to delete existing data points

#### 3.9.7 Delete
1. The system shall allow the user to delete an unlocked object.
2. The system shall allow the user to delete a locked object under the following conditions:
   - The user has selected to delete all associated objects/projects that reference the project.
3. The system shall delete all associated input and model output data for this project during deletion.

#### 3.9.8 Visualization (Low Priority)
TBD - Later

### 3.10 Daymet Parameterization Object
This project contains all the parameterizations values for a daymet model run.

#### 3.10.1 Collaboration
Daymet Parameterization Objects can be templates.

#### 3.10.2 Creation
1. New Blank Object:
   - The system shall provide a user interface to manage all parameterization values.

#### 3.10.3 Read
1. The system shall display a list of all the objects the user currently has in the system
2. The system shall display the object details:
   - Display all metadata associated for the object

#### 3.10.4 Update
Go through the locked / invalidation sequence

#### 3.10.5 Delete
Go through the locked / invalidation sequence

### 3.11 DEM Object
Object that contains DEM datasets and the associated Analysis mask data.

#### 3.11.1 Collaboration
DEM Objects can be shared.

#### 3.11.2 Object Types
1. List datasets
2. Grid datasets

#### 3.11.3 Creation
1. New Blank Object:
   - User can upload files to the system
   - DEM Datasets:
     - NetCDF
     - What is the native model format?
   - Analysis Masks:
     - NetCDF
     - What is the native model format?
   - Other Datasets?
2. Merge existing objects

#### 3.11.4 Read
1. The system shall display a list of all the objects the user currently has in the system
2. The system shall display the object details:
   - Display all metadata associated for the object

#### 3.11.5 Update
Go through the locked / invalidation sequence

#### 3.11.6 Delete
Go through the locked / invalidation sequence

#### 3.11.7 Visualization (Low Priority)
TBD – Later

### 3.12 Analysis Mask Object

#### 3.12.1 Collaboration
Analysis Mask objects can be shared.

#### 3.12.2 Object Types
1. List datasets
2. Grid datasets

#### 3.12.3 Creation
1. New Blank Object:
   - User can upload files to the system
   - DEM Datasets:
     - NetCDF
     - What is the native model format?
   - Analysis Masks:
     - NetCDF
     - What is the native model format?
   - Other Datasets?
2. Merge existing objects

#### 3.12.4 Read
1. The system shall display a list of all the objects the user currently has in the system
2. The system shall display the object details:
   - Display all metadata associated for the object

#### 3.12.5 Update
Go through the locked / invalidation sequence

#### 3.12.6 Delete
Go through the locked / invalidation sequence

#### 3.12.7 Visualization (Low Priority)
TBD – Later

### 3.13 Daymet Project
This project aggregates all input objects and simulation control functions.

This project is the defining project for determining whether the project chain is list or grid based.

#### 3.13.1 Referenced Objects
1. Site Data Object
2. Surface Weather Data Object
3. Projection Object:
   - Must be the same as other input objects
4. Registration:
   - Must be the same as other input objects
5. DEM Object

#### 3.13.2 Templates
This project can NOT be a template.

#### 3.13.3 Sharing
This project can NOT be shared.

#### 3.13.4 Creation
New Blank Project

#### 3.13.5 Read
1. The system shall display a list of all the projects the user currently has in the system
2. The system shall display the project details:
   - Display all metadata associated for the project

#### 3.13.6 Update
1. The system shall allow the user to delete an unlocked data project.
2. TODO – Reference the whole project dependency flow....

#### 3.13.7 Delete
1. The system shall allow the user to delete an unlocked project.
2. The system shall allow the user to delete a locked project under the following conditions:
   - The user has selected to delete all associated projects that reference the project.
3. The system shall delete all associated input and model output data for this project during deletion.

#### 3.13.8 Model Runs
1. The system shall allow user to start a new model run:
   - The system shall display a list of computational resources to select from.
   - The system shall provide the user with an approximate execution time estimate based on the computational resource selected.
2. The system shall allow the user to monitor and control model runs:
   - The system shall display a list of runs currently active for the user
   - The system shall display the overall run status
   - Daymet model runs shall be monitored on a tile by tile basis:
     - The system shall display the list of tiles for a run.
     - The system shall maintain the following information for each tile:
       - Status – Queued, Running, Complete, Error
       - The system shall save and display Stdout messages.
       - The system shall save and display Stderr messages.
3. The system shall allow the user to terminate a model run:
   - The system shall delete all output data associated with the run:
     - Cached input files
     - Temporary files
     - Output files
4. The system shall allow a user to restart a model run:
   - The system shall only permit a run to be restarted under the following conditions:
     - The previous instance has completed
     - The previous instance has been terminated
   - The system shall delete all previous model output prior to starting the run.

### 3.14 Daymet Output Object
This is the object that will contain the output data for a daymet run......

#### 3.14.1 Collaboration
Daymet Output Objects can be shared.

#### 3.14.2 Creation
The systems shall automatically create this object for completed simulation runs

#### 3.14.3 Read
1. Display a list of objects for a user
2. Display the details of each object
3. List all tiles for a object.

#### 3.14.4 Contained datasets
1. Cross Validation Output
2. Model Weather Data output

#### 3.14.5 Deletion
Reference: the invalidation logic flow....

#### 3.14.6 Data Downloading
1. The system shall allow the user to download the output data from the portal:
   - The system shall display a list of all the output tiles to the user.
   - The system shall allow the user to download the data files on a tile by tile basis.
   - The system shall allow the user to download the data in the native system formats and conventions only.

### 3.15 Plant Functional Type Object

#### 3.15.1 Sharing
Plant Functional Type Objects can be shared.

#### 3.15.2 Templates
Plant Functional Type Objects can NOT be templates.

#### 3.15.3 Creation
1. New Blank Object:
   - User can upload files to the system:
     - EPC File Format
     - Raw ASCII file format, not archived.
   - User can hand enter the values

#### 3.15.4 PFT Id's
User can hand enter the PFT Id number. This is so it can be related back to a site data project.

#### 3.15.5 Read
1. List user's objects
2. List object values [list object only]

#### 3.15.6 Update

#### 3.15.7 Delete
Reference deletion logic.

#### 3.15.7.1 Download
1. The system shall allow the user to download the data in an EPC file format.

### 3.16 BiomeBGC Site Data Object
This will encapsulate the site data specific for the BiomeBGC runs....

#### 3.16.1 Collaboration
Projection Objects can be shared.

References:
- Projection
- Registration

### 3.17 Output Specification Object
The biome bgc model has approximately 700 possible output variables. It is not realistically possible to use all the 700 output variables to perform meaningful analysis.

#### 3.17.1 Collaboration
Output Specification Objects can be templates.

#### 3.17.2 User Interface
The system shall provide a graphical user interface to manage the output parameters:
1. Parameter Categories:
   - The system shall provide 1 level of parameter categorization
   - The system shall provide a list of all parameters for each category
   - The system shall allow the user to select individual parameters as needed.
2. Selected Categories:
   - The system shall provide a display of the categories a user currently has selected.
   - The system shall provide a method to add new categories to the project.
   - The system shall provide a method to remove categories from the project.

#### 3.17.3 Creation
1. New Blank Object
2. Copy other user's object

#### 3.17.4 Read
1. The system shall display the list of objects the user currently has.
2. The system shall allow the user to view the details of a specific object.

#### 3.17.5 Update
1. The system shall allow the user to modify an unlocked object.

#### 3.17.6 Delete
1. The system shall allow users to delete unlocked objects.
2. The system shall allow users to delete locked objects under the following conditions:
   - The user shall be able to choose to delete all objects referencing this object.

### 3.18 Nitrogen Deposition Object

#### 3.18.1 Collaboration
Nitrogen Deposition Objects can be templates.

#### 3.18.2 Object Types Supported
1. List Datasets
2. Grid Datasets

#### 3.18.3 Creation
1. New Blank object:
   - User can upload files to the system:
     - List File Formats
     - Specify required archive structure
   - User can hand enter the values [list project only]:
     - Provide GUI interface for entering values
2. Merge existing list objects

#### 3.18.4 Read
1. List user's objects in the system
2. List individual object details

#### 3.18.5 Update
1. Grid objects:
   - Cannot be updated, must delete/create new.
2. List Objects:
   - Unlocked projects can be edited via online GUI

#### 3.18.6 Delete
1. The system shall allow the user to delete unlocked objects.
2. The system shall allow the user to delete locked objects.
   - All dependant objects/projects shall be invalidated

#### 3.18.7 Invalidated Objects
1. The system shall change the project to an unlocked state.
2. Invalidate all dependant projects.

### 3.19 Disturbance Objects
A disturbance object contains the information representing climate factors that influence the biome-BGC model. This includes information such as fires and deforestation events.

A disturbance project will have a series of events.
Each disturbance project can have an unlimited number of events
Each event will have a particular date in time associated with it.
An event occurs at a particular point in time, it does not have an associated duration.

The system shall support the following types of events:
1. Fire
2. Deforestation

The user shall specify the intensity value for the event.

#### 3.19.1 Collaboration
Projection Objects can be templates.

#### 3.19.2 Creation
The user shall be able to create a new disturbance object

#### 3.19.3 Read
1. The system shall list the user's objects in the system
2. The system shall list the object details

#### 3.19.4 Update
1. Unlocked Objects:
   - The system shall allow users to edit unlocked objects
2. Locked Objects:
   - The system shall allow users to edit locked objects
   - The system shall invalidate dependent objects

#### 3.19.5 Delete
1. The system shall allow the user to delete unlocked objects.
2. The system shall allow the user to delete locked objects.
   - All dependant objects/projects shall be invalidated

### 3.20 BiomeBGC Project

#### 3.20.1 Referenced Projects
1. Daymet Output Object
2. BiomeBGC Site Data
3. PFT Object
4. Output Specification Project

#### 3.20.2 Simulation Topology
1. The system shall allow the user to define a simulation topology
2. The user shall be able to create the following topology options:
   - 1 Site x 1 PFT
   - 1 Site x all PFT's
   - All Sites x 1 PFT's
   - All Sites x All PFT's
   - n Sites x 1 PFT
   - n Sites x All PFT's
   - n Sites x n PFT's
   - 1 Site x n PFT's
   - All Sites x n PFT's
   - Site Specific PFT List (number and weight) – TBD - What is this?

#### 3.20.3 Creation
The system shall allow the user to create new blank projects

#### 3.20.4 Read
1. The system shall list all the user's projects in the system
2. The system shall display all the project details

#### 3.20.5 Update
1. The system shall allow the user to change the project details for unlocked projects.
2. The system shall allow the user to ability to invalidate a locked project:
   - Will this trigger all running jobs to be terminated?
   - This will trigger all downstream projects to be invalidated.

#### 3.20.6 Delete
1. The system shall allow the user to delete unlocked projects.
2. The system shall allow the user to delete locked projects.
   - All dependant objects/projects shall be invalidated

#### 3.20.7 Model Runs
1. The system shall allow user to start a new model run:
   - The system shall display a list of computational resources to select from.
2. The system shall allow the user to monitor and control model runs:
   - The system shall display a list of runs currently active for the user
   - The system shall display the overall run status
   - BiomeBGC model runs shall be monitored on a tile by tile basis:
     - The system shall display the list of tiles for a run.
     - The system shall maintain the following information for each tile:
       - Status – Queued, Running, Complete, Errror
       - The system shall save and display Stdout messages.
       - The system shall save and display Stderr messages.
3. The system shall allow the user to terminate a model run:
   - The system shall delete all output data associated with the run:
     - Cached input files
     - Temporary files
     - Output files
4. The system shall allow a user to restart a model run:
   - The system shall only permit a run to be restarted under the following conditions:
     - The previous instance has completed
     - The previous instance has been terminated

#### 3.20.8 Invalidated Projects
1. The system shall change the project to an unlocked state.
2. Invalidate all dependant projects.
3. The system shall delete the output data project if created:
   - Delete all the files from disk storage as well.

### 3.21 BiomeBGC Output Object
This is the object that will contain the output data for a BiomeBGC run......

#### 3.21.1 Sharing
BiomeBGC Output Objects can be shared.

#### 3.21.2 Templates
BiomeBGC Output Objects can NOT be templates.

#### 3.21.3 Creation
The systems shall automatically create this object for completed simulation runs

#### 3.21.4 Read
1. Display a list of projects for a user
2. Display the details of each project
3. List all tiles for a project.

#### 3.21.5 Deletion
Reference: the invalidation logic flow....

#### 3.21.6 Data Downloading
1. The system shall allow the user to download the output data from the portal:
   - The system shall display a list of all the output tiles to the user.
   - The system shall allow the user to download the data files on a tile by tile basis.
   - The system shall allow the user to download the data in the native system formats and conventions only.

### 3.22 Daymet Visualization Project
TBD

### 3.23 BiomeBGC Visualization Project
TBD

### 3.24 Evaluation Project
TBD

### 3.25 Portal Administration

#### 3.25.1 Portal Metrics
1. Currently Registered Users
2. Data Metrics:
   - Number of files
   - Total storage size
   - Average File size
3. Computational Metrics:
   - # of jobs completed
   - # of jobs running
   - # of jobs queued
4. Template Metrics:
   - # of templates by object type
5. Objects/Projects Metrics:
   - # of Objects/Projects by type
   - # of Objects/Projects by type and by user
6. Shared Objects/Projects:
   - # of Objects/Projects by type
   - # of Objects/Projects by type and by user

#### 3.25.2 System Consistency Check
1. The system shall provide the portal admin a function to validate file references in the system correspond to actual files on the storage system.
2. The system shall generate a listing of any missing files.
3. Error Correction:
   - Could give the admin the ability to reset a file pointer to a new file on the storage system.
   - Could give the admin the ability to invalidate/delete the object that corresponds to the inconsistent file pointer
   - Other thoughts????

##### Compute Node Resources
1. The system shall list all the compute nodes
2. The system shall display the compute node resource details
3. The system shall allow the admin to manage compute resources:
   - Add new nodes
   - Lock a node
   - Unlock a node
   - Delete nodes
4. The system shall allow the admin to change compute node settings:
   - TBD – Determine what the admin can change....

##### System Settings
1. The system shall allow the portal admin to control the following system settings:
   - TBD – List all the general configuration settings the admin has control over.

## 4. External Interface Requirements

### 4.1 User Interfaces

#### 4.1.1 The web portal shall be usable in the following web browsers
1. Internet Explorer 6.0
2. Netscape 7.1
3. Safari 1.2.1?

#### 5 The system shall require the users enable cookies to use the system.

### 5.1 Hardware Interfaces

#### 5.1.1 NCAR Mass Storage System (MSS)
1. The system shall allow users the ability to store data on the NCAR Mass Storage System.
2. TBD – Can we use the users portal credentials to use the MSS or are we going to proxy the user through a central account with MSS access.

### 5.2 Software Interfaces

### 5.3 Communication Interfaces

## 6. Other Nonfunctional Requirements

### 6.1 Performance Requirements

### 6.2 Safety Requirements

### 6.3 Security Requirements

### 6.4 Software Quality Requirements

## 7. To Be Determined (TBD) Items

## 8. Appendix A: Data Dictionary and Data Model
Do example data dictionary

## 9. Appendix B: Analysis Models.
Workflows, GUI Maps, etc....
