n = int(input("N = "))

ss = 0

for i in range(-n, n+1):
    if i == 0:
        continue
    else:
        ss += 1/i
    
print(round(ss, 2))