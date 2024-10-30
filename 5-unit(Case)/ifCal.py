num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
action = str(input("Choose action: Add(+), Sub(-), Mul(*), Div(/) -> "))


print("Result is ", end="")
if action == "+":
    print(num1 + num2)
elif action == "-":
    print(num1 - num2)
elif action == "*":
    print(num1 * num2)
else:
    print(num1 / num2)