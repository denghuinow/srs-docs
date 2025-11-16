# Standard Co-Emulation Modeling Interface (SCE-MI) Requirements Specification

## 1. Introduction

### 1.1 Purpose
This document describes a proposal for a standard C/C++ modeling interface for emulators and other verification platforms. The interface provides multiple communication channels between software models running on a host workstation and a device under test (DUT) represented as a structural hardware netlist running on a verification platform such as an emulator.

### 1.2 Scope
This document describes the Standard Co-Emulation API: Modeling Interface (SCE-MI) - a multichannel communication interface that addresses verification challenges for SoC design teams. The interface provides multiple channels of communication that allow software models describing system behavior to connect to structural models describing implementation of a device under test (DUT).

## 2. Overall Description and Use Model

### 2.1 High Level Description
The SCE-MI provides a transport infrastructure between the emulator and host workstation sides, interconnecting transactor models in the emulator to C (untimed or RTL) models on the workstation. Each message channel has two ends - the end on the software side is called a message port proxy (C++ object), and the end on the hardware side is a message port macro instantiated inside a transactor.

### 2.2 Users of the Interface
Three target audiences:
- End user: Bridges software testbench with hardware DUT
- Transactor implementor: Provides plug-and-play transactor models
- SCE-MI infrastructure implementor: Furnishes working implementation of SCE-MI

### 2.3 Bridging Levels of Modeling Abstraction
- Untimed Software Level: Testbench consisting of models that stimulate and respond to DUT at different interface points
- Cycle Accurate Hardware Level: RTL-represented DUT verified on high speed emulation platform
- Messages and Transactions: Unit of data of arbitrary size and abstraction transported over channels

### 2.4 Work Flow
1. Software model compilation
2. Infrastructure linkage
3. Hardware model elaboration
4. Software model construction and binding

### 2.5 SCE-MI Interface Components

#### 2.5.1 Hardware Side Interface Components
Four macros:
- SceMiMessageInPort macro
- SceMiMessageOutPort macro
- SceMiClockControl macro
- SceMiClockPort macro

#### 2.5.2 Software Side Interface Components
C++ objects and methods providing:
- Version discovery
- Parameter access
- Initialization and shutdown
- Message port proxy binding and callback registration
- Infrastructure service loop polling function
- Message input/output handling
- Error handling

## 3. User's Guide and Tutorial

### 3.1 Hardware Side Interfacing
Four macros characterize the hardware side interface:
- SceMiMessageInPort: Messages arriving from software side to transactor
- SceMiMessageOutPort: Transactors send messages to software side
- SceMiClockControl: Clock control for transactors
- SceMiClockPort: Controlled clock and reset generator to DUT

### 3.2 The Routed Tutorial
Example design simulating air passengers traveling between locations through interconnected pipes and hubs. Demonstrates multi-threaded SystemC environment use model.

## 4. Formal Functional Specification

### 4.1 Hardware Side Interface Macros

#### 4.1.1 Dual Ready Protocol
PCI-like dual ready protocol for message port macros with TransmitReady and ReceiveReady signals.

#### 4.1.2 SceMiMessageInPort Macro
Presents messages from software side to transactor with dual-ready handshake and data bus.

#### 4.1.3 SceMiMessageOutPort Macro
Allows transactors to send messages to software side with dual ready handshake.

#### 4.1.4 SceMiClockPort Macro
Supplies controlled clock to DUT with configurable frequency, phase shift, and duty cycle.

#### 4.1.5 SceMiClockControl Macro
Provides means for transactor to control DUT clock and indicates uclock cycles when controlled clock has edges.

### 4.2 Infrastructure Linkage
Process that analyzes user's bridge netlist and compiles it into form suitable for emulator, expanding interface macros into infrastructure components.

### 4.3 Software Side Interface - C++ API

#### 4.3.1 Primitive Data Types
- typedef unsigned int SceMiU32;
- typedef unsigned long long SceMiU64;

#### 4.3.2 Error Handling
Flexible error handling with traditional status checking or callback-based scheme using SceMiEC structure.

#### 4.3.3 SceMi Class
Singleton object representing software side of SCE-MI infrastructure with methods for:
- Version discovery
- Initialization
- Shutdown
- Message port proxy binding
- Service loop processing

#### 4.3.4 SceMiParameters Class
Generic API for accessing interface parameter set organized as database of attributed objects.

#### 4.3.5 SceMiMessageData Class
Represents vector of message data transferred between software and hardware sides.

#### 4.3.6 SceMiMessageInPortProxy Class
Proxy interface to transactor message input port for sending messages.

#### 4.3.7 SceMiMessageOutPortProxy Class
Proxy interface to transactor message output port for receiving messages via callbacks.

### 4.4 Software Side Interface - C API
ANSI standard C API providing equivalent functionality to C++ API with functions wrapping C++ methods.
