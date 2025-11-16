# eProcurement Functional Requirements Specification v4.0

## Overview
This specification defines functional requirements for eProcurement interoperability in the UK public sector, covering information exchange from catalogue to remittance. It provides a common language for describing eProcurement documents that is modular and extensible.

## Scope
- Covers electronic document exchange between public sector Buyers and external Sellers
- Applies to all industry sectors
- Messages implemented as XML documents compliant with e-Government Interoperability Framework (e-GIF)
- Excludes: seller discovery, online negotiations, e-tendering, third-party communications, message transport/security, data protection rules

## Key Benefits
- Generates value for money efficiency savings
- Supports UK's goal to be best place for e-business
- Enables 100% electronic government-business interactions by 2005
- Reduces back-office costs through automation (e.g., three-way matching)
- Provides SMEs with clear standards for trading with Government
- Reduces need for software providers to support multiple specifications

## Methodology
- Developed by Office of Government Commerce (OGC) e-Commerce team
- Based on e-Service Development Framework (e-SDF)
- Refined through public consultation and expert input

## Core Components

### Business Processes
- Interactions between parties throughout procurement cycle
- Defined party roles: Buyer, Seller, Carrier, Bank, Fiscal Authority
- Standardized codes and identifiers

### Common Elements
- **Party**: Organizations and individuals participating in procurement
- **Document**: Electronic messages exchanged between parties
- **Line**: Details within documents (items, quantities, prices)
- **Item**: Goods or services being procured
- **Data Types**: Standardized data formats

### Document Types
1. **Catalogue**: Product/service listings with pricing
2. **RFQ (Request for Quotation)**: Request for pricing information
3. **Quotation**: Seller's response to RFQ with pricing/terms
4. **Purchase Order (PO)**: Buyer's request for goods/services
5. **PO Response**: Seller's acceptance/rejection of PO
6. **Fulfilment Notification**: Seller's notification of shipment
7. **Receipt Advice**: Buyer's confirmation of goods receipt
8. **Rectification Advice**: Seller's proposed solution to discrepancies
9. **Invoice**: Seller's request for payment
10. **Self Billed Invoice**: Buyer-generated invoice
11. **Credit Note**: Seller's confirmation of buyer credit
12. **Debit Note**: Buyer's notification of seller debit
13. **Remittance Advice**: Buyer's payment notification
14. **Statement**: Account status summary

### Document Status Attributes
All documents include mandatory status:
- Original: First sent document
- Copy: Reproduction of original
- Revision: Modified version of original
- Cancellation: Complete withdrawal of original

## Technical Standards
- XML markup with XML schema validation
- Compliance with e-Government Interoperability Framework (e-GIF)
- Use of standardized codes and identifiers
