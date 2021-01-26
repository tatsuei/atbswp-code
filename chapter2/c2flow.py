print('Hello! What\'s your name?')
playerName = input();
print('I see! Welcome, ' + playerName + '!')
print('Would you please key in your passphrase?')
playerPassword = input();
if playerPassword == 'swordfish':
    print('Welcome, ' + playerName + '!')
else:
    print('That wasn\'t the right passphrase. Please try again!')
    
