kg_sweet = float(input("Price of a kg sweet $"))

for i in range(1, 11):
    print(f"{i/10}kg --> ${i/10*kg_sweet}")