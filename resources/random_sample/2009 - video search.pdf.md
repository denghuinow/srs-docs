# Short Summary

- **Background and objectives**: The Video Search Engine aims to reduce user search time by querying multiple websites for streaming videos and torrents through a single interface, improving efficiency and relevance of results.

- **In scope**:
  - Search for torrents and streaming videos from multiple websites.
  - Filter results by content type, website, or age restrictions.
  - Sort results by name, size, date, or other categories.
  - Save favorite videos for later access.
  - Cross-platform compatibility across Windows, Mac, and Linux.

- **Out of scope**:
  - Hosting any video content.
  - Storing user personal data.
  - Searching UseNet Binaries (planned for future version).
  - Automatic content moderation without developer review.
  - Integration with non-listed external websites.

- **Roles and core use cases**:
  - As a general user, I want to search for videos and torrents so that I can find content quickly across multiple sites.
  - As a general user, I want to filter and sort results so that I can easily locate relevant videos.
  - As a system developer, I want to update the site database so that the search remains current and safe.

- **Success metrics**:
  - Query response time under 5 seconds.
  - Program load time under 10 seconds.
  - Sorting results in less than 0.1 seconds.

- **Major constraints**:
  - Must work across multiple operating systems and browsers.
  - Requires active internet connection.
  - No display of torrents with 0 seeds or rating below 1.
  - Monthly safety review of all websites in database.
  - Legal review required before public release.

- **Undecided issues**:
  - Specific communication protocols (PHP or others).
  - Full list of supported websites beyond examples.
  - Detailed parental control implementation.
  - Handling of region-restricted streaming content.
  - Not mentioned.