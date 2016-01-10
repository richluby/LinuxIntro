Linux Fundamentals
=====================

This project aims to provide fundamental knowledge for a person new to the Linux environment. 

# Organization

The organization of the project is folder based. The course material, written in markdown, exists in the *markdown* directory. Built files ready for distribution belong in the *dist* folder. The *buildMDToC.py* creates a table of contents for a markdown file based on the heading markers. 

# Course Module Structure

Each module consists of three parts. The first portion provides the lecture and basic knowledge behind the topic; when practical, it also provides a live demonstration. The second portion gives students a task to accomplish as the instructor provides real-time feedback to students with questions or problems. The final part of a module gives students a task that incorporates the main topic and encourages critical thinking skills, ideally without instructor assistance.

# Table of Contents

* Unix, POSIX, Linux and more
* coreutils
* Command Line Interface
* Navigation
* File creation & viewing
* File permissions
* Users and Groups
* Networking Configuration
* Packet Capture
* Networking Tools
* Remote Shells
* SSH Tunneling
* Bonus

# Running

`hugo server --theme=angels-ladder -w --baseUrl="http://192.168.210.220:80" --bind="192.168.210.220" --pluralizeListTitles=false --port=80`

