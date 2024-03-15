#!/usr/bin/python3
def uppercase(str):
    newString = ""
    for i in str:
        if i >= 'a' and i <= 'z':
            newChar = chr(ord(i) - 32)
            newString += newChar
        else:
            newString += i
    print("{}".format(newString))
