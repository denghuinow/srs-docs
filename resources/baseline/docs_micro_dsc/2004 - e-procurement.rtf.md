# Software Requirements Specification (SRS)
## Electronic Procurement Document Interoperability System (EPDIS)
**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Approved for Development

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for a system enabling standardized electronic procurement document exchange between public sector buyers and external sellers. The primary purpose is to ensure seamless, unambiguous, and legally compliant interoperability across the entire procurement lifecycle, from catalogue publication to final remittance.

#### 1.2 Scope
The scope of this project encompasses the definition, structure, validation, and exchange protocol for a suite of electronic business documents. The system will facilitate the automated exchange between disparate buyer (public sector) and seller (external vendor) systems.

**In-Scope:**
*   Specification of XML schemas for core procurement documents.
*   Rules for unique identification and cross-document referencing.
*   Validation against the e-Government Interoperability Framework (e-GIF).
*   Definition of mandatory metadata attributes (e.g., document status).
*   Mandate for the use of standardized code lists.

**Out-of-Scope:**
*   Development of specific buyer or seller Enterprise Resource Planning (ERP) or procurement applications.
*   User interface design for end-user applications.
*   Payment gateway or financial settlement processing.
*   Long-term archival and retrieval systems.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **e-GIF:** e-Government Interoperability Framework. The set of policies and standards governing IT interoperability in the public sector.
*   **XML:** eXtensible Markup Language. A markup language that defines a set of rules for encoding documents.
*   **UBL:** Universal Business Language (OASIS standard). May be referenced as a potential alignment standard.
*   **PEPPOL:** Pan-European Public Procurement Online. A network and set of specifications for e-procurement.
*   **ID:** Identifier.
*   **SRS:** Software Requirements Specification.

#### 1.4 References
*   e-Government Interoperability Framework (e-GIF) - [Latest Version]
*   ISO/IEC 19845:2015 - Universal Business Language (UBL) Version 2.1
*   UN/CEFACT Cross Industry Invoice (CII) schema
*   ISO 20022 - Financial services - Universal financial industry message scheme
*   Relevant national coding standards for parties (e.g., VAT ID, Legal Entity Identifier) and products (e.g., UNSPSC, CPV).

#### 1.5 Overview
The remainder of this document describes the overall description of the system (Section 2) and the specific requirements (Section 3). It is structured to provide stakeholders, architects, and developers with a complete and unambiguous specification for implementation.

---

### 2. Overall Description

#### 2.1 Product Perspective
The EPDIS is not a standalone application but a **specification and set of constraints** that must be implemented by both buyer and seller systems to achieve interoperability. It acts as a middleware "contract" between independent systems.

#### 2.2 Product Functions
The core functions mandated by this specification are:
1.  **Document Exchange:** Ability to generate, transmit, receive, and process standardized electronic documents.
2.  **Identification & Traceability:** Ability to assign and resolve unique identifiers to documents, trading parties, and line items, creating an auditable trail across the procurement cycle.
3.  **Document Lifecycle Management:** Ability to manage document status (original, copy, revision, cancellation) and handle revisions or cancellations appropriately.
4.  **Validation:** Ability to validate document structure, data types, and code values against the defined XML schemas and code lists.

#### 2.3 User Characteristics
The primary "users" are systems and applications, with the following human roles interfacing indirectly:
*   **Public Sector Buyer Administrators:** Configure their procurement systems to comply with this specification.
*   **Seller/Vendor IT Staff:** Configure their invoicing/order management systems to comply with this specification.
*   **System Integrators:** Develop or adapt middleware to ensure compliance for their clients.

#### 2.4 Constraints
1.  **Technical Constraint:** All electronic documents **must** be implemented as XML 1.0 or later.
2.  **Regulatory Constraint:** All implementations **must** comply with the national e-Government Interoperability Framework (e-GIF).
3.  **Design Constraint:** A `DocumentStatus` attribute with a controlled vocabulary is **mandatory** in the root element of every document type.
4.  **Data Constraint:** Identifiers for parties, items, and currencies **must** use standardized international (e.g., ISO 4217 for currency) or national codes.

#### 2.5 Assumptions and Dependencies
*   It is assumed that both buyer and seller systems possess basic capabilities for XML generation, parsing, and transport (e.g., via AS4, web services, or secure email).
*   The specification depends on the availability and maintenance of the referenced external code lists and standards.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 System Interfaces
*   **SI-1:** The document exchange mechanism shall support secure, reliable transport protocols as recommended by the e-GIF (e.g., HTTPS with mutual authentication, AS4).
*   **SI-2:** System endpoints shall be capable of accepting and responding with XML documents conforming to the schemas defined in this SRS.

