# Software Requirements Specification (SRS)
## eProcurement Interoperability Specification for UK Public Sector

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional requirements for an eProcurement interoperability framework across the United Kingdom public sector. Its primary purpose is to specify the precise information content of electronic documents exchanged between public sector buyers and external sellers. The specification aims to establish a common, modular "language" for the entire procurement cycle to enable seamless, accurate, and efficient data exchange without manual re-keying.

#### 1.2 Document Conventions
- Requirements are categorized as **Functional (FR)** and **Non-Functional (NFR)**.
- Key terms are defined in Section 3.
- All electronic documents are specified as XML structures, compliant with the e-Government Interoperability Framework (e-GIF).

#### 1.3 Intended Audience and Reading Suggestions
This document is intended for:
- **Office of Government Commerce (OGC) Staff:** To develop, maintain, and govern the specification.
- **Software/Service Providers:** To design and implement compliant systems for buyers and sellers.
- **System Analysts & Implementers:** To understand the data requirements for integration projects.
- **Public Sector Buyers & External Suppliers (SMEs):** To understand the standard for electronic trading.

#### 1.4 Project Scope

##### 1.4.1 In Scope
- The information content and logical structure of business messages exchanged between public sector buyers and external sellers.
- The procurement cycle phases: **Sourcing, Ordering, Fulfilment, and Accounting**.
- Specification of electronic documents (e.g., Catalogue, Request for Quotation, Purchase Order, Receipt Advice, Invoice, Remittance Advice) marked up in XML.
- Definition of common, reusable data elements and structures (e.g., Party, Address, Item, Price) across all documents.
- Support for incremental adoption, allowing organizations to implement key documents (e.g., Purchase Order and Invoice) first.

##### 1.4.2 Out of Scope
- Processes for seller discovery, e-auctions, e-tendering, and negotiation of trade terms.
- Direct communication protocols or message transport mechanisms (e.g., AS1, AS2, PEPPOL).
- Security, data protection, and data retention policies and implementations.
- The application of internal public sector purchasing policies (e.g., approval workflows, spending limits).
- The definition of the final XML Schema Definitions (XSDs). This document specifies *what* data is required, not the final *syntax*.
- Integration with third-party systems such as carriers, banks, or fiscal authorities.

#### 1.5 References
- e-Government Interoperability Framework (e-GIF)
- ISO Standard Codes (e.g., ISO 3166 for countries, ISO 4217 for currencies)
- UNSPSC (United Nations Standard Products and Services Code)
- Relevant UK Government Digital Service standards

### 2. Overall Description

#### 2.1 Product Perspective
This specification acts as an **interoperability layer** between independent buyer and seller systems, which are treated as "black boxes." It defines the common interface (the electronic documents) to ensure that procurement data can be exchanged accurately and understood unambiguously by all parties, regardless of their internal system architecture.

#### 2.2 Product Functions (Summary)
The framework will enable the electronic exchange of the following core procurement documents:
1.  **Catalogue:** For suppliers to provide product/service information and pricing.
2.  **Request for Quotation (RFQ):** For buyers to solicit pricing and terms.
3.  **Quotation:** For sellers to respond to an RFQ.
4.  **Purchase Order (PO):** For buyers to formally commit to a purchase.
5.  **Order Response:** For sellers to acknowledge or confirm a PO.
6.  **Despatch Advice:** For sellers to notify of shipment.
7.  **Receipt Advice:** For buyers to confirm receipt of goods/services.
8.  **Invoice:** For sellers to request payment.
9.  **Remittance Advice:** For buyers to confirm payment.

#### 2.3 User Classes and Characteristics
| User Class | Role | Characteristics & Needs |
| :--- | :--- | :--- |
| **Purchasing Manager (Buyer)** | Maintains supplier catalogues, oversees procurement. | Needs accurate, up-to-date product and price data. |
| **Originator (Buyer)** | Identifies requirement, initiates sourcing. | Needs to solicit formal quotes from suppliers. |
| **Order Point (Buyer)** | Creates and issues purchase orders. | Needs to create legally binding, clear purchase commitments. |
| **Delivery Point (Buyer)** | Receives goods/services. | Needs to confirm receipt and report discrepancies. |
| **Accounts Payable (Buyer)** | Processes invoices for payment. | Needs accurate invoice data to match against PO and receipt. |
| **Sales Point (Seller)** | Manages customer quotes and orders. | Needs to provide quotes and acknowledge orders electronically. |
| **Despatch Point (Seller)** | Manages fulfilment and shipping. | Needs to advise buyers of shipments. |
| **Accounts Receivable (Seller)** | Manages invoicing and collections. | Needs to submit correct, timely invoices that reference the PO. |

