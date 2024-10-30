def sumRange(a,b):
    total_sum = 0
    if a<b:
        for i in range(a,b+1):
            total_sum += i 
        return total_sum
    elif a>b:
        return 0   

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

# a,b=sumRange(a,b)
# b,c=sumRange(b,c)

print(f"{a} va {b} sonlarining raqamlar yigindisi {sumRange(a,b)}")
print(f"{b} va {c} sonlarining raqamlar yigindisi {sumRange(b,c)}")


