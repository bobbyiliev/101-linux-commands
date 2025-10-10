# The ifplugstatus Command

The `ifplugstatus` command is a diagnostic utility used to check the **physical link status** of network interfaces on Linux systems. It reports whether an interface (such as eth0, enp0s3, or wlan0) has a network cable connected or not. This tool is particularly useful for troubleshooting wired network connectivity and detecting unplugged cables.

## Syntax
```bash
ifplugstatus [options] [interface]
```
### Parameters

- interface — the network interface to check (e.g., eth0, enp0s3, wlan0).

- options — optional flags for customizing output.

## Installation

`ifplugstatus` is part of the `ifplugd` package.
It can be installed using the following commands depending on your distribution:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ifplugd

# CentOS/RHEL/Fedora
sudo yum install ifplugd
# or
sudo dnf install ifplugd
```
### To verify installation:
```bash
which ifplugstatus
```

##  Basic Usage

### 1. Check the status of a single interface
```bash
ifplugstatus eth0
```
### Sample Output:
```bash
eth0: link beat detected
```
### or
```bash
eth0: link beat not detected
```
### Explanation:

- link beat detected → cable is plugged in and active.

- link beat not detected → cable is unplugged or inactive.
*Note: 'link beat' is a legacy term from older Ethernet (10/100 Mbps). Modern Gigabit or higher interfaces may use different link detection signals, but the command generally reports an active physical link.*

### 2. Check multiple interfaces
```bash
ifplugstatus eth0 wlan0
```
### Sample Output:
```bash
eth0: link beat detected
wlan0: link beat not detected
```
This allows quick verification of all available interfaces.


## Options
Some popular option flags include:
| Option | Description |
|--------|-------------|
| `-a`   | Show all interfaces (default behavior). |
| `-i`   | Specify a particular interface. |
| `-s`   | Display a short summary only. |
| `-v`   | Verbose output with more details. |
| `-q`   | Quiet mode — minimal output. |
| `-h`   | Display help information. |


## Practical Examples
### 1. Check if the main Ethernet interface is connected
```bash
ifplugstatus eth0
```
Displays the current cable connection status for eth0.

### 2. Check all available network interfaces
```bash
ifplugstatus -a
```
Lists link status for every detected interface.

### 3. Use verbose mode for detailed results
```bash
ifplugstatus -v eth0
```
Provides more descriptive information about the link state.

### 4. Quiet mode for scripting or automation
```bash
ifplugstatus -q eth0
```
Outputs only the essential information, suitable for shell scripts.

## Understanding the Output

A typical output may look like this:
```bash
eth0: link beat detected
enp0s3: link beat not detected
```
- Interface Name: eth0, enp0s3, etc.

- Link Status: Indicates whether a physical link (cable or signal) is present.

When integrated into scripts, this helps automate detection of disconnected interfaces or faulty cabling.


## Common Use Cases
### 1. Cable Connectivity Testing
```bash
ifplugstatus eth0
```
Quickly verify if a cable is physically connected to the network port.

### 2. Multi-Interface Monitoring
```bash
ifplugstatus eth0 wlan0
```
Check multiple interfaces simultaneously for link activity.

### 3. Continuous Monitoring
```bash
watch -n 5 ifplugstatus eth0
```
Updates the interface status every 5 seconds for real-time link monitoring.


## Troubleshooting Common Issues
### 1. Interface Not Found
If an incorrect interface name is given:
```bash
eth5: No such device
```
**Fix:** Use the ip a or ifconfig command to list valid interfaces.

### 2. Permission Denied

Some systems may require elevated privileges:
```bash
sudo ifplugstatus eth0
```
### 3. Command Not Found

If the command is missing:
```bash
 ifplugstatus: command not found
```
**Fix:** Install the ifplugd package using your package manager. 

**Tip:** Always ensure the ifplugd package is installed and your user has permission to access network interfaces.


## Related Commands

| Command               | Description                                           |
|-----------------------|-------------------------------------------------------|
| `ip a` (preferred) / `ifconfig` | Display all network interfaces and details. `ip a` is the modern tool; `ifconfig` is legacy. |
| `ethtool eth0`        | Retrieve advanced information about the network interface. |
| `nmcli device status` | Check connection status via NetworkManager.          |
| `ping`                | Test network reachability after confirming cable connection. |

## Important Notes

- Works best with wired Ethernet interfaces.

- Wireless interfaces may not always report link status accurately.

- The tool is read-only — it does not modify system settings.

- Lightweight and safe for use in both desktop and server environments.

## Manual Reference

For additional information and advanced usage:

```bash
man ifplugstatus
```