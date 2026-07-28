# Software Requirements Specification (SRS)
## UK Government eProcurement Interoperability Standard

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the Software Requirements Specification for the UK Cross-Government eProcurement Interoperability Standard. The purpose of this standard is to establish a common, structured data format for the electronic exchange of procurement messages between public sector Buyer organizations and external Seller organizations. This SRS serves as the definitive source of requirements for system implementers, solution architects, and procurement system vendors.

#### 1.2 Scope
The scope of this specification encompasses the definition of a common data model and XML schema for key procurement documents exchanged across the full procurement-to-payment (P2P) cycle.

**In-Scope Elements:**
*   Definition of XML-based message structures for core procurement documents.
*   Specification of data elements, data types, cardinality, and semantic meaning for each document.
*   Coverage of the procurement cycle from catalogue management through to payment remittance.
*   Support for electronic data interchange (EDI) between Buyer and Seller enterprise systems.

**Explicitly Out-of-Scope Elements:**
*   Seller discovery mechanisms or supplier portals.
*   e-Auctions, e-Tendering, or negotiation platforms.
*   Direct communication interfaces with third-party systems (e.g., banking networks, carrier tracking systems, fiscal authority portals).
*   Message transport protocols, security layers (encryption, digital signatures), or reliability mechanisms.
*   Data retention, archival, or data lifecycle management rules.
*   Internal business logic or processes within Buyer or Seller systems.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **Buyer** | A public sector organization procuring goods or services. |
| **Seller** | An external organization supplying goods or services to the Buyer. |
| **e-GIF** | e-Government Interoperability Framework. |
| **EDI** | Electronic Data Interchange. |
| **RFQ** | Request for Quotation. |
| **PO** | Purchase Order. |
| **UUID** | Universally Unique Identifier. |
| **UNSPSC** | United Nations Standard Products and Services Code. |
| **P2P** | Procure-to-Pay. |

#### 1.4 References
*   UK e-Government Interoperability Framework (e-GIF) Policies and Standards.
*   ISO 3166 (Country Codes), ISO 4217 (Currency Codes).
*   UNSPSC Classification System.
*   Relevant UK legislation (e.g., pertaining to VAT, invoicing).

#### 1.5 Document Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product and its context. Section 3 details the specific functional and non-functional requirements. Appendices may provide illustrative examples or reference information.

### 2. Overall Description

#### 2.1 Product Perspective
This specification is a **data interoperability standard**, not a standalone software application. It exists within the ecosystem defined by the UK e-GIF, providing a common "language" for procurement data. The standard interfaces with the internal procurement/financial systems of Buyers and Sellers, which are treated as black-box systems.

**System Context Diagram:**
```
+----------------+      XML Messages       +----------------+
|                | (Catalogue, Order,      |                |
|  Buyer System  |<----------------------->|  Seller System |
|  (Black Box)   |  Invoice, Remittance)   |  (Black Box)   |
+----------------+                         +----------------+
         |                                        |
         | (Out of Scope)              (Out of Scope)
         v                                        v
+----------------+                     +----------------+
| Internal Buyer |                     | Internal Seller|
|  Processes     |                     |  Processes     |
+----------------+                     +----------------+
```

#### 2.2 Product Functions
The core function of this standard is to enable the unambiguous exchange of the following document types:
1.  **Catalogue Management:** Seller product/service catalogue publication and update.
2.  **Pre-Order:** Request for Quotation (RFQ) and Quotation.
3.  **Ordering:** Purchase Order (PO) and PO Response (acceptance/rejection).
4.  **Fulfilment:** Fulfilment Notification, Receipt Advice, and Rectification Advice.
5.  **Financial Settlement:** Invoice, Credit Note, Debit Note, Remittance Advice, and Statement.

#### 2.3 User Characteristics
| Role | Organization | Description & Key Interactions |
| :--- | :--- | :--- |
| **Purchasing Manager / Originator** | Buyer | Initiates demand, creates and sends RFQs. |
| **Order Point** | Buyer | Creates, issues, and revises Purchase Orders. |
| **Delivery Point / Goods Receiver** | Buyer | Receives goods/services, issues Receipt and Rectification Advices. |
| **Accounts Payable** | Buyer | Processes Invoices and issues Remittance Advices. |
| **Sales Point** | Seller | Responds to RFQs with Quotations, receives and responds to POs. |
| **Despatch Point** | Seller | Issues Fulfilment Notifications upon shipment/dispatch. |
| **Accounts Receivable** | Seller | Issues Invoices, Credit/Debit Notes, and Statements. |
| **Customer Service** | Seller | Handles queries and rectifications. |

#### 2.4 Assumptions and Dependencies
*   **Assumption:** Buyer and Seller systems possess the capability to generate, transmit, receive, and parse XML documents.
*   **Assumption:** Trading partners will establish bilateral agreements for transport, security, and trading terms outside this standard.
*   **Dependency:** The standard relies on the stability and availability of external code lists (ISO codes, UNSPSC, etc.).
*   **Constraint:** The specification must be fully compliant with the overarching principles and technical standards of the UK e-GIF.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Document Exchange Requirements
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-1** | The system **shall** support the generation and consumption of XML messages conforming to the defined schema for all in-scope document types. | High |
| **FR-2** | Each document instance **shall** include a mandatory `DocumentStatus` attribute with allowed values: `Original`, `Copy`, `Revision`, `Cancellation`. | High |
| **FR-3** | Each complete document instance **shall** be uniquely identified by a `DocumentID` element containing a UUID (version 4 recommended). | High |
| **FR-4** | Each line item within any document **shall** be uniquely identified by a `LineID` element containing a UUID. | High |
| **FR-5** | A `Revision` of a document **shall** reference the `DocumentID` of the document it supersedes. | Medium |
| **FR-6** | A `Cancellation` document **shall** reference the `DocumentID` of the document it cancels. | Medium |

