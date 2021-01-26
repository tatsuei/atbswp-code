# For precision check, look at math.trunc() function for more info.
import math     # For all the joosi mafs equations anddd also it run FAST

total = 0       # Sum total counter
counter = 0     # How many numbers
for num in range(101):
    total = total + num
    root = math.sqrt(num)   # Try using 'gmpy2' library from PyPi
    if int(root + 0.5) ** 2 == num: # Offset of 0.5 for precision check
        print('Subtotal: ' + str(total), 'Current number: ' + str(num),
              'It is a perfect square!')
    else:
        print('Subtotal: ' + str(total), 'Current number: ' + str(num),
              'It\'s not a perfect square!')
    counter += 1
print('Sum total: ' + str(total), 'Total numbers: ' + str(counter),
      'Initial number: 0', 'Final number: ' + str(num))
