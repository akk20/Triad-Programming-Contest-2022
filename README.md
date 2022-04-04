# Triad Programming Contest 2022
Repository for the 2022 Spring Triad Programming Contest. Much easier to read than the original website.

## Problem A: Password Validator

Write a program that will validate a password.

Passwords must have,
1. `8` to `32` characters
2. at least one numeric digit
3. at least one uppercase letter
4. at least one lowercase letter
5. must not have space or slash (`/`)
6. starting character must not be a number

Sample passwords will be read in from a file named password.txt with the first line containing the number of passwords that will follow.  Each password is on a separate line of the file.

You should display the password followed by YES if the password if valid, or NO if the password is not valid.

Sample Input from `password.txt`
```
5
Pass5
passwordpasswordpasswordpassword
p4223076
Password1
PASSWORD47
```

Sample Output:
```
Pass5 NO
passwordpasswordpasswordpassword NO
p4223076 NO
Password1 YES
PASSWORD47 NO
```
## Problem B: Stack Script

Write a program that will interpret a simple stack oriented script language.  The script language starts with data declarations followed by commands. Data declarations are one to a line in the format:

`variablename number`

where `variablename` is the name of a program variable. Program variables are case insensitive and may contain only letters. The number is an integer value.  There may be up to `16` variables. The end of the variable list is denoted by a line containing only `program`. Following the program line are executable statements. There are *seven* possible statement types:

| Statement | Action |
| :------------- | :------------- |
| push var | Push the value of the specified variable onto the stack. |
| pop var | Remove the top of stack value and store it in the specified variable. |
| add | Add the top two values on the stack. Remove the two values on top of the stack and store the addition result on the top of the stack. |
| sub | Subtract the top of the stack value from the value immediately below the top of the stack.  Remove the two values on top of the stack and store the subtraction result on the stack. |
mult | Multiply the top of the stack value with the value immediately below the top of the stack. Remove the two values on top of the stack and store the product result on the stack. |
| div | Divide the top of the stack value by the value immediately below the top of the stack. Remove the two values on top of the stack and store the division result on the stack. |
| display | Display “Top of stack:” followed by the value of the top of the stack. The value on the top of the stack is not changed or removed. |

There may be up to `256` program statements. The end of the program statements is denoted by a line containing only `end`. All variable names and commands are case insensitive, so `ADD`, `add` and `Add` are all the same.

Your program is to execute a program written in this stack script language.  The script programs are written by Computer Science faculty, so there are no errors in them. There will be no undeclared variables and no stack overflows or underflows. The script program should be read from `script.txt`

Example input from `script.txt`
```
dog 5
cat 3
bird 11
program
push bird
push cat
push dog
display
sub
add
display
end
```

Example output:
```
Top of stack: 5
Top of stack: 9
```
<!-- ```
Top of stack: 5
Top of stack: 13
``` -->
