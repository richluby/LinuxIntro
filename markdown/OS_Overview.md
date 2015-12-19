UNIX Context and Overview
=========================

The Linux architecture is originally based on the UNIX system produced by AT&T. Due to the licensing of the original codebase, Linus Torvalds began creating his own OS to run on personal hardware. Gradually, the system attracted fellow developers and gained traction in the CS community. 

# Structure of the Linux OS

There exist 3 major portions of a Linux Operating System.

~~~

----------------------------------------------------------------
|                          User Space                          |
|                    |---------------------|                   |
---------------------|        SCI          |--------------------
|                    |---------------------|                   |
|                                                              |
|                         Kernel Space                         |
----------------------------------------------------------------

~~~

**User Space**
:	Contains the user-level applications. This space has its allowed actions restricted in order to prevent harm to the system.

**System Call Interface (SCI)** 
:	Forms the bridge between user and kernel space. When an application wishes to read/write a file, the call goes to the SCI. The SCI then handles the communication channel between the two spaces.

**Kernel Space**
:	Contains the linux kernel, and will receive more coverage next. In short, it serves as the operating system and interfaces between the user space and the hardware. 

## Kernel Space

The kernel space has several subsystems that comprise its operations. The primary architecture of the kernel allows it to be ported to a wide variety of hardware systems. The kernel code for handling general OS functions is separated from the code that interfaces with the hardware of a system. This allows the underlying hardware-specific code to be modified, while leaving most the OS functions untouched.

The kernel handles several different aspects related to operating a computer.

**Processes**
:	The programs running on a given machine. The kernel determines when each process runs on the hardware, and handles killing or creating processes. 

**Memory**
:	RAM Memory is the area given to an active process to hold its data while running. The kernel handles the memory for a process, and attempts to increase the apparent memory through swapping. 

**Virtual File System**
:	The file system is a level of abstraction build to provide a common interface to applications. The interface allows an aplication to focus on the file itself, not on how the file gets read from the disk into memory.

**Network Stack**
:	Networking in Linux is implemented in a manner similar to the protocols themselves. The way an application works with the network is through a stacked interface in much the same way that network protocols encapsulate one another.

**Drivers**
:	Drivers enable the use of hardware peripherals. They permit the OS to speak the same language as a piece of hardware connected to the system.

Source: IBM Developer Works
