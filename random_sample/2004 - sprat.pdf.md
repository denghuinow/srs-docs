# Detailed Summary

## Background and Scope
SPRAT is a security and privacy requirements analysis tool designed to help analysts systematically extract, manage, and reconcile goals and scenarios from policy documents. It addresses the common problem where privacy/security policies are developed as afterthoughts, leading to misalignment with system requirements. The tool maintains a repository of traceable goals and scenarios while supporting multi-user analysis comparison. Non-goals include full implementation of all low-priority features in the initial version and providing complete automated conflict resolution.

## Role Matrix and Use Cases
**Roles:**
- Administrator: Manages user groups and access permissions
- Project Manager: Oversees projects, assigns analysts, manages policy domains
- Analyst: Performs core analysis activities (goal/scenario extraction, classification)
- Guest: Views restricted repository content

**Key Scenarios:**
- Project manager creates new policy domain and assigns analysts
- Analyst extracts and classifies goals from assigned privacy policy
- System automatically compares multi-user classification results
- Guest views policy content with project manager restrictions

## Business Process
**Main Process: Policy Analysis (8 steps)**
1. Project manager imports policy document
2. Project manager assigns analysts to policy
3. Analyst extracts goals from policy text
4. Analyst classifies goals using taxonomy templates
5. System tracks goal occurrences and context
6. Multiple analysts complete independent classifications
7. System compares classification results upon request
8. Project manager exports analysis results

**Key Branch: Conflict Resolution (4 steps)**
- Trigger: System detects classification discrepancies
- Analyst reviews conflicting classifications
- Project manager mediates resolution
- System updates reconciled classifications

## Domain Model
**Key Entities:**
- User (ID, role, password*required*)
- Policy Document (ID, domain, content*required*)
- Goal (ID, description*required*, taxonomy, subject, actor)
- Scenario (ID, name*required*, actors, events, goals)
- Classification Result (ID, analyst*reference*, goal*reference*)
- Access Control Policy (ID, subject, object, action*required*)
- Project (ID, manager*reference*, domain*required*)
- Domain (ID, name*unique*, description)

## Interfaces and Integrations
- **Ponder Policy Editor**: Outbound → Policy specification → Policy rules input → Formal policy output → Manual translation required
- **Alloy Tool**: Outbound → Formal verification → Partial automated translation → Verification results → Limited automation support
- **XML Export**: Outbound → Data interchange → Project data → Structured XML file → On-demand generation

## Acceptance Criteria
**Policy Management:**
- Given a project manager with valid credentials, when they create a new policy domain, then the system should allow assignment of existing documents to this domain

**Goal Classification:**
- Given an analyst assigned to a policy, when they complete goal classification, then the system should withhold results until all analysts finish to prevent bias

## Non-functional Metrics
- **Performance**: Support concurrent multi-user analysis sessions; Generate comparison results within 30 seconds
- **Security**: Secure password storage using encryption; Access logs for all CRUD operations
- **Reliability**: Preserve data when users are disabled; Maintain traceability links during updates

## Milestones and Release Strategy
1. Database schema implementation
2. High-priority requirements implementation
3. RACAF module core functionality
4. User access control system
5. Basic goal/scenario management
6. Multi-user comparison feature

## Risk List and Mitigation Strategies
- **Classification bias**: Blind analysis until all users complete work
- **Data integrity during updates**: Automatic propagation of changes to linked policies
- **Complex taxonomy management**: Allow dynamic classification type addition
- **Integration with external tools**: Provide partial translation support for Ponder/Alloy

## Undecided Issues and Responsible Parties
- Complete statistical analysis methodology for comparison (Not mentioned)
- Full conflict identification automation approach (Not mentioned)
- EPAL implementation timeline (Not mentioned)
- Trial version object limit finalization (William Stufflebeam)
- P3P/EPAL integration details (Dr. Annie I. Antón)
- Formal verification completeness criteria (Qingfeng He)
- Keyword definition locking mechanism (Dr. Annie I. Antón)
- Guest access restriction granularity (Project Manager)