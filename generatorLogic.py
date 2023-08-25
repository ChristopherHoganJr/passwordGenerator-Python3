from pwCharacters import charList as cl
from pwCharacters import lowerCaseCharacters as lcc
from pwCharacters import upperCaseCharacters as ucc
from pwCharacters import symbolCharacters as sc
from pwCharacters import numberCharacters as nc
import random

def logic(lowerCharacters, upperCharacters, symbolCharacters, numberCharacters):
    pwChars = []
    for _ in range(lowerCharacters):
        randChar = random.randint(0, len(lcc)-1)
        pwChars += lcc[randChar]
    for _ in range(upperCharacters):
        randChar = random.randint(0, len(ucc)-1)
        pwChars += ucc[randChar]
    for _ in range(symbolCharacters):
        randChar = random.randint(0, len(sc)-1)
        pwChars += sc[randChar]
    for _ in range(numberCharacters):
        randChar = random.randint(0, len(nc)-1)
        pwChars += nc[randChar]

    random.shuffle(pwChars)

    return pwChars


