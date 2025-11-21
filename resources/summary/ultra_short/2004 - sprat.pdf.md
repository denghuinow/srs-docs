Purpose & Scope:  
SPRAT addresses misaligned privacy/security policies in web systems by enabling goal and scenario mining, reconciliation, and management from policy documents. It maintains a traceable repository for policy goals (strategic) and scenario goals (tactical), excluding policy creation or direct policy enforcement.  

Product Background / Positioning:  
SPRAT integrates with existing privacy analysis workflows for organizations developing web systems. It serves as a standalone tool for requirements engineers, CPOs, and auditors to analyze policies against goals/scenarios, replacing ad-hoc manual processes.  

Core Functional Overview:  
- Manage goal/scenario repositories with traceability to source policies.  
- Support RACAF framework for access control analysis and policy verification.  
- Enable multi-user goal classification with automatic comparison and conflict resolution.  
- Organize policy documents by domain (e.g., healthcare, finance) with role-based access.  
- Extract and reconcile P3P privacy policy data against user preferences.  
- Track all system actions via access logs for auditability.  

Key Users & Usage Scenarios:  
- **Administrators**: Manage user groups, reset passwords, disable accounts.  
- **Project Managers**: Assign policies/domains, delegate analysts, export project data.  
- **Analysts**: Add/edit goals/scenarios, classify goals, reconcile conflicts.  
- **Guests**: View restricted policy data per project manager permissions.  

Major External Interfaces:  
- P3P standard for privacy policy data extraction.  
- Ponder language for access control policy specification.  
- Alloy tool for security verification (partial integration).  

Key Non-functional Requirements:  
- Secure password storage and user authentication (NFR-UAM 2, 3).  
- Full audit trail for all system actions (add/edit/delete) via access logs (SR 1).  
- Support for multi-user analysis with conflict resolution (FR-ADM 7).  

Constraints, Assumptions & Dependencies:  
- Requires secure database for sensitive policy data.  
- Depends on Ponder editor for access control policy specification.  
- Assumes P3P policy documents follow standard structure for parsing.  

Priorities & Acceptance Approach:  
- **Critical (Priority 1)**: RACAF analysis, goal/scenario management, access logs, secure authentication.  
- **Acceptance**: System must satisfy all Priority 1 requirements; traceability links and conflict resolution must be verifiable.