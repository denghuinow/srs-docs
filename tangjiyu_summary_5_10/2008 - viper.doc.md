- # 2008 - viper.md

  ## System Overview
  This document outlines the Software Requirements Specification (SRS) for the SCM (Supply Chain Management) system developed by VIPER Team. The system aims to streamline supply chain processes for Ejada company, focusing on customer service management, procurement, product development, manufacturing flow management, and more.

  ## Key Requirements

  ### 1. Purpose
  - **Objective**: Describe the external behavior and non-functional requirements (usability, availability, security, maintainability, reliability) of the SCM system.

  ### 2. Scope
  - **Baseline Document**: This SRS serves as the foundation for subsequent software development lifecycle phases.

  ### 3. Definitions, Acronyms, and Abbreviations
  - **SYSTEM**: Supply Chain Management Software.
  - **SCM**: Supply Chain Management.
  - **ERP**: Enterprise Resource Planning.

  ### 4. Product Perspective
  - **Objective**: Deliver Ejada company products and services efficiently and cost-effectively, comparable to larger systems from Oracle and SAP but tailored to Ejada's needs.

  ### 5. Product Functions
  - **Customer Service Management**: Simple processes to establish and maintain customer rapport.
  - **Procurement**: Manage procurement processes.
  - **Product Development**: Coordinate with CRM to identify customer needs and manage product development.
  - **Manufacturing Flow**: Develop production technology and integrate into the supply chain.
  - **Outsourcing and Partnerships**: Maintain outsourcing and partnerships.
  - **Performance Measurement**: Measure cost, customer service, productivity, asset, and quality performance.

  ### 6. User Characteristics
  - **Users**: Ejada employees, customers, and suppliers with basic computer knowledge.

  ### 7. Constraints
  - **Web-based System**: Must be compliant with .Net technologies (ASP.NET, C#, MS SQL).
  - **Integration**: Future integration with other modules in Ejada's framework.

  ### 8. Assumptions & Dependencies
  - **Server**: Suitable Microsoft OS with internet connection.

  ### 9. Interface Requirements
  - **User Interface**: Web-based interface with login, domain selection (coordinator, customer, supplier), and navigation bars.
  - **Software Interfaces**: SQL Server (Version 7.0.1), Internet Explorer (Versions 6, 7), Mozilla Firefox (Versions 2, 3).
  - **Communication Interfaces**: TCP/IP for internet/network communication.

  ### 10. Functional Requirements
  - **Request Management**: Coordinator can add, view, edit, and delete requests.
  - **Item Management**: Coordinator can manage items including adding, viewing, editing, and deleting.
  - **Customer Management**: Coordinator can add, view, edit, and delete customer information.
  - **Supplier Management**: Coordinator can add, view, edit, and delete supplier information.

  ### 11. Performance Requirements
  - **Concurrent Users**: Handle at least 100 concurrent users.
  - **Transaction Time**: 90% of transactions must be completed in less than 1 second.

  ### 12. Logical Database Requirements
  - **Tables**: Coordinator, Customer, Supplier, Resource Location, Item, Request.

  ### 13. Design Constraints
  - **Programming Language**: ASP.NET, C#.
  - **Database**: MS SQL.
  - **Software Process**: Waterfall model with Object-Oriented design.

  ### 14. Software System Attributes
  - **Reliability**: Daily automatic data backup, error detection, and recovery mechanisms.
  - **Availability**: 100% uptime, understandable feedback in case of fatal errors.
  - **Security**: Role-based access control (coordinator, supplier, customer).
  - **Maintainability**: Modular design for easy error detection and updates.
  - **Portability**: Operable on latest Microsoft OS with .Net framework and IIS.15. Change Management Process

  - **Documentation**: All changes in SRS will be documented with date, author, affected sections, and reasons for changes.