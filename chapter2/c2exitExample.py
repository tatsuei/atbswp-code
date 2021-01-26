import sys

while True:
    print('Hey, wanna exit? Type exit.')
    response = input()
    if response == 'exit':
        print('You said it! Exiting...')
        sys.exit()
    print('Alright, we\'re staying cuz you typed', '\'' + str(response)
          + '\'' + '!')
