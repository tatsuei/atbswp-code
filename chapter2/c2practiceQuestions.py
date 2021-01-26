##Chapter 2 Practice Questions 
import sys

##  Q1. What are the two values of the Boolean data type?
##      How do you write them?
##q1_ans = ['true', 'false']
##print('Q1. What are the two values of the Boolean data type?',
##      '\nHow do you write them?')
##while True:
##    q1_r1 = str(input('Bool 1: ')).lower()
##    q1_r2 = str(input('Bool 2: ')).lower()
##    if q1_r1 in q1_ans and q1_r2 in q1_ans:
##        print('That\'s correct! Your answers were:', '\'' + q1_r1 + '\'',
##              'and', '\'' + q1_r2 + '\'' + '!')
##        break
##    else:
##        print('Hmmm. Your answers were:', '\'' + q1_r1 + '\'',
##              'and', '\'' + q1_r2 + '\'', ', let\'s try again!')
##
####  Q2. What are the three Boolean operators?
##q2_ans = ['and', 'or', 'not']
##print('Q2. What are the three Boolean operators?')
##while True:
##    q2_r1 = str(input('Operator 1: ')).lower()
##    q2_r2 = str(input('Operator 2: ')).lower()
##    q2_r3 = str(input('Operator 3: ')).lower()
##    if q2_r1 in q2_ans and q2_r2 in q2_ans and q2_r3 in q2_ans:
##        print('That\'s correct! Nicely done :)',
##              '\nYour answers were:', '\'' + q2_r1 + '\'',
##              'and', '\'' + q2_r2 + '\'', 'and',
##              '\'' + q2_r3 + '\'' + '!')
##        break
##    else:
##        print('Hmmm. That doesn\'t seem right.',
##              '\nYour answers were:', '\'' + q2_r1 + '\'',
##              '\'' + q2_r2 + '\'', 'and', '\'' + q2_r3 + '\'',
##              'let\'s try again!')

##  Q3. Write out the truth tables of each Boolean operator (that is,
##      every possible combination of Boolean values for the operator
##      and what they evaluate to).
##  A:
##        AND operator:
##            False + False = False
##            False + True = False
##            True + False = False
##            True + True = True
##        OR operator:
##            False + False = False
##            False + True = True
##            True + False = True
##            True + True = True
##        NOT operator:
##            False = True
##            True = False
        
##Working on the below code to check for user input
        
