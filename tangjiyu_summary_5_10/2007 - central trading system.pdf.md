# Central Trading System - Software Requirements Specification

## 1. Introduction

### 1.1 Goals and Objectives
The Central Trading System (CTS) is a subsystem of the Stock Trading System (STS) designed to complete stock trading operations. The system analyzes incoming instructions, categorizes them, and matches them according to specific rules. CTS also provides interfaces for sending messages to other modules.

### 1.2 System Context
CTS is one of six subsystems in the STS, including:
- Stock account operation
- Financing account operation
- Trade client serve
- Network message promulgating
- Central trading system
- Trading system manage

The CTS receives instructions from the trade client serve, processes them, and generates messages for the network message promulgating module. The trading system management module is authorized to access CTS information.

### 1.3 Potential Users' Specification
There are two main types of users:
1. Terminal users who perform simplified operations through mouse clicks and keyboard input
2. System maintainers who must be familiar with Java programming and socket communication to troubleshoot issues and modify the program when needed

Due to frequent instruction operations (fetch, process, cancel), the system experiences heavy transfer loads, requiring maintainers to have strategies for handling system crashes when overhead exceeds capacity.

## 2. User Scenarios

### 2.1 User Profiles
Five main actors interact with the Central Trading System:
- Transaction User Interface
- Security Account Management
- Trading Management System
- Trading Information Release

### 2.2 User Scenarios Specification

#### Buy Stock Use-Case
- **Primary Actor**: Transaction User Interface
- **Goal**: Fulfill buy transactions
- **Preconditions**: Customer successfully logged in and submitted buy information
- **Trigger**: 'Buy' button clicked on UI
- **Scenario**:
  1. Transaction user interface submits buy instruction
  2. CTS saves the buy instruction
  3. CTS matches instructions with same stock ID
  4. CTS executes trade by matching
  5. CTS modifies information of matched instructions
- **Priority**: Essential, must be implemented in first increment
- **Frequency**: Frequent

#### Sell Stock Use-Case
- **Primary Actor**: Transaction User Interface
- **Goal**: Fulfill sell transactions
- **Preconditions**: Customer successfully logged in and submitted sell information
- **Trigger**: 'Sell' button clicked on UI
- **Scenario**:
  1. Transaction user interface submits sell instruction
  2. CTS saves the sell instruction
  3. CTS matches instructions with same stock ID
  4. CTS executes trade by matching
  5. CTS modifies information of matched instructions
- **Priority**: Essential, must be implemented in first increment
- **Frequency**: Frequent

#### Cancel Trading Instruction Use-Case
- **Primary Actor**: Transaction User Interface
- **Goal**: Fulfill cancel transactions
- **Preconditions**: Customer successfully logged in and submitted cancel information
- **Trigger**: 'Cancel' button clicked on UI
- **Scenario**:
  1. Transaction user interface submits cancel instruction
  2. CTS saves the cancel instruction
  3. CTS cancels the correlative instruction
- **Priority**: Moderate, to be implemented after basic functions
- **Frequency**: Many times per day

#### Save Trade Information Use-Case
- **Primary Actor**: Security Account Management
- **Goal**: Save all successful trade information
- **Preconditions**: Correlative trade transactions successfully conducted
- **Trigger**: Any trade transaction conducted
- **Scenario**:
  1. CTS outputs successful trade information
  2. Security account management saves trade information
- **Priority**: Essential, must be implemented in first increment
- **Frequency**: Frequent

#### Query Trade Information Use-Case
- **Primary Actor**: Trading Information Release
- **Goal**: Query trading information for statistical analysis and web release
- **Preconditions**: CTS handles transactions properly
- **Trigger**: Trading Information Release System sends query
- **Scenario**:
  1. Trading information release system sends query
  2. CTS implements the query
  3. CTS structures the queried data
  4. CTS sends data to release system
- **Priority**: Essential, must be implemented in first increment
- **Frequency**: Frequent

## 3. Data Flow

### 3.1 System Architecture
The system processes instructions through two main modules:
1. **Instruction Pretreatment Module**: Judges instruction validity, freezes funds, and writes log files
2. **Instruction Manager Module**: Handles all three types of instructions and sends results to Trading Client Serve and Information Releasing Module while maintaining logs

### 3.2 Instruction Processing Flow
1. Instructions first arrive at the Instruction Pretreatment Module which validates instructions and freezes funds
2. Validated instructions proceed to the Instruction Manager Module for detailed processing
3. Three types of instructions are handled:
   - Query instructions reference the Database or instruction list
   - Cancel instructions delete instructions from the instruction list
   - Trade instructions go to the trade manager for matching in the instruction list

## 4. Data Dictionary
Key data elements include:
- User instructions from Trading Client Serve to CTS input
- Instruction results from CTS output to other subsystems
- Database instructions for query, write, and modify operations
- Newest trading results from CTS to Information Releasing Module
- Log instructions from Trading Client Serve to CTS
- Fund freezing instructions from Instruction Pretreatment to Database
- List instructions from Instruction Manager to instruction list

## 5. State Diagram
The system operates through several states: decoding, researching, canceling, analyzing, rejecting, queuing, storing, matching, queue modifying, and responding. Transitions between states follow specific conditions.

## 6. Class Responsibilities

### PretreatmentOfInstruction Class
- Determines price increments/decrements constraints
- Freezes buyer accounts
- Prededucts commission charges and taxes
- Logs instructions
- Sends instructions to ManagementOfInstruction

### ManagementOfInstruction Class
- Adds instructions
- Cancels instructions
- Searches instructions
- Sorts instructions

### ManagementOfDealing Class
- Executes trades following key rules
- Logs business results
- Stores key data to database
- Determines commission charges and taxes

### ManagementOfDatabase Class
- Provides database operation interfaces for other modules
- Supports account operations (insert, delete, update)
- Supports stock operations (insert, delete, update)

## 7. Validation Criteria

### 7.1 Interface Criteria
CTS interfaces with three modules:
1. **Transaction User Interface**: Inputs three types of instructions (buy, sell, query)
2. **Information Releasing Module**: Queries stock prices
3. **Trading Manager System**: Accesses user trading instructions

### 7.2 Function Criteria
Key system functions include:

#### Instruction Matching
- Applies price-first and time-first principles
- Matches trades when lowest buy price exceeds highest sell price

#### Rising and Falling Limits
- Rejects trading instructions exceeding price limits

#### Result Return
- Returns results to client serve for all trading instructions
- Trading states: totally finished or partially finished

#### Outdated Instructions
- Removes unfinished instructions from CTS at end of trading day
