n = int(input("Enter n = "))

number = 0
m = n
for i in range(n, 0, -1):
    number = m/i
    m -= 1
print(number)