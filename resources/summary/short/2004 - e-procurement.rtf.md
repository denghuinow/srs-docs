**Short Summary**

**Background and objectives**  
This document defines functional requirements for eProcurement interoperability across the UK public sector, specifying the information content of electronic documents exchanged between buyers and sellers. The goal is to establish a common, modular “language” for the procurement cycle—from catalogue to remittance—to enable seamless data exchange without re-keying, supporting government efficiency and e-business initiatives.

**In scope**  
- Information content of messages exchanged between public sector buyers and external sellers.  
- The procurement cycle covering sourcing, ordering, fulfilment, and accounting.  
- Electronic documents (e.g., Purchase Order, Invoice) marked up in XML, compliant with the e-GIF.  
- Common data elements and structures reusable across all documents.  
- Support for incremental adoption, starting with key documents like Purchase Order and Invoice.

**Out of scope**  
- Seller discovery, e-auctions, e-tendering, and negotiation of trade terms.  
- Communication with third parties (e.g., carriers, banks, fiscal authorities).  
- Message transport, security, data protection, and retention rules.  
- Application of public sector purchasing policy.  
- XML schema definition (specification of message content only).

**Stakeholders and core use cases**  
*Stakeholders:*  
- **Buyer (Public Sector Organisation):** Purchases goods/services; roles include Purchasing Manager, Originator, Order Point, Delivery Point, Accounts Payable.  
- **Seller (External Supplier):** Supplies goods/services; roles include Sales Point, Despatch Point, Customer Service, Accounts Receivable.  
- **Office of Government Commerce (OGC):** Develops and maintains the specification to ensure cross-government interoperability.  
- **Software/Service Providers:** Implement systems based on the specification for buyers and sellers.  
- **Small to Medium-sized Enterprises (SMEs):** Benefit from a clear standard for trading with government.  
- **Analysts/Implementers:** Use the specification to design and build eProcurement solutions.

*User stories:*  
1. As a Purchasing Manager, I want to receive catalogues from sellers so that I can maintain accurate pricing and product information.  
2. As an Originator, I want to send a Request for Quotation (RFQ) so that I can obtain terms and pricing for specific goods/services.  
3. As an Order Point, I want to send a Purchase Order so that I can formally commit to purchasing items.  
4. As a Delivery Point, I want to send a Receipt Advice so that I can confirm receipt and report any delivery variances.  
5. As Accounts Payable, I want to receive an Invoice so that I can process payment for delivered goods/services.  
6. As a Sales Point, I want to send a Quotation so that I can propose terms and pricing to a potential buyer.

**Success metrics**  
- Reduction in manual data re-entry and processing errors across the procurement cycle.  
- Increased adoption of electronic document exchange among public sector buyers and sellers.  
- Achievement of automated “three-way match” (Purchase Order, receipt, Invoice) in accounts payable.

**Major constraints**  
- Must comply with the e-Government Interoperability Framework (e-GIF) and use XML.  
- No assumptions about internal buyer/seller systems; treated as “black boxes.”  
- Must support incremental implementation, allowing adoption of documents over time.  
- Relies on existing international and national coding schemes (e.g., ISO standards, UNSPSC).  
- Documents must include mandatory status attributes (original, copy, revision, cancellation).

**Undecided issues**  
- Specific business rules for automated handling of document copies, revisions, and cancellations.  
- Final XML schema definitions are not provided in this specification.  
- Handling of application-specific identifiers that may not be universally unique.  
- Optional elements required to support certain business processes may need further clarification.  
- Integration details with third-party systems (e.g., carriers, banks) are not addressed.