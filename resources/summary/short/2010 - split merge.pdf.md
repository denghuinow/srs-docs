# Short Summary: PDF Split and Merge (v2.1.0)

## Background and objectives
PDF Split and Merge (PDFsam) is a free, open-source tool designed to provide an easy and efficient way to manipulate PDF files through a simple graphical interface and command-line console. Its objective is to offer comprehensive PDF handling capabilities—such as splitting, merging, and page manipulation—without cost, filling a gap in the market for feature-rich, accessible PDF software.

## In scope
- Splitting PDF documents by pages, size, or bookmarks.
- Merging multiple PDFs or extracting specific page ranges.
- Visually reordering, rotating, and composing pages via a graphical interface.
- Saving and loading the working environment to automate repetitive tasks.
- Providing both a GUI (with plugin-based features) and a command-line console.

## Out of scope
- Editing PDF content (e.g., text or image modification).
- Web-based or network collaboration features.
- Advanced security features like encryption or digital signatures.
- Integration with other document formats (e.g., Word, Excel).
- Real-time collaboration or cloud storage integration.

## Stakeholders and core use cases
**Stakeholders:**
- **General Users:** Individuals needing to manipulate PDFs for personal or professional tasks.
- **Open Source Developers:** Contributors extending or modifying the software's source code.
- **Translators:** Volunteers localizing the application into different languages.
- **Testers:** Professionals validating functionality against requirements.
- **End Users:** Individuals using the application for PDF manipulation.

**Core Use Cases:**
1. As a general user, I want to split a PDF by bookmarks so that I can separate chapters easily.
2. As a general user, I want to merge selected pages from multiple PDFs so that I can create a single document.
3. As a general user, I want to visually reorder and rotate pages so that I can customize document layout intuitively.
4. As a general user, I want to save my working environment so that I can automate repetitive PDF tasks.
5. As a developer, I want to access the console for batch processing so that I can handle large files efficiently.
6. As a user, I want to view log messages so that I can troubleshoot operations.

## Success metrics
- Support for all listed PDF manipulation features (split, merge, rotate, etc.) without errors.
- Compatibility across major platforms (Windows, Linux, Mac OS X) via Java JVM 1.6+.
- User satisfaction with the GUI's ease of use and responsiveness for common tasks.

## Major constraints
- Requires Java Runtime Environment version 1.6 or higher.
- Maximum memory usage capped at 254MB by default (adjustable for large files).
- Licensed under GNU GPLv2, enforcing open-source distribution terms.
- GUI built with Java Swing, limiting UI development to this framework.
- Output file compression requires PDF version 1.5 or above.

## Undecided issues
- Potential expansion of supported input formats beyond PDF.
- Implementation of additional advanced features for the enhanced version.
- Localization updates and addition of new languages.
- Optimization strategies for handling extremely large PDF files.
- Integration with external tools or plugins.