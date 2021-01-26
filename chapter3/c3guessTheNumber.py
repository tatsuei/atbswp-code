import random

secretNumber = random.randint(1, 20) # Generate pseudorandom number
print('I am thinking... of a number between 1 and 100.')

for guessesTaken in range(0, 6):
    print('Try guessing what\'s on my mind!')
    guess = int(input())

    if guess < secretNumber:
        print('That was too low, try again!')
    elif guess > secretNumber:
        print('Nah, that was way too high, wanna guess lower?')
    else:
        break

if guess == secretNumber:
    print('Nice! You guessed my number in', str(guessesTaken), 'guesses!')
else:
    print('Awww. The number was', str(secretNumber) + '!')
    
