#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is not None:
        if not roman_string.isalpha():
            return 0
        roman = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 10000}
        sum = 0

        for char in roman_string:
            sum += roman[char]
        return sum
    return 0
