floofNames = []
while True:
    print('Hey! Give this smol floof a name?', str(len(floofNames) + 1),
          ' (Or you could just press enter to skip this.):')
    name = input()
    if name == '':
        break
    floofNames = catNames + [name]
print('So, our floofs are called:')
for name in floofNames:
    print('   ' + name)