##q3_and1 = ['false', 'false', 'false']
##q3_and2 = ['false', 'true', 'false']
##q3_and3 = ['true', 'false', 'false']
##q3_and4 = ['true', 'true', 'true']
##q3_or1 = ['false', 'false', 'false']
##q3_or2 = ['false', 'true', 'false']
##q3_or3 = ['true', 'false', 'true']
##q3_or4 = ['true', 'true', 'true']
##q3_not1 = ['false', 'true']
##q3_not2 = ['true', 'false']
##
##while True:
##    q3_and1_r1 = str(input('Combo In 1: ')).lower()
##    q3_and1_r2 = str(input('Combo In 2: ')).lower()
##    q3_and1_r3 = str(input('Combo Out: ')).lower()
##    print('In 1:', q3_and1_r1, 'In 2:', q3_and1_r2, 'Out:', q3_and1_r3)
##    if (q3_and1_r1 in q3_and1 and q3_and1_r2 in q3_and1 and q3_and1_r3 in
##    q3_and1):
##        print('That\'s correct!')
##    q3_and2_r1 = str(input('Combo In 1: ')).lower()
##    q3_and2_r2 = str(input('Combo In 2: ')).lower()
##    q3_and2_r3 = str(input('Combo Out: ')).lower()
##    print('In 1:', q3_and2_r1, 'In 2:', q3_and2_r2, 'Out:', q3_and2_r3)
##    if (q3_and2_r1 in q3_and2 and q3_and2_r2 in q3_and2 and q3_and2_r3 in
##    q3_and2):
##        print('That\'s correct!')
##    break
##    q3_and3_r1 = str(input('Combo In 1: ')).lower()
##    q3_and3_r2 = str(input('Combo In 2: ')).lower()
##    q3_and3_r3 = str(input('Combo Out: ')).lower()
##    q3_and4_r1 = str(input('Combo In 1: ')).lower()
##    q3_and4_r2 = str(input('Combo In 2: ')).lower()
##    q3_and4_r3 = str(input('Combo Out: ')).lower()
##    if (q3_and1_r1 in q3_and1 and q3_and1_r2 in q3_and1 and q3_and1_r3 in
##    q3_and1) and (q3_and2_r1 in q3_and2 and q3_and2_r2 in q3_and2 and
##    q3_and2_r3 in q3_and2) and (q3_and3_r1 in q3_and3 and q3_and3_r2 in
##    q3_and3 and q3_and3_r3 in q3_and3) and (q3_and4_r1 in q3_and4 and
##    q3_and4_r2 in q3_and4 and q3_and4_r3 in q3_and4):
##        print('That\'s correct!')
##        break
##    else:
##        print('Hmm. That isn\'t quite right.')
##
##while True:
##    q3_or_r1 = str(input('Input 1: ')).lower()
##    q3_or_r2 = str(input('Input 2: ')).lower()
##    q3_or_r3 = str(input('Output: ')).lower()
##    if q3_or_r1 in q3_and and q3_or_r2 in q3_and and q3_or_r3 in q3_and:
##        print('That\'s correct!')
##        break
##    else:
##        print('Hmm. That isn\'t quite right.')
##
##while True:
##    q3_not_r1 = str(input('Input 1: ')).lower()
##    q3_not_r2 = str(input('Output: ')).lower()
##    if q3_not_r1 in q3_and and q3_not_r2 in q3_and and q3_not_r3 in q3_and:
##        print('That\'s correct!')
##        break
##    else:
##        print('Hmm. That isn\'t quite right.')

##  Q4. What do the following expressions evaluate to?
##A:
##    False
##    False
##    True
##    False
##    False
##    True
##print('Q4. What do the following expressions evaluate to?\n')
##
##print('Q4A. (5 > 4) and (3 == 5)')
##while True:
##    response1 = str(input('Your answer? '))
##    if response1.lower() == 'false':
##        print('That\'s correct!', '\nSince it is', '\'(True)', 'and',
##              '(False)\',', 'it will evaluate to False!\n')
##        break
##    else:
##        print('Hmm. Try again maybe?')
##        
##print('Q4B. not (5 > 4)')
##while True:
##    response1 = str(input('Your answer? '))
##    if response1.lower() == 'false':
##        print('That\'s correct!', '\nSince it is', '\'not (True)\'',
##              'it will result in False! Let\'s keep going!''\n')
##        break
##    else:
##        print('Hmm. Wanna try again?')
##        
##print('Q4C. (5 > 4) or (3 == 5)')
##while True:
##    response1 = str(input('Your answer? '))
##    if response1.lower() == 'true':
##        print('That\'s correct!', '\nSince it is', '\'(True)', 'or',
##              '(False)\',', 'it will evaluate to True!\n')
##        break
##    else:
##        print('Hmm. Try again maybe?')
##
##print('Q4D. not ((5 > 4) or (3 == 5))')
##while True:
##    response1 = str(input('Your answer? '))
##    if response1.lower() == 'false':
##        print('That\'s correct!', '\nSince it is', '\'not((True)', 'or',
##              '(False))\',', 'resulting in \'not (True)\',',
##              'which would evaluate to False!\n')
##        break
##    else:
##        print('Hmm. Try again maybe?')
##
##print('Q4E. (True and True) and (True == False)')
##while True:
##    response1 = str(input('Your answer? '))
##    if response1.lower() == 'false':
##        print('That\'s correct!', '\nSince it is', '\'(True)', 'and',
##              '(False)\',', 'it will evaluate to False!\n')
##        break
##    else:
##        print('Hmm. Try again maybe?')
##
##print('Q4F. (not False) or (not True)')
##while True:
##    response1 = str(input('Your answer? '))
##    if response1.lower() == 'true':
##        print('That\'s correct!', '\nSince it is', '\'(True)', 'or',
##              '(False)\',', 'it will evaluate to True!')
##        break
##    else:
##        print('Hmm. Try again maybe?')

