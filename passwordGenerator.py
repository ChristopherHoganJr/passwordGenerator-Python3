from getPasswordLen import pwLength
from generatorLogic import logic
from retry import tryAgain

gameActive = True
# Greetings / Introduction
print()
print('-------------------------------------')
print('Welcome to my password generator tool')
print('-------------------------------------')
print()

def createPW():
    # Ask the user how many characters they'd like their password to be
    print('-------------------------------------------')
    passwordLength = pwLength()
    # Randomly pick a character and store each character in a list
    newPW = logic(passwordLength)
    # Join the list together in a string
    encryptedPW = ''.join(newPW)
    # Give the user their new password
    print('---------------------')
    print(f'Your new password is: {encryptedPW}')
    print('')

while gameActive != False:
    createPW()
    gameActive = tryAgain()





