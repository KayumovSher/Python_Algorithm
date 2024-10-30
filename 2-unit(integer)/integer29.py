A = int(input("To'g'ri to'rtburchakning A tomonini kiriting: "))
B = int(input("To'g'ri to'rtburchakning B tomonini kiriting: ")) 

C = int(input("Tomonlari C bo'lgan kvadratga ixtiyoring qiymat kiriting: "))

S_AB = A*B 

S_C = C**2

capacity = S_AB // S_C 
residal_capasity = S_AB%S_C

print(f"\nKiritilgan to'g'ri to'rtburchakning tomonlari A = {A}, B = {B} va uning yuzasi S = {S_AB}.\nKiritilgan kvadratning qiymati C = {C} va uning yuzasi S_2 = {S_C}.\nKvadrat - To'g'ri to'rtburchakda {capacity} martta joylashadi va {residal_capasity} tasi joylashmaydi.")

