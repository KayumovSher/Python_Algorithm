# Optimal Tub son


from math import *
#It is included to import all math methods to calculate the math calculation
n = int(input("n = "))
# It is input that asks from user what integer number do you want to input.
print(2, end=" ")
# The print is for first prime number to show you without calculation.
conclution = 0
# It is variable to sum the iteration of loop action.
for i in range(3, n+1, 2):
# It is for loop that includes into 'i' variable the calculation the task.
    s = 0
    for j in range(3,int(sqrt(i))+1, 2):
        conclution += 1   
        if i%j == 0:
            s += 1
            break
    if s == 0:
        print(i, end=" ")
print("\nSum of loop: ", conclution)