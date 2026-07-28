# Software Requirements Specification (SRS)
## eProcurement Interoperability for UK Public Sector

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review  
**Authors:** [Expert SRS Author]  
**Governance Body:** OGC/OeE Joint Interoperability Working Group

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for an eProcurement interoperability standard within the UK public sector. Its primary purpose is to serve as the authoritative source for the information content and structure of electronic business documents exchanged between public sector Buyers and external Sellers, ensuring consistent implementation across disparate systems.

#### 1.2 Scope
This specification covers the full procurement-to-payment cycle, including:
*   The definition of standardised electronic document types (e.g., Catalogue, Purchase Order, Invoice).
*   A common, extensible data model for all document types.
*   The business processes and document flows between Buyer and Seller roles.
*   Requirements for system interfaces to generate, send, receive, and process these documents.

**Out of Scope:**
*   Seller discovery, e-auctions, and e-tendering processes.
*   Negotiation of commercial trade terms.
*   Direct system-to-system communication with third parties (carriers, banks, fiscal authorities).
*   Specification of message transport protocols, security layers, or network infrastructure.
*   Data protection legislation application rules.
*   Definition or enforcement of public sector purchasing policy.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **Buyer:** A UK public sector organisation initiating a procurement.
*   **Seller:** An external supplier providing goods or services.
*   **e-GIF:** UK e-Government Interoperability Framework.
*   **ERP:** Enterprise Resource Planning system.
*   **UUID:** Universally Unique Identifier.
*   **RFQ:** Request for Quotation.
*   **PO:** Purchase Order.
*   **UNSPSC:** United Nations Standard Products and Services Code.
*   **GTIN:** Global Trade Item Number.
*   **OGC:** Office of Government Commerce.
*   **OeE:** Office of the e-Envoy.
*   **VAT:** Value Added Tax.
*   **HMCE:** Her Majesty's Customs and Excise (now part of HMRC).

#### 1.4 References
*   UK e-Government Interoperability Framework (e-GIF) policies and technical standards.
*   Relevant HMCE regulations on VAT invoicing and self-billing.

#### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2** describes the overall system perspective and product functions.
*   **Section 3** details specific requirements for external interfaces, functions, and data.
*   **Appendices** provide supporting information, including use case elaborations and a data dictionary.

### 2. Overall Description

#### 2.1 Product Perspective
This specification defines a **data interchange standard**, not a specific software product. It sits as a conceptual layer between the internal systems of Buyers and Sellers (e.g., ERP, procurement, order management systems). Compliance requires these internal systems to implement interfaces capable of producing and consuming XML documents that conform to the schemas derived from this SRS.

```
[Buyer's Internal System] <--> [XML Document per SRS] <--> [Seller's Internal System]
        (e.g., ERP)          (Over e-GIF compliant transport)     (e.g., Order Management)
```

#### 2.2 Product Functions
The core product functions are the generation, exchange, and processing of standardised business documents. The main document types and their high-level functions are:

| Document Type | Originator | Primary Function |
| :--- | :--- | :--- |
| Catalogue | Seller | Provide product/service descriptions, prices, and terms. |
| Request for Quotation (RFQ) | Buyer | Solicit pricing for specified items. |
| Quotation | Seller | Respond to RFQ with offered prices and terms. |
| Purchase Order (PO) | Buyer | Formally request supply of goods/services. |
| PO Response | Seller | Acknowledge and confirm acceptance/rejection of a PO. |
| Fulfilment Notification | Seller | Advise of shipment or service completion. |
| Receipt Advice | Buyer | Confirm receipt of goods/services and note variances. |
| Rectification Advice | Seller | Propose resolution for variances identified in Receipt Advice. |
| Invoice | Seller | Request payment for supplied goods/services. |
| Self Billed Invoice | Buyer | Issue invoice on behalf of Seller under self-billing agreement. |
| Credit Note | Seller | Adjust an Invoice downwards (e.g., for errors, returns). |
| Debit Note | Buyer | Adjust an Invoice upwards (e.g., for undercharging). |
| Remittance Advice | Buyer | Notify Seller of payment made. |
| Statement | Seller | Provide summary of account status. |

#### 2.3 User Characteristics
**Actors and Roles:**