#### 2.4 Operating Environment
- **Logical Environment:** Any system capable of generating, transmitting, receiving, and processing XML documents as per this specification.
- **Technical Constraint:** All documents must be structured in XML and align with e-GIF principles.

#### 2.5 Design and Implementation Constraints
1.  **FR-CON-001:** The specification MUST comply with the UK e-Government Interoperability Framework (e-GIF).
2.  **FR-CON-002:** All specified documents MUST be expressible in XML.
3.  **FR-CON-003:** The design MUST NOT assume any specific internal architecture for buyer or seller systems.
4.  **FR-CON-004:** The framework MUST support incremental implementation (e.g., an organization can start by implementing only PO and Invoice exchange).
5.  **FR-CON-005:** The specification MUST utilise existing international and national coding schemes (e.g., ISO country codes, UNSPSC) for key data elements.
6.  **FR-CON-006:** Every document instance MUST include a mandatory status attribute indicating if it is an `Original`, `Copy`, `Revision`, or `Cancellation`.

#### 2.6 Assumptions and Dependencies
- It is assumed that trading partners have agreed to exchange documents electronically.
- Successful implementation depends on software providers building compliant solutions.
- The utility of the specification depends on widespread adoption across the UK public sector and its suppliers.

### 3. System Features and Requirements

#### 3.1 Common Data Components
These reusable structures form the building blocks for all procurement documents.

**3.1.1 Party Information (FR-COM-001)**
*Description:* A structure to unambiguously identify and locate a party (Buyer, Seller, Ship-To, Bill-To).
*Requirements:*
- Must include a unique party identifier (e.g., DUNS number, Company Registration Number).
- Must include a party name.
- Must include a postal address structure (see FR-COM-002).
- May include contact information (e.g., email, phone) for specific roles (e.g., accounts contact).

**3.1.2 Address (FR-COM-002)**
*Description:* A standard structure for representing postal addresses.
*Requirements:*
- Must support structured address lines.
- Must include a town/city name.
- Must include a postal code.
- Must include a country code using ISO 3166-1 alpha-2.

