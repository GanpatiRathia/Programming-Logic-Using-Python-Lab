import re

password = input("Enter a password: ")

if (7 <= len(password) <= 20 and 
    re.search(r"[A-Z]", password) and 
    re.search(r"[a-z]", password) and 
    re.search(r"\d", password) and 
    re.search(r"[$#@!]", password)):
    print("Password is valid.")
else:
    print("Password is invalid.")
