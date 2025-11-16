# Ultra Short Summary

This document specifies the requirements for porting the Open Watcom GUI library to Linux using the GTK toolkit, focusing on enabling Open Watcom applications to run natively on Linux with a compatible graphical interface.

- **MVP points**: Port core GUI initialization and window creation functions; implement basic dialog and control rendering using GTK widgets; enable text drawing and common UI controls like buttons and lists; support standard window operations such as resize, minimize, and maximize.
- **Key constraints**: GTK does not support Windows/OS/2-style resource files or MDI "Windows in Window" model; the port must handle type conversions for OS-specific handles like HWND; target systems require specific libraries including GTK+, GLib, and Pango.
- **Major risks/undecided issues**: Handling of resource files and string tables is unresolved; the help subsystem integration is not addressed.