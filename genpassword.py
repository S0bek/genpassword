#!/usr/bin/python

#Generateur de mot de passe aleatoire en python (equivalent a celui defini en perl)

import os
import sys
from random import randint
from optparse import OptionParser

prog = os.path.basename(sys.argv[0])
chars = [chr(x) for x in range(65 , 123)]
specchar = ['&' , '#' , '+' , '%' , '$']#La liste peut etre adaptee pour prendre plus de caracteres au besoin

#Traitement des arguments
parser = OptionParser()
parser.prog = prog
parser.usage = parser.prog + " -l length"
parser.description = "Generate random passwords with a minimum of security"
parser.add_option("-l", "--length", type=int, dest="strengh", help="length of the password generated")

(options, args) = parser.parse_args()

#On verifie les arguments fournis au programme
if (options.strengh == None):
    parser.print_help(file=None)
    exit(1)
else:
    strengh = options.strengh

class Password(object):

    def __init__(self , strengh):
        self.strengh = strengh

    def __repr__(self):
        return "Given length: %s , Generated password: %s" % (self.strengh , self.password)

    def genpass(self):
        self.password = ""

        for i in range(0 , self.strengh):
            rndchar = str(chars[randint(0 , len(chars) - 1)])#We take select a random char from the list chars
            self.password += rndchar

        return self.password

    def enforce(self):
        found = 0
        newpass = ""

        for char in specchar:
            if char in self.password:
                print("trouve: " + str(char))
                found += 1

        if found < 1:
            rndpos = randint(0 , len(self.password) - 1)
            rndchar = specchar[int(randint(0 , len(specchar) - 1))]

            #Ajout du caractere special si le mot de passe est percu comme n'etant pas assez fort
            for i in range(0 , len(self.password)):
                if i == rndpos:
                    newpass += rndchar
                else:
                    newpass += self.password[i]
        else:
            newpass = self.password

        #return newpass
        self.password = str(newpass)
        return self.password

genpassword = Password(strengh)
genpassword.genpass()
genpassword.enforce()

print("Mot de passe genere: " + genpassword.password)

#Decommenter la ligne qui suit si on a besoin un jour de se souvenir quels ont ete les attributs qui ont ete stockes et comment fonctionne la classe (si on a besoin d'appeler la classe dans un autre programme un jour...)
#print genpassword
