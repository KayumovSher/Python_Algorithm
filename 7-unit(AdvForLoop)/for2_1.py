# 1.  n natural soni berilgan. 1 dan n gacha bo’lgan sonlarning yig'indisini 
# hisoblovchi dastur tuzing. 
# Kiritish: 7
# 1 2 3 4 5 6 7
# Natural sonlarning yig'indisi: 28

n = int(input("n = "))
s = 0
for i in range(1, n+1):
    s += 1
    for j in range(1, i+1):
        print(s)