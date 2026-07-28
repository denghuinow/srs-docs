# Short Summary: Dallas/Ft. Worth Regional Center-to-Center Communications Network

## Background and Objectives
This project aims to establish a regional Center-to-Center (C2C) communications network for the Dallas/Ft. Worth area to integrate disparate traffic management systems. Its primary objectives are to create a common repository for regional traffic data, enable cross-agency device command and control, and provide public traffic information displays, all based on national ITS standards for future extensibility.

## In Scope
*   Implementation of interfaces for data exchange on roadway networks, traffic conditions, incidents, and lane closures.
*   Support for status monitoring and remote control of various ITS field devices (e.g., Dynamic Message Signs, CCTV cameras, ramp meters).
*   Development of a web-based graphical map to display real-time traffic conditions and incidents.
*   Creation of a Windows application for agencies without formal Traffic Management Centers to input incident data.
*   Utilization of ITS standards (TMDD, DATEX/ASN) over TCP/IP for all communications.

## Out of Scope
*   Detailed specification of internal system processes or data structure implementations.
*   Resolution of firewall and network gateway connectivity for the Remote Control GUI.
*   Support for specific device commands not agreed upon by all centers (e.g., certain CCTV commands for Fort Worth).
*   Management of data consistency challenges between separately managed roadway and transit networks.
*   Expansion on the rationale for requirements deemed "obvious" from their description.

## Stakeholders and Core Use Cases
*   **North Central Texas Council of Governments (NCTCOG) / Software Task Force:** The project sponsor and governing body overseeing regional transportation integration.
*   **Texas Department of Transportation (TxDOT) TMCs:** Primary operators and owners of traffic management systems and field devices, providing and consuming data.
*   **Local Traffic Management Agencies (e.g., City of Dallas, DART):** Participants managing specific devices (signals, transit) and contributing data to the regional network.
*   **Southwest Research Institute (SwRI):** The system developer responsible for designing and implementing the software per this specification.
*   **Public / Travelers:** End-users of the traffic information displayed via the public web map.

**Core User Stories:**
1.  As a **Traffic Management Center operator**, I want to **send control commands to a Dynamic Message Sign in another agency's jurisdiction** so that **I can coordinate region-wide traveler alerts**.
2.  As a **public traveler**, I want to **view a color-coded map of current traffic speeds and incidents online** so that **I can plan my route effectively**.
3.  As an **agency without a formal TMC**, I want to **input incident and lane closure data via a dedicated application** so that **my information is included in the regional repository**.
4.  As a **system integrator**, I want the **software to use configurable building blocks based on ITS standards** so that **it can be cost-effectively deployed and extended for new partners**.
5.  As a **transit agency operator**, I want to **share real-time bus location and schedule adherence data** so that **multimodal traffic conditions can be assessed**.
6.  As a **network administrator**, I want the **system to operate in a test mode with detailed activity logging** so that **I can perform development and troubleshooting**.

## Success Metrics
*   Successful bidirectional exchange of status and control data for all specified device types (DMS, CCTV, ramp meters, etc.) between connected centers.
*   Public web map accurately displays real-time traffic conditions, incidents, and device locations sourced from the integrated data repository.
*   The system architecture demonstrably supports the addition of new local or regional partners through configuration, not major redevelopment.

## Major Constraints
*   The software must execute in a Microsoft Windows NT environment and be implemented using C/C++.
*   The web map application must utilize ESRI's ARC Internet Map Server (ARC IMS) product.
*   Data transmission must comply with the Traffic Management Data Dictionary (TMDD) standard, encoded in DATEX/ASN and transported via TCP/IP.
*   Interfaces must accommodate existing, dissimilar traffic management systems by converting proprietary formats to the project's standard protocol.
*   Specific graphical user interfaces (Incident GUI, Remote Control GUI) must be developed using C/C++ and ESRI Map Objects.

## Undecided Issues
*   The specific speed thresholds (TBD MPH) for color-coding traffic conditions (green, yellow, red) on the web map.
*   The exact mechanism and responsibility for maintaining link identifier consistency between separately managed roadway and transit data sets.
*   Full resolution of command compatibility for certain device functions (e.g., CCTV "tour" commands for Dallas, momentary commands for Fort Worth).
*   Final determination of all "Days/Times Commands Accepted" for each device type per center in response to timeframe requests.
*   Complete strategy for secure Remote Control GUI connectivity across public networks and agency firewalls.