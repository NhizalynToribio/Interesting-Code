# PROGRAMMER: NHIZALYN P. TORIBIO
# YEAR & SECTION: BSCOE 2 - 2
# SECOND EXCITING CODES

# This is importing a random file
import random


def Generate_Password(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = []

    for i in pwlength:
        password = ""
        for j in range(i):
            letterindex = random.randrange(len(alphabet))
            password = password + alphabet[letterindex]

        password = ExchangeNumber(password)
        password = replaceWithUppercaseLetter(password)

        passwords.append(password)

    return passwords


def ExchangeNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword