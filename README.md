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

where `variablename` is the name of a program variable. Program variables are case insensitive and may contain only letters. The `number` is an integer value.  There may be up to `16` variables. The end of the variable list is denoted by a line containing only `program`. Following the program line are executable statements. There are *seven* possible statement types:

| Statement | Action |
| :------------- | :------------- |
| `push var` | Push the value of the specified variable onto the stack. |
| `pop var` | Remove the top of stack value and store it in the specified variable. |
| `add` | Add the top two values on the stack. Remove the two values on top of the stack and store the addition result on the top of the stack. |
| `sub` | Subtract the top of the stack value from the value immediately below the top of the stack.  Remove the two values on top of the stack and store the subtraction result on the stack. |
| `mult` | Multiply the top of the stack value with the value immediately below the top of the stack. Remove the two values on top of the stack and store the product result on the stack. |
| `div` | Divide the top of the stack value by the value immediately below the top of the stack. Remove the two values on top of the stack and store the division result on the stack. |
| `display` | Display “Top of stack:” followed by the value of the top of the stack. The value on the top of the stack is not changed or removed. |

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

## Problem C: Fire Plane Dispatcher

Airplanes to dump water and fire retardant on forest fires, stand ready at several airports. Write a program to be used by the fire service to dispatch the closest airplane to help put out a fire. Airports are located by their latitude and longitude which are each represented by **three** integers, the *degrees, minutes and seconds*.  We will assume that all latitudes are north, and longitudes are west, the portion of the globe that encompasses North America. Airports are identified by `A`, `B`, `C`, `D`, etc. The first airport is identified by `A`, the second airport is `B`, the third airport is `C`, etc. There is a maximum of `10` airports. The fire location is identified by its latitude and longitude coordinates. Your program will calculate the closest airport to dispatch airplanes to fight the fire.

Input from `fire.txt` consists of:
- The number of airports
- Latitude and longitude coordinates of each airport
- Latitude and longitude coordinates of the emergency location

Your program should print the airport that is closest to the fire. The closest airport is defined as the one with the shortest straight line distance. You may ignore the curvature of the earth. The airport must be identified by its letter.

Sample input from `fire.txt`:
```
5
37   57   5    120  1    49
49   25   45   98   35   42
45   38   40   94   10   27
31   59   22   79   39   18
36   6    48   81   7    17
41   34   23   104  14   60
```

Sample Output:
```
The call should be serviced by airport B
```

## Problem D: Square Farmland

You have been hired by a binary farmer to find the largest square plot of land for planting crops on her new farm. The plot to be farmed must be a square where the width and depth are the same. (Her plants have square roots.) She has created a text file that models her property. Every square hectare of land good for planting is denoted by a `1`, and every hectare that is deemed not suitable is represented by a `0`. The input for this program comes from `largestsquare.txt`. The first line of the input file will be the integer `n`, the number of rows and columns of the matrix. The following `n` rows will contain `n` 1’s or 0’s separated by spaces. Your program should find the row and column position of the upper left corner (corner with the smallest index) of the largest square that is suitable for planting and output the number of hectares in that square. The first row and first column are numbered zero. If there is more than one square of the largest size, your program can output any largest square.

Example input from `largestsquare.txt`:
```
13
0 0 0 0 0 0 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 0 0 1 1 1
0 0 0 0 1 1 0 0 1 1 1 1 1
1 1 0 0 1 1 0 1 0 1 0 1 0
1 1 0 0 1 1 1 1 0 0 0 0 0
1 1 0 0 1 1 0 0 1 1 1 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1
0 0 0 1 1 1 1 0 0 0 0 1 0
0 1 1 1 1 1 1 1 1 1 0 1 1
0 0 1 1 1 1 1 1 0 0 1 1 1
0 1 1 0 1 0 1 0 1 1 1 1 0
1 1 1 0 0 1 1 0 1 0 0 1 1
1 0 1 0 1 0 1 0 1 0 1 0 1
```

Example output
```
Biggest plot is at 6, 3 of size 16 hectare
```

## Problem E: Sum to Nothing

Given a set of integers, is there a non-empty subset of the numbers whose sum is zero? For example, given the set `{ −7, −3, −2, 5, 8 }`, the answer is yes because the subset `{ −3, −2, 5 }` sums to zero.

The input to this program comes from the text file `zero.txt`. The first line of the file is the number of sets to be checked. Each set contains an integer number `N` (between `2` and `10`) giving the number of values to follow. The next line for each set has `N` integers. If there is a subset of the `N` integers (size `1` to `N`) that sums to zero, the program should display the integers in the subset, each separated by a space. If more than one subset exists, only one has to be shown. If no subset exists for that set, the program should print `No zero sum`.

Example input from `zero.txt`:
```
3
5
-7 -3 -2 5 8
3
-1 -2 4
6
2 4 6 -1 -3 8
```

Example output:
```
-3, -2, 5
No zero sum
4 -1 -3
```

