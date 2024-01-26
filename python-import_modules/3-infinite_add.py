#!/usr/bin/python3

if (__name__ == "__main__"):
    import sys
    numbers = 0

    for i in sys.argv[1:]:
        numbers += int(i)

    print ("{}".format(numbers))
