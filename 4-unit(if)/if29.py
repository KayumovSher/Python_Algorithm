N = int(input("Enter any integer number -> "))

if N>0:
    if N%2==0:
        print(f"{N} is Positive even integer number.")
    elif N%3==0:
        print(f"{N} is Positive odd integer number.")
    else:
         print(f"{N} is Positive odd integer number.")
if N<0:    
    if N%2==0:
        print(f"{N} is Negative even integer number.")
    elif N%3==0:
        print(f"{N} is Negative odd integer number.")
    else:
        print(f"{N} is Negative odd integer number.")

elif N==0:
    print("Entered integer number is equal to (0)")