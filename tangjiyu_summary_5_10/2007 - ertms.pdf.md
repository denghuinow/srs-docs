# ERTMS/ETCS Functional Requirements Specification

## 1. Introduction
This document defines the functional requirements for ERTMS/ETCS (EUROPEAN RAIL TRAFFIC MANAGEMENT SYSTEM / EUROPEAN TRAIN CONTROL SYSTEM). The system is required to be functional to a maximum train speed of 500 km/h.

## 2. General Requirements

### 2.1 Basic Functioning
- ETCS shall provide the driver with information to allow him to drive the train safely
- ETCS shall be able to supervise train and shunting movements
- If supervision is performed by a RBC it shall be possible to prevent movements of a traction unit in its area if not authorised by the RBC

### 2.2 Application Levels
Four ETCS application levels are defined:
- Level 0: ETCS active for limited train control function; trackside not fitted with any train control system or fitted with a train control system for which no STM is available onboard
- Level 1: Basic track to train information via intermittent transmission media (e.g. balises), supported by infill via balise, loop or radio
- Level 2: Basic track to train and train to track information via continuous transmission media (radio), with train detection provided by trackside
- Level 3: Same as level 2 except that train integrity is provided by onboard and therefore trackside train detection is optional
- Level STM: Track to train information provided by national system, with onboard functions provided by national system (STM) in cooperation with onboard ETCS

Trains equipped for higher levels shall be able to run on lines equipped with lower levels. The current application level shall be indicated on the DMI. Driver shall acknowledge level transitions when requested from trackside.

### 2.3 Operation with Existing National Train Control Systems
ETCS shall be compatible with existing national systems listed in the CCS TSI such that it does not interfere with the national systems and is not interfered with by the national systems.

### 2.4 Operational States
ETCS trainborne equipment shall supervise the following operational states:
1. Full Supervision operation
2. Partial Supervision operation (Staff Responsible, On Sight, Unfitted Line, Train Trip, Post Trip)
3. National operation (STM)
4. Tandem operation
5. Multiple operation
6. Shunting operation
7. Stand By operation
8. Reversing operation

Transitions occurring while the train is moving shall occur automatically. Transitions while stationary shall be initiated automatically or manually. The current operational status shall be indicated to the driver on the DMI.

### 2.5 National Values
ETCS on-board shall be capable of receiving National values from the trackside to adapt to National requirements. These values shall be applicable to a defined area and remain valid even if the onboard equipment is switched off. Default harmonised values shall be permanently stored in all ETCS on board equipment.

## 3. Functions

### 3.1 Operational Functions

#### 3.1.1 On Board Equipment Self Test
At Start Up, the on board equipment shall perform an automatic self-test requiring no action on the part of the driver. The DMI shall indicate the result of the self-test.

#### 3.1.2 Train and Driver Data Entry
Train data shall be entered before the on-board ETCS equipment allows train movement, only when stationary. The driver shall be able to select Train Data Entry on the DMI. Train data may be entered automatically from a railway management system or from train memory. The driver shall be able to consult train data when the train is stationary or moving. Stored train data shall be offered to the driver to be confirmed when Data Entry starts. The system shall provide for the input of other data required by STMs connected to ETCS.

Data to be entered includes:
- Driver identification
- Train identification (train number)
- STM ready for use
- Data required for brake calculation
- Maximum train speed
- Train length
- Status of air tight system
- Type of electric power accepted
- Data additional required for STM (if any)
- International train category
- Train gauge
- Maximum axle load of the train

#### 3.1.3 Shunting Operation
An ETCS equipped traction unit shall be capable of being moved in Shunting without train data, track data or movement authority. Transfer to Shunting on driver's selection shall only be possible when stationary, with permission from the RBC if the train is operating under RBC control. Automatic transfer to Shunting may occur at speeds lower than or equal to the supervised shunting speed. ETCS shall supervise Shunting operation to a permitted national speed value. Exit from Shunting shall only be possible when the train is stationary.

#### 3.1.4 Partial Supervision
Partial Supervision shall be selected either by the Driver, or by information received from track-to-train transmission. In Partial Supervision the train shall be supervised according to train speed and distance data available, with a ceiling speed that may be shown momentarily when selected by the driver.

#### 3.1.5 Full Supervision Operation
Transferring to Full Supervision shall occur automatically when a movement authority and all other necessary information is received through track-to-train transmission. Full Supervision shall provide supervision of speed and distance.

#### 3.1.6 Isolation of ETCS Trainborne Equipment
The ETCS trainborne equipment shall be capable of being isolated, disconnecting the ETCS trainborne equipment from the vehicle braking system. When isolated, the system shall not show any ETCS information other than the fact that the system is isolated.

#### 3.1.7 Compatibility with Existing Train Control Systems
The ETCS trainborne equipment shall be capable of receiving information from national train control systems by means of the STM. The DMI shall display or be compatible with information from national train control systems.

#### 3.1.8 Unfitted Line Operation
Unfitted operation shall be possible if ordered by trackside or selected by the driver at start up. The on board shall supervise the train against a ceiling speed determined by the lower value of maximum train speed and national value for unfitted operation.

### 3.2 Infrastructure Functions

#### 3.2.1 Infrastructure Data Collection
The ETCS on-board shall be capable of receiving track description from the trackside. It shall be possible to send information on adhesion conditions from trackside, with priority given to trackside information over driver changes. Track to train transmission shall provide the capability to send different speed profiles for specific train categories. If track data to the location where the relevant movement authority ends are not available on-board, the movement authority shall be rejected.

#### 3.2.2 End of Movement Authority
The ETCS trainborne equipment shall supervise the end of movement authority if this information is available on-board. The target distance to be displayed on the DMI shall be based on the most restrictive braking curve. Together with the movement authority, the on board shall be able to receive one or more time-outs for certain sections and shorten the movement authority accordingly when a time out expires.

#### 3.2.3 On Sight Operation
Using train data and infrastructure data, braking curves shall be calculated taking into account target information but not the location of vehicles occupying the track. The ceiling speed level shall be defined as data National Value. Before entering an occupied track, driver acknowledgement shall be requested. The train shall be supervised according to train speed data available with a minimum ceiling speed supervision.

### 3.3 Trainborne Functions

#### 3.3.1 Static Train Speed Profile Calculation
ETCS shall collect all relevant information concerning train and line speed. ETCS shall calculate the permitted speed for the train for all locations of the authorised movement, respecting maximum line speed, track speed and special speed levels for special classes of trains. The ETCS trainborne equipment calculates the static train speed profile on the basis of infrastructure data and train data.

#### 3.3.2 Dynamic Train Speed Profile Calculation
Based on all relevant data, the ETCS shall calculate an emergency braking curve and a service braking curve. It shall be possible to permit/inhibit the service brake intervention by trackside. When changing to a lower speed level, the front end of the train shall respect the dynamic train speed profile. When changing to a higher speed level the rear end of the train shall respect the static train speed profile. The braking curves shall ensure that the train complies with its speed requirements. Where failure to apply the full service brake is detected the emergency brake shall stop the train in rear of the danger point.

#### 3.3.3 Release Speed Calculation
The release speed shall be calculated on board or given from the trackside, with trackside values taking priority. The release speed shall be indicated on the DMI. If calculated on board it shall ensure that the train will stop before reaching the danger point. When the train is stationary or after a certain time, the release speed calculation shall be based on the distance to the danger point.

#### 3.3.4 Train Location
The ETCS trainborne equipment shall be able to determine the location of the entire train. On lines fitted with RBC, the ETCS trainborne equipment shall be able to transmit the location of the entire train to the RBC. The train location calculation shall take into account error of odometry.

#### 3.3.5 Speed Calculation and Indication
Actual speed shall be indicated on the DMI. There shall be no discrepancy between the speed shown to the driver and the speed used for supervision of movement authorities and speed limits.

#### 3.3.6 Indication Displayed on the DMI
The indication provided shall enable the driver to drive at the permitted speed without receiving a warning and without intervention of ETCS. The driver shall know the distance to the next point defining the indicated braking curve and the permitted speed allowed. Visual and acoustic warnings to the driver about possible intervention from ETCS shall be given to enable the driver to react and avoid intervention. The driver shall have the possibility to select the language.

