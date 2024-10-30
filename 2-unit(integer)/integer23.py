vaqt = int(input("Kun boshidan boshlab N sekund vaqt o'tdi N = "))

soat = vaqt // 3600
daqiqa = vaqt // 60 % 60
sekund = vaqt % 60

print("Kun boshidan boshlab {} soat, {} daqiqa va {} soniya vaqt o'tdi.".format(soat,daqiqa,sekund))