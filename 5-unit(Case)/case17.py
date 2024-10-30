N = int(input("10-40 orasida son kiriting:"))

on = N//10
bir=N%10

if on==1:
    print("o'n", end="")
if on==2:
    print("yigirma", end="")
if on==3:
    print("o'ttiz", end="")
if on==4:
    print("qirq", end="")
if bir==0:
    print(" ta", end="")
if bir==1:
    print(" bitta", end="")
if bir==2:
    print(" ikkita", end="")
if bir==3:
    print(" uchta", end="")
if bir==4:
    print(" to'rtta", end="")
if bir==5:
    print(" beshta", end="")
if bir==6:
    print(" oltita", end="")
if bir==7:
    print(" yettita", end="")
if bir==8:
    print(" sakkizta", end="")
if bir==9:
    print(" to'qqizta", end="")  
    
print(" masala")