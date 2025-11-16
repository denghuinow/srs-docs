# Software Requirements Specification for KeePass Password Safe

## 1. Introduction

### 1.1 Purpose
This document includes software requirements for KeePass Password Safe, release number 1.10. KeePass Password Safe is an OSI Certified Open Source Software distributed under the terms of the GNU General Public License Version 2 or later. The system solves the password memorization problem by keeping all user passwords, data, email accounts, usernames and URLs stored in a secure, encrypted database protected by a Master Password. The system is small and portable, providing several functionalities on encrypted data.

### 1.2 Document Conventions
All requirements have the same priority. The document presents an overall view of KeePass followed by detailed analysis of features and functions.

### 1.3 Intended Audience and Reading Suggestions
This document is intended for developers, testers, users, documentation writers, advanced end users, end users/desktop, and system administrators.

### 1.4 Project Scope
KeePass Password Safe is a small, portable system that solves the problem of memorizing multiple passwords by providing a secure, encrypted database where users can store passwords, usernames, email accounts, URLs, and notes protected by a Master Password and/or key file. There is no recovery password or back door if the Master Password/key file is lost. KeePass also provides functionalities to keep the database organized and up to date.

### 1.5 References
- http://sourceforge.net/projects/keepass/
- http://keepass.info/

## 2. Overall Description

### 2.1 Product Perspective
KeePass consists of a database containing data for one or more users. Each user's data are divided into groups and subgroups. Every user has a unique Master Key which can be simple or composite that uniquely opens the database. Groups and subgroups contain entries with usernames, passwords, URLs, etc. that can be sent or copied to websites, applications, and accounts. There is also the ability for one-time key creation for single-use transactions.

### 2.2 Product Features
- Database: New, Open, Close, Save, Print, Search, Import, Export
- Group/Subgroup: Add, Modify, Delete, Find
- Entry: Add, View/Edit, Duplicate, Delete
- Change Language
- Auto-Type
- Command Line Options
- Composite Master Key
- Configuration
- Import/Export
- Integration
- Password Generator
- Secure Edit Controls
- TAN Support
- URL Field
- Using Stored Passwords
- Lock Workspace

### 2.3 User Classes and Characteristics
- Advanced end users: familiar with programming and can personalize their database
- End users/Desktop: users with no particular knowledge of computer programming
- System administrators: administrators working on computers supporting lots of accounts and personal data
- Science/Research Telecommunications: for organizing data related to many people and applications
- Industry: for one-time passwords for testing controls or expired entries

### 2.4 Operating Environment
KeePass should run on Operating Systems: WINE, 32-bit MS Windows (95/98), 32-bit MS Windows (NT/2000/XP), All 32-bit MS Windows (95/98/NT/2000/XP), Win2K, WinXP, Microsoft Windows Server 2003. User interfaces used are: NET/Mono, Win32 (MS Windows).

### 2.5 Design and Implementation Constraints
Timing requirements: When a password is copied, it remains in memory for only 10 seconds for security.

Language Requirements: Not all translations have translated help files and tutorials available.

Specific Technologies:
- Advanced Encryption Standard (AES/Rijndael) or Twofish algorithms (128-bit block size, 256-bit key size)
- Secure Hash Algorithm SHA-256 for key creation
- Pseudo-random sources for Initialization Vector, master key salt, etc.
- ARC4 encryption algorithm for passwords stored in process memory

### 2.6 User Documentation
- Compiled HTML Help file with tutorial and full help on all features
- KeePass Internet shortcut to official website for downloads, translations, plug-ins, and extensions

## 3. System Features

### 3.1 New Database
Allows creation of a new database with Master Password and/or Key File determination.

Functional Requirements:
- REQ-1: KeePass must be downloaded and installed
- REQ-2: Master Password has no limits in length

### 3.2 Open Database
Allows the user to open an existing database by navigating to it and entering the Master Password.

Functional Requirements:
- REQ-3: Folder selected must be of type the database can read (".kdb" extension)

### 3.3 Save Database
Allows the user to save any changes or updates to the database.

Functional Requirements:
- REQ-4: Databases must have different names or else the previous one will be replaced

### 3.4 Print Database
Allows user to print selected data from the database including backup entries, password groups, group tree, title, username, password, URL, notes, creation time, last access, last modification, expires, icon, UUID, and attachment.

Functional Requirements:
- REQ-5: There must be entries in the database in order to print them

### 3.5 Search Database
Allows user to search for keywords in the database for usernames, groups, passwords, URLs, notes, and titles.

Functional Requirements:
- REQ-6: All data related to the search word must be shown

