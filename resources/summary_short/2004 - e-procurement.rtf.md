# Short Summary

- **Background and objectives**: This document specifies functional requirements for eProcurement interoperability across the UK public sector, aiming to provide a common, modular language for electronic procurement documents from catalogue to remittance, supporting government efficiency and e-business goals.

- **In scope**:
  - Information content of messages exchanged between public sector buyers and external sellers.
  - Procurement cycle covering sourcing, ordering, fulfilment, and accounting.
  - Electronic documents marked up in XML, compliant with e-GIF.
  - Common data elements and document structures for interoperability.
  - Support for incremental implementation starting with key documents like Purchase Order and Invoice.

- **Out of scope**:
  - Seller discovery, e-auctions, and e-tendering.
  - Negotiation of trade terms and conditions.
  - Communication with third parties such as carriers, banks, or fiscal authorities.
  - Message transport, security, data protection, and retention rules.
  - Application of public sector purchasing policy.

- **Roles and core use cases**:
  - As a **Buyer**, I want to exchange procurement documents electronically so that I can automate purchasing and payment processes.
  - As a **Seller**, I want to receive and send standardized procurement messages so that I can trade efficiently with public sector organizations.
  - As an **Implementer**, I want clear interoperability specifications so that I can develop compliant software and services.

- **Success metrics**:
  - Reduction in end-to-end procurement costs through automation (e.g., three-way match).
  - Increased adoption of eProcurement across public sector and SMEs.
  - Support for 100% electronic government-business interactions by 2005.

- **Major constraints**:
  - Must use XML and comply with e-Government Interoperability Framework (e-GIF).
  - No assumptions about internal buyer or seller systems (treated as black boxes).
  - Mandatory status attribute in all documents (original, copy, revision, cancellation).
  - Reliance on international and national coding schemes (e.g., ISO, UNSPSC, VAT identifiers).
  - Support for universally unique identifiers (UUID) for exact machine matching.

- **Undecided issues**:
  - XML schema implementation details (Not mentioned).
  - Business rules for document variants, revisions, and cancellations (Not mentioned).
  - Specific data protection and retention policies (Not mentioned).
  - Integration with third-party systems like carriers or banks (Not mentioned).
  - Handling of non-standard or extended business contexts (Not mentioned).