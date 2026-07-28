# Detailed Summary: TACHOnet Software Requirements Specification

## Background and Scope
TACHOnet is a network system designed to facilitate secure communication between Member States' Card Issuing Authorities (CIAs) for managing tachograph driver smart cards. The system enables checking driver card issuance, verifying card status, declaring card status modifications, and assigning cards to driving licenses across borders. It ensures data privacy, non-repudiation, and prevents the reconstruction of a consolidated European database. Non-goals include managing individual CIA users (handled by each Member State) and supporting non-tachograph card types beyond the defined scope.

## Stakeholders Matrix and Use Cases
*   **CIA Application:** Represents the Card Issuing Authority's system as a single entity; exchanges XML messages with TACHOnet for administrative tasks.
*   **CIA Administrator:** A user within a Member State responsible for administering the CIA application and browsing TACHOnet usage statistics via a secure web interface.
*   **TCN Administrator:** Responsible for the overall administration, configuration, monitoring, and maintenance of the TACHOnet system.
*   **CIA User:** Clerks or enforcement officers within a Member State who perform administrative tasks; may access TACHOnet web services (e.g., Phonex, transliteration) but are managed locally by the CIA.

**Main/Exception Scenarios (≤8):**
1.  **Check Driver's Issued Cards:** A CIA requests verification if a driver has been issued a card in another Member State (online or batch mode).
2.  **Check Tachograph Card Status:** A CIA or enforcer verifies the current status (e.g., valid, lost, stolen) of a specific tachograph card.
3.  **Declaration of Card Status Modification:** A CIA declares a change in a card's status (e.g., to lost, stolen, confiscated) to the issuing Member State.
4.  **Send Card/Driving License Assignment:** A CIA notifies the driving license issuing Member State when a new card is issued against a foreign license.
5.  **Get Phonex Search Keys:** A CIA obtains standardized phonetic search keys for driver names to enable consistent cross-border searches.
6.  **Generate/Browse Statistics:** Automated nightly generation and secure web-based browsing of system usage statistics (e.g., request volumes, status codes, response times).
7.  **Monitor the System:** The TCN Administrator uses monitoring tools (e.g., Microsoft Operations Manager) to ensure system health and performance.
8.  **Manage Member State:** The TCN Administrator adds, configures, or updates Member State CIAs within the TACHOnet system (BizTalk configuration, reporting accounts).

