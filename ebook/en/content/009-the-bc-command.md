# The `bc` command

The `bc` command provides the functionality of being able to perform mathematical calculations through the command line.

### Examples:

1 . Arithmetic:

```
Input : $ echo "11+5" | bc
Output : 16
```
2 . Increment:
- var++ : Post increment operator, the result of the variable is used first and then the variable is incremented.
- ++var : Pre increment operator, the variable is increased first and then the result of the variable is stored.

```
Input: $ echo "var=3;++var" | bc
Output: 4
```
3 . Decrement:
- var–– : Post decrement operator, the result of the variable is used first and then the variable is decremented.
- ––var : Pre decrement operator, the variable is decreased first and then the result of the variable is stored.

```
Input: $ echo "var=3;--var" | bc
Output: 2
```
4 . Assignment:
- var = value : Assign the value to the variable
- var += value : similar to var = var + value
- var -= value : similar to var = var – value
- var *= value : similar to var = var * value
- var /= value : similar to var = var / value
- var ^= value : similar to var = var ^ value
- var %= value : similar to var = var % value

```
Input: $ echo "var=4;var" | bc
Output: 4
```
5 . Comparison or Relational:
- If the comparison is true, then the result is 1. Otherwise,(false), returns 0
- expr1<expr2 : Result is 1, if expr1 is strictly less than expr2.
- expr1<=expr2 : Result is 1, if expr1 is less than or equal to expr2.
- expr1>expr2 : Result is 1, if expr1 is strictly greater than expr2.
- expr1>=expr2 : Result is 1, if expr1 is greater than or equal to expr2.
- expr1==expr2 : Result is 1, if expr1 is equal to expr2.
- expr1!=expr2 : Result is 1, if expr1 is not equal to expr2.

```
Input: $ echo "6<4" | bc
Output: 0
```
```
Input: $ echo "2==2" | bc
Output: 1
```
6 . Logical or Boolean:

- expr1 && expr2 : Result is 1, if both expressions are non-zero.
- expr1 || expr2 : Result is 1, if either expression is non-zero.
- ! expr : Result is 1, if expr is 0.

```
Input: $ echo "! 1" | bc
Output: 0

Input: $ echo "10 && 5" | bc
Output: 1
```

### Syntax:

```
bc [ -hlwsqv ] [long-options] [  file ... ]
```

### Additional Flags and their Functionalities:

*Note: This does not include an exhaustive list of options.*

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-i`|`--interactive`|Force interactive mode|
|`-l`|`--mathlib`|Use the predefined math routines|
|`-q`|`--quiet`|Opens the interactive mode for bc without printing the header|
|`-s`|`--standard`|Treat non-standard bc constructs as errors|
|`-w`|`--warn`|Provides a warning if non-standard bc constructs are used|

### Notes:

1. The capabilities of `bc` can be further appreciated if used within a script. Aside from basic arithmetic operations, `bc` supports increments/decrements, complex calculations, logical comparisons, etc.
2. Two of the flags in `bc` refer to non-standard constructs. If you evaluate `100>50 | bc` for example, you will get a strange warning. According to the POSIX page for bc, relational operators are only valid if used within an `if`, `while`, or `for` statement.
