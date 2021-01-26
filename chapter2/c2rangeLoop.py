##Initialising int and array/list values
c1 = 0
c2 = 0
c3 = 0
a1 = []
a2 = []
a3 = []

for i in range(12, 16):
    if c1 == 2:
        print(str(c1) + 'nd', 'integer,', str(i))
    else:
        print(str(c1) + 'th', 'integer,', str(i))
    c1 += 1
    a1.append(i)    # Adds the current number to the array
print('This is a loop starting with', str(a1[0]),
      'and ending with', str(a1[-1]))
print('Current array:', str(a1), 'Array length:', str(len(a1)))

##range(starting_number, stop_before_number, step_number)
for i in range(0, 10, 2):
    if c2 == 2:
        print(str(c2) + 'nd', 'integer,', str(i))
    else:
        print(str(c2) + 'th', 'integer,', str(i))
    c2 += 1
    a2.append(i)
print('This is a loop starting with', str(a2[0]),
      'and ending with', str(a2[-1]))
print('Current array:', str(a2), 'Array length:', str(len(a2)))

for i in range(5, -1, -1):
    if c3 == 2:
        print(str(c3) + 'nd', 'integer,', str(i))
    else:
        print(str(c3) + 'th', 'integer,', str(i))
    c3 += 1
    a3.append(i)
print('This is a loop starting with', str(a3[0]),
      'and ending with', str(a3[-1]))
print('Current array:', str(a3), 'Array length:', str(len(a3)))
