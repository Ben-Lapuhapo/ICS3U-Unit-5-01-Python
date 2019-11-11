#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: Nov 2019
# This program uses user defined functions


def calculate_farenheit():
    # calculate area

    # input
    degrees_celsius = input("Enter a Temperature in Celsius: ")
    print()

    # process and output
    try:
        degrees_celsius_int = int(degrees_celsius)
        degrees_farenheit = (9/5) * degrees_celsius_int + 32
        print("The Temperature in Farenheit is: {0} ".format(degrees_farenheit))
    
    except ValueError:
        print("Not a Number")

    finally:
        print()
        print("Thanks For Using The Program")


def main():
    # this function just calls other functions

    # call functions
    calculate_farenheit()


if __name__ == "__main__":
    main()
