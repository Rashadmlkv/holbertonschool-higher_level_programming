#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
new_dict = simple_delete(a_dictionary, 'a')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