| Actor | Role | System Interaction |
| :--- | :--- | :--- |
| **Buyer Organisation** | Purchasing Manager | Initiates/maintains catalogues & trading agreements. |
| | Originator/Requisitioner | Creates and sends RFQs. |
| | Order Point | Creates and sends Purchase Orders. |
| | Delivery Point/Goods Inwards | Creates and sends Receipt Advices. |
| | Accounts Payable | Processes incoming invoices, generates Self Billed Invoices, Debit Notes, and Remittance Advices. |
| **Seller Organisation** | Sales Point | Manages quotations, order responses, and customer communication. |
| | Despatch Point | Generates Fulfilment Notifications. |
| | Customer Service | Generates Rectification Advices. |
| | Accounts Receivable | Generates Invoices, Credit Notes, and Statements. |

*   **Assumptions:** Users operate through enterprise software (ERP, procurement systems) which will implement the interfaces defined herein. They are not expected to interact directly with the XML.

#### 2.4 Constraints
1.  **Regulatory:** Must comply with the UK e-GIF mandate for XML-based data exchange.
2.  **Technical:** All document instances must be well-formed and valid XML according to the published schemas.
3.  **Business:** Must support UK VAT regulations, including specific requirements for Self Billed Invoices.
4.  **Implementation:** The standard must be implementable by both large-scale ERP systems and SME-level business software.

#### 2.5 Assumptions and Dependencies
*   A secure and reliable transport mechanism for XML documents exists (though its specification is out of scope).
*   Trading partners will exchange necessary party identifiers (e.g., VAT numbers, organisational IDs) out-of-band to populate documents.
*   The OGC/OeE Working Group will publish and maintain the definitive XML schemas.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 System Interfaces (Logical)
*   **SI-1: Buyer Outbound Interface**
    *   **Description:** Interface from the Buyer's internal system to generate outbound documents.
    *   **Inputs:** Internal data (requisition, goods receipt, payment data).
    *   **Outputs:** Valid XML documents for: RFQ, Purchase Order, Receipt Advice, Self Billed Invoice, Debit Note, Remittance Advice.
    *   **SLA:** Must generate XML that validates against the official schema for the document type and version.

*   **SI-2: Seller Outbound Interface**
    *   **Description:** Interface from the Seller's internal system to generate outbound documents.
    *   **Inputs:** Internal data (product, sales order, shipment, invoice data).
    *   **Outputs:** Valid XML documents for: Catalogue, Quotation, PO Response, Fulfilment Notification, Rectification Advice, Invoice, Credit Note, Statement.
    *   **SLA:** Must generate XML that validates against the official schema for the document type and version.

*   **SI-3: Buyer Inbound Interface**
    *   **Description:** Interface to the Buyer's internal system to process inbound documents.
    *   **Inputs:** XML documents from Sellers.
    *   **Outputs:** Data ingested into internal modules (order tracking, goods receipt, invoice processing).
    *   **SLA:** Must be able to parse, validate, and process incoming XML. Must correctly handle document `Status` (e.g., `original`, `revision`, `copy`).

*   **SI-4: Seller Inbound Interface**
    *   **Description:** Interface to the Seller's internal system to process inbound documents.
    *   **Inputs:** XML documents from Buyers.
    *   **Outputs:** Data ingested into internal modules (sales order processing, accounts receivable).
    *   **SLA:** Must be able to parse, validate, and process incoming XML. Must generate a PO Response upon receipt of a Purchase Order.

##### 3.1.2 Compliance Interface
*   **CI-1: e-GIF Compliance**
    *   **Description:** All XML documents must adhere to e-GIF standards.
    *   **Requirement:** Document payloads shall be encoded in UTF-8 XML, following the schema definitions published by the governing body.

#### 3.2 Functional Requirements

##### 3.2.1 Document Processing Requirements
*   **FUN-DOC-001: Document Referencing**
    *   **Description:** A document must be able to reference a prior related document.
    *   **Condition:** When an Invoice is created for a Purchase Order.
    *   **Action:** The Invoice document must contain the `UUID` of the referenced Purchase Order in a designated field.
*   **FUN-DOC-002: Document Status Handling**
    *   **Description:** Systems must correctly process documents based on their status.
    *   **Condition:** A Purchase Order with `Status="revision"` is received.
    *   **Action:** The Seller's system must identify the original PO using the referenced `UUID` and update its records accordingly, not create a new order.

##### 3.2.2 Core Procurement Process Requirements
*   **FUN-PROC-001: Order Acknowledgement**
    *   **Description:** Sellers must formally acknowledge receipt of a Purchase Order.
    *   **Condition:** Upon receiving a valid Purchase Order.
    *   **Action:** The Seller's system shall generate and transmit a PO Response document with a `Status` indicating acceptance, rejection, or pending review.
