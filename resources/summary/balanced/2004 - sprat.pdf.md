# Balanced Summary: Security and Privacy Requirements Analysis Tool (SPRAT)

## Goals and Scope
SPRAT is a tool designed to assist analysts in mining, reconciling, and managing goals and scenarios derived from privacy and security policies for web-based systems. It aims to maintain a repository of goals and scenarios to support ongoing analysis of policies and other documents, ensuring traceability between goals and their source policies. The tool provides strong management features, including flexible user-defined search conditions and support for automatic multi-user analysis comparison.

## Stakeholders and User Stories
*   **Administrator**: A super user responsible for managing user groups and overall system access.
*   **Project Manager**: A user who manages projects, assigns analysts, and controls access to documents and information within the system.
*   **Analyst**: A member of the project team who analyzes assigned policies to extract and manage goals, scenarios, and requirements.
*   **Guest**: A user with restricted, view-only access to certain information in the repository as permitted by the Project Manager.
*   **Customer/Sponsor (Dr. Annie I. Antón)**: The originator of requirements and the project sponsor.
*   **Developer (Qingfeng He, William Stufflebeam)**: Responsible for implementing the system, particularly the RACAF module.

**User Stories:**
1.  As an **Administrator**, I want to create user groups and manage user accounts so that I can control system access.
2.  As a **Project Manager**, I want to assign analysts to projects and set access restrictions so that I can manage project workflows and data security.
3.  As an **Analyst**, I want to add, classify, and search for goals from a privacy policy so that I can build a traceable repository for analysis.
4.  As an **Analyst**, I want to specify scenarios and associate them with goals so that I can model desired system behavior.
5.  As a **Guest**, I want to view permitted policy information so that I can review analysis results without making changes.
6.  As a **Developer**, I want to implement the RACAF module for access control analysis so that the tool supports formal policy specification and verification.

## Key Processes
1.  **User Authentication & Authorization (Trigger: User login)**: The system authenticates users and enforces role-based permissions (Administrator, Project Manager, Analyst, Guest).
2.  **Project & Document Setup (Trigger: Project Manager action)**: A Project Manager adds policy documents to the repository, assigns them to domains, and allocates analysts.
3.  **Goal Mining & Management (Trigger: Analyst selects a policy)**: An analyst extracts goals from a policy, classifies them (e.g., policy/scenario, protection/vulnerability), and enters them into the repository with full traceability.
4.  **Scenario Specification (Trigger: Analyst action)**: An analyst creates, edits, or reuses scenarios, linking them to relevant goals and requirements.
5.  **Analysis & Comparison (Trigger: Project Manager or Analyst request)**: The system supports queries, displays goal/scenario details, and can compare classification results from multiple analysts.
6.  **Access Control Analysis (RACAF) (Trigger: Analyst initiates RACAF workflow)**: An analyst defines data objects, organizational structures, and roles to specify and verify access control policies.
7.  **System Auditing (Trigger: Any add, edit, or delete action)**: The system logs all user actions for security and tracking purposes.

## Domain Data Elements
*   **User**: (PK: UserID) Role, Password, ContactInfo, AssignedGroups.
*   **Policy Document**: (PK: DocID) Name, Domain, Text, FleschReadabilityScore.
*   **Goal**: (PK: GoalID) Description, Taxonomy, SubjectClassification, Actor, SourcePolicyID.
*   **Scenario**: (PK: ScenarioID) Name, Actors, Events, Actions, Pre/Post-Conditions.
*   **Requirement**: (PK: ReqID) Description, LinkedGoals, Constraints.
*   **Access Control Policy (RACAF)**: (PK: PolicyID) Subject, Object, Action, RuleSpecification.

## Non-Functional Requirements
1.  **Security**: The system must provide secure password storage and user authentication.
2.  **Access Control**: Different user roles must have distinct access levels and privileges within projects.
3.  **Data Integrity**: The system must maintain traceability links between goals and their source policies.
4.  **Auditability**: The system must generate an access log for all add, edit, and delete actions.
5.  **Usability**: The system shall provide templates for entering goals, scenarios, and requirements.
6.  **Interoperability**: The RACAF module shall provide interface support to interact with external policy editors (e.g., Ponder).

## Milestones and External Dependencies
1.  Implementation of core database structure and high/medium priority requirements.
2.  Development and integration of the Requirements-level Access Control Analysis Framework (RACAF) module.
3.  Successful parsing and integration of P3P policy documents according to the P3P standard.
4.  Provision of a demo/trial version of the tool for evaluation.
5.  Dependency on external tools/languages for advanced features (e.g., Ponder for policy specification, Alloy for formal verification in RACAF).

## Risks and Mitigation Strategies
1.  **Risk**: Misalignment or conflicts between system requirements and privacy policies.
    *   **Mitigation**: Use goal and scenario mining to provide rationale and detect conflicts early in the requirements process.
2.  **Risk**: Bias in multi-user analysis due to analysts viewing each other's classifications prematurely.
    *   **Mitigation**: Implement a constraint where an analyst's classifications are withheld from others until their own analysis is complete.
3.  **Risk**: Complexity in translating access control policies for formal verification.
    *   **Mitigation**: Provide partial, automated translation support to minimize manual specification effort.
4.  **Risk**: Inconsistent classification of goals and scenarios by different analysts.
    *   **Mitigation**: Implement templates and standardized classification taxonomies, and support comparison tools for reconciliation.
5.  **Risk**: Security breaches due to improper access control or insecure data handling.
    *   **Mitigation**: Enforce strict role-based permissions, secure authentication, and comprehensive action logging.

## Undecided Issues
1.  The specific statistical analysis required behind the scenes for multi-user analysis comparison.
2.  Detailed mechanisms for automated conflict identification and resolution between requirements and policies.
3.  The exact implementation approach for dynamically adding new goal classification types.
4.  Final determination of which users (e.g., guests) should see specific analytical information like goal occurrence counts.
5.  The full scope and definition of "partial support" for translating Ponder policies into Alloy specifications.
6.  The complete set of elements and workflow for the EPAL-dedicated section in the tool.