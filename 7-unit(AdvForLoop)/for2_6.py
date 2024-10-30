n = int(input("N = "))

for i in range(2, n+1):
    s = 0
    for j in range(1, i+1):
        if i%j == 0:
            s += 1
            
            
    if s == 2:
        oxirgi = i

print("Oxirgi tub son:", oxirgi)