**3.1.3 Item Identification (FR-COM-003)**
*Description:* A structure to identify a product or service.
*Requirements:*
- Must include at least one identifier from a standard scheme (e.g., Supplier's Part ID, UNSPSC, EAN).
- Must include a description.
- May include the buyer's internal item identifier for cross-referencing.

**3.1.4 Price and Amount (FR-COM-004)**
*Description:* A structure to represent monetary values.
*Requirements:*
- Must include the monetary amount.
- Must specify the currency using ISO 4217.
- Must be capable of representing unit price, line extension amounts, and document totals.
- Must support VAT/GST breakdown (rate, taxable amount, tax amount).

#### 3.2 Core Document Specifications

**3.2.1 Purchase Order (FR-DOC-001)**
*Description:* A document issued by the buyer to the seller to formally request the supply of goods or services under specified terms.
*User Story:* "As an Order Point, I want to send a Purchase Order so that I can formally commit to purchasing items."
*Key Data Requirements:*
- Unique PO identifier and issue date.
- Buyer and Seller party information.
- Ship-To and Bill-To addresses.
- List of ordered items (using FR-COM-003), each with quantity, unit price (FR-COM-004), and line total.
- PO total amount (FR-COM-004).
- Delivery instructions and requested delivery date.
- Payment terms.
- **Status:** Must be marked as `Original`.

**3.2.2 Invoice (FR-DOC-002)**
*Description:* A document issued by the seller to the buyer requesting payment for goods supplied or services rendered.
*User Story:* "As Accounts Payable, I want to receive an Invoice so that I can process payment for delivered goods/services."
*Key Data Requirements:*
- Unique Invoice identifier and issue date.
- Buyer and Seller party information (Bill-To, Ship-To if different).
- Reference to the corresponding Purchase Order number(s).
- List of invoiced items, matching or aggregating PO lines, with quantities, prices, and line totals.
- Invoice total, with clear subtotals, tax breakdown, and grand total (FR-COM-004).
- Payment details (bank account, due date).
- **Status:** Must be marked as `Original`.

**3.2.3 Receipt Advice (FR-DOC-003)**
*Description:* A document issued by the buyer to the seller to confirm receipt of goods/services and report any discrepancies.
*User Story:* "As a Delivery Point, I want to send a Receipt Advice so that I can confirm receipt and report any delivery variances."
*Key Data Requirements:*
- Reference to the corresponding Purchase Order and Despatch Advice (if used).
- List of received items, with received quantities and condition.
- Identification of any shortages, overages, or damaged goods.
- Date of receipt.
- **Status:** Can be `Original` or `Revision` (e.g., to correct a receipt entry).

**3.2.4 Request for Quotation / Quotation (FR-DOC-004)**
*Description:* RFQ is issued by the buyer to solicit pricing. The Quotation is the seller's response.
*User Stories:*
- "As an Originator, I want to send a Request for Quotation (RFQ) so that I can obtain terms and pricing for specific goods/services."
- "As a Sales Point, I want to send a Quotation so that I can propose terms and pricing to a potential buyer."
*Key Data Requirements (Quotation):*
- Reference to the RFQ identifier.
- Proposed items, prices (FR-COM-004), and validity period.
- Proposed delivery and payment terms.
- **Status:** Must be marked as `Original`.

#### 3.3 Non-Functional Requirements

**3.3.1 Interoperability (NFR-INT-001)**
- The data specification MUST be unambiguous to allow independent implementation by different software vendors, resulting in syntactically and semantically interoperable systems.

**3.3.2 Extensibility (NFR-EXT-001)**
- The document structures MUST allow for the inclusion of organization-specific or industry-specific data elements in a standardised "Extension" area without breaking core interoperability.

### 4. External Interface Requirements

#### 4.1 User Interfaces
Not applicable. This specification defines data interfaces, not human-user interfaces.

#### 4.2 Hardware Interfaces
Not applicable. Hardware is dependent on the implementing systems.

#### 4.3 Software Interfaces
This is the core of the specification. The interface is defined by the XML-based document structures described in Section 3.

#### 4.4 Communications Interfaces
Out of scope. The specification defines the *payload* of messages, not the transport protocol (e.g., HTTP/S, FTP, web service).

### 5. Other Non-Functional Requirements

#### 5.1 Performance Requirements
Not directly specified. Performance is a function of the implementing systems and transport mechanisms.

#### 5.2 Security Requirements
Out of scope for this data content specification. Security (confidentiality, integrity, non-repudiation) must be addressed at the transport and application layers by implementers.

#### 5.3 Business Rules
- **Three-Way Match:** The data within the Invoice, corresponding Purchase Order, and Receipt Advice must be sufficiently detailed and structured to support automated or semi-automated matching in Accounts Payable systems.
- **Document Lifecycle:** The `status` attribute (`Original`, `Copy`, `Revision`, `Cancellation`) must be used correctly to manage document versions. *(Specific automated handling rules are an undecided issue).*

### 6. Success Metrics
The success of this specification will be measured by:
1.  A measurable reduction in manual data entry and associated processing errors within the procurement cycles of adopting organizations.
2.  Year-on-year increase in the volume of electronic documents (POs, Invoices) exchanged between UK public sector bodies and their suppliers using this standard.
3.  An increase in the percentage of invoices processed by public sector bodies using an automated "three-way match" without manual intervention.

### Appendix A: Glossary
- **e-GIF:** e-Government Interoperability Framework. The UK government's policy and standards for achieving interoperability.
- **Interoperability:** The ability of disparate systems to exchange data with unambiguous, shared meaning.
- **Three-Way Match:** An accounts payable process of matching an Invoice to its corresponding Purchase Order and Goods Receipt Note before payment.
- **UNSPSC:** United Nations Standard Products and Services Code. A global taxonomy for classifying goods and services.

### Appendix B: Undecided Issues / Open Questions
1.  The specific business rules governing the automated system handling of document `Revisions` and `Cancellations`.
2.  The final, normative XML Schema Definitions (XSDs) are not part of this SRS and must be developed separately.
3.  Policies for handling application-specific identifiers that are not globally unique.
4.  Clarification on which optional data elements are essential for supporting specific, common business processes (e.g., partial deliveries, consignment stock).
5.  Detailed requirements for integration points with third-party logistics or financial systems, though these are currently out of scope.

---
*This document provides a functional specification for data interchange. Implementation requires the subsequent development of technical schemas and integration guides.*