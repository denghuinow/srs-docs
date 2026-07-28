**Purpose & Scope**
The system is the European Train Control System (ETCS), part of ERTMS. Its purpose is to provide information to the driver to allow safe train driving and to supervise train and shunting movements. It defines functional requirements for onboard and trackside equipment across different application levels. It does not define detailed technical specifications, implementation plans, or training procedures.

**Product Background / Positioning**
ETCS is a standardized train control system for European railways. It must be compatible with existing national train control systems listed in the CCS TSI without mutual interference. It is designed to operate across different national networks by receiving and adapting to national values.

**Core Functional Overview**
*   Supervise train speed and movement authorities to ensure safe operation.
*   Operate in multiple defined application levels (0, 1, 2, 3, STM) and support transitions between them.
*   Manage multiple operational states (e.g., Full Supervision, Shunting, On Sight) with defined transition rules.
*   Calculate and enforce braking curves (emergency and service) based on train data, infrastructure data, and movement authorities.
*   Provide a Driver-Machine Interface (DMI) to display supervision information, warnings, and receive driver inputs.
*   Record all relevant ETCS data, including interventions and received information.
*   Execute protection functions, including emergency stop commands and the train trip function for passing stop signals.

**Key Users & Usage Scenarios**
The primary user is the train driver. The driver interacts with the system to enter train data, acknowledge transitions and messages, and respond to warnings. The system provides different levels of supervision based on the operational state, from full automatic supervision (Full Supervision) to driver-responsible modes with speed ceilings (e.g., Shunting, On Sight).

**Major External Interfaces**
Key interfaces are track-to-train and train-to-track data transmission via balises, loops, or radio (GSM-R). The onboard system interfaces with the vehicle's braking system. It also interfaces with national systems via a Specific Transmission Module (STM). The Radio Block Centre (RBC) is a major external trackside system for levels 2 and 3.

**Key Non-functional Requirements**
*   **Performance:** Must be functional for train speeds up to 500 km/h.
*   **Safety:** Failures compromising safety shall cause an immediate brake application. The system must ensure supervision is at least as protective as the least restrictive state during transitions.
*   **Reliability/Availability:** Onboard equipment performs an automatic self-test at start-up.
*   **Maintainability:** Recorded data must be outputtable via standardized interfaces for investigation.
*   **Security:** Not explicitly defined in functional terms within this excerpt.

**Constraints, Assumptions & Dependencies**
*   Must be compatible with existing national systems as per the CCS TSI.
*   Implementation is constrained by mandatory (M) and optional (O) classification of requirements.
*   Depends on the provision of national values and infrastructure data from the trackside.
*   Assumes the availability of harmonized default values stored onboard.

**Priorities & Acceptance Approach**
Mandatory (M) requirements shall be implemented in every application. Optional (O) requirements are not mandatory but must be respected if implemented. Acceptance is based on conformity with the specified mandatory functions, performance limits, and safety reactions to failures.