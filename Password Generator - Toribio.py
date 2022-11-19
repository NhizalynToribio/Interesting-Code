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
        password = ExchangeUppercaseLetter(password)

        passwords.append(password)

    return passwords


# This section replace the word with numbers
def ExchangeNumber(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword


# This section replace a element with an Uppercase Letter
def ExchangeUppercaseLetter(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword)//2, len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword


def main():

    Number_Passwords = int(input("\nHow many passwords do you want to generate? "))

    print("Generating " + str(Number_Passwords) + " passwords")

    passwordLengths = []

    print("The Minimum length of password should be 3")