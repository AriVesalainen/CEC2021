#!/usr/bin/python3
#
import random
import string

def getRndStr(length):
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(length))
    return result

print(getRndStr(5))
print(getRndStr(5))
