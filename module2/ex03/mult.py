#!/usr/bin/env python3

def multi(a,b):
    return(a * b)

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

c = multi(a,b)

if c > 0 :
    print (f"{a} x {b} = {c}\nThe result is positive.")
elif c == 0 :
    print (f"{a} x {b} = {c}\nThe result is positive and negative.")
else :
    print (f"{a} x {b} = {c}\nThe result is negative.")

