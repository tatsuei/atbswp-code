import re   # Regular expression library
import sys

# Checking user input to see if they wanna restart the program
def checkRes():
    noNames = input('Aww. They don\'t have names yet. Wanna name them?'
                    ' (Y/N)\n')
    return noNames

def floofNaming():
    floofNames = []
    while True:
        print('Hello! Give this smol floof a name?', 'Floof #' + 
              str(len(floofNames) + 1), '(Or press enter to skip.):')

        name = input()
        if name == '':
            break
        elif not re.match("^[a-z]*$", name, flags=re.I): 
            print('Hey! Names begin with letters! L E T T E R S!')
            continue

        floofNames = floofNames + [name]

    # Checks for empty array using Boolean logic, ie fN != fN == null/None
    if not floofNames:
        while True:
            userRes = checkRes()
            if userRes.lower() == 'y':
                floofNaming()
            elif userRes.lower() == 'n':
                print('Okay :( You should give them names next time! :D')
                sys.exit()
            else:
                continue
    else:
        print('So, our floofs are called:')

    for name in floofNames:
        print('   ' + name)

floofNaming()

# elif not re.match("^[a-z]*$", name, flags=re.I): 
# Regex checking for letters, 're.I' where I = ignorecase.
# expression meaning: 'if any (*) character at the start (^)
# or end ($) doesn't match letters between a-z (represented
# by [a-z] with the square brackets meaning the set of
# characters to match
