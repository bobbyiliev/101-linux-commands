# The `nmtui` Command

The **`nmtui`** (Network Manager Text User Interface) command is a **menu-driven tool** for configuring network connections in Linux.  
It provides a simple, text-based interface to manage network settings such as Wi-Fi, Ethernet, hostname, and more — without using complex command-line options.

---

### 🔹 What it Does

`nmtui` allows you to:
- View and edit **network connections**
- **Activate or deactivate** interfaces
- **Set or change** the system **hostname**
- Connect to **Wi-Fi networks**
- Manage **IPv4 / IPv6 settings**

It is especially useful on servers or systems **without a graphical desktop environment**.

---

### 🧠 Syntax

nmtui [OPTION]

---

### 🖥️ Examples

1. **Open the main menu interface:**

   nmtui  
   Opens the main TUI (text user interface) window with options to *Edit a connection*, *Activate a connection*, or *Set system hostname*.

2. **Directly edit a network connection:**

   nmtui edit  
   Lets you create, modify, or delete network connections (both Ethernet and Wi-Fi).

3. **Directly activate or deactivate connections:**

   nmtui connect  
   Opens the *Activate a connection* menu where you can enable or disable network interfaces.

4. **Set or change the system hostname:**

   nmtui hostname  
   Opens a dialog box to set your system’s hostname (used for identification on a network).

5. **Connect directly to a specific Wi-Fi network:**

   nmtui connect "MyWiFiNetwork"  
   Connects to the specified Wi-Fi network if it exists in range.

6. **Quit the interface:**  
   Simply use **Tab → Quit** or press **Esc**.

---

### 🧩 Common Options and Subcommands

| **Command** | **Description** |
|:-------------|:----------------|
| `nmtui` | Launches the interactive main menu |
| `nmtui edit` | Opens the “Edit a connection” screen |
| `nmtui connect` | Opens the “Activate a connection” screen |
| `nmtui hostname` | Opens the “Set system hostname” dialog |
| `nmtui connect <SSID>` | Connects to a specific Wi-Fi network directly |
| `nmtui help` | Displays basic usage help |

---

### ⚙️ Interface Navigation

- Use the **arrow keys** or **Tab** to move between fields.  
- Press **Enter** to select.  
- Use **Spacebar** to toggle checkboxes or options.  
- Press **Esc** or select **Quit** to exit safely.

---

### 📡 Common Use Cases

**1. Configure a static IP address:**

nmtui edit  
→ Choose your Ethernet connection  
→ Set “IPv4 CONFIGURATION” to *Manual*  
→ Enter IP, Gateway, and DNS  
→ Save → Activate connection  

---

**2. Connect to Wi-Fi from terminal:**

nmtui connect  
→ Select your wireless interface  
→ Choose the SSID  
→ Enter the password  
→ Activate connection  

---

**3. Change the hostname:**

nmtui hostname  
→ Type your new hostname  
→ Confirm and exit  
→ The new hostname will apply immediately.

---

### 🛠 Troubleshooting

| **Issue** | **Possible Solution** |
|:-----------|:----------------------|
| `nmtui` command not found | Install NetworkManager TUI: `sudo apt install network-manager` (Debian/Ubuntu) or `sudo dnf install NetworkManager-tui` (Fedora/RHEL/CentOS) |
| Changes don’t take effect | Restart NetworkManager: `sudo systemctl restart NetworkManager` |
| Interface not showing | Ensure your interface is managed by NetworkManager: check `/etc/NetworkManager/NetworkManager.conf` |
| Wi-Fi missing | Make sure wireless drivers are installed and `nmcli device status` shows the Wi-Fi adapter |

---

### 🧰 Related Commands

| **Command** | **Purpose** |
|:-------------|:------------|
| `nmcli` | Command-line (non-interactive) NetworkManager control |
| `ip addr` | Show IP addresses of all interfaces |
| `ifconfig` | (Deprecated) Interface configuration command |
| `systemctl restart NetworkManager` | Restart NetworkManager service |
| `hostnamectl` | Manage the system hostname directly |

---

### 🧾 Example: Configuring Ethernet via `nmtui`

sudo nmtui  
→ Select **Edit a connection**  
→ Choose **Wired connection 1**  
→ Set IPv4 to **Manual**  
→ Fill in:
Address: 192.168.1.50/24  
Gateway: 192.168.1.1  
DNS: 8.8.8.8  
→ Save → Back → **Activate a connection** → Select **Wired connection 1**  

✅ Your network connection will now use a static IP.

---

### 📘 Notes

- Changes made with `nmtui` are persistent across reboots.  
- Requires **NetworkManager** to be active.  
- `nmtui` provides the same functionality as `nmcli` but in a more user-friendly interface.  
- Perfect for **server environments** or **SSH sessions** where GUI tools are unavailable.
