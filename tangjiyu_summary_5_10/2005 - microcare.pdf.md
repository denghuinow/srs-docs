# Voucher Management System - Software Requirements Specification

## 1. Introduction

### 1.1 General Overview
The Voucher Management Unit System (VMUS) is developed for Marie Stopes International Uganda (MSIU) to manage an Output-Based Aid (OBA) program for STD treatment services. The system will be developed on Oracle 9i platform with VB front-end and Crystal Reports 9 for reporting.

Key design features include:
- User-friendly interface with dropdown menus to minimize data entry errors
- Master table structure with minimal keyboard entry for faster transactions
- Easy training for users with minimal computer skills
- High security with intrusion controls and access level management
- Bar-code and bio-metrics interface capabilities

### 1.2 Purpose
This document specifies requirements for the Voucher Management System to automate the Voucher Management Unit processes, minimize manual work, maximize project quality, track progress, and enable timely decision-making.

### 1.3 Project Scope

#### 1.3.1 MSIU and OBA Program
The OBA program finances agreed outputs with predefined quality rather than inputs by selling vouchers for STD services at subsidized prices. The program targets:
- Quality health care services for STD treatment
- Sexually active population of Mbarara district
- 1-year pilot phase through qualified, approved providers

#### 1.3.2 Voucher Management System
The system controls fraud in claims and ensures timely payments to service providers. It consists of seven modules:
1. Voucher Creation/Preparation
2. Marketing/Sales
3. Claim Entry/Processing
4. Voucher Sales Return
5. Client Feedback
6. Reports (Standard and Customized)
7. Security and User Privileges

## 2. Overall Description

### 2.1 System Perspective
The system handles 20,000 vouchers in the pilot phase with scalability for future expansion. Core workflow:
- VMU creates vouchers and sells through distributors
- Distributors submit sales details
- Clients choose service providers for treatment
- Service providers submit claims to VMU field office
- Field office validates claims manually and through system
- Validated claims generate financial reports for MSIU admin team
- MSIU collects client feedback for quality monitoring

### 2.2 System Modules

#### Module 1: Voucher Creation/Preparation
- System-generated unique voucher numbers with security protocols
- Barcode printing for tracking at all levels
- Voucher structure: Project Code-Group Batch-Batch Number-Voucher Number-Security Code
- Three tear-off portions per voucher (client and partner)
- Validity date management
- Security features preventing editing/deletion after creation

#### Module 2: Marketing/Sales
**Distributor Master Information:**
- Unique distributor codes with business details
- Geographical location tracking
- Sales history reporting

**MSIU Sales Team Information:**
- Salesman details with team assignments
- Performance tracking capabilities

**Distribution Transactions:**
- Sales from MSIU to distributors
- Automatic voucher allocation from stock
- Invoice generation and payment tracking

#### Module 3: Claim Entry/Processing
**VSP Master Information:**
- Service provider details with facility information
- Payment terms management (Bi-monthly/Monthly)
- Fraud detection and automatic deactivation

**VSP Staff Master:**
- Staff details with qualifications
- Unique staff coding system

**Claim Submission and Entry:**
- Treatment form processing with validation
- Barcode reading for voucher verification
- Thumbprint comparison for fraud prevention
- Multi-level visit tracking (consultation, follow-ups)
- Automated claim amount calculation
- Quarantine system for suspicious claims

#### Module 4: Voucher Sales Return
- Distributor return processing
- Validation against original sales
- Return amount calculation

#### Module 5: Client Feedback
- Treatment satisfaction tracking
- Automatic population of treatment details
- Privacy and counseling satisfaction metrics

#### Module 6: Reports
Required reports include:
- Monthly payment reports (clean claims/withheld payments)
- Provider-specific claim reports
- Quarterly summary reports
- Syndrome frequency analysis
- Provider performance comparisons
- Quality documentation tracking

#### Module 7: Security and User Privileges
- Role-based access control through user groups
- Screen-level permissions (New/Edit/Delete/View/Print)
- Individual user management with password protection

## 3. Technical Requirements

### 3.1 Platform and Tools
- Oracle 9i database platform
- Visual Basic front-end
- Crystal Reports 9 for reporting
- Barcode reader interface
- Bio-metrics thumbprint reader interface

### 3.2 Database Design
- Sequential links with surrogate keys
- Efficient storage with defragmentation
- Scalable structure for program expansion

### 3.3 Security Features
- High intrusion controls
- Granular access level controls
- Organizational level user settings

## 4. Design Constraints
- Voucher creation limited to authorized personnel only
- Minimum voucher creation quantities
- Non-editable voucher numbers after creation
- Future date sale validation
- Mandatory information validation for all transactions
- Fraud detection through thumbprint mismatch monitoring

## 5. References
- Programme Design Study (Final report dated 10-September-2005)
- Functional Flow of VMUS (Microcare, 30th November 2005)
