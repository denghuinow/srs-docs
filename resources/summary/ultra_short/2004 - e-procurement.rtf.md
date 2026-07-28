**Purpose & Scope**
The system defines a common data standard for electronic procurement (eProcurement) messages exchanged between public sector Buyers and external Sellers. It covers the full procurement cycle from catalogue management to payment remittance. It explicitly excludes seller discovery, e-auctions, e-tendering, negotiation of terms, communication with third parties (like banks or carriers), message transport, security, and data retention rules.

**Product Background / Positioning**
This specification establishes a UK cross-government interoperability standard for eProcurement to enable electronic data interchange (EDI) between public sector buyers and all sellers. It is intended to be the common 'language' for procurement documents, supporting initiatives for government efficiency and 100% electronic interaction with business. It sits within the e-Government Interoperability Framework (e-GIF).

**Core Functional Overview**
The system must support the structured exchange of these key document types: Catalogue, Request for Quotation (RFQ) and Quotation, Purchase Order and PO Response, Fulfilment Notification and Receipt Advice (including Rectification Advice), and Invoice, Credit/Debit Note, Remittance Advice, and Statement.

**Key Users & Usage Scenarios**
Primary users are Buyer roles (Purchasing Manager, Originator, Order Point, Delivery Point, Accounts Payable) and Seller roles (Sales Point, Despatch Point, Customer Service, Accounts Receivable). A typical scenario involves an Originator (Buyer) sending an RFQ, a Sales Point (Seller) responding with a Quotation, an Order Point (Buyer) issuing a Purchase Order, and the subsequent exchange of fulfilment and accounting documents.

**Major External Interfaces**
The specification defines the structure and content of XML-based messages exchanged between Buyer and Seller systems. Interfaces to third-party systems (e.g., carrier, bank, fiscal authority systems) and the underlying message transport & security layer are out of scope.

**Key Non-functional Requirements**
The data standard must enable precise, identical interpretation of every data element by both sender and receiver systems to ensure semantic interoperability. All documents must support a mandatory status attribute (original, copy, revision, cancellation). Document and Line instances must be uniquely identifiable using Universally Unique Identifiers (UUIDs).

**Constraints, Assumptions & Dependencies**
The specification must comply with the UK e-Government Interoperability Framework (e-GIF). It relies on external international and national coding standards (e.g., ISO country/currency codes, UNSPSC, UK VAT numbers). It assumes no specific internal system design for buyers or sellers, treating them as black boxes.

**Priorities & Acceptance Approach**
The core set of documents (like Purchase Order and Invoice) are foundational, with an expectation of incremental adoption. Acceptance is based on the correct implementation of the common data model and document structures, enabling successful electronic exchange and automated processing (e.g., three-way matching) between conformant systems.