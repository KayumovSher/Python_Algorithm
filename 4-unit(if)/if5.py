n1 = int(input("1-son: "))
n2 = int(input("2-son: "))
n3 = int(input("3-son: "))


count = 0
counter_count = 0

if n1 > 0:
    count += 1
elif n1 < 0:
    counter_count += 1

if n2 > 0:
    count += 1
elif n2 < 0:
    counter_count += 1
    
if n3 > 0:
    count += 1
elif n3 < 0:
    counter_count += 1

print("Berilgan 3ta sonning {}tasi musbat va {}tasi manfiy".format(count, counter_count))
