# TACHOnet Software Requirements Specification

## Introduction

### Purpose
This document captures complete software requirements for the TACHOnet system. It fully describes the external behaviour of the application(s) or subsystem(s) identified. It also describes non-functional requirements, design constraints and other factors necessary to provide a complete and comprehensive description of the requirements for the software.

### References
- Specific Agreement n°36 under framework contract n° DI/02450-00 – 13-Nov-03
- TCN XML Messaging Reference Guide V1.40
- Card Issuing Working Group – General Report – URBA 2000

### Abbreviations
- CIA – Card Issuing Authority
- MS – Member State
- SPOC – Single Point Of Contact
- TCN – TACHOnet

## Chapter 1: Requirements

### Types of Requirements

A requirement is defined as "a condition or capability to which a system must conform".

Functional requirements specify actions that a system must be able to perform, without taking physical constraints into consideration. These are often best described in a use-case model and in use cases. Functional requirements thus specify the input and output behaviour of a system.

Non-functional requirements describe only attributes of the system or attributes of the system environment.

#### FURPS+ Model
- Functionality (FUN)
- Usability (USA)
- Reliability (REL)
- Performance (PER)
- Supportability (SUP)
- Design Requirements (DES)
- Interface Requirements (INT)
- Physical Requirements (HAR)

### List of Functional Requirements

| ID | Description |
|----|-------------|
| FUN-01 | The system must allow a member of the network to send requests to a particular or all the other members about possible delivery of a driver's smart card to a similar person |
| FUN-02 | The system must allow a member of the network to send a bulk request on all or a large part of its driver's smart card holders to a particular or all members of the network |
| FUN-03 | The system must allow a member to do statistics on messages issued and received from/to his system |
| FUN-04 | The system must provide automatic reply to the sender of the request through the use of a standard interface to the Members systems |
| FUN-05 | The system must track the workflow between senders and related replies |
| FUN-06 | The system must be able, in accordance with the rules on delays for each transaction, to automatically transmit alert messages to senders/replier/administrator when constraints on delay for reply are not fulfilled |
| FUN-07 | The system must allow the administrator to extract statistics of use, standard delay of reply by member/period, percentage of unsuccessful transaction |
| FUN-08 | The system must provide the management of user rights and permissions |
| FUN-09 | The system must be able to define and manage various type of messages already in the driver's smart card holder like pre-delivery check, stolen/lost cards, renewals, exchanges and duplicates |
| FUN-10 | The system must be able to include new members in the network through simple administrative tasks |
| FUN-11 | The system must be highly automatic to relieve the users of as many repetitive and tedious tasks as possible |
| FUN-12 | The system must provide at application level a full security (including non repudiation) and encryption policy compatible with the level of security required |
| FUN-13 | The system must guarantee that none of the Member of the network, including the administrator, is technically able to re-construct a consolidated European database through the use of the messages exchanged |
| FUN-14 | The system must allow a Member State (through its Card Issuing Authority) to ask for the status of card (lost, stolen) to the corresponding Card Issuing Authority of the Member State having issued the card |
| FUN-15 | The system must allow a Member State (through its Card Issuing Authority) to send card status modification requests (lost, stolen) to the corresponding Card Issuing Authority of the Member State having issued the card |
| FUN-16 | The system must allow enforcement authorities (through its Card Issuing Authority) to ask for driver's card status (based on either card number + issuing Member State code or driver's surname, first names, date of birth and issuing Member State code) to the corresponding Card Issuing Authority |
| FUN-17 | The system must allow enforcement authorities (through its Card Issuing Authority) to ask for workshop card status (based on workshop card number + issuing Member State code) to the corresponding Card Issuing Authority |

### List of Non-functional Requirements

#### Usability Requirements
| ID | Description |
|----|-------------|
| USA-01 | The system must guide users through an interface based on end user concepts |
| USA-02 | The system must be easy to learn and does not obstruct the thematic understanding of the users |
| USA-03 | The system must make it easy to correct mistakes |

#### Reliability Requirements
| ID | Description |
|----|-------------|
| REL-01 | The system is to be designed as a robust and dependable operational system which is tolerant to operator errors and which will recover cleanly from power cuts or other disasters |
| REL-02 | The system must function reliably, with few or no interruptions in its first operational year and fewer still thereafter |
| REL-03 | The system must give stable and reproducible results |