*   **FUN-PROC-002: Three-Way Match**
    *   **Description:** The Buyer's system must support invoice validation.
    *   **Condition:** Upon receipt of an Invoice from a Seller.
    *   **Action:** The Buyer's system shall be capable of automatically matching the Invoice against the corresponding Purchase Order and Receipt Advice based on referenced `UUIDs` and line details.

##### 3.2.3 Variance Handling Requirements
*   **FUN-VAR-001: Variance Reporting**
    *   **Description:** Buyers must report discrepancies upon receipt of goods/services.
    *   **Condition:** A variance (quantity, quality, damage) is identified at the Delivery Point.
    *   **Action:** The Receipt Advice document shall include details of the variance (type, quantity affected, description).
*   **FUN-VAR-002: Rectification Initiation**
    *   **Description:** Sellers must respond to reported variances.
    *   **Condition:** After reviewing a Receipt Advice containing variances.
    *   **Action:** The Seller's system shall generate and send a Rectification Advice proposing an action (replace, credit, return).

##### 3.2.4 Accounting & Payment Requirements
*   **FUN-ACC-001: Self-Billed Invoice Generation**
    *   **Description:** Buyers must generate compliant Self Billed Invoices.
    *   **Condition:** A self-billing arrangement is active, and goods/services are received.
    *   **Action:** The Buyer's system shall generate a Self Billed Invoice containing: both parties' VAT identifiers, a mandatory VAT statement text as per HMCE, and all other mandatory invoice data fields.
*   **FUN-ACC-002: Payment Notification**
    *   **Description:** Buyers should notify Sellers of payments made.
    *   **Condition:** A payment is issued by the Buyer's Accounts Payable.
    *   **Action:** The Buyer's system should generate a Remittance Advice referencing the paid Invoice(s) and optional payment method details.

#### 3.3 Domain Data Model Requirements
The following core entities shall be supported in the data model:

*   **Entity: Party**
    *   **Requirement:** Must be identifiable by a `UUID`.
    *   **Attributes (Key):** `ContactName`, `Address` (structured), `VATIdentifier`, `RegistrationNumber`.
    *   **Specialisations:** `Buyer`, `Seller`, `OrderPoint`, `AccountsReceivable`, etc.

*   **Entity: Document**
    *   **Requirement:** Must contain a `UUID`, a human-readable `ID`, `IssueDate`, and `Status`.
    *   **Attributes (Key):** `SenderPartyReference`, `ReceiverPartyReference`, `TestFlag`, `SchemaVersion`, `TotalAmount`.
    *   **Specialisations:** `Catalogue`, `PurchaseOrder`, `Invoice`, etc.

*   **Entity: Line**
    *   **Requirement:** Must contain a `UUID`, `LineNumber`, and `Status`.
    *   **Attributes (Key):** `Note`, `Quantity`, `UnitPrice`, `LineTotalAmount`.
    *   **Specialisations:** `QuantifiedLine`, `PricedLine`.

*   **Entity: Item**
    *   **Requirement:** Must have a `Name` and `UnitOfMeasure`.
    *   **Attributes (Key):** `Description`, `SellerItemID`, `GTIN`, `CommodityCode` (UNSPSC), `UnitPrice`.
    *   **Specialisations:** `PricedItem`.

*   **Entity: Aspect**
    *   **Requirement:** Used to extend Item descriptions with domain-specific attributes.
    *   **Attributes:** `Name`, `Value`, `UnitOfMeasure` (optional).

#### 3.4 Non-Functional Requirements

