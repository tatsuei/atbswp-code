print('Hello! My name is Cal!') 
counter = 0;        # initial counter
for i in range(5):  # for 5 items/iterations, do:
    if i == 0:      # Condition for initial iteration
        print('Cal ' + str(i) + 'th time')
    else:
        print('Cal ' + str(i) + ' times')
    counter += 1    # Increment counter after each iteration
print('\'Cal\' has been printed ' + str(counter) + ' times!')
    
