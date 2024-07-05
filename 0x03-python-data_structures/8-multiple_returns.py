#!/usr/bin/python3

def multiple_returns(sentence):
    if(sentence == ""):
        return None
    returnedTuple = len(sentence), sentence[0]
    return returnedTuple
