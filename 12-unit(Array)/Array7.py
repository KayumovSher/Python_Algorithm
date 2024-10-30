n = int(input("n = "))

a=[]

for i in range(n):
    i = int(input("a = "))
    a.append(i)
    
a.reverse()
print(a)
# print(a[::-1])