# The `ls` command

The `ls` command lets you see the files and directories inside a specific directory *(current working directory by default)*.
It normally lists the files and directories in ascending alphabetical order.

### Examples:

1. To show the files inside your current working directory:

```
ls
```

2. To show the files and directory inside a specific Directory:

```
ls {Directory_Path}
```

3. List all files including hidden ones in long format with human-readable sizes:

```
ls -lah
```

4. Sort files by modification time, newest first:

```
ls -lt
```

5. List files by size, largest first:

```
ls -lhS
```

6. Show only directories in the current path:

```
ls -d */
```

7. List all text files with details:

```
ls -lh *.txt
```

8. Recursively list all files in subdirectories:

```
ls -R
```

### Syntax:

```
ls [-OPTION] [DIRECTORY_PATH]
```

### Interactive training

In this interactive tutorial, you will learn the different ways to use the `ls` command:

[The ls command by Tony](https://devdojo.com/tnylea/ls-command)

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-l`|<center>-</center>|Show results in long format|
|`-S`|<center>-</center>|Sort results by file size|
|`-t`|<center>-</center>|Sort results by modification time|
|`-r`|`--reverse`|Show files and directories in reverse order *(descending alphabetical order)*|
|`-a`|`--all`|Show all files, including hidden files *(file names which begin with a period `.`)*|
|`-la`|<center>-</center>|Show long format files and directories including hidden files|
|`-lh`|<center>-</center>|list long format files and directories with readable size|
|`-A`|`--almost-all`|Shows all like `-a` but without showing `.`(current working directory) and `..` (parent directory)|
|`-d`|`--directory`|Instead of listing the files and directories inside the directory, it shows any information about the directory itself, it can be used with `-l` to show long formatted information|
|`-F`|`--classify`|Appends an indicator character to the end of each listed name, as an example: `/` character is appended after each directory name listed|
|`-h`|`--human-readable`|like `-l` but displays file size in human-readable unit not in bytes|
|`-i`|`--inode`|Display inode number for each file|
|`-R`|`--recursive`|List subdirectories recursively|
|`-1`|<center>-</center>|List one file per line|
|`-c`|<center>-</center>|Sort by change time (when file metadata was last changed)|
|`-u`|<center>-</center>|Sort by access time (when file was last accessed)|
|`-X`|<center>-</center>|Sort alphabetically by file extension|
|<center>-</center>|`--color=auto`|Colorize output to distinguish file types|
|`-g`|<center>-</center>|Like `-l` but without showing owner|
|`-o`|<center>-</center>|Like `-l` but without showing group|
|`-C`|<center>-</center>|List entries by columns|
|<center>-</center>|`--group-directories-first`|List directories before files|


### File Type Indicators:

When using the `-F` or `--classify` flag, `ls` appends special characters to filenames to indicate their type:

|**Indicator**|**File Type**|**Example**|
|:---|:---|:---|
|`/`|Directory|`docs/`|
|`*`|Executable file|`script.sh*`|
|`@`|Symbolic link|`link@`|
|`\|`|FIFO (named pipe)|`pipe\|`|
|`=`|Socket|`socket=`|
|No indicator|Regular file|`file.txt`|

**Example:**

```bash
ls -F
documents/  script.sh*  link@  data.txt  pipe|  socket=
```


### SELinux Support on Red Hat-Based Systems:

On Red Hat-based distributions (RHEL, CentOS, Fedora, Rocky Linux, AlmaLinux) that use SELinux, the `ls` command provides additional options to display SELinux security context information:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-Z`|`--context`|Display SELinux security context for files and directories|
|`-lZ`|<center>-</center>|Show long format with SELinux security context|

**Example Output:**

```bash
ls -Z
unconfined_u:object_r:user_home_t:s0 file.txt
unconfined_u:object_r:user_home_t:s0 directory
```

```bash
ls -lZ
-rw-rw-r--. 1 user user unconfined_u:object_r:user_home_t:s0 1234 Jan 15 10:30 file.txt
drwxrwxr-x. 2 user user unconfined_u:object_r:user_home_t:s0 4096 Jan 15 10:25 directory
```

The SELinux context format is: `user:role:type:level`

**Note:** The `-Z` option is only functional on systems with SELinux enabled. On non-SELinux systems, this option may not be available or will show no additional information.


### Understanding Long Format Output:

When using `ls -l`, each line displays detailed information about a file or directory:

```bash
-rw-r--r-- 1 user group 1234 Jan 15 10:30 file.txt
```

**Column breakdown:**

1. **File Type and Permissions** (`-rw-r--r--`):
   - First character: File type (`-` = regular file, `d` = directory, `l` = symlink, `b` = block device, `c` = character device, `p` = pipe, `s` = socket)
   - Next 9 characters: Permissions in three groups (owner, group, others)
     - `r` = read, `w` = write, `x` = execute, `-` = no permission

2. **Link Count** (`1`): Number of hard links to the file

3. **Owner** (`user`): Username of the file owner

4. **Group** (`group`): Group name that owns the file

5. **Size** (`1234`): File size in bytes (use `-h` flag for human-readable format like `1.2K`, `3.4M`)

6. **Modification Time** (`Jan 15 10:30`): Date and time the file was last modified

7. **Filename** (`file.txt`): Name of the file or directory

**Example with human-readable sizes:**

```bash
ls -lh
drwxr-xr-x 2 user group 4.0K Jan 15 10:25 documents
-rwxr-xr-x 1 user group 2.3M Jan 14 09:15 script.sh
-rw-r--r-- 1 user group  15K Jan 16 14:30 data.csv
```


### Using Wildcards and Patterns:

The `ls` command supports wildcards for pattern matching:

|**Wildcard**|**Description**|**Example**|**Matches**|
|:---|:---|:---|:---|
|`*`|Matches any number of characters|`ls *.txt`|All files ending with `.txt`|
|`?`|Matches exactly one character|`ls file?.txt`|`file1.txt`, `file2.txt`, but not `file10.txt`|
|`[]`|Matches any character within brackets|`ls file[123].txt`|`file1.txt`, `file2.txt`, `file3.txt`|
|`[!]`|Matches any character NOT in brackets|`ls file[!3].txt`|`file1.txt`, `file2.txt`, but not `file3.txt`|
|`{}`|Matches any of the comma-separated patterns|`ls *.{jpg,png,gif}`|All image files with these extensions|

**Examples:**

```bash
# List all PDF and DOCX files
ls *.{pdf,docx}

# List files starting with 'test' followed by a single digit
ls test?.log

# List all files starting with uppercase letters
ls [A-Z]*

# List all hidden configuration files
ls .config*
```


### SELinux Support on Red Hat-Based Systems:

On Red Hat-based distributions (RHEL, CentOS, Fedora, Rocky Linux, AlmaLinux) that use SELinux, the `ls` command provides additional options to display SELinux security context information:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-Z`|`--context`|Display SELinux security context for files and directories|
|`-lZ`|<center>-</center>|Show long format with SELinux security context|

**Example Output:**

```bash
ls -Z
unconfined_u:object_r:user_home_t:s0 file.txt
unconfined_u:object_r:user_home_t:s0 directory
```

```bash
ls -lZ
-rw-rw-r--. 1 user user unconfined_u:object_r:user_home_t:s0 1234 Jan 15 10:30 file.txt
drwxrwxr-x. 2 user user unconfined_u:object_r:user_home_t:s0 4096 Jan 15 10:25 directory
```

The SELinux context format is: `user:role:type:level`

**Note:** The `-Z` option is only functional on systems with SELinux enabled. On non-SELinux systems, this option may not be available or will show no additional information.


### Setting Persistent Options:


Customizing command behavior in Linux is easy using the `alias` command. To make these changes permanent, follow these steps:

1. **Create the Alias**: Define your alias with the desired options. For example, to enhance the `ls` command:

    ```bash
    alias ls="ls --color=auto -lh"
    ```

2. **Persistence**: This alias is effective only for the current session. To make it permanent, add the alias to your shell's configuration file:

    - **Bash**: Append the alias to `~/.bashrc`:

        ```bash
        echo 'alias ls="ls --color=auto -lh"' >> ~/.bashrc
        source ~/.bashrc
        ```

3. **Verification**: Open a new terminal session, and the `ls` command will display files as configured.


### Performance Tips:

**1. Avoid recursive listing on large directories:**
   - The `-R` flag can be slow on directories with many subdirectories and files
   - Consider using `find` command for more control: `find /path -type f`

**2. Disable color output in scripts:**
   - Use `--color=never` when piping output or in scripts to improve performance
   - Example: `ls --color=never | grep pattern`

**3. Limit output for large directories:**
   - Combine with `head` to see only first few entries: `ls -1 | head -n 20`
   - Or use `ls -1 | wc -l` to just count files without displaying them

**4. Use specific paths instead of wildcards when possible:**
   - `ls /var/log/syslog` is faster than `ls /var/log/sys*` when you know the exact filename


### Common Use Cases:

**1. Find the largest files in a directory:**

```bash
ls -lhS | head -n 10
```

**2. List only directories:**

```bash
ls -d */
```

Or with full details:

```bash
ls -ld */
```

**3. Count files in a directory:**

```bash
ls -1 | wc -l
```

**4. List files modified in the last 24 hours:**

```bash
ls -lt | head
```

**5. Show files sorted by extension:**

```bash
ls -lX
```

**6. List files with their inode numbers (useful for debugging):**

```bash
ls -li
```

**7. Display directory contents one per line (useful for scripting):**

```bash
ls -1
```

**8. Combine multiple sort options (size + reverse):**

```bash
ls -lhSr
```


