Purpose & Scope  
The system searches torrents and streaming video sources across multiple websites to reduce manual searching. It does not host video content, store user data, or provide video playback.  

Product Background / Positioning  
Developed from ethnography studies identifying user pain points in manually searching video sites. Positioned as a standalone tool complementing existing platforms like YouTube and Facebook without integrating with them.  

Core Functional Overview  
- Search torrents across a developer-maintained site database.  
- Search streaming video hosts and link sites (e.g., YouTube, surfthechannel.com).  
- Filter results by site, content type, or age restrictions.  
- Sort results by name, size, date, or length.  
- Display results in tabbed views (torrents, streaming hosts, streaming links).  
- Store favorite video links for later access.  

Key Users & Usage Scenarios  
General users: Search, filter, sort, and save results. Developers: Update site databases for safety, compatibility, and relevance.  

Major External Interfaces  
Single-screen user interface. Uses hyperlinks to open sites in default browsers. Communicates with external sites via PHP-based queries.  

Key Non-functional Requirements  
Query response within 5 seconds; program load under 10 seconds; results sorted in <0.1 seconds; 100 results per page; no 0-seed torrents displayed.  

Constraints, Assumptions & Dependencies  
Monthly safety checks of all database sites; no user data storage; relies on external sites’ availability for search results.  

Priorities & Acceptance Approach  
High priority for torrent and streaming search features. Acceptance requires all search results to display within specified performance metrics.