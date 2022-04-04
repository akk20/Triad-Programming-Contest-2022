#!/usr/bin/env python3

__author__ = ["Aidan Kelley"]
__copyright__ = "Copyright 2022"
__credits__ = ["Ryan Hirscher", "Ally Taylor"]
__license__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = ""
__email__ = ["akelley1@highpoint.edu", "rhirsche@highpoint.edu", "ataylor5@highpoint.edu"]
__status__ = ""

# To run:
# python3 problem_a.py

# Passwords must have,
# 1)      8 to 32 characters
# 2)      at least one numeric digit
# 3)      at least one uppercase letter
# 4)      at least one lowercase letter
# 5)      must not have space or slash (/)
# 6)      starting character must not be a number

def main():

    data = open("password.txt", "r")

    passwordList = data.read().splitlines()
    #print(passwordList)

    num_of_passwords = passwordList[0]
    passwordList.pop(0)

    # validArray = [False]*num_of_passwords

    #print(passwordList)


    symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for password in passwordList:
        # print(password)
        valid = False

        length = True
        first = True
        white = True

        # 1) 8 to 32 characters
        if len(password) <8 or len(password) >32:
            length = False

        # 6) starting character must not be a number
        if password[0] in nums:
            first = False

        # 5) must not have space or slash (/)
        for char in password:
            if ord(char) in [32, 47]:
                white = False


        # 2)      at least one numeric digit
        # 3)      at least one uppercase letter
        # 4)      at least one lowercase letter
        uppercase = False
        numeric = False
        lowercase = False
        for char in password:
            if ord(char) in range(97, 122): # lower case
                lowercase = True
            if ord(char) in range(65, 90): # upper case
                uppercase = True
            if ord(char) in range(48, 57):
                numeric = True


        if(lowercase and uppercase and numeric and white and length and first):
            valid = True

        # print(password, lowercase, uppercase, numeric, white, length, first)
        if(valid):
            print(password, "YES")
        else:
            print(password, "NO")



if __name__ == '__main__':
   main()
