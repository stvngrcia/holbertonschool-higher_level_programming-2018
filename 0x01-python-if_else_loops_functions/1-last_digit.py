#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
flag = 0
grater_five = "and is greater than 5"
zero = "and is 0"
less_six = "and is less than 6 and not 0"

if (number < 0):
    number = number * -1
    flag = 1
print("Last digit of", end=" ")
if (number % 10 > 5):
    print("{} is {} {}".format(number, number % 10, grater_five))
elif (number % 10 == 0):
    print("{} is {} {}".format(number, number % 10, zero))
elif (flag == 1):
    print("{} is {} {}".format(number * -1, (number % 10) * -1, less_six))
else:
    print("{} is {} {}".format(number, number % 10, less_six))
