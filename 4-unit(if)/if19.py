a = int(input("Enter any integer number -> "))
b = int(input("Enter any integer number -> "))
c = int(input("Enter any integer number -> "))
d = int(input("Enter any integer number -> "))

if b==c==d!=a:
    print("Unequal number of index is 1")
elif a==c==d!=b:
    print("Unequal number of index is 2")
elif a==b==d!=c:
    print("Unequal number of index is 3")
elif a==b==c!=d:
    print("Unequal number of index is 4")
else:
    while not b==c==d!=a or a==c==d!=b or a==b==d!=c or a==b==c!=d or a==b==c==d or a!=b!=c!=d:
        print("Entered invalid number! at least three numbers must be equal.")
        a = int(input("Enter any integer number -> "))
        b = int(input("Enter any integer number -> "))
        c = int(input("Enter any integer number -> "))
        d = int(input("Enter any integer number -> "))