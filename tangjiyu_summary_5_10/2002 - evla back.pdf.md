# EVLA Correlator Backend System Requirements Specification

## 1. Introduction

### 1.1 Purpose
This document provides a complete and accurate list of requirements for the EVLA Correlator Backend System. It serves as a binding contract between developers and users and provides a common point of reference for system expectations.

### 1.2 Scope
The Correlator Backend System lies between the Correlator and the End-to-End Systems. It is the primary component of the real-time astronomical data processing capability (the processing pipeline) of the EVLA. Its primary responsibilities are:
- Receive data from the Correlator in real-time
- Assemble time-series from the Correlator lag output
- Perform Fourier Transforms of the assembled time series
- Perform a limited number of additional processes upon user request
- Deliver suitably formatted results to the End-to-End System

## 2. Overall Description

### 2.1 Product Perspective
The EVLA Correlator Backend System is designed as a real-time data processing system implemented on a distributed memory cluster of connected processors. All computers in the system are identical and communicate over a network. Data input from the Correlator and output to the End-to-End System occur over very high-speed networks.

### 2.2 Product Functionality

#### 2.2.1 Data Input
- Receive Correlator lag data directly from Correlator Baseline Boards in the form of Lag Frames
- Receive auxiliary data and meta-data via the Monitor and Control System
- Receive status requests and control commands via the M&C System

#### 2.2.2 Data Processing
- Assemble lag frames into time series and normalize
- Apply time stamp adjustments when necessary
- Perform Fourier Transforms and other user selectable time and/or frequency domain processes

#### 2.2.3 Data Output
- Transfer formatted spectra to the End-to-End System with all pertinent meta-data
- Produce error, warning, status and other reports transferred to the M&C for final disposition

#### 2.2.4 Monitoring
- Conduct self-monitoring activities on application and system software as well as hardware systems
- Detect system failure and out of spec conditions

#### 2.2.5 Recovery
- Attempt recovery from failure and out of spec performance conditions

#### 2.2.6 Control
- Provide control and auxiliary parameters to input, output, processing, monitor, recovery, and other functions
- Communicate with the external Monitor and Control System

### 2.3 User Characteristics
All use of the Correlator Backend System is indirect via the Monitor and Control System. The BE system does not directly produce any user interface screens.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 Correlator to Backend Interface
- Receive LTA or Speed Dump Lag Frames from the Correlator
- Transfer data so all needed to perform any Fourier Transform shows up on a single processor

#### 3.1.2 Backend to/from Monitor and Control Interface
- Receive State Count data produced by the Correlator
- Receive data and parameters specific to the current EVLA Observational Mode
- Receive all meta-data necessary to format BE results for delivery to the E2E
- Provide operational status data to and receive control data from the M&C System
- Provide error and warning reports to M&C as operating conditions warrant
- Provide optionally selectable levels of printed messages detailing operational parameters

#### 3.1.3 Backend to e2e Interface
- Deliver formatted final results to the e2e System in a form compatible with AIPS++ Measurement Sets

### 3.2 Functional Requirements

#### 3.2.1 Information and Data Flows
- Acknowledge receipt of all data received from M&C
- Notify M&C of any detected interruptions of data delivery from the Correlator
- Verify successful delivery of output to the e2e
- Guarantee safe delivery of all internal messages
- Handle lag frames of less than 128 values
- Handle lag sets up to a maximum size of 262,144 values

