num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

action = str(input("Choose action: Add(a), Sub(s), Mul(m), Div(d) -> "))

print("Result is ", end="")
if action == "a":
    print(num1 + num2)
elif action == "s":
    print(num1 - num2)
elif action == "m":
    print(num1 * num2)
else:
    print(num1 / num2)