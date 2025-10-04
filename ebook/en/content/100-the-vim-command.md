# The `vim` command

The [vim](https://www.vim.org/) is a text editor for Unix that comes with Linux, BSD, and macOS. It is known to be fast and powerful, partly because it is a small program that can run in a terminal (although it has a graphical interface). 
Vim text editor is developed by [Bram Moolenaar](https://en.wikipedia.org/wiki/Bram_Moolenaar). It supports most file types and the vim editor is also known as a programmer's editor. It is mainly because it can be managed entirely without menus or a mouse with a keyboard.

**Note:** Do not confuse `vim` with `vi`. `vi`, which stands for "Visual", is a text editor that was developed by [Bill Joy](https://en.wikipedia.org/wiki/Bill_Joy) in 1976. `vim` stands for "Vi Improved", and is an improved clone of the `vi` editor.

### The most searched question about ```vim``` :
``How to exit vim editor?``

The most searched question about vim editor looks very funny but it's true that the new user gets stuck at the very beginning when using vim editor.

The command to save the file and exit vim editor: ```:wq``` or ```:x```

The command to exit vim editor without saving the file: ```:q!```

#### Fun reading:
Here's a [survey](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/) for the same question, look at this and do not think to quit the vim editor.

### Installation:
First check if vim is already installed or not, enter the following command:
```
vim --version
```
If it is already installed it will show its version, else we can run the below commands for the installations:

On Ubuntu/Debian:

```
sudo apt-get install vim
```

On Arch:

```
sudo pacman -S vim
```

On CentOS/Fedora:

```
sudo yum install vim
```
If you want to use advanced features on CentOS/Fedora, you'll need to install enhanced vim editor, to do this run the following command:

```
sudo yum install -y vim-enhanced
```

On macOS:

```
brew install vim
```

### Syntax:

```
vim [FILE_PATH/FILE_NAME]
```

### Examples:

1. To open the file named "demo.txt" from your current directory:

```
vim demo.txt
```

2. To open the file in a specific directory:

```
vim {File_Path/filename}
```

3. To open the file starting on a specific line in the file:

```
vim {File_Path/filename} +LINE_NUMBER
```
### Modes in vim editor: 
There are some arguments as to how many modes that vim has, but the modes you're most likely to use are ```command mode``` and ```insert mode```. These [modes](https://www.freecodecamp.org/news/vim-editor-modes-explained/) will allow you to do just about anything you need, including creating your document, saving your document, and doing advanced editing, including taking advantage of search and replace functions.

### Workflow of `vim` editor:
1. Open a new or existing file with ```vim filename```.
2. Type ```i``` to switch into insert mode so that you can start editing the file.
3. Enter or modify the text of your file.
4. When you're done, press the ```Esc``` key to exit insert mode and back to command mode.
5. Type :w or :wq to save the file or save and exit from the file respectively.

### Navigate in vim
Some common commands:

- `j` : move down one line
- `k` : move up one line
- `h` : Move left one character
- `l` : move right one character
- `w` : move forward one word
- `b` : move backward one word
- `e` : Move to the end of your word
- `0` : move to begining of line
- `$` : move to end of line
- `gg` : go to begining of file
- `G` : go to end of file
- `:linenumber` : go to a specific line number

### Copy, Paste and Delete
1. Copy(Yank):
Copying in vim is called "yanking":

- `yy` : yank (copy) the current line
- `2yy` : yank 2 lines
- `y$` : yank from cursor to end of line
- `y^` : yank from cursor to begining of line
- `yw` : yank one word
- `y}` : yank until end of paragraph

2. Paste:

- `p` : paste after the cursor
- `P` : paste before the cursor

3. Delete:

- `x` : delete a single character
- `dd` : delete the whole current line
- `2dd` : delete 2 lines (or use any number `n dd`)
- `d$` : delete from cursor to end of line
- `d^` : delete from cursor to begining of line
- `dG` : delete from cursor to end of file
- `dgg`:  delete from cursor to begining of file
- `dw` : delete from cursor to end of word
- `di"` : delete inside double quotes
- `diw` : delete inner word (without spaces)
- `dip` : delete inner paragraph (no newline)

### Selection (visual mode)

- `v` : start character-wise selection
- `V` : start line-wise selection
- `ctrl + v`  : start block-wise selection

### Interactive training

In this interactive tutorial, you will learn the different ways to use the `vim` command:

[The Open vim Tutorial](https://www.openvim.com/)

### Additional Flags and their Functionalities:

|**Flags/Options**  |<center>**Description**</center>   |
|:---|:---|
|`-e`|Start in Ex mode (see [Ex-mode](http://vimdoc.sourceforge.net/htmldoc/intro.html#Ex-mode))|
|`-R`|Start in read-only mode|
|`-R`|Start in read-only mode|
|`-g`|Start the [GUI](http://vimdoc.sourceforge.net/htmldoc/gui.html#GUI)|
|`-eg`|Start the GUI in Ex mode|
|`-Z`|Like "vim", but in restricted mode|
|`-d`|Start in diff mode [diff-mode](http://vimdoc.sourceforge.net/htmldoc/diff.html#diff-mode)|
|`-h`|Give usage (help) message and exit|
|`+NUMBER`|Open a file and place the cursor on the line number specified by NUMBER|

### Read more about vim: 

vim can not be learned in a single day, use in day-to-day tasks to get hands-on in vim editor.

To learn more about ```vim``` follow the given article:

[Article By Daniel Miessler](https://danielmiessler.com/study/vim/) 

