n = int(input("N = "))

for a in range(2, n+1):

    num = 0

    for i in range(1, a+1):
        if a%i == 0:
            num += 1
            # print(num)
        # else:
        #     print("Tub son mavjud emas!")
    if num == 2:
        print("Tub son: ", a)
    
