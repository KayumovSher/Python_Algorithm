d = int(input("Enter the day: "))
m = int(input("Enter the month: "))

d += 1

if m == 4 or m == 6 or m == 9 or m == 11:
    if d > 30:
        d = 1
        m += 1
elif m == 2:
    if d > 28:
        d = 1
        m += 1
else:
    if d > 31 or m > 12:
        d = 1
        m = 1

print(d, m, sep=".")