##### 3.1.2 Data Interfaces
*   **DI-1:** All data exchange shall be in the form of XML instance documents.
*   **DI-2:** The character encoding for all XML documents shall be UTF-8.

#### 3.2 Functional Requirements

##### 3.2.1 Document Structure & Compliance
*   **FR-1:** The system shall define and enforce XML Schema Definitions (XSD) for the following core document types:
    *   Catalogue
    *   Purchase Order
    *   Order Response
    *   Despatch Advice
    *   Invoice
    *   Credit Note
    *   Remittance Advice
*   **FR-2:** All XML instance documents shall validate without error against their respective XSDs.
*   **FR-3:** All document schemas shall incorporate the e-GIF core components and naming conventions where applicable.

##### 3.2.2 Unique Identification & Referencing
*   **FR-4:** Each document instance shall have a globally unique identifier (`DocumentID`), composed of the issuing party's ID and a unique sequence.
*   **FR-5:** A Purchase Order document shall contain a unique `BuyerOrderID` and `SellerOrderID`.
*   **FR-6:** An Invoice document shall contain mandatory references (`OrderReference`) to the related Purchase Order's `BuyerOrderID`.
*   **FR-7:** Each line item within a document shall have a unique `LineID` within that document.
*   **FR-8:** Invoice line items shall be able to reference (`OrderLineReference`) the specific `LineID` of the corresponding Purchase Order line item.

##### 3.2.3 Document Status Management
*   **FR-9:** The root element of every document shall contain a mandatory `DocumentStatus` attribute.
*   **FR-10:** The `DocumentStatus` attribute shall have a value restricted to the following list:
    *   `Original`
    *   `Copy`
    *   `Revision`
    *   `Cancellation`
*   **FR-11:** A document with `DocumentStatus="Cancellation"` shall contain a mandatory reference to the `DocumentID` of the document it is canceling.

##### 3.2.4 Standardized Code Usage
*   **FR-12:** Party identifiers (buyer, seller) shall use official national registration numbers (e.g., VAT ID, Company Number) as defined by the e-GIF.
*   **FR-13:** Item identifiers shall use a standard classification code (e.g., UNSPSC, CPV Code) in a dedicated `ItemClassificationCode` element.
*   **FR-14:** Currency codes shall conform to ISO 4217 (3-letter alphabetic code).
*   **FR-15:** Country codes shall conform to ISO 3166-1 alpha-2 (2-letter code).

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **PER-1:** The XML schemas shall be designed to allow for efficient parsing and validation by standard XML tools.

##### 3.3.2 Security Requirements
*   **SEC-1:** The specification shall recommend digital signature standards (e.g., XML-DSig) for document integrity and non-repudiation, as per e-GIF guidelines.
*   **SEC-2:** All identifiers shall not contain personally identifiable information (PII) unless absolutely necessary and in compliance with data protection regulations.

##### 3.3.3 Data Quality Requirements
*   **DQ-1:** The use of codes over free-text descriptions shall be maximized to ensure unambiguous data exchange.

#### 3.4 Logical Data Model (Excerpt)
A high-level view of core elements and their relationships:

```xml
<!-- Example of a simplified Invoice root element structure -->
<Invoice xmlns="urn:epdis:invoice:2.0"
         DocumentStatus="Original">
    <DocumentID>INV-2023-10-12345</DocumentID>
    <IssueDate>2023-10-27</IssueDate>

    <BuyerParty>
        <PartyID schemeID="VAT">GB123456789</PartyID>
        <PartyName>Public Sector Body Ltd.</PartyName>
    </BuyerParty>

    <SellerParty>
        <PartyID schemeID="VAT">GB987654321</PartyID>
        <PartyName>Vendor Corp.</PartyName>
    </SellerParty>

    <OrderReference>
        <BuyerOrderID>PO-2023-09-555</BuyerOrderID>
    </OrderReference>

    <InvoiceLine>
        <LineID>1</LineID>
        <OrderLineReference>1</OrderLineReference>
        <Item>
            <Description>Office Supplies</Description>
            <ItemClassificationCode listID="UNSPSC">44121600</ItemClassificationCode>
        </Item>
        <Quantity unitCode="EA">10</Quantity>
        <Price>
            <Amount currencyID="GBP">15.00</Amount>
        </Price>
        <LineTotal currencyID="GBP">150.00</LineTotal>
    </InvoiceLine>

    <LegalTotal currencyID="GBP">150.00</LegalTotal>
</Invoice>
```

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| Quality Assurance | | | |