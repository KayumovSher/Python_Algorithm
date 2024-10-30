a = int(input('a = '))
b = int(input('b = '))

if a != b:
    if a > b:
        b = a
        print('a =', a, 'b =', b)
    elif a < b:
        a = b
        print('a =', a, 'b =', b)
elif a == b:
    a = 0
    b = 0
    print('a =', a, 'b =', b)