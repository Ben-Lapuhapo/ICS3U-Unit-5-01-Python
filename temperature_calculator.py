#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: Nov 2019
# This program uses user defined functions


def calculate_farenheit():
    # calculate area

    # input
    degrees_celsius = int(input("Enter a Temperature in Celsius: "))

    # process
    degrees_farenheit = (9/5) * degrees_celsius + 32

    # output
    print("The Temperature in Farenheit is: {0} ".format(degrees_farenheit))


def main():
    # this function just calls other functions

    # call functions
    calculate_farenheit()


if __name__ == "__main__":
    main()
