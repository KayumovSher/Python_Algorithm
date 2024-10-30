import sys
n = int(input("Ixtiyoriy butun son kiriting -> "))

res=[int(x) for x in str(n)]

if n//1:
    print(n)

if n//10:
    sum_num=res[0]+res[1]
    print(sum_num)

if n//100:
    sum_num=res[0]+res[1]+res[2]
    print(sum_num)

if n//1000:
    sum_num=res[0]+res[1]+res[2]+res[3]
    print(sum_num)

if n//10000:
    sum_num=res[0]+res[1]+res[2]+res[3]+res[4]
    print(sum_num)
    
if n//100000:
    sum_num=res[0]+res[1]+res[2]+res[3]+res[4]+res[5]
    print(sum_num)
    