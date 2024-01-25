#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(str(number)[-1])
lastdigitof = "Last digit of {} is {}"

print(lastdigitof.format(number, lastdigit), end = ' ');
if (lastdigit > 5):
    print("and is greater than 5")
elif (lastdigit < 6 and lastdigit != 0):
    print("and is less than 6 and not 0")
else:
    print("and is 0")

