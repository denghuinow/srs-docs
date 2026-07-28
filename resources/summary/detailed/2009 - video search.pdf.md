# Detailed Summary: Video Search Engine (X-ray)

## Background and Scope
This project aims to develop a desktop application, "X-ray," that aggregates search results for online videos from multiple websites, including both video streaming sites and torrent trackers. The system is designed to reduce user effort by providing a single interface to query multiple sources, with features for filtering, sorting, and managing results. The scope includes developing a cross-platform client with a unified search interface, maintaining a configurable database of source websites, and displaying categorized results. Non-goals include hosting any video content, storing user data beyond local favorites, and directly handling video playback or downloads.

## Stakeholders Matrix and Use Cases
*   **End User:** Uses the software's front-end to search for and access video streams and torrents. Responsible for entering queries and interacting with results.
*   **System Developer/Admin:** Maintains and updates the software and its internal database of searchable websites. Responsible for ensuring site compatibility, safety, and usefulness.
*   **Website Operator (External):** Owns and operates the external video hosting, linking, or torrent sites that are queried by the system.

**Use Cases:**
1.  **Main:** User performs a combined search for torrents and streaming videos.
2.  **Main:** User filters search to only include specific types (e.g., only torrents) or to exclude specific websites.
3.  **Main:** User sorts search results by various attributes (name, size, date).
4.  **Main:** User navigates through paginated search results.
5.  **Main:** User saves a video link to a local favorites list.
6.  **Main:** User applies content filters (e.g., parental controls) to exclude adult content.
7.  **Exception:** A search returns zero results, and the system displays an appropriate message.
8.  **Exception:** Developer updates the internal database of searchable websites via an online mechanism.

## Business Process
**Main Process: Execute Video Search**
1.  **Trigger:** User launches the application.
2.  **Input:** User enters a search term and selects content types (Torrent, Video Host, Video Link) via tick boxes.
3.  The system queries its internal database for the list of active websites corresponding to the selected types.
4.  The system sends the search query concurrently to each relevant external website.
5.  The system collects and parses the responses from the websites.
6.  The system applies local filters (e.g., minimum seed count for torrents, excluded sites).
7.  **Output:** The system displays the aggregated, filtered results in the appropriate tab(s) of the main interface.
8.  User can sort results, page through them, or click a link to open the target in their default browser.

**Key Branch A: Manage Favorites**
1.  **Trigger:** User selects a "Add to Favorites" action from a result.
2.  The system stores the video metadata (name, link) in a local, persistent store.
3.  User can later view and select from the list of favorites via a menu option.
4.  Selecting a favorite re-opens the link in the default browser.

**Key Branch B: Admin Updates Site Database**
1.  **Trigger:** Developer initiates a database update.
2.  The system fetches an updated list of websites (and potentially their query templates) from a managed, remote source.
3.  The system validates and integrates the new site list into its local configuration.
4.  Future searches include the newly added websites.

## Domain Model
*   **SearchQuery:** (required: term, contentTypes)
*   **SearchResult:** (required: title, sourceUrl, sourceSite; reference: SearchQuery)
    *   **TorrentResult:** (fields: seedCount, peerCount, fileSize, datePosted, rating)
    *   **StreamingResult:** (fields: length, datePosted)
        *   **HostResult:** (fields: fullVideoName)
        *   **LinkResult:** (fields: showName, episodeName)
*   **WebsiteSource:** (required: url, type [TorrentTracker, VideoHost, VideoLink], isActive)
*   **UserFavorite:** (required: title, url, dateAdded)
*   **ContentFilter:** (fields: excludedSites, minimumRating, excludeAdultContent)

## Interfaces and Integrations
1.  **System:** External Video/Torrent Websites | **Direction:** Outbound | **Theme:** Query and scrape search results | **Input:** Search term, website-specific query format | **Output:** HTML/structured data containing result lists | **SLA:** Query response time <5 seconds.
2.  **System:** User's Default Web Browser | **Direction:** Outbound | **Theme:** Launch hyperlink | **Input:** URL from a SearchResult | **Output:** Browser opens to the specified page | **SLA:** Launch time <1 second.
3.  **System:** Remote Configuration Service | **Direction:** Outbound | **Theme:** Fetch updated site database | **Input:** Software version/request | **Output:** Structured list of WebsiteSource entities | **SLA:** Update check on admin request; integrity validation required.

## Acceptance Criteria
**Capability: Combined Search**
*   Given the user has entered a search term and selected both "Torrent" and "Video Host" options, when they execute the search, then results from both torrent sites and video hosting sites are displayed in their respective tabs.
*   Given a search has been executed, when the user clicks the "Size" column header in the torrent results tab, then the list is sorted by file size in ascending/descending order.

**Capability: Result Filtering**
*   Given torrent results include a file with 0 seeds, when the results are displayed, then that specific torrent is not shown in the list.
*   Given the user has added "SiteX" to the exclusion filter, when a new search returns results from SiteX, then those results are omitted from the display.

## Non-functional Metrics
*   **Performance:** Program load time <10 seconds. Sorting operation latency <0.1 seconds.
*   **Reliability:** Graceful handling of unresponsive external websites (timeout, skip, log).
*   **Security:** No storage of sensitive user data. Software must not introduce vulnerabilities.
*   **Compliance:** Legal review required before public release to ensure indemnification against liability for linked content.
*   **Observability:** Logging of search queries and external site response failures for maintenance.

## Milestones and Release Strategy
1.  Core search functionality for one website type (e.g., video hosts).
2.  Integration of torrent search and streaming link search.
3.  Implementation of filtering, sorting, and pagination UI.
4.  Favorites and content filter feature completion.
5.  Cross-platform compatibility testing (Windows XP/Vista, Mac OS X, Linux).
6.  Beta release followed by final v1.0 release after legal review.

## Risk List and Mitigation Strategies
1.  **Risk:** External website changes break query parsing. **Mitigation:** Implement a modular, easily updatable parser for each site; remote database updates can push new parsing logic.
2.  **Risk:** Legal liability for linking to copyrighted or illegal content. **Mitigation:** Conduct pre-release legal review; implement user content filters; regularly audit site database.
3.  **Risk:** Poor performance due to slow external sites. **Mitigation:** Implement query timeouts, concurrent requests, and caching where possible.
4.  **Risk:** Software flagged as "adware" or blocked for accessing torrent sites. **Mitigation:** Clear communication of software purpose; provide easy site exclusion for users/networks.
5.  **Risk:** Cross-platform compatibility issues. **Mitigation:** Use portable development frameworks; early and continuous testing on target platforms.
6.  **Risk:** Database of websites becomes outdated. **Mitigation:** Build a reliable remote update mechanism with manual override for admins.

## Undecided Issues and Responsible Parties
1.  **Issue:** Specific technology stack for cross-platform development (e.g., Java, Qt, Electron). **Responsible:** Development Team.
2.  **Issue:** Protocol and format for the remote website database updates. **Responsible:** System Architect.
3.  **Issue:** Detailed specification for the "rating" system used to filter torrents. **Responsible:** Product Manager.
4.  **Issue:** Implementation of the monthly website safety review process. **Responsible:** Development Team Lead.
5.  **Issue:** Handling of websites requiring authentication (e.g., BBC iPlayer). **Responsible:** Product Manager / Development Team.
6.  **Issue:** Final list of websites to be included in the initial database. **Responsible:** Product Manager.