<p align="center"><img src="https://raw.githubusercontent.com/bobbyiliev/101-linux-commands/main/ebook/en/assets/cover.jpg" height="450" width="auto"></p>

<div align="center">
    <p>
	    <a name="stars"><img src="https://img.shields.io/github/stars/bobbyiliev/101-linux-commands?style=for-the-badge"></a>
	    <a name="forks"><img src="https://img.shields.io/github/forks/bobbyiliev/101-linux-commands?logoColor=green&style=for-the-badge"></a>
	    <a name="contributions"><img src="https://img.shields.io/github/contributors/bobbyiliev/101-linux-commands?logoColor=green&style=for-the-badge"></a>
      <a name="ebook" href="https://bobbyiliev.github.io/101-linux-commands/" target="_blank"><img src="https://img.shields.io/static/v1?label=eBook&message=Read%20Online&color=orange&logoColor=green&style=for-the-badge&logo=github"></a>
	    <a name="madeWith"><img src="https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg?style=for-the-badge"></a>
	    <a name="license"><img src="https://img.shields.io/github/license/bobbyiliev/101-linux-commands?style=for-the-badge"></a>
    </p>
</div>

## 💻 ++101 Linux commands Open-source eBook

This is an open-source eBook with 101 Linux commands that everyone should know. No matter if you are a DevOps/SysOps engineer, developer, or just a Linux enthusiast, you will most likely have to use the terminal at some point in your career.

**Make sure to star the repository** ⭐

