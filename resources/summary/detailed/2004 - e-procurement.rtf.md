# Detailed Summary: eProcurement Functional Requirements Specification

## Background and Scope
This document specifies the functional requirements for eProcurement interoperability within the UK public sector. It defines the information content of electronic messages exchanged between public sector Buyers and external Sellers, covering the full procurement cycle from catalogue management through to payment remittance. The requirements are designed to be sector-agnostic, providing a common, extensible data model for eProcurement documents to be implemented as XML in compliance with the e-Government Interoperability Framework (e-GIF). Key non-goals include Seller discovery, e-auctions, e-tendering, negotiation of trade terms, direct communication with third parties (carriers, banks, fiscal authorities), message transport/security specifics, data protection rules, and the application of public sector purchasing policy.

## Stakeholders Matrix and Use Cases
*   **Buyer (Public Sector Organisation):** The purchasing entity that initiates procurement processes and receives goods/services.
*   **Seller (Supplier):** The external entity that provides goods/services and responds to procurement actions.
*   **Purchasing Manager (Buyer Role):** Responsible for establishing and maintaining trading agreements and supplier catalogues.
*   **Originator/Requisitioner (Buyer Role):** Has the initial demand for goods/services and may raise Requests for Quotation.
*   **Order Point (Buyer Role):** Raises formal Purchase Orders, potentially using purchase card details.
*   **Delivery Point/Goods Inwards (Buyer Role):** Receives goods/services and identifies any variances from the order.
*   **Accounts Payable (Buyer Role):** Processes invoices, makes payments, and may issue Self Billed Invoices.
*   **Sales Point (Seller Role):** Manages all pre-order communication with the Buyer, including quotations and order responses.
*   **Despatch Point (Seller Role):** Responsible for shipping goods, performing services, and notifying the Buyer.
*   **Customer Service (Seller Role):** Resolves issues arising from order fulfilment variances.
*   **Accounts Receivable (Seller Role):** Manages invoicing, credit control, and provides bank details for payment.

**Main Scenarios:** 1) Seller sends a Catalogue to the Buyer's Purchasing Manager. 2) Buyer's Originator sends an RFQ to the Seller's Sales Point. 3) Seller's Sales Point sends a Quotation to the Buyer. 4) Buyer's Order Point sends a Purchase Order to the Seller. 5) Seller's Sales Point sends a PO Response acknowledging the order. 6) Seller's Despatch Point sends a Fulfilment Notification upon shipment/service completion. 7) Buyer's Delivery Point sends a Receipt Advice, noting any variances. 8) Seller's Customer Service sends a Rectification Advice in response to variances.
**Exception Scenarios:** 1) Buyer's Accounts Payable issues a Self Billed Invoice under a self-billing arrangement. 2) Seller's Accounts Receivable issues a Credit Note to rectify invoicing errors. 3) Buyer's Accounts Payable issues a Debit Note to claim money from the Seller. 4) Buyer sends a Remittance Advice to notify payment. 5) Seller sends a Statement summarizing the account status.

## Business Process
**Main Process (Procurement Cycle):**
1.  **Sourcing (Trigger:** Need identification): Exchange of Catalogue, RFQ, and Quotation documents.
2.  **Ordering (Trigger:** Approved requisition): Exchange of Purchase Order and PO Response.
3.  **Fulfilment (Trigger:** Order acceptance): Exchange of Fulfilment Notification, Receipt Advice, and Rectification Advice.
4.  **Accounting (Trigger:** Delivery/service completion): Exchange of Invoice/Self Billed Invoice, Credit/Debit Notes, Remittance Advice, and Statement.

**Key Branch A - Variance Handling (Trigger:** Variance in Receipt Advice):
1.  Buyer's Delivery Point identifies and reports a variance (e.g., damage, short delivery) in the Receipt Advice.
2.  Seller's Customer Service reviews the variance and determines a rectification action.
3.  Seller's Customer Service sends a Rectification Advice to the Buyer.
4.  The agreed action (e.g., return, replace, destroy goods) is executed.

**Key Branch B - Self-Billing (Trigger:** Existence of a self-billing arrangement):
1.  Upon delivery/service completion, the Buyer's Accounts Payable generates a Self Billed Invoice.
2.  The Self Billed Invoice is sent to the Seller's Accounts Receivable, replacing the need for a Seller-generated Invoice.
3.  Payment proceeds based on the Self Billed Invoice.

## Domain Model
Core entities define the structure of all procurement documents:
*   **Party (Required:** UUID): Represents any organisation, person, or system. Specialisations: Buyer, Seller, and specific roles (e.g., Order Point, Accounts Receivable). Key fields: Contact Name, Address, VAT Identifier, Registration Number.
*   **Document (Required:** UUID, ID, Date, Status): The main container for a business message. Specialisations: Catalogue, RFQ, Quotation, Purchase Order, Invoice, etc. Key fields: Sender/Receiver (Party references), Test Status, Schema Version, Total amounts.
*   **Line (Required:** UUID, Number, Status): A component of a Document relating to a single Item type. Specialisations: Quantified Line, Priced Line. Key fields: Line Note, Quantity, Amounts.
*   **Item (Required:** Name, Unit of Measure): Describes a product or service. Specialisations: Priced Item. Key fields: Description, Seller Item ID, GTIN, Commodity Class (UNSPSC), Unit Price.
*   **Priced Item Validity:** Defines price applicability based on quantity ranges and date ranges.
*   **Item Instance:** Describes a specific physical instance of an Item (e.g., Serial Number, Batch Number).
*   **Extended Item ID (Required:** ID, Source): An alternative part number for an Item (e.g., OEM reference).
*   **Aspect (Required:** Name, Value): Captures domain-specific Item attributes (e.g., colour, dimensions).