##Q5. What are the six comparison operators? 
##A:
##    ==
##    !=
##    >
##    <
##    >=
##    =<
##operators = ['==', '!=', '>', '<', '>=', '=<']
##print('Q5. What are the six comparison operators?')
##while True:
##    response = str(input('Enter all of em, each separated by a space!\n'))
##    print(response)
##    if response in operators:
##        print('That\'s absolutely correct! You got em all!')
##    else:
##        print('Hmm. There might have been some typos!')

##Q6. What is the difference between the equal to operator and the
##    assignment operator?
##A:
##    The equal to '==' operator compares two given values, while variables
##    can be assigned values using the assignment '=' operator.

##Q7. Explain what a condition is and where you would use one.
##A:
##    A condition is a clause placed in an expression to evaluate its truth
##    and usually would be used in loops and 'if statements'.

##Q8. Identify the three blocks in this code:
##    spam = 0
##    if spam == 10:
##        print('eggs')
##        if spam > 5:
##            print('bacon')
##        else:
##            print('ham')
##        print('spam')
##    print('spam')
##A:
##    Codeblock 1:
##        print('eggs')
##    Codeblock 2:
##        print('bacon')
##    Codeblock 3:
##        print('ham')
##
##    * Codeblocks start where the indentation starts, and contain every
##    line after that.

##Q9. Write code that prints Hello if 1 is stored in spam, prints Howdy if
##    2 is stored in spam, and prints Greetings! if anything else is
##    stored in spam.
##A:
##    spam = str(input('What\'s spam gonna hold/store?\n'))
##    if spam == '1':
##        print('Hello')
##    elif spam == '2':
##        print('Howdy')
##    else:
##        print('Greetings!')
    
##Q10. What can you press if your program is stuck in an infinite loop?
##A:
##    Ctrl+D

##Q11. What is the difference between break and continue?
##A:
##    A break statement would force the program to finish without a system
##    call to exit.
##    A continue statement would force the program to jump back to the
##    beginning of the loop to reevaluate input.

##Q12.What is the difference between range(10), range(0, 10),
##    and range(0, 10, 1) in a for loop?
##A:
##    range(10) iterates between 0 and 9, stopping before 10.
##    range(0, 10) does what range(10) does.
##    range(0, 10, 1) does what range(10) does, in increments(steps) of 1.

##Q13. Write a short program that prints the numbers 1 to 10 using a for
##     loop. Then write an equivalent program that prints the numbers
##     1 to 10 using a while loop.
##A:
##    for i in range(1, 11):
##        print(i)
##    while i < 11:
##        print(i)
##        i += 1
        
##Q14. If you had a function named bacon() inside a module named spam,
##how would you call it after importing spam?
##
##Extra credit: Look up the round() and abs() functions on the Internet,
##and find out what they do. Experiment with them in the interactive shell.

##print('Q14. If you had a function named bacon() inside a module named',
##      'spam, how would you call it after importing spam?')
##while True:
##    response = str(input('What would you type?\n'))
##    if response == 'spam.bacon()':
##        print('Yup! You got it right!')
##        break
##    else:
##        print('Hmmm, that doesn\'t seem quite right ._.')
##A:
##    Calling the function:
##        spam.bacon()
##    round() rounds a given number up or down, depending on the last
##    decimal place value. Round up if n >= 6, and round down otherwise.
##    abs() returns the absolute value of the given number/float.
    























