#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None:
        if len(a_dictionary) == 0:
            return None
        max = ""
        max = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[max]:
                max = key
        return max
    else:
        return None