If you need a Linux virtual machine to test these commands on, use the following referral link to get a [free $200 Credit For DigitalOcean](https://m.do.co/c/2a9bba940f39)!

## Introduction to Linux eBook

If you are looking for a comprehensive guide for beginners, check out this eBook: [Introduction to Linux eBook](https://leanpub.com/introduction-to-linux)

## 📙 Online eBook

An online copy :zap:🌐 of this ebook is available [**here** 📙](https://bobbyiliev.github.io/101-linux-commands/).

## 🔽 Download links

### 📚 Multiple Formats Available

This eBook is now available in multiple formats to suit different reading preferences:

- **📄 PDF (Light Theme)**: [Download PDF](https://github.com/bobbyiliev/101-linux-commands/releases/latest/download/101-linux-commands-light.pdf) - Perfect for printing and desktop reading
- **🌙 PDF (Dark Theme)**: [Download PDF](https://github.com/bobbyiliev/101-linux-commands/releases/latest/download/101-linux-commands-dark.pdf) - Ideal for dark mode readers
- **📱 EPUB**: [Download EPUB](https://github.com/bobbyiliev/101-linux-commands/releases/latest/download/101-linux-commands.epub) - Compatible with e-readers, tablets, and mobile devices
- **🌐 HTML**: [Download HTML](https://github.com/bobbyiliev/101-linux-commands/releases/latest/download/101-linux-commands.html) - Single-page web version

### 🔄 Latest Releases

Visit our [Releases page](https://github.com/bobbyiliev/101-linux-commands/releases) to download the latest versions or browse previous releases.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=bobbyiliev/101-linux-commands&type=date&legend=top-left)](https://www.star-history.com/#bobbyiliev/101-linux-commands&type=date&legend=top-left)

---

# Content <!-- omit in toc -->

- [Basics](#basics)
  - [File Hierarchy Standard (FHS)](#file-hierarchy-standard-fhs)
  - [Commands](#commands)
- [Disk and File System Management](#disk-and-file-system-management)
  - [General Disk Manipulation (non-LVM)](#general-disk-manipulation-non-lvm)
  - [Globs (Wildcards)](#globs-wildcards)
  - [Regex](#regex)
  - [Stream redirection](#stream-redirection)
- [Text Readers & Editors](#text-readers--editors)
  - [Less](#less)
  - [VI](#vi)
- [User and Group Management](#user-and-group-management)
- [File System Permissions](#file-system-permissions)
- [SSH](#ssh)
- [Cronjobs](#cronjobs)
- [Package Management](#package-management)
  - [RPM](#rpm)
  - [YUM](#yum)
- [📃 List of commands by category:](#-list-of-commands-by-category)
  - [Directory Navigation](#directory-navigation)
  - [File Commands](#file-commands)
  - [File and Directory Manipulation](#file-and-directory-manipulation)
  - [Package archive and compression tools](#package-archive-and-compression-tools)
  - [System commands](#system-commands)
  - [Networking Commands](#networking-commands)
  - [Package Management](#package-management-1)
  - [User Information commands](#user-information-commands)
  - [Session commands](#session-commands)
  - [Getting Help](#getting-help)
  - [Applications](#applications)
- [📃 List of commands by chapter:](#-list-of-commands-by-chapter)
- [🔗Links](#links)
- [📖Other eBooks](#other-ebooks)
- [🤲Contributing](#contributing)

---

# Basics

## File Hierarchy Standard (FHS)

| Path     | Content                             |
| -------- | ----------------------------------- |
| `/bin`   | Binaries (User)                     |
| `/boot`  | Static boot loader files            |
| `/etc`   | Host specific configs               |
| `/lib`   | Shared libraries and kernel modules |
| `/sbin`  | Binaries (System/root)              |
| `/var`   | Varying files (e.g. Logs)           |
| `/usr`   | 3rd party software                  |
| `/proc`  | Pseudo file system                  |
| `/sys`   | Pseudo file system                  |
| `/mnt`   | Mountpoint for internal drives      |
| `/media` | Mountpoint for external drives      |
| `/home`  | User homes                          |
| `/run`   | PID files of running processes      |

---

## Commands

**File System Commands**

| Command                                                                                                         | Options          | Description                                       |
| --------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------- |
| [`cd`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/002-the-cd-command.md)       | `-`              | Navigate to last dir                              |
|                                                                                                                 | `~`              | Navigate to home                                  |
|                                                                                                                 | `~username`      | Navigate to home of specified user                |
| [`pwd`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/006-the-pwd-command.md)     |                  | Print working dir                                 |
| [`ls`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/001-the-ls-command.md)       |                  | Print dir content                                 |
|                                                                                                                 | `-l`             | Format as list                                    |
|                                                                                                                 | `-a`             | Show hidden items (`-A` without `.` and `..`)     |
|                                                                                                                 | `-r`             | Invert order                                      |
|                                                                                                                 | `-R`             | Recurse                                           |
|                                                                                                                 | `-S`             | Sort by size                                      |
|                                                                                                                 | `-t`             | Sort by date modified                             |
| [`mkdir`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/014-the-mkdir-command.md) | `-p`             | Create dir with parents                           |
| [`cp`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/031-the-cp-command.md)       | `-r`             | Copy dir                                          |
| [`rmdir`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/103-the-rmdir-command.md) | `-p`             | Remove dir and empty parents                      |
| [`rm`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/040-the-rm-command.md)       | `-rf`            | Remove dir recursively, `-f` without confirmation |
| [`mv`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/032-the-mv-command.md)       |                  | Move recursively                                  |
| [`find`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/102-the-find-command.md)   | `-iname pattern` | Search dir/file case-insensitive                  |
|                                                                                                                 | `-mmin n`        | Last modified n minutes ago                       |
|                                                                                                                 | `-mtime n`       | Last modified n days ago                          |
|                                                                                                                 | `-regex pattern` | Path matches pattern                              |
|                                                                                                                 | `-size n[kMG]`   | By file size (`-n` less than; `+n` greater than)  |
|                                                                                                                 | `! searchparams` | Invert search                                     |

---

**File Manipulation**

| Command                                                                                                         | Options                                    | Description                                |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------ |
| [`cat`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/003-the-cat-tac-command.md) | `file`                                     | Print content                              |
| [`tac`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/003-the-cat-tac-command.md) | `file`                                     | Print content inverted                     |
| [`sort`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/059-the-sort-command.md)   | `file`                                     | Print sorted                               |
|                                                                                                                 | `file -r -u`                               | Print sorted descending without dublicates |
| [`head`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/004-the-head-command.md)   | `-n10 file`                                | Print lines 5-10                           |
| [`tail`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/005-the-tail-command.md)   | `-f file`                                  | Print new lines automatically              |
| [`cut`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/098-the-cut-command.md)     | `-f -4,7-10,12,15- file`                   | Print selected fields (tab delimited)      |
|                                                                                                                 | `-c -4,7-10,12,15- file`                   | Print selected characters positions        |
|                                                                                                                 | `-f 2,4 -d, --output-delimiter=$'\t' file` | Change delimiter (but use tab for output)  |
| [`uniq`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/074-the-uniq-command.md)   | `file`                                     | Hide consecutive identical lines           |
|                                                                                                                 | `file -c`                                  | Show consecutive identical line count      |
|                                                                                                                 | `file -u`                                  | Hide consecutive identical lines           |
| `file`                                                                                                          | `file`                                     | Get file type                              |
| `wc`                                                                                                            | `file`                                     | Count Lines, Words, Chars (Bytes)          |

---

**Archiving**

| Command                                                                                                         | Options                          | Description                                         |
| --------------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------- |
| [`tar`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/063-the-tar-command.md)     | `cfv archiv.tar file1 file2`     | Create archive / add or overwrite content           |
|                                                                                                                 | `tfv archiv.tar`                 | Show content                                        |
|                                                                                                                 | `xf archiv.tar [-C ~/extracted]` | Extract (and decompress) archive (to ~ / extracted) |
|                                                                                                                 | `cfvj archiv.tar.bz2 file`       | Create bzip2 compressed archive                     |
|                                                                                                                 | `cfvz archiv.tar.gz file`        | Create gzip compressed archive                      |
|                                                                                                                 | `cfa archiv.tar.[komp] file`     | create compressed archive (auto type based on name) |
| [`bzip2`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/069-the-bzip2-command.md) | `file1 file2`                    | Dateien (einzeln) komprimieren                      |
|                                                                                                                 | `-d file1 file2`                 | Compress files (one at a time)                      |
| [`gzip`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/015-the-gzip-command.md)   | `file1 file2`                    | Dateien (einzeln) komprimieren                      |
|                                                                                                                 | `-d file1 file2`                 | Decompress files                                    |

---

# Disk and File System Management

## General Disk Manipulation (non-LVM)

Creating physical partitions is **not required**! You can create PVs directly!

| Command                                                                                                   | Options                               | Description                          |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------ |
| `fdisk`                                                                                                   | `-l`                                  | List physical disks and partitions   |
|                                                                                                           | `/dev/sdb`<br>`n`                     | Create new partition                 |
|                                                                                                           | `/dev/sdb`<br>`t`<br>`8e`             | Change partition type to _Linux LVM_ |
| `mkfs.xfs`                                                                                                | `/dev/myVG/myVol`                     | Format LV with XFS                   |
| `mkfs.ext4`                                                                                               | `-f /dev/myVG/myVol`                  | Format LV with EXT4 (overwrite)      |
| `blkid`                                                                                                   | `/dev/myVG/myVol`                     | Show UUID and formatting of volume   |
| `mount`                                                                                                   |                                       | Show current mounted file systems    |
|                                                                                                           | `-t ext4 /dev/myVG/myVol /mountpoint` | Mount LV to /mountpoint              |
|                                                                                                           | `-a`                                  | Mount as configured in /etc/fstab    |
| `umount`                                                                                                  |                                       | Unmount a file system                |
|                                                                                                           | `/dev/myVG/myVol`                     | Unmount LV from /mountpoint          |
|                                                                                                           | `/mountpoint`                         | Unmount LV from /mountpoint          |
| [`df`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/010-the-df-command.md) | -                                     | Show disk usage                      |
| `xfs_growfs`                                                                                              | `/dev/myVG/myVol`                     | Resize xfs filesystem                |
| `resize2fs`                                                                                               | ` /dev/myVG/myVol`                    | Resize ext3/4 filesystem             |

---

**Other**

| Command                                                                                                     | Options         | Description                                |
| ----------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------ |
| `<command>`                                                                                                 | `--help`        | Help of current command (not standardized) |
|                                                                                                             | `-h`            |                                            |
|                                                                                                             | `-?`            |                                            |
| [`man`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/024-the-man-command.md) | `<command>`     | Manual page of command                     |
|                                                                                                             | `-k keyword`    | Search command by keyword (oder `apropos`) |
| `alias`                                                                                                     |                 | Show aliases                               |
|                                                                                                             | `name='befehl'` | Create alias                               |

---

## Globs (Wildcards)

The dot `.` in front of hidden items is ignored by glob patterns!

| Character | Description             |
| --------- | ----------------------- |
| `?`       | Any single character    |
| `*`       | Any characters          |
| `[ac-e]`  | 1 character in enum     |
| `[!ac-e]` | 1 character not in enum |

## Regex

Bash itself does not know regex. Use programs like `grep`, `sed`, `awk`.

**Control characters**

| Character      | Description             |
| -------------- | ----------------------- |
| `.`            | Any single character    |
| `[ac-e]`       | 1 character in enum     |
| `[^ac-e]`      | 1 character not in enum |
| `^`            | Start of string         |
| `$`            | End of string           |
| `\d`           | Digit                   |
| `\D`           | Not a digit             |
| `\s`           | Whitespace              |
| `\S`           | Not a Whitespace        |
| `\<`           | Start of word           |
| `\>`           | End of word             |
| `pattern?`     | Quantifier 0 or 1       |
| `pattern*`     | Quantifier 0..n         |
| `pattern+`     | Quantifier 1..n         |
| `pattern{x}`   | Quantifier exactly x    |
| `pattern{x,}`  | Quantifier x..n         |
| `pattern{x,y}` | Quantifier x..y         |
| `pattern{,y}`  | Quantifier 0..y         |

**Grep**

| Command                                                                                                       | Options           | Description    |
| ------------------------------------------------------------------------------------------------------------- | ----------------- | -------------- |
| [`grep`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/107-the-grep-command.md) | `pattern file`    | Extended Regex |
|                                                                                                               | `-E pattern file` | Extended Regex |
|                                                                                                               | `-v pattern file` | Invert match   |
|                                                                                                               | `-w pattern file` | Word match     |
|                                                                                                               | `-i pattern file` | Ignore case    |

## Stream redirection

- `>` overwrite
- `>>` append

| Character             | Description                     |
| --------------------- | ------------------------------- |
| `> file` or `1> file` | STDOUT to file                  |
| `< file`              | Datei to STDIN                  |
| `2> file`             | STDERR to file                  |
| `2>&1`                | STDERR to same target as STDOUT |
| `> file 2>&1`         | STDOUT and STDERR to file       |

# Text Readers & Editors

## Less

| Command             | Description                     |
| ------------------- | ------------------------------- |
| `q`                 | Quit                            |
| `R`                 | Refresh content                 |
| `F`                 | Auto scroll                     |
| `g number`          | Go to line                      |
| `m lowercaseLetter` | Mark line                       |
| `' lowercaseLetter` | Go to mark                      |
| `/pattern`          | Search forward                  |
| `?pattern`          | Search backward                 |
| `n`                 | Next search result              |
| `N`                 | Last search result              |
| `ESC u`             | Remove highlighting from search |

## VI

[`VI/VIM`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/100-the-vim-command.md)
**Editing**

To leave editing mode press `ESC`.

| Command   | Description           |
| --------- | --------------------- |
| `i`       | insert before cursor  |
| `a`       | insert after cursor   |
| `A`       | insert at end of line |
| `o`       | new line below        |
| `O`       | new line above        |
| `u`       | undo                  |
| `.`       | repeat last command   |
| `yy`      | copy line             |
| `5yy`     | copy 5 lines          |
| `p`       | paste below           |
| `P`       | paste above           |
| `x`       | delete character      |
| `5x`      | delete 5 characters   |
| `dd`      | delete line           |
| `5dd`     | delete 5 lines        |
| `:10,20d` | delete lines 10-20    |
| `d0`      | delete to line begin  |
| `d$`      | delete to line end    |

**Navigation**

Navigate as usual with `arrow keys`, `home`, `end`, `pg up`, `pg dn`.

| Command | Description            |
| ------- | ---------------------- |
| `5G`    | go to line 5           |
| `H`     | go to top of screen    |
| `M`     | go to middle of screen |
| `L`     | go to end of screen    |
| `5w`    | move over 7 words      |
| `5b`    | move back 5 words      |

**Other**

| Command     | Description                  |
| ----------- | ---------------------------- |
| `/foo`      | search forward               |
| `?foo`      | search backwards             |
| `n`         | repeat search                |
| `:w`        | save                         |
| `:q`        | close                        |
| `:wq`       | save and close               |
| `:q!`       | close without saving         |
| `:!command` | run bash command             |
| `:r foo`    | read file foo into this file |

# User and Group Management

**UID**

| UID   | Type           |
| ----- | -------------- |
| <1000 | system account |
| >1000 | user account   |

**User Database**

User info without passwords is stored in `/etc/passwd`.

| username | PW  | UID  | GID  | GECOS | HOME        | SHELL     |
| -------- | --- | ---- | ---- | ----- | ----------- | --------- |
| hfict    | x   | 1000 | 1000 |       | /home/hfict | /bin/bash |

**Group Database**

Group info with secondary group members are stored in `/etc/group`.
Primary group members are identified by GID in user database.

| groupname | PW  | GID | Users       |
| --------- | --- | --- | ----------- |
| wheel     | x   | 10  | hfict,user2 |

**Password Database**

Hashed user passwords are stored in `/etc/shadow`.
Password encryption is configured in `/etc/login.defs`.

| username | PW     | Last PW change | Minimum | Maximum | Warn | Inactive | Expire |
| -------- | ------ | -------------- | ------- | ------- | ---- | -------- | ------ |
| hfict    | [hash] | 17803          | 0       | 99999   | 7    |          |        |

PW:

- `[hash]` Encrypted test password
- `! [hash]` Account locked
- `!!` or `*` Account locked, no password set

**Commands**

| Command                                                                                                             | Param                                         | Description                                           |
| ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------- |
| `id`                                                                                                                | `username`                                    | Show a user's ID and groups                           |
| [`who`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/017-the-who-command.md)         |                                               | Show logged in users                                  |
| [`last`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/048-the-last-command.md)       |                                               | Show last logins                                      |
| `lastb`                                                                                                             |                                               | Show last failed logins                               |
| [`sudo`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/051-the-sudo-command.md)       | `-u user command`                             | Execute command with user rights (default is root)    |
|                                                                                                                     | `-i` or` su -`                                | Shell with root rights                                |
| [`su`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/044-the-su-command.md)           |                                               | Shell as root (non-login shell)                       |
|                                                                                                                     | `-`                                           | Shell as root (login shell)                           |
|                                                                                                                     | `- user`                                      | Shell as user                                         |
| [`useradd`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/080-the-useradd-command.md) | `-u 2101 -g primarygroup -c comment username` | Create user (without `-g`, new group will be created) |
| [`usermod`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/082-the-usermod-command.md) | `-G group1, group2`                           | Define (overwrite) secondary groups                   |
|                                                                                                                     | `-ag group, group2`                           | Add secondary groups                                  |
|                                                                                                                     | `-l username`                                 | Change username                                       |
|                                                                                                                     | `-L`                                          | Lock Account                                          |
|                                                                                                                     | `-U`                                          | Unlock Account                                        |
|                                                                                                                     | `-s shellpath`                                | Change shell                                          |
| [`userdel`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/081-the-userdel-command.md) | `-r username`                                 | Delete user including home and mail spool             |
| [`passwd`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/025-the-passwd-command.md)   | `username`                                    | Change password (interactive)                         |
| `groupadd`                                                                                                          | `groupname`                                   | Create group (optionally set GID with `-g`)           |
| `groupdel`                                                                                                          | `groupname`                                   | Delete group                                          |

# File System Permissions

Permissions can be set on:

- User (owner)
- Group (owner)
- Others

Only root can change _User_. _User_ can change _Group_.

Basic permissions (Add binary flags to combine):

| Char | Binary Flag | Permission |
| ---- | ----------- | ---------- |
| r    | 4           | read       |
| w    | 2           | write      |
| x    | 1           | execute    |

Advanced permissions (place in front of basic permissions: `chmod 1777 shared`).:

| Char  | Binary Flag | Name       | Description                                                                |
| ----- | ----------- | ---------- | -------------------------------------------------------------------------- |
| t / T | 1           | Sticky Bit | _Others_ can't delete content (only applicable for directories)            |
| s / S | 2           | SGID-Bit   | File: run with permissions of _Group_<br>Dir: New elements inherit _Group_ |
| s / S | 4           | SUID-Bit   | File is run with permissions of _User_ (only applicable for files)         |

Advanced permissions replace the **x** when using `ls -l`. Lower case if **x** is set, upper case if **x** is not set.

_Read_ permission on a directory only allows to see the directory itself but not it's contents. Use _execute_ permission to show contents.

**Commands**

| Command                                                                                                         | Options                  | Description                                       |
| --------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------- |
| [`chmod`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/106-the-chmod-command.md) | `-R [uog] dirname`       | Set permissions recursively using binary flags    |
|                                                                                                                 | `+[suog] filename`       | Add permissions using binary flags                |
|                                                                                                                 | `-[suog] filename`       | Remove permissions using binary flags             |
|                                                                                                                 | `u+x filename`           | Add _execute_ permission for _User_               |
|                                                                                                                 | `g+wx filename`          | Add _write_ and _execute_ permissions for _Group_ |
|                                                                                                                 | `o-r filename`           | Remove _read_ permission for _Others_             |
| [`chown`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/101-the-chown-command.md) | `-R user:group filename` | Change owner (_User_ & _Group_) recursively       |
|                                                                                                                 | `user filename`          | Change owner (_User_)                             |
|                                                                                                                 | `:group filename`        | Change owner (_Group_)                            |
| `chgroup`                                                                                                       | `group filename`         | Change owner (_Group_)                            |

# SSH

[`SSH`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/089-the-ssh-command.md)
Configuration is done in `/etc/ssh/sshd_config`.

Reload SSH service with `systemctl reload sshd` to apply changes!

DenyUsers, AllowUsers, DenyGroups, AllowGroups override each other and are applied in the order listed above.

| Config            | Option             | Description                                   |
| ----------------- | ------------------ | --------------------------------------------- |
| `PermitRootLogin` | `no`               | Deny root to login via SSH                    |
|                   | `yes`              | Allow root to login via SSH                   |
|                   | `without-password` | Allow only with private/public key auth       |
| `AllowUsers`      | `user1 user2`      | Allow only user1 and user2                    |
| `DenyUsers`       | `user1 user2`      | Allow all users but user1 and user2           |
| `AllowGroups`     | `group1 group2`    | Allow only users from specified groups        |
| `DenyGroups`      | `group1 group2`    | Allow all users but those in specified groups |

# Cronjobs

**[`Crontab`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/091-the-crontab-command.md)**

Cronjobs are configured in crontab files. Do not edit these files directly. Use `crontab -e` instead. This runs all required actions to activate a cronjob after saving the edited crontab. The locations are as follows:

- `/var/spool/cron/username` user specific
- `/etc/crontab` system wide crontab

The format of the files is (user specific crontabs **do not** have the column _user-name_):

```
Example of job definition:
.---------------- minute (0 - 59 | */5 [every 5 minutes])
|  .------------- hour (0 - 23)
|  |  .---------- day of month (1 - 31)
|  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
|  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
|  |  |  |  |
*  *  *  *  * user-name  command to be executed
```

| Command                          | Description                   |
| -------------------------------- | ----------------------------- |
| `rpm -q cronie`                  | Check if package is installed |
| `systemctl status crond.service` | Check if service is running   |
| `crontab -l`                     | List current users crontab    |
| `crontab -e`                     | Edit current users crontab    |
| `crontab -e -u username`         | Edit specific users crontab   |
| `crontab -r`                     | Remove current users crontab  |

**Script folders**

Scripts in one of the following directories will be executed at the interval specified by the directory's name:

- `/etc/cron.hourly`
- `/etc/cron.daily`
- `/etc/cron.weekly`
- `/etc/cron.monthly`

**Allow / Deny usage**

Add user names one per line to the following files:

- `/etc/cron.allow` Whitelist
- `/etc/cron.deny` Blacklist

If none of the files exists, all users are allowed.

**Logs and Results**

Execution of cronjobs is logged in `/var/log/cron`.
Results are sent to the users mail `/var/spool/mail/username`.

# Package Management

## RPM

[`RPM`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/075-the-rpm-command.md)

| Command                  | Description                               |
| ------------------------ | ----------------------------------------- |
| `rpm -i rpmfile\|rpmurl` | Install package                           |
| `rpm -e packagename`     | Uninstall package                         |
| `rpm -q packagename`     | Check if package is installed             |
| `rpm -ql packagename`    | List files in a package                   |
| `rpm -qa`                | List all installed packages               |
| `rpm -qf /path/to/file`  | Get package that installed the file       |
| `rpm -qf $(which <exe>)` | Get package that installed the executable |
| `rpm -V packagename`     | Validate installed package                |

## YUM

[`YUM`](https://github.com/bobbyiliev/101-linux-commands/blob/main/ebook/en/content/053-the-yum-command.md) is configured in `/etc/yum.conf`

Repos are configured in `/etc/yum.repos.d/`

Log is in `/var/log/yum.log`

| Command                               | Description                               |
| ------------------------------------- | ----------------------------------------- |
| `yum install packagename [-y]`        | Install package (`-y` no confirm message) |
| `yum remove packagename`              | Uninstall package                         |
| `yum update`                          | Update all installed packages             |
| `yum update packagename`              | Update specific package                   |
| `yum update pattern*`                 | Update packages using wildcard            |
| `yum info packagename`                | Get detailed info about package           |
| `yum list packagename`                | List installed and available packages     |
| `yum search searchstring`             | search for a package (name & summary)     |
| `yum search all searchstring`         | search for a package (all infos)          |
| `yum deplist packagename`             | List dependencies of a package            |
| `yum reinstall packagename`           | Reinstall (corrupted) package             |
| `yumdownloader --resolve packagename` | Download rpm package with dependencies    |

---

# 📃 List of commands by category:

If you want to contribute, feel free to pick up a topic marked as `TODO` and submit a pull request 🙌

Feel free to add new topics in case that you don't find one that you like from the current list.

---

### Directory Navigation

- [cd](ebook/en/content/002-the-cd-command.md) - change working directory
- [ls](ebook/en/content/001-the-ls-command.md) - list directory contents
- [dir](ebook/en/content/057-the-dir-command.md) - directory listing, columnar format
- [pwd](ebook/en/content/006-the-pwd-command.md) - return working directory name
- [tree](ebook/en/content/095-the-tree-command.md) - list subdirectories in a tree structure

### File Commands

- [cat/tac](ebook/en/content/003-the-cat-tac-command.md) - concatenate and print files
- [column](ebook/en/content/162-the-column-command.md) - format text into columns
- [diff/sdiff](ebook/en/content/062-the-diff-sdiff-command.md) - compare files line by line
- [find](ebook/en/content/102-the-find-command.md) - search for files
- [grep](ebook/en/content/107-the-grep-command.md) - file pattern matcher
- [head](ebook/en/content/004-the-head-command.md) - display the first lines of a file
- [locate](ebook/en/content/049-the-locate-command.md) - find files and directories
- [stat](ebook/en/content/079-the-stat-command.md) - display file status
- [tail](ebook/en/content/005-the-tail-command.md) - display the last lines of a file
- [uniq](ebook/en/content/074-the-uniq-command.md) - report or filter out repeated lines in a file

### File and Directory Manipulation

- [awk](ebook/en/content/090-the-awk-command.md) - pattern-directed scanning and processing language
- [chmod](ebook/en/content/106-the-chmod-command.md) - change permissions
- [chown](ebook/en/content/101-the-chown-command.md) - change file owner and group
- [cp](ebook/en/content/031-the-cp-command.md) - copy files and directories
- [cut](ebook/en/content/098-the-cut-command.md) - remove sections from files
- [ln](ebook/en/content/137-the-ln-command.md) - create links between files
- [mkdir](ebook/en/content/014-the-mkdir-command.md) - make a new directory
- [mv](ebook/en/content/032-the-mv-command.md) - move files and directories
- [nano](ebook/en/content/039-the-nano-command.md) - text editor
- [rm](ebook/en/content/040-the-rm-command.md) - delete files and directories
- [rmdir](ebook/en/content/103-the-rmdir-command.md) - remove directory
- [paste](ebook/en/content/060-the-paste-command.md) - merge corresponding or subsequent lines of file
- [rsync](ebook/en/content/086-the-rsync-command.md) - remote copy files
- [scp](ebook/en/content/076-the-scp-command.md) - secure copy
- [basename](ebook/en/content/111-the-basename-command.md) - strips directory information and suffixes from file path
- [sed](ebook/en/content/099-the-sed-command.md) - text transformation tool
- [sort](ebook/en/content/059-the-sort-command.md) - arrange or merge lines of files
- [split](ebook/en/content/078-the-split-command.md) - split a file into pieces
- [touch](ebook/en/content/007-the-touch-command.md) - change file access and modification times
- [vim](ebook/en/content/100-the-vim-command.md) - text editor

### Package archive and compression tools

- [bzip2](ebook/en/content/069-the-bzip2-command.md) - block-sorting file compressor
- [cpio](ebook/en/content/152-the-cpio-command.md) - copy files to/from archives
- [gzip](ebook/en/content/015-the-gzip-command.md) - compression tool
- [gunzip](ebook/en/content/064-the-gunzip-command.md) - decompression tool
- [tar](ebook/en/content/063-the-tar-command.md) - create, extract and manipulate archives
- [zip](ebook/en/content/054-the-zip-command.md) - package and compress files
- [unzip](ebook/en/content/055-the-unzip-command.md) - list, test, extract compressed ZIP files

### System commands

- [badblocks](ebook/en/content/149-the-badblocks-command.md) - search for bad blocks on storage devices
- [cfdisk](ebook/en/content/160-the-cfdisk-command.md) - curses-based disk partitioning tool
- [crontab](ebook/en/content/091-the-crontab-command.md) - maintain individual tables used to drive the cron daemon
- [df](ebook/en/content/010-the-df-command.md) - display free disk space
- [dmidecode](ebook/en/content/154-the-dmidecode-command.md) - retrieve hardware information from DMI table
- [dmesg](ebook/en/content/156-the-dmesg-command.md) - display kernel ring buffer messages
- [du](ebook/en/content/084-the-du-command.md) - display disk usage statistics
- [free](ebook/en/content/018-the-free-command.md) - show memory usage information
- [fsck](ebook/en/content/150-the-fsck-command.md) - file system check and repair
- [hostname](ebook/en/content/038-the-hostname-command.md) - set or print name of current host system
- [hostnamectl](ebook/en/content/065-the-hostnamectl-command.md) - change hostname settings
- [ionice](ebook/en/content/083-the-ionice-command.md) - get/set I/O process priority
- [iostat](ebook/en/content/050-the-iostat-command.md) - I/O statistics
- [journalctl](ebook/en/content/139-the-journalctl-command.md) - view systemd journal logs
- [kill](ebook/en/content/034-the-kill-command.md) - terminate or signal a process by id
- [killall](ebook/en/content/035-the-killall-command.md) - kill processes by name
- [lsb_release](ebook/en/content/153-the-lsb_release-command.md) - display LSB and distribution information
- [lsblk](ebook/en/content/104-the-lsblk-command.md) - display block and loop devices
- [lsof](ebook/en/content/068-the-lsof-command.md) - list open files
- [lspci](ebook/en/content/159-the-lspci-command.md) - list PCI devices
- [mkfs](ebook/en/content/151-the-mkfs-command.md) - build file systems
- [mpstat](ebook/en/content/072-the-mpstat-command.md) - CPU statistics
- [ncdu](ebook/en/content/073-the-ncdu-command.md) - curses-based disk usage
- [ps](ebook/en/content/033-the-ps-command.md) - display process status
- [pstree](ebook/en/content/094-the-pstree-command.md) - show processes in tree format
- [reboot](ebook/en/content/058-the-reboot-command.md) - restart the system
- [service](ebook/en/content/070-the-service-command.md) - run an init script
- [shutdown](ebook/en/content/056-the-shutdown-command.md) - close down the system at a specific time
- [systemctl](ebook/en/content/138-the-systemctl-command.md) - control systemd services
- [top/htop](ebook/en/content/019-the-top-htop-command.md) - display process information
- [tty](ebook/en/content/158-the-tty-command.md) - print terminal name
- [uname](ebook/en/content/013-the-uname-command.md) - prints operating system details
- [useradd](ebook/en/content/080-the-useradd-command.md) - add/update user accounts
- [userdel](ebook/en/content/081-the-userdel-command.md) - delete user account
- [usermod](ebook/en/content/082-the-usermod-command.md) - modify user properties
- [vmstat](ebook/en/content/071-the-vmstat-command.md) - virtual memory statistics
- [watch](ebook/en/content/140-the-watch-command.md) - execute commands repeatedly
- [whereis](ebook/en/content/096-the-whereis-command.md) - locate programs

### Networking Commands

- [dig](ebook/en/content/087-the-dig-command.md) - DNS lookup utility
- [ifconfig](ebook/en/content/041-the-ifconfig-command.md) - configure network interface parameters
- [ip](ebook/en/content/042-the-ip-command.md) - perform network administration tasks
- [iptables](ebook/en/content/066-the-iptables-command.md) - configure netfilter firewall
- [lscpu](ebook/en/content/030-the-lscpu-command.md) - display CPU architecture information
- [netstat](ebook/en/content/067-the-netstat-command.md) - show network status
- [nmcli](ebook/en/content/148-the-nmcli-command.md) - NetworkManager command line interface
- [ping](ebook/en/content/085-the-ping-command.md) - check network connectivity
- [traceroute](ebook/en/content/147-the-traceroute-command.md) - trace network path to destination
- [ufw](ebook/en/content/146-the-ufw-command.md) - uncomplicated firewall
- [whois](ebook/en/content/088-the-whois-command.md) - information about Internet domain names and network numbers

### Package Management

- [apt](ebook/en/content/052-the-apt-command.md) - Debian package management
- [rpm](ebook/en/content/075-the-rpm-command.md) - RPM package manager (RedHat)
- [yum](ebook/en/content/053-the-yum-command.md) - package manager for RedHat Linux

### User Information commands

For user modification, see useradd, userdel, usermod under System commands

- [groups](ebook/en/content/023-the-groups-command.md) - show group memberships
- [finger](ebook/en/content/022-the-finger-command.md) - shows information about users
- [last](ebook/en/content/048-the-last-command.md) - displays most recent user logins
- [passwd](ebook/en/content/025-the-passwd-command.md) - modify a user's password
- [w](ebook/en/content/026-the-w-command.md) - display who is logged in and what they are doing
- [who](ebook/en/content/017-the-who-command.md) - display who is logged in
- [whoami](ebook/en/content/027-the-whoami-command.md) - display effective user id

### Session commands

- [bg](ebook/en/content/142-the-bg-command.md) - put jobs in background
- [clear](ebook/en/content/043-the-clear-command.md) - clear terminal screen
- [env](ebook/en/content/036-the-env-command.md) - display environment variables, or set variables for command execution
- [exit](ebook/en/content/061-the-exit-command.md) - close the active session/shell
- [export](ebook/en/content/145-the-export-command.md) - set environment variables
- [fg](ebook/en/content/143-the-fg-command.md) - bring jobs to foreground
- [history](ebook/en/content/028-the-history-command.md) - display the command history
- [jobs](ebook/en/content/141-the-jobs-command.md) - display active jobs
- [login](ebook/en/content/029-the-login-command.md) - login and initiate a user session
- [nohup](ebook/en/content/093-the-nohup-command.md) - invoke a utility immune to hangups
- [printenv](ebook/en/content/037-the-printenv-command.md) - print specified environment variables
- [screen](ebook/en/content/108-the-screen-command.md) - start a screen session
- [sleep](ebook/en/content/077-the-sleep-command.md) - suspend execution for a time interval
- [ssh](ebook/en/content/089-the-ssh-command.md) - secure shell login
- [su](ebook/en/content/044-the-su-command.md) - substitute user identity
- [sudo](ebook/en/content/051-the-sudo-command.md) - execute a command as another user
- [wall](ebook/en/content/136-the-wall-command.md) - message to all users

### Getting Help

- [apropos](ebook/en/content/155-the-apropos-command.md) - search manual page names and descriptions
- [man](ebook/en/content/024-the-man-command.md) - format and display online manual pages
- [help](ebook/en/content/011-the-help-command.md) - displays help about basic commands not covered by 'man'
- [whatis](ebook/en/content/016-the-whatis-command.md) - display one-line command descriptions

### Applications

- [!!](ebook/en/content/157-the-bangbang-command.md) - history expansion (repeat last command)
- [bc](ebook/en/content/009-the-bc-command.md) - basic calculator
- [cal](ebook/en/content/008-the-cal-command.md) - displays a calendar
- [cmatrix](ebook/en/content/105-the-cmatrix-command.md) - enter the Matrix
- [curl](ebook/en/content/046-the-curl-command.md) - transfer data to or from a server
- [echo](ebook/en/content/021-the-echo-command.md) - display interpreted arguments
- [factor](ebook/en/content/012-the-factor-command.md) - prints prime factors of numbers
- [printf](ebook/en/content/097-the-printf-command.md) - format output
- [sl](ebook/en/content/020-the-sl-command.md) - runs a steam locomotive across your terminal
- [time](ebook/en/content/144-the-time-command.md) - measure command execution time
- [wget](ebook/en/content/045-the-wget-command.md) - non-interactive web file download
- [xargs](ebook/en/content/092-the-xargs-command.md) - construct argument lists and execute utility
- [yes](ebook/en/content/047-the-yes-command.md) - print continous output stream
- [banner](ebook/en/content/112-the-banner-command.md) - Writes ASCII character strings in large letters to standard output.
- [aplay](ebook/en/content/125-the-aplay-command.md) - aplay is a command-line to play audio files.
- [spd-say](ebook/en/content/126-the-spd-say-command.md) - plays the given text as the sound from the command line.

---

# 📃 List of commands by chapter:

If you want to contribute, feel free to pick up a topic, update it with `New Examples | [Options]`and submit a pull request 🙌

Feel free to add new topics in case that you don't find one that you like from the current list.

- [001-the-ls-command.md](ebook/en/content/001-the-ls-command.md)
- [002-the-cd-command.md](ebook/en/content/002-the-cd-command.md)
- [003-the-cat-tac-command.md](ebook/en/content/003-the-cat-tac-command.md)
- [004-the-head-command.md](ebook/en/content/004-the-head-command.md)
- [005-the-tail-command.md](ebook/en/content/005-the-tail-command.md)
- [006-the-pwd-command.md](ebook/en/content/006-the-pwd-command.md)
- [007-the-touch-command.md](ebook/en/content/007-the-touch-command.md)
- [008-the-cal-command.md](ebook/en/content/008-the-cal-command.md)
- [009-the-bc-command.md](ebook/en/content/009-the-bc-command.md)
- [010-the-df-command.md](ebook/en/content/010-the-df-command.md)
- [011-the-help-command.md](ebook/en/content/011-the-help-command.md)
- [012-the-factor-command.md](ebook/en/content/012-the-factor-command.md)
- [013-the-uname-command.md](ebook/en/content/013-the-uname-command.md)
- [014-the-mkdir-command.md](ebook/en/content/014-the-mkdir-command.md)
- [015-the-gzip-command.md](ebook/en/content/015-the-gzip-command.md)
- [016-the-whatis-command.md](ebook/en/content/016-the-whatis-command.md)
- [017-the-who-command.md](ebook/en/content/017-the-who-command.md)
- [018-the-free-command.md](ebook/en/content/018-the-free-command.md)
- [019-the-top-htop-command.md](ebook/en/content/019-the-top-htop-command.md)
- [020-the-sl-command.md](ebook/en/content/020-the-sl-command.md)
- [021-the-echo-command.md](ebook/en/content/021-the-echo-command.md)
- [022-the-finger-command.md](ebook/en/content/022-the-finger-command.md)
- [023-the-groups-command.md](ebook/en/content/023-the-groups-command.md)
- [024-the-man-command.md](ebook/en/content/024-the-man-command.md)
- [025-the-passwd-command.md](ebook/en/content/025-the-passwd-command.md)
- [026-the-w-command.md](ebook/en/content/026-the-w-command.md)
- [027-the-whoami-command.md](ebook/en/content/027-the-whoami-command.md)
- [028-the-history-command.md](ebook/en/content/028-the-history-command.md)
- [029-the-login-command.md](ebook/en/content/029-the-login-command.md)
- [030-the-lscpu-command.md](ebook/en/content/030-the-lscpu-command.md)
- [031-the-cp-command.md](ebook/en/content/031-the-cp-command.md)
- [032-the-mv-command.md](ebook/en/content/032-the-mv-command.md)
- [033-the-ps-command.md](ebook/en/content/033-the-ps-command.md)
- [034-the-kill-command.md](ebook/en/content/034-the-kill-command.md)
- [035-the-killall-command.md](ebook/en/content/035-the-killall-command.md)
- [036-the-env-command.md](ebook/en/content/036-the-env-command.md)
- [037-the-printenv-command.md](ebook/en/content/037-the-printenv-command.md)
- [038-the-hostname-command.md](ebook/en/content/038-the-hostname-command.md)
- [039-the-nano-command.md](ebook/en/content/039-the-nano-command.md)
- [040-the-rm-command.md](ebook/en/content/040-the-rm-command.md)
- [041-the-ifconfig-command.md](ebook/en/content/041-the-ifconfig-command.md)
- [042-the-ip-command.md](ebook/en/content/042-the-ip-command.md)
- [043-the-clear-command.md](ebook/en/content/043-the-clear-command.md)
- [044-the-su-command.md](ebook/en/content/044-the-su-command.md)
- [045-the-wget-command.md](ebook/en/content/045-the-wget-command.md)
- [046-the-curl-command.md](ebook/en/content/046-the-curl-command.md)
- [047-the-yes-command.md](ebook/en/content/047-the-yes-command.md)
- [048-the-last-command.md](ebook/en/content/048-the-last-command.md)
- [049-the-locate-command.md](ebook/en/content/049-the-locate-command.md)
- [050-the-iostat-command.md](ebook/en/content/050-the-iostat-command.md)
- [051-the-sudo-command.md](ebook/en/content/051-the-sudo-command.md)
- [052-the-apt-command.md](ebook/en/content/052-the-apt-command.md)
- [053-the-yum-command.md](ebook/en/content/053-the-yum-command.md)
- [054-the-zip-command.md](ebook/en/content/054-the-zip-command.md)
- [055-the-unzip-command.md](ebook/en/content/055-the-unzip-command.md)
- [056-the-shutdown-command.md](ebook/en/content/056-the-shutdown-command.md)
- [057-the-dir-command.md](ebook/en/content/057-the-dir-command.md)
- [058-the-reboot-command.md](ebook/en/content/058-the-reboot-command.md)
- [059-the-sort-command.md](ebook/en/content/059-the-sort-command.md)
- [060-the-paste-command.md](ebook/en/content/060-the-paste-command.md)
- [061-the-exit-command.md](ebook/en/content/061-the-exit-command.md)
- [062-the-diff-sdiff-command.md](ebook/en/content/062-the-diff-sdiff-command.md)
- [063-the-tar-command.md](ebook/en/content/063-the-tar-command.md)
- [064-the-gunzip-command.md](ebook/en/content/064-the-gunzip-command.md)
- [065-the-hostnamectl-command.md](ebook/en/content/065-the-hostnamectl-command.md)
- [066-the-iptables-command.md](ebook/en/content/066-the-iptables-command.md)
- [067-the-netstat-command.md](ebook/en/content/067-the-netstat-command.md)
- [068-the-lsof-command.md](ebook/en/content/068-the-lsof-command.md)
- [069-the-bzip2-command.md](ebook/en/content/069-the-bzip2-command.md)
- [070-the-service-command.md](ebook/en/content/070-the-service-command.md)
- [071-the-vmstat-command.md](ebook/en/content/071-the-vmstat-command.md)
- [072-the-mpstat-command.md](ebook/en/content/072-the-mpstat-command.md)
- [073-the-ncdu-command.md](ebook/en/content/073-the-ncdu-command.md)
- [074-the-uniq-command.md](ebook/en/content/074-the-uniq-command.md)
- [075-the-rpm-command.md](ebook/en/content/075-the-rpm-command.md)
- [076-the-scp-command.md](ebook/en/content/076-the-scp-command.md)
- [077-the-sleep-command.md](ebook/en/content/077-the-sleep-command.md)
- [078-the-split-command.md](ebook/en/content/078-the-split-command.md)
- [079-the-stat-command.md](ebook/en/content/079-the-stat-command.md)
- [080-the-useradd-command.md](ebook/en/content/080-the-useradd-command.md)
- [081-the-userdel-command.md](ebook/en/content/081-the-userdel-command.md)
- [082-the-usermod-command.md](ebook/en/content/082-the-usermod-command.md)
- [083-the-ionice-command.md](ebook/en/content/083-the-ionice-command.md)
- [084-the-du-command.md](ebook/en/content/084-the-du-command.md)
- [085-the-ping-command.md](ebook/en/content/085-the-ping-command.md)
- [086-the-rsync-command.md](ebook/en/content/086-the-rsync-command.md)
- [087-the-dig-command.md](ebook/en/content/087-the-dig-command.md)
- [088-the-whois-command.md](ebook/en/content/088-the-whois-command.md)
- [089-the-ssh-command.md](ebook/en/content/089-the-ssh-command.md)
- [090-the-awk-command.md](ebook/en/content/090-the-awk-command.md)
- [091-the-crontab-command.md](ebook/en/content/091-the-crontab-command.md)
- [092-the-xargs-command.md](ebook/en/content/092-the-xargs-command.md)
- [093-the-nohup-command.md](ebook/en/content/093-the-nohup-command.md)
- [094-the-pstree-command.md](ebook/en/content/094-the-pstree-command.md)
- [095-the-tree-command.md](ebook/en/content/095-the-tree-command.md)
- [096-the-whereis-command.md](ebook/en/content/096-the-whereis-command.md)
- [097-the-printf-command.md](ebook/en/content/097-the-printf-command.md)
- [098-the-cut-command.md](ebook/en/content/098-the-cut-command.md)
- [099-the-sed-command.md](ebook/en/content/099-the-sed-command.md)
- [100-the-vim-command.md](ebook/en/content/100-the-vim-command.md)
- [101-the-chown-command.md](ebook/en/content/101-the-chown-command.md)
- [102-the-find-command.md](ebook/en/content/102-the-find-command.md)
- [103-the-rmdir-command.md](ebook/en/content/103-the-rmdir-command.md)
- [104-the-lsblk-command.md](ebook/en/content/104-the-lsblk-command.md)
- [105-the-cmatrix-command.md](ebook/en/content/105-the-cmatrix-command.md)
- [106-the-chmod-command.md](ebook/en/content/106-the-chmod-command.md)
- [107-the-grep-command.md](ebook/en/content/107-the-grep-command.md)
- [108-the-screen-command.md](ebook/en/content/108-the-screen-command.md)
- [109-the-nc-command.md](ebook/en/content/109-the-nc-command.md)
- [110-the-make-command.md](ebook/en/content/110-the-make-command.md)
- [111-the-basename-command.md](ebook/en/content/111-the-basename-command.md)
- [112-the-banner-command.md](ebook/en/content/112-the-banner-command.md)
- [113-the-alias-command.md](ebook/en/content/113-the-alias-command.md)
- [114-the-which-command.md](ebook/en/content/114-the-which-command.md)
- [115-the-date-command.md](ebook/en/content/115-the-date-command.md)
- [116-the-mount-command.md](ebook/en/content/116-the-mount-command.md)
- [117-the-nice-command.md](ebook/en/content/117-the-nice-command.md)
- [118-the-wc-command.md](ebook/en/content/118-the-wc-command.md)
- [119-the-tr-command.md](ebook/en/content/119-the-tr-command.md)
- [120-the-fdisk-command.md](ebook/en/content/120-the-fdisk-command.md)
- [121-the-wait-command.md](ebook/en/content/121-the-wait-command.md)
- [122-the-zcat-command.md](ebook/en/content/122-the-zcat-command.md)
- [123-the-fold-command.md](ebook/en/content/123-the-fold-command.md)
- [124-the-quota-command.md](ebook/en/content/124-the-quota-command.md)
- [125-the-aplay-command.md](ebook/en/content/125-the-aplay-command.md)
- [126-the-spd-say-command.md](ebook/en/content/126-the-spd-say-command.md)
- [127-the-xeyes-command.md](ebook/en/content/127-the-xeyes-command.md)
- [128-the-parted-command.md](ebook/en/content/128-the-parted-command.md)
- [129-the-nl-command.md](ebook/en/content/129-the-nl-command.md)
- [130-the-pidof-command.md](ebook/en/content/130-the-pidof-command.md)
- [131-the-shuf-command.md](ebook/en/content/131-the-shuf-command.md)
- [132-the-less-command.md](ebook/en/content/132-the-less-command.md)
- [133-the-nslookup-command.md](ebook/en/content/133-the-nslookup-command.md)
- [134-the-cmp-command.md](ebook/en/content/134-the-cmp-command.md)
- [135-the-expr-command.md](ebook/en/content/135-the-expr-command.md)
- [136-the-wall-command.md](ebook/en/content/136-the-wall-command.md)
- [137-the-ln-command.md](ebook/en/content/137-the-ln-command.md)
- [138-the-systemctl-command.md](ebook/en/content/138-the-systemctl-command.md)
- [139-the-journalctl-command.md](ebook/en/content/139-the-journalctl-command.md)
- [140-the-watch-command.md](ebook/en/content/140-the-watch-command.md)
- [141-the-jobs-command.md](ebook/en/content/141-the-jobs-command.md)
- [142-the-bg-command.md](ebook/en/content/142-the-bg-command.md)
- [143-the-fg-command.md](ebook/en/content/143-the-fg-command.md)
- [144-the-time-command.md](ebook/en/content/144-the-time-command.md)
- [145-the-export-command.md](ebook/en/content/145-the-export-command.md)
- [146-the-ufw-command.md](ebook/en/content/146-the-ufw-command.md)
- [147-the-traceroute-command.md](ebook/en/content/147-the-traceroute-command.md)
- [148-the-nmcli-command.md](ebook/en/content/148-the-nmcli-command.md)
- [149-the-badblocks-command.md](ebook/en/content/149-the-badblocks-command.md)
- [150-the-fsck-command.md](ebook/en/content/150-the-fsck-command.md)
- [151-the-mkfs-command.md](ebook/en/content/151-the-mkfs-command.md)
- [152-the-cpio-command.md](ebook/en/content/152-the-cpio-command.md)
- [153-the-lsb_release-command.md](ebook/en/content/153-the-lsb_release-command.md)
- [154-the-dmidecode-command.md](ebook/en/content/154-the-dmidecode-command.md)
- [155-the-apropos-command.md](ebook/en/content/155-the-apropos-command.md)
- [156-the-dmesg-command.md](ebook/en/content/156-the-dmesg-command.md)
- [157-the-bangbang-command.md](ebook/en/content/157-the-bangbang-command.md)
- [158-the-tty-command.md](ebook/en/content/158-the-tty-command.md)
- [159-the-lspci-command.md](ebook/en/content/159-the-lspci-command.md)
- [160-the-cfdisk-command.md](ebook/en/content/160-the-cfdisk-command.md)
- [161-the-column-command.md](ebook/en/content/162-the-column-command.md)
- [162-the-nmtui-command.md](ebook/en/content/161-the-nmtui-command.md)

# 🔗Links

- [Free $200 Credit For DigitalOcean](https://m.do.co/c/2a9bba940f39)
- [Join DevDojo](https://devdojo.com?ref=bobbyiliev)
- [Ibis Next](https://github.com/Hi-Folks/ibis-next)
- [Canva](https://www.canva.com/join/determined-cork-learn)
- [Tails](http://devdojo.com/tails)

# 📖Other eBooks

- [Introduction to SQL](https://github.com/bobbyiliev/introduction-to-sql)
- [Introduction to Git and GitHub](https://github.com/bobbyiliev/introduction-to-git-and-github-ebook)
- [Introduction to Bash Scripting](https://github.com/bobbyiliev/introduction-to-bash-scripting)
- [Laravel tips and tricks](https://github.com/bobbyiliev/laravel-tips-and-tricks-ebook)

# 📚 eBook Generation

This project uses [Ibis Next](https://github.com/Hi-Folks/ibis-next) to generate eBooks in multiple formats:

## Quick Start

1. Install dependencies:

```bash
composer install
```

2. Generate eBooks:

```bash
# Generate PDF (light theme)
composer run pdf

# Generate PDF (dark theme)
composer run pdf-dark

# Generate EPUB
composer run epub

# Generate HTML
composer run html
```

## Available Formats

- **PDF**: Available in both light and dark themes, perfect for printing or desktop reading
- **EPUB**: Compatible with most e-readers, tablets, and mobile devices
- **HTML**: Single-page HTML version, great for web viewing and sharing

All generated files are saved in the `ebook/en/export/` directory.

---

# 🤲Contributing

If you are contributing 🍿 please read the [contributing file](CONTRIBUTING.md) before submitting your pull requests.
