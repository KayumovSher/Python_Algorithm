n = int(input("n = "))

for i in range(2, n+1):
    num = 0
    for j in range(1, i+1):
        if i%j == 0:
            num += 1
    if num == 2:
        oxirgi = i
        print(i)
        
print("The last prime number is ", oxirgi)