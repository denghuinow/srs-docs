Purpose & Scope  
The system manages voucher lifecycle for Marie Stopes International Uganda’s STD treatment voucher pilot in Mbarara District, covering voucher creation, sales, claim processing, and reporting. It excludes fraud investigation beyond automated mismatch detection and does not handle voucher distribution logistics.  

Product Background / Positioning  
It is the central system for MSIU’s Output-Based Aid (OBA) pilot, replacing manual voucher tracking. Integrates with distributors and service providers (VSPs) to process claims for subsidized STD treatments under a 1-year pilot.  

Core Functional Overview  
- Voucher generation with unique barcoded IDs and validity dates  
- Distributor sales tracking (batch, quantity, payment)  
- Claim processing with automated validation against treatment algorithms  
- Voucher return handling from distributors  
- Client feedback collection on treatment satisfaction  
- Automated report generation for claims, providers, and syndromes  

Key Users & Usage Scenarios  
MSIU admins (full access: voucher creation, fraud monitoring), distributors (view sales history, return vouchers), VSP staff (submit claims, enter treatment data). Admins process claims monthly; VSPs submit claims post-treatment; distributors manage sales returns.  

Major External Interfaces  
Bar-code readers for voucher verification and claim form processing. Biometric thumbprint scanners for patient identity validation during treatment.  

Key Non-functional Requirements  
- Process 20,000 vouchers during pilot phase  
- Reimburse valid claims within one month of submission  
- Automatically deactivate VSPs after two thumbprint mismatches on same voucher  
- Role-based access control for all modules  

Constraints, Assumptions & Dependencies  
Vouchers cannot be edited/deleted post-creation; validity dates editable only by admins. Assumes VSPs follow MSIU treatment algorithms. Depends on distributor sales data and VSP claim submissions.  

Priorities & Acceptance Approach  
Top priority: Fraud prevention via thumbprint matching and VSP deactivation. Acceptance requires: 1) Valid claims processed within payment terms, 2) No manual claim entry without mandatory fields, 3) VSP deactivation triggered by two mismatched thumbprints.