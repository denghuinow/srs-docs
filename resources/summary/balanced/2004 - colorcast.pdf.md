# Balanced Summary: ABC Paint Project (CS179G)

## Goals and Scope
This project aims to develop a web-based application, "ColorKast," to facilitate ABC Paint's transition to a new paint numbering scheme by Q2 2004. The system will help customers and distributors convert old paint numbers to new ones and explore colors, ensuring business continuity. It is designed as a modular, standalone web application for long-term use, to be integrated into ABC Paint's existing website.

## Stakeholders and User Stories
*   **ABC Paint Customers:** End-users who need to find and translate paint colors.
*   **ABC Paint Distributors:** Business users who assist customers and require access to the translation tools.
*   **ABC Paint IT Department:** Responsible for deploying, hosting, and maintaining the application.
*   **ABC Paint Administrators (Levels 1-3):** Employees who manage paint data and user permissions within the system.
*   **ColorKast Development Team:** The group responsible for building and delivering the application.

**User Stories:**
1.  As a **customer**, I want to **translate an old paint number to the new scheme** so that **I can order the correct, current product**.
2.  As a **customer**, I want to **search for paints by name or color** so that **I can explore the available collections**.
3.  As a **distributor**, I want to **find colors closest to a given paint** so that **I can suggest alternatives to discontinued products**.
4.  As a **user**, I want to **save my recent color searches in a session** so that **I can easily refer back to them**.
5.  As an **administrator**, I want to **add, update, or delete paint information in the database** so that **the application's data remains accurate**.
6.  As the **IT department**, I want **clear setup documentation** so that **we can integrate and manage the application on our website**.

## Key Processes
1.  **Trigger: User accesses the web application.** The user navigates to the application via the ABC Paint website.
2.  **Trigger: User initiates a search or translation.** The user inputs a paint number, name, or uploads an image for matching.
3.  The application queries the backend paint and color-space databases.
4.  The server processes the request (e.g., performs translation, finds closest colors) in sub-second time.
5.  Results are formatted and returned to the user's client browser.
6.  **Trigger: User selects colors.** The user can save selected colors to their session-persistent palette.
7.  **Trigger: Administrator logs in.** Authorized admin users can manage paint data and user permissions through a separate interface.

## Domain Data Elements
*   **Paint**
    *   *Primary Key:* Paint Number (New Scheme)
    *   *Key Fields:* Old Scheme Number, Paint Name, Color Value (RGB), Collection ID
*   **Color Collection**
    *   *Primary Key:* Collection ID
    *   *Key Fields:* Collection Name, Company, Designer
*   **User Session**
    *   *Primary Key:* Session ID
    *   *Key Fields:* Client Identifier, Recent Color Searches, Uploaded Images (temp), Creation Timestamp
*   **Administrative User**
    *   *Primary Key:* Username
    *   *Key Fields:* Hashed Password, Access Level (1-3), Permissions

## Non-Functional Requirements
1.  **Performance:** Server-side color searches and translations must complete in sub-second time.
2.  **Usability:** The interface must support keyboard-only operation where possible, with a task-based design for low learning curve.
3.  **Security:** Administrative access must be secured with industry-standard authentication; general user session data is private but not secured.
4.  **Compatibility:** The client must work with Internet Explorer 4.01+, Netscape 6.0+, or Mozilla 1.0+.
5.  **Maintainability:** The application must be modular for easy updates and integration via a theming mechanism.
6.  **Client Environment:** Requires a display capable of 16.7 million colors; color accuracy depends on client calibration.

## Milestones and External Dependencies
1.  **Q2 2004:** System must be in place for customer transition.
2.  **Dependency:** Successful integration into the existing ABC Paint website.
3.  **Dependency:** Availability and performance of third-party color space and paint information databases.
4.  **Dependency:** Client and server hardware meeting specified requirements (1GHz/512MB server per 50 users).
5.  **Dependency:** Final legal review of the product by ABC Paint prior to rollout.

## Risks and Mitigation Strategies
1.  **Risk:** Client display calibration affects color accuracy for consumers.
    *   *Mitigation:* Acknowledge the limitation in documentation; consider a display calibration tool as a future extension.
2.  **Risk:** Internet latency affects perceived application performance for end-users.
    *   *Mitigation:* Clearly display server processing time separately from total request time to set expectations.
3.  **Risk:** Repetitive use of input devices could lead to user injury.
    *   *Mitigation:* Include safety disclaimers and recommend adherence to workplace ergonomic regulations.
4.  **Risk:** The "closest color" algorithm in RGB space may not yield perceptually ideal matches.
    *   *Mitigation:* Proceed with the RGB-based search as assumed acceptable; validate results with ABC Paint.
5.  **Risk:** Administrative privilege escalation if business rules are not followed.
    *   *Mitigation:* Implement strict hierarchical permission controls as specified (Level 3 > Level 2 > Level 1).

## Undecided Issues
*(Based on Appendix C, there are no formally listed undecided issues. However, the document implies the following are not fully specified or are optional.)*
1.  Implementation protocol for database interfaces (Software Interface 1 & 2).
2.  Inclusion and final specification of the low-priority **Color Sample Matcher** feature.
3.  Specific theming/stylesheet mechanism for website integration.
4.  Detailed error reporting and recovery utility specifications.
5.  Process for automatic purging of user session data after 30 days.
6.  Decision on whether to implement a client-side display calibration tool.