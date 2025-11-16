# PEPPOL Deliverable D2.1: Functional and Non-Functional Requirements Specification for the VCD

## 1. Introduction

### 1.1 Purpose
This document specifies functional and non-functional requirements for the Virtual Company Dossier (VCD) as part of the PEPPOL project. The VCD aims to provide interoperable solutions for economic operators to utilize company information already registered somewhere and submit this information electronically to any public sector awarding entity from a different Member State when applying for public contracts.

### 1.2 Project Scope
The VCD focuses on interoperable solutions for economic operators in any European country to:
- Utilize company information already registered somewhere
- Submit this information electronically to any public sector awarding entity from a different Member State
- Address company information requirements for public procurement procedures

## 2. Overall Description

### 2.1 Product Perspective
The VCD is designed as a four-stage maturity model solution that supports cross-border submission of evidences via VCD packages. It connects with:
- European Service Provider ensuring pre-VCD mapping functionality
- National VCD Service Providers implementing VCD compilation for economic operators in their countries
- PEPPOL WP8 transport infrastructure for cross-border evidence submission

### 2.2 Product Features
- Pre-VCD mapping tool (Stage 1): Provides mappings between European criteria and national evidences
- VCD simple package (Stage 2): Basic VCD package compilation and submission
- VCD advanced package (Stage 3): Enhanced features including recompilation, merging, and context-specific data
- VCD network package (Stage 4): On-demand retrieval of attestations

### 2.3 User Classes and Characteristics
1. Economic Operators: Companies submitting evidence for public procurement
2. Contracting Authorities: Public sector entities receiving and evaluating evidence
3. Issuing Bodies: Entities providing certificates and attestations
4. National Service Providers: Host VCD systems and services
5. European Service Provider: Maintains pre-VCD mapping tool

## 3. System Features

### 3.1 Pre-VCD Mapping Tool (Stage 1)
Provides a semantic interoperability model supporting mutual recognition of qualification documents across Member States.

#### Major Features
- Mapping between national attestations and European criteria (Articles 45-50 of Directive 2004/18/EC)
- Provision of alternative means for evidencing criteria for foreign economic operators
- Tool to facilitate identification of evidences needed across countries
- Up-to-date mappings maintenance

#### Requirements
- Standard representation of European criteria for qualitative selection and exclusion
- Correspondence between national criteria and European criteria
- Template ensuring comparable and reliable mappings
- Formal adoption and approval procedure for compliance and mutual recognition
- Infrastructure providing mapping service
- Governing model ensuring liability, sustainability, and maintainability
- Accessibility for all relevant stakeholders

### 3.2 VCD Simple Package (Stage 2)
Establishes national VCD service providers hosting VCD systems to provide economic operators with services necessary to create early VCD packages.

#### Major Features
- VCD package structure definition containing evidence for economic operator suitability
- VCD system acting as single point of contact for economic operators
- VCD creation service compiling VCD packages from various data sources
- VCD transportation system for submitting packages to contracting authorities
- VCD viewing system for displaying package contents
- Identity and access management

#### Requirements
- Application and management of VCD accounts with sensitive economic operator data verification
- Initialization of VCD requests with tender-specific data
- Arrangement of VCD instances with compilation suggestions
- Collection of evidence from various sources (automated, semi-automated, manual)
- Compilation of VCD instances from different data formats
- Authentication to VCD transportation system
- Exchange of VCD packages between economic operators and contracting authorities
- Authentication to VCD viewing system
- View VCD packages with various data formats

### 3.3 VCD Advanced Package (Stage 3)
Enhances VCD capabilities with recompilation, merging, and context-specific data features.

#### Major Features
- Recompiling existing VCD packages with updated evidence
- Merging data from several consortium members into one VCD package
- Embedding context-specific data for decision support
- Improved VCD creation service

#### Requirements
- Context specific data collection and processing for all evidence types
- IT interfaces to issuing bodies providing machine interpretable evidence
- User interfaces for issuing bodies to provide context specific data
- Validation of provided context specific data
- Interfaces for retrieving context specific data from issuing bodies
- VCD system user-interface for initiating VCD advanced package creation
- Functionality to check consistency of existing VCD packages
- Merging capabilities for data from multiple VCD packages
- VCD re-compilation service with user-interface for initiating recompilation
- Decomposition of existing VCD packages
- Identification of outdated or obsolete evidences
- Retrieval of actual instances of outdated evidences

### 3.4 VCD Network Package (Stage 4)
Introduces on-demand retrieval of attestations and potential implementation of Article 52 of Directive 2004/18/EC.

#### Major Features
- On-demand retrieval of attestations sufficiently described through context specific data
- Opportunity for national VCD service providers to establish official lists of approved economic operators
- Mandating contracting authorities to request attestations on individual basis
- Storing attestations with referencing capabilities
- Retrieving attestations on demand
- Conflict resolution mechanisms
- Implementation of Article 52 provisions

#### Requirements
- Functionality enabling economic operators to mandate contracting authorities to request attestations
- Detection of attestations suitable for on-demand feature
- Functionality for National VCD Service Providers to store attestations
- Referencing mechanisms to attestations within VCD system
- Functionality to check contracting authority access rights
- Retrieval of attestations by contracting authorities
- Conflict resolution process initiation
- Functionality to approve attestations through validation data
- Access policies for economic operators mandating contracting authorities
- General reference structure and syntax definition
- Service-level agreements between parties involved
- Validation points establishment for Article 52 implementation

