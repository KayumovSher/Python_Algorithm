n = int(input("Check the levels of 2 numbers up to N: "))

massiv = []

for i in range(n):
    power = 2**i
    massiv.append(power)
 
print(f"Given level is {n}. The 2 must be power from 1 to {n}. {massiv}")