##### 3.1.2 Core Document Requirements
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-10** | **Purchase Order (PO):** Shall contain header data (Buyer/Seller IDs, dates, delivery address) and at least one line item detailing material/service, quantity, price, and accounting codes. | High |
| **FR-11** | **PO Response:** Shall allow the Seller to communicate acceptance, rejection, or proposed amendment of the PO, referencing the original `DocumentID`. | High |
| **FR-12** | **Invoice:** Shall contain header data, line items linked to PO `LineID`s, tax calculations, and payment terms. Must support both summary and line-level taxation. | High |
| **FR-13** | **Credit/Debit Note:** Shall be structurally identical to an Invoice but with a negative amount indicator, and must reference the `DocumentID` of the adjusted Invoice. | High |
| **FR-14** | **Remittance Advice:** Shall be issued by the Buyer to detail which Invoices are being paid, with optional partial payment and deduction information. | Medium |
| **FR-15** | **Catalogue:** Shall allow Sellers to provide structured item descriptions, prices, and classifications (e.g., UNSPSC). | Medium |
| **FR-16** | **Receipt Advice:** Shall allow the Buyer to confirm receipt of goods/services, referencing PO `LineID`s and received quantities. | Medium |
| **FR-17** | **Rectification Advice:** Shall allow the Buyer to report discrepancies (shortages, damages) against a Receipt Advice. | Low |

#### 3.2 Non-Functional Requirements

##### 3.2.1 Interoperability Requirements
| ID | Requirement |
| :--- | :--- |
| **NFR-1** | **Semantic Interoperability:** The data standard must be defined with sufficient precision to ensure an identical interpretation of every data element by any conformant sender and receiver system. |
| **NFR-2** | **Syntactic Interoperability:** All messages must be well-formed XML documents valid against the published XML Schema Definition (XSD). |

##### 3.2.2 Data Quality Requirements
| ID | Requirement |
| :--- | :--- |
| **NFR-3** | **Uniqueness:** The combination of `DocumentID` (UUID) and Sender Party Identifier must be globally unique. |
| **NFR-4** | **Traceability:** The data model must support end-to-end traceability of a procurement transaction through linked `DocumentID` and `LineID` references across documents. |

##### 3.2.3 Compliance Requirements
| ID | Requirement |
| :--- | :--- |
| **NFR-5** | The specification **shall** comply with all mandatory standards prescribed by the UK e-Government Interoperability Framework (e-GIF). |
| **NFR-6** | Where applicable, code values **shall** be taken from the referenced international or national standards (e.g., ISO Country Codes, UK VAT numbers). |

#### 3.3 External Interface Requirements

##### 3.3.1 Software Interfaces
*   **SI-1:** The interface for all messages is defined by a set of W3C XML Schema Definition (.xsd) files.
*   **SI-2:** Character encoding for all XML messages **shall** be UTF-8.

##### 3.3.2 Communications Interfaces
*   **CI-1:** The specification of message transport protocols (e.g., AS1, AS2, SFTP, web service) is explicitly out of scope. The data standard is transport-agnostic.
*   **CI-2:** The specification of security protocols (e.g., TLS, S/MIME, XML-DSig) is explicitly out of scope.

### 4. Appendices

#### 4.1 Data Element Examples (Illustrative)
```xml
<!-- Example of core header elements present in most documents -->
<DocumentHeader>
    <DocumentID>urn:uuid:550e8400-e29b-41d4-a716-446655440000</DocumentID>
    <DocumentStatus>Original</DocumentStatus>
    <IssueDateTime>2023-10-27T14:30:00Z</IssueDateTime>
    <BuyerParty>
        <ID scheme="GB:VAT">GB123456789</ID>
        <Name>Example Public Body</Name>
    </BuyerParty>
    <SellerParty>
        <ID scheme="GB:VAT">GB987654321</ID>
        <Name>Example Supplier Ltd</Name>
    </SellerParty>
</DocumentHeader>

<!-- Example of a line item referencing a PO LineID -->
<InvoiceLine>
    <LineID>urn:uuid:123e4567-e89b-12d3-a456-426614174000</LineID>
    <ReferencedPurchaseOrderLineID>urn:uuid:550e8400-e29b-41d4-a716-446655440001</ReferencedPurchaseOrderLineID>
    <ItemDescription>Technical Consultancy - Senior</ItemDescription>
    <InvoicedQuantity unitCode="DAY">5</InvoicedQuantity>
    <LinePriceAmount currencyID="GBP">750.00</LinePriceAmount>
</InvoiceLine>
```

#### 4.2 Document Flow Scenario
**Typical Procure-to-Pay Sequence:**
1.  Buyer (`Originator`) → Seller (`Sales Point`): **RFQ**
2.  Seller → Buyer: **Quotation**
3.  Buyer (`Order Point`) → Seller: **Purchase Order** (`Status=Original`)
4.  Seller → Buyer: **PO Response** (`Status=Original`, indicating acceptance)
5.  Seller (`Despatch Point`) → Buyer: **Fulfilment Notification**
6.  Buyer (`Delivery Point`) → Seller: **Receipt Advice**
7.  Seller (`Accounts Receivable`) → Buyer: **Invoice** (referencing PO and Receipt)
8.  Buyer (`Accounts Payable`) → Seller: **Remittance Advice** (referencing Invoice)

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Technical Lead | | | |
| Governance Authority | | | |