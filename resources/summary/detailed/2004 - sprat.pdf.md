# Detailed Summary: Security and Privacy Requirements Analysis Tool (SPRAT)

## Background and Scope
SPRAT is a tool designed to assist analysts in mining, reconciling, and managing goals and scenarios derived from privacy and security policies for web-based systems. It aims to maintain a repository of goals and scenarios, ensuring traceability to source policies and supporting analysis to detect conflicts and misalignments. The tool targets requirements engineers, Chief Privacy Officers, policy analysts, and auditors. Non-goals include not being a general-purpose requirements management tool and not fully automating legal compliance verification.

## Stakeholders Matrix and Use Cases
*   **Administrator**: Manages user groups and system access, including creating project managers/analysts/guests and resetting passwords.
*   **Project Manager**: Oversees projects, manages policy documents and domains, assigns analysts, and controls data export/versioning.
*   **Analyst**: Performs core analysis by adding/updating/deleting goals, scenarios, requirements, and access control policies within assigned projects.
*   **Guest**: Views repository information with restrictions set by the project manager.
*   **Customer/Sponsor (Dr. Annie I. Antón)**: Provides high-level direction and requirements origin.
*   **Developer (Qingfeng He, William Stufflebeam)**: Provides technical input and specific requirements for module development (e.g., RACAF).

**Main Scenarios**: 1) Administrator creates user groups and accounts. 2) Project Manager imports a new privacy policy and assigns analysts. 3) Analyst extracts and classifies goals from an assigned policy. 4) Analyst creates a scenario linked to extracted goals. 5) Project Manager exports project data for comparison. 6) Guest views permitted policy information.
**Exception Scenarios**: 1) Analyst requests a new goal classification type for Project Manager approval. 2) Conflict detected during automatic multi-user analysis comparison requiring resolution.

## Business Process
**Main Process: Analyze a Privacy Policy**
1.  **Trigger**: Project Manager adds a new policy document to the repository and assigns a domain.
2.  Project Manager assigns the policy to one or more Analysts.
3.  Analyst logs in and selects the assigned policy.
4.  Analyst extracts and adds goals, providing ID, description, taxonomy, subject, actor, etc.
5.  Analyst classifies goals (e.g., policy/scenario, protection/vulnerability).
6.  Analyst may create or link scenarios and requirements to the goals.
7.  System maintains traceability links between goals and the source policy.
8.  **Output**: Enriched repository with traceable goals, scenarios, and requirements for the policy.

**Key Branch A: Multi-User Analysis Comparison**
1.  **Trigger**: Project Manager requests comparison for a policy.
2.  System withholds individual analyst classifications until each completes their work.
3.  System automatically compares classification results from multiple analysts.
4.  **Output**: Report highlighting differences for resolution.

**Key Branch B: Goal Reconciliation & Update**
1.  **Trigger**: Analyst identifies a goal to delete or replace.
2.  Analyst deletes or updates the goal.
3.  System automatically propagates changes, updating all linked policies.
4.  **Output**: Updated repository with consistent goal references.

## Domain Model
Core entities (≤8) with key fields:
*   **User**: UserID (unique), Role (required), Password (required, secure), ContactInfo.
*   **Project**: ProjectID (unique), Name (required), Manager (reference to User).
*   **PolicyDocument**: DocID (unique), Name (required), Domain (required), Text.
*   **Goal**: GoalID (unique), Description (required), Taxonomy, SubjectClassification, Actor, SourcePolicy (reference to PolicyDocument), Granularity.
*   **Scenario**: ScenarioID (unique), Name (required), Actors, Events, LinkedGoals (reference to Goal).
*   **Requirement**: ReqID (unique), Description, LinkedGoals (reference to Goal).
*   **AccessControlPolicy**: ACPID (unique), Subject, Object, Action.
*   **AnalysisLog**: LogID (unique), Timestamp (required), UserID (reference to User), Action, Object.

