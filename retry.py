def tryAgain():
    tryAgainAnswer = int(input('Try Again? \n1. for \'Yes\'  \n2. for \'No\'\n'))
    if tryAgainAnswer == 1:
        return True
    elif tryAgainAnswer == 2:
        print('Always be safe and use a strong password.')
        return False
    else:
        tryAgain()
