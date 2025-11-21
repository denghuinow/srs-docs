Purpose & Scope  
Standardizes electronic procurement messages across UK public sector from catalogue to remittance (e.g., Purchase Order, Invoice). Excludes seller discovery, e-auctions, negotiation, third-party communication, transport/security, and data retention. Treats internal systems as "black boxes"; requires all messages to use a common data structure for interoperability.  

Product Background / Positioning  
Enables 100% electronic government-business interactions by 2005, supporting value-for-money savings and SME adoption. Provides a unified standard to replace fragmented specifications, reducing software complexity for vendors and enabling automated three-way matching (PO, receipt, invoice) in accounts payable.  

Core Functional Overview  
- Purchase Order (Buyer to Seller) with status tracking (original/revision/cancellation)  
- Invoice (Seller to Buyer) with VAT compliance and payment references  
- Remittance Advice (Buyer to Seller) linking payments to specific invoices  
- Catalogue (Seller to Buyer) for price and item information  
- Status attribute management (original/copy/revision/cancellation) for all documents  

Key Users & Usage Scenarios  
Buyers: Purchasing Manager (catalogue), Order Point (PO), Accounts Payable (invoice processing). Sellers: Sales Point (quoting), Accounts Receivable (invoicing). Scenarios include automated PO-to-invoice matching, self-billed invoicing for SMEs, and variance handling (e.g., damaged goods via Receipt Advice/Rectification Advice).  

Major External Interfaces  
XML-based messages exchanged between Buyer and Seller systems, validated per e-Government Interoperability Framework (e-GIF). No details on transport protocols, security, or UI; interfaces defined solely by document structure.  

Key Non-functional Requirements  
- 100% electronic procurement interactions mandated by 2005  
- Document status (original/copy/revision/cancellation) mandatory for all messages  
- VAT compliance required for Invoice, Self Billed Invoice, Credit Note, Debit Note  

Constraints, Assumptions & Dependencies  
No XML schema provided; systems treated as "black boxes." Excludes e-auctions, seller discovery, and third-party communication (e.g., carriers, banks). Assumes internal systems handle business logic; interoperability limited to message content.  

Priorities & Acceptance Approach  
Highest priority: Document status handling and VAT compliance. Acceptance requires all documents to include mandatory status attributes and comply with VAT rules. Incremental adoption permitted (e.g., starting with PO/Invoice), but all adopted documents must use the common data structure.