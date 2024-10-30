ogirlik_kg = int(input("Enter the kilogram: "))

action = input("Choose one of these actions; kilogramm(1), milligramm(2), gramm(3), tons(4), centner(5) -> ")

kg = ogirlik_kg
mg = ogirlik_kg * 1000000
gr = ogirlik_kg * 1000
t = ogirlik_kg // 1000
cen = ogirlik_kg // 100


result = print("The result is ", end="")
if action == "1":
    print(result, kg, "kg")
    print("All units are {}kilogram, {}miligram, {}gramm, {}tonna, {}centner".format(kg, mg, gr, t, cen))
elif action == "2":
    print(result, mg, "mg")
    print("All units are {}kilogram, {}miligram, {}gramm, {}tonna, {}centner".format(kg, mg, gr, t, cen))
elif action == "3":
    print(result, gr, "gr")
    print("All units are {}kilogram, {}miligram, {}gramm, {}tonna, {}centner".format(kg, mg, gr, t, cen))
elif action == "4":
    print(result, t, "t")
    print("All units are {}kilogram, {}miligram, {}gramm, {}tonna, {}centner".format(kg, mg, gr, t, cen))
elif action == "5":
    print(result, cen, "cen")
    print("All units are {}kilogram, {}miligram, {}gramm, {}tonna, {}centner".format(kg, mg, gr, t, cen))
else:
    print("Please enter number from 1 to 5")