#### Performance Requirements
| ID | Description |
|----|-------------|
| PER-01 | The system should be able to cover more than one contact point per country depending on the administrative organisation adopted by each country and able to work in a multi hierarchical environment |
| PER-02 | There will be no restriction in time or place for the use of the software built from the specifications |
| PER-03 | The system must be able to establish and keep the dialog with the Members systems despite the various technical environments and technologies used on their sites |
| PER-04 | The system will be designed so that background tasks can continue while the user performs foreground tasks |
| PER-05 | The system will be used 24x7 by operators under pressure to produce results rapidly. The system must respond rapidly to user requests irrespective of any background tasks |

#### Supportability Requirements
| ID | Description |
|----|-------------|
| SUP-01 | The system should be able to support other types of message structure to cover future driving licence network and correlated activities |
| SUP-02 | The system must be maintainable and extensible |
| SUP-03 | The system must be designed so that it can migrate to upgraded hardware or new versions of the operating systems involved |
| SUP-04 | The system must be able to migrate to other type of network than the one proposed by TESTA-II |
| SUP-05 | The system must provide solutions/rules regarding data encoding problems such as supporting different character sets, name truncation rules, name matching in case of misspelling |

#### Design Requirements
| ID | Description |
|----|-------------|
| DES-01 | The system must be designed and documented with the expectation that its operational lifetime will be many years |
| DES-02 | Each Member of this network will organise its data about smart card holders with no constraints or recommendations on operating system and/or technology used. The system will be able to dialog with these environments or specify a generic interface |

#### Interface Requirements
| ID | Description |
|----|-------------|
| INT-01 | The system must use the network facilities supplied by the TESTA-II network |
| INT-02 | The algorithms in the software will be based on existing techniques and no research will be required to develop new algorithms |
| INT-03 | Most of the functionality of the new software shall depend on pre-existing or commercially available software |

## Chapter 2: Use-Case Model

### Actor Catalog
- CIA Application: Single user representing a whole Card Issuing Authority
- CIA Administrator: Single user in charge of administering the CIA application
- TCN Administrator: In charge of administering the whole TACHOnet services
- CIA User: Clerks or enforcers performing administrative tasks

### Use Case Packages

#### TCN Administrative Tasks
- Check Driver's Issued Cards
- Check Tachograph Card Status
- Declaration of Card Status Modification
- Send Card/Driving License Assignment
- Get Phonex Search Keys
- Get US/Ascii Transliteration

#### TCN Statistics Tasks
- Add a new CIA
- Reset Password
- Generate Statistics
- Browse Statistics
- Log the message

#### TCN System Tasks
- Monitor the system
- Manage Member State

### Key Use Cases Details

#### UC-01: Check Driver's Issued Cards
System processes requests for checking driver's issued cards from Card Issuing Authority. Can handle single driver (online) or multiple drivers (batch). System deciphers requests, validates syntax, assigns refid, builds new requests for each issuing Member State, sends requests, waits for responses, consolidates responses and sends back to caller.

#### UC-02: Check Tachograph Card Status
System checks status of tachograph card based on card number and issuing Member State code. System deciphers request, validates syntax, assigns refid, figures out target issuing Member State, builds and sends request, waits for response, consolidates responses and sends back to caller.

#### UC-03: Declaration of Card Status Modification
System processes requests for declaring modification of card status. System deciphers request, validates syntax, assigns refid, figures out target issuing Member State, builds and sends request, waits for response, consolidates responses and sends back to caller.

#### UC-04: Send Card/Driving License Assignment
Based on "Luxemburg agreement", used when card issued to driver with foreign driving license. System warns Member State that issued card number is associated with driving license number.

#### UC-05: Get Phonex Search Keys
System computes search keys (Phonex algorithm) for given surname and first names. Member State CIAs should call this service when issuing new card to store computed search keys in local data store.

#### UC-06: Get US/Ascii Transliteration
System provides US/Ascii transliteration (from Latin or Greek) of surname, first names, place of birth and driving license number.

#### UC-07: Add a new CIA
TCN Administrator creates new CIA Administrator account in Active Directory for access to Statistics Reporting.

#### UC-08: Reset Password
TCN Administrator resets CIA Administrator password in Active Directory.

#### UC-09: Generate Statistics
System transfers expired transactions nightly, stores them and generates usage statistics for TCN Administrator and CIA Administrators.

#### UC-10: Browse Statistics
TCN Administrator and CIA Administrators browse usage statistics reports via secure Web interface.

#### UC-11: Log the message
System logs every message sent or received. Provided out-of-the-box by BizTalk and configured at channel level.

#### UC-12: Monitor the system
System monitoring based on MOM (Microsoft Operations Manager) product with BizTalk Management Pack.

#### UC-13: Manage Member State
Managing Member State configuration (add, edit, remove). Adding involves BizTalk configuration and reporting system updates. Modifying involves updating properties or url addresses.
