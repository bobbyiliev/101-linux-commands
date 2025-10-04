# The `history` command

The `history` command displays a list of previously executed commands from your current shell session and past sessions. This allows you to review, search, and re-execute commands without retyping them.

### Command Syntax

```bash
history [options] [n]
```

### How History Works

Your command history is stored in a file in your home directory:
- **Bash**: `~/.bash_history`
- **Zsh**: `~/.zsh_history`

The number of commands stored is controlled by shell variables:
- `HISTSIZE`: Maximum number of commands to keep in memory during a session
- `HISTFILESIZE`: Maximum number of commands to keep in the history file

You can check these values with:
```bash
echo $HISTSIZE
echo $HISTFILESIZE
```

### Common Options

- `history n` - Display the last `n` commands
- `history -c` - Clear the history list (current session only)
- `history -d offset` - Delete the history entry at position `offset`
- `history -a` - Append new history lines to the history file
- `history -w` - Write the current history to the history file

### Examples

**1. Display your full command history:**
```bash
history
```

**2. Show only the last 10 commands:**
```bash
history 10
```

**3. Search for specific commands in your history:**
```bash
history | grep artisan
history | grep git
history | grep docker
```

**4. Execute a command by its history number:**
```bash
!123
```
This re-runs the command at position 123 in your history.

**5. Execute the most recent command starting with a specific string:**
```bash
!git
```
This runs the most recent command that started with "git".

**6. Execute the previous command:**
```bash
!!
```

**7. Execute the previous command with sudo:**
```bash
sudo !!
```

**8. Reuse arguments from the previous command:**
```bash
# If you ran: cat /var/log/syslog
# You can use the last argument with:
vim !$
# This runs: vim /var/log/syslog
```

**9. Clear your command history:**
```bash
history -c
```

**10. Delete a specific entry from history:**
```bash
history -d 456
```

### Reverse Search (Ctrl+R)

One of the most powerful features is **reverse incremental search**:

1. Press `Ctrl+R`
2. Start typing part of a command
3. The most recent matching command appears
4. Press `Ctrl+R` again to cycle through older matches
5. Press `Enter` to execute, or `Esc` to edit the command

### History Control Variables

You can customize history behavior using these variables in your `~/.bashrc` or `~/.zshrc`:

```bash
# Increase history size
export HISTSIZE=10000
export HISTFILESIZE=20000

# Ignore duplicate commands
export HISTCONTROL=ignoredups

# Ignore commands starting with a space
export HISTCONTROL=ignorespace

# Combine both options
export HISTCONTROL=ignoreboth

# Ignore specific commands from being saved
export HISTIGNORE="ls:cd:pwd:exit:history"

# Add timestamps to history
export HISTTIMEFORMAT="%Y-%m-%d %H:%M:%S "
```

### Security Considerations

**Preventing sensitive commands from being saved:**

1. **Prefix with a space** (if `HISTCONTROL=ignorespace` is set):
```bash
 mysql -u root -p
```

2. **Temporarily disable history:**
```bash
set +o history
# Run sensitive commands here
set -o history
```

3. **Remove specific entries:**
```bash
history -d <line_number>
```

4. **Clear history before logging out:**
```bash
history -c && history -w
```

### Practical Use Cases

- **Debugging**: Review the sequence of commands that led to an error
- **Documentation**: Copy command sequences for scripts or documentation
- **Efficiency**: Quickly re-execute complex commands without retyping
- **Learning**: Review commands used by others when sharing a system (in appropriate contexts)
- **Audit trail**: Track what commands were executed and when (with timestamps enabled)