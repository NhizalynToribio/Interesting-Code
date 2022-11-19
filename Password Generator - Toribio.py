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


# This section will ask the user to input how many password he/she wants
def main():

    Number_Passwords = int(input("\nHow many passwords do you want to generate? "))

    print("Generating " + str(Number_Passwords) + " passwords")

    passwordLengths = []

    print("\nThe Minimum length of password should be 3")

    # This section will show the output of the program or the Generated Password
    for i in range(Number_Passwords):
        length = int(input("\nEnter the length of the Password #" + str(i + 1) + " "))
        if length < 3:
            length = 3
        passwordLengths.append(length)

    Password = Generate_Password(passwordLengths)

    for i in range(Number_Passwords):
        print("\nThis is the Generated Password #" + str(i + 1) + " = " + Password[i])


main()
