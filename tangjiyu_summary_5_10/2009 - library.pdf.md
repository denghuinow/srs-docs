# 2009 - library.md

## System Overview
This document outlines the Software Requirements Specification (SRS) for the Management Processes of an Integrated Library System (ILS), focusing on functional and nonfunctional requirements to support library services, programs, and policies.^[1]^

## Key Requirements

### 1. Purpose and Perspective
- **Objective**: Define requirements for management processes within the Georgia Public Library Service's PINES system.^[2]^
- **Mission**: Enhance Evergreen ILS reports interface and management capabilities.^[3]^

### 2. Product Scope and Features
- **Management Activities**: Support analyzing library collections, patron demographics, staff productivity, and financial transactions.^[4]^
- **ILS Integration**: Presuppose general ILS functionality, focusing on management-specific requirements.^[5]^

### 3. Intended Audience
- **Stakeholders**: Library managers, staff, software project managers, and developers.^[6]^
- **Collaboration**: Highly collaborative and iterative environment for software development.^[7]^

### 4. User Classes and Characteristics
- **Patrons**: Georgia residents utilizing library resources.^[8]^
- **Staff**: Paid employees involved in library service design and provision.^[9]^
- **Administrators**: Local and global system administrators overseeing library processes.^[10]^

### 5. Operating Environment
- **Scalability**: Support 286 library locations, 17 million annual circulations.^[11]^
- **Accessibility**: Web-browser and Windows-compatible client access, with screen-reading software support.^[12]^

### 6. Design and Implementation Constraints
- **Database**: Fully relational database back-end.^[13]^
- **Standards Compliance**: Produce standards-compliant HTML.^[14]^
- **Security**: User rights and privileges controlled through security groups/roles.^[15]^

### 7. Management Tools: General
- **Streamlined Login**: Support streamlined staff login methods.^[16]^
- **Report Templates**: Create and modify report templates with fine-grained permissions.^[17]^
- **Query Tool**: User-friendly interface for designing queries against all record types.^[18]^

### 8. Management Tools: Demographics
- **Behavior Analysis**: Produce statistics on patron behavior and material use.^[19]^
- **Demographic Statistics**: Generate useful, anonymized demographic statistics.^[20]^

### 9. Management Tools: Inventory Control
- **Material Volume Report**: Report on material volume by category.^[21]^
- **Shelf Space Report**: Compare circulations, collection size, and shelf space by genre/format.^[22]^
- **Item Transfer Utility**: Utility for transferring batches of items between branches.^[23]^

### 10. Management Tools: Patron Records
- **Patron Characteristics**: Query and report by patron characteristics (age, zip code, etc.^[24]^).^[25]^
- **Inactive Patrons Report**: Generate list of inactive patrons.^[26]^

### 11. Management Tools: Transaction Records
- **Transaction History**: Maintain transaction history with configurable retention periods.^[27]^
- **Types of Transactions**: Count and categorize different types of check-ins and check-outs.^[28]^

### 12. Management Tools: Financial Records
- **Value of Items Report**: Generate reports on the value of items in the collection.^[29]^
- **Financial Reports**: Provide financial reports including patron account balances, fines, and payments.^[30]^

### 13. Assumptions and Dependencies
- **Enterprise System**: Part of an enterprise-level Library Automation System.^[31]^
- **Data Structures**: Rely on data structures and functionality of an enterprise-level ILS.