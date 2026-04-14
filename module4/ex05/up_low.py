#!/usr/bin/env python3

word = input("Enter a word! :")
res = ""
for i in word :
    if i.isupper():
        res += i.lower()
    elif i.islower():
        res += i.upper()
    else :
        res += i
print(res)
