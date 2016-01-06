Linux Networking  
================

Networking in Linux is modeled after the TCP/IP model. <-- TODO --> more stuff and explanation must needs go here ------------

# Networking Commands  

## Arp

This command allows the user to view known devices on the local network. `arp` queries */proc/net/arp* in order to retrieve the information for the ARP tables. Note that ipv6 obsoletes the ARP protocol. The ARP table entries in Linux are marked as valid for up to 45 seconds by default.

> `arp -an`				:	displays the ARP table without attempting to resolve DNS names.  
> `less /proc/net/arp`	:	displays the contents of the table directly.  

## Ifconfig

`ifconfig` has been deprecated in favor of `ip` because it has not been maintained for several years on Linux distributions (however, it is still active on \*BSD implementations). Despite this lack of development, it is still ubiquitous and a necessary fallback in the event that a system does not have `ip` (as in a default install of ArchLinux).

> `ifconfig -a`					:	view all configured NICs on the system.  
> `ifconfig <iface> [up|down]`	:	given without the `up` or `down`, displays information only for the specified interface. The options allows bringing the interface up or taking it down.  
> `ifconfig <iface> <ip> netmask <netmask>` :	sets the IP address of the selected interface.  
> `ifconfig <iface> promisc`				:	sets the interface to Promiscuous mode. Promiscuous mode allows a NIC to process all packets instead of solely the ones addressed to itself.  
> `ifconfig <iface> -promisc`				:	disables promiscuous mode on the selected interface.  

## IP

`ip` is part of the *iproute2* suite of tools designed to manage the Linux networking stack. It subsumes many previous commands such as `ifconfig`, `nestat`, and `route`. It does not replace all functionality of each of the tools, so some other commands still remain necessary.  

> `ip addr`								:	shows all NICs on the system.  
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

## Forwarding Packets

## IPTables


# Sources:
- [www.tldp.org](www.tldp.org)  
- [www.computerhope.com](http://www.computerhope.com/)
