Linux Networking  
================

Networking in Linux is modeled after the OSI stack model. more stuff and explanation must needs go here_______________________________________________________d_

# Networking Commands  

## Ifconfig

`ifconfig` has been deprecated in favor of `ip` because it has not been maintained for several years on Linux distributions (however, it is still active on \*BSD implementations). Despite this lack of development, it is still ubiquitous and a necessary fallback in the event that a system does not have `ip` (as in a default install of ArchLinux).

> `ifconfig -a`					:	view all configured NICs on the system.  
> `ifconfig <iface> [up|down]`	:	given without the `up` or `down`, displays information only for the specified interface. The options allows bringing the interface up or taking it down.  
> `ifconfig <iface> <ip> netmask <netmask>` :	sets the IP address of the selected interface.  
> `ifconfig <iface> promisc`				:	sets the interface to promiscous mode. Promiscous mode allows a NIC to process all packets instead of solely the ones addressed to itself.  
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

## Arp

This command allows the user to view known devices on the local network. `arp` queries */proc..................................* in order to retrieve the information for the ARP tables. Note that ipv6 obsoletes the ARP protocol. The ARP table entries in Linux are marked as valid for up to 45 seconds by default.

> `arp -an`					:	displays the ARP table without attempting to resolve DNS names.  
> `cat /proc/............`	:	displays the contents of the table directly.  

# Networking Files

## Hosts

## Resolver

## TCP Slow Start

Linux has a setting that enables compatibility across a higher number of networks via its *tcp_slow_start* option.

# Network Security  