#### 3.3.7 Supervision of Movement Authorities and Speed Limits
A train shall be supervised to its static and dynamic train speed profiles. Within the braking curve area, a warning shall be given to the driver to enable him to react and avoid intervention from ETCS equipment at least 5 sec. before the intervention. If the train exceeds the permitted ceiling speed by a certain harmonised margin, the trainborne equipment shall execute a brake intervention until the actual speed does not exceed permitted speed.

#### 3.3.8 Roll Away and Reverse Movement Protection
To protect a traction unit from roll away and unwanted reverse movements the trainborne equipment shall monitor the direction of movement in relation to the permitted direction. The trainborne equipment shall apply the emergency brake after a distance defined by a national value is travelled by the train. When the traction unit has come to a standstill, the driver shall be able to release the emergency brake. After releasing the emergency brake ETCS will provide the supervision appertaining when roll away protection was initiated. When using more than one traction unit this function shall be disabled in all but the leading traction unit.

#### 3.3.9 Recording the ETCS Information
All data entered, received or indicated to the driver shall be recorded onboard related to UTC and a reference point. Information shall be recorded to an accuracy which enables a clear view of the functioning of ETCS and way the traction unit has been driven. Standardised output interfaces shall enable transmission of information recorded to other media for investigation. Data for accident investigation shall be stored for at least 24 hours, operational data for at least one week. Recorded information includes transitions of Level and operational status, driver's confirmation of transitions, train supervision data, actual speed, brake interventions, train trip function, override control, route suitability function, and isolation of on board ETCS equipment.

### 3.4 Special Operations

#### 3.4.1 Using Multiple Traction Units
It shall be possible to use multiple traction units without isolating the ETCS trainborne equipment on traction unit(s) with an in-operative cab. Information received shall not influence the traction unit(s) with in-operative cabs. The train trip function shall be suppressed in traction unit(s) with in-operative cabs.

#### 3.4.2 Using Tandem Traction Units
It shall be possible to use tandem traction units without isolating the ETCS trainborne equipment on the tandem traction unit. The train trip function shall be suppressed on the tandem traction unit. The driver shall enter the driver ID.

#### 3.4.3 Train Reversing
It shall be possible to drive the train backwards in a supervised way (speed and distance) according to information received from trackside.

### 3.5 Functions Required in the Event of Incidents

#### 3.5.1 Passing a Stop Signal with Restricted Movement Authority
The train speed shall be at or below a speed specified by a national value. The driver shall select an override control according to the permission received, protected against inadvertent operation. When the train passes the stop signal, the train trip function shall be suppressed. Actual speed shall still be shown on the DMI with a special indication. The train shall be capable of receiving any track-to-train information intended and relevant for this train including movement authority.

### 3.6 Protection Functions

#### 3.6.1 Emergency Stop to Train(s)
If supervised by an RBC it shall be possible to command an emergency stop to all trains in a particular area or to a specific train. It shall be possible to command an immediate train stop or a conditional emergency stop. When a train has received an emergency stop ETCS shall command the emergency brake, indicated to the driver on the DMI.

#### 3.6.2 Route Suitability
It shall be possible to prevent a train from entering a route for which it does not meet the required criteria. Route unsuitability shall be indicated on the DMI. The driver shall be able to override the function when the train is stationary. After overriding this function the movement authority shall be re-established.

#### 3.6.3 Train Trip
When a traction unit passes a stop-signal the emergency brake shall be triggered. Operation of the train trip shall be indicated on the DMI. The emergency brake shall be applied until the traction unit is stationary. When the traction unit is stationary the driver shall be required to acknowledge the train trip condition, releasing the emergency brake. After the acknowledgement the driver shall be able to continue the movement or drive backwards for a certain distance defined by national value.

### 3.7 Train Control Centre Functions

#### 3.7.1 Train Identification
The ETCS trainborne equipment shall transmit its own train identification to the RBC. The train running number shall consist of a maximum of 8 numeric digits.

#### 3.7.2 Geographical Position of the Train
On demand, the position of the front end of the train at the time of the demand shall be indicated on the DMI while the train is moving or stationary.

### 3.8 Additional Functions

#### 3.8.1 Control of Pantograph and Power Supply
The ETCS on-board shall be capable of receiving information about pantograph and power supply from the trackside. The ETCS trainborne equipment shall indicate on the DMI the information regarding pantograph and power supply. Information regarding lowering and raising of the pantograph and opening/closing of the circuit breaker shall be provided separately and in combinations.

