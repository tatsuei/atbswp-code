def spam():
    eggs = 'local spam'
    print(eggs)

def bacon():
    eggs = 'local bacon'
    print('Initial execution...', eggs)
    spam()
    print('Execution in progress...', eggs)

eggs = 'global'
bacon()     # This is the first line of execution
print(eggs + '.', 'Execution complete.') # Outputs 'global' for the global var

# c3sameName2.py
def spam2():
    global eggs     # Global var overrides local vars
    eggs = 'spam'

eggs = 'global'
spam2()     # This fx assigns 'spam' to 'eggs'
print(eggs) # Outputs the current 'eggs' data

# c3sameName3.py
def spam3():
    global eggs
    eggs = 'spam'   # Global var

def bacon3():
    eggs = 'bacon'  # Local var

def ham():
    print(eggs)     # Global var 'eggs'

eggs = 42
spam3()         # Overrides the 'eggs' var with 'spam'
print(eggs)
