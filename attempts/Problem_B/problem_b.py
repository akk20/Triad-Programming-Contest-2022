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
# python3 problem_b.py

def main():

    data = open("script.txt", "r")

    rawData = data.read().splitlines()
    # print(rawData)
    variables = {}

    i = 0;
    current = rawData[i]
    while (current != "program"):
        [key, value] = current.split()
        variables[key] = value
        i += 1
        current = rawData[i]

    # print(variables)

    commands = []
    for command in range(i+1, len(rawData)):
        print(rawData[command])

# 
#     stack = []
#     push(variables['dog'])
#     print(stack)
#
#
# def push(var):
#     stack.push(variables[var])

    # totalAirports = int(rawData[0])
    # rawData.pop(0)
    #
    # airportLocation = {}
    # for i in range(totalAirports):
    #     airportLocation[chr(i+65)] = rawData[i].split()
    # fireLocation = rawData[totalAirports].split()



if __name__ == '__main__':
   main()
