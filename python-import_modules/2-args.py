#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    leng = len(sys.argv) - 1

    if (leng == 0):
        print("{} arguments.".format(leng))
    elif(leng == 1):
        print("{} argument:\n{}: {}".format(leng, leng, sys.argv[1]))
    else:
        print("{} arguments:".format(leng))
        j = 1
        for i in sys.argv[1:]:
            print("{}: {}".format(j, i))
            j += 1