| Category | Requirement ID | Description | Metric / Standard |
| :--- | :--- | :--- | :--- |
| **Performance** | NFR-PER-001 | Document generation time. | System shall generate standard Purchase Order XML (<100 lines) within 30 seconds of user submission. |
| | NFR-PER-002 | Document processing time. | System shall parse, validate, and initiate processing of an incoming Invoice within 60 seconds of receipt. |
| | NFR-PER-003 | Batch processing. | System shall support processing of Catalogue files containing up to 10,000 items. |
| **Reliability** | NFR-REL-001 | Data integrity. | Systems shall handle document revisions without corrupting the master record of the original transaction. |
| | NFR-REL-002 | Duplicate handling. | If a document with `Status="copy"` is received, the system shall log it but not reprocess it as a new business event. |
| **Security** | NFR-SEC-001 | Document authentication. | The XML payload structure **shall support** the inclusion of a W3C XML Digital Signature element (ds:Signature). |
| | NFR-SEC-002 | Data integrity (Fiscal). | The system shall ensure that VAT-critical fields in invoices and self-billed invoices cannot be altered after generation without invalidating the document. |
| **Compliance** | NFR-COM-001 | Standards adherence. | All generated XML **shall validate** against the published XSD schemas for the specified `SchemaVersion`. |
| | NFR-COM-002 | Regulatory reporting. | System **must support** capture and storage of VAT Identifier (Seller & Buyer) and UNSPSC codes where applicable. |
| **Observability** | NFR-OBS-001 | Traceability. | Every document **must contain** metadata identifying the generating software: `SoftwareManufacturer`, `SoftwareProduct`, `SoftwareVersion`. |
| | NFR-OBS-002 | Version management. | Every document **must contain** the `SchemaVersion` attribute to which it conforms. |

#### 3.5 Acceptance Criteria
*   **AC-ORDER-001:** Given a valid Purchase Order XML document from a known Buyer, when it is received by the Seller's test system, then the system shall generate a PO Response XML document with `Status="accepted"` within the performance threshold (NFR-PER-002).
*   **AC-ORDER-002:** Given a Purchase Order XML with `Status="revision"` and a valid reference to a previous PO `UUID`, when processed by the Seller's system, then the system shall update the existing order record and not create a duplicate.
*   **AC-ACCT-001:** Given an Invoice XML, a corresponding Purchase Order XML, and a Receipt Advice XML (all linked by `UUIDs`), when the Buyer's system executes a three-way match, then the Invoice shall be flagged as "Approved for Payment" if quantities, prices, and items match across all three documents.
*   **AC-ACCT-002:** Given a self-billing agreement is configured and a Receipt Advice is logged, when the Buyer's system triggers the accounting process, then it shall generate a Self Billed Invoice XML containing the exact VAT statement mandated by HMCE and both party VAT IDs.

### 4. Appendices

#### Appendix A: Use Case Elaboration (Sample)
*   **Use Case:** UC-001 Process Purchase Order
*   **Primary Actor:** Seller's ERP System (via Sales Point role)
*   **Preconditions:** Seller system is operational; Trading relationship with Buyer is established.
*   **Main Success Scenario:**
    1.  System receives a valid Purchase Order XML document.
    2.  System validates XML against the published XSD schema.
    3.  System parses document, extracting header and line details.
    4.  System creates or updates an internal sales order record.
    5.  System generates a PO Response XML document with `Status="accepted"`.
    6.  System transmits the PO Response to the Buyer.
*   **Extensions:**
    *   2a. XML is invalid: System generates an error log and may send a rejection notification (out of scope).
    *   4a. Item not found: System sets PO Response `Status="rejected"` with appropriate note on the line.

#### Appendix B: Data Dictionary (Excerpt)
| Field Name | Entity | Data Type | Req'd | Description | Example |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `UUID` | Document | String (URN) | M | Universally unique identifier for the document instance. | `urn:uuid:123e4567-e89b-12d3-a456-426614174000` |
| `ID` | Document | String | M | Human-readable document number. | `PO-2023-98765` |
| `Status` | Document | Enum | M | Lifecycle status. Values: `original`, `revision`, `copy`. | `original` |
| `VATIdentifier` | Party | String | C | VAT registration number. Required for VAT-able entities. | `GB 123 4567 89` |
| `SellerItemID` | Item | String | M | Seller's unique identifier for the item. | `WIDGET-2000-BLUE` |
| `CommodityCode` | Item | String | O | UNSPSC code classifying the item. | `43211504` (Desktop computers) |

#### Appendix C: Open Issues & Governance
1.  **Issue:** Final approval and versioning of XML Schemas.
    *   **Responsible:** OGC/OeE Joint Interoperability Working Group.
2.  **Issue:** Formal certification process for compliant software.
    *   **Responsible:** OGC in consultation with BASDA.
3.  **Issue:** Guidelines for industry-specific extensions using the `Aspect` model.
    *   **Responsible:** Domain Expert Panels & Working Group.
4.  **Issue:** Detailed business rules for automated cancellation workflows.
    *   **Responsible:** Implementer Community & Working Group for best practices.
5.  **Issue:** Long-term maintenance and deprecation policy for the standard.
    *   **Responsible:** OGC as publishing authority.

---
*Document End*