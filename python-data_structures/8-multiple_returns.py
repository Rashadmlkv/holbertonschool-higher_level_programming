#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_sentence = ()

    if (len(sentence) == 0):
        tuple_sentence = (0, None)
        return tuple_sentence
    else:
        tuple_sentence = (len(sentence), sentence[0])
        return tuple_sentence
