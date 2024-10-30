a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)