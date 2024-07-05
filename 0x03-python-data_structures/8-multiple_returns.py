#!/usr/bin/python3

def multiple_returns(sentence):
    if (sentence == ""):
        returnedTuple = len(sentence), None
        return returnedTuple
    returnedTuple = len(sentence), sentence[0]
    return returnedTuple
