# Video Search Engine Requirements Specification

## 1. Introduction

### 1.1 Purpose
This document specifies requirements for a Video Searching software that searches multiple websites for streaming videos and torrents, returning results to the user.

### 1.2 Project Scope
The Video Searching software uses an active internet connection to search multiple websites for streaming videos or torrents. It aids users in locating specific videos or genres, reducing search time across various websites through a single query. The system contains databases of different websites used in searches, which can be easily updated for wider search coverage.

## 2. Overall Description

### 2.1 Product Perspective
The program is a new self-contained product developed due to demand identified in ethnography studies. These studies showed people regularly spend time searching websites for videos they want to watch, either for streaming or downloading. The system aims to speed up this process.

### 2.2 Product Features
- Search engine for finding torrent and streaming video locations on the internet
- User can specify whether to search for torrents, streaming videos, or both
- Results divided into specified types using different tabs
- Results orderable by categories such as name, size, site, etc.
- Option to filter videos by age restrictions (e.g., adult content)
- Option to filter or exclusively search certain websites (e.g., YouTube only)
- Facility for users to store favorite videos for later access

### 2.3 User Classes and Characteristics
Two user levels:
1. General users who use the software to find videos (frontend only)
2. System developers who can edit which sites the system searches based on safety, compatibility, search speed, and usefulness

### 2.4 Operating Environment
- Portable across different operating systems: Microsoft XP/Vista, Mac OS X, and Linux platforms
- Compatible with different web browsers: Internet Explorer, Firefox, Safari
- Requires reasonably up-to-date computer with internet connection via modem

## 3. System Features

### 3.1 Torrent Search
High-priority feature that searches a database of compatible torrent websites.

#### Functional Requirements
- Shares search bar with streaming search
- Database of torrent sites can be updated via internet
- Tick box to include/exclude torrent searching
- Retrieves seed/peer count, file size, date posted, and webpage link
- Displays "No results were found for this search" when no results
- Results arrangeable by size/date/alphabetical order via column headers
- Page navigation buttons for results

### 3.2 Video Stream Search
Searches a database of compatible video streaming websites, including both hosting sites (YouTube, MegaVideo) and linking sites (surfthechannel.com).

#### Functional Requirements
- Shares search bar with torrent search
- Database of video hosting/linking sites can be updated via internet
- Separate tick boxes for video host and video link searching
- Video hosting queries retrieve full video name, length, date posted, and video link
- Video linking queries retrieve show name, episode name, and webpage link
- Displays "No results were found for this search" when no results
- Results arrangeable by length/date/alphabetical order via column headers
- Page navigation buttons for results

## 4. External Interface Requirements

### 4.1 User Interfaces
Single main screen containing all functionality for ease of use. Layout includes:
- Menu bar with standard features plus filter (parental controls) and favorites options
- Main search entry field
- Tick boxes for torrent/streaming search selection
- Tabs for different search result pages
- Results display area showing video name, website location, size, rating, and comments

### 4.2 Software Interfaces
Uses hyperlinks to open websites in default web browser.

### 4.3 Communications Interfaces
Uses PHP or similar languages to query different website servers.

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements
- Query times no longer than 5 seconds to any website
- Hyperlink sending to browser less than 1 second
- Program loading less than 10 seconds
- Torrent results with 0 seeds not displayed
- Sorting results less than 0.1 seconds
- Results page displays 100 results
- Torrent results with rating less than 1 not displayed

### 5.2 Safety Requirements
Development team must investigate each website in database monthly to ensure no illegal or harmful content exposure.

### 5.3 Security Requirements
No user data maintained or content hosted.

### 5.4 Legal Requirements
Requires full legal review before public release for indemnification of liability. Software stays within legal requirements as it only lists links for video streams/downloads and does not host videos.
