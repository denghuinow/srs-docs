# Balanced Summary

## Goals and Scope
The Get Real website aims to attract and encourage Oregon high school students to pursue computer science degrees at Oregon University System campuses. It provides teen-friendly navigation with sufficient career information depth while maintaining visual appeal to hold student attention. The scope is limited to Oregon high school students with potential expansion to students considering CS minors.

## Roles and User Stories
- **Interested Student**: I want to explore CS career information so that I can make informed degree decisions.
- **Undecided Student**: I want to see engaging CS content so that I might consider CS as a career option.
- **CS Minor Candidate**: I want to understand CS minor benefits so that I can complement my primary major.
- **Website Administrator**: I want to track site usage metrics so that I can evaluate and improve content effectiveness.
- **Content Editor**: I want to manage RSS feeds and FAQs so that the site remains current and relevant.

## Key Processes
1. **Site Navigation** (trigger: user visits homepage) - Users browse organized sections through intuitive menus.
2. **Content Consumption** (trigger: section selection) - Students access career information, profiles, and resources.
3. **Search Execution** (trigger: search query) - Users perform internal and external CS-related searches.
4. **FAQ Interaction** (trigger: question submission) - Students submit questions to grads/professors.
5. **Content Updates** (trigger: new information) - Administrators refresh RSS feeds and articles.
6. **Usage Tracking** (trigger: site access) - System monitors hits and engagement metrics.
7. **Design Updates** (trigger: evaluation data) - Team implements improvements based on usage patterns.

## Domain Data Elements
- **User Profile**: (UserID) + role, preferences, interaction history
- **Career Content**: (ContentID) + title, category, media type, description
- **College Information**: (CollegeID) + name, programs, contact details
- **Real People Profile**: (ProfileID) + name, career, story, media
- **FAQ Entry**: (QuestionID) + question, answer, category, date
- **RSS Feed**: (FeedID) + source, update frequency, content summary

## Non-functional Requirements
- Fast server response time for short attention spans
- Browser compatibility with IE, Firefox, and Netscape
- Consistent design standards with OUS website
- Copyright security matching OUS protocols
- Maintainability for content updates
- Usability with visual appeal and white space

## Milestones and External Dependencies
- Version 2 summer 2007 deployment
- Potential Version 3 future development
- OUS server infrastructure dependency
- Campus CS program information coordination
- High school curriculum recommendations from ACM/UO

## Risks and Mitigation Strategies
- **Limited bandwidth for video**: Optimize media compression
- **Resource constraints**: Prioritize high-impact features
- **Student engagement**: Implement visual design improvements
- **Content maintenance**: Establish update schedules
- **Technical compatibility**: Multi-browser testing protocols

## Undecided Issues
- Extent of community and private college inclusion
- Video profile implementation approach
- High school course recommendation sources
- Professional organization listing scope
- RSS feed maintenance resource allocation
- CS minor content development timeline