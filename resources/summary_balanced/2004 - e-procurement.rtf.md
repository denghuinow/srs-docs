# Balanced Summary

## Goals and Scope
This specification defines functional requirements for eProcurement interoperability across UK public sector organizations, covering the procurement cycle from catalogue to remittance. It establishes a common language for electronic document exchange between buyers and sellers using XML, while excluding aspects like seller discovery, e-auctions, and message transport security. The approach supports incremental implementation starting with core documents like Purchase Orders and Invoices.

## Roles and User Stories
- **Purchasing Manager**: I want to maintain trading agreements and catalogue data so that procurement relationships are properly managed
- **Originator**: I want to request quotations for goods/services so that I can obtain competitive pricing
- **Order Point**: I want to create purchase orders so that I can formally commit to purchases
- **Delivery Point**: I want to report receipt variances so that delivery issues can be resolved
- **Accounts Payable**: I want to process invoices and payments so that financial obligations are met accurately

## Key Processes
1. **Sourcing** (triggered by procurement need): Exchange catalogue information, RFQs and quotations between parties
2. **Ordering** (triggered by purchase decision): Create and respond to purchase orders
3. **Fulfilment** (triggered by order acceptance): Notify delivery, acknowledge receipt, and resolve variances
4. **Accounting** (triggered by delivery completion): Process invoices, credit/debit notes, and payment remittances

## Domain Data Elements
- **Party**: UUID (primary key), Contact Name, Address, VAT Identifier, Registration Number
- **Document**: Document UUID (primary key), Document ID, Document Date, Status, Sender/Receiver
- **Line**: Line UUID (primary key), Line Number, Status, Quantity, Amount
- **Item**: Item Name (primary key), Unit of Measure, Seller Item ID, GTIN, Commodity Class

## Non-functional Requirements
- Semantic interoperability through standardized identifiers and codes
- Compliance with e-Government Interoperability Framework (e-GIF)
- Support for incremental implementation approach
- Modular and extensible design for specialized business contexts
- XML schema validation capability

## Milestones and External Dependencies
- Support for 100% electronic government-business interactions by 2005
- Compliance with international standards (ISO codes, UNSPSC)
- Adherence to VAT requirements for fiscal documents
- Dependence on established coding schemes (GTIN, GLN, D-U-N-S)
- Alignment with Government Data Standards Catalogue

## Risks and Mitigation Strategies
- **Identifier mismatches**: Use UUIDs for exact machine matching alongside existing IDs
- **Implementation complexity**: Support incremental adoption starting with core documents
- **Semantic interpretation**: Standardize data element definitions across all documents
- **VAT compliance**: Include mandatory VAT evidence and identifiers in fiscal documents

## Undecided Issues
- Specific XML schema implementation details
- Business rules for document variants and revisions
- Third party communication protocols
- Data protection and retention policies
- Internal system design requirements
- Not mentioned