def spam(divideBy):
    return 42 / divideBy
try:    
    print(spam(2))
    print(spam(1234))
    print(spam(99))
    print(spam(0))
    print(spam(3))
except ZeroDivisionError:
    print('Nah man, don\'t put in a 0.')
