a = int(input('a = '))
b = int(input('b = '))

if a != b:
    result = a + b
    print('a =', result, 'b =', result)
elif a == b:
    a = 0
    b = 0
    print('a =',a,'b =', b)