## 4. External Interface Requirements

### 4.1 User Interfaces
- Web-based interfaces for all VCD system components
- Single-sign-on functionality across connected systems
- User interfaces for different stakeholder roles (economic operators, contracting authorities, issuing bodies)
- VCD viewing interfaces for package contents display

### 4.2 Hardware Interfaces
- Standard computing hardware requirements
- Internet connectivity for cross-border communication
- x86 compatible CPU for performance-critical sections

### 4.3 Software Interfaces
- Integration with PEPPOL WP8 infrastructure
- Interfaces with existing eProcurement frameworks
- Connection to national issuing body systems
- Support for standard web service protocols

### 4.4 Communications Interfaces
- Secure communication channels for VCD transportation
- PEPPOL infrastructure for cross-border evidence submission
- Electronic addressability for all participating parties
- Discovery mechanisms for party addresses and capabilities

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements
- Response times for VCD package creation and submission
- System availability requirements for service providers
- Scalability to handle multiple concurrent users
- Processing time requirements for evidence collection

### 5.2 Safety Requirements
- Error handling with appropriate help messages
- System functionality with incorrect data/settings
- Data integrity during transmission and storage
- Protection against unauthorized access

### 5.3 Security Requirements
- Authentication mechanisms for all system users
- Confidentiality protection for sensitive economic operator data
- Secure transportation of VCD packages
- Non-repudiation of origin for business document instances
- Data integrity assurance during operations
- Time stamping for certification of relevant dates

### 5.4 Software Quality Attributes
- User-friendly interfaces suitable for users with minimal computer experience
- Comprehensive help documentation and tutorials
- Reliability in cross-border operations
- Maintainability through modular design
- Interoperability with existing systems and standards

## 6. Legal, Organisational and Semantic Framework

### 6.1 Organisational Framework
- Stakeholder analysis and management
- Utilization of existing national procedures and infrastructures
- Trust establishment through national authorities
- Conformance with pre-VCD mapping tool
- National freedom in implementing pilot solutions
- Support for Article 52 implementation
- Specification of evidence subsets by contracting authorities

### 6.2 Semantic Framework
- Semantic interoperability for evidential documents
- Correspondence between national and European criteria
- VCD specific characteristics (economic operator and tender specificity)
- Method for ensuring level of completeness
- Placeholders in VCD packages
- Semantics of evidence representation
- Visualization of VCD packages
- Implementation approach with regard to maturity stages
- Principle for including attestations in advanced stages

### 6.3 Legal Framework
- Equal treatment of foreign economic operators
- Minimum period of validity for VCD packages
- Equivalence between automated transformation and official translation
- Legal effect of subset criteria and evidences
- Scope of mutual recognition
- Correct implementation of directives into national procurement law
- Legal basis for exchanging validation data
- Requirements regarding service providers (European and National)
- Legal requirements for evidence collection
- Data protection compliance
- Separation of VCD package and tender
- Trust model between entities involved
- Legal validity of electronic documents and signatures

## 7. Technical Framework

### 7.1 Infrastructure Requirements
- Interrelation of governance models between WP2 and WP8
- Authentication of PEPPOL actors
- Allocation of identifiers for participants
- Identity management for all parties
- Addressability of participating organizations
- Discovery mechanisms for party information
- Access points to PEPPOL infrastructure
- Usage of infrastructure for VCD submission
- Confidentiality mechanisms for sensitive documents
- Integration with WP1 validation services
- Reliable transport mechanisms
- Security measures for document exchange
- Data integrity assurance
- Non-repudiation of origin support
- Time stamping capabilities
- Audit trail requirements

## 8. Pilot Implementation Concepts

### 8.1 Overall Approach
- European Service Provider implementation for pre-VCD mapping tool
- National VCD Service Provider implementations for stages 2+
- Cross-border submission of evidences via VCD packages
- Integration with national infrastructures for accessing issuing bodies

### 8.2 Austrian Implementation
- Stage 3 VCD advanced package solution
- Full pan-European interoperability
- Flexibility for legal and organizational changes
- Advanced SME support
- Ontology-based execution engine
- Four building blocks: UI/Workflow-System, osSso machine, SOA Engine, VCD packager

### 8.3 Italian Implementation
- Adaptation of current company's dossier builder to PEPPOL standards
- Focus on legal investigation and technical engineering
- Multi-stage approach conformance
- Document acquisition infrastructure improvement
- Evidence transformation from conventional to electronic form
- Certificate information extraction and management

## 9. Implementation Stages and Maturity Model

### 9.1 Stage 1: Pre-VCD Mapping
- Basic semantic interoperability model
- European criteria to national evidence mapping
- Transparency on cross-border tendering requirements
- Mutual recognition support

### 9.2 Stage 2: VCD Simple Package
- National VCD service provider establishment
- Basic VCD package structure
- Evidence collection from multiple sources
- Cross-border VCD submission capability

### 9.3 Stage 3: VCD Advanced Package
- Recompilation services
- Consortium VCD merging
- Context-specific data integration
- Enhanced decision support

### 9.4 Stage 4: VCD Network Package
- On-demand evidence retrieval
- Article 52 implementation support
- Validation value exchange
- Conflict resolution mechanisms
