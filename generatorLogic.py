from pwCharacters import charList as cl
import random

def logic(characterAmount,newPW=[]):
    # If characterAmount == 0
    if characterAmount < 1:
        # End function
        return newPW
    # Else there are still characters to add
    else:
        # Pick a random number for the index of list
        randChar = random.randint(0, len(cl)-1)
        # Add the character at the random number index
        newPW += cl[randChar]
        # Minus 1 character from the counter
        characterAmount -= 1
        # Run the function again to get another character
        logic(characterAmount, newPW)
        # Return or recursive function will not work
        return newPW

