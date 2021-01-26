##This program is the first of many
print('Hello there!')
print('And what\'s your name?')
myName = input()
print('Nice to meetcha, ' + myName + '!')
print('The length of your name is: ')
print(len(myName))
print('Hmm. How old are you?')
myAge = input()
print('Great! We\'re the same age! Turning ' + str(int(myAge) + 1) +
      ' in a year\'s time, eh?')

Practice Questions - Chapter 1 
1. Which of the following are operators, and which are values?
A:
    Operators:
        *
        -
        /
        +
    Values:
        'hello'
        -88.8
        5

2. Which of the following is a variable, and which is a string?
A:
    spam - var
    'spam' - str

3. Name three data types.
A:
    integers
    strings
    floats

4. What is an expression made up of? What do all expressions do?
A:
    An expression can contain a combination of: values, variables, operators,
    or even calls to functions! All expressions (and their inputs, stdin)are
    evaluated by the interpreter and an output is produced (stdout).

5. This chapter introduced assignment statements, like spam = 10.
What is the difference between an expression and a statement?
A:
    An expression would be a combination of operations including math operators,
    while a statement only declares or assigns a value to something.

6. What does the variable bacon contain after the following code runs?
bacon = 20
bacon + 1
A:
    bacon = 21

7. What should the following two expressions evaluate to?
'spam' + 'spamspam'
'spam' * 3
A:
    'spamspamspam' for both expressions.


8. Why is eggs a valid variable name while 100 is invalid?
A:
    By convention all varnames should start with either an underscore or a
    letter. Numbers are strictly reserved for well, numbers!

9. What three functions can be used to get the integer, floating-point num,
or string version of a value?
A:
    int()
    float()
    str()

10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
A:
    Well, the above expression is trying to concatenate strings with an
    integer. An easy solution would be to call the str() function on '99'
    to convert it to a string.






































