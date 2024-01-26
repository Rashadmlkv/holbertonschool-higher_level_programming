#!/usr/bin/python3

if (__name__ == "__main__"):
    import sys
    leng = len(sys.argv) - 1

    if (leng == 0):
        print(f"{leng} arguments.")
    elif(leng == 1):
        print(f"{leng} argument:\n{leng}: {sys.argv[1]}")
    else:
        print(f"{leng} arguments:")

        j = 1
        for i in sys.argv[1:]:
            print(f"{j}: {i}")
            j+=1
