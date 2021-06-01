#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program rounds decimals


def rounding(rounding_num, decimal):

    # process
    integer = decimal * 10 ** rounding_num
    decimal_rounded = int(integer)
    decimal_final = decimal_rounded / 10 ** rounding_num

    # output
    print("\nYour number is rounded to {0}".format(decimal_final))


def main():
    # this function calls other functions as well as
    #   takes input

    # input
    decimal = float(input("Input a decimal to round: "))
    print("Input how many decimal places ", end="")
    rounding_num = int(input("you'd like to round to: "))

    # call fucntions
    rounding(rounding_num, decimal)


if __name__ == "__main__":
    main()
