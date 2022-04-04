# Triad-Programming-Contest-2022
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
