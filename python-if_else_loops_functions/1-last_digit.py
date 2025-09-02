#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnumber = abs(number)[-1] % 10

print(f"Last digit of {number} is {lastnumber} ", end ="")

if lastnumber > 5:
    print("and is greater than 5")

elif lastnumber == 0:
    print("and is 0")

elif lastnumber < 6 and not 0:
    print("and is less than 6 and not 0")
