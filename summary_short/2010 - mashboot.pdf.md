# Short Summary

**Background and objectives**  
Mashbot is a web service for managing a company’s presence on social networks. It aims to unify interfaces of multiple social networks and enable scheduled marketing campaigns.

**In scope**  
- Schedule content for concurrent publishing across services  
- View historical campaign metrics  
- Create and manage user accounts with roles  
- Associate Mashbot accounts with external service accounts  
- Provide dashboard, content creation, scheduling, and explore views  

**Out of scope**  
- Customer service functionality  
- Management of traditional campaigns (direct mail, trade shows)  
- Audio and video content types (Priority 3)  
- User-created campaign classes  
- Bulk user account actions by admins  

**Roles and core use cases**  
- As a Contributor, I want to create and edit content so that I can prepare campaign materials.  
- As an Approver, I want to approve contributor actions so that content meets quality standards.  
- As a Publisher, I want to schedule approved content so that it is published at the right time.  

**Success metrics**  
- Clickthrough rate  
- Page views  
- Number of comments  

**Major constraints**  
- Server memory usage ≤ 1 GB RAM  
- Web client compatible with HTTP 1.1 and HTML 4.0  
- Data encryption using TLS  
- Backup process must not cause outages >10 minutes  
- Supports only text and image content initially  

**Undecided issues**  
- Audio and video content support (Priority 3)  
- User account deactivation and undeletion process  
- Warning emails for failed login attempts  
- Hierarchical permissions for members  
- Workflow approval process for campaigns