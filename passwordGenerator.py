from generatorLogic import logic
from retry import tryAgain


# Set appActive to True
appActive = True

# Greetings / Introduction
print()
print('-------------------------------------')
print('Welcome to my password generator tool')
print('-------------------------------------')
print()

def createPW():
    lowerCharacters = int(input("How many lowercase characters would you like?: "))
    upperCharacters = int(input("How many uppercase characters would you like?: "))
    symbolCharacters = int(input("How many symbol characters would you like?: "))
    numberCharacters = int(input("How many number characters would you like?: "))
    # Randomly pick a character and store each character in a list
    newPW = logic(lowerCharacters, upperCharacters, symbolCharacters, numberCharacters)
    # Join the list together in a string
    encryptedPW = ''.join(newPW)
    # Give the user their new password
    print('\n---------------------')
    print(f'Your new password is: {encryptedPW}')
    print('---------------------\n')

while appActive:
    createPW()
    appActive = tryAgain()





