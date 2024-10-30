digit = int(input("Koordinatalar tekisligi uchun istalgan butun son kiriting: "))

x = int(input("Koordinataning x o'qi uchun istalgan butun son kiriting: "))
y = int(input("Koordinataning y o'qi uchun istalgan butun son kiriting: "))

sum_digit = x+y

if sum_digit==0 and digit==0:
    print(0)

if digit==x:
    print(1)
elif digit==y:
    print(2)
elif (digit!=x and digit!=y) or sum_digit!=digit:
    print(3)