## Business Process
**Main Process: Handle Administrative Request (e.g., Check Driver's Issued Cards)**
*   **Trigger:** Receipt of an encrypted XML request from a CIA Application.
*   **Input:** XML request message.
*   **Process:**
    1.  Decrypt and log the original request.
    2.  Validate syntax and assign a unique TACHOnet reference ID (TCNRefId).
    3.  Parse request and group sub-requests by target issuing Member State(s).
    4.  For each target Member State, build a new request, log it, encrypt it, and send it.
    5.  Wait for and collect responses from each target CIA.
    6.  For each response, decrypt, log, validate, and store the data.
    7.  Upon receiving all responses or reaching a timeout, build a consolidated response.
    8.  Log, encrypt, and send the consolidated response back to the original requesting CIA.
*   **Output:** XML response message to the requesting CIA.
*   **Key Branches:**
    *   **Invalid Message:** If the request is syntactically invalid, immediately return a negative receipt and alert the TCN Administrator.
    *   **Timeout or Error:** If a response is not received in time or indicates an error, log the event and reflect the status (e.g., 'timeout', 'Server Error') in the consolidated response.

## Domain Model (Entities ≤8)
*   **Transaction (TCNRefId):** Core entity tracking each request/response cycle. Fields: TCNRefId (unique), RequestTimestamp, RequestingCIA, RequestType, Status, TimeoutDateTime.
*   **Member State / CIA:** Represents a participating country's authority. Fields: CountryCode (unique), CIA_Name, ContactInfo, DigitalCertificate, URL_Endpoint.
*   **Driver Query:** Represents a sub-request within a transaction. Fields: QueryId, Surname, FirstNames, DateOfBirth, SearchKey_Surname, SearchKey_FirstName, IssuingMemberStateCode (reference).
*   **Card Query:** Represents a card status check request. Fields: QueryId, CardNumber, CardType, IssuingMemberStateCode (reference, required).
*   **Card Status Modification:** Represents a request to change a card's state. Fields: ModificationId, CardNumber, NewStatus (required), Reason, IssuingMemberStateCode (reference, required).
*   **Driving License Assignment:** Links a card to a foreign driving license. Fields: AssignmentId, CardNumber, DrivingLicenseNumber, DrivingLicenseIssuingNation (required).
*   **Message Log:** Records all raw messages for tracking and non-repudiation. Fields: LogId, Timestamp, Direction (In/Out), MessageContent (required), TCNRefId (reference).
*   **Statistics Snapshot:** Aggregated data for reporting. Fields: SnapshotDate, CIA_Code, RequestType, StatusCode, Count, AverageResponseTime.

## Interfaces and Integrations (≤8)
1.  **CIA Application Interface (XML over TESTA-II)**
    *   **Direction:** Bidirectional.
    *   **Interaction:** Asynchronous exchange of encrypted XML messages for all administrative use cases (UC-01 to UC-04).
    *   **Input Key Points:** Encrypted XML requests adhering to TCN schema.
    *   **Output Key Points:** Encrypted XML responses or receipts.
    *   **SLA Key Points:** High availability (24x7), response time for enforcement requests <1 minute, automatic retry on failure.

2.  **Phonex/Transliteration Web Service**
    *   **Direction:** TACHOnet to CIA User/Application.
    *   **Interaction:** Synchronous web service (and web UI) to compute phonetic search keys and perform character transliteration (UC-05, UC-06).
    *   **Input Key Points:** UTF-8 encoded name strings.
    *   **Output Key Points:** Computed search keys or transliterated strings.
    *   **SLA Key Points:** Available over TESTA network, downloadable component for local installation.

3.  **Statistics Reporting Web Interface**
    *   **Direction:** TACHOnet to CIA/TCN Administrator.
    *   **Interaction:** Secure web portal (ReportManager) for browsing and downloading pre-generated usage statistics reports (UC-10).
    *   **Input Key Points:** User credentials (Windows Authentication), report parameters.
    *   **Output Key Points:** Dynamic reports in HTML, XML, Excel formats.
    *   **SLA Key Points:** Secure access, data updated nightly.

4.  **Monitoring Interface (MOM)**
    *   **Direction:** TACHOnet to TCN Administrator.
    *   **Interaction:** Integration with Microsoft Operations Manager for system health and performance monitoring (UC-12).
    *   **Input Key Points:** System events, performance counters from TACHOnet servers and BizTalk.
    *   **Output Key Points:** Alerts and notifications in the MOM console.
    *   **SLA Key Points:** Configurable alert rules, dependent on Data Center FW policies.

5.  **Backend Data Processing (SQL Server)**
    *   **Direction:** Internal.
    *   **Interaction:** SQL Server Agent jobs and Integration Services (DTS) for nightly transfer of transaction data to a data warehouse and OLAP cube processing for statistics (UC-09).
    *   **Input Key Points:** Expired transactions from the production tracking database.
    *   **Output Key Points:** Processed data in the data warehouse and OLAP cubes.
    *   **SLA Key Points:** Scheduled execution, must not impact production performance.

## Acceptance Criteria (2–4 per capability)
*   **Capability: Cross-Border Driver Card Check**
    *   Given a CIA submits a valid "Check Driver's Issued Cards" request for a driver, When TACHOnet processes it and receives responses from all target Member States, Then the CIA receives a consolidated response within the defined timeout period.
    *   Given a CIA submits a batch request with an invalid XML format, When TACHOnet receives it, Then the system immediately returns a negative receipt and logs an alert for the administrator.
*   **Capability: Secure Message Handling**
    *   Given any XML message is sent to or from TACHOnet, When the message transport is complete, Then an immutable, encrypted log of the raw message is stored in the tracking database.
    *   Given a network failure occurs while sending a request to a Member State, When the failure persists, Then TACHOnet retries 3 times before recording a 'Server Error' status.
*   **Capability: Administrative Reporting**
    *   Given the nightly statistics job runs, When it completes, Then the CIA Administrator can log into the secure web portal and view updated reports for their Member State.
    *   Given a CIA Administrator has forgotten their password, When the TCN Administrator resets it via Active Directory, Then the CIA Administrator can log in and is prompted to set a new password.

## Non-Functional Metrics
*   **Performance:** System must respond to user requests rapidly irrespective of background tasks; enforcement authority request response time <1 minute.
*   **Reliability:** High availability (24x7 operation); designed for robustness, tolerance to operator errors, and clean recovery from disasters.
*   **Security:** Guaranteed non-repudiation and data privacy for all transactions; access to statistics portal secured via Windows accounts.
*   **Compliance:** Must use TESTA-II network facilities; adhere to defined XML messaging standards and cryptographic policies.
*   **Observability:** All messages logged as-is for tracking; system monitoring via MOM with configurable alerts for BizTalk and infrastructure.

## Milestones and Release Strategy (≤6)
1.  Finalize and approve Software Requirements Specification (SRS v01_00).
2.  Complete detailed design for core messaging flows and security architecture.
3.  Develop and unit test core TACHOnet components (message routing, encryption/decryption, logging).
4.  Integrate with TESTA-II network and conduct end-to-end testing with pilot Member States.
5.  Deploy production environment, configure initial Member States, and conduct user acceptance testing (UAT).
6.  Go-live and operational handover to support team.

## Risk List and Mitigation Strategies (≤8)
1.  **Risk:** High volume of messages leads to tracking database performance degradation.
    *   **Mitigation:** Implement proactive database sizing, archiving strategy for old messages, and performance tuning.
2.  **Risk:** Member State CIA systems have varying technical capabilities, leading to integration failures.
    *   **Mitigation:** Provide clear interface specifications, reference implementations, and a conformance testing phase.
3.  **Risk:** Security breach compromising card holder data or system integrity.
    *   **Mitigation:** Enforce strict cryptographic standards, regular security audits, and principle of data minimization (no consolidated DB).
4.  **Risk:** Failure of the TESTA-II network causes system unavailability.
    *   **Mitigation:** Design for graceful degradation where possible; establish clear communication protocols with network provider.
5.  **Risk:** Inability to meet the <1 minute response time requirement for enforcement requests.
    *   **Mitigation:** Optimize message processing pipelines, enforce SLA on Member State responses, and implement caching where appropriate.
6.  **Risk:** Complex BizTalk configuration leads to errors when adding new Member States.
    *   **Mitigation:** Create detailed, scripted procedures and checklists for the "Manage Member State" process.
7.  **Risk:** Statistics generation job impacts the performance of the live transaction system.
    *   **Mitigation:** Schedule resource-intensive jobs for off-peak hours and use separate reporting databases.
8.  **Risk:** Lack of clarity on long-term data retention policy for message logs.
    *   **Mitigation:** Document the open issue and define a policy with legal/compliance stakeholders prior to go-live.

## Undecided Issues and Responsible Parties (≤8)
1.  **How long should TACHOnet keep detailed message logs in the tracking database before archiving?** (Responsible: DG TREN / Legal & Compliance)
2.  **What is the exact firewall configuration required between TACHOnet servers and the central MOM monitoring console?** (Responsible: EC DI's Data Center & TCN Administrator)
3.  **Which specific BizTalk Management Pack rules need to be configured in MOM for effective TACHOnet monitoring?** (Responsible: TCN Administrator & MOM Specialists)
4.  **Are there requirements for supporting transliteration from character sets other than Greek/Latin (e.g., Cyrillic)?** (Responsible: DG TREN / Member State Representatives)
5.  **What is the detailed process and criteria for removing a Member State from the TACHOnet configuration?** (Responsible: DG TREN / TCN Administrator)
6.  **Final agreement on the set of allowed card status transitions for the "Declaration of Card Status Modification" use case.** (Responsible: Card Issuing Working Group / DG TREN)