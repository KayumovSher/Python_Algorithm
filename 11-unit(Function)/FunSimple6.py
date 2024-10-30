a = int(input("Raqamni kiriting: "))
b = int(input("Raqamni kiriting: "))
c = int(input("Raqamni kiriting: "))

def DigitCountSum(x):
    raqamlar_soni = 0
    yigindi = 0 
    while x > 0:
        raqam = x % 10  # Raqamni olish
        yigindi += raqam  # Raqamni yig'indiga qo'shish
        raqamlar_soni += 1  # Raqamlar sonini oshirish
        x //= 10  # Raqamni o'chirish
    return raqamlar_soni, yigindi

raqamlar_soni1, yigindi1 = DigitCountSum(a)
raqamlar_soni2, yigindi2 = DigitCountSum(b)
raqamlar_soni3, yigindi3 = DigitCountSum(c)

print(f"1;\nRaqam = {a}, Raqamlar soni = {raqamlar_soni1}, Raqamlar yig'indisi = {yigindi1}")
print(f"2;\nRaqam = {b}, Raqamlar soni = {raqamlar_soni2}, Raqamlar yig'indisi = {yigindi2}")
print(f"3;\nRaqam = {c}, Raqamlar soni = {raqamlar_soni3}, Raqamlar yig'indisi = {yigindi3}")