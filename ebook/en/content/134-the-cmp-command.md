# The `cmp` command

The `cmp` command is a simple utility used to compare two files byte by byte. 

If the files are identical, `cmp` produces no output and returns a successful exit status. If the files differ, it reports the byte and line number where the first difference occurred.

## Syntax
```bash
$ cmp [OPTION]... FILE1 [FILE2]
```

## Examples :

For the following examples, let's assume we have three files:

file1.txt:
```bash
hello world
```

file2.txt:
```bash
hello world
```

file3.txt:
```bash
hello World
```

### 1. Comparing two identical files
When the files are the same, cmp will produce no output. This is the standard way to confirm that two files are identical.

```bash
$ cmp file1.txt file2.txt
```
(No output is shown)

### 2. Comparing two different files
When a difference is found, cmp reports the location of the first differing byte.

```bash
$ cmp file1.txt file3.txt
file1.txt file3.txt differ: byte 7, line 1
```

### 3. Displaying all differing bytes (--verbose or -l)
The -l (lowercase L) flag is very powerful. It prints the byte number (in decimal) and the value of the differing bytes (in octal) for every difference in the files.

```bash
$ cmp -l file1.txt file3.txt
 7 167 127
```

#### Explanation: 
This output means that at byte position 7, file1.txt has the octal value 167 (the letter 'w'), while file3.txt has the octal value 127 (the letter 'W').

### 4. Comparing only the first "n" bytes (--bytes or -n)
You can limit the comparison to a certain number of bytes. Here, we only compare the first 5 bytes. Since "hello" is the same in both files, cmp finds no difference.

```bash
$ cmp -n 5 file1.txt file3.txt
```
(No output is shown)

### 5. Ignoring the initial "n" bytes (--ignore-initial or -i)
You can tell cmp to skip a certain number of bytes at the beginning of the files before starting its comparison. Here, we skip the first 6 bytes, so the comparison starts at the letter 'w'.

```bash
$ cmp -i 6 file1.txt file3.txt
file1.txt file3.txt differ: byte 1, line 1
```
#### Explanation: 
The output now says the difference is at "byte 1" because the comparison started after the initial 6 bytes were ignored.

### Common Options

| Short Flag | Long Flag                  | Description                                             |
|------------|----------------------------|---------------------------------------------------------|
| -b         | --print-bytes              | Print the differing bytes.                             |
| -i SKIP    | --ignore-initial=SKIP      | Skip the first SKIP bytes of both files.               |
| -l         | --verbose                  | Output the byte number and the values of all differing bytes. |
| -n LIMIT   | --bytes=LIMIT              | Compare at most LIMIT bytes.                           |
| -s         | --quiet, --silent          | Suppress all output. Only return an exit status.       |