**Purpose & Scope**
The system is a distance learning platform for NJIT to enable more effective communication between professors and students. It provides a secure application platform with features for collaboration, communication, and testing. It does not replace existing university databases or systems for core student administration.

**Product Background / Positioning**
This is a new online website intended to create a classroom-like environment. It will integrate with and modify the existing NJIT user database. It is positioned as an enhancement to current distance learning capabilities, not a replacement for all existing systems like email.

**Core Functional Overview**
*   Real-time instant messaging (text chat) between users.
*   Live and on-demand audio/video streaming and conferencing.
*   Online exam administration, submission, and grading.
*   Personal file storage and management with quota enforcement.
*   User profile creation and customization.
*   Document collaboration and file sharing between users.
*   Recording and distribution of class lectures as podcasts.
*   Application and whiteboard sharing for live collaboration.

**Key Users & Usage Scenarios**
*   **System Administrators:** Full system control, manage enrollment, create classes.
*   **Administrative End Users (Professors):** Manage their classes and enrolled users, grade exams, host lectures.
*   **Limited End Users (Students):** Participate in classes, communicate, submit assignments and exams, customize own profile.
*   Typical scenarios include attending a live video lecture, collaborating on a document with a team, taking a timed online exam, and downloading a podcast of a past lecture.

**Major External Interfaces**
*   **User Interface:** A web-based portal with compartmentalized sections for different features (welcome, class selection, application launch).
*   **Software Interfaces:** Must interface with the local operating system and require Microsoft Excel/PDF readers for reporting. Relies on a web browser as the primary client.
*   **Communications Interfaces:** Uses standard web protocols; requires SSH, FTP, and VPN clients for certain connections. Specific browsers (Internet Explorer, Firefox, Safari) are mandated.

**Key Non-functional Requirements**
*   **Performance:** The server must support at least 250 concurrent users. Client workstations require a minimum 500 MHz CPU, 512 MB RAM, and a broadband internet connection for conferencing.
*   **Security:** User passwords must be 8-12 characters (letters and numbers), changed every three months. All user content must comply with NJIT conduct policies.
*   **Reliability/Availability:** System has an estimated 99% uptime. Scheduled maintenance will be announced with at least 24 hours notice.
*   **Maintainability:** System rollouts and validation must be scheduled during periods of low usage to minimize downtime.

**Constraints, Assumptions & Dependencies**
*   **Constraints:** Development occurs while the university is in session. Only specific browsers (Internet Explorer, Firefox, Safari) and operating systems (Windows XP/Vista, Mac OS) are supported. Pop-up windows and JavaScript must be enabled by users.
*   **Assumptions:** The existing NJIT database will be available and modifiable. Users have adequate computers, network connections, and peripherals (webcam, microphone). Staff and students are willing to learn and use the new system.
*   **Dependencies:** Modification of the existing NJIT user database to meet new requirements. Availability of funding for required hardware, software, and personnel.

**Priorities & Acceptance Approach**
*   High-priority features include instant messaging and core communication tools. Medium-priority features include audio/video streaming, user profiles, and basic file hosting. Lower-priority items are enhanced GUI and file management features.
*   Acceptance is based on the implementation of all specified features within the allotted timeframe and budget, adhering to the defined constraints and performance thresholds (e.g., concurrent user support).