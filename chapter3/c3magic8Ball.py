import random

##Defining the function
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Man just get it already!'
    elif answerNumber == 2:
        return 'Nuh uh, it\'s decided.'
    elif answerNumber == 3:
        return 'Ye'
    elif answerNumber == 4:
        return 'That was wild, try again.'
    elif answerNumber == 5:
        return 'Nah man I\'m not in the mood.'
    elif answerNumber == 6:
        return 'Gimme yo full focus B O I!'
    elif answerNumber == 7:
        return 'That\'s a NO, N O, NO.'
    elif answerNumber == 8:
        return 'Fam, you don\'t look too gud.'
    elif answerNumber == 9:
        return 'For real? Damn.'

print(getAnswer(random.randint(1,9)))
# Generating a pseudorandom number between 1-9
# and printing out the result

# For every print() statement or function without
# 'return', a 'return None' is appended to it;
# this results in some quirky tings.
# Try this in the console:
# kek = print('Ey yo my g')
# kek == None
