num = int(input("Uch xonali butun son kiriting: "))

if  100 <= num <= 999:
    
    digits = [int(digit) for digit in str(num)]
    # print(digits)
    
    if digits[0] < digits[1] < digits[2]:
        print(True)
        
    elif digits[0] > digits[1] > digits[2]:
        print(True)
        
    else:
        print(False)
        
else:
    print("Siz uch xonali butun son kiritmadingiz.")