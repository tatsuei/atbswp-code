import sys

# sequence() is top level to allow references from bottom-level functions
def sequence():    
    while True:
        userResponse = input('Type in a number, any number!\n')
        if userResponse == '0':
            print('Please give a number higher than 0!')
        elif userResponse != '0':
            try:
                userResponse = int(userResponse)
                collatz(userResponse)
            except ValueError:  # Exceptions such as words, symbols
                print('Please enter numbers only!')           

# Check for response 
def goAgain():
    response = input('Wanna enter another number? Y/N\n')
    return response

# Pasta to perform input check loop; P.S plis fix this in the future Cal.
def goAgainCheck():
    while True:
        print('Please enter "Y" to continue, or "N" to exit!')
        properRepeat = goAgain()
        if properRepeat.lower() == 'y':
            sequence()
        elif properRepeat.lower() == 'n':
            sys.exit()
        else:
            continue
    
def collatz(number):
    if number % 2 == 0:
        res = number // 2
    else:
        res = number * 3 + 1

    # Try cleaning up this section: nested loops can't be a good idea Cal.
    if res == 1:
        print(res)
        repeat = goAgain()
        userInput = repeat.lower()
        if userInput == 'y':
            sequence()
        elif userInput == 'n':
            sys.exit()
        else:
            goAgainCheck()
    # Loop this when the expression doesn't evaluate to 1
    elif res != 1:
        print(res)
        number = res # 'userResponse' is assigned the resulting number
        return collatz(number)  # Starts the Collatz loop again
    
sequence()  # Program starts here
