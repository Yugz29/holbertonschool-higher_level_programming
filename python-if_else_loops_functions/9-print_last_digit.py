#!/usr/bin/python3
def print_last_digit(number):
    lastnumber = abs(number) % 10
    print("{}".format(lastnumber), end="")
    return lastnumber
