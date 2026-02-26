# The `touch` Command
The `touch` command modifies a file's timestamps. If the file specified doesn't exist, an empty file with that name is created.


### Syntax
```
touch [OPTION]... FILE...
```

### Options
|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-a`|<center>-</center>|Change only the access time.|
|`-c`|`--no-create`|Do not create any files.|
|`-d` STRING|`--date=STRING`|Parse *STRING* and use it instead of the current time.|
|`-f`|<center>-</center>|(Ignored) This option does nothing but is accepted to provide compatibility with BSD versions of the `touch` command.|
|`-h`|`--no-dereference`|Affect each symbolic link instead of any referenced file (useful only on systems that can change the timestamps of a symlink). This option implies `-c`, nothing is created if the file does not exist.|
|`-m`|<center>-</center>|Change only the modification time.|
|`-r=FILE`|`--reference=FILE`|Use this file's times instead of the current time.|
|`-t STAMP`|<center>-</center>|Use the numeric time  *STAMP*  instead of the current time. The format of *STAMP*  is [[**CC**]**YY**]**MMDDhhmm**[**.ss**].|
|<center>-</center>|`--time=WORD`|An alternate way to specify which type of time is set (e.g. *access*, *modification*, or *change*). This is equivalent to specifying `-a` or `-m`- WORD is `access`, `atime` : equivalent to `-a` or WORD is `modify` or `mtime` : equivalent to `-m`.

An alternate way to specify what type of time to set (as with  **-a**  and  **-m**).|
|<center>-</center>|`--help`|Display a help message, and exit.|
|<center>-</center>|`--version`|Display version information, and exit.|

### Examples
1. If **file.txt** exists, set all of its timestamps to the current system time. If **file.txt** doesn't exist, create an empty file with that name.
```
touch file.txt
```

2. If **file.txt** exists, set its times to the current system time. If it does not exist, do nothing.
```
touch -c file.txt
```

3. Change the *access* time of **file.txt**. The *modification* time is not changed. The *change* time is set to the current system time. If **file.txt** does not exist, it is created.
```
touch -a file.txt
```

4. Change the times of file **symboliclink**. If it's a symbolic link, change the times of the symlink, ***NOT*** the times of the referenced file.
```
touch -h symboliclink
```

5. Change the *access* and *modification* times of **file-b.txt** to match the times of **file-a.txt**. The *change* time will be set to the current system time. If **file-b.txt** does not exist, it is not created. Note, **file-a.txt** must already exist in this context.
```
touch -cr file-a.txt file-b.txt
```

6. Set the *access* time and *modification* time of **file.txt** to ***February 1st*** of the current year. The *change* time is set to the current system time.
```
touch -d "1 Feb" file.txt
```
