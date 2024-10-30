n = int(input("n sonini kiriting: "))

if n <= 0:
    print("n soni musbat bo'lishi kerak!")
else:
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1

    if n == 1:
        print(f"k = {k}")
    else:
        print("n soni 2ning darajasi emas!")