def Calc(A,B,Op):
    if Op == 1:
        return A+B
    elif Op == 2:
        return A-B
    elif Op == 3:
        return A*B
    elif Op == 4:
        return A/B
    
A = int(input("A = "))
B = int(input("B = "))
Op = int(input("Airfmetik amallardan birini tanlang:\n1 - '+', 2 - '-', 3 - '*', 4 - '/' |-> "))
if Op==1:
    arif = "+"
elif Op==2:
    arif = "-"
elif Op==3:
    arif = "*"
elif Op==4:
    arif = "/"
# A,B,Op=Calc(A,B,Op)

print(f"{A}{arif}{B}={Calc(A,B,Op)}")2