#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is not None:
        if not isinstance(roman_string, str):
            return 0
        roman = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 10000}
        sum = 0
        char = 0
        while char < len(roman_string):
            if (char != len(roman_string) - 1 and
                    roman_string[char] == "I" and
                    roman_string[char + 1] == "V"):
                sum += 4
                char += 2
            elif (char != len(roman_string) - 1 and
                    roman_string[char] == "I" and
                    roman_string[char + 1] == "X"):
                sum += 9
                char += 2
            elif (char != len(roman_string) - 1 and
                    roman_string[char] == "X" and
                    roman_string[char + 1] == "C"):
                sum += 90
                char += 2
            else:
                sum += roman[roman_string[char]]
                char += 1

        return sum
    return 0
