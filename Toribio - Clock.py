# PROGRAMMER: NHIZALYN P. TORIBIO
# YEAR & AND SECTION: BSCOE 2 - 2
# LABORATORY EXERCISE NO 4

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()
mainloop()


# Reference in Making a Clock: https://www.youtube.com/watch?v=at7rpdT8FeI

while True:

    import random


def generatePassword(pwlength):
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


def replaceWithNumber(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
        return pword


def main():
    numPasswords = int(input("How many passwords do you want to generate? "))

    print("Generating " + str(numPasswords) + " passwords")

    passwordLengths = []

    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i + 1) + " "))
        if length < 3:
            length = 3
        passwordLengths.append(length)

    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print("Password #" + str(i + 1) + " = " + Password[i])
