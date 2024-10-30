L_sm = int(input('L = (sm) -> '))

L_metr = L_sm // 100
qoldiq = L_sm % 100

print('Metr = {}m, Qoldiq = {}sm'.format(L_metr, qoldiq))