# Balanced Summary: eProcurement Functional Requirements Specification

## Goals and Scope
This document specifies the functional requirements for eProcurement interoperability in the UK public sector, covering the information content of messages exchanged between public sector Buyers and external Sellers throughout the procurement cycle from catalogue to remittance. The requirements aim to provide a common, modular 'language' for describing eProcurement documents, supporting electronic data interchange using XML in compliance with the e-Government Interoperability Framework (e-GIF). Out of scope are aspects such as seller discovery, e-auctions, e-tendering, negotiation of trade terms, and communication with third parties like carriers or banks.

## Stakeholders and User Stories
*   **Buyer (Public Sector Organisation):** The purchasing entity that sends requests, orders, and payments, and receives goods, services, and invoices.
*   **Seller (Supplier):** The external entity that provides goods or services, sends catalogues, quotations, and invoices, and receives orders and payments.
*   **Purchasing Manager (Buyer Role):** Responsible for arranging and maintaining trading agreements and managing catalogue data.
*   **Originator/Order Point (Buyer Role):** Initiates demand and raises purchase orders.
*   **Sales Point (Seller Role):** Manages communication with the buyer up to and including order acceptance.
*   **Accounts Payable/Receivable (Buyer/Seller Roles):** Handle invoice processing, payment, and credit control.

**User Stories:**
1.  As a **Purchasing Manager**, I want to **receive electronic catalogues from sellers** so that **I can maintain accurate, up-to-date product and pricing information locally**.
2.  As an **Originator**, I want to **send a Request for Quotation (RFQ)** so that **I can obtain terms and pricing for specific goods or services before ordering**.
3.  As a **Sales Point**, I want to **send a Quotation in response to an RFQ** so that **I can formally propose supply terms and enable the buyer to place an order**.
4.  As an **Order Point**, I want to **send a Purchase Order** so that **I can formally commit to buying specified goods or services from the seller**.
5.  As an **Accounts Receivable clerk**, I want to **send an Invoice** so that **I can request payment for delivered goods or performed services**.
6.  As an **Accounts Payable clerk**, I want to **send a Remittance Advice** so that **I can notify the seller of payment and specify which invoices are being settled**.

## Key Processes
1.  **Sourcing (Trigger: Need for goods/services identified):** The buyer may request a quotation (RFQ), and the seller may provide catalogue information or a formal quotation.
2.  **Ordering (Trigger: Decision to purchase):** The buyer issues a Purchase Order to the seller.
3.  **Order Acknowledgment (Trigger: Receipt of Purchase Order):** The seller sends a Purchase Order Response to confirm receipt and intent to fulfill.
4.  **Fulfillment (Trigger: Goods are despatched or services performed):** The seller sends a Fulfillment Notification; upon receipt, the buyer may send a Receipt Advice, potentially followed by a seller's Rectification Advice for any variances.
5.  **Invoicing (Trigger: Delivery or service completion):** The seller sends an Invoice, or under a self-billing arrangement, the buyer issues a Self Billed Invoice.
6.  **Payment & Settlement (Trigger: Invoice is due for payment):** The buyer sends a Remittance Advice to notify payment, and the seller may send periodic Statements.
7.  **Dispute Resolution (Trigger: Billing or delivery variance):** Corrections are handled via Credit Notes (from seller) or Debit Notes (from buyer).

## Domain Data Elements
*   **Document (Primary Key: Document UUID):** Document ID, Document Date, Document Status, Sender, Receiver, Total Amount.
*   **Party (Primary Key: Party UUID):** Contact Name, Address, Organisation Registered Name, VAT Identifier, Role (e.g., Buyer, Seller).
*   **Line (Primary Key: Line UUID):** Line Number, Line Status, Quantity, Amount, Linked Item.
*   **Item (Primary Key: Seller Item ID / GTIN):** Item Name, Description, Unit of Measure, Commodity Class, Unit Price.
*   **Purchase Order (Specialization of Document):** Required By Date, Delivery Terms, Customer Reference Identifier (CRI).
*   **Invoice (Specialization of Document):** Tax Point, VAT Evidence, Paid In Full status, Cost Centre Ref.

## Non-Functional Requirements
1.  **Interoperability:** Must comply with the UK e-Government Interoperability Framework (e-GIF) and use XML for data exchange.
2.  **Extensibility:** The common data model must be modular and extensible to accommodate specialized business contexts.
3.  **Incremental Adoption:** The specification must support phased implementation, starting with core documents like Purchase Order and Invoice.
4.  **Semantic Precision:** Requires unambiguous interpretation of all data elements by both sender and receiver systems.
5.  **Uniqueness & Referencing:** Supports the use of Universally Unique Identifiers (UUIDs) for exact machine matching of document and line instances.
6.  **Auditability:** Documents must be uniquely identifiable for audit purposes, supporting statuses like original, copy, revision, and cancellation.

## Milestones and External Dependencies
1.  Development and ratification of the XML schema based on this functional specification.
2.  Adoption and implementation by public sector bodies and their software providers.
3.  Reliance on international and national coding standards (e.g., ISO country/currency codes, UNSPSC, UK postcodes, VAT numbers).
4.  Alignment with HM Customs & Excise (HMCE) rules for self-billed invoices and VAT documentation.
5.  Support from software and service providers to build compliant systems, reducing the need for multiple specifications.

## Risks and Mitigation Strategies
1.  **Risk:** Complexity hindering adoption, especially by SMEs.
    *   **Mitigation:** Promote incremental implementation and provide clear implementation guidance.
2.  **Risk:** Proliferation of incompatible document variants or interpretations.
    *   **Mitigation:** Define a strict, common core data model and mandate the use of standardized XML schemas.
3.  **Risk:** Inability to ensure unique identifiers across all systems.
    *   **Mitigation:** Recommend the use of UUIDs for instance matching while supporting existing application-specific IDs.
4.  **Risk:** Changes in external standards (e.g., tax regulations, coding schemes).
    *   **Mitigation:** Design a versioned schema and establish a maintenance process for the specification.
5.  **Risk:** Security of data in transit and at rest is out of scope.
    *   **Mitigation:** Explicitly state that transport and security must be addressed by implementing systems and protocols.

## Undecided Issues
1.  The specific business rules for automated handling of document copies, revisions, and cancellations.
2.  The detailed XML schema to be used for implementation.
3.  How to fully integrate with third-party systems (carriers, banks) which are currently out of scope.
4.  The application of specific public sector purchasing policies within the electronic documents.
5.  Data protection and retention rules for the exchanged documents.
6.  The mandatory enforcement of structured vs. unstructured addresses for all parties.