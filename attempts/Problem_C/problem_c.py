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
# python3 problem_c.py
from math import sqrt

def main():

    data = open("fire.txt", "r")

    rawData = data.read().splitlines()
    totalAirports = int(rawData[0])
    rawData.pop(0)

    airportLocation = {}
    for i in range(totalAirports):
        airportLocation[chr(i+65)] = rawData[i].split()
    fireLocation = rawData[totalAirports].split()


    # print(airportLocation)
    # print(DMS(airportLocation.get('A')))

    distance(DMS(airportLocation.get('A')), DMS(airportLocation.get('B')))

    smallest = distance( DMS(airportLocation.get(chr(i+65))) , DMS(fireLocation) )
    smallest = 10000
    airport = "A"
    for key in airportLocation:
        temp = (distance( DMS(airportLocation.get(key)) , DMS(fireLocation) ))
        if temp < smallest:
            smallest = temp
            airport = str(key)
        # print(key, temp)

    # print(smallest, airport)
    print("The call should be serviced by airport", airport)

def distance(point1, point2):
    return sqrt( pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1], 2) )


def DMS(set):

    dd1 = float(int(set[0])) + float(int(set[1]))/60 + float(int(set[2]))/(60*60);
    dd2 = float(int(set[3])) + float(int(set[4]))/60 + float(int(set[5]))/(60*60);

    output = [dd1, dd2]
    return output

if __name__ == '__main__':
   main()
