+++
date = "2016-01-06"
draft = true
weight = 100
title = "Lab 01 - Networking Configuration"
+++

### Lab Objective

The objective of this lab is to introduce network configuration and status monitoring.

#### 1. net-tools
Most unix-like systems come with a suite of networking tools outside of the coreutils loosely named net-tools.  These include: `ifconfig`, `arp`, `netstat`, and `route`

These tools are important to be familiar with in order to configure networking interfaces, show status of existing network connections, and manage routing and link layer tables.


#### 2. iproute2
Linux has deprecated the net-tools and has replicated the functionality provided by several of these utilities in the new iproute2 tool suite.  The motivation for this rewrite was the need to incorporate new routing and tunneling configurations without adding additional complexities on to existing tools.  Additionally Linux reworked the entire networking stack after kernel version 2.2 and took advantage of this rewrite to improve upon the tools.

#### Sources: 

* https://dougvitale.wordpress.com/2011/12/21/deprecated-linux-networking-commands-and-their-replacements/
* https://www.tty1.net/blog/2010/ifconfig-ip-comparison_en.html
* http://lartc.org/howto/lartc.iproute2.html
* http://serverfault.com/questions/458628/should-i-quit-using-ifconfig
