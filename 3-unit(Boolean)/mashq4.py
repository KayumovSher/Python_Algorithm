paralapiped_a = int(input("Parralapipedning a tomonini kiriting - "))
paralapiped_b = int(input("Parralapipedning b tomonini kiriting - "))
paralapiped_c = int(input("Parralapipedning c tomonini kiriting - "))
kubik = int(input("Kubik tomonini kiriting - "))

paralapiped_yuzi = 2*(paralapiped_a*paralapiped_b + paralapiped_b * paralapiped_c + paralapiped_a * paralapiped_c)
kubik_yuza = 6 * kubik**2

# sigim = paralapiped_a // kubik * paralapiped_b // kubik * paralapiped_c // kubik
sigim = paralapiped_yuzi //kubik_yuza

print(sigim)