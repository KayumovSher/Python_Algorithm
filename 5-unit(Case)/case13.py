from math import sqrt

element = input("Tengyonli uchburchak elementlaridan birini miqdorini kiritish uchun tanlang:\n('1'-katet(a), '2'-gipotenuza(c), '3'-gipotenuzaga tushirilgan balandlik(h), '4'-yuzasi(s)) -> ")
num = int(input("Miqdorini kiriting -> "))

print("Kiritilgan miqdor: ", end="")

if element == '1':
    c = num*sqrt(2)
    h = c/2
    s = (c*h)/2
    print(f"Katet(a) = {num}, Gipotenuza(c) = {c}, Gipotenuzaga tushirilgan balandlik(h) = {h}, Yuzasi(S) = {s}")
elif element == '2':
    a = num/sqrt(2)
    h = num/2
    s = (num*h)/2
    print(f"Katet(a) = {a}, Gipotenuza(c) = {num}, Gipotenuzaga tushirilgan balandlik(h) = {h}, Yuzasi(S) = {s}")
elif element == '3':
    c = 2*num
    a = c/sqrt(2)
    s = (c*num)/2
    print(f"Katet(a) = {a}, Gipotenuza(c) = {c}, Gipotenuzaga tushirilgan balandlik(h) = {num}, Yuzasi(S) = {s}")
elif element == '4':
    a = sqrt(2*num)
    c = a*sqrt(2)
    h = c/2
    print(f"Katet(a) = {a}, Gipotenuza(c) = {c}, Gipotenuzaga tushirilgan balandlik(h) = {h}, Yuzasi(S) = {num}")