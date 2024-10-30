n1 = int(input('son1 = '))
n2 = int(input('son2 = '))
n3 = int(input('son3 = '))

count = 0

if n1 > 0:
    count += 1

if n2 > 0:
    count += 1

if n3 > 0:
    count += 1
    
print("Uchta sonning {}tasi musbat".format(count))