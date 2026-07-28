**Short Summary**

**Background and objectives**  
The project aims to rewrite the core Laboratory Information System (LIS) to improve performance, ensure system integrity, and comply with HIPAA and FDA standards. The goal is to create a stable, automated, and maintainable system that supports business growth.

**In scope**  
- Re-writing core LIS functionalities with enhanced performance and reliability.  
- Implementing critical defect fixes and architectural enhancements.  
- Developing an Admin module for user management (e.g., create/add users).  
- Providing online help documentation using RoboHelp version 8.  
- Ensuring HIPAA compliance in all new and existing functionalities.

**Out of scope**  
- Functionalities not documented in this FRS.  
- Non-critical enhancements or defects.  
- Changes to existing core functionalities beyond specified enhancements.  
- Development outside the defined module-by-module approach.  
- Proprietary custom components where open-source frameworks are appropriate.

**Stakeholders and core use cases**  
*Stakeholders:*  
- CIO: Business/Technical owner and final approver.  
- IT Manager: Oversees QA/QC and implementation.  
- Programmer Analyst/Project Manager: Manages development and serves as SME.  
- Technical Writer: Creates user documentation and help systems.  
- QA Analyst: Conducts testing and quality assurance.  
- Sr. Business Systems Analyst: Leads requirements analysis and validation.

*User stories:*  
1. As an Admin, I want to create/add new users and assign roles so that system access is properly managed.  
2. As a user, I want to access context-sensitive help on each screen so that I can quickly resolve issues.  
3. As a QA Analyst, I want to perform regression testing on scheduled builds so that system stability is maintained.  
4. As a Technical Lead, I want to review code before commit so that coding standards are followed.  
5. As the CIO, I want to approve production deployments so that business risks are minimized.  
6. As a developer, I want to use open-source frameworks where appropriate so that maintainability is improved.

**Success metrics**  
- System downtime limited to scheduled maintenance windows (e.g., Tuesdays 7pm–7am).  
- Successful completion of User Acceptance Testing (UAT) before production deployment.  
- Adherence to HIPAA compliance in all new functionalities.

**Major constraints**  
- Development must use .NET 3.5 platform and a single SQL Server 2008 database.  
- Production releases require signoff from the Technical Owner/Lead.  
- UI changes must be demonstrated to stakeholders early and adjusted only if schedule permits.  
- Coding and maintainability standards must be followed, with logging to external files.  
- Weekly integrations and labeled builds in source control are mandatory.

**Undecided issues**  
- Specific details of all functional issues and requirements from gathering sessions.  
- Exact schedule for UI adjustments based on stakeholder feedback.  
- Full list of open-source frameworks to be utilized.  
- Complete error handling and notification mechanisms beyond specified logging.  
- Final content and structure of the online help glossary.