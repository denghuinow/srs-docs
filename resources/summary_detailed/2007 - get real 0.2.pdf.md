# Detailed Summary

## Background and Scope
The Get Real website aims to attract Oregon high school students to pursue computer science degrees at Oregon University System campuses. This version 2 update focuses on improving navigation, content depth, and visual appeal while maintaining teen-friendly design. Non-goals include developing user documentation and creating hardware/software interfaces beyond standard web capabilities.

## Role Matrix and Use Cases
- **Primary Users**: Oregon high school students (grades 9-12)
- **CS-Interested Students**: Seek detailed career and college information
- **Non-CS Students**: Need engaging content to attract them to CS fields
- **CS Minor Candidates**: Students from other disciplines considering CS minor
- **Web Designers**: Maintain and update site content
- **Content Editors**: Manage RSS feeds and FAQ responses

Main scenarios include browsing career information, comparing colleges, viewing real people profiles, and searching for CS information. Exception scenarios involve handling outdated content and managing video streaming limitations.

## Business Process
**Main Process - Student Information Access (≤8 steps)**
1. Student visits homepage
2. Navigates to section of interest (careers, colleges, people)
3. Views content with visual elements
4. Uses internal/external search
5. Accesses additional resources
6. Considers CS career path
7. Views call-to-action elements
8. Returns for updated content

**Key Branch - Content Management (≤4 steps)**
Trigger: New content available
1. Editor reviews RSS feeds
2. Curates relevant articles
3. Updates FAQ responses
4. Publishes to appropriate sections
Output: Updated website content

## Domain Model
- **Student Profile** (grade_level, interests)
- **College Information** (campus_name, programs_offered, required)
- **Career Profile** (job_title, salary_range, description, required)
- **Real People Profile** (name, photo, video_url, story, required)
- **Article** (title, source, publication_date, url, required)
- **FAQ** (question, answer, category, date_posted, required)
- **High School Course** (course_name, recommendation_level, required)
- **Professional Organization** (org_name, website_url, description)

## Interfaces and Integrations
- **OUS Main Site**: Inbound integration for domain hosting and search engine optimization
- **RSS Feed System**: Outbound integration for current CS information
- **Search Engines**: External integration for site indexing and external searches
- **Video Streaming**: External integration for real people profiles

## Acceptance Criteria
- Given a student visits the Real People section, when they view video profiles, then they should see diverse CS career examples
- Given a student searches for college information, when they use the search function, then relevant OUS campus details should appear
- Given a non-CS student browses the site, when they encounter visual content, then text walls should be minimized with adequate white space

## Non-functional Metrics
- **Performance**: Page load times comparable to OUS main site; adequate bandwidth for video streaming
- **Reliability**: Consistent uptime matching OUS standards; regular content updates
- **Security**: Copyright protection equivalent to OUS policies
- **Compliance**: Adherence to OUS web design conventions and CSS standards
- **Observability**: Hit tracking and time-on-site metrics for content evaluation

## Milestones and Release Strategy
1. Complete design prototype review
2. Implement new page sections
3. Integrate search functionality
4. Add video profiles
5. Deploy RSS feed system
6. Launch version 2 with monitoring

## Risk List and Mitigation Strategies
- Limited bandwidth for video: Optimize video compression and provide alternative content
- Resource constraints: Prioritize high-impact features and phase implementation
- Content maintenance: Establish clear ownership for regular updates
- Student engagement: Continuously evaluate hit metrics and adjust content
- Browser compatibility: Test across IE, Firefox, and Netscape
- Search functionality: Use proven Google search tools
- Visual design: Incorporate student feedback on prototypes
- Information accuracy: Regular review of college and career data

## Undecided Issues and Responsible Parties
- Extent of community and private college inclusion: OUS Task Force
- Video profile implementation approach: Web Design Team
- High school course recommendations: UO and other campuses
- RSS feed editing resource allocation: Chancellor's Office
- Professional organization listing scope: Content Editors
- FAQ response management: Not mentioned
- CS minor content development: Not mentioned
- External search implementation details: Web Design Team