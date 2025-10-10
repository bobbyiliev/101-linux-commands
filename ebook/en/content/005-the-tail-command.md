# The `tail` command

The `tail` command prints the last ten lines of a file.

Example:
```
tail filename.txt
```

Syntax:
```
tail [OPTION] [FILENAME]
```

## Common Use Cases

### Get a specific number of lines:

Use the `-n` option with a number (should be an integer) of lines to display.

Example:
```
tail -n 10 foo.txt
```

This command will display the last ten lines of the file `foo.txt`.

### Monitor new entry on files in real-time

It is possible to let tail output any new line added to the file you are looking into. So, if a new line is written to the file, it will immediately be shown in your output. This can be done using the `--follow` or `-f` option. This is especially useful for monitoring log files.

Example:
```
tail -f foo.txt
```
Press `Ctrl+C` to stop following.

### Combine options for log monitoring

```
tail -n 100 -f app.log      # Show last 100 lines, then follow
tail -f -s 2 slow.log       # Follow with 2-second refresh interval
```

### Follow multiple files simultaneously

```
tail -f /var/log/nginx/access.log /var/log/nginx/error.log
```

### Display specific byte ranges

```
tail -c 100 file.txt        # Last 100 bytes
tail -c +50 file.txt        # From byte 50 to end
```

### Follow logs even after rotation

```
tail -F /var/log/app.log
```
The `-F` option is crucial for monitoring logs managed by logrotate.

### Skip header lines

```
tail -n +2 data.csv         # Start from line 2 (skip header)
tail -n +11 file.txt        # Start from line 11 onwards
```

### Quiet mode for multiple files

```
tail -q -n 5 *.log          # No filename headers
```

### Additional Flags and their Functionalities

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-c`|`--bytes=[+]NUM`|Output the last NUM bytes;<br> or use -c +NUM to <br>output starting with byte NUM of each file|
|`-f`|<code>--follow[={name&#124;descriptor}]</code>|Output appended data as the file grows;<br>an absent option argument means 'descriptor'|
|`-F`||Same as --follow=name --retry|
|`-n`|`--lines=[+]NUM`|Output the last NUM lines, instead of the last 10;<br>or use -n +NUM to output starting with line NUM|
||`--max-unchanged-stats=N`|with --follow=name, reopen a FILE which has not<br>changed size after N (default 5) iterations<br>to see if it has been unlinked or rename<br>(this is the usual case of rotated log files);<br>with inotify, this option is rarely useful|
||`--pid=PID`|with -f, terminate after process ID, PID dies|
|`-q`|`--quiet, --silent`|Never output headers giving file names|
||`--retry`|keep trying to open a file if it is inaccessible|
|`-s`|`--sleep-interval=N`|With -f, sleep for approximately N seconds<br>(default 1.0) between iterations;<br>with inotify and --pid=P, check process P at<br>least once every N seconds|
|`-v`|`--verbose`|Always output headers giving file names|
|`-z`|`--zero-terminated`|Line delimiter is NUL, not newline|
||`--help`|Display this help and exit|
||`--version`|Output version information and exit|

## Tips

- Use `-F` instead of `-f` for production log monitoring
- Combine with `grep`, `awk`, or `sed` for filtered monitoring
- For large files, `tail` is much faster than opening in an editor
- Use `-n +N` to start from a specific line (useful for skipping headers)
