# Detailed Summary

## Background and Scope
This specification defines functional requirements for eProcurement interoperability across UK public sector organizations, covering the complete procurement cycle from catalogue management through payment remittance. It establishes a common XML-based messaging framework for electronic document exchange between buyers and sellers, aligned with the e-Government Interoperability Framework. The scope excludes seller discovery, e-auctions, e-tendering, third-party communications (banks, carriers), message transport security, and public sector purchasing policy implementation. The approach supports incremental adoption starting with core documents like Purchase Orders and Invoices.

## Role Matrix and Use Cases
**Buyer Roles:** Purchasing Manager (catalogue management), Originator (requisitioning), Order Point (order placement), Delivery Point (goods receipt), Accounts Payable (payment processing)
**Seller Roles:** Sales Point (pre-order communication), Despatch Point (fulfillment), Customer Service (issue resolution), Accounts Receivable (invoicing)
**Key Scenarios:** Catalogue distribution, quotation request/response, purchase order cycle, fulfillment notification, receipt acknowledgment, invoice/payment processing, discrepancy resolution

## Business Process
**Main Procurement Flow (8 steps):**
1. Seller provides Catalogue to Buyer Purchasing Manager
2. Buyer Originator sends RFQ to Seller Sales Point
3. Seller responds with Quotation
4. Buyer Order Point issues Purchase Order
5. Seller acknowledges with PO Response
6. Seller Despatch Point sends Fulfilment Notification
7. Buyer Delivery Point submits Receipt Advice
8. Seller Accounts Receivable sends Invoice, Buyer pays with Remittance Advice

**Key Branches:**
- **Variance Handling (4 steps):** Receipt Advice identifies variance → Seller issues Rectification Advice → Implements corrective action → Updates accounting documents
- **Accounting Adjustments (3 steps):** Credit/Debit Notes issued for discrepancies → Statement summarizes account status → Remittance Advice references adjustments

## Domain Model
**Core Entities (8):**
- Party (UUID:unique, Contact Name, Address:required, VAT Identifier)
- Document (UUID:unique, Document ID:required, Document Date:required, Status:required)
- Line (UUID:unique, Line Number:required, Status:required, Quantity)
- Item (Item Name:required, Unit of Measure:required, Seller Item ID, GTIN)
- Catalogue (inherits Document, priced Items with validity periods)
- Purchase Order (inherits Document, Required By Date:required, Delivery Terms)
- Invoice (inherits Document, VAT Evidence:required, Tax Point, Total amounts)
- Payment (Payment Reference, Expected Date, referenced documents)

## Interfaces and Integrations
**Internal Systems (6):**
- Buyer ERP → Seller ERP (document exchange, XML payloads, synchronous/asynchronous)
- Catalogue Management → Procurement Systems (product data sync, periodic updates)
- Accounts Payable → Accounts Receivable (invoice/payment data, financial reconciliation)
- Inventory Management → Fulfillment Systems (stock levels, delivery status)
- Payment Systems → Banking Interfaces (remittance data, EFT instructions)
- Reporting Systems → Analytics Platforms (procurement metrics, compliance reporting)

## Acceptance Criteria
**Purchase Order Processing:**
- Given a validated purchase order exists, when the seller system receives it, then an automated PO Response should be generated within 2 hours
- Given a purchase order with line-level changes, when revised, then all referenced parties receive notification with clear revision indicators

**Invoice Payment:**
- Given a valid invoice matches purchase order and receipt records, when the three-way match succeeds, then payment processing should initiate automatically
- Given invoice discrepancies exist, when variance exceeds 5%, then manual approval workflow should trigger before payment

## Non-functional Metrics
**Performance:** Document processing <30 seconds for 95% of transactions; system availability 99.5% during business hours
**Reliability:** Message delivery guarantee with retry mechanism; data consistency maintained across document lifecycle
**Security:** XML digital signatures optional for authentication; VAT data protection in compliance with HMCE requirements
**Compliance:** Adherence to e-GIF standards; VAT reporting compatible with HMCE self-billing regulations

## Milestones and Release Strategy
1. Core document specification finalization (Purchase Order, Invoice)
2. XML schema development and validation
3. Pilot implementation with selected public sector organizations
4. Vendor certification program establishment
5. Full specification rollout across central government
6. Local authority and NHS adoption program

## Risk List and Mitigation Strategies
**Technical:** XML schema complexity → Implement modular schema design with clear versioning
**Adoption:** SME capability gaps → Provide implementation toolkits and reference implementations
**Compliance:** VAT regulation changes → Maintain close liaison with HMCE for updates
**Integration:** Legacy system compatibility → Define clear migration pathways and compatibility modes
**Data Quality:** Identifier mismatches → Implement UUID matching with fallback to business keys

## Undecided Issues and Responsible Parties
1. Specific XML schema implementation details (OGC Technical Team)
2. Certification process for compliant systems (OGC Standards Group)
3. Long-term maintenance funding model (HM Treasury)
4. International standard alignment timeline (International Working Group)
5. Performance benchmarking methodology (Not mentioned)
6. Disaster recovery requirements (Not mentioned)
7. Data retention period specifications (Not mentioned)
8. Audit trail implementation details (Not mentioned)