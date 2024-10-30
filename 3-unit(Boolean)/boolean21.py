num = int(input("Uch xonali son kiriting: "))

if 100 <= num <= 999:
    
    digits = [int(digit) for digit in str(num)]
    
    if digits[0] < digits[1] < digits[2]:
        print(True)
    else:
        print(False)
else:
    print("Uch xonali son kiriting." )