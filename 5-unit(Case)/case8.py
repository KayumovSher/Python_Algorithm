d = int(input("Enter the date please: "))
m = int(input("Enter the month please: "))

if m == 4 or m == 6 or m == 9 or m == 11:
    if d <= 30:
        print(d, m, sep=".")
    elif d > 30:
        print("Invalid date please try again!")
elif m == 2:
    if d <= 28:
        print(d, m, sep=".")
    elif d > 28:
        print("Invalid date please try again!")
else:
    if d <= 31:
        print(d, m, sep=".")
    elif d > 31:
        print("Invalid date please try again!")
        
