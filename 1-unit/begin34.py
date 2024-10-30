shololad_kg = int(input('shokolad kg-'))
shololad_narx = int(input('shokolad narx-'))

konfet_kg = int(input('Konfet kg-'))
konfet_narx = int(input('Konfet narx-'))

birkg_shokolad = shololad_narx // shololad_kg
birkg_konfet = konfet_narx // konfet_kg 

if birkg_shokolad > birkg_konfet:
    x = birkg_shokolad - birkg_konfet
    print(x)
elif birkg_konfet > birkg_shokolad:
    y = birkg_konfet - birkg_shokolad
    print(y)