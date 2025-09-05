#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    numbers = [int(x) for x in args]
    total = sum(numbers)
    print(total)
