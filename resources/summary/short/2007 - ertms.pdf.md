**Short Summary**

**Background and objectives**  
The ERTMS/ETCS Functional Requirements Specification (FRS) version 5.00 defines the operational requirements for the European Train Control System, aiming to provide safe train supervision and control across different application levels and national systems. Its primary objective is to ensure interoperability and safety by specifying mandatory and optional functions for onboard and trackside equipment.

**In scope**  
- Definition of ETCS application levels (0, 1, 2, 3, STM) and operational states (e.g., Full Supervision, Shunting).  
- Core functions including train data entry, speed profile calculation, movement authority supervision, and train location determination.  
- Driver-Machine Interface (DMI) requirements for displaying speed, distance, warnings, and system status.  
- Handling of failures and fall-back procedures for transmission interruptions or onboard equipment failures.  
- Compatibility with existing national train control systems via Specific Transmission Modules (STMs).

**Out of scope**  
- Detailed technical specifications (covered in the System Requirements Specification).  
- Implementation processes or specific data structures.  
- Training, environmental, and RAMS (Reliability, Availability, Maintainability, Safety) details.  
- Driver-Machine Interface design specifics.  
- Other technical functions not listed in the FRS.

**Stakeholders and core use cases**  
- **Driver**: Operates the train using ETCS information for safe movement.  
- **Railway Infrastructure Manager**: Provides trackside data and manages movement authorities.  
- **Train Operator**: Ensures train data is correctly entered and maintained.  
- **Maintenance Personnel**: Handles fault indications and system isolation.  
- **Safety Regulator**: Oversees compliance with mandatory requirements.  
- **System Integrator**: Implements ETCS functions across different levels and national systems.  

*User stories*  
1. As a driver, I want to receive clear speed and distance information on the DMI so that I can drive safely without ETCS intervention.  
2. As a driver, I want to acknowledge level transitions when requested so that I can maintain supervision without unnecessary braking.  
3. As a railway infrastructure manager, I want to send movement authorities and track data to trains so that train separation and speed limits are enforced.  
4. As a train operator, I want to enter train data before movement so that ETCS can calculate accurate braking curves.  
5. As maintenance personnel, I want fault indications to be displayed on the DMI so that I can address onboard equipment failures promptly.  
6. As a system integrator, I want ETCS to be compatible with national systems via STMs so that trains can run across different railway networks.

**Success metrics**  
- ETCS functions correctly at train speeds up to 500 km/h.  
- Onboard equipment performs automatic self-tests at startup without driver action.  
- System records all relevant data (e.g., transitions, brake interventions) for investigation and performance assessment.

**Major constraints**  
- Mandatory (M) requirements must be implemented in every ETCS application.  
- Transitions between operational states must maintain at least the same protection as the least restrictive state.  
- National values must be applicable to defined areas and stored permanently onboard.  
- Default values must be harmonized and used when national values are unavailable.  
- ETCS must not interfere with existing national systems and vice versa.

**Undecided issues**  
- Specific conditions for implementing optional (O) functions as required by safety regulations.  
- Detailed procedures for handling certain transmission failure reactions (options 1–3 in section 5.1.3).  
- Exact retention periods for recorded data beyond the specified minimums (24 hours for accidents, one week for operational data).  
- Prioritization of multiple application levels on a line when more than one is implemented.  
- Language support for non-predefined texts sent from trackside.