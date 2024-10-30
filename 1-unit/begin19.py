from math import *

x1 = int(input('x1 = '))
y1 = int(input('y1 = '))

x2 = int(input('x2 = '))
y2 = int(input('y2 = '))


length = abs(x2- x1)
width = abs(y2 - y1)
perimetr = (length + width) * 2
s = length * width

print('perimetr = ', perimetr, 'yuza = ', s)