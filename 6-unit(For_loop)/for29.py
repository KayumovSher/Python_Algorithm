n = int(input("Butun son = "))
a = int(input("Sonlar o'qidagi A kesma: "))
b = int(input("Sonlar o'qidagi B kesma: "))


size = (b-a) / n

for i in range(n + 1):
    point =  + i * size
    
print("Point {}: {}".format(i, point))