

def tryAgain():
    tryAgainAnswer = int(input('Try Again? 1 for \'Yes\' | 2 for \'No\''))
    if tryAgainAnswer == 1:
        return True
    elif tryAgainAnswer == 2:
        print('Always be safe and use a strong password.')
        return False
    else:
        tryAgain()
        return