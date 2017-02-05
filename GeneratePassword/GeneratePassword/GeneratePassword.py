#!/usr/bin/python

from random import choice
import string

def GeneratePassword(length):
    defaultsize = 100
    password = []
    specchars = ['$' , '*' , '#' , '+' , '!']

    if not type(length) == int or length == '': length = defaultsize

    for i in range(0 , length):
        rndlet = choice(string.letters + string.digits + choice(specchars))
        password.append(rndlet)

    return string.join(password , "")

