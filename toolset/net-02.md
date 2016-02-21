+++
date = "2016-01-06"
draft = true 
weight = 10
title = "Lab 10 - Networking Tools"
+++

### Lab Objective

The objective of this lab is to introduce and demonstrate the use of various networking tools for moving and syncing files and network connectivity. 

#### 1. File Transfer Protocol

0. Skim the `ftp` man page

    `$` `man ftp`

0. Connect to an anonymous ftp server
  
    `$` `ftp ftp://speedtest.tele2.net`

  ```
  ftp> ?
  ftp> dir
  ftp> ls
  ftp> get 512KB.zip aaa
  ftp> cd upload
  ftp> put aaa aaa
  ftp> exit
  ```

#### 2. Secure FTP

0. Skim the `sftp` man page

    `$` `man sftp`

0. Connect to the ubuntu user sftp server

    `$` `sftp ubuntu@192.168.210.220`

#### 3. Secure Copy

0. Skim the `scp` man page

    `$` `man scp`

0. Connect to the ubuntu server

    `$` `scp ubuntu@192.168.210.220:nandcat.png .`

#### 4. rsync

0. Skim the `rsync` man page

    `$` `man rsync`

0. Connect to the ubuntu server

    `$` `rsync ubuntu@192.168.210.220:~ .`

#### 5. netcat

0. Read the `nc` man page

    `$` `nc scp`

0. Connect to the ubuntu server and setup a nc server