## Interfaces and Integrations
*   **Buyer's Internal ERP/Procurement System (Outbound):** Generates and sends Buyer-originated documents (RFQ, PO, Receipt Advice, etc.). Input: Internal requisition/payment data. Output: Structured XML documents per specification. SLA: Must generate valid XML compliant with the defined schema version.
*   **Seller's Internal ERP/Order Management System (Outbound):** Generates and sends Seller-originated documents (Catalogue, Quotation, Invoice, etc.). Input: Internal order/sales data. Output: Structured XML documents per specification. SLA: Must generate valid XML compliant with the defined schema version.
*   **Buyer's Internal ERP/Procurement System (Inbound):** Receives and processes Seller-originated documents. Input: XML documents from Sellers. Output: Data ingested into internal systems for order tracking, goods receipt, and invoice processing. SLA: Must be able to parse and validate incoming XML; handle document statuses (original, revision).
*   **Seller's Internal ERP/Order Management System (Inbound):** Receives and processes Buyer-originated documents. Input: XML documents from Buyers. Output: Data ingested into internal systems for order fulfilment and accounts receivable. SLA: Must be able to parse and validate incoming XML; acknowledge receipt (e.g., via PO Response).
*   **(Conceptual) e-GIF Compliance Layer:** All document exchanges must adhere to the UK e-Government Interoperability Framework, mandating the use of XML and specific data standards.

## Acceptance Criteria
**For Ordering Capability:**
*   Given a validated Purchase Order from a Buyer, When the Seller's system receives it, Then it must generate a PO Response with a status acknowledging receipt and intent to fulfil.
*   Given a Purchase Order marked with status 'revision', When the Seller's system processes it, Then it must correctly identify and update the referenced original order.

**For Accounting Capability:**
*   Given a valid Invoice from a Seller referencing a Purchase Order, When the Buyer's system performs a three-way match against the PO and Receipt Advice, Then it should flag the Invoice for payment if all details align.
*   Given a self-billing arrangement is in place, When goods are received, Then the Buyer's system must generate a Self Billed Invoice containing the mandatory VAT statement and both parties' VAT IDs.

## Non-functional Metrics
*   **Performance:** Systems must generate and process XML documents within acceptable business timeframes (e.g., sub-minute for PO processing). Support for batch processing of documents (e.g., Catalogue updates).
*   **Reliability:** Document exchange mechanisms must ensure reliable delivery; senders should be able to re-send documents with 'copy' status if needed. Systems must handle document revisions and cancellations without data corruption.
*   **Security:** While transport security is out of scope, the payload supports a W3C Digital Signature for document authentication (optional for receivers). VAT-relevant documents must ensure integrity of fiscal data.
*   **Compliance:** Must comply with the UK e-GIF. Must support required identifiers (e.g., VAT numbers, UNSPSC codes) for public sector reporting.
*   **Observability:** Documents contain mandatory metadata: Sender Software Manufacturer/Product/Version and Schema Version for traceability and version management.

## Milestones and Release Strategy
1.  Finalize and publish the functional requirements specification (this document).
2.  Develop and publish the corresponding XML schemas for each document type.
3.  Pilot implementation with a limited set of core documents (e.g., Purchase Order and Invoice).
4.  Gather feedback from pilot implementations and refine schemas if necessary.
5.  Gradual rollout, encouraging adoption of additional document types (e.g., Catalogue, Fulfilment Notification).
6.  Achieve broad interoperability across UK public sector procurement.

## Risk List and Mitigation Strategies
1.  **Risk:** Complexity of full implementation may deter SMEs. **Mitigation:** Promote incremental adoption, starting with basic PO/Invoice exchange.
2.  **Risk:** Proliferation of incompatible extensions or interpretations of the specification. **Mitigation:** Provide clear schemas, conformance testing, and a governance body for the standard.
3.  **Risk:** Inability of legacy systems to generate or consume the required XML. **Mitigation:** Encourage middleware solutions and phased migration plans.
4.  **Risk:** Misalignment with international (e.g., UN/CEFACT) or European standards. **Mitigation:** Ensure the specification is mapped to and can be aligned with broader standards where possible.
5.  **Risk:** Security of financial data (e.g., purchase card details) within documents. **Mitigation:** Rely on secure transport protocols (out of scope here) and keep sensitive data fields optional.
6.  **Risk:** Poor performance when handling large catalogues or documents with many lines. **Mitigation:** Specification should allow for efficient XML structures; implementation guidance on handling large files.
7.  **Risk:** Lack of unique identifiers causing matching errors between documents. **Mitigation:** Mandate use of UUIDs for Documents and Lines to ensure reliable referencing.
8.  **Risk:** VAT compliance issues, especially with Self Billed Invoices. **Mitigation:** Include mandatory fields and verbiage as required by HMCE, and provide clear guidance.

## Undecided Issues and Responsible Parties
1.  **Issue:** Final definition and governance of the XML schemas. **Responsible:** OGC/OeE Joint Interoperability Working Group with technical contributors.
2.  **Issue:** Certification process for software claiming compliance with the specification. **Responsible:** OGC in consultation with software supplier associations (e.g., BASDA).
3.  **Issue:** Handling of industry-specific or commodity-specific data extensions beyond the core Aspect model. **Responsible:** Domain experts and the Working Group for establishing extension guidelines.
4.  **Issue:** Detailed business rules for automated handling of document revisions, copies, and cancellations. **Responsible:** Implementers and the Working Group for providing best practice guidance.
5.  **Issue:** Long-term maintenance and versioning strategy for the specification and schemas. **Responsible:** OGC as the publishing authority.