<link rel="stylesheet" type="text/css" href="MD_styling.css" />

VIM  
========

*VIM* is a command-line text editor that varies from *nano* and *emacs* in its presentation. Based on *Vi*, a text editor for Unix systems, *VIM* runs on all systems with the standard *c* library. For the simplest use cases, *Vi* and *VIM* interact in the same manner, although *Vi* is required for a system to be POSIX compliant. Configuration for *VIM* can be placed in `~/.vimrc`; this allows users to create a deep level of customization.

*VIM* operates in three modes. Command Mode and Insert Mode it shares with *Vi*; *VIM* also offers Visual Mode for mouse interaction. Another improvement offered by *VIM* is the syntax highlighting: it will color code keywords or phrases if the file extension is recognized.  Use `vim <file>` to start editing a file.

# Command Mode

*VIM* starts in Command Mode, in which the user issues commands to perform some action. Key presses take on a particular meaning. `j` and `k` control vertical movement; `h` and `l` control horizontal movement; use `w` to jump forward by words. To enter a command, the user types `:<command>`. The `:` informs *VIM* that a particular command is about to be run. To get back to Command Mode, use the `escape` key. 

> `:w`			:	writes the current file to disk.  
> `:q`			:	quits the program.  
> `:q!`			:	quits the program, ignoring any errors that may have occurred such as unsaved changes or no write permissions.  
> `:wq`			:	writes the active file, and then exits the program.  
> `:wa`			:	writes all active, changed files.  
> `:e <file>`	:	edits  a different file without closing the program by opening a new buffer in which to hold the new file.  
> `:bd`			:	closes the currently active file. Files in *VIM* are referred to as "buffers", hence the "b". The command stands for "buffer delete".  
> `:bn`			:	goes to the next open file (buffer).  
> `:dd`			:	deletes the line under the cursor. The line is placed in the paste register.  
> `:p`			:	paste the contents of the paste register.  

# Insert Mode

Use `i` to enter Insert Mode at the current character; use `A` to enter Insert Mode at the end of the current line. Insert Mode allows the user to enter text into the active buffer. To return to Command Mode, use `escape`. 

> `C-x C-n`	:	auto-suggest a word to complete after typing a few characters. Use `C-n` to select the next suggestion.  
