#!/usr/bin/python

import GeneratePassword

length = str(raw_input("Longueur du mot de passe: "))

try:
    if not length == '': length = int(length)
except:
    raise

password = GeneratePassword.GeneratePassword(length)
print(password)
