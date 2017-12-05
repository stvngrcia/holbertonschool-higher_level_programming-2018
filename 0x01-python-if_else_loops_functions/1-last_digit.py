#!/usr/bin/python3
import random
flag = 0
number = random.randint(-10000, 10000)
grater_five = "and is greater than 5"
zero = "and is 0"
less_six = "and is less than 6 and not 0"

if (number < 0):
    number = number * -1
    flag = 1
if (number % 10 > 5):
    print("Last digit of {} is {} {}".format(number, number % 10, grater_five))
elif (number % 10 == 0):
    print("Last digit of {} is {} {}".format(number, number % 10, zero))
elif (flag == 1):
    print("Last digit of -{} is -{} {}".format(number, number % 10, less_six))
else:
    print("Last digit of {} is {} {}".format(number, number % 10, less_six))
