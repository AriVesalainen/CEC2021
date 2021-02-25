#!/usr/bin/python3
import math

def calcFactorial(n):
   try:
        f = math.factorial(n)
        r = float(f)
        return "Factorial of {} = {}".format(n,r)
   except Exception as e:
        return "Factorial of {} = infinite".format(n)


print(calcFactorial(10))
print(calcFactorial(100))
print(calcFactorial(1000))
print(calcFactorial(10000))
print(calcFactorial(100000))

