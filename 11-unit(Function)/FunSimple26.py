# Define K element can divided to 5 or not
def IsPower(K):
    if K%5 == 0:
        return print(True)
    else:
        return print(False)
    
# Input elements
n1 = int(input("Enter 1st value: "))
while not n1 > 0:
    print("n1 must be bigger than 0. Please Enter valid number!")
    n1 = int(input("Enter 1st value: "))
n2 = int(input("Enter 2nd value: "))
while not n2 > 0:
    print("n2 must be bigger than 0. Please Enter valid number!")
    n2 = int(input("Enter 2nd value: "))
n3 = int(input("Enter 3rd value: "))
while not n3 > 0:
    print("n3 must be bigger than 0. Please Enter valid number!")
    n2 = int(input("Enter 3rd value: "))
n4 = int(input("Enter 4th value: "))
while not n4 > 0:
    print("n4 must be bigger than 0. Please Enter valid number!")
    n2 = int(input("Enter 4th value: "))
n5 = int(input("Enter 5th value: "))
while not n5 > 0:
    print("n5 must be bigger than 0. Please Enter valid number!")
    n2 = int(input("Enter 5th value: "))

# Calculate the elements
result1 = IsPower(n1)
result2 = IsPower(n2)
result3 = IsPower(n3)
result4 = IsPower(n4)
result5 = IsPower(n5)

# print(IsPower(n1))
# print(IsPower(n2))
# print(IsPower(n3))
# print(IsPower(n4))
# print(IsPower(n5))