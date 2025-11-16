# GParted Software Requirements Specification

## 1. Introduction

### 1.1 Purpose
This document describes and defines the functional requirements of the GParted application, following the IEEE standard for Software Requirements Specification documents. GParted is a graphical partition editor for creating, reorganizing, and deleting disk partitions, also known as the Gnome Partition Editor. It is a frontend to the GNU Parted partition editor, using its library libparted to detect and manipulate devices and partition tables.

### 1.2 Project Scope
GParted deals with two different versions:
- GParted install version: Resides permanently on a computer's hard drive as a program installed on a Linux operating system
- GParted Live: A .zip or .iso file that can be burned as an image on a CD or used to create a bootable USB flash drive

GParted uses GNU Parted as a backend and aims to keep the GUI as simple as possible. It supports creating partition tables (e.g., msdos, gpt), enabling and disabling partition flags (e.g., boot, hidden), and performing actions with partitions such as create, delete, resize, move (while preserving data), check, label, copy and paste. It supports file systems such as ext2/ext3/ext4, FAT16/FAT32, hfs/hfs+, linux-swap, NTFS, reiserfs/4, ufs, xfs.

## 2. Overall Description

### 2.1 Product Perspective
GParted is a program for manipulating disk partitions, supporting more file systems and providing more functions than similar tools. It is written in C++ and based on the Debian GNU/Linux operating system. It uses GNU libparted to detect and manipulate devices and partition tables, and several optional file system tools provide support for file systems not included in libparted.

### 2.2 User Classes
- Casual Users: Basic understanding of computers and disk partitions required
- Developers: Interested in improving the application and contributing to the GParted community
- Testers: Use beta versions to test for bugs and errors
- Documentation Writers: Use this document to assist in documenting program functions

### 2.3 Operating Environment
GParted is developed on x86 based computers using GNU/Linux and can be used on other operating systems by booting from media containing GParted Live. The Live version requires a basic x86 computer with a CD drive and/or USB port.

### 2.4 Design and Implementation Constraints
The program does not support every kind of operation on every file system but is constantly being updated. GParted does not currently support logical volume management (LVM2), although this feature has been requested and may be implemented in a future release.

## 3. System Features

### 3.1 Boot Menu
After booting with GParted Live, the first screen presents various modes including default, loading to RAM only, safe graphic settings, failsafe mode, and options to boot the computer's operating system or run RAM tests using Memtest86+.

### 3.2 Select Keymap
The keymap is the layout of symbols on the keyboard. Different keymaps are supported with the default option (don't touch keymap) being recommended.

### 3.3 Language Selection Menu
Supports a wide variety of languages. Users enter the number corresponding to their desired language, followed by a video mode preference menu.

### 3.4 GParted Desktop
The desktop contains all program functions including:
- Exit to quit
- Take screenshots of desktop or windows
- Open terminal
- Open main GParted window
- Find information about GParted and its packages
- Launch screen resolution application

### 3.5 GParted Main Window
Contains a menu bar (GParted, Edit, View, Device, Partition) and a bar with common functions. Shows a graphical representation of the selected drive's partitions and a detailed list.

### 3.6 Refresh Connected Devices
From GParted->Refresh Devices, users can refresh the list of connected devices, useful when plugging in USB drives after GParted has booted.

### 3.7 Undo & Apply
Operations go into pending mode. Users can undo or apply changes through Edit->Undo Last Operation, Clear All Operations, Apply All Operations, or respective buttons on the main functions bar.

### 3.8 View Device Information
View->Device Information displays details about the selected device including model, size, heads, sectors, cylinders, etc.

### 3.9 Create Partition Table
Device->Create Partition Table lets users create the drive's partition table. A warning indicates all data will be erased.

### 3.10 Create a New Partition
Users select the desired device, then click New from the main functions bar or Partition->New. A dialog appears with options for size, position, partition type (Primary, Logical, Extended), file system, and labeling.

### 3.11 Delete a Partition
Select the partition and press Delete on the main functions bar or Partition->Delete. No warning dialog appears, but Apply is required for changes to take effect.

### 3.12 Resize or Move a Partition
Select the partition and click Resize/Move from the main functions bar or Partition->Resize/Move. A dialog with a slider for size and position appears.

### 3.13 Copy Partition
Select the partition and click Copy from the functions bar or Partition->Copy. The selected partition is copied to the clipboard for cloning purposes.

### 3.14 Paste Partition
Paste the copied partition to unallocated space of the same drive, another drive, or unallocated space of another drive. A dialog window opens with a slider for positioning and sizing.

### 3.15 Format Partition
Select the partition and click Partition->Format to. A list of supported file systems appears for selection.

### 3.16 Unmount Partition
Click Partition->Unmount to unmount a partition from its mount point.

### 3.17 Manage Flags
Select a partition and click Partition->Manage Flags to access a dialog with flags and checkboxes for partition functions like bootable or hidden status.

### 3.18 Check and Repair File System
Select a partition and click Partition->Check to send the check and repair operation to pending mode. Apply to analyze, check for errors, and repair the file system.

### 3.19 Label Partition
Select a partition and click Partition->Label to open a dialog for naming the partition. Not all file systems support labeling.

### 3.20 Take a Screenshot
Click Screenshot on the desktop to take screenshots of the desktop or active windows. Cross-pointer appears for selection.

### 3.21 Terminal & Mount Partitions
Launch a command line utility through Terminal for advanced operations or mounting partitions to mount points. Also used for copying screenshots from the system's virtual drive to physical storage.

### 3.22 Information
Click Info for a dialog with options for List of packages or Windows Information. The first opens a list of packages and libraries, while the second shows resize considerations for Windows XP and Vista partitions.

### 3.23 Screen Resolution Changer
Click Screen resolution for monitor or resolution options including resolution selection, rotation, and layout changes for multiple monitors.

### 3.24 Date and Time
Date and time are displayed on the desktop's taskbar, read from the computer's BIOS.

## 4. External Interface Requirements

### 4.1 User Interfaces
Main menu is the first screen where most operations occur, with a menu bar (GParted, Edit, View, Device, Partition) and common function bar. Selected drive's partitions are presented graphically and in detail. Confirmation dialogs warn about potential data loss with Cancel and Apply options.

### 4.2 Hardware Interfaces
Requires a PC (Windows or Linux) or Mac with or without an operating system. Needs a CD/DVD drive or USB port, and functional keyboard and mouse. Supports hard disks, USB flash drives, external hard drives, and IDE/SATA/RAID controllers.

### 4.3 Software Interfaces
GParted Live runs on every system without specific software requirements. Depends on libraries and tools pre-included in the .iso image, including Parted >= 1.7.1, Gtkmm >= 2.8.x, and various file system tools.

### 4.4 Communications Interfaces
Network communication is available through Terminal commands (ifconfig, route, dhclient eth0). Editing /etc/resolve.conf enables updating and adding new packages to GParted.

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements
Not a resource-hungry program that runs on most systems without problems. Functions are not computationally intensive. Requires only a working CD/DVD drive or USB port. Loads and runs quickly.

### 5.2 Safety Requirements
Data loss is a serious possibility if not careful. Users should back up data and use the program with extreme caution. When dealing with partition changes, human or application error could result in complete data loss. GParted comes with no warranty.

### 5.3 Security Requirements
GParted Live does not deal with security or privacy issues as it does not run within an operating system. All users have administrator rights and full access as root from program start.

### 5.4 Software Quality Attributes
Provides a friendly user interface with operations accessible from menu bar and main toolbar. Average or casual users should not find problems using main functions. Interoperability is guaranteed as it runs on both Mac and PC (Linux, Windows, or other OS).

### 5.5 Other Requirements
GParted is free software under GNU General Public License version 2 or later. Users have the freedom to run, copy, distribute, study, change, and improve GParted without payment.
