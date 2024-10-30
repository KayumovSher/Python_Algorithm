oy_raqami = int(input("Please enter number from 1 to 12 -> "))

if 1 <= oy_raqami <= 12:
    if oy_raqami == 1:
        print("The first month is January Winter")
    elif oy_raqami == 2:
        print("The second month is Febuary Winter")
    elif oy_raqami == 3:
        print("The third month is March Spring")
    elif oy_raqami == 4:
        print("The fourth month is April Spring")
    elif oy_raqami == 5:
        print("The fifth month is May Spring")
    elif oy_raqami == 6:
        print("The sixth month is June Summer")
    elif oy_raqami == 7:
        print("The seventh month is July Summer")
    elif oy_raqami == 8:
        print("The eighth month is August Summer")
    elif oy_raqami == 9:
        print("The nineth month is September Autumn")
    elif oy_raqami == 10:
        print("The tenth month is October Autumn")
    elif oy_raqami == 11:
        print("The eleventh month is November Autumn")
    elif oy_raqami == 12:
        print("The twelfth month is December Winter")
else:
    print("You should enter number from 1 to 12")