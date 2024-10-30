a = int(input("Enter A = "))
b = int(input("Enter B = "))

if a < b:
    for i in range(a, b+1):
        for j in range(i-a+1):
            print(i, end=' ')
else:
    print("B value should be bigger than A value. A < B")