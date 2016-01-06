Linux Networking  
================

Networking in Linux is modeled after the TCP/IP model. <-- TODO --> more stuff and explanation must needs go here ------------

# Networking Commands  

## Arp

This command allows the user to view known devices on the local network. `arp` queries */proc/net/arp* in order to retrieve the information for the ARP tables. Note that ipv6 obsoletes the ARP protocol. The ARP table entries in Linux are marked as valid for up to 45 seconds by default.

> `arp -an`				:	displays the ARP table without attempting to resolve DNS names.  
> `less /proc/net/arp`	:	displays the contents of the table directly.  

## DNS

The *Domain Information Groper*, or `dig`, tool displays information for DNS related to the current network. `nslookup` can also provide information about nameservers for the current network.

## Ifconfig

`ifconfig` has been deprecated in favor of `ip` because it has not been maintained for several years on Linux distributions (however, it is still active on \*BSD implementations). Despite this lack of development, it is still ubiquitous and a necessary fallback in the event that a system does not have `ip` (as in a default install of ArchLinux).

> `ifconfig -a`					:	view all configured NICs on the system.  
> `ifconfig <iface> [up|down]`	:	given without the `up` or `down`, displays information only for the specified interface. The options allows bringing the interface up or taking it down.  
> `ifconfig <iface> <ip> netmask <netmask>` :	sets the IP address of the selected interface.  
> `ifconfig <iface> promisc`				:	sets the interface to Promiscuous mode. Promiscuous mode allows a NIC to process all packets instead of solely the ones addressed to itself.  
> `ifconfig <iface> -promisc`				:	disables promiscuous mode on the selected interface.  

## IP

`ip` is part of the *iproute2* suite of tools designed to manage the Linux networking stack. It subsumes many previous commands such as `ifconfig`, `nestat`, and `route`. It does not replace all functionality of each of the tools, so some other commands still remain necessary.  

> `ip addr`								:	shows all NICs on the system, with corresponding network information.  
> `ip link set <iface> [up|down]`		:	enables or disables the given interface.  
> `ip addr [add|del] <CIDR_IP|IP NETMASK> dev <iface>`	:	adds or deletes the given IP address for the specified interface.  
> `ip link set <iface> promisc [on|off]`:	enables or disables promiscuous mode on the given interface.  
> `ip route`							:	shows the routing information for the system.  
> `ip route [add|del] <CIDR dest> via <gateway>`		:	adds or deletes a route to the given destination through the specified gateway.  
> `ip neigh`							:	shows the known neighbors in the network.  

## Netstat

`netstat` displays information about the current network status.

> `netstat`		:	displays open sockets.  
> `netsat -rn`	:	displays information regarding the routing tables.  

## Remote Procedure Call

*Remote Procedure Call* is a protocol that allows a user to remotely execute a command. The configuration for RPC resides in */etc/rpc*, and `rpcinfo` provides information about the running services on a specified host.  

> `rpcinfo`	:	returns information about the RPC information for the current host.  
> `rpcinfo <host>`	: returns information about the RPC information for the given host.  
> `rpcinfo -s`	:	returns information in a more concise manner.

## Web Interaction

For downloading web pages via the command-line, `wget` or `curl` provides the functionality. Both commands can operate autonomously; that is, without user interaction.

### Download a Webpage  
`wget <URL>` 	: saves the webpage to the current working directory.  
`curl <URL>` 	: dumps the raw HTML to `stdout`. Redirect the output to save the file.  
`curl -O <URL>`	: saves the files to the current working directory.  

### Continue a Partial Download  
`wget -c <URL>`		: continues the download from the last position, *if* the file exists in the current working directory.  
`curl -C - -O <URL>`: continues the download from the last position, *if* the file exists in the current working directory. The `-` after `-C` instructs `curl` to use the provided file names as the byte offset.

# Networking Files

## Hosts

This file associates IP addresses with hostnames. Often, DNS supersedes this file.

## Resolver

`/etc/resolv.conf` contains the nameserver addresses to use when determining domain names.

## TCP Slow Start

Linux has a setting that enables compatibility across a higher number of networks via its *tcp_slow_start_after_idle* option.

# Network Security  

## Capturing Packets

By default, a NIC makes available only those packets addressed to itself. Promiscuous mode allows the user to work with all the packets seen by the NIC.