## Interfaces and Integrations
*   **Ponder Policy Editor**: External, Outbound. **Theme**: Access control policy specification. **Input**: Policy elements from SPRAT. **Output**: Formal Ponder policy. **SLA**: Interface stability for data exchange.
*   **Alloy Analyzer**: External, Outbound. **Theme**: Formal verification. **Input**: Translated specifications from Ponder policies. **Output**: Verification results. **SLA**: Partial automated translation support.
*   **Internal GUI Modules**: Internal, Bidirectional. **Theme**: User interaction for all modules (UAM, GSM, SSM, etc.). **Input**: User commands and data entry. **Output**: Data displays, templates, and analysis views. **SLA**: Consistent responsive interface.
*(Note: External system integrations like P3P/EPAL parsers are implied but not detailed in the provided text.)*

## Acceptance Criteria
*   **Capability: User Access Control**
    *   Given an Administrator is logged in, when they create a new Analyst account, then the account is created with 'Analyst' privileges and added to the specified user group.
    *   Given a Guest is logged in, when they attempt to view a policy not permitted by the Project Manager, then access is denied.
*   **Capability: Goal Management**
    *   Given an Analyst is viewing a policy, when they extract and add a new goal with a 'Protection' taxonomy, then the goal is saved with a unique ID and traceable link to the source policy.
    *   Given a Goal is deleted, when it was linked to multiple policies, then those policy records are automatically updated to remove the reference.
*   **Capability: Analysis Comparison**
    *   Given two Analysts have completed classifying goals for the same policy, when the Project Manager runs a comparison, then a report highlighting discrepancies in their classifications is generated.

## Non-Functional Metrics
*   **Performance**: User login authentication response time < 2 seconds. Generation of multi-user comparison reports for a standard policy < 30 seconds.
*   **Reliability**: System availability > 99% during business hours. All user actions (add/edit/delete) are logged for audit trails.
*   **Security**: Passwords stored securely (hashed) in the database. Secure user authentication required for all access levels.
*   **Compliance**: Supports analysis against regulations like HIPAA, COPPA, GLBA (via goal classification).
*   **Observability**: All critical actions (add, delete, edit) generate an access log with timestamp, user ID, action, and object.

## Milestones and Release Strategy
1.  Core database schema and User Access Module (UAM) implementation.
2.  Implementation of high/medium priority requirements for Goal (GSM) and Scenario (SSM) Management modules.
3.  Implementation of Requirements-level Access Control Analysis Framework (RACAF) module core features.
4.  Integration of Flesch Readability and basic Policy Document Management modules.
5.  Internal alpha testing with the development team.
6.  Beta release to a limited group of analysts (e.g., NCSU TPP.org) for feedback.

## Risk List and Mitigation Strategies
1.  **Risk**: Ambiguity in conflict identification algorithms (FR-GSM-19). **Mitigation**: Implement a simple rule-based initial version and refine based on user feedback.
2.  **Risk**: Complexity of integrating with external tools (Ponder, Alloy). **Mitigation**: Define clear interface specifications early; aim for "partial support" initially.
3.  **Risk**: Performance degradation with large policy repositories. **Mitigation**: Implement database indexing and optimize queries for common searches.
4.  **Risk**: Bias in multi-user analysis if classifications are not blinded. **Mitigation**: Enforce system constraint to withhold other analysts' results until an analyst completes their work.
5.  **Risk**: Evolving legal and policy standards. **Mitigation**: Design classification taxonomies to be extensible by Project Managers.
6.  **Risk**: Secure handling of sensitive policy data. **Mitigation**: Implement role-based access control, secure authentication, and audit logs as high-priority requirements.
7.  **Risk**: Usability challenges for non-technical analysts. **Mitigation**: Provide templates and intuitive wizards for goal/scenario entry.
8.  **Risk**: Scope creep due to many low-priority "desirable" features. **Mitigation**: Strictly adhere to defined priority levels for the initial release.

## Undecided Issues and Responsible Parties
1.  Specific statistical analysis methods for multi-user comparison results (FR-ADM-7). **Responsible**: Dr. Annie I. Antón / Development Team.
2.  Detailed specification and implementation approach for the P3P module requirements. **Responsible**: Bharathy / Development Team.
3.  Final design and workflow for the EPAL dedicated section. **Responsible**: Dr. Annie I. Antón / Development Team.
4.  Granular access control details for displaying goal occurrence information (Note in FR-GSM-11). **Responsible**: Qingfeng He / Development Team.
5.  Scope and implementation details for the "demo version" of the tool (FR-LC-1). **Responsible**: William Stufflebeam / Development Team.