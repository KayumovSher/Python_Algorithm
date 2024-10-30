n = int(input("Enter a three-digit number exp(123) -> "))
while n<100 or n>999:
    print("Entered invalid number. Numbers must be more less than 1000(N < 1000) or must be bigger than two-digit number (N > 99).") 
    n = int(input("Enter a three-digit number exp(123) -> "))
else:
    yuzlik = n//100
    onlik = n%100//10
    birlik = n%100%10

    change_onlik = birlik
    change_birlik = onlik

    onlik = change_onlik
    birlik = change_birlik

    yuzlik = str(yuzlik)
    onlik = str(onlik)
    birlik = str(birlik)

    print(yuzlik + onlik + birlik)
        