#### 3.2.2 Process Descriptions
- Receive incoming data packets from the Correlator to Backend network interface
- Verify successful receipt of incoming data from the Correlator
- Store input data records in a memory buffer and track buffer locations
- Respond to incoming correlator mode changes and user optional processing sequence/parameter changes
- Assemble received input data into continuous time series (lag sets)
- Ensure time series data is correctly ordered and contains valid data values
- Replace invalid data with zero values and keep track of data invalids
- Apply normalizations based on reported data invalid counts
- Apply corrections based on state count and/or quantizer power measurement data (VanVleck correction)
- Make time stamp adjustments as required by the observational mode
- Perform windowing operations prior and subsequent to Fourier Transform
- Apply user selected time domain processes that are chainable and repeatable
- Perform Fourier Transform the lag set time series using power-of-two complex-to-complex Fast Fourier Transform
- Apply user selected frequency domain processes that are chainable and repeatable
- Sum the frequency domain, spectral results with integration controlled by observational mode parameter
- Combine finished spectra with meta- and auxiliary data to form suitably formatted output data sets
- Store formatted output data records in a memory buffer with backup disk buffering
- Send output data to the e2e System and verify successful receipt
- Monitor data transfer rates from the Correlator and to the e2e
- Monitor overall data processing rate
- Trap, flag and repair inf's, NaN's, underflows, overflows and other computation errors
- Periodically check PID's and assure all started tasks are alive and running
- Periodically check Backend physical processors and assure all needed processors are alive and responding
- Periodically check all Backend internal networks and assure all communication connections are intact
- Initiate processing tasks, signal kills, alter priorities, and reboot processors/networks
- Redistribute internal workload among its processors
- Ensure all processes are reversible with raw unconverted input always recoverable from the output

#### 3.2.3 Data Construct Specifications
- Input Data Queue: memory buffer of lag frames with data entry status queue
- Output Data Queue: memory buffer plus backup disk storage of processed spectra
- Processing Parameters: names, positions, and adjustable parameters for all processing pipeline applications
- Processing flags: table of flags needed to identify various internal conditions
- Metadata: all internally and externally generated data about processed time series and spectra
- Error/Warning/Failure/Recovery/Status Reports with appropriate data elements

### 3.3 Performance Requirements

#### 3.3.1 General
- Maintain input data fidelity and dynamic range across all processing functions
- Flag and mark corrupted data segments and proceed without interruption

#### 3.3.2 Hardware
- Accept an aggregate data input stream from the Correlator of minimum 1.6 Gbytes/sec
- Deliver an output data stream to the e2e System of minimum 25 MBytes/sec
- Have sufficient processor capability to accomplish all processing tasks
- Have sufficient memory with sufficient access speeds to accomplish all processing tasks
- Have sufficient storage with sufficient access speeds to meet short duration Correlator bursting demands

#### 3.3.3 Software
- Math/science application software takes optimal advantage of all computational features
- Management software functions take optimal advantage of all features to reduce overheads
- Input and output operations take optimal advantage of all system resources to reduce overhead and latency
- All data processing functions are chainable and repeatable in the processing pipeline
- Operating system, message passing and other middle-ware follow industry standards

### 3.4 Reliability/Availability
- Self-monitoring with capability to detect, report on and automatically remedy abnormal conditions
- Software part performs without total system restart between array maintenance windows
- Hardware part performs indefinitely without complete loss of service
- Respond in a loss-less manner to I/O and processing changes from Correlator mode changes
- Continue to operate in a loss-less manner during temporary loss of e2e System
- Complete processing of all onboard data and maintain availability for immediate resumption after Correlator access restoration
- Continue to operate during absence of M&C System until first encounter of unavailable critical auxiliary data
- Sit at idle and resume operations with minimal delay

### 3.5 Serviceability
- All system processing and interconnect hardware readily accessible for maintenance
- All systems and application source code available
- All software application modules debuggable
- All software processes killable, restartable, debuggable and testable without affecting normal operations

### 3.6 Maintainability
- Software tools with complete diagnostic package and customer support
- Operating system software with source code available or sufficient diagnostics and customer support

### 3.7 Scalability
- I/O, communications, and processing hardware easily expandable and reconfigureable
- Accomplished in manner transparent to processing, communications and I/O software functions
- Accomplished in a manner seamless to hardware modules or software functionality at interfaces
- Ultimately scaleable to handle up to two Gbytes per second per Correlator output channel in real-time

### 3.8 Security
- Robust security mechanism restricting access to authorized users
- All users uniquely identified via username and associated password scheme
- All login attempts done in secure manner
- System administrator with unrestricted access
- Each user has system access properties defining privileges
- Administrator can create, remove, edit users and block access

### 3.9 Installation and Upgrades
- Continue operations during partial shutdowns for maintenance
- Handle non-real-time operations in transparent fashion
- Employ modular design principles with maximal use of "hot-swappable" devices

### 3.10 Documentation
- Complete and comprehensible hardware systems specifications available
- Well documented software system and application code in familiar language
- Code written in readable style with minimal confusion
