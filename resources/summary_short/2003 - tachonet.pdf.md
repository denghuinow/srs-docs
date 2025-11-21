# Short Summary

- **Background and objectives**: TACHOnet is a system designed to facilitate secure communication and administrative tasks between EU Member States' Card Issuing Authorities (CIAs) for driver tachograph card management, ensuring data privacy and preventing consolidated European database reconstruction.

- **In scope**:
  - Check driver(s)' issued cards and tachograph card status.
  - Declaration of card status modifications (e.g., lost, stolen).
  - Send card/driving license assignment notifications.
  - Generate and browse usage statistics for monitoring.
  - Manage Member State configurations and user access.

- **Out of scope**:
  - Reconstruction of a consolidated European database.
  - Management of individual CIA users (handled by Member States).
  - Research and development of new algorithms.
  - Direct management of Member States' internal data organization.
  - Support for non-TESTA-II network infrastructures.

- **Roles and core use cases**:
  - As a CIA Application, I want to exchange XML messages with TACHOnet so that administrative tasks like card checks and status updates are processed.
  - As a CIA Administrator, I want to browse TACHOnet usage statistics so that I can monitor system performance and transaction statuses.
  - As a TCN Administrator, I want to manage Member State configurations and monitor system health so that TACHOnet operates reliably and securely.

- **Success metrics**:
  - System availability 24x7 with response times under 1 minute for enforcement requests.
  - High reliability with minimal interruptions and stable, reproducible results.
  - Effective non-repudiation and data privacy in all transactions.

- **Major constraints**:
  - Must use TESTA-II network facilities and comply with predefined XML message formats.
  - No ability to reconstruct a consolidated European database.
  - Must support existing techniques and commercially available software.
  - Design must ensure long operational lifetime and migration capability.
  - Member States manage their own internal user and data organization.

- **Undecided issues**:
  - Duration for message tracking retention.
  - Specific BizTalk monitoring rules configuration for MOM.
  - Firewall configuration between TACHOnet servers and central MOM console.
  - Handling of late or multiple responses from Member State CIAs.
  - Not mentioned.