#### 3.8.2 Air Tightness Control
The ETCS on-board shall be capable of receiving information regarding air tightness from the trackside.

#### 3.8.3 Plain Text Transmission
It shall be possible to send plain text messages from track to train. When the plain text message appears on the DMI, the driver shall be alerted. The onboard equipment shall display plain text messages as received. The character set used shall support different languages.

#### 3.8.4 Fixed Text Messages
It shall be possible to send fixed text messages from track to train. Fixed text messages shall be provided in the language selected by the driver.

#### 3.8.5 Management of Special Brakes
It shall be possible to send information regarding the inhibition of regenerative brake, eddy current brake, and magnetic shoe brake. Information shall be shown on the DMI.

### 3.9 Functions Primarily Related to RBC

#### 3.9.1 Train Integrity
The ETCS on-board shall be capable of sending to the trackside train integrity information detected by a system outside ETCS. The driver shall be able to confirm the train integrity to the RBC manually when the train is stationary.

#### 3.9.2 Train Data to be Sent to Trackside
The on board shall be capable of sending train data to the trackside after confirmation by the driver, or when entering the RBC area. Data includes train running number, STM ready for use, train gauge, max. axle load, status of air tight system, type of el. power accepted, international train category, max. train speed, and train length.

#### 3.9.3 Revocation of a Movement Authority
It shall be possible to revoke a Movement Authority that has already been issued to a train in a co-operative way between RBC and train. The co-operative revocation shall be possible to a new target location proposed from RBC. The new target location shall be checked for acceptance by the on board. If a train cannot stop at the proposed new target location it shall reject the request and keep the old target location.

#### 3.9.4 Reversing
The Reversing function shall only be possible in one active cab which is not closed at any time during the procedure. Reversing shall be possible as defined by a value given with the MA. The driver shall be able to use the Reversing function without needing to re-confirm the train data. Reversing shall be supervised to a distance and speed set as National Values. The distance supervised can be extended from the trackside. Once the train starts reversing the MA shall be cancelled.

#### 3.9.5 Handover Between RBC Areas
The train shall be able to automatically pass from one RBC area to another without driver intervention. If the train is equipped with two operational radios there shall be no performance penalty as a result of a transition. If the train is equipped with only one operational radio, passing from one RBC to another shall still be possible but might result in a performance penalty.

## 4. Failures and Fall-back Procedures

### 4.1 Interruption in Transmission
In the event of a Transmission Failure the following reactions shall be capable of being applied according to a National Value:
- Option 1: The ETCS trainborne equipment shall immediately command the emergency brake
- Option 2: The ETCS trainborne equipment shall immediately command the full service brake
- Option 3: The train may proceed unrestricted to the end of its movement authority

### 4.2 On Board Equipment Failures
If there are failures of the trainborne equipment which compromise the safety of train supervision, the ETCS trainborne equipment shall immediately command the brake and bring the train to a stop. The occurrence of a failure shall be displayed on the DMI. In ETCS with RBC this restriction on performance shall, if possible, be transmitted to the RBC.

## 5. Glossary
The document includes a comprehensive glossary of terms used in ETCS including: Absolute braking distance, Acknowledge, Advisory information, Axle counter, Balise, Banking, Block, Braking curve, Confirm, Continuous data transmission, CTS, Default value, DMI, Driving "on sight", Dynamic train speed profile, Emergency brake, End of movement authority, Equipped line, Exit signal, Fixed block, Full service brake, In advance of, Infill information, In rear of, Interlocking, Intermittent transmission, Intervention, Local Time, Loop, Main signal, Movement authority, Moving block, Multiple, National values, Non-equipped line, Odometry, Overlap, Pantograph, Permissive signal, Permitted speed, Propelling, Railway management system, RBC, Reference point, Relative braking distance, Release speed, Reversing, Route, Route map, Safety distance, Shunt hauling, Shunt propelling, Shunting movement, Shunting signal, SRS, Static speed profile, Station, STM, Stop signal, SSRS, Tandem, Target, Temporary speed restriction, Traction unit, Track circuit, Track free, Track occupied, Track-to-train transmission, Train, Train data, Train memory, Train movement, Train-to-track transmission, Train trip, Warning, Wheelslip, Wheelslide.
