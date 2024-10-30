# Assuming you have three numbers a, b, and c
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

# Check if at least one pair is mutually exclusive
if (a != b) or (b != c) or (a != c):
    result = True
else:
    result = False

print(result)
