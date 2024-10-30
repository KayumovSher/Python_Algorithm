son = int(input('tort xonali son kiriting - '))

a = son // 1000
b = son % 1000 // 10 // 10
c = son % 1000 // 10 % 10
d = son % 1000 % 100 % 10
yigindi = a + b + c + d

print('1 =', a, '2 =', b, '3 =', c, '4 =', d, 'Raqamlar yigindisi =', yigindi)