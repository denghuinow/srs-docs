# Balanced Summary: Pontis 5.0 Bridge Management System

## Goals and Scope
Pontis 5.0 is the next-generation Bridge Management System (BMS) designed to replace Pontis 4.x, providing a robust repository for bridge data and technically correct bridge management capabilities. It aims to offer a technologically up-to-date, flexible, and customizable application while preserving agency investments in existing BMS implementations.

## Stakeholders and User Stories
*   **Pontis Users:** Day-to-day users who initiate and review requirements.
*   **Pontis Task Force:** Ensures product quality, technical correctness, and provides oversight.
*   **Technical Advisory Group (TAG):** Develops requirements, architecture, and the implementation plan.
*   **BRIDGEWare Integration TAG:** Assesses impacts on BRIDGEWare and coordinates database design.
*   **AASHTO:** Manages the project, product quality, marketing, and licensing.
*   **Contractor:** Responsible for developing the Pontis software.

**User Stories:**
1.  As an **Inspector**, I want to **create and edit bridge inspection data** so that **field-collected condition information is accurately recorded**.
2.  As a **Bridge Management Engineer**, I want to **run program simulations** so that **I can forecast network trends and generate work recommendations**.
3.  As a **Bridge Project Planner**, I want to **create and edit projects by assigning work items** so that **bridge maintenance and improvement plans are developed**.
4.  As a **System Administrator**, I want to **define user roles and manage application configurations** so that **system access and behavior align with agency policies**.
5.  As a **Data Analyst**, I want to **browse, filter, and select bridge and project data** so that **I can review inventory and generate reports**.
6.  As an **Engineer**, I want to **develop and update preservation policies and cost models** so that **the system's deterioration and action recommendations remain accurate**.

## Key Processes
1.  **Browse Data:** Users find and view bridge or project data, triggered by a login.
2.  **Inventory & Inspection:** Inspectors create or edit structure inventory and inspection records, triggered by new data collection.
3.  **Calculate Derived Results:** The system calculates NBI condition ratings and Sufficiency Ratings, triggered by saving inspection data.
4.  **Preservation Model Development:** Users update deterioration probabilities and action costs to develop optimal preservation policies, triggered by new cost data or expert input.
5.  **Program Simulation:** Users configure and run network-level simulations to generate work recommendations, triggered by a need for program analysis.
6.  **Project Development:** Users create projects by assigning simulation results or inspector recommendations, triggered by planning cycles.
7.  **Data Management:** Users import/export data (e.g., NBI, PDI, XML) and perform validation, triggered by data exchange needs or quality checks.

## Domain Data Elements
*   **Structure:** (Primary Key: Structure ID) - Name, Feature Intersected, Location, Construction Date.
*   **Inspection:** (Primary Key: Inspection ID) - Inspection Date, Inspector, Element Conditions, NBI Ratings.
*   **Project:** (Primary Key: Project ID) - Project Name, Program, Status, Budget, End Date.
*   **Preservation Policy:** (Primary Key: Policy ID) - Element, Action, Cost, Transition Probability.
*   **Simulation Scenario:** (Primary Key: Scenario ID) - Timeframe, Budget, Included Rules, Results.
*   **User:** (Primary Key: User ID) - Name, Role, Authentication Details, Access Filters.

## Non-Functional Requirements
1.  **Usability:** Users should be comfortable with core operations after two days of training.
2.  **Performance:** Target login/logout within 2 seconds and generating a formatted report within 10-20 seconds.
3.  **Operational:** The thin client will be designed for Microsoft Internet Explorer; the standalone app requires Windows XP and .NET Framework.
4.  **Security:** Will utilize a single sign-on (SSO) approach and provide application-level security controls.
5.  **Maintainability:** Source code will be clearly documented for maintainability by other developers.
6.  **Legal:** Must export data in the specified NBI format and support future NBI coding guide changes.

## Milestones and External Dependencies
1.  Completion and approval of the Functional Requirements Specification.
2.  Coordination with the Virtis/Opis development team for BRIDGEWare integration.
3.  Incorporation of results from NCHRP Project 12-67 (Multiple-Objective Optimization).
4.  Support for TransXML schema once established by NCHRP Project 20-64.
5.  Accommodation of any changes to Federal National Bridge Inventory (NBI) coding standards.

## Risks and Mitigation Strategies
1.  **Requirement Creep:** Manage by finalizing a requirements document before development.
2.  **Technology Obsolescence:** Mitigate by adopting a phased design/development approach.
3.  **Development Cost/Schedule Overruns:** Use detailed COSMIC-FFP estimation and phased releases to control scope.
4.  **User Dissatisfaction:** Use prototypes in the design phase and gather feedback through phased releases.
5.  **Changes to NBI Standards:** Plan for flexibility in the design to accommodate anticipated changes.

## Undecided Issues
1.  Level and approach for achieving ADA (Section 508) compliance.
2.  Specific strategy for migrating user-customized PowerBuilder forms and reports.
3.  Final decision on supporting web servers other than Microsoft IIS.
4.  Resolution of "may" requirements listed in the "Waiting Room" (e.g., electronic signatures, GIS interfaces, data archiving details).
5.  Licensing arrangement for web application users.
6.  Support for tablet or handheld computers in field inspection contexts.