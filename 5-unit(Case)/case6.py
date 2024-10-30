distance_meter = int(input("Enter the distance in meter(m): "))

action = input("Choose the action; Decimetr(1), Kilometr(2), Meter(3), Milmeter(4), Cantimeter(5) -> ")

decimeter = distance_meter * 10
kilometer = distance_meter // 1000
meter = distance_meter
milemeter = distance_meter * 1000
cantimeter = distance_meter * 100

print("Unity is ", end="")

if action == "1":
    print(decimeter, "decimeter")
    print("All Unities:\n", decimeter, "decimeter, ", kilometer, "kilometer, ", meter, "meter, ", milemeter, "milemeter, ", cantimeter, "cantimeter",)
elif action == "2":
    print(kilometer, "kilometer")
    print("All Unities:\n", decimeter, "decimeter, ", kilometer, "kilometer, ", meter, "meter, ", milemeter, "milemeter, ", cantimeter, "cantimeter",)
elif action == "3":
    print(meter, "meter")
    print("All Unities:\n", decimeter, "decimeter, ", kilometer, "kilometer, ", meter, "meter, ", milemeter, "milemeter, ", cantimeter, "cantimeter",)
elif action == "4":
    print(milemeter, "milemeter")
    print("All Unities:\n", decimeter, "decimeter, ", kilometer, "kilometer, ", meter, "meter, ", milemeter, "milemeter, ", cantimeter, "cantimeter",)
elif action == "5":
    print(cantimeter, "cantimeter")
    print("All Unities:\n", decimeter, "decimeter, ", kilometer, "kilometer, ", meter, "meter, ", milemeter, "milemeter, ", cantimeter, "cantimeter",)
else:
    print("You did not enter from 1 to 5 number!")
    
