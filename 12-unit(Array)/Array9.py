n = int(input("n = "))
a = []
for i in range(n):
    a.append(int(input("a = ")))
    natija = (n % 2 == 0) * a
    a.reverse()
print(a)