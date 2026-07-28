# Short Summary: Security and Privacy Requirements Analysis Tool (SPRAT)

## Background and Objectives
SPRAT is a tool designed to assist analysts in mining, reconciling, and managing goals and scenarios derived from privacy and security policies for web-based systems. Its primary objective is to align system requirements with policies, prevent conflicts, and maintain a traceable repository to support ongoing analysis and foster stakeholder trust.

## In Scope
- Implementation of user access control with four distinct privilege levels (Administrator, Project Manager, Analyst, Guest).
- Development of core modules for goal, scenario, and policy specification, management, and traceability.
- Integration of the Requirements-level Access Control Analysis Framework (RACAF) for data, task, and organizational analysis.
- Provision of templates for goals, scenarios, P3P statements, EPAL rules, and access control policies.
- Support for automatic multi-user analysis results comparison and conflict identification.

## Out of Scope
- Full implementation of all low-priority functional requirements (e.g., dynamic goal classification, advanced conflict resolution).
- Complete automation of formal verification processes (e.g., full translation of Ponder policies to Alloy).
- Expansion of the tool to support non-web-based systems or unrelated document types.
- Development of a comprehensive, production-ready demo version beyond a basic trial.
- Detailed statistical analysis for multi-user comparison without further stakeholder consultation.

## Stakeholders and Core Use Cases
*   **Administrator**: Manages user groups and system-wide access, including creating accounts and resetting passwords.
*   **Project Manager**: Oversees projects, assigns analysts, manages policy documents, and controls guest access permissions.
*   **Analyst**: Performs core analysis by extracting, classifying, and managing goals, scenarios, and requirements from assigned policies.
*   **Guest**: Views repository information with restrictions set by the Project Manager.
*   **Project Sponsor (Dr. Annie I. Antón)**: Provides strategic direction, funding, and final approval for project requirements.

**User Stories:**
1.  As a **Project Manager**, I want to assign analysts to specific projects and policy documents so that work is distributed efficiently.
2.  As an **Analyst**, I want to add and classify a new goal with multiple subject tags so that I can accurately capture its context from a policy.
3.  As an **Administrator**, I want to disable a user's access while preserving their historical data so that system security is maintained without data loss.
4.  As an **Analyst**, I want to view all scenarios associated with a specific goal so that I can understand its operational context.
5.  As a **Guest**, I want to view policy documents and their associated goals within my granted access so that I can review analysis work.
6.  As an **Analyst**, I want to specify access control rules while viewing related scenario elements side-by-side so that I can ensure policy alignment.

## Success Metrics
- Successful implementation and integration of all high-priority requirements, particularly for user access and the RACAF module.
- Ability to maintain full traceability links between goals, scenarios, and their source policy documents.
- Generation of a secure access log for all critical add, edit, and delete actions within the system.

## Major Constraints
- The system must enforce secure password storage and login procedures.
- Multi-user analysis comparisons must withhold other analysts' classifications until a user completes their own to prevent bias.
- The summer development focus is on implementing the database and high/medium priority requirements, including RACAF.
- The tool must support integration with external tools like the Ponder policy editor and Alloy for verification.
- Access levels and permissions must be strictly enforced according to defined user roles.

## Undecided Issues
- The specific statistical analysis methods required behind the scenes for multi-user comparison.
- The exact implementation details for the automated conflict identification and resolution mechanism.
- The final scope and feature set for the demo/trial version of the tool.
- The complete list of elements and interface design for the P3P and EPAL dedicated sections.
- Handling of all edge cases in the P3P policy evaluation against user preferences.