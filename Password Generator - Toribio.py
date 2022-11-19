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
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]

        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)

        passwords.append(password)

    return passwords
