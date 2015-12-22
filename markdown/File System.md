<link rel="stylesheet" type="text/css" href="MD_styling.css" />

File Systems and Organization 
=============================

*"Everything is a file."*

If an item is not a file, then it is a process. Some of the "files" have special properties, like most of those under */dev*. The *Linux File System Standard*, or *FSSTND*, describes a standard that organizes compliance structures across Linux distributions. The standards allow a person to understand a new system by understanding the standard. 

For a refresher, run *man hier*.

# 

# Directories

**/bin**
:	consists of programs required in single-user mode. This directory makes the commands available to all users. 

**/boot**
:	static files for the boot process. Only files necessary to boot the device exist in this folder.

**/dev** 
:	consists of devices available to the system. */dev/sda* is often the drive on which the OS is mounted. *diskutil* and *fdisk* can be used to find disk information. 

> diskutil list 	: displays disk information about mounted disks  
> fdisk -l			: displays information about mounted disks  
> df				: displays information about active, non-swap partitions

**/etc**
:	consists of configuration files. Programs will store system-wide configuration information here. Non-traditionally, configuration files may also be found in */usr/etc*. The recommended behavior places configuration files in */etc* or a sub-folder therein, and then links if necessary to */usr/etc*.

**/home**
:	consists of the user home directories, if present. This directory does not always exist, and its organization remains at the discretion of the system administrator. However, many user-based Linux distros will include this directory for simplicity. User-specific programs, configuration, and data reside here. 

**/media**
:	consists of mount points for removable media. CDROMs, DVDs, and USBs should mount here. 

**/mnt**
:	consists of temporary mount points. Network drives and other similar systems receive temporary mount points here. 

**/opt**
:	consists of static files that provide additional functionality. Applications install here in a directory tree, i.e. */opt/WordPerfect/...*. Distributions may not modify or remove packages installed in */opt* without receiving confirmation from the system administrator.

**/proc**
:	is not a directory of the common file conception. */proc* allows direct access to the kernel during run time. Kernel properties can be modified on the fly; processes can be given runtime input. "Files" in this directory act as pointers to the related information. 

> man proc		:	displays detailed information about each aspect in the */proc* directory 

**/root**
:	optional directory for the root user. *root* may not appear in */home* because */home* is not always mounted in all situations (such as in a single-user mode).

**/sbin** 
:	consists of superuser binary programs. These binaries perform system adminstration and require special privileges to run. Only those binaries necessary for "booting, restoring, and/or repairing the system" [FSSTND] should exist in */sbin*.

**/usr**
:	consists of the most amount of data (usually). Programs that operate in user space generally belong here. 

> */usr/include*:	header files for compiling user-space programs.  
> */usr/local*	:	local and 3rd-party programs belong here. This directory is safe from overwrites when updating system software.  
> */usr/share*	:	directory for programs to store information that should not be modified.  
> */usr/src*	:	directory for linux kernel sources, header files, and documentation.

**/tmp**
:	directory for temporary data. Data stored here is not guaranteed to exist after the process ends; indeed, many distros clear this directory during reboots. 

**/var**
:	consists of changing data.

> */var/log*	:	location of log files for most applications and system events.  
> */var/cache*	:	programs may cache data here. Data persistence is not guaranteed, so it can be safely deleted.  
> */var/local*	:	programs in */usr/local* may store variable data here.

Source : www.tldp.org
