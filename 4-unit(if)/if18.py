a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
while (a!=b and b!=c and a!=c) or (a==b==c):
    print("Entered invalid numbers! At least two numbers must be same. Please enter two same and one different numbers.")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
else:
    if b == c != a:
        print("Unequal number of index is 1")
    elif a == c != b:
        print("Unequal number of index is 2")
    elif a == b != c:
        print("Unequal number of index is 3")