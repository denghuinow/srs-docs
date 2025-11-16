# BLIT102 System Functional Requirements Specification

## 1. Introduction

### 1.1 Purpose
This Functional Requirements Specification (FRS) captures changes in functionality for the BLIT102 system re-writing effort, part of the xxx Enhancements project. All functionalities for the new system are documented in this FRS. Undocumented requirements are considered out of scope.

### 1.2 Scope
The project is limited to enhancements and critical defects in the core Laboratory Information System (LIS). Scope includes system architecture enhancements to facilitate efficient growth of the system and business operations. Functional issues and requirements gathered and validated in Requirements Gathering and Validating Sessions are documented in this FRS.

## 2. Specific Requirements

### 2.1 Functionality

#### 2.1.1 Module: Admin

##### 2.1.1.1 Use Case: xxx Page, UC ID: UC_RR_xxx_xxx_000
- System shall display hyperlinks and descriptions for users to perform desired functions
- User shall view listed hyperlinks and descriptions
- User shall choose a function by clicking hyperlink
- System shall display desired operational page after hyperlink click

##### 2.1.1.2 Use Case: xxx Page, UC ID: UC_RR_xxx_xxx_000

###### Action: Create/Add User
- Admin users shall add/create new users and associate specified roles
- System shall display error if new user exists in system
- System shall display error if new user is inactive in Active Directory
- System shall display xxx tab as default tab
- User shall create/add new user manually or from template
- User records inherit role settings from template when created from template
- User shall add additional roles manually when creating from template
- System saves user info with associated roles and divisions
- System searches user display name and user name columns to verify existence
- System searches Active Directory to verify user status when creating new user

Additional requirements:
- System generates confirmation message after saving data
- System generates warning/caution messages after cancel/close button click
- User may click any tab to commence adding process (xxx Tab default)
- Required fields marked with red asterisk
- User may save or cancel data when creating new user
- System clears data if user clicks Cancel during creation
- System directs user to xxx Page if user clicks close without entering data
- User must associate at least one role, division, designator code, and lab location
- User must fill required fields (User Name and Display Name)
- System generates error/warning if required criteria missing

### 2.2 Usability

#### 2.2.1 User Interface Guidelines
- Project Team must demonstrate UI mockups to stakeholders early in development
- Project Team must permit reasonable UI adjustments by stakeholders when schedule permits

### 2.3 Reliability

#### 2.3.1 System Downtime
- Updates scheduled only on Tuesdays between 7pm and 7am

### 2.4 Performance

#### 2.4.1 Quality Assurance
- Project Team performs testing against new functionality before production release
- Project Team allows reasonable time for User Acceptance Testing (UAT) before production deployment

### 2.5 Supportability

#### 2.5.1 Coding Standards
- Development Team defines and follows coding standards consistently
- Development Team adjusts existing code to follow standards only if modification required

#### 2.5.2 Maintainability Standards
- System logs errors, warnings, and informational messages to external log file
- Development Team adjusts existing code to use external log file only if modification required
- System logs error message to external data file when user directed to error page
- System sends notification email to Client Services distribution list when user directed to xxx error page

### 2.6 Design Constraints

#### 2.6.1 Development Platform
- Development Team develops using xx language on .NET 3.5 Platform
- Development Team utilizes open source frameworks instead of proprietary components where appropriate
- System continues to depend on single SQL Server 2008 database

#### 2.6.2 Production Releases
- Technical Owner/Lead provides signoff before any build deployed to production

#### 2.6.3 Development Process
- Development Team performs weekly integrations and deploys to Staging environment
- Development Team labels every scheduled build in source control system
- Development Team performs scheduled builds using code checked out with defined label
- Development Team develops and sends release notes via email after Staging deployment
- Technical Lead performs code reviews before changes committed to source control
- QA/QC Team performs regression testing against all scheduled builds

### 2.7 Online User Documentation and Help System Requirements

#### 2.7.1 Robohelp Tool
- RoboHelp version 8 creates online help hypertext links
- System displays "Help" hyperlink at top right corner on each user screen
- Help topic pop-up windows contain same content as user manuals

Requirements:
- System provides pop-up window with page information and supporting help topics
- System displays "[system name] Overview" as default help topic
- Users navigate help topics via hypertext links in left frame
- System displays company logo in top right of help pages
- Help pages use specified color scheme and background
- System provides search ability for specific topics
- System provides index for in-depth topic search
- System provides Glossary for industry-related terms

### 2.8 Interfaces
(Requirements not specified in detail)

### 2.9 Applicable Standards

#### 2.9.1 HIPAA Compliance
- System retains existing HIPAA compliance capabilities
- System follows HIPAA compliance in new functionality

### 3. Glossary
(No terms defined)
