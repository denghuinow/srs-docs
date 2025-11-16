# Balanced Summary

**Goals and scope**  
TACHOnet is a secure network system enabling EU Member States' Card Issuing Authorities (CIAs) to exchange tachograph card information. It facilitates administrative tasks like card status checks and declarations while preventing reconstruction of a consolidated European database. The system operates via standardized XML messaging over the TESTA-II network.

**Roles and user stories**  
- *CIA Application*: Exchange XML messages with TACHOnet to validate card data  
- *CIA Administrator*: Browse TCN usage statistics reports via a secure web interface  
- *TCN Administrator*: Monitor system performance and manage Member State configurations  
- *CIA User*: Access phonetic search and transliteration services for card issuance  
- *Enforcement Authority*: Check card status during road checks through CIA systems  

**Key processes**  
1. Trigger: Receipt of XML request → Decrypt and log message in tracking database  
2. Validate syntax and assign unique TCN reference ID  
3. Route requests to appropriate Member States based on issuing codes  
4. Broadcast requests to all Member States when no issuing code specified  
5. Collect and validate responses within configured timeout period  
6. Build consolidated response from all received replies  
7. Encrypt and send final response to original requester  

**Domain data elements**  
- *Transaction*: TCNRefId (PK), MessageType, StatusCode, Timestamp, SenderCIA  
- *Member State*: CountryCode (PK), CIAContact, DigitalCertificate, ServiceURL  
- *Card*: CardNumber (PK), IssuingMS, Status, DriverName, ExpiryDate  
- *Statistics*: ReportId (PK), Period, TransactionCount, ResponseTimes, ErrorRates  

**Non-functional requirements**  
- High availability (24x7 operation) with <1 minute response time  
- Secure messaging with non-repudiation and data encryption  
- Maintainability and extensibility for future message types  
- Robust error handling and automatic retry mechanisms  
- Compatibility with diverse Member State technical environments  
- Support for international character sets and transliteration  

**Milestones and external dependencies**  
- Integration with TESTA-II network infrastructure  
- Member State CIA system readiness for XML messaging  
- Digital certificate deployment for all participating CIAs  
- BizTalk Server 2002 configuration completion  
- SQL Reporting Services implementation for statistics  

**Risks and mitigation strategies**  
- Network failures: Implement automatic retry logic with 3 attempts  
- Late responses: Configure timeout handling and status reporting  
- Invalid messages: Deploy syntax validation with error feedback  
- Security breaches: Use encryption and digital certificates  
- Performance degradation: Monitor via Microsoft Operations Manager  

**Undecided issues**  
- Archive duration for message tracking data  
- Additional transliteration standards beyond Greek/Latin  
- Firewall configuration for central monitoring  
- Specific BizTalk monitoring rules for MOM  
- Member State removal procedures  
- Not mentioned