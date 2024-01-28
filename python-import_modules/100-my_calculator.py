#!/usr/bin/python3

import sys
import calculator_1


if (__name__ == "__main__"):
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = sys.argv[2]
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    result = 0

    if (operator == '+'):
        result = calculator_1.add(num1, num2)
    elif (operator == '-'):
        result = calculator_1.sub(num1, num2)
    elif (operator == '/'):
        result = calculator_1.div(num1, num2)
    elif (opeartor == '*'):
        result = calculator_1.mul(num1, num2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(num1, operator, num2, result))
