Purpose & Scope  
GParted is a LiveCD-based disk partitioning tool that creates, modifies, and deletes partitions without installation. It operates entirely in RAM, disappearing after reboot. Excludes LVM support, data recovery guarantees, and direct OS installation.  

Product Background / Positioning  
Serves as a graphical frontend to GNU Parted, targeting Linux users seeking a simple partition management solution. Runs independently of host OS via LiveCD/USB, replacing command-line tools like Parted. Integrates with existing Linux ecosystems but requires no host OS dependencies.  

Core Functional Overview  
Create/delete partitions; resize/move partitions (data-preserving); copy/paste partitions; format partitions; check/repair file systems; manage partition flags (e.g., bootable).  

Key Users & Usage Scenarios  
Casual users (primary): Perform basic partitioning tasks via GUI. Developers/testers: Contribute to code/testing (root access). All users operate as root in LiveCD mode; no permission tiers.  

Major External Interfaces  
GUI interfaces (main window, dialogs, menus). Hardware interfaces (USB/CD drives for boot, standard storage devices). Software interfaces (libparted dependency for core functions).  

Key Non-functional Requirements  
Runs on standard x86 hardware without high resource demands. No data recovery capability; data loss possible during operations. Requires CD/USB boot media for Live version.  

Constraints, Assumptions & Dependencies  
Requires CD/DVD drive or USB port for boot. Depends on libparted library and OS-specific file system tools. Explicitly excludes LVM support.  

Priorities & Acceptance Approach  
Highest priority: Prevent data loss during operations. Acceptance: All core partitioning functions (create/delete/resize) must work as documented; LVM exclusion must be unambiguous.