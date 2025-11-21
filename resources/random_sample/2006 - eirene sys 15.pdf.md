# Balanced Summary

**Goals and Scope**  
The EIRENE system defines a GSM-based digital radio standard for European railways to ensure interoperability and support mobile communications for ground-train voice/data and ground-based personnel. It aims to provide consistent services across national borders while allowing manufacturing economies of scale.

**Roles and User Stories**  
- *As a train driver, I want to initiate emergency calls so that I can quickly alert controllers during critical situations.*  
- *As a shunting team member, I want to join dedicated group calls so that I can coordinate movements safely.*  
- *As a controller, I want to terminate group calls using DTMF signals so that I can manage communications efficiently.*  
- *As maintenance staff, I want to register my functional number so that I can be reached by role rather than device.*  
- *As a general user, I want to send/receive SMS so that I can exchange text messages for operational support.*

**Key Processes**  
1. *Trigger: Mobile power-on* → Mobile performs self-test and registers with the network.  
2. *Trigger: User action* → Functional number registration/deregistration via USSD messages.  
3. *Trigger: Emergency button press* → Railway emergency call initiated as VGCS with high priority.  
4. *Trigger: Call receipt* → Arbitration rules applied to manage concurrent calls based on priority.  
5. *Trigger: Call termination* → Confirmation messages sent for high-priority calls using UUS1.  
6. *Trigger: Shunting mode activation* → Mobile joins common shunting group and transitions to dedicated groups.  
7. *Trigger: Network failure* → Direct mode enables local communications without infrastructure.

**Domain Data Elements**  
- *Mobile Station (MS)*: Primary Key: IMSI; Fields: MSISDN, Functional Number, Power Class, Network List.  
- *Train*: Primary Key: Train Number; Fields: Journey ID, Functional Codes, Controller Associations.  
- *Shunting Group*: Primary Key: Group ID; Fields: Area ID, Member Roles, Emergency Status.  
- *Controller*: Primary Key: Location Number; Fields: Controller Type, Priority Level, Cell Association.  
- *Call Record*: Primary Key: Call ID; Fields: Caller FN, Callee FN, Priority, Timestamp, Confirmation Status.  
- *Network Configuration*: Primary Key: Cell ID; Fields: Service Area, Frequency Band, Coverage Level.

**Non-Functional Requirements**  
- Coverage probability of 95% at specified field strengths for voice and safety-critical data.  
- Handover success rate of at least 99.5% under design load conditions.  
- Call setup times compliant with eMLPP priority levels, with authentication enabled.  
- Equipment operation in temperatures from -20°C to +55°C and storage down to -40°C.  
- EMC immunity per railway standards, with emissions limited to GSM transmission bands.  
- Battery life supporting 8 hours of mixed usage for handheld units.

**Milestones and External Dependencies**  
- Approval by GSM-R Operators, Functional, and Industry Groups (May 2006).  
- Implementation of ERTMS/ETCS interfaces using EURORADIO FFFIS.  
- Allocation of frequency bands (876–880 MHz / 921–925 MHz) by national regulators.  
- Integration with national public numbering plans for MSISDN and functional numbers.  
- Development of bilateral agreements for service areas in network boundary regions.

**Risks and Mitigation Strategies**  
- *Risk: Loss of functional number correlation* → Mitigation: Implement recovery mechanisms and prevent unverified number use.  
- *Risk: Network congestion during emergencies* → Mitigation: Use random offsets for confirmation messages and apply eMLPP pre-emption.  
- *Risk: Interference with legacy systems* → Mitigation: Adhere to EMC standards and validate coexistence during trials.  
- *Risk: Roaming authentication failures* → Mitigation: Ensure mobiles support all required algorithms and international subscriptions.  
- *Risk: Direct mode disrupting GSM-R* → Mitigation: Prevent direct mode access when GSM services are available.

**Undecided Issues**  
- Final validation of ETCS coverage levels and speed limitations after initial implementations.  
- National protocols for re-establishing contact via GSM-R if direct mode is disrupted.  
- Specific time-out intervals for deregistration of on-train functional numbers.  
- Use of alphanumeric train numbers and their translation methods.  
- Implementation of automatic network selection versus manual/directed methods.  
- Not mentioned: Resolution of potential numbering conflicts for trains with similar IDs.