# Short Summary: Enterprise E-mail Functional Requirements Specification

## Background and Objectives
The Agency for Enterprise Information Technology (AEIT) is developing a proposed plan for a statewide e-mail system as mandated by Florida Statute 282.34, aiming to reduce operational costs and meet the needs of all executive branch agencies. The primary objective is to submit a comprehensive plan by December 31, 2009, which includes sourcing options, cost-benefit analysis, and a migration schedule.

## In Scope
*   Core e-mail, calendar, and contact functionalities for end-users.
*   Archiving, retention, and e-discovery capabilities to meet legal and regulatory requirements.
*   Security features including anti-virus, content filtering, and encryption.
*   Remote access and mobile messaging support for various devices.
*   Basic administrative functions for agency and data center administrators.

## Out of Scope
*   Collaboration services such as shared documents, workflows, and instant messaging.
*   Detailed agency inventory and financial data (collected separately).
*   Specific technical implementation or data structure details.
*   Final vendor selection or contract negotiation processes.
*   Agency-specific application dependencies not integrated with core e-mail.

## Stakeholders and Core Use Cases
*   **End-User:** An employee of an executive branch agency who uses e-mail for daily communication and scheduling.
*   **Agency Administrator:** An IT staff member within an agency responsible for managing user accounts, distribution lists, and agency-specific e-mail functions.
*   **Data Center Administrator (SSRC Admin):** A technical administrator responsible for system-wide management, security, backup, and infrastructure.
*   **AEIT Project Team:** The central team leading the requirements gathering, planning, and oversight for the enterprise e-mail system.
*   **Legal/Compliance Personnel (e.g., OIG):** Agency staff who require the ability to review, redact, and hold e-mails for legal discovery and compliance.

**Core User Stories:**
1.  As an **End-User**, I want to send, receive, and organize e-mails with attachments so that I can communicate effectively.
2.  As an **End-User**, I want to access my e-mail and calendar securely from a web browser or mobile device so that I can work remotely.
3.  As an **Agency Administrator**, I want to provision user accounts and create distribution lists integrated with our directory service so that I can manage my agency's users efficiently.
4.  As an **Agency Administrator**, I want to archive e-mails and perform searches for discovery so that the agency can comply with public records and legal requests.
5.  As a **Data Center Administrator**, I want to implement pre-emptive virus scanning and content filtering so that I can protect the system and its users from threats.
6.  As a **Legal/Compliance Personnel**, I want to search archives, place results on legal hold, and review/redact them so that I can fulfill litigation and investigation requirements.

## Success Metrics
*   Submission of a complete proposed plan to state leadership by the December 31, 2009 deadline.
*   Development of a plan that demonstrates cost savings compared to existing agency e-mail services.
*   Creation of a feasible migration schedule to decommission agency systems and transition to the new system between July 2010 and June 2013.

## Major Constraints
*   The project must comply with Florida Statutes 282.34 and 282.0041, defining the service's scope and establishment.
*   The functional requirements specification must be completed within a 6-week (30 business day) timeframe.
*   The solution must meet federal and state requirements for confidentiality, privacy, and security.
*   The plan must identify and consider existing e-mail infrastructure for potential reuse.
*   All functional requirements are subject to technical and financial feasibility analysis.

## Undecided Issues
*   The final sourcing model (in-house, externally sourced, or a hybrid option).
*   The specific technical and financial feasibility of each listed functional requirement.
*   The standardization format for state e-mail addresses.
*   The detailed cost estimates and savings for each sourcing option.
*   The exact technical approach for integrating with existing agency applications and directories.