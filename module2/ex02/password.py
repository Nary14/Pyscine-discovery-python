#!/usr/bin/env python3
password = "Python is awesome"

password_user = input("Enter the password : ")
if password_user == password :
    print(f"{password_user}\nACCESS GRANTED")
else :
    print(f"{password_user}\nACCESS DENIED")
