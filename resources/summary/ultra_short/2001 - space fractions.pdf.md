Purpose & Scope  
A web-based interactive game for sixth-grade students to improve fraction-solving skills through gameplay. Solves the problem of students struggling with fraction concepts in classroom settings. Excludes offline functionality, non-sixth-grade users, and hardware installation requirements.  

Product Background / Positioning  
Serves as an umbrella interface for existing S2S math projects, hosted on the S2S website. Integrates with Pecan Springs Elementary School’s educational needs but operates independently as a standalone web application.  

Core Functional Overview  
1. Introductory movie with skip option.  
2. Main menu with help section and game access.  
3. Adaptive fraction question sequence (multiple-choice).  
4. Storyline progression based on user answers.  
5. Score-based ending scene with replay option.  
6. Admin question updater via password-protected interface.  
7. Links to other S2S math projects via "Math Umbrella."  

Key Users & Usage Scenarios  
Students (Alice, Bobby): Play game via mouse clicks; Alice uses help, Bobby seeks competition. Teacher (Claire): Administers questions via updater, accesses game stats. Claire has privileged admin access; students cannot modify content.  

Major External Interfaces  
Requires Flash 5-compatible web browser. No hardware dependencies. All interactions occur through standard web browser interfaces; no external system integrations.  

Key Non-functional Requirements  
- Performance: Game components downloadable within 1 minute via modem.  
- Maintainability: Primary design goal; code structured for easy future updates.  
- Security: Constrained by browser security; no additional security measures.  
- Reliability: Ensured via team testing.  

Constraints, Assumptions & Dependencies  
- Must run on Flash 5 browsers; no support for non-Flash environments.  
- Single-user instance per browser session.  
- Depends on S2S website hosting and Pecan Springs Elementary’s educational context.  

Priorities & Acceptance Approach  
Maintainability is top priority. Acceptance requires:  
- Game playable on Flash 5 browsers.  
- Admin question updater functional with password protection.  
- Score feedback and adaptive storyline operational.