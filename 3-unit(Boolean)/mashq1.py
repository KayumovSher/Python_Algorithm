from math import * 

x = int(input('x= '))
y = int(input('y= '))
z = int(input('z= '))

# son = pow((pow(x, 2) - pow(y, 2) + pow(z, 2)), 1/4)

son = pow((sqrt(x) - sqrt(y) + sqrt(z)), 1/4)

print(son)