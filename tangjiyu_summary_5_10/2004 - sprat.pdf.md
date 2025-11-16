# Security and Privacy Requirements Analysis Tool (SPRAT) - Requirements Specification

## 1. Introduction

SPRAT is a tool designed to assist analysts in privacy and security policy analysis, goal mining, reconciliation, and management. It maintains a repository of goals and scenarios traceable to source policies, supporting automatic multi-user analysis results comparison. The tool targets requirements engineers, Chief Privacy Officers (CPO), policy analysts, and auditors.

## 2. Module Breakdown

SPRAT comprises 9 main modules:
1. User Access Module (UAM) - Manages user access levels (Administrator, Project Manager, Analysts, Guest)
2. Goal Specification and Management Module (GSM) - Supports goal management
3. Analysis Document Management Module (ADM) - Handles policy document management
4. Flesch Readability Module (FRE) - Calculates readability index of documents
5. Scenario Specification and Management Module (SSM) - Supports scenario management
6. Requirements Specification Module (RS) - Manages system requirements
7. Legal Compliance Module (LC) - Handles legal compliance aspects
8. Requirements-level Access Control Analysis Framework Module (RACAF) - Supports access control analysis
9. P3P Module - Extracts goals from P3P privacy policies

## 3. Key Functional Requirements

### 3.1 User Access Module (Priority 1)
- Administrator privileges: Create user groups, manage users, reset passwords, disable access
- Project Manager privileges: Manage policies, domains, assign analysts, export data, save repository versions
- Analyst privileges: Select policies, manage goals/scenarios/requirements, view access control policies
- Guest privileges: View restricted repository information

### 3.2 Goal Specification and Management (Priority 1-3)
- Add/update/delete goals with detailed attributes (ID, description, taxonomy, subject classification, actor, etc.)
- Classify goals as policy or scenario goals, observable or unobservable
- Support multiple subject classifications per goal
- Maintain traceability links between goals and source policies
- Display goal occurrences and context information
- Search goals by attributes

### 3.3 Analysis Document Management (Priority 2-3)
- Add/modify/delete analysis documents and assign domains
- Create document types and domains
- Display documents alphabetically within domains
- Support multi-user analysis results comparison

### 3.4 Scenario Management (Priority 1-3)
- Add/edit/delete scenarios with detailed elements (name, sources, actors, events, actions, etc.)
- Reuse scenarios
- View scenario elements and associated goals
- Generate lists of scenarios by shared attributes

### 3.5 Requirements Management (Priority 3)
- Specify/add/edit/delete requirements
- Associate requirements with goals and constraints
- Use templates for requirement specification

### 3.6 RACAF Module (Priority 1-3)
- Data Analysis: Add objects, associate privacy preferences, support hierarchical data structures
- Task Analysis: Derive access control elements, view scenario elements with access control rules
- Organizational Structure: Represent hierarchical structures, boundaries via roles, actor relationships
- Information Analysis: Analyze data flows within/across organizational boundaries
- Access Control Policy: Support Ponder language specification
- Formal Verification: Partial support for translating Ponder policy to Alloy specifications

### 3.7 P3P Module (Priority 3)
- Extract goals data-usage information from P3P policies/preferences
- Capture mined information into databases
- Evaluate policy information against user preferences

## 4. System Requirements

### 4.1 Security Requirements (Priority 1)
- Secure password storage
- Secure user login
- Generate access logs for all add/delete/edit actions

### 4.2 Non-Functional Requirements
- Different access levels for users and projects
- Database for organized data storage
- Support for empirical studies through logging

## 5. Priority Classification

1. High - Critical requirements that may cause system failure if not satisfied
2. Medium - Important but non-critical requirements
3. Low - Desirable but non-essential requirements