### 3.6 Add Group/Subgroup
Used to organize data into categories for easier access. User can create new groups or subgroups with names and optional images.

Functional Requirements:
- REQ-7: A name is required for new group/subgroup creation
- REQ-8: A subgroup cannot be created when no group is selected

### 3.7 Modify Group/Subgroup
Allows user to change the name of an existing group or subgroup.

Functional Requirements:
- REQ-9: A name is required for the group/subgroup to be renamed

### 3.8 Delete Group/Subgroup
Allows the user to delete an existing group/subgroup after confirmation.

### 3.9 Find Group/Subgroup
Allows user to find data within a specific group/subgroup by searching for title, username, password, URL, notes, or group name.

Functional Requirements:
- REQ-10: A word must be placed in the find field to search within a group

### 3.10 Add Entry
Adds a new entry to the database with fields for group, title, username, password, URL, notes, expiration date, and attachment file. Not all fields are required.

Functional Requirements:
- REQ-11: An entry must belong to a group to be created
- REQ-12: When the password field is completed, the repeat password field must also be completed
- REQ-13: Password field and repeat password field must be identical

### 3.11 View/Edit Entry
Allows the user to change or modify an existing entry's fields.

Functional Requirements:
- REQ-14: An entry must be selected to be viewed or modified
- REQ-15: When the password field is changed, the repeat password field must also be changed and identical

### 3.12 Duplicate Entry
Creates an exact copy of the selected entry in the same group.

Functional Requirements:
- REQ-16: An entry must be selected before it is duplicated

### 3.13 Delete Entry
Allows the user to delete an existing entry after confirmation.

Functional Requirements:
- REQ-17: An entry must be selected to be deleted

### 3.14 Change Language
Allows user to choose from available language translations.

Functional Requirements:
- REQ-18: An internet connection and browser are required to download new language translations

### 3.15 Auto-Type
Allows user to define a sequence of keypresses which KeePass will automatically perform.

Functional Requirements:
- REQ-19: The prefix "Auto-Type:" is required in front of each sequence
- REQ-20: Sequence's length must not exceed one line (59 characters)
- REQ-21: If two auto-types are referred in one note field, only the first is used

### 3.16 Command Line Options
Allows user to pass a file path in the command line so KeePass will open it immediately after startup.

Functional Requirements:
- REQ-22: Only one database file is allowed in command line options
- REQ-23: In case a space is found in the path, it must be enclosed in quotes

### 3.17 Composite Master Key
A composition of master password and key files where all components are required to unlock the database.

Functional Requirements:
- REQ-24: If a master password is required, the database doesn't open unless the password is entered
- REQ-25: If a key file is required, the database doesn't open unless the key file is present
- REQ-26: If there is a composite key, both master password and key file are required
- REQ-27: In case of lost master password or key file, the database never unlocks again (no recovery)
- REQ-28: There is no backdoor or key that unlocks all databases

### 3.18 Import/Export
Gives the ability to import/export files from/to database from CSV files, Code Wallet, Password Safe, and Personal Vault.

Functional Requirements:
- REQ-29: File formats are not specialized password database formats
- REQ-30: File formats only specify a low-level layout of stored data

### 3.19 Integration
Allows switching back from an application to KeePass using global hot key (Ctrl+Alt+K).

Functional Requirements:
- REQ-31: Global hot key cannot be changed

### 3.20 Password Generator
Generates random passwords when creating entries, based on character sets, patterns, or rules.

### 3.21 TAN Support
Allows creation of Transaction Authentication Numbers for additional security.

Functional Requirements:
- REQ-32: Title, username, or URL cannot be changed in a TAN entry
- REQ-33: When a TAN is used, it expires automatically and can never be used again

## 4. External Interface Requirements

### 4.1 User Interfaces
User interface includes various forms and windows with main database window containing menu bar (File, Edit, View, Tools, Help), toolbar with shortcuts, and side bar for groups/subgroups. Active windows performing actions make the main database window inactive until closed.

### 4.2 Communications Interfaces
Internet connection and browser are required for downloading plug-ins.

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements
When a password is copied, it remains in memory for only 10 seconds for security purposes.

### 5.2 Safety Requirements
When a USB containing the database is removed while changes haven't been completely saved, the database may be damaged. Repair functionality can help from Tools menu, but won't help if Master Password is forgotten/lost or if database header is corrupted. Regular backups are recommended.

### 5.3 Software Quality Attributes
- Small and light project that doesn't need installation (unpacking from Zip package)
- Leaves no trace behind when uninstalled
- Developed under GNU General Public License version 2 or later
- Available for free download from SourceForge and official website