> `wireshark`	: 	graphical packet analyzer.  [Wireshark](https://www.wireshark.org/) allows the user to write a custom protocol analyzer and allows protocols to be pieced back together at the application layer.  
> `tcpdump`		: 	command-line packet displayer that allows the user to save a packet dump file. `tcpdump` is generally installed by default, and serves as a network debugging tool.  

## IPTables

The Linux firewall originally started as `ipchains`. Due to several shortcomings, it was rewritten as `iptables`. `iptables` provides stateful packet filtering, improved speed, proxy integration, and several other features. The configuration file exists at */etc/sysconfig/iptables*. To allow the system to support packet forwarding, the value of */proc/sys/net/ipv4/ip_forward* must change to **1**.

The firewall uses up to 5 different tables when processing packets. The available tables depend on the kernel configuration. The three most commonly used have been emphasized.  

| Table        | Purpose        
|:-------------|:--------------------------------------------------
| *Filter*     | Determines how to handle the packet
| *Mangle*     | Sets the QOS header bits
| *NAT*        | Modifies the addressing of the packet  
| Raw          | used for configuring exemptions; called before any other table  
| Security     | sets MAC or DAC after the filer table

------

#### IPTABLES Logical Layout

```
+---------------------------+
|          Table            |
|  +---------------------+  |
|  |       Chain         |  |
|  |  +---------------+  |  |
|  |  | Rule 1        |  |  |
|  |  | Rule 2        |  |  |
|  |  | ...           |  |  |
|  |  | Rule n        |  |  |
|  |  +---------------+  |  |
|  +---------------------+  |
+---------------------------+
```

### Data Flow of a Packet

![IPTABLES Data Flow](http://www.linuxhomenetworking.com/wiki/images/f/f0/Iptables.gif)  
Image courtesy of [www.linuxhomenetworking.com](http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch14_:_Linux_Firewalls_Using_iptables).

------

Each packet enters the firewall for processing. At each step, the firewall checks if the packet matches a target; if so, it gets handled according to that target. The process continues until the packet leaves the firewall, or until a rule drops the packet. By default, many of the kernel modules for the firewall are not loaded. The user must manually load the required modules for full operation.   
`iptables` allows rules to be specified either on the command-line or in a file. For file inputs, use `iptables-restore < <file>` to update the ruleset according to the given file. To save the current configuration to a file, use `iptables-save > <file>`.

### Common Commands  

> `iptables -N <chain>`	:	create a new chain rule.  
> `iptables -A <chain>`	:	append to a chain rule.  
> `iptables -C <chain>`	:	check for the existence of a rule.  
> `iptables -D <chain> <num>`	:	delete the given rule from the chain. `num` is a 1-indexed number determining which rule from the chain to delete.    
> `iptables -F [chain]`			:	delete the rules from the given chain, or delete all rules.  
> `iptables -X [chain]`			:	delete the given chain. With no argument, all non-default chains are deleted.  
> `iptables -I <chain> [num]`	:	insert a rule at the index, with a default of 1.  
> `iptables -R <chain> <num>`	:	replace the given rule from the chain.  
> `iptables -[L|S] [chain [num]]`	:	list the rules. Lists all rules if nothing is specified, or lists the rules in the specified chain.  

------

### Understanding a Chain

In general, firewalls are configured to allow only desired connections. Many firewalls block anything not explicitly allowed with an implicit deny rule. By default, `iptables` allows all connections.

The default table when appending a new rule is the *FILTER* table. Common chains for this table include *OUTPUT*, *FILTER*, and *FORWARD*. When a packet matches a rule, a `-j` can specify a target for the packet. A table of common targets exists at [www.linuxhomenetworking.com](http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch14_:_Linux_Firewalls_Using_iptables#Table_14-2_Descriptions_Of_The_Most_Commonly_Used_Targets).

```
	iptables -A OUTPUT -j DROP -s 192.168.2.31
```
> `-A OUTPUT`	:	this rule is being appended to the *OUTPUT* chain of the default table (*FILTER*). The *OUTPUT* chain handles packets leaving the system.  
> `-j DROP`		:	on a match, the packet jumps to the *DROP* target. This target stops processing a packet and drops it.    
> `-s 192.168.2.31`	:	any packet with a source address of *192.168.2.31* matches this rule.  

Note that additional matching options provide much more specific control over particular packets. Use `man iptables` to view additional parameters for specifying packets at a more granular level. 

# Sources:
- [www.tldp.org](www.tldp.org)  
- [www.computerhope.com](http://www.computerhope.com/)  
- [www.linuxhomenetworking.com](http://www.linuxhomenetworking.com/)