## Problem F: Asteroid Position

There are lots of objects moving around in space. Write a program that will predict the position of an asteroid at a given time in the future based on its current position and speed.

In 1687, Isaac Newton formulated the principles governing the motion of two particles under the influence of their mutual gravitational attraction. As a close approximation, we will assume everything orbits the sun on a two-dimensional plane. Let `Δx` represent the difference in the position of two object, `A` & `B`, along the X coordinate and let `Δy` represent the difference along the Y coordinate. Calculate `r`, the distance between the two objects in meters, using

Asteroids are primarily influenced by the gravitational attractions of the sun since it is six orders of magnitude more massive than any of the planets. We can represent the mass of the sun, 1.9890 × 10^30 Kg, as MSUN and the mass of an asteroid as MA.

The force in Newtons pulling an asteroid to the sun can be calculated using

where `G` is the gravitational constant, 6.67 × 10−11 in the units N·m2·kg−2.  The force can be divided into X and Y components by:

The force will accelerate the asteroid following Newton's second law of motion, F = ma. Over a small change in time, `Δt`, the velocity of an asteroid is changed by

After calculating the change in velocity of an asteroid, the position of the asteroid can be updated by

By repeating these calculations every `Δt` seconds, the asteroid will move under the gravitational force of the sun. A `Δt` of `21`, `600` seconds (6 hours) should be used for an accurate location.

The program must first read in data about the asteroid. The input file, `asteroid.txt`, contains the position, velocity and mass of the asteroid. A single line contains:
- X position of the asteroid in meters from the sun
- Y position of the asteroid in meters from the sun
- X direction velocity of the asteroid in meters/second
- Y direction velocity of the asteroid in meters/second
Mass of the asteroid in Kg

We will assume the sun is motionless at position `0, 0`.

Display the X and Y coordinates of the asteroid in one week, 604, 800 seconds, from the start.

Sample input from `asteroid.txt`:
```
7.7578E+09  5.7378E+10  -4.7468E+04  6.4179E+03  8.7E+19
```

Sample output:
```
After a week, the asteroid is at -2.10211E10, 6.81892E10
```

**Note that accuracy within four decimal digits is sufficient.**

## Problem G: Correct Change

Each hot dog costs $5 at the Myrtle beach food truck festival. Customers are standing in a queue to buy them from you, and order only one at a time with bills of $5, $10, or $20. Each customer will only buy one hot dog and pay with either a $5, $10, or $20 bill. As a seller, you must provide the correct change to each customer to make sure the net transaction of customer payment is $5. Note that you don't have any change on hand at first. For a given list of bills, write a program to decide if you can give each customer the correct change. If so, display `true`, otherwise display `false`.

Input will be from the file `money.txt` The first number in the file will be an integer specifying the number of test cases. Each test case will start with an integer, `n`, indicating how many hot dog purchases will be made. This will be followed by `n` numbers, either `5`, `10` or `20`, separated by whitespace.

Sample input from `money.txt`:
```
2
5
5  5  5  10  20
5
5 5 10 10 20
```

Sample output:
```
true
false
```

Explanation for `5  5  5  10  20`:
- From the first 3 customers, we collect **three** `$5` bills in order.
- From the fourth customer, we collect a `$10` bill and give back a `$5`.
- From the fifth customer, we give a `$10` bill and a `$5` bill.
- Since all customers got correct change, we output `true`.

Explanation for `5 5 10 10 20`:
- From the first two customers in order, we collect **two** `$5` bills.
- For the next two customers in order, we collect a `$10` bill and give back a `$5` bill.
- For the last customer, we cannot give the change of `$15` back because we only have **two** `$10` bills.
- Since not every customer received the correct change, the answer is `false`.

## Problem H: Donut Trail

Given a `n * m` matrix donut, `donut[i][j]` denotes the number of donuts at coordinates `(i, j)`. The program is to find a path from the specified starting point always moving to an adjacent location with the largest number of donuts.  Movements can only be one index up, down, left or right. No diagonal movements are allowed. You must always move in the direction of the largest number of donuts. You cannot visit a position more than once. The path ends when all adjacent locations have already been visited and no move is possible. All numbers in the matrix are unique positive integers.

The program should display the number of donuts found in the path, including those at the starting point.

Input will be from the file `donut.txt` in the format:

- The first line will have two integers, `n` and `m`, the number of rows and columns in the matrix
- The second line with have two integers indicating the start row and column, counting from zero.
- `n` rows of `m` integers will follow

Sample input from `donut.txt`:
```
5 5
1 1
2 3 18 22 6
4 8 11 7 12
1 9 21 16 17
5 19 33 15 13
44 10 14 18 20
```


Sample output:
```
161 donuts were found
```

Explanation for solution:
<!-- The correct path is:
2 3 18 22  6
4  8 11  7 12
1  9 21 16 17
5 19 33 15 13
44 10 14 18 20 -->
