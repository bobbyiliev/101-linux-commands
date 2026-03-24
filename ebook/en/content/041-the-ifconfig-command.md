# The `ifconfig` command

`ifconfig` is used to configure the kernel-resident network interfaces.  It is used at boot time to set up interfaces as necessary.  After that, it is usually only needed when debugging or when system tuning is needed.


If no arguments are given, `ifconfig` displays the status of the currently active interfaces.  If a single interface argument is given, it displays the  status  of the  given interface only; if a single -a argument is given, it displays the status of all interfaces, even those that are down.  Otherwise, it configures an interface.
### Syntax:

```
ifconfig [-v] [-a] [-s] [interface]
ifconfig [-v] interface [aftype] options
```

### Examples:

1. To display the currently active interfaces:

```
ifconfig
```

2. To show all interfaces which are currently active, even if down:

```
ifconfig -a
```

3. To show all the error conditions:

```
ifconfig -v
```

4. To show a short list:

```
ifconfig -s
```

5. To display details of the specific network interface (say `eth0`):
```
ifconfig eth0
```

6. To activate the driver for a interface (say `eth0`):
```
ifconfig eth0 up
```

7. To deactivate the driver for a interface (say `eth0`):
```
ifconfig eth0 down
```

8. To assign a specific IP address to a network interface (say `eth0`):
```
ifconfig eth0 10.10.1.23
```

9. To change MAC(Media Access Control) address of a network interface (say `eth0`):
```
ifconfig eth0 hw ether AA:BB:CC:DD:EE:FF
```
10. To define a netmask for a network interface (say `eth0`):
```
ifconfig eth0 netmask 255.255.255.224
```

11. To enable promiscous mode on a network interface (say `eth0`): 
```
ifconfig eth0 promisc
```
In normal mode, when a packet is received by a network card, it verifies that it belongs to itself. If not, it drops the packet normally. However, in the promiscuous mode, it accepts all the packets that flow through the network card.

12. To disable promiscous mode on a network interface (say `eth0`):
```
ifconfig eth0 -promisc
```

13. To set the maximum transmission unit to a network interface (say `eth0`):
```
ifconfig eth0 mtu 1000
```
The MTU allows you to set the limit size of packets that are transmitted on an interface. The MTU is able to handle a maximum number of octets to an interface in one single transaction.

14. To add additional IP addresses to a network interface, you can configure a network alias to the network interface:
```
ifconfig eth0:0 10.10.1.24
```
Please note that the alias network address is in the same subnet mask of the network interface. For example, if your eth0 network ip address is `10.10.1.23`, then the alias ip address can be `10.10.1.24`. Example of an invalid IP address is `10.10.2.24` since the interface subnet mask is `255.255.255.224`

15. To remove a network alias:
```
ifconfig eth0:0 down
```
Remember that for every scope  (i.e.  same  net  with  address/netmask  combination)  all aliases are deleted, if you delete the first alias.
### Help Command
Run below command to view the complete guide to `ifconfig` command.
```
man ifconfig
```
