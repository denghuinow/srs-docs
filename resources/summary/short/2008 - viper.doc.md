**Short Summary**

**Background and objectives**  
This SRS defines a web-based Supply Chain Management (SCM) system for Ejada company to manage customer requests, supplier interactions, and internal resources. The system aims to streamline product delivery and coordination among customers, suppliers, and coordinators.

**In scope**  
- Customer, supplier, and coordinator management (add, view, edit, delete).  
- Request lifecycle management (creation, tracking, feedback).  
- Item and resource-location management.  
- Web-based interface with role-based access (coordinator, customer, supplier).  
- Integration with Ejada’s .NET framework and MS SQL database.

**Out of scope**  
- Hardware interfaces.  
- Direct integration with external systems (e.g., CRM, HR) beyond future customization.  
- Non-web-based access methods.  
- Advanced analytics or reporting beyond basic performance metrics.  
- Mobile or offline functionality.

**Stakeholders and core use cases**  
- **Coordinator**: Manages customers, suppliers, requests, items, and resource locations.  
- **Customer**: Submits and manages requests, edits own profile.  
- **Supplier**: Views supply requests, provides feedback, edits own profile.  

*User stories*:  
1. As a coordinator, I want to add a new customer so that I can manage their requests.  
2. As a coordinator, I want to send a request to a supplier so that I can fulfill customer needs.  
3. As a customer, I want to submit a request so that I can receive products or services.  
4. As a customer, I want to view my pending requests so that I can track their status.  
5. As a supplier, I want to view pending requests so that I can respond with feedback.  
6. As a supplier, I want to send feedback on a request so that the coordinator knows my availability.

**Success metrics**  
- Support at least 100 concurrent users.  
- 90% of transactions completed in under 1 second.  
- System availability of 100% with understandable error feedback.

**Major constraints**  
- Must be web-based using ASP.NET, C#, and MS SQL.  
- Must comply with Ejada’s .NET framework and integrate with two existing modules.  
- Must follow Waterfall process model and object-oriented design.  
- Supported browsers: Internet Explorer (v6-7) and Mozilla Firefox (v2-3).  
- Server requires Microsoft OS with IIS and .NET Framework 3.5.

**Undecided issues**  
- Specific communication channels for notifications (e.g., email, SMS).  
- Whether to disable request editing after coordinator acknowledgment.  
- Refinement criteria for filtered views (e.g., customer/supplier lists).  
- Handling of request deletions when suppliers are unavailable.  
- Exact backup procedures and disaster recovery details.