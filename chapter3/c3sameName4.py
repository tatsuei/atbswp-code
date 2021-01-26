def spam():
    print(eggs)
    eggs = 'local cb'

eggs = 'global knn'
spam()  # Error will be displayed cuz 'eggs' isn't defined yet.
