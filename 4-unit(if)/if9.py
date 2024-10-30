a = float(input('a = '))
b = float(input('b = '))

if a > b:
    a = a + b
    b = a - b
    a = a - b
    print('a =',a,'b =', b)
else:
    print('a =',a,'b =', b)
    