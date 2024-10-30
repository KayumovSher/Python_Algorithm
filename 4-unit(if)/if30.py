N = int(input("Enter any integer from 1 to 999 -> "))

if N >= 1 and N <= 9 :
    if N%2==0:
        print("Bir xonalik juft son")
        print("The number entered is an even number with one digit")
    elif N%3==0:
        print("Bir xonalik toq son")
        print("The number entered is an odd number with one digit")
    else:
        print("Bir xonalik toq son")
        print("The number entered is an odd number with one digit")
        
elif N <= 99 and N >= 10:
    if N%2==0:
        print("Ikki xonalik juft son")
        print("The number entered is an even number with two digit")
    elif N%3==0:
        print("Ikki xonalik toq son")
        print("The number entered is an odd number with two digit")
    else:
        print("Ikki xonalik toq son")
        print("The number entered is an odd number with two digit")
    
elif N <= 999 and N >= 100:
    if N%2==0:
        print("Uch xonalik juft son")
        print("The number entered is an even number with three digit")
        
    elif N%3==0:
        print("Uch xonalik toq son")
        print("The number entered is an odd number with three digit")
    else:
        print("Uch xonalik toq son")
        print("The number entered is an odd number with three digit")
        
else:
    while N > 999 or N < 1:
        print("According to the condition of the example, Given number must be from 1 to 999 (1<N<999).\nPlease try again!")
        N = int(input("Enter any integer from 1 to 999 -> "))