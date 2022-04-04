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
# python3 problem_e.py

import itertools

def main():

    data = open("zero.txt", "r")

    rawData = data.read().splitlines()
    # rawData = data.read().readlines()
    # print(rawData)


    totalSets = int(rawData[0])
    rawData.pop(0)

    # print(findsubsets(s, 0));

    for i in range(totalSets):
        setLength = int(rawData[0])
        rawData.pop(0)
        set = rawData[0].split(" ")
        set = [int(i) for i in set]
        rawData.pop(0)

        hasZeroSum = False
        zeroSet = []
        for i in range(len(set)):
            subset = findsubsets(set, i+1)
            # print(subset)
            for j in range(len(subset)):
                if sum(subset[j]) == 0:
                    hasZeroSum = True
                    zeroSet = subset[j]

        if (hasZeroSum):
            output = ""
            for num in zeroSet:
                output += str(num) + " "
            print(output)
        else:
            print("No zero sum")

def findsubsets(set, setLength):
    return list(itertools.combinations(set, setLength))


if __name__ == '__main